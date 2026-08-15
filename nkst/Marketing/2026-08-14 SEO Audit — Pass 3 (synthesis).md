---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-14
status: REPORT ONLY — NO CHANGES APPLIED
---

# NKST SEO Audit — Pass 3 (Synthesis / Re-verification), 2026-08-14

**This is a synthesis and re-verification pass, not a third from-scratch audit.** Two full audits already ran today with an identical data-availability picture:
- `Marketing/SEO + Tech SEO Audit — 2026-08-14.md` (generated ~13:27)
- `Marketing/2026-08-14 SEO + Technical Audit NKST.md` (generated later, same day)

Both are correct and thorough. This pass exists to (1) confirm whether anything changed in the hours since, (2) check again whether GSC/GA4/GBP access came back, and (3) surface one thing neither prior pass dug into: a large stash of already-written, unpublished content sitting in this vault that quietly resolves most of the "Strategic Work" content gaps both audits flagged. **REPORT ONLY — nothing below has been applied to the live site, WordPress, GBP, or any ad platform.**

---

## 1. MCP / data access — still broken, confirmed again

Ran ToolSearch this session against "search console gsc keywords," "ga4 analytics property," and "google business profile reviews." No `gsc_*`, `ga4_*`, or GBP tools surfaced — same result as both earlier passes today. `PSI_KEY` is still not set (`~/.claude/.env` exists but contains no `PSI_KEY` entry; keyless PSI quota was already confirmed exhausted by the second audit via direct curl). **No change. Still recommend fixing the `google-nkst`/`gbp` MCP connections and adding a `PSI_KEY` before the next run** — three passes in one day have now hit the same wall.

## 2. Live re-verification — nothing material changed

Independently re-checked robots.txt, sitemap.xml, HTTP status on the 9 key URLs, and JSON-LD schema (via a proper Python/urllib parse, not just grep — the naive grep run initially mis-triggered on inline SVG `<title>` icon labels and had to be redone) on the six pages named in the brief.

| Check | Result | vs. prior two audits |
|---|---|---|
| robots.txt | 200, sitemap referenced correctly, same scraper-blocklist pattern | Unchanged |
| sitemap.xml | 200, valid sitemap index → 3 child sitemaps | Unchanged |
| HTTP status, 9 URLs incl. both "best swamp tour" pages and both Honey Island URLs | All 200 | Unchanged |
| `/` schema | LocalBusiness, Organization, WebSite, WebPage, VideoObject — no AggregateRating, no FAQPage | Unchanged |
| `/tours/swamp/` schema | BreadcrumbList only | Unchanged — still the under-built money page |
| `/alligators-vs-crocodiles/` schema | Article, BreadcrumbList — no FAQPage | Unchanged |
| `/alligators-vs-crocodiles/` → `/tours/swamp/` internal link | Confirmed absent again (fresh href scan, full link list pulled — 30 unique on-page links, `/tours/swamp/` is not among them) | Unchanged — still the #1 quick win in both prior lists |
| Manchac tour page schema | BreadcrumbList, VideoObject — no Product/Offer/AggregateRating | Unchanged |
| `/julie-white/` schema (not previously schema-checked) | Article, BreadcrumbList. New data point: title tag is "Julie White - Haunted Louisiana Swamp By Voodoo Priestess" — ties directly to the haunted/legend content angle covered in §3 below | New data point, not a change |
| Honey Island real tour page schema (not previously schema-checked) | BreadcrumbList, VideoObject — no Product/Offer/AggregateRating, same pattern as Manchac | New data point, confirms the "6 tour pages" schema gap applies here too, not a change |
| Honey Island archive URL meta description | Still literally `"Click to view honey island swamp tour category posts in Blog | Page 1 of 2"` | Unchanged |

**Bottom line: zero material change since the 13:27 and later-today passes.** Nothing shipped in the last few hours. Every open item from both prior lists is still open.

## 3. New finding: the "Strategic Work" content gap is mostly already solved, pending David's approval

