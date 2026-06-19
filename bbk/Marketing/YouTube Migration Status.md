# Buffalo Bayou Kayak — Instagram to YouTube Migration

Pulling every @buffalobayoukayak video reel over to YouTube as Shorts, with content-themed clickable titles, Houston/kayak SEO descriptions + tags, and big-font hook thumbnails. Modeled on the NOLA Party Barge pipeline, improved (NPB used one content-blind title pool; BBK themes each title to the actual clip).

## Status (as of 2026-06-19)

- **101 videos** pulled from Instagram (April 2023 → June 2026), downloaded locally. None failed.
- **101 titles + descriptions + tags** generated, themed by content (bat tour, sunset/date, wildlife, beginner, skyline, regatta, cleanup, special event, general). All titles unique.
- **101 hook thumbnails** rendered: big white Impact hook, gold underline, bayou-green "BUFFALO BAYOU KAYAK" bar.
- **Uploader staged**, quota-aware, sets the custom thumbnail on each video.

### Blocked on one thing: the YouTube channel

No Buffalo Bayou Kayak YouTube channel is connected yet. The channel lives under the BBK Google account, **lonestarkayaktours@gmail.com** (same account as BBK's Gmail, Google Business Profile, and Analytics).

Two Desktop scripts handle it (the BBK Google login never touches the chat):
1. **`1. Check Buffalo Bayou Kayak YouTube.command`** — opens the channel switcher so we confirm whether a BBK channel already exists or needs creating.
2. **`2. Buffalo Bayou Kayak YouTube Auth.command`** — authorizes the channel, saves the token.

Once authorized, register the MCP and drip-upload.

## Heads-up: TikTok watermarks

Some of the reels were reposted from TikTok and carry the TikTok watermark + handle baked into the frame. YouTube quietly suppresses recycled watermarked clips. We're uploading them anyway (you asked for all), just know the watermarked ones may underperform vs. the clean IG-native ones.

## Quota reality

The YouTube API allows roughly **6 uploads per day** on the default quota. 101 videos = about **17 days** of dripping at 6/day, or we request a quota bump. The uploader is built to run daily and resume until done.

## Files

- Working dir: `~/bbk-yt-migration/` (videos, thumbs, upload_queue.json, manifest.json)
- Pipeline scripts: `~/.claude/mcp-servers/youtube/_bbk_*.mjs` + `_bbk_thumbs.py`
  - `_bbk_inventory.mjs` — pull IG video list (Graph API)
  - `_bbk_download.mjs` — download MP4s
  - `_bbk_gen_metadata.mjs` — themed titles + SEO descriptions + tags + hooks
  - `_bbk_thumbs.py` — big-font hook thumbnails
  - `_bbk_upload.mjs` — quota-aware drip uploader + thumbnail setter

## Next after auth

1. Register `youtube-bbk` MCP (token + expected channel id).
2. Set channel About + keywords, create theme playlists (Bat Tours, Sunset & Date Night, Wildlife, Beginner, Cleanups).
3. Run the uploader daily until all 101 are live.
