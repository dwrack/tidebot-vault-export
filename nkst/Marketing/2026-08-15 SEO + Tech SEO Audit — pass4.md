---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: DRAFT — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech SEO Audit — 2026-08-15 (Pass 4, delta check)

> **DRAFT. REPORT ONLY.** Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform. This is a light delta check against Pass 3 (`Marketing/2026-08-15 SEO + Tech SEO Audit — pass3.md`, ~05:36), not a fourth full audit — per Pass 3's own recommendation, a full re-run wasn't warranted.

**Bottom line: nothing material changed on the live site since Pass 3. The one real development, again, is more staged drafts — three new ones, and one of them closes a gap that's been open since the May 4 audit. Read the recommendation at the bottom: it's the same as Pass 3's, and it's getting more urgent, not less.**

---

## 1. MCP check

Ran ToolSearch for GSC/Search Console, GA4/Analytics, and PageSpeed Insights tooling this session. **Still nothing registered.** No fresher ranking, traffic, or Core Web Vitals data exists to pull. Same wall as passes 1–3.

## 2. Live-site re-fetch — all confirmed unchanged from Pass 3

Re-fetched directly via HTTP (curl), not re-read from the prior file:

| Check | Result |
|---|---|
| Homepage nav | Still links to `/new-orleans-zipline-tour-kayak-tour-combo/`, which still 301s straight back to `/` — dead end, unresolved |
| Homepage links to `/tours/swamp/` or `/swamp-tours-new-orleans-guide/` | Still 0 matches |
| `/alligators-vs-crocodiles/` links to `/tours/swamp/` or the guide | Still 0 matches |
| `/tours/kayak-tours/honey-island-swamp-tour/` meta description | Still the literal boilerplate "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2" |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Both still live (200), H1s still distinct ("New Orleans swamp tour reviews" vs. "What is the best Swamp Tour near New Orleans?") — cannibalization unresolved |
| Dual canonical: `/swamp-tours-new-orleans-guide/` vs `/blog/swamp-tours-new-orleans-guide/` | Both still 200, both still self-canonicalize to themselves — no consolidation signal, unresolved |
| `/alligator-tour-new-orleans/` | Still 404 (draft exists, page doesn't) |
| `/how-much-does-a-swamp-tour-cost-new-orleans/` | Still 404 (draft exists, page doesn't) |

Nothing here diverges from Pass 3 in any way. No new re-litigation needed.

## 3. Staged drafts backlog — grew again

`Marketing/Blog Drafts - Staged/` now holds **23 files**, up from Pass 3's 20 (18 usable + 2 confirmed duplicates). **Three new drafts appeared after Pass 3 ran**, timestamped 05:45–05:49:

- `2026-08-15 - bachelorette-bachelor-party-swamp-tour-new-orleans.md` — content-gate 91/100. This is the one worth flagging on its own: it closes **Pass 2's Strategic item #14** ("Bachelor/bachelorette content rebuild... no draft found in either `SEO Content/` or `Blog Drafts - Staged/`... genuinely still a gap"), open since the 2026-05-04 audit. Same pattern as the `alligator-tour-new-orleans` draft Pass 2 flagged — a "needs research and writing" line item is now just a publish decision.
- `2026-08-15 - cypress-trees-manchac-swamp-ecology-restoration.md` — content-gate 90/100. Closes a Week 2–4 Content Plan roadmap item, never drafted until now.
- `2026-08-15 - things-to-do-new-orleans-fall-outdoors.md` — content-gate 88/100. Fall installment of the "things to do in New Orleans in [month]" series flagged as an open GSC-confirmed gap in the 2026-05-04 audit.

All three read as genuinely new, non-duplicate topics per their own draft notes (each cites what it's distinct from). No new duplicate-content risk to flag.

**Net effect on the fix list:** Pass 2 §9, Quick Win #1 (David batch-reviews the staged drafts) gets one more concrete item — add `bachelorette-bachelor-party-swamp-tour-new-orleans` to the batch, and note that it also closes Strategic item #14, so #14 can be downgraded from "no draft exists" to "draft exists, pending publish" once approved. Nothing else on the standing 15-item list (Pass 2 §9) changes. See Pass 2 and Pass 3 for the full list — not repeated here.

---

## Recommendation

Same as Pass 3, restated because it still holds and the gap between "audited" and "acted on" just got wider again: **hold this cadence.** Four consecutive same-day audits (Pass 1 ~00:28, Pass 2 ~01:49, Pass 3 ~05:36, this one) have confirmed the identical set of open items — price discrepancy, GA4 tracking gap, GBP MCP unreachable, Crescent City Kayak decision, dual-canonical URLs, zipline dead nav link, cannibalizing "best swamp tour" pages, two 404s with drafts sitting unpublished — with zero forward motion, because none of them can move without David at a keyboard. The staged-drafts folder has grown from 14 (Pass 2) to 20 (Pass 3) to 23 (now) over the course of one day, entirely unattended. **Recommend pass 5 not be run until David clears the batch-review of the staged drafts and the standing Pass 2 §9 fix list.** Another delta check tomorrow will very likely say the same thing again, plus a bigger folder.

---

## Notes

- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in producing this report.
- All "confirmed unchanged" findings above were re-fetched live via curl this pass, not copied from Pass 3's text.
