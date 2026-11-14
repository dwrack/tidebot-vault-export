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
| Tier 1 model | `~/lanes/ee/structure.py`, `~/lanes/_model/serve.sh` | `com.djl.lane-ee-structure` | every 20 min | PRIMARY: bigly qc30 (Qwen3-Coder 30B Q4_K_M via Ollama, called over ssh from mbp-2). The lane takes bigly's `~/.guard/heavy.lock` for each batch (self-expires in 15 min) and skips bigly when it is asleep, the lock is held, Draw Things or ComfyUI runs, another model is loaded, or memory_pressure free is under 25%, the same floor as `~/bin/heavy`. FALLBACK: Qwen2.5-3B on mbp-2 via llama.cpp (built from source b12374), 2 threads, killed after each batch, refuses under 3 GB free. A code gate drops messages addressed to someone else before any model call. Two narrow calls per event: yes/no (schema), then JSON; grounding swaps in the verbatim source quote or rejects. SHADOW: `preview/structure-*.jsonl` and `unsure.jsonl` only. |
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
- Tier 1, same 110-event golden sample, four versions on 2026-11-13 (rows in `Eval.md`):
  | version | precision | recall | unsure |
  |---|---|---|---|
  | v1 3B, yes/no/unsure | 100% (3 calls) | 20% | 96.4% |
  | v2 3B tuned (yes/no, thread context, 20+20 shots) | 71.4% | 26.3% | 0.9% |
  | v3 bigly qc30 | 66.7% | 68.4% | 1.8% |
  | v4 bigly qc30 + address gate (production) | 80.6% | 65.8% | 1.8% |
  All 3 hand-labelled misses are yes on v3 and v4. Still shadow: promotion needs 90% for a week. Speed on bigly with the model warm: question 1 median 0.33 s, question 2 median 1.0 s, 110 events in 130 s; first call after a cold load adds about 10 s. On the mbp-2 fallback: about 17 s per event, 3.7 GB RSS.
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

## Tier 1 fine-tune by distillation (started 2026-11-13, Davey: "train it")

Goal: the always-on 3B on mbp-2 clears 90% precision on the golden sample, so Tier 1 stops depending on bigly being awake.

| Step | Where | What |
|---|---|---|
| Pool | mbp-2 `~/lanes/train/build_pool.py` | 12 months of business messages, same normalizer as the collector: E&E texts, davey@, sauna@, slack-et; plus the 12 DJL brand inboxes and brand-manager texts Comms Radar reads. Excluded entirely: dwrack81 personal inbox, family and personal-friend handles, Holman Dock. Balanced candidates in `pool_cand.jsonl` (all likely asks, a capped share of the rest, about 4% of noise). |
| Holdout | build_pool + make_sft | The 110-event golden sample and the last 14 days never become training data (checked twice). |
| Labels | mbp-2 `label.py`, launchd `com.djl.lane-train` 23:05 | Headless Claude Sonnet, tools off, 30 messages per call, same two outputs as Tier 1 (yes/no, then JSON with a verbatim quote). Answer key per message: Davey's next reply in the thread, matching Command Center lines (open or struck), Needs You Log, in-flight asks. Capped at 1.5M tokens a night, 23:00 to 06:00 only, resumes from `label_state.json`. Positives whose quote cannot be grounded are excluded from training. |
| Gate | `~/lanes/train/SPOTCHECK_OK` | Training starts only after 50 labels are spot-checked by hand. |
| Pairs | mbp-2 `make_sft.py` | MLX chat pairs built with the served prompt builders (`structure.q1_text`, `q2_text`, `event_block` with thread context), without the few-shot block; the fine-tuned model runs with `tier1.local_fewshot=false`, so no golden text sits in any training prompt. Negatives capped at 2x positives; split 90/10 by thread. |
| Train | bigly `~/lanes-train/train_bigly.sh` | LoRA on Qwen2.5-3B-Instruct with MLX (`mlx_lm.lora --mask-prompt`, 16 layers, 1,200 iters), fuse, convert to GGUF, quantize to Q4_K_M with llama.cpp b12374. Frees Ollama models first and runs under bigly's `~/bin/heavy` (lock + 25% free floor; memguard still watches). |
| Deploy + eval | mbp-2 `pipeline.py` | Pulls `qwen2.5-3b-lane-ft-q4_k_m.gguf` into `~/lanes/_model/` next to the base model, runs the golden sample locally with no few-shots, appends a row to `Eval.md`. Switch by config: `tier1.local_model`, `tier1.local_fewshot`, `tier1.backends`. |
| Promotion | pipeline.py | If the fine-tune reaches 90% precision with recall at or above the 30B's 65.8%, it becomes primary (`backends: ["local","bigly"]`); otherwise bigly qc30 stays primary. Tier 1 stays shadow either way for at least one more week. One dashboard line reports the result. |
| Monthly retrain | `retrain_monthly.py` | Designed and stubbed only, not scheduled. |

Data handling: the pool, labels, pairs and model weights stay on mbp-2 and bigly (mode 600 files under `~/lanes/train` and `~/lanes-train`); nothing is uploaded anywhere except the Sonnet labeling calls on Davey's own Claude subscription. The fine-tuned weights are trained on business messages from several brands, so they stay local and are never shared.
