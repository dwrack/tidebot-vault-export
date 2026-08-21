# Slack App Scope Setup — Ebb & Ember / Elevated Tides workspace

App: A0BQ221MDKN  ·  Workspace: T0B0XUPSDHD
Where: api.slack.com/apps → pick the app → OAuth & Permissions → Scopes

Decision made 2026-08-21: full bot token, plus a user token limited to search only.

## Bot Token Scopes (xoxb)

Paste these in under "Bot Token Scopes."

### Already needed for what works today
- channels:read
- channels:history
- users:read
- users.profile:read
- chat:write
- reactions:write

### Reading more of the workspace
- groups:read            private channels the bot is in
- groups:history
- im:read                DMs with the bot
- im:history
- mpim:read              group DMs
- mpim:history
- users:read.email
- team:read
- emoji:read
- reactions:read

### Canvases  ← the thing that was blocking us
- canvases:read
- canvases:write

### Files
- files:read
- files:write

### Pins and bookmarks  ← lets me pin a post instead of asking you to
- pins:read
- pins:write
- bookmarks:read
- bookmarks:write

### Channel management
- channels:manage        create / rename / set topic + purpose
- channels:join          bot can join a public channel on its own
- groups:write
- im:write
- mpim:write

### Nice to have
- links:read
- metadata.message:read

## User Token Scopes (xoxp)

This token acts as Davey. Two scopes, both deliberate.

- search:read     search across channels and DMs (bot tokens cannot search at all)
- chat:write      post as Davey, for messages he wants coming from him personally

Nothing else. Do not add file, channel-management, or admin scopes here. The bot
token covers all of that, and anything the bot does is clearly attributable to
the app rather than to Davey.

### How posting identity works

The `slack_post_message_advanced` tool takes a `post_as` parameter:

- `post_as: "claude"` (default) posts as the app. Obviously automated.
- `post_as: "me"` posts as Davey via the user token. Indistinguishable from him
  typing it, so it is used only when he asks for that specific message to come
  from him.

Worth knowing: a Slack message can only be edited by whoever posted it. There is
no scope that makes a posted message editable by other people. When something
needs to be team-editable, it goes in a canvas, not a message.

## After changing scopes

1. Scroll up on the OAuth & Permissions page and hit "Reinstall to Workspace."
2. Approve the new permissions.
3. Copy BOTH tokens from that page:
   - Bot User OAuth Token, starts with xoxb-
   - User OAuth Token, starts with xoxp-
4. Run the setup script on the Desktop ("Slack Tokens Setup.command"). It
   prompts for both with hidden input and writes them into the local MCP
   registration. Neither token is ever typed into a chat or written into the
   vault.
5. Restart Claude Code so the MCP server reloads.

## Note on reinstalling

Reinstalling regenerates the bot token, so the old one stops working the moment
you reinstall. Anything else using that token will break until it gets the new
value. As far as I know nothing else uses it, but worth a beat of thought before
you click.
