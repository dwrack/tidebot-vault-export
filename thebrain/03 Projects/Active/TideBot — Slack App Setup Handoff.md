# TideBot — Slack App Setup Handoff

Use Playwright to finish setting up the TideBot Slack app. The workspace "Davey Jones' Locker" already exists. The bot code is built at `~/Projects/tidebot/`. This doc has everything needed to create the app, get tokens, and go live.

---

## What's Done

- Bot code at `~/Projects/tidebot/` (renamed from wavey-davey)
- Multi-vault reader indexes 114 docs across 10 Obsidian vaults
- Scope-based access control (managers only see their business's docs)
- Vault search, Claude Q&A, gap logging, helm approval reactions
- Slash commands: `/tidebot-stats`, `/tidebot-gaps`, `/tidebot-reload`
- Setup scripts ready: `scripts/generate-manifest.js`, `scripts/setup-slack.js`
- `@slack/web-api` installed

## What's NOT Done

- Slack app not created yet (no tokens)
- `.env` file doesn't exist yet (setup script generates it)
- User IDs not mapped in `config/scopes.js`
- Channels not created yet (setup script does this)

---

## Step 1: Create Slack App with Playwright

Navigate to: https://api.slack.com/apps

1. Click "Create New App"
2. Select "From an app manifest"
3. Select workspace "Davey Jones' Locker"
4. Switch to JSON tab
5. Paste this manifest:

```json
{
  "display_information": {
    "name": "TideBot",
    "description": "Vault-powered Q&A and ops bot for Davey Jones' Locker",
    "background_color": "#1a5276"
  },
  "features": {
    "bot_user": {
      "display_name": "TideBot",
      "always_online": true
    },
    "slash_commands": [
      {
        "command": "/tidebot-stats",
        "description": "Show TideBot stats (questions, gaps, pending items)"
      },
      {
        "command": "/tidebot-gaps",
        "description": "Show open knowledge gaps"
      },
      {
        "command": "/tidebot-reload",
        "description": "Force reload vault documents"
      },
      {
        "command": "/tidebot-connect",
        "description": "Create a monitored group DM between team members"
      },
      {
        "command": "/tidebot-disconnect",
        "description": "Stop monitoring this conversation"
      },
      {
        "command": "/tidebot-digest",
        "description": "Get a summary of all monitored conversations"
      }
    ]
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "chat:write",
        "channels:read",
        "channels:history",
        "channels:manage",
        "channels:join",
        "groups:read",
        "groups:history",
        "reactions:read",
        "users:read",
        "im:read",
        "im:write",
        "im:history",
        "mpim:read",
        "mpim:write",
        "mpim:history",
        "users:read.email",
        "app_mentions:read",
        "commands"
      ]
    }
  },
  "settings": {
    "event_subscriptions": {
      "bot_events": [
        "message.im",
        "message.channels",
        "message.mpim",
        "app_mention",
        "reaction_added",
        "member_joined_channel",
        "team_join"
      ]
    },
    "interactivity": {
      "is_enabled": true
    },
    "org_deploy_enabled": false,
    "socket_mode_enabled": true,
    "token_rotation_enabled": false
  }
}
```

6. Click "Next", review, click "Create"

## Step 2: Generate App-Level Token

After the app is created, you'll land on the app's "Basic Information" page.

1. Scroll down to "App-Level Tokens"
2. Click "Generate Token and Scopes"
3. Token Name: `tidebot-socket`
4. Add scope: `connections:write`
5. Click "Generate"
6. Copy the token (starts with `xapp-`). Save it.

## Step 3: Install App to Workspace

1. In the left sidebar, click "Install App"
2. Click "Install to Workspace"
3. Click "Allow" on the OAuth page
4. Copy the "Bot User OAuth Token" (starts with `xoxb-`). Save it.

## Step 4: Run the Setup Script

In terminal, run:

```bash
cd ~/Projects/tidebot
node scripts/setup-slack.js <xoxb-token> <xapp-token>
```

Replace `<xoxb-token>` and `<xapp-token>` with the actual tokens from steps 2 and 3.

This script will:
- Create 6 channels: #the-helm, #managers, #nola, #doorcounty, #texas, #portland
- Set channel topics and purposes
- Join TideBot to all channels
- List workspace members with their Slack user IDs
- Generate the `.env` file with all tokens and the helm channel ID

## Step 5: Map User IDs

The setup script prints workspace members like:
```
U0123ABCDEF: David Rack (dwrack81@gmail.com)
U0456GHIJKL: Michael Fischer (...)
```

Open `~/Projects/tidebot/config/scopes.js` and uncomment/fill in the USER_SCOPES entries with real Slack user IDs:

```js
const USER_SCOPES = {
  'U_DAVID_ID': { name: 'David', scopes: ['all'] },
  'U_MICHAEL_ID': { name: 'Michael', scopes: ['nkst', 'npb', 'akt', 'lskt', 'hpb', 'bbk'] },
  'U_DYLAN_ID': { name: 'Dylan', scopes: ['nkst'] },
  'U_MICHELLE_ID': { name: 'Michelle', scopes: ['nkst'] },
  'U_JEFFREY_ID': { name: 'Jeffrey', scopes: ['npb'] },
  'U_JT_ID': { name: 'JT', scopes: ['npb'] },
  'U_BELLA_ID': { name: 'Bella', scopes: ['dckt'] },
  'U_CONNOR_ID': { name: 'Connor', scopes: ['akt', 'lskt', 'hpb', 'bbk'] },
  'U_JONAH_ID': { name: 'Jonah', scopes: ['ee', 'et'] },
};
```

## Step 5b: Map Channel Managers

Still in `~/Projects/tidebot/config/scopes.js`, fill in `CHANNEL_MANAGERS` so TideBot auto-connects new team members with their manager via a monitored group DM:

```js
const CHANNEL_MANAGERS = {
  'nola':        ['U_DYLAN_ID', 'U_JEFFREY_ID'],  // Dylan manages NKST, Jeffrey manages NPB
  'doorcounty':  ['U_BELLA_ID'],
  'texas':       ['U_CONNOR_ID'],
  'portland':    ['U_JONAH_ID'],
};
```

Also add all manager IDs to `MANAGER_USER_IDS` so they don't get auto-connected to themselves:

```js
const MANAGER_USER_IDS = new Set([
  'U_DAVID_ID',
  'U_DYLAN_ID', 'U_JEFFREY_ID', 'U_BELLA_ID', 'U_CONNOR_ID', 'U_JONAH_ID',
  'U_MICHAEL_ID',
]);
```

## Step 6: Add Anthropic API Key

Edit `~/Projects/tidebot/.env` and replace `your-anthropic-api-key` with the real key.

The key is available in the default Playwright profile's saved passwords or at https://console.anthropic.com/settings/keys

## Step 7: Start TideBot

```bash
cd ~/Projects/tidebot
node index.js
```

Expected output:
```
TideBot is running.
Vault: 114 docs loaded from 10 vaults
Helm channel: C0XXXXXXX
```

## Step 8: Test

In Slack:
1. DM TideBot: "what's the pre-trip checklist for kayak tours?"
2. In #nola, just type "what are the NKST SOPs?" (no @tag needed, should only return NKST docs)
3. In #doorcounty, type "what are the SOPs?" (should only return DCKT docs)
4. Run `/tidebot-stats` to see stats
5. Run `/tidebot-reload` to force vault refresh
6. Invite a test user to #nola. They should get:
   - A DM walkthrough + quiz from TideBot
   - A monitored group DM with the #nola manager(s)
   - David gets notified in #the-helm
7. Run `/tidebot-connect @person1 @person2` to manually create a monitored conversation
8. Run `/tidebot-digest` to get a summary of all monitored conversations
9. Run `/tidebot-disconnect` inside a monitored group DM to stop monitoring

---

## Codebase Reference

```
~/Projects/tidebot/
  index.js              Main bot: message handler, scope resolution, helm reactions, monitoring
  lib/
    tidebot.js          Gemini API wrapper with TideBot personality + monitor + digest prompts
    vault.js            Multi-vault reader with scope-based filtering
    onboarding.js       Welcome walkthrough + quiz for new channel members
    db.js               SQLite: qa_log, helm_queue, knowledge_gaps tables
  config/
    vaults.js           Vault allowlist (which folders from which vaults are indexed)
    scopes.js           Channel/user to business scope mapping
  scripts/
    generate-manifest.js  Prints the app manifest JSON
    setup-slack.js        Creates channels, generates .env
    test-vault.js         CLI test for vault search with scope filtering
  data/                   SQLite DB created at runtime
  .env.example            Template for environment variables
```

## Access Control Summary

| Person | Sees Docs From |
|---|---|
| David | All vaults |
| Michael | NKST, NPB, Austin, Lone Star, Houston PB, Buffalo Bayou |
| Dylan, Michelle | NKST only |
| Jeffrey, JT | NPB only |
| Bella | DCKT only |
| Connor | Austin, Lone Star, Houston PB, Buffalo Bayou |
| Jonah | Ebb & Ember, Elevated Tides |

All managers also see TheBrain cross-business docs (marketing playbooks, guide bio template, interview questions).

Protected from all staff: Legal, HR, Contracts, Insurance, Financial Records, Manager Coaching, anything with "buyout", "compensation", "EIN", "tax", "password" in the filename.
