# Michael — Data Access Kit

Created 2026-09-23. Goal: Michael's Claude pulls the same live data David's does, with zero OAuth setup on his side.

## What the kit gives him (user scope, works in every vault he opens)

| Server | Data | Auth it carries |
|---|---|---|
| facebook | Meta paid ads: campaigns, insights, pixel stats for act_87863118 | David's FB access token (see swap note below) |
| meta-organic | IG + FB page organic: posts, reach, comments | same token + per-brand IG tokens |
| google | GA4 + GSC for all 11 properties incl. NPB 322288940 | service-account key file (no OAuth, cleanest) |
| google-ads | Google Ads read + write across the account map | google-ads.yaml |
| clarity | Microsoft Clarity sessions | project ids only |

Not included on purpose: gbp and google-personal (they run on David's personal Google OAuth token, which is also his Gmail/Drive), gmail-*, youtube-*, slack, twilio, imessage.

## How it moves (no secret in chat or in a synced vault)

Status 2026-09-23: Claude was blocked from writing the pack/install scripts (they bundle David's tokens for another person, which the permission layer treats as exfiltration). David decides the transfer path:

- **Option A, scoped creds (recommended):** David hands Michael (1) the Google service-account key file `~/.claude/mcp-servers/google/keys/gravity-trails-mcp.json`, (2) `~/.config/google/google-ads.yaml`, and (3) a Meta System User token made in Business Settings with ads_read, read_insights, pages_read_engagement, instagram_basic, instagram_manage_insights. Plus the server code folders (facebook, google, google-ads, meta-organic, clarity from `~/.claude/mcp-servers/`, minus node_modules). AirDrop or a password zip; password by text.
- **Option B, fast:** same files, but reuse David's existing FB_ACCESS_TOKEN from `~/.claude.json` instead of making a System User. Michael's pulls then look like David on Meta. Swap later.
- Michael registers each with `claude mcp add --scope user <name> -e KEY=VALUE -- node ~/.claude/mcp-servers/<name>/index.js`. The env var names each server needs: facebook FB_ACCESS_TOKEN + FB_BM_MAP; google GOOGLE_KEY_FILE + GOOGLE_PROPERTIES; google-ads GOOGLE_ADS_CREDENTIALS + GOOGLE_ADS_ACCOUNTS; meta-organic FB_ACCESS_TOKEN (+ per-brand IG_TOKEN_*); clarity CLARITY_PROJECT_ID + CLARITY_PROJECTS. GOOGLE_PROPERTIES, FB_BM_MAP and GOOGLE_ADS_ACCOUNTS are non-secret JSON maps and can be copied out of David's `~/.claude.json` as-is.
- Michael also needs node on his PATH and `ln -s $(which node) ~/.local/bin/node` so his Claude stops rewriting the shared `.mcp.json`.

## Two follow-ups

- **GSC for NPB.** The service account can read GA4 for NPB already. For Search Console, add the service-account email as a user on the `sc-domain:nolapartybarges.com` property (GSC > Settings > Users, one minute) and change the npb gsc entry in GOOGLE_PROPERTIES to `sc-domain:nolapartybarges.com`. Until then NPB GSC needs David's personal token.
- **Meta token swap.** The FB token in the kit is David's user token, so Michael's pulls look like David. When there's a quiet hour, make a System User in Business Settings (2FA step-up, see Chrome bridge note) with ads_read, read_insights, pages_read_engagement, instagram_basic, instagram_manage_insights, and hand Michael that token instead. Revocable without touching David's login.

## Vault .mcp.json rule (root cause of the 9/4 breakage)

Michael's Claude rewrote the shared NPB `.mcp.json` with `/Users/michaelfischer/.local/bin/node` because bare `node` wasn't on his PATH, which broke 5 servers on David's Macs. The installer symlinks node into his `~/.local/bin` so the paths resolve either way. Rule for both Claudes: commands in a synced `.mcp.json` stay as bare `node` / `npx` with `${HOME}` and `${VAR}` refs. Never an absolute `/Users/<name>` path, never a literal secret.
