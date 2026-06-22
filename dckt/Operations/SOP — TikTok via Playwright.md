# SOP — DCKT TikTok via Playwright

*How we run analysis and posting on @doorcountykayaktour through the Playwright browser, the same way we do it for Houston Pedal Barge. Last updated June 22, 2026.*

This is for whoever is driving Claude Code in the DCKT vault (David, Lea, Jessica). It assumes you're working inside the Door County Kayak Tours vault so the right browser profile is used.

---

## How the login works (read this once)

There is no API for posting to TikTok organically, so everything runs through a real browser that Claude controls (the Playwright MCP, already in this vault's `.mcp.json`). The key thing to understand:

- Playwright keeps a **separate, persistent Chrome profile for each vault**, stored under `~/Library/Caches/ms-playwright/`. Because the DCKT vault has its own profile, the TikTok login we did here is saved here and does not touch the Houston Pedal Barge login (or any other account). They can't collide.
- That means **we only log in once**. The session persists across days and sessions automatically. You do not re-enter the password each time.
- The account is **@doorcountykayaktour** (display name "doorcountykayaktours"). It already has analytics access (TikTok Studio works).

### Confirming the session is alive
Ask Claude to navigate to `https://www.tiktok.com/profile`. If it lands on the @doorcountykayaktour profile with no login wall, we're good. If it shows a "Log in" button, the session expired (happens every few weeks), go to re-login below.

### Re-login when the session drops
1. Have Claude open `https://www.tiktok.com/login` in the Playwright browser.
2. **You** type the DCKT TikTok credentials directly into that browser window. Never paste the password into the chat, it gets stored in the transcript. Type it into the browser only.
3. Once you see the DCKT feed/profile, tell Claude "logged in" and it continues. The session is saved again.

---

## Job 1: Analysis (pull the numbers)

Goal: refresh `Marketing/DCKT TikTok Analytics Readout.md`. Run this every 3 to 4 weeks during the season, or after any posting push.

Steps Claude runs in the browser:
1. Go to `https://www.tiktok.com/@doorcountykayaktour`, scroll the grid, and read every post's views + caption straight from the page (more accurate than screenshots).
2. Go to `https://www.tiktok.com/tiktokstudio/analytics`, set the range to **Last 365 days** (and check Last 7 days for the recent pulse).
3. Read the four tabs: Overview (views, traffic source, search queries), Viewers, Followers (gender/age/location), Content.
4. Cross-check the follower count against the live profile header before trusting the numbers (per the vault's reconcile-before-claiming rule).
5. Rewrite the readout. Watch the three numbers that matter for a waking-up account: **For You traffic % (was 0), 7-day views (was 23), and net followers (was flat)**.

Note: the analytics page animates a chart that makes full-page screenshots time out. Don't fight it, just read the data via the page text. Per-post viewer demographics stay hidden until a post clears 100 viewers.

---

## Job 2: Posting (native scheduler, reviewed batch)

We do NOT run an unattended auto-poster. TikTok has no upload API and flags headless posting, so a daily cron would silently break. Instead we batch-schedule through TikTok's own scheduler, with you reviewing each post before it goes live.

The plan lives in `Marketing/DCKT TikTok Queue.csv`. Columns:
`date, asset_path, onscreen_text, caption, hook, status, scheduled_for, posted_at, video_url`
- `asset_path` is the source Instagram reel to repurpose (these are our proven, finished vertical reels from `Marketing/IG Video Content Catalog.md`). Pull the clip, trim/re-export vertical if needed, strip the IG watermark.
- `onscreen_text` is the hook to burn into the first second of the video.
- `caption` is the TikTok caption (already in brand voice, soft CTA, hashtags).
- `hook` is the category tag for later analysis (sea-caves, question-hook, social-proof, booking-urgency, wildlife, weather-moment, local-knowledge, e-bike).

### The batch-schedule loop
1. Get the video files ready locally (downloaded/re-exported from the source reels). The raw source footage also lives in `Assets/DCKT/DCKT Videos/` if you want to cut something fresh.
2. Have Claude open `https://www.tiktok.com/tiktokstudio/upload`.
3. For each queued row whose `date` is within the next 10 days (TikTok only schedules ~10 days out):
   - Upload the video file.
   - Paste the `caption`.
   - Toggle **Schedule** on and set it to the row's `date` (default time: late afternoon/early evening Central for the Midwest audience until real data says otherwise).
   - Review it yourself, then confirm.
   - Update the CSV row: `status` -> scheduled, fill `scheduled_for`. Once it's live, fill `posted_at` and `video_url`.
4. Rows beyond 10 days stay `queued`. Run the loop again next week to schedule the next wave.

### Cadence
Default 4 posts/week (the queue runs Mon/Wed/Fri/Sat, weekend recaps on Monday). The Social Media Plan allows 3 to 5x/week. Consistency matters more than volume, the account's whole problem is that it goes dark for months.

---

## What we learned on the first pull (June 2026)

- Account was dark since Nov 30, 2025. Zero posts in 2026 peak season.
- 100% of traffic is Search, 0% For You. The algorithm isn't pushing anything. Only consistent posting changes that.
- The 489 followers are almost exactly the DCKT avatar (women 35-54, US). Warm audience, gone cold.
- Both all-time best posts paired Cave Point with a claim or question hook. That's the template. Generic "pretty water + song" posts sit at the bottom.

Full detail in `Marketing/DCKT TikTok Analytics Readout.md`.
