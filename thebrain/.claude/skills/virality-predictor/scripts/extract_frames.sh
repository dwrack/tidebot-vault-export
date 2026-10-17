#!/usr/bin/env bash
# Break a short-form video into frames for virality scoring.
# Usage: extract_frames.sh <video> [out_dir]
set -euo pipefail

video="${1:?usage: extract_frames.sh <video> [out_dir]}"
out="${2:-./virality_frames}"
mkdir -p "$out"

command -v ffmpeg >/dev/null || { echo "ffmpeg not installed" >&2; exit 1; }

dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$video")
read -r w h fps < <(ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate -of csv=p=0:s=x "$video" | tr x ' ')
fps=$(awk -v f="$fps" 'BEGIN { split(f, a, "/"); printf "%.1f", (a[2] ? a[1]/a[2] : a[1]) }')
aspect=$(awk -v w="$w" -v h="$h" 'BEGIN {
  r = w / h
  if (r < 0.6) print "9:16 vertical"; else if (r < 0.9) print "4:5 portrait";
  else if (r < 1.1) print "1:1 square"; else print "16:9 horizontal" }')

has_audio=no
if [ -n "$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$video")" ]; then
  has_audio=yes
  loud=$(ffmpeg -hide_banner -nostats -i "$video" -af volumedetect -vn -f null - 2>&1 \
    | awk -F': ' '/mean_volume/ { m=$2 } /max_volume/ { x=$2 } END { print "mean " m ", max " x }')
fi

printf 'duration: %.1fs\nresolution: %sx%s (%s)\nfps: %s\naudio: %s%s\n' \
  "$dur" "$w" "$h" "$aspect" "$fps" "$has_audio" "${loud:+ ($loud)}"

grab() { ffmpeg -hide_banner -loglevel error -y -ss "$1" -i "$video" -frames:v 1 -vf "scale=-2:720" "$2"; }

# Hook window: the first 3 seconds, densely
for t in 0.0 0.5 1.0 1.5 2.0 3.0; do
  awk -v t="$t" -v d="$dur" 'BEGIN { exit !(t < d) }' && grab "$t" "$out/hook_${t}s.jpg"
done

# Body: one frame every ~2s after the hook
t=4
while awk -v t="$t" -v d="$dur" 'BEGIN { exit !(t < d - 0.5) }'; do
  grab "$t" "$out/t_$(printf '%02d' "$t")s.jpg"
  t=$((t + 2))
done

# Last frame, for loop check against hook_0.0s.jpg
grab "$(awk -v d="$dur" 'BEGIN { printf "%.2f", (d > 0.15 ? d - 0.1 : 0) }')" "$out/last.jpg"

# Contact sheet of ~12 evenly spaced frames
ffmpeg -hide_banner -loglevel error -y -i "$video" \
  -vf "fps=12/${dur},scale=-2:360,tile=6x2" -frames:v 1 "$out/sheet.jpg" || true

echo "frames: $out"
ls "$out"
