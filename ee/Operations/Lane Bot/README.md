# E&E Lane Bot (Comms Lane Bots, phase 1)

**CURRENT STATUS (verified 2026-11-13 19:25 PT):** LIVE on davids-mbp-2. Collector every 3 min, Tier 0 rules filing sign / pay / approve asks to the Command Center within one cycle, 3B model in shadow, ledger + rollups live. Design: `TheBrain/03 Projects/Active/Comms Lane Bots — Design (Nov 13 2026).md`. Decision record: `TheBrain/07 Reference/Decisions/2026-11-13 Comms Lane Bots.md`.

## Why this exists
On 11/10 Jonah emailed davey@ a marina approval for signature and it reached nothing for three days. The old watcher only tracked work items and ran Sonnet over a 221-row list every 2 hours (~250k tokens a day). This lane reads the same sources every 3 minutes with zero tokens, files asks instantly, and keeps the model tiers narrow and grounded.

## What runs where (all on davids-mbp-2, `~/lanes/`)

| Piece | Path | launchd | Cadence | Does |
|---|---|---|---|---|
| Dashboard writer | `~/lanes/dashboard-writer/writer.py` | `com.djl.dashboard-writer` | every 2 min | The ONLY process that edits `Command Center Notes.md` under `## Waiting on you`. Applies `~/lanes/_queue/*.json` (add / strike by tag), atomic write, 12 adds per lane per day (extras held in `_queue/overflow/`). |
| E&E collector | `~/lanes/ee/collect.py` (+ `~/lanes/_lib/lanelib.py`) | `com.djl.lane-ee` (ssh localhost for chat.db Full Disk Access) | every 3 min | iMessage chat.db, davey@ + sauna@ Gmail (incl. Google Voice texts), slack-et 13 channels + DMs the bot is in. Normalizes (quotes, signatures, HTML, tracking links stripped; handles -> names; threads; brand tag), dedupes into `events.jsonl`, noise bucket (Periode notices, receipts, newsletters, missed-call mails). Then runs Tier 0. |
| Tier 0 rules | `~/lanes/ee/rules.py` | (called by collector) | each cycle | Asks of Davey from lane people, addressed to him; Davey's promises; dates; money; silence; auto-strike when Davey replies in the thread. Queue JSON carries the verbatim quote and tag `[bot:ee:0:<key>]`. |
| Tier 1 model | `~/lanes/ee/structure.py`, `~/lanes/_model/serve.sh` | `com.djl.lane-ee-structure` | every 20 min | Qwen2.5-3B-Instruct Q4_K_M via llama.cpp (built from source b12374; the prebuilt needs macOS 13). 2 threads, 127.0.0.1:8089, loaded per batch and killed after (idle unload), refuses to load under 3 GB free. Two narrow calls per unsettled event: yes/no/unsure (grammar), then schema JSON; code checks the quote span is verbatim. SHADOW: writes `preview/structure-*.jsonl` and `unsure.jsonl` only. |
| Ledger + rollups | `~/lanes/ee/ledger.py` -> `ledger.sqlite` | (called by rules) | each cycle | people, vendors, projects, money, promises, asks, dates. Code-only rollups to `Rollups.md` here. |
| Golden set + eval | `~/lanes/ee/golden.jsonl`, `eval.py` | `com.djl.lane-ee-eval` | Mondays 7:20 | Precision/recall for Tier 0 and Tier 1, weekly line in `Eval.md` here. |
| Heartbeats | `~/lanes/ee/heartbeat.json`, `structure_heartbeat.json`, `~/lanes/dashboard-writer/heartbeat.json` | in `loop_watchdog.py` EXTRA_HEARTBEATS | | Newest event timestamp per source, counts, errors, seconds, CPU. Collector exits 1 on any source failure; one Slack DM a day to Davey after 2 failed cycles. |
| Tier 2 / Tier 3 | `recheck.py`, `brief.py` | none | phase 2 | Stubs with the interface only. |

Old writers switched 2026-11-13: `~/ee-inflight-watch/watch.py` (`file_asks`, `file_commits`) and `~/ee-contractor-watch/contractor_watch.py` (`file_cc_notes`) now READ the dashboard for dedupe and drop ops into the queue; they no longer write the file (two writers raced over iCloud on 11/13 and lost 3 lines). Backups: `*.bak-20261113-queue`. The in-flight watcher otherwise runs unchanged (open decision 5).

