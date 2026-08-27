# Claude Slack Bridge — Davey Jones Locker

Lets David and Michael Fischer tag **@Claude** in the Davey Jones Locker Slack workspace and get real answers from the DJL vaults and analytics (GA4, GSC, GBP, Google Ads, Meta paid + organic, Clarity, YouTube), plus make approved changes.

Everything is installed and waiting on davids-mbp-2 (`~/.config/djl-claude-slack/`). Two steps to go live:

## Step 1 — Create the Slack app (~3 min, David)

1. Go to https://api.slack.com/apps → **Create New App** → **From a manifest**
2. Pick the **Davey Jones Locker** workspace
3. Paste this manifest (JSON tab):

```json
{
  "display_information": {
    "name": "Claude",
    "description": "Analytics and vault assistant for Davey Jones Locker",
    "background_color": "#1a1a2e"
  },
  "features": {
    "bot_user": { "display_name": "Claude", "always_online": true }
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "channels:history", "channels:read", "groups:history",
        "groups:read", "users:read", "chat:write", "reactions:write"
      ]
    }
  },
  "settings": {
    "org_deploy_enabled": false,
    "socket_mode_enabled": false,
    "token_rotation_enabled": false
  }
}
```

4. **Install to Workspace** → approve
5. Copy the **Bot User OAuth Token** (starts `xoxb-`)

## Step 2 — Activate (double-click, David)

Run `Activate DJL Claude Slack Bridge.command` on the Desktop (if it won't open, run once in Terminal: `chmod +x ~/Desktop/Activate\ DJL\ Claude\ Slack\ Bridge.command`). Paste the token when asked. It installs the token on davids-mbp-2 over SSH — the token never appears on screen or in any file on this Mac — verifies it against Slack, and kicks the bridge.

## Step 3 — Wire the channel

- Create a private channel, e.g. **#ask-claude**, with David + Michael
- `/invite @Claude` there
- Tag `@Claude` with a question. It reacts 👀 and replies in the thread within ~3 minutes (launchd polls every 180s).

## What Michael can do

- Ask anything across DCKT, Gravity Trails, Lone Star, Cave Point Paddle and Pedal, Door County Detours: bookings docs, GA4/GSC/GBP/Clarity numbers, Google Ads + Meta performance, reviews, IG insights, YouTube stats
- Make changes: vault docs, Google Ads, Meta ads, GBP posts, review replies. Anything touching live spend or public content, Claude states the exact change and waits for a "confirm" reply in the thread first
- Hard-blocked regardless of who asks: sending email/SMS, publishing IG/FB organic posts, YouTube uploads, deleting GBP content, changing business NAP info, and any data from the non-DJL brands (NOLA, Houston, Ebb & Ember, etc.)

## Guardrails / plumbing

- Only David (U0ASH7AQ1LP) and Michael (U0ATYT71R25) get answers — mentions from the ~100 staff in the workspace are ignored silently. Edit `ALLOWED_USERS` in `~/.config/djl-claude-slack/watcher.py` on davids-mbp-2 to change that.
- Separate bot from TideBot on purpose: TideBot's DigitalOcean service answers every @tidebot mention, so reusing its token would double-reply.
- Sessions run headless (`claude -p`) in the DCKT vault with the other four DJL vaults added, `--strict-mcp-config` (only the 11 DJL servers in `mcp.json` load), permissions in `bridge-settings.json`.
- launchd job: `com.djl.claude-slack-bridge`, every 180s. Logs: `~/.config/djl-claude-slack/bridge.log`.
- Modeled on the Ebb & Ember bridge (`~/.config/ee-claude-slack/`), which stays read+draft-only and untouched.
