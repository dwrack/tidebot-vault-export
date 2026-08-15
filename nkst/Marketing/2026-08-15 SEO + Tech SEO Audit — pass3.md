---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: DRAFT — PENDING DAVID'S REVIEW — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech SEO Audit — 2026-08-15 (Pass 3)

> **DRAFT. REPORT ONLY.** Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform. This is the third unattended audit today, run ~05:36, roughly 3.5 hours after Pass 2 (~01:49) and 5 hours after Pass 1 (~00:28).

**Read this first: nothing material changed on the live site or in the ranking/traffic data since Pass 2, and that's expected — it's a 3.5-hour, report-only window. The one real development is that the content pipeline generated three more staged drafts while this audit was sleeping, which makes the approval backlog Pass 2 flagged as the real bottleneck bigger, not smaller. Pass 2's own closing line still stands word for word: "the bottleneck on this site is not research, not writing, and increasingly not even technical — it's an approval queue." Three consecutive same-day audits have now confirmed the same open items (price discrepancy, GA4 tracking gap, GBP MCP unreachable, Crescent City Kayak decision) with zero forward motion, because none of them can be resolved by another audit — they need David at a keyboard. See the recommendation at the bottom.**

---

## Data Sources & Gaps

**GSC/GA4/PSI MCP: checked again via ToolSearch this session, still not registered.** Same result as all prior passes today and this week. No fresher GSC or GA4 numbers exist to pull — every figure below is carried forward from the 2026-08-10 GSC pull (90-day window) and the March 2026 GA4 pull, both already cited in Pass 2.

**PageSpeed Insights: ran fresh again, same `HTTP 429` quota-exceeded on both mobile and desktop, all 8 FareHarbor sites including NKST.** No `PSI_KEY` on file. Cached data still `~/Projects/tech-seo/out/psi-20260619.json`, now **58 days old** (unchanged from Pass 2 — same day, no new staleness to report, but still the number driving every Core Web Vitals line below). `node` this time resolved automatically at `/usr/local/bin/node` without the PATH workaround Pass 2 needed — minor, but the Pass 2 note asking to fix that is now moot.

**What this pass actually did:** re-fetched the live homepage, `/alligators-vs-crocodiles/`, the dual-canonical URL pairs, the zipline dead-end link, the Honey Island archive meta description, and the two duplicate "best swamp tour" H1s directly via HTTP — all confirmed byte-for-byte unchanged from Pass 2's fresh fetches 3.5 hours ago. Then opened `Marketing/Blog Drafts - Staged/` again, since that's where Pass 2 found its one real finding.

---

## What's genuinely new in this pass

**Three more staged drafts appeared, all timestamped 01:53 — four minutes after Pass 2 finished (~01:49).** The automated content pipeline is still running unattended alongside the audit pipeline:

- `2026-08-15 - bayou-sauvage-wildlife-refuge-new-orleans.md` — content-gate 86/100. Covers a real, currently-offered NKST tour (Bayou Sauvage National Wildlife Refuge) that has never had a dedicated post. Cites its own source: named as a geography-cluster target in `SEO Content/Content Plan.md`, previously mentioned only once in a GBP calendar post.
- `2026-08-15 - photograph-manchac-swamp-from-kayak.md` — content-gate 89/100. Directly closes competitor-gap idea #9 from `Marketing/Competitor Content-Gap Analysis — Wild Louisiana (June 2026).md` ("Best Spots to Photograph the Manchac Swamp (From Your Kayak)"), never actioned until now. Confirmed distinct from the existing birding field-guide draft (species-ID vs. composition/timing/gear).
- `2026-08-15 - rougarou-louisiana-swamp-legend.md` — content-gate 89/100. Zero prior mentions of "Rougarou"/"loup-garou" anywhere in `Marketing/` or `SEO Content/` per the draft's own note. Confirmed distinct from the two existing Julia Brown/Manchac haunted drafts and from the Honey Island Swamp Monster material already inside the `honey-island-swamp-visitor-guide` FAQ.

All three read as genuinely new topics, not restages of shipped content — no third duplicate problem to flag alongside the two Pass 2 already caught (`airboat-vs-kayak-swamp-tour-new-orleans`, `first-time-kayak-swamp-tour-new-orleans`).

**Net effect on the backlog:** `Marketing/Blog Drafts - Staged/` now holds **20 files** (verified via direct directory listing this pass), not the 14 Pass 2 counted a few hours ago. Of those 20: 2 are confirmed duplicates that should be discarded, leaving **18 genuinely usable, unpublished, content-gate-passed drafts**, plus the 5 already-published Content Plan posts — **23 real content assets**, up from Pass 2's 19. The backlog grew while this audit slept. Nothing else about the content-gap picture changed; Pass 2's table of which gaps are closed-in-staging vs. genuinely open (bachelor/bachelorette content, OTA listing rewrites, GBP work) is unchanged and not repeated here.

