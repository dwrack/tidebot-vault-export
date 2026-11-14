# Comms Lane Bots — Design (Nov 13 2026)

Status: DESIGN, not built. Owner: Davey + Claude. Machines: davids-mbp-2 (always-on core), bigly (optional heavy model), Claude (daily synthesis only).

## Why

2026-11-10 Jonah emailed davey@ "For your signature: marina approval" and it reached neither the Command Center nor the morning digest for three days. Root cause was structural: the E&E in-flight watcher only tracked "work items", wrote rows nobody displayed, and ran Sonnet over a 221-row list every 2 hours (~250k tokens a day) while still missing the ask. Davey wants (1) asks and facts surfaced within minutes, (2) near-zero token spend, (3) a CEO-level picture of every brand, not just his to-dos, (4) nothing important handed to a model that hallucinates, (5) lanes that cannot garble each other.

## What already exists (checked 2026-11-13, so this is an extension, not a new system)

- **Comms Radar** (`~/comms-radar/` on mbp-2, `com.djl.comms-radar`, every 2h): reads 14 brand Gmail inboxes + DJL Slack, keeps `00 Dashboard/Comms Radar/Ledger.md` (about 200 open threads across 11 brands), and already feeds the Command Center through `needs_you.py` `src_radar`. It does NOT watch iMessage, davey@, sauna@, the personal inbox, or E&E at all, and it runs one Sonnet call per run over the whole ledger.
- **E&E in-flight watcher** (`~/ee-inflight-watch/`): E&E only, texts + davey@ + sauna@ + slack-et, writes Drive rows for Jonah's sweep; asks pass added 11/13.
- **Contractor Watch**, **Incident Log**, **morning-brief**: narrower feeds that already write to the dashboard.

So the lane bots are: Comms Radar split into per-brand lanes with per-lane config and ledgers, the E&E watcher becoming the E&E lane (keeping its Drive publisher), plus the five genuinely new parts: Tier 0 rules, the grounded 3B tier on mbp-2, the single dashboard writer, code-only rollups (promises, silence, money, idle projects), and the daily CEO brief that reads every lane. Retire: the radar's whole-ledger Sonnet call and the watcher's whole-list Sonnet call.

## Principles

1. One bot per lane. A lane is one brand (E&E, DCKT, NPB, HPB, NKST, ...) plus the personal lane. Each bot has its own config (people, inboxes, Slack channels, keywords), its own ledger, its own state, its own prompts. Bots never read another lane's ledger. Cross-brand questions are answered by the daily brief, which reads all ledgers read-only.
2. Trust by tier, stakes decide the tier. Code first, small model for structure only, big model for ambiguity, Claude for judgment and anything outbound. A lower tier can never promote its own output; it can only propose.
3. Ground or drop. Every field a model extracts must carry the verbatim source span; code checks the span exists in the message. No span, no fact. This single rule removes most hallucination risk.
4. Shadow before live. A bot writes to its preview folder until its precision on a golden set is over 90 percent for a week. Then it may write dashboard lines. Dashboard lines from a bot always carry the quote and a tag `[bot:<lane>:<tier>]` so Davey can judge in one glance.
5. One writer. A single `dashboard-writer` process is the only thing that edits Command Center Notes. Bots drop JSON into a queue dir. (Today two writers raced over iCloud and three lines were lost.)
6. Models never send. No tier below Claude posts to Slack, email, text, GBP, or the shared record. Drafts only, and only Tier 3.

## Tiers

| Tier | What | Where | Allowed to do | Cost |
|---|---|---|---|---|
| 0 Rules | regex + allowlists + parsers | mbp-2, every 3 min | file an ask or a fact instantly; strike when Davey's reply lands in the thread; parse dates, amounts, attachments | zero |
| 1 Small model | Qwen2.5-3B-Instruct Q4 via llama.cpp, 2 threads, unload when idle, refuse to load under 3 GB free | mbp-2 | one yes/no question per call, then one JSON extraction per call, schema-validated, span-grounded; writes to lane ledger as `proposed` | zero, ~2.5 GB RAM while loaded, ~20 s a message |
| 2 Heavy model | Qwen 27B/30B on bigly Ollama (127.0.0.1:11434, over ssh) | bigly, when awake | re-check Tier 1 `unsure` items; thread summaries; same grounding rule | zero; skipped if bigly is asleep |
| 3 Claude | Sonnet batch | once a day + on demand | daily CEO brief, shared-record rows (E&E), memory and CLAUDE.md update proposals, any draft to a human, money/legal/people items | ~100k to 200k tokens a day, down from ~250k today |

What never goes below Tier 3: anything with a dollar amount over 500, legal, insurance, personnel, anything that will be sent, anything that changes the E&E shared record.

## Pipeline (per lane)

