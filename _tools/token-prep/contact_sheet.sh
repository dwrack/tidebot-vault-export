#!/bin/bash
# Turn N images (or one video) into ONE downscaled image for Claude to read.
#   contact_sheet.sh out.jpg img1.png img2.png ...   # tiles up to 6 images, 2 per row
#   contact_sheet.sh out.jpg video.mov               # 6 frames across the video
# Uses sips (built into macOS) for single-image downscaling; tiling and video frames
# need ffmpeg. If ffmpeg is missing the script says so and does NOT install it.
set -e
out="$1"; shift
[ -z "$out" ] || [ $# -eq 0 ] && { echo "usage: $0 out.jpg <images... | video>"; exit 1; }
if [ $# -eq 1 ] && [[ "$1" =~ \.(mov|mp4|m4v|MOV|MP4)$ ]]; then
  command -v ffmpeg >/dev/null || { echo "ffmpeg not found; install with: brew install ffmpeg"; exit 2; }
  ffmpeg -v error -y -i "$1" -vf "fps=6/$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1" | cut -d. -f1),scale=640:-1,tile=3x2" -frames:v 1 -q:v 4 "$out"
elif [ $# -eq 1 ]; then
  sips -Z 1200 "$1" --out "$out" >/dev/null   # one image: just downscale (≈1,200 tokens instead of ≈1,600)
else
  command -v ffmpeg >/dev/null || { echo "ffmpeg not found for tiling; install with: brew install ffmpeg (or pass one image at a time to use sips)"; exit 2; }
  n=$#; [ $n -gt 6 ] && { echo "max 6 images per sheet"; exit 1; }
  cols=2; rows=$(( (n + cols - 1) / cols ))
  args=(); for f in "$@"; do args+=(-i "$f"); done
  filter=""; for i in $(seq 0 $((n-1))); do filter+="[$i:v]scale=800:600:force_original_aspect_ratio=decrease,pad=800:600:(ow-iw)/2:(oh-ih)/2:color=black[v$i];"; done
  for i in $(seq 0 $((n-1))); do filter+="[v$i]"; done
  filter+="xstack=inputs=$n:layout="
  for i in $(seq 0 $((n-1))); do x=$(( (i % cols) * 800 )); y=$(( (i / cols) * 600 )); filter+="${x}_${y}|"; done
  filter="${filter%|}"
  ffmpeg -v error -y "${args[@]}" -filter_complex "$filter" -frames:v 1 -q:v 4 "$out"
fi
echo "wrote $out ($(du -h "$out" | cut -f1))"