**Everything else checked came back identical to Pass 2:**

| Item | Status this pass |
|---|---|
| Homepage links to `/tours/swamp/` or `/swamp-tours-new-orleans-guide/` | Still 0 matches |
| `/alligators-vs-crocodiles/` links to `/tours/swamp/` | Still 0 matches |
| Dual-URL canonical tags (`/swamp-tours-new-orleans-guide/` vs `/blog/swamp-tours-new-orleans-guide/`) | Still self-canonicalizing on both variants — unresolved duplicate-content pair, confirmed again |
| `/new-orleans-zipline-tour-kayak-tour-combo/` nav link | Still 301s straight back to homepage — dead end, unresolved |
| `/tours/kayak-tours/honey-island-swamp-tour/` meta description | Still the literal boilerplate "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2" |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Both still live, H1s still distinct ("New Orleans swamp tour reviews" vs. "What is the best Swamp Tour near New Orleans?") — cannibalization unresolved |
| `alligator-tour-new-orleans` and `how-much-does-a-swamp-tour-cost-new-orleans` live URLs | Both still confirmed 404 — the drafts exist, the pages don't |
| robots.txt | Unchanged |
| PSI/Core Web Vitals | Still 429, still the 58-day-old 2026-06-19 numbers (mobile 37/red, desktop 54/amber) |
| Price mix across tour pages ($65/$79/$195 per the Aug 2026 AEO audit; live spot-check found $25 on the Honey Island page, no Offer schema anywhere) | Unresolved, no Offer/pricing schema added anywhere — consistent with every prior pass |
| GA4 (11,848 sessions/90d baseline), FareHarbor→GA4 purchase-event gap (58 events vs. 23,385 GHL contacts) | No fresher pull reachable, still unconfirmed whether ever fixed |
| GBP category mismatch, duplicate-listing cluster, Crescent City Kayak decision | No new data, GBP MCP still unreachable |

No SEO or technical finding in this pass required re-litigating at length — Pass 2 is the record for all of the above; this table exists only to show it was re-verified, not assumed.

---

## Merged Prioritized Fix List — Changes From Pass 2 Only

Pass 2's 15-item list (Marketing/2026-08-15 SEO + Tech SEO Audit — pass2.md, §9) stands unchanged. Nothing below replaces it — this is what's different:

### Quick Wins (this week)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 (updated) | `Marketing/Blog Drafts - Staged/` (now 20 files, was 14 at Pass 2) | Same recommendation as Pass 2 item #1, now with a bigger pile: discard the 2 confirmed duplicates, then batch-review all 18 remaining content-gate-passed drafts in one sitting, including the 3 new ones from this pass (`bayou-sauvage-wildlife-refuge-new-orleans`, `photograph-manchac-swamp-from-kayak`, `rougarou-louisiana-swamp-legend`, all PASS at 86-89/100). | Same thesis as Pass 2, stronger: every hour this queue sits unattended, the automated pipeline adds to it faster than any audit can process it. This is now visibly a growing-backlog problem, not a static one. |

No other Quick Win or Strategic item changed — see Pass 2 §9 for the full 15-item list (schema on `/tours/swamp/`, dual-canonical fix, Honey Island 301, best-swamp-tour merge, zipline nav link, PSI key, GBP, Crescent City Kayak, GA4 tracking confirmation, etc.), all still open exactly as stated there.

---

## Recommendation

This pass found nothing that changes the fix list, nothing that closes an open item, and one new data point (3 more drafts, 20 total) that makes the backlog worse, not better. That's the honest read: **three same-day audits have now independently re-confirmed the same unresolved items** (price discrepancy, FareHarbor→GA4 gap, GBP MCP down, Crescent City Kayak, dual-canonical, zipline dead link) with zero forward motion on any of them, because none of them can move without David.

**Recommend pausing this recurring unattended-audit cadence until David clears the existing backlog** — 18 usable staged drafts and the 15-item Pass 2 fix list. A 4th or 5th pass today would almost certainly repeat this exact pattern: confirm everything's still the same, note the staging folder grew again. Another audit doesn't help until someone acts on the last one.

---

## Notes

- Everything marked "confirmed" or "unchanged" above was re-fetched live this pass, not copied from Pass 2's text.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in producing this report.
