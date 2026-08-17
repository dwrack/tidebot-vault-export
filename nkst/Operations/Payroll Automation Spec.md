# NKST Payroll Automation — Spec

Locked with David 2026-08-17. Build target: `~/Projects/fareharbor-brief/payroll-run.mjs`

## Decisions

| Item | Decision |
|---|---|
| Scope | NKST only. Clone to other brands after 2 clean periods. |
| Pay period | Semimonthly: 1-15 and 16-EOM |
| Run days | 1st and 16th |
| Automation level | Compute → draft → David approves → sends. Never auto-sends. |
| Approval channel | `#the-helm`, react ✅ to release |
| Guide stub | Slack **DM** to each guide after release. Never the shared channel (rates differ). |
| Payout rail | PayPal Payouts API batch. Manual send list as fallback until creds exist. |
| Doubles | Full rate to each guide. Tips from that departure split 50/50. |
| Adjustments | David replies to the `#the-helm` post with line items; it recalcs before sending. |

## Rate card (authoritative — this file is now the rate card)

| Guide | Standard tour | Extended tour |
|---|---|---|
| Michelle Healey | $125 | $200 |
| Nick Napoda | $125 | $200 |
| Chelsea Hines | $110 | $200 |
| Stephanie Lazensky | $100 | $200 |
| River Bourne | $100 | $200 |
| Alexis Hingle | $100 | $200 |
| Abbie Marks | $100 | $200 |

Extended tours are a flat $200 for everyone regardless of standard rate. Nick confirmed $125 on 2026-08-17 (was previously unconfirmed; the unsigned ICA Exhibit A draft was right on this one).

Any guide not listed = STOP and ask David. Do not default to $100.

## Pay components

Included:
- Per-tour rate × tours run (from FareHarbor crew_member assignments)
- Extended tours at $200 flat
- Gratuity pass-through (from `guide-gratuity.mjs`), split 50/50 on doubles
- Manual bonuses / line items via reply-to-approval (manager day rate, self-guide, consolidation, monthly)

Excluded: mileage and reimbursements. No submission channel exists, so these stay manual outside the system.

## Pipeline

1. **Tally** — `guide-payroll.mjs neworleanskayakswamptours <start> <end>`. Already works. Playwright scrape, no API needed. A tour counts as RUN when the availability is in range, `customer_count > 0`, and not cancelled.
2. **Tips** — `guide-gratuity.mjs` for the same range.
3. **Rate apply** — join against the rate card above. Unknown guide = hard stop.
4. **Draft** — post table to `#the-helm`: guide, tours (standard/extended), rate, tour pay, tips, adjustments, total. Plus period total and a variance line vs last period.
5. **Approve** — David ✅, or replies with adjustments and then ✅.
6. **Pay** — PayPal Payouts batch, one item per guide, memo `NKST tours <period>`.
7. **Stub** — DM each guide their own breakdown with the dates of every tour credited.
8. **Record** — append to a YTD ledger per guide for 1099-NEC, and write a period close file to `Operations/Payroll/`.

## Hard rules

- No guide gets paid an amount that wasn't in the approved draft.
- Auth expiry: the FareHarbor scrape cookie (`auth.json`) expires ~2026-09-02. If it's dead the run must fail loudly in `#the-helm`, never silently pay zero or pay stale numbers.
- Rate changes get written HERE first, then into code. The whole reason payroll has been wrong twice is that no written rate card existed.

## Build status (2026-08-17)

Built and validated. Files live in `~/Projects/fareharbor-brief/`:

| File | Does |
|---|---|
| `payroll-config.json` | Rate card, payable-item allowlist, roster with FareHarbor slugs and Slack IDs |
| `payroll-run.mjs` | The run: scrape → filter → rate → tips → draft → send list. `--post` to Slack. |
| `payroll-roster.mjs` | Resolves guide Slack IDs and emails into the config |

**Validated against real money.** Re-running the 7/16-31 period produced **$1,670.00**, matching the close David paid by hand, per guide, including the $125 Michelle and $110 Chelsea corrections.

Usage: `node payroll-run.mjs` (last completed period, dry run) → review → `--post` to put the draft in #helm-nkst.

## What the build found in real data

1. **Most calendar "departures" aren't tours.** Aug 1-15 had 17 departures, only 9 payable. Gift Cards, Bayou Kayak Rentals and Monthly Passes all appear as departures with pax and no crew. Hence the `payableItems` allowlist — without it every period shows 8-9 phantom unassigned tours and the noise hides a real one.
2. **FareHarbor slugs don't match names.** Michelle is `michelle`, Nick is `nick`. Guessing `michellehealey` silently dropped her two July tours, $250. This is how the original underpayments happened. `fhUsernames` is an array because some guides have two accounts.
3. **An unassigned tour is eating money right now.** `2026-08-01 09:00 Manchac, 10 pax, no crew` — and it carries the period's only **$65 of tips**. Someone guided 10 people and is owed a tour rate plus that tip.
4. **Five unidentified crew slugs** ran real Manchac tours May-Aug: `poboy` (14 tours), `davidryan` (9), `mj` (2), `alex` (2), `river` (1). Until David names them and sets rates, any period containing them halts.
5. **Slack has no emails exposed.** The TideBot token lacks `users:read.email`, so PayPal-from-Slack-email can't self-resolve. Michelle's known address (mcnamml@gmail.com) looks nothing like her name, which confirms guessing addresses would have been wrong.

## Open items

1. **Identify 5 crew slugs** — `poboy`, `davidryan`, `mj`, `alex`, `river`. Name + rate each, or mark as settled/not owed.
2. **Assign the 8/1 Manchac tour** — 10 pax, $65 tip, currently paid to nobody.
3. **PayPal addresses for 6 guides** — only Michelle's is known and it's unverified. Either add `users:read.email` to the TideBot Slack app and re-run `payroll-roster.mjs --write`, or paste them.
4. **Confirm River's Slack account** — workspace has three Rivers; `@riverbourne.here` ("river b.", U0B0C988FAR) matches the FareHarbor slug but is not bound automatically.
5. **PayPal Payouts enablement** — developer.paypal.com → Apps & Credentials → Live. Rail stays `manual` until then; nothing in the repo can move money while it is.
6. **Adjustment reader** — bonuses currently come in via `--adjust "Name:amount:reason"`. Reading them from David's Slack reply is not built yet.
7. **1099-NEC** — PayPal Payouts does not relieve NKST of filing for contractors over $600. YTD ledger not built yet. Confirm with Bob Draught how he wants the file.
8. **Scheduling** — no launchd job yet. Deliberate: don't schedule it until a period runs clean by hand.

## Known landmines

- The Alex Wallace review anomaly is unresolved and blocks review-linked bonuses. Don't wire review counts into pay until that's settled.
- Guide roster is in flux — 3 fixed-day guides being hired, Thu empty and Fri dark after Aug 28. New hires need a rate in this file before their first payroll.
