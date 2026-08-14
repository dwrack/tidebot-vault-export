---
name: ig-saved-export
description: Export your saved Instagram posts to a JSON file using Playwright. Use when the user wants to pull their Instagram "Saved" collection into the vault so it can be turned into content. The scraper must run on the user's own computer (Instagram blocks datacenter/cloud logins); this skill produces the script and walks them through running it, then hands the output to the ig-content-router skill.
---

# Instagram Saved Posts — Export

Pulls the user's **Saved** posts off Instagram and into a `saved_posts.json`
file the rest of the pipeline can read.

## Why this can't run in a Claude Code cloud session

Instagram is blocked by the cloud egress policy (the proxy returns 403), and a
personal-account login from a datacenter IP trips Instagram's "suspicious login"
checkpoint + 2FA. So the scrape runs on the **user's own machine**, where they're
already a normal logged-in user. The rest of the pipeline (routing posts into the
Content Engine) runs fine in any session.

## What to tell the user (run these on their computer)

```bash
# 1. one-time setup, in the folder containing export_saved.mjs
npm i playwright
npx playwright install chromium

# 2. run it (a real browser window opens — log in by hand the first time)
node export_saved.mjs YOUR_IG_USERNAME
```

A Chromium window opens. The user logs in manually (2FA included); the session is
cached in `./ig-user-data` so future runs skip login. The script scrolls the saved
grid, collects every post, visits each one, and writes `saved_posts.json` next to
the script — saving incrementally so a crash doesn't lose progress.

Useful flags:
- `--collection "Trip Ideas"` — scrape a single named saved collection instead of All Posts
- `--limit 200` — cap how many posts to pull
- `--out path.json` — choose the output location
- `--headless` — no visible window (only after login is cached once)

## Output shape

`saved_posts.json` is an array of:

```json
{
  "url": "https://www.instagram.com/reel/ABC123/",
  "shortcode": "ABC123",
  "type": "reel",
  "author": "somecreator",
  "caption": "…og:description text…",
  "thumbnail": "https://…jpg",
  "savedFrom": "All Posts",
  "scrapedAt": "2026-08-14T00:00:00.000Z"
}
```

Caption comes from the post's Open Graph description, which is truncated for long
captions — enough to categorize and adapt, not a full transcript. That's fine for
routing; the `url` is kept so the original is always one click away.

## Handing off

Once the user has `saved_posts.json`, tell them to drop it into the vault
(recommended: `thebrain/03 Projects/Active/Content Engine/saved_posts.json`), then
run the **`ig-content-router`** skill to turn each post into swipe-file entries and
per-business content ideas.

## Guardrails

- This scrapes only the user's OWN saved posts using their OWN login. Don't
  repurpose it to scrape other accounts at scale.
- If Instagram changes its DOM and the selectors stop matching, the script will
  report 0 posts — update the `a[href*="/p/"]` / `og:*` selectors in
  `export_saved.mjs`, don't add credential-harvesting or third-party API keys.
- Never commit `ig-user-data/` (the logged-in session) to git. It's already
  covered by this skill's `.gitignore`.
