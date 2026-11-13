# Contractor Watch

**CURRENT STATUS (verified 2026-11-13 1:20 PM PT):** LIVE on davids-mbp-2, launchd `com.ebbember.contractor-watch`, every 2h at :25 from 7:25am to 9:25pm PT. First live run 11/13 covered the previous 10 days. Decision: Davey 11/13 ("get you access to watch for contractors communications and keeping them on point, on task and accountable").

Keeps every contractor on the V2 build (and the social sauna fixes) accountable without Davey re-reading threads. Reads Davey's iMessages (mbp-2 chat.db via `ssh localhost`), Slack #private-saunas-build / #maintenance / #founders, and sauna@ + davey@ email from the people in `contractors.json`. Claude (Sonnet) keeps a ledger per contractor: commitments and promised dates, money (quoted, approved, invoiced, paid), questions we asked them, questions they asked us.

| Piece | Where |
|---|---|
| `contractor_watch.py`, `run.sh`, `contractors.json`, `threads.py` | mbp-2 `~/ee-contractor-watch/` (this folder is the canonical copy; deploy with `scp <file> davidrack@100.113.229.1:ee-contractor-watch/`) |
| `config.json` | mbp-2 only (`config.example.json` here mirrors it). `dry_run: true` pauses writes. |
| `ledger.json`, `state.json`, `watch.log`, `heartbeat.json` | mbp-2 `~/ee-contractor-watch/` |
| `Contractor Status.md` | this folder, rewritten every run. The Slack @Claude bridge reads it to answer Jonah. |

## What it does each run
1. New messages since the last run go to Claude with the current ledger; Claude returns the updated ledger (stable ids, so a question is only flagged once).
2. Flags are computed in code, not by Claude: contractor silent on our question after 24h (**nudge**, with a draft text), promised date passed (**overdue**), contractor waiting on us after 24h (**you owe**), plus Claude's watch items (safety, permit, price change, scope change).
3. Outputs:
   - `Contractor Status.md` (full picture, every contractor).
   - One Slack DM to Davey with the new flags only, ranked (overdue, safety, you owe, nudge, permit, price, scope), max 12, each nudge with a ready-to-send draft. Same flag again only after 72h. Nothing is ever sent to a contractor.
   - "You owe" items go under `## Waiting on you` in TheBrain Command Center Notes, tagged `[cw:<key>]`; struck through when the ledger shows them answered.
   - Shared record: a row in `ee-in-flight/incoming/ee-in-flight__davey__<date>.csv` for each commitment whose status, next step or date changed (merged onto the in-flight watcher's file for the day; Jonah's sweep merges).
4. Failure: two failed runs in a row DM Davey once a day.

## Add or change a contractor
Edit `contractors.json` here (name, aliases, role, phone handles, emails, Slack names), then scp it to mbp-2. Roster-less people doing E&E work show up under "Not on the roster yet" in the status file.

## On demand
`python3 ~/ee-contractor-watch/threads.py sergey --days 14` prints a contractor's texts (read-only; reroutes through `ssh localhost` when the Messages database is blocked for the calling process). Rebuild the status file from the ledger without a scan: `contractor_watch.py --status-only`.

## Related
- In-flight watcher (readers reused): `Operations/In-Flight Watcher/README.md`
- Incident log: `Operations/Incident Log/README.md`. 11/13: its classifier no longer calls rust or maintenance on gas parts "fire/gas" (that needs a flame, smoke, smell, leak, CO or alarm) and ignores contractor scheduling chatter about logged items. INC-0004 reclassified to maintenance.