This is the one thing worth a third pass to surface. Neither prior audit today opened `Marketing/Blog Drafts - Staged/` or `SEO Content/` — both correctly flagged content gaps (Manchac haunted cluster, kayak-vs-airboat, first-timer anxiety content, "how much does it cost," swamp-tour money-page copy) as **unbuilt**. They're not unbuilt. They're written and sitting unpublished:

**`SEO Content/` — 5 full CMS-ready posts + a content plan + an internal-linking audit, all dated May 6-7, 2026 (over 3 months old, never published):**
- Post 1 — Swamp Tours New Orleans Guide (slug `swamp-tours-new-orleans-guide`) — **this is the exact money page** both audits' Strategic item #8 says to build, already written, with FAQ schema spec'd.
- Post 2 — Airboat vs Kayak (`airboat-vs-kayak-swamp-tour-new-orleans`) — Strategic item #10, already written.
- Post 3 — Manchac Swamp Visitor Guide — feeds the Manchac haunted cluster gap (item #11).
- Post 4 — Bayou Bienvenue Vanishing Swamp.
- Post 5 — First Time Kayak Swamp Tour — the practical-anxiety gap (item #4 in the content-gap section).
- `Internal Linking Audit.md` — has the exact "More reading" HTML block to append to `/alligators-vs-crocodiles/`, i.e. the literal Quick Win #1 both audits list today, already drafted with the anchor text and link targets written out.
- `Content Plan.md` — the GSC-driven rationale, word counts, slugs, and a Week 2-4 roadmap that already lists "Honey Island vs. Manchac," "Whitney Plantation combo," and "what to wear" as next up — which brings us to the second folder.

**`Marketing/Blog Drafts - Staged/` — 11 more drafts, in two batches:**
- 5 from 2026-06-13: best-time-to-see-alligators, haunted-manchac-swamp-legend (directly covers content-gap item #1, the Manchac haunted cluster), haunted-swamp-tours-near-new-orleans, honey-island-vs-manchac-swamp-tour, what-to-wear-louisiana-swamp-kayak-tour (covers content-gap item #4).
- 6 from **2026-08-14 — today, some as recent as 15:58-16:00**, each carrying a logged content-gate score (88-92/100, all PASS): whitney-plantation-swamp-tour-combo-guide, alligator-safety-kayak-swamp-tour-new-orleans (covers content-gap item #2, "will I see an alligator"), bayou-st-john-kayak-marie-laveau-voodoo-history, airboat-vs-kayak-swamp-tour-new-orleans, how-much-does-a-swamp-tour-cost-new-orleans (covers content-gap item #5, the highest commercial-intent PAA question both audits flagged as "nothing built yet"), first-time-kayak-swamp-tour-new-orleans.

**One thing to flag before David approves any of this:** two topics now exist as two separate, differently-angled drafts each — "airboat vs kayak" (May 6 CMS post vs. an Aug 14 restaged version, different H1s: "Airboat vs. Kayak Swamp Tour: An Honest Comparison" vs. "Airboat vs. Kayak Swamp Tour in New Orleans: An Honest Comparison") and "first time kayak swamp tour" (same pattern, different H1s). They're not identical copy-paste duplicates, but publishing both under near-identical slugs would recreate the exact cannibalization problem both audits already flagged elsewhere on the site (the two "best swamp tour" pages). **Pick one per topic before publishing, don't ship both.**

**Net effect on both prior audits' Strategic Work lists:** items #8 (`/tours/swamp/` rebuild), #10 (kayak vs airboat), #11 (Manchac haunted cluster), #12 is separate (the free-walks rewrite, still genuinely unbuilt), and #13 ("how much does it cost") are not research or writing gaps anymore — they're a **publishing decision** sitting on David's desk. The internal-linking work (Quick Win #1 in both lists) is also pre-written, not just recommended.

---

## 4. Updated prioritized fix list

Synthesized from both prior lists, de-duplicated, with the Section 3 finding folded in. Items unchanged from both prior audits are compressed; only what's new or reframed gets full explanation.

### Quick Wins (this week)

| # | Page/URL | Exact change | Status |
|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | Publish the "More reading" link block from `SEO Content/Internal Linking Audit.md` (already-written HTML) linking to the new Post 1 (swamp-tours-new-orleans-guide), Post 3 (Manchac guide), and Post 2 (airboat vs kayak) — but only once those posts are live, see item 6 below. In the meantime, at minimum add a link to `/tours/swamp/` and the Manchac tour page. | Confirmed still 0 links to `/tours/swamp/`, unchanged all day |
| 2 | `/alligators-vs-crocodiles/` | Add FAQPage schema to the existing Q&A content. | Unchanged, still open |
| 3 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 the blog-archive URL (boilerplate meta, zero schema) to the real tour page. | Unchanged, still open |
| 4 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/` — or better, into the new Post 1 once published (`Internal Linking Audit.md` already recommends this exact redirect target). | Unchanged, still open; now has a clear final destination once Post 1 ships |
| 5 | `/`, Manchac page, Honey Island real tour page, other tour pages | Add AggregateRating (homepage) and Product+Offer+AggregateRating (tour pages). | Unchanged; confirmed today Honey Island's real tour page has the identical gap as Manchac's |
| 6 | `SEO Content/Post 1-5` + `Marketing/Blog Drafts - Staged/` (11 drafts) | David reviews and approves for publish. Resolve the two overlapping-topic pairs (airboat-vs-kayak, first-time-kayak) down to one draft each first. | **New this pass** — this is the single highest-leverage quick win found today: it turns three "strategic, multi-week" items into a publish-approval decision |
| 7 | `~/.claude/.env` | Add `PSI_KEY` (David generates at Google Cloud Console). | Unchanged, still blocking fresh Core Web Vitals data |

### Strategic Work (this quarter)

| # | Page/URL | Exact change | Status |
|---|---|---|---|
| 8 | `/tours/swamp/` | Rebuild as the true money page — largely superseded by Post 1 in `SEO Content/`, which already covers price, duration, comparison content, and FAQ schema per the plan. Publish Post 1 at its own slug and 301/merge `/tours/swamp/` into it, or port Post 1's content into `/tours/swamp/` directly (David's call on URL strategy — Post 1 was drafted as a blog slug, `/tours/swamp/` is the existing indexed page). | Reframed — was "build," now "decide how to ship what's already written" |
| 9 | New page: `/alligator-tour-new-orleans/` | Still genuinely unbuilt — no draft exists for this specific commercial page (the alligator-safety draft is informational, not a booking-page play on this keyword). | Unchanged, still open |
| 10 | Kayak vs. airboat comparison | Two drafts exist (May 6 + Aug 14). Pick one, publish it. | Reframed — was "build," now "choose and publish" |
| 11 | Manchac haunted-swamp pillar | 2 of the ~3-4 planned pieces already drafted (haunted-manchac-swamp-legend, haunted-swamp-tours-near-new-orleans, June 13). Publish and see what's still missing from the pillar. | Reframed — largely drafted, not unbuilt |
| 12 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite every section to end with a paid-tour CTA. No draft exists for this — it's an edit to a live page, not a new post. | Unchanged, still genuinely open |
| 13 | "How much does a swamp tour cost?" page | Drafted today (`how-much-does-a-swamp-tour-cost-new-orleans.md`, content-gate 90/100). | Reframed — was "build," now "publish" |
| 14 | OTA listings (GetYourGuide/TripAdvisor/Viator) rewrite | Still open, no draft exists, needs to happen off-site. | Unchanged |
| 15 | GBP category + duplicate-listing cleanup | Still needs a live GBP check, MCP still down. | Unchanged |
| 16 | Crescent City Kayak property decision | Still open, still undecided. | Unchanged |

---

## Notes

- All HTTP/schema/link checks in §2 were independently re-run this session via direct HTTP requests (Python urllib + regex JSON-LD parsing), not copied from either prior audit — results matched.
- §3 is genuinely new ground: neither prior audit today looked inside `Marketing/Blog Drafts - Staged/` or `SEO Content/`. This is the most actionable finding of the day — David has roughly 16 blog-length assets sitting ready for review, several of which directly close "Strategic Work" gaps both earlier audits described as needing net-new research and writing.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in producing this report.
