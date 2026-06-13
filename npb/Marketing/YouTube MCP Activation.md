# YouTube MCP - Activation
*Built 2026-06-13. Lets Claude manage the channel directly: upload videos, set titles/descriptions/tags, unlist old videos, build playlists, push the banner, pull analytics.*

## What it can and can't do

**Can (via YouTube Data + Analytics API):** channel title + description + keywords, banner image, video upload, all video metadata, privacy (unlist the old pedal videos), playlists, custom thumbnails, caption uploads, analytics.

**Can't (Google API limitation, manual in Studio):** the **@handle** and the **profile avatar**. Two 60-second manual changes, nothing else.

## Setup (one time)

Reuses your existing shared OAuth client (`~/.config/google/oauth-client.json`, project `dwrack81-gmail-mcp`). No new Cloud project.

**Step 1 - turn on the APIs** (your account, project dwrack81-gmail-mcp). Open both, click Enable:
- YouTube Data API v3: https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=dwrack81-gmail-mcp
- YouTube Analytics API: https://console.cloud.google.com/apis/library/youtubeanalytics.googleapis.com?project=dwrack81-gmail-mcp

**Step 2 - authorize.** Double-click `YouTube Channel Auth.command` on your Desktop. Browser opens, sign in as **nolapedalbarge@gmail.com** (the channel owner), approve. If it warns the app isn't verified, Advanced > Continue (it's your own app). Token saves to `~/.config/google/tokens/nolapedalbarge-youtube.json`.

**Step 3 - tell Claude "auth done."** Claude runs `youtube_get_channel` to confirm, then executes the whole rebrand + uploads the 4 launch Shorts from `~/Projects/npb-youtube/pipeline/output/`.

## After it works

The same MCP works for the weekly cadence: Claude uploads each batch as `private`, you eyeball them in Studio, flip to public (or Claude schedules them with `publishAt`). The avatar + handle stay the only manual touches, and only once.

## Server details
- Code: `~/.claude/mcp-servers/youtube/index.js`
- Registered: user scope, env `YOUTUBE_TOKEN_FILE` → the token above
- Tools: youtube_get_channel, youtube_list_my_videos, youtube_update_branding, youtube_set_banner, youtube_upload_video, youtube_update_video, youtube_set_thumbnail, youtube_create_playlist, youtube_add_to_playlist, youtube_upload_caption, youtube_analytics
