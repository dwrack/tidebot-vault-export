# IG → YouTube Shorts mirror — install brief

**Run this on the always-on Mac** (`David's MacBook Pro (2)`, user `davidrack`, Intel, macOS 12.7.6, Python 3.8.9). Everything below is deliberate — read the gotchas before improvising.

Ebb & Ember's Instagram reels stopped reaching YouTube after the one-time June 2026 migration finished and retired itself. This installs the ongoing mirror that should have existed since.

---

## What's in this folder

| File | Purpose |
|---|---|
| `mirror.py` | The mirror. Self-contained, no imports from the laptop |
| `mirrored.json` | 25 IG reels already on YouTube. **Seeds dedup — without it you re-upload 25 Shorts** |
| `skip.json` | 10 reels deliberately excluded (dead promos) |
| `TAYBasal.otf` | Brand display font for thumbnails |

## Gotchas (all learned the hard way)

1. **Nothing launchd-run may touch the iCloud vault.** launchd has no Full Disk Access to `Mobile Documents` and dies with `PermissionError`. That's why everything gets copied to `~/.config/ebb-youtube/` first. The old thumbnail job failed 77 times this way.
2. **`ig_id` in the old migration manifest is an IG *shortcode*** (`DWKlUtMAXCK`), not a Graph media id. They don't interoperate. State is keyed by shortcode.
3. **`yt-dlp` reports `duration: None` for Instagram** without a full download. Don't try to fingerprint reels by duration.
4. **YouTube caps custom thumbnails at ~10/day** (HTTP 429). Uploads themselves aren't capped. `MAX_PER_RUN = 4` keeps us under it.
5. **Disk on that box is 98% full** (~19GB free). `mirror.py` deletes each working file after upload. Don't remove that cleanup.
6. **Do not install Homebrew.** Standalone binaries only — the box has no package manager and this job doesn't justify adding one.

---

## 1. Install the toolchain

```bash
mkdir -p ~/bin ~/.config/ebb-youtube/thumbnails ~/.config/ebb-youtube/logs
cd ~/bin

# yt-dlp — standalone build, bundles its own Python.
# Do NOT `pip install yt-dlp`: this box is on Python 3.8 and modern yt-dlp needs 3.9+,
# so pip would silently give you an ancient version that fails on Instagram.
curl -fsSL -o yt-dlp https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos
chmod +x yt-dlp && ./yt-dlp --version

# ffmpeg — static Intel build, single binary
curl -fsSL -o ff.zip https://evermeet.cx/ffmpeg/getrelease/zip
unzip -oq ff.zip && rm -f ff.zip && chmod +x ffmpeg && ./ffmpeg -version | head -1

# Pillow for the thumbnail builder
/usr/bin/python3 -m pip install --user Pillow
/usr/bin/python3 -c "import PIL; print('PIL', PIL.__version__)"
```

## 2. Stage files out of iCloud

```bash
V="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Ebb and Ember/Operations/Tracking/ig-yt-mirror"
cp "$V/mirrored.json" "$V/skip.json" "$V/TAYBasal.otf" ~/.config/ebb-youtube/
mkdir -p ~/.claude/scripts/ebb-ig-yt
cp "$V/mirror.py" ~/.claude/scripts/ebb-ig-yt/mirror.py
chmod +x ~/.claude/scripts/ebb-ig-yt/mirror.py
```

Credentials are already on this box — do not copy or re-create them:
- `~/.config/google/tokens/ebbandember-youtube.json` (YouTube OAuth, channel-locked)
- `~/.claude/settings.json` → `env.META_IG_TOKEN` (Instagram Graph)

## 3. Dry run first

```bash
/usr/bin/python3 ~/.claude/scripts/ebb-ig-yt/mirror.py --dry-run --limit 50
```

Expect **36 reels** listed and **zero** uploads. Sanity checks:
- If it lists ~61, `mirrored.json` didn't get copied — stop and fix.
- If it lists 46, `skip.json` didn't get copied — stop and fix.
- Titles should read like real sentences, not hashtag soup.

## 4. Drain the backlog

The script is channel-locked: it aborts if the token doesn't control `UCbzG-G9b9s9Uz49QZuGqOeQ`.

```bash
/usr/bin/python3 ~/.claude/scripts/ebb-ig-yt/mirror.py --limit 8
```

These are **public** uploads to the live Ebb & Ember channel. Run one batch, eyeball the result on YouTube, then continue. Thumbnails will start 429-ing after ~10/day; that's expected and harmless — the video still uploads and the thumbnail is stashed in `~/.config/ebb-youtube/thumbnails/` for a later pass.

Repeat until `Run end. ... 0 still pending.`

## 5. Schedule it

`~/Library/LaunchAgents/com.ebbember.igyt-mirror.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.ebbember.igyt-mirror</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/davidrack/.claude/scripts/ebb-ig-yt/mirror.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key><integer>10</integer>
        <key>Minute</key><integer>30</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/davidrack/.config/ebb-youtube/logs/launchd.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/davidrack/.config/ebb-youtube/logs/launchd.log</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

```bash
launchctl unload ~/Library/LaunchAgents/com.ebbember.igyt-mirror.plist 2>/dev/null
launchctl load ~/Library/LaunchAgents/com.ebbember.igyt-mirror.plist
launchctl list | grep igyt-mirror
```

## 6. Report back

- How many uploaded, how many failed, and the tail of `~/.config/ebb-youtube/logs/mirror.log`
- Confirm `launchctl list` shows the job
- Anything that looked wrong (bad titles, wrong channel, thumbnail failures beyond the daily cap)

Do **not** change the skip list, the channel id, or `privacyStatus` without checking with David first.
