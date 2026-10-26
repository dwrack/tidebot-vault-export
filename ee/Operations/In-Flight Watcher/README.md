# In-Flight Watcher

Keeps the shared E&E in-flight list (Drive "E&E Data Exchange" / ee-in-flight) current from Davey's texts, sauna@ + davey@ email and team Slack. Decision record: `TheBrain/07 Reference/Decisions/2026-10-22 E&E in-flight watcher.md`.

| Piece | Where | Schedule |
|---|---|---|
| `watch.py`, `run.sh`, `config.json` | mbp-2 `~/ee-inflight-watch/` (launchd `com.ebbember.inflight-watch`, via `ssh localhost` for chat.db access) | 7:10am to 9:10pm PT, every 2h; digest at the first run after 9am |
| `dash.py` | laptop `~/.config/ee-inflight-dash/` (launchd `com.ebbember.inflight-dash`) | every 3h and on wake, only when the CSV changed |

This folder is the canonical copy. Deploy: `scp watch.py run.sh davidrack@100.113.229.1:ee-inflight-watch/` (config.json lives on mbp-2; `config.example.json` here mirrors it).

- Writes only `incoming/ee-in-flight__davey__YYYY-MM-DD.csv`. Never the master, never REVIEW.md. Jonah's Daily Sweep merges.
- Dry run: `"dry_run": true` in mbp-2 `config.json` pauses it. LIVE since 2026-10-22 12:15 (dry_run false).
- Health: `~/ee-inflight-watch/heartbeat.json` and `watch.log` (newest chat.db time is logged each run). Two failed runs in a row DM Davey once a day (live mode only).
- iMessage: only chats with the people in `config.json` `people`, plus messages that mention sauna/ebb/ember/periode/plunge.
- Slack: bot is in all listed channels incl. #pricing-revamp and #founders. #holman-dock and #slip-7 are excluded on purpose.