## Tiers and what reaches the dashboard
- Tier 0 LIVE for kinds at or above 90% precision on the golden set: **sign, pay, approve**. `reply` (direct questions) is 81% and stays in shadow (`preview/rules-YYYY-MM-DD.jsonl`) until Davey's feedback lifts it. Config: `rules.live_kinds` in `~/lanes/ee/config.json`.
- Tier 1 shadow only. Promotion needs 90% precision for a week (design rule); demote under 80.
- No tier sends anything. No model writes prose for a human. Dollar amounts over the proposed $500 are marked "Tier 3 review" on the line and in the ledger.

## Numbers (2026-11-13 bootstrap, last 30 days)
- Events collected: 2543 (560 texts, 820 gmail of which 362 noise, 167 Google Voice texts, 996 Slack).
- Golden set: 1093 events, 200 labelled asks (3 hand-labelled known misses: marina approval email 11/10, slip 9 DocuSign text 11/2, Ohana check ask 11/13; the rest provisional labels from one Sonnet pass, to be corrected by Davey's feedback).
- Tier 0: precision 83.8%, recall 46.5% overall. Per kind: sign 92% (12/13), pay 100% (3/3), approve 100% (6/6), reply 81% (72/89). All 3 known misses caught. Recall is capped by design: Tier 0 only fires for listed people, the rest is Tier 1's job.
- Tier 1 (sample of 120 golden events, running in the background at write time): see `Eval.md` for the first line once `structure.py --golden` finishes.
- Machine cost: collector 0.7 CPU-s per cycle (about 5 CPU-min a day), 17 to 25 s wall. Model: loads in 4 to 12 s, 3.2 to 3.3 GB RSS while loaded (above the 2.5 GB estimate), 21 prompt tok/s, 7.6 gen tok/s, about 0.3 CPU-min per event. Zero dollars.

## Sealed lanes and privacy (phase 1 scope)
- Family and Holman Dock are NOT collected (design: sealed lanes). `exclude_handles` in config lists family and personal-friend numbers found in the bootstrap; `exclude_keywords` drops Holman threads. One sender asked by text not to be imported into any AI platform; that handle is excluded and its events were purged.
- iMessage keyword pull was narrowed to business-only terms (docusign, earnest, invoice, lease, slip, binder, periode, elevated tides); "sauna" alone was pulling friends into the lane.
- Everything stays on mbp-2 (`~/lanes`, mode 600). Dashboard lines are scrubbed of phones and emails.

## Open decisions for Davey (recorded, not decided)
1. Lane order after E&E (design proposes Personal, then NPB).
2. Who sees the daily brief (Davey only vs an E&E cut for Jonah). `brief.py` stub waits on this.
3. Where the brief lives (Command Center tab recommended vs Slack DM).
4. Dollar threshold that forces Tier 3. Code uses the PROPOSED 500 (`rules.tier3_amount`) and labels it as proposed.
5. Retire the in-flight watcher's whole-list Sonnet scan now that the lane is live (recommended: retire, keep its Drive row writer).
Plus: Slack DMs. The bot only reads DMs it is a member of. Reading all of Davey's DMs needs either the bot invited to each DM or a user token.

## Operating it
```
ssh davidrack@100.113.229.1
cat ~/lanes/ee/heartbeat.json                       # collector health
tail -20 ~/lanes/ee/rules.log                       # FILE (live) vs SHADOW lines
cat ~/lanes/dashboard-writer/heartbeat.json; tail ~/lanes/dashboard-writer/writer.log
~/lanes/_model/serve.sh status                      # model up? free RAM?
~/ee-stove-watchdog/venv/bin/python ~/lanes/ee/eval.py --misses
~/ee-stove-watchdog/venv/bin/python ~/lanes/ee/rules.py --replay ~/lanes/ee/events.jsonl --print   # shadow replay
```
Flip `rules.live_kinds` in `config.json` to add `reply` when its golden precision passes 90. Set `rules.live` false to put the whole lane back in shadow. Feedback: tell Claude "that lane line was wrong" and the event's label in `golden.jsonl` is corrected (label_source "hand").