1. Capture (code): iMessage chat.db, the lane's Gmail inboxes, the lane's Slack channels, Google Voice texts via sauna@ forwarding. Append raw events to `~/lanes/<lane>/events.jsonl`. Dedupe by (source, id).
2. Normalize (code): strip quoted replies, signatures, HTML, tracking links; resolve handles to names from the lane's people list; group into threads; tag brand by inbox/channel/people BEFORE any model sees it; drop newsletters, receipts, booking notices into a `noise` bucket (regex on sender and subject).
3. Rules (Tier 0): asks of Davey (from a listed person, addressed to him, with sign/DocuSign/approve/pay/invoice/check/need you/can you/question mark, or an attachment plus sign); commitments by Davey ("I'll", "will do", "on it"); dates; money; silence (listed person quiet more than N days); strike-throughs.
4. Structure (Tier 1): for events rules did not settle, ask the 3B two narrow questions: "Is this a request that Davey personally has to act on? yes/no/unsure" and, if yes, "Fill this JSON: who, what (imperative, under 15 words), kind, due, amount, quote_span." Validate span and enum; anything invalid or `unsure` goes to the Tier 2 queue.
5. Recheck (Tier 2): same two questions, bigger model, plus thread summary. Still unsure stays `unsure` and shows in the daily brief as "could not classify" rather than being guessed.
6. Ledger (code): `people`, `vendors`, `projects`, `money`, `promises`, `asks` tables per lane with status and last_touch. Rollups are pure code: open asks, Davey's unkept promises, due inside 7 days, silence over 5 days, projects idle over 10 days, money due this month.
7. Publish: Tier 0 and validated Tier 1 asks go to the dashboard queue at once. Everything else waits for the daily brief.
8. Daily CEO brief (Tier 3): reads every lane's rollups and deltas, writes three sections: What you should know (decisions pending, risks, money, people), What Claude should know (facts that changed; proposed memory and CLAUDE.md edits, applied only on Davey's tap), What we should do (3 to 5 moves this week, and what we are ignoring). Ends with "what I could not see" (failed collector, unknown handle, unsure items). Feedback buttons on the Command Center: right, wrong, skip, more of this; stored per lane and fed back as examples.

## Making it easy for the small model

- Never ask it an open question. Yes/no first, then a fixed JSON schema with enums.
- One message or one short thread per call, under 1,500 tokens, with the people list and brand already resolved in the prompt.
- Few-shot examples from this lane's golden set (10 positives, 10 negatives), refreshed weekly from Davey's feedback.
- Temperature 0, JSON grammar enforced by llama.cpp, 3 retries then `unsure`.
- It never sees other lanes, never sees the ledger, never writes prose for a human.

## Lanes and sources (phase 1)

| Lane | People allowlist | Inboxes | Slack | Texts |
|---|---|---|---|---|
| E&E | Jonah, Grant, Alex, Max, Sergey, Mack, L, Kimberlynn, Hannah, Jess, Adrian | davey@, sauna@ | slack-et channels (13) | chat.db, partner handle rule |
| Personal | Jac, family, Dustin buyout counsel | dwrack81@ | none | chat.db |
| NPB (phase 2) | Jeff, Michael, captains | nolapedalbarge | DJL slack | chat.db |

Other brands join one at a time after NPB proves the lane template.

## Evaluation

Golden set: last 30 days of each lane, hand-labelled from Davey's feedback plus the known misses (marina approval 11/10, slip 9 earnest 11/2). Weekly report per lane: asks precision/recall, facts precision, unsure rate, tokens used, model minutes on mbp-2. Promotion to live needs 90 percent precision; demotion back to shadow if it drops under 80.

## Costs

- Dollars: zero for Tiers 0 to 2 (electricity). Tier 3 about 100k to 200k Sonnet tokens a day on the subscription.
- mbp-2: 3B model 2.5 GB RAM only while loaded, about 30 CPU minutes a day at 100 messages. Polls every 3 minutes are negligible. 127 launchd jobs already run there; this adds 1 collector per lane plus the writer.
- Build: phase 1 (E&E lane, rules + 3B + writer + brief) about two working days. Phase 2 (personal, NPB) one day each.

## Open decisions for Davey

1. Lane list and order after E&E.
2. Who sees the daily brief: Davey only, or an E&E cut for Jonah without non-E&E matter.
3. Where the brief lives: Command Center tab (recommended) vs Slack DM.
4. Dollar threshold that forces Tier 3 (proposed 500).
5. Keep or retire the current E&E in-flight watcher once the lane bot is live (recommended: retire, keep its Drive row writer as the E&E publisher).

## Related

- E&E in-flight watcher: `~/ee-inflight-watch/` on mbp-2 (asks pass added 2026-11-13)
- Contractor Watch: `~/ee-contractor-watch/`
- Command Center: `~/.claude/scripts/command-center/needs_you.py` (sources: radar, queue, notes, approvals, outbox, deadlines, fires)
- bigly: Ollama on 127.0.0.1:11434, models qwen27-cc, qc30
