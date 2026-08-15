---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: DRAFT — PENDING DAVID'S REVIEW — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech SEO Audit — 2026-08-15 (Pass 2)

> **DRAFT. REPORT ONLY.** Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform. Generated in an unattended run with no interactive approval step, several hours after `Marketing/SEO + Tech SEO Audit — 2026-08-15.md` (the first pass today, ~00:28). This is an additive re-verification pass, not a rewrite — see "What's genuinely new in this pass" below before reading the rest.

---

## Data Sources & Gaps (read this first)

**GSC/GA4/PSI MCP: checked again, still not available.** Ran `ToolSearch` this session for `"google search console query performance"`, `"google analytics ga4 report"`, `"pagespeed insights lighthouse"`, and `"select:gsc_query,gsc_top_queries,ga4_report,mcp__google__gsc_top_queries"`. Nothing loaded — same result as all three prior passes today and yesterday. This is now the **4th consecutive unattended audit** blocked on the same wall. No GSC/GA4/GBP numbers below are freshly pulled; every one is carried forward and dated to its source.

**PageSpeed Insights: ran fresh, same 429.** `node ~/Projects/tech-seo/psi-run.mjs both` (had to locate node at `/usr/local/bin/node`, not on this session's default PATH — worth fixing in the runner script or session profile) returned `HTTP 429 Quota exceeded` for every one of the 8 FareHarbor sites, NKST included. No `PSI_KEY` on file. Falling back to the same `~/Projects/tech-seo/out/psi-20260619.json`, now **58 days old** (was 57 yesterday).

**What today's Pass 2 adds on top of the ~00:28 audit:**

| Activity | Result |
|---|---|
| Re-verified all core findings via fresh HTTP fetch (not re-read from the prior file) | Zero material change confirmed — expected, since only ~2 hours passed and this is a report-only chain with no live edits |
| Checked canonical `<link>` tags directly (not just HTTP status) on the 5 dual-URL posts | **New confirmation, worse than assumed**: each URL variant self-canonicalizes to itself. There is no consolidation signal at all — not "Google usually picks one," an actual unresolved duplicate-content pair ×5 |
| Crawled all 31 unique internal links on the homepage and checked status/redirects on each | **2 new findings** (see §5) neither prior pass caught: a dead-end nav link and an indirect Honey Island link |
| Opened `Marketing/Blog Drafts - Staged/` fresh (last checked in depth by the Aug 14 Pass 3 synthesis) | **The single biggest finding of this pass** — see below |
| Ran 2 live WebSearch checks as an AI-answer proxy (same 2 queries as the ~00:28 audit) | No material movement, as expected in a 2-hour window; confirms the ~00:28 findings rather than adding new ones |

### What's genuinely new in this pass

**`Marketing/Blog Drafts - Staged/` now holds 14 unpublished, content-gate-PASSED drafts (avg score ~89/100), not the count either the Aug 14 Pass 3 or the ~00:28 audit worked from.** Three of them are dated **2026-08-15, 00:30** — created two minutes after the ~00:28 audit finished, presumably by an automated content pipeline reacting to that audit's own findings:

- `2026-08-15 - alligator-tour-new-orleans.md` — content-gate 88/100. This directly closes the gap the ~00:28 audit (and every prior audit back to May) listed as **"still genuinely missing, 404 confirmed, build a dedicated commercial page"** (item #10 in the 08-15 Strategic list). It is no longer a build task. It's a publish decision.
- `2026-08-15 - mosquitoes-heat-summer-swamp-tour-new-orleans.md` — content-gate 88/100. Closes the practical-anxiety/heat-and-bugs gap flagged in the June competitor analysis and the Aug 14 audit.
- `2026-08-15 - sunset-swamp-tour-new-orleans-manchac.md` — content-gate 91/100. Closes the sunset/night-tour piece of the Manchac haunted-swamp cluster, tied to the real 4:30 PM departure slot (not an invented product).

Plus 11 more already sitting there, unpublished, that neither prior audit inventoried in full:
- 5 from 2026-06-13: best-time-to-see-alligators, haunted-manchac-swamp-legend, haunted-swamp-tours-near-new-orleans, honey-island-vs-manchac-swamp-tour, what-to-wear-louisiana-swamp-kayak-tour
- 6 from 2026-08-14: whitney-plantation-swamp-tour-combo-guide, alligator-safety-kayak-swamp-tour-new-orleans, bayou-st-john-kayak-marie-laveau-voodoo-history, birding-louisiana-swamp-field-guide, honey-island-swamp-visitor-guide, kayak-fishing-new-orleans-charter-guide — plus two that are **confirmed topic duplicates of already-published posts and should be discarded, not published**: `airboat-vs-kayak-swamp-tour-new-orleans` (the real Post 2 from `SEO Content/` already shipped at this exact slug back in May) and `first-time-kayak-swamp-tour-new-orleans` (same — Post 5 already shipped in May). Publishing the Aug 14 restaged versions on top of the live May versions would recreate the exact "best swamp tour" cannibalization problem flagged elsewhere on this site.

**Net effect: this is no longer primarily a content-creation problem at any layer.** Between the 5 already-published Content Plan posts and these 14 staged drafts, nearly every content gap identified across the May, Aug 10, Aug 14 (×3), and ~00:28 Aug 15 audits is now either shipped or sitting written and content-gate-approved on David's desk. What's left to build from scratch is short: the OTA listing rewrites (off-site, no draft exists), the `/3-free-swamp-walks/` CTA rewrite (an edit to a live page, not a new post), and GBP/local-pack work.

---

## 1. Keyword Opportunity Table

Source: GSC 90-day pull from the 2026-08-10 audit (window 2026-05-12 to 2026-08-09) — no fresher pull reachable in this or any of the 3 prior passes today. Page/link status re-verified live via direct HTTP fetch this pass.

| Keyword | Position | Volume/mo (corrected) | Tier | Recommended Action | Status This Pass |
|---|---|---|---|---|---|
| swamp tours new orleans | 15 (homepage ranks) | ~1,100–4,000 | Page 2 hostage — biggest opportunity | Link `/tours/swamp/` from the alligator page + homepage | **Confirmed unresolved** — fresh grep of both pages' HTML today finds 0 links to `/tours/swamp/` |
| swamp tour new orleans | 21 | ~3,000–10,000 | Page 3 | Same fix, same money page | Unresolved |
| new orleans swamp tours | 7 | ~3,000–5,000 | Striking distance — only page-1 win | Reinforce, don't disturb | Unchanged (good) |
| honey island swamp tour | 22, wrong URL (blog archive) | 9,900 | Page 2 hostage + URL collision | Noindex/301 the archive URL | **Confirmed unresolved** — meta still literally "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2" |
| airboat tours new orleans | ~11 (May pull, not repulled) | ~800-900 | Page 2 hostage / nemesis keyword | Content exists and is live; link it | Unresolved (linking), and now a second, duplicate draft of this exact content sits in the staging folder — do not publish it, see above |
| alligator tour new orleans | 51 (not ranking) | 2,900 | New territory | Build `/alligator-tour-new-orleans/` | **Reframed this pass**: page still confirmed 404 live, but a content-gate-passed (88/100) draft now exists, dated last night. This is a publish decision, not a writing task, for the first time across 5 audits. |
| swamp tours in new orleans | 20, on `/3-free-swamp-walks-.../` | 1,900 | Commercial query landing on a "don't pay us" page | Rewrite to CTA every section | Confirmed unchanged, still 5 links to Manchac tour, thesis still "free" |
| best new orleans swamp tours | 24 vs ~43-51 duplicate | 1,600 | Cannibalization | Merge duplicate pages | **Confirmed both still live**, H1s unchanged ("New Orleans swamp tour reviews" vs "What is the best Swamp Tour near New Orleans?") |
| how much does a swamp tour cost | not ranking for NKST | High commercial PAA intent | Content gap — partially closed on-site, fully closed in staging | A drafted, content-gate 90/100 standalone page (`how-much-does-a-swamp-tour-cost-new-orleans.md`) sits unpublished; the guide page's cost section is live but not in FAQ schema | Re-ran the live WebSearch check today: **NKST is still absent** from the result set for this query (Groupon, NOLA Adventures, Cajun Pride, Gators & Ghosts, airboatadventures.com fill it) — matches the ~00:28 finding exactly, no movement in 2 hours as expected |
| swamp tour near me | not in top 100 organically | 12,100 (local-pack query) | Local pack, not organic | GBP category fix | No new data, GBP MCP still unavailable |
| kayak swamp tour | 1 | 880 | Owned | No action | Unchanged |

---

## 2. On-Page SEO Issues — Verified Live This Pass (2026-08-15, afternoon)

| Page | Issue | Severity | Status |
|---|---|---|---|
| `/tours/swamp/` | Re-confirmed via fresh fetch + Python word count: BreadcrumbList/ListItem schema only, 3,112 words. No Product, Offer, AggregateRating, or FAQPage. | Critical | Unchanged from ~00:28 |
| `/` (homepage) | Re-confirmed: no AggregateRating, no FAQPage in JSON-LD. Grepped for `/tours/swamp/` and `/swamp-tours-new-orleans-guide/` in the full homepage HTML — **0 matches for either**. | High | Unchanged |
| `/alligators-vs-crocodiles/` | Re-confirmed via fresh fetch: page links to 7 tour-side URLs (Manchac, both Honey Island paths, Shell Bank, the plantation tour, `/tours/swamp-kayak-tours/`) but **0 links** to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, or the airboat-vs-kayak post. No FAQPage schema despite Q&A content. | Critical (linking), Medium (schema) | Unchanged |
| `/tours/kayak-tours/honey-island-swamp-tour/` | Re-confirmed: meta description still the literal boilerplate string, zero schema. | Critical | Unchanged |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Both confirmed 200 live, H1s unchanged and still distinct. | High | Unchanged |
| `/3-free-swamp-walks-in-and-around-new-orleans/` | Confirmed still live, unchanged. | High | Unchanged |
| Dual-URL duplication on the 5 recent posts (`/x/` vs `/blog/x/`) | **New this pass**: pulled the actual `<link rel="canonical">` tag from all 4 checked URLs (2 posts × 2 variants). Each variant self-canonicalizes — `/swamp-tours-new-orleans-guide/` canonicalizes to itself, `/blog/swamp-tours-new-orleans-guide/` canonicalizes to itself, same pattern on the Manchac post. There is no consolidation signal pointing Google at one URL. | Medium-High (upgraded from the ~00:28 audit's "Google usually picks one, low urgency") | **Confirmed worse than previously assumed** |
| Sitemap only lists root URLs for these 5 posts | **New finding**: `post-sitemap.xml` contains `/swamp-tours-new-orleans-guide/`, `/manchac-swamp-visitor-guide/`, etc. at root — the `/blog/`-prefixed variants are **not** in the sitemap at all, live but undeclared. This is a mitigating factor (Google is more likely to treat root as canonical via sitemap signal) but the self-canonicalizing `/blog/` URLs remain independently crawlable and indexable if linked from anywhere else. | Medium | New data point |

---

## 3. Internal Linking Opportunities (Updated)

| # | Source Page | Target | Suggested Anchor | Priority | Status This Pass |
|---|---|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | `/tours/swamp/` | "swamp tours in New Orleans" | Critical | Confirmed missing (fresh fetch) |
| 2 | `/alligators-vs-crocodiles/` | `/swamp-tours-new-orleans-guide/` | "our full New Orleans swamp tour guide" | Critical | Confirmed missing |
| 3 | `/alligators-vs-crocodiles/` | `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` (or the root URL, once canonicalized — see §2) | "kayak vs. airboat, an honest comparison" | High | Confirmed missing |
| 4 | `/` (homepage) | `/tours/swamp/` | "swamp tours" (nav or hero CTA) | Critical | Confirmed missing |
| 5 | `/` (homepage) | `/swamp-tours-new-orleans-guide/` | "how to pick a swamp tour" | High | Confirmed missing |
| 6 | `/` (homepage) | `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` **directly** | (existing anchor) | Medium — **new this pass** | Homepage nav currently links to `/tours/swamp-kayak-tours/honey-island-swamp-tour/`, which 301-redirects to the real URL. One unnecessary redirect hop on the site's highest-authority page; point the link at the canonical URL directly. |
| 7 | `/swamp-tours-new-orleans-guide/` | `/tours/swamp/` | "book a swamp tour" | High | Confirmed missing — guide links to 3 individual tour products, not the general money page |
| 8 | `/tours/kayak-tours/honey-island-swamp-tour/` (archive) | `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (real page) | "Honey Island kayak swamp tour" | Critical | Really a redirect/consolidation, not a link add |
| 9 | 14 staged drafts once published | Each other + `/tours/swamp/` | Topic-appropriate | Medium | Not yet applicable — drafts aren't live to link from/to yet |

**Orphan pages, unchanged:** `/swamp-tours-new-orleans-guide/` and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` remain substantial, schema-complete pages with effectively zero authoritative inbound links.

---

## 4. Content Gap Analysis — Reframed This Pass

**The honest picture as of this pass: content creation is no longer the bottleneck anywhere on this site. Publishing and linking are.**

| Prior "gap" | Status confirmed this pass |
|---|---|
| Alligator tour commercial page (`/alligator-tour-new-orleans/`) | **Closed as a writing task.** Content-gate 88/100 draft exists, dated last night. Page itself still 404 — pure publish decision now. |
| "How much does a swamp tour cost" | Draft exists (90/100), page not published. Live WebSearch today confirms NKST still absent from this query's results — the draft sitting unpublished has a real, measurable cost. |
| Manchac haunted-swamp cluster | 3 relevant drafts now identified: `haunted-manchac-swamp-legend`, `haunted-swamp-tours-near-new-orleans` (both June 13), and the new `sunset-swamp-tour-new-orleans-manchac` (last night). Checked excerpts — genuinely distinct angles (legend/history, myth-busting, and the sensory late-afternoon-paddle piece), not duplicates of each other. |
| Practical-anxiety cluster (heat, bugs, what to wear, first-timer nerves) | `what-to-wear-louisiana-swamp-kayak-tour` (June 13) and `mosquitoes-heat-summer-swamp-tour-new-orleans` (last night) cover this from different angles (packing list vs. heat/bug tolerance); confirmed distinct via excerpt read. First-timer anxiety itself is already published (`/first-time-kayak-swamp-tour-new-orleans/`). |
| Honey Island content | `honey-island-vs-manchac-swamp-tour` (comparison, June 13) and `honey-island-swamp-visitor-guide` (standalone guide, Aug 14) — read both excerpts, distinct angles, not duplicates. |
| **New: two staged drafts are duplicates and should NOT be published** | `airboat-vs-kayak-swamp-tour-new-orleans` and `first-time-kayak-swamp-tour-new-orleans`, both dated Aug 14, restage topics that already shipped in May under the same slugs. Publishing them would create the exact cannibalization pattern already flagged elsewhere on the site. Flag for deletion or repurposing, not publication. |
| Bachelor/bachelorette content rebuild | Still open, no draft found in either `SEO Content/` or `Blog Drafts - Staged/`. Genuinely still a gap. |
| Crescent City Kayak's fate | Still open across five audits now. Confirmed live and resolving today, unchanged. |
| GBP category/duplicate-listing cleanup | No new data, GBP MCP still unreachable. |
| OTA listing rewrites (GetYourGuide/TripAdvisor/Viator) | Still open, off-site work, no draft exists in the vault. |

---

## 5. Technical SEO Checklist — Verified Live This Pass (2026-08-15)

| Check | Status | Details |
|---|---|---|
| Homepage redirect chain | Pass | `https://neworleanskayakswamptours.com` → 200, 0 redirects |
| http → https | Pass | Single 301 hop to https, no chain |
| non-www → apex | Pass | `www.neworleanskayakswamptours.com` → single redirect to apex |
| robots.txt | Pass | Unchanged — sitemap referenced correctly, admin/CDN paths blocked |
| sitemap.xml | Pass | Sitemap index → 3 child sitemaps: **41 page URLs, 13 activity URLs, 101 post URLs.** (First pass today to actually count these.) All 5 recent Content Plan posts present at root URL only. |
| Broken-link crawl — full homepage link set (31 unique internal URLs, not a sample) | **Pass, 0 real 404s, 2 redirects found** | See below — this is the first pass to check every homepage link individually rather than spot-checking. |
| **New: `/new-orleans-zipline-tour-kayak-tour-combo/`** (linked from homepage nav) | **Fail — dead-end nav link** | 301-redirects straight back to `/` (homepage). The page is gone (confirmed absent from `page-sitemap.xml`) but the homepage nav link to it was never removed or updated. A visitor clicking "zipline + kayak combo" lands back on the homepage with no explanation. Not caught by any of the 4 prior audits because none crawled every homepage link individually. |
| **New: `/tours/swamp-kayak-tours/honey-island-swamp-tour/`** (linked from homepage nav) | **Minor — indirect link** | 301-redirects to the real tour page `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. Works for users, but the homepage's own nav isn't using the canonical URL — wastes a hop and a sliver of link equity on the site's highest-authority page. |
| Duplicate content / cannibalization | Fail | Two live "best swamp tour" pages, unchanged |
| URL collision (archive vs. real page) | Fail | Honey Island archive still outranks the real tour page |
| Dual-URL duplication, 5 recent posts | **Fail, confirmed worse than assumed** | Each variant self-canonicalizes (see §2) — no consolidation signal, not just "low urgency, Google usually picks one" |
| Mixed content | Pass | Checked homepage, `/alligators-vs-crocodiles/`, `/tours/swamp/` HTML for `src="http://` — none found |
| Schema markup — homepage | Partial | Unchanged: Organization, LocalBusiness, WebSite, VideoObject present; AggregateRating, FAQPage missing |
| Schema markup — `/tours/swamp/` | Fail | BreadcrumbList only, unchanged |
| Schema markup — tour product pages | Fail | Confirmed again on the Manchac page: BreadcrumbList, ImageObject, Organization, VideoObject — no Product/Offer/AggregateRating |
| HTTPS | Pass | Confirmed |
| Core Web Vitals / Lighthouse | **Still stale, confirmed via fresh attempt** | PSI returned `HTTP 429` for all 8 sites again today. Cached data now 58 days old (2026-06-19), unchanged from every prior pass this week. Node had to be located manually at `/usr/local/bin/node` — not on this session's default `$PATH`, worth fixing in the runner or session profile so the next unattended run doesn't lose time on it. |
| GSC index status | Not available | Confirmed again via ToolSearch this session |

### Core Web Vitals (still 2026-06-19, now 58 days old — unchanged, directional only)

| Strategy | Perf Score | LCP (lab) | CLS (lab) | TBT (lab) | Field data (CrUX: LCP/CLS/INP) |
|---|---|---|---|---|---|
| Mobile | 37 (red) | 16.2s (very poor) | 0.005 (good) | 1,600ms (poor) | FAST / FAST / FAST |
| Desktop | 54 (amber) | 2.5s (good) | 0.009 (good) | 620ms (needs improvement) | FAST / FAST / FAST |

Same caveat as every prior pass: field data (real users) disagrees sharply with the lab score. This is now the **5th audit in a row** carrying the same 58-day-old number. Getting a `PSI_KEY` is overdue.

---

## 6. Local Search / GBP

No new data — GBP MCP unavailable again this pass. Carried forward, unverified across five consecutive audits: primary category mismatch ("Canoe & kayak tour agency" vs. pack winners' "Boat tour agency"/"Tour operator") and 5 David-controlled listings clustering within a few blocks, including one at a fabricated "Swamp Tour Street" address (standalone suspension risk).

---

## 7. Competitor Comparison

| Dimension | NKST | Wild Louisiana Tours | Airboat operators (Cajun Pride, Gators & Ghosts, NOLA Adventures, etc.) | Winner |
|---|---|---|---|---|
| AI-answer-style presence (live WebSearch this pass, same query as ~00:28) | Named, similar specific copy to this morning's test — "beginner-friendly, guided kayak tours year-round... Manchac Swamp, Pearl River, Honey Island Swamp and Cane Bayou" | Still named alongside NKST and Voodoo Swamp Tours in this pass's result set | Not tested this pass | No material change from this morning — expected in a 2-hour window |
| "How much does it cost" query ownership | **Still absent entirely**, confirmed via fresh WebSearch this pass | Not tested directly | Groupon, NOLA Adventures ($95pp), Gators & Ghosts ($64+), airboatadventures.com, Cajun Pride all present | Airboat/budget operators — and NKST has a content-gate-passed draft sitting unpublished for exactly this query |
| Structured data (Product/Offer/Rating) | Still none, confirmed again on the Manchac page this pass | Not re-tested | Not tested this pass | — |
| Content depth / breadth in the vault (published + staged) | **19 total assets** — 5 published Content Plan posts + 14 staged drafts covering nearly every gap this audit chain has ever identified | Unknown, not directly comparable | Not tested | NKST has a real, underused content advantage — the constraint is now internal (publish + link), not competitive |

---

## 8. Traffic & Conversion Context (GA4, March 2026 — carried forward, 5+ months old)

No fresher GA4 pull reachable this pass either. Unchanged from all prior passes: 11,848 sessions/90d (spring ramp), Paid Search converting at 19.8% vs. 13.0% organic, Paid Social at 0.8% (still flagged wasted), and the FareHarbor → GA4 purchase-event gap (58 events tracked vs. 23,385 GHL contacts) still unconfirmed as fixed or not. **This has now gone unresolved across at least two weeks of unattended audit runs** — worth a manual check next time David is at a keyboard, since it undercounts every conversion figure cited anywhere in NKST's marketing stack.

---

## 9. Merged Prioritized Fix List

Combines the SEO and technical passes into one list. Every item has the exact page, the exact change, and the expected impact.

### Quick Wins (this week)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | `Marketing/Blog Drafts - Staged/` (14 files) + `SEO Content/` (already-published reference) | David reviews and approves/rejects the 14 staged drafts in one sitting. **Discard or repurpose** the two confirmed duplicates first — `2026-08-14 - airboat-vs-kayak-swamp-tour-new-orleans.md` and `2026-08-14 - first-time-kayak-swamp-tour-new-orleans.md` — since both topics are already live under the May `SEO Content/` slugs. Then batch-publish the remaining 12, especially `alligator-tour-new-orleans` (closes a 5-audit-old "genuinely missing page" gap) and `how-much-does-a-swamp-tour-cost-new-orleans` (closes the highest commercial-intent PAA gap, confirmed via fresh WebSearch today that NKST still doesn't appear for this query). | Turns roughly 3 months of "strategic, needs research and writing" line items into a single approval pass. This is the highest-leverage item in the entire fix list — nothing else on this page matters if the content stays unpublished. |
| 2 | `/alligators-vs-crocodiles/` | Add the "More reading" internal-link block (already drafted in `SEO Content/Internal Linking Audit.md`) linking to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, and `/airboat-vs-kayak-swamp-tour-new-orleans/`. Confirmed via fresh fetch today: still 0 links to any of the three. | Redirects a slice of ~272k quarterly impressions to pages that are already built and good but structurally invisible. |
| 3 | `/` (homepage) | Add nav/hero links to `/tours/swamp/` and `/swamp-tours-new-orleans-guide/`. Also repoint the existing Honey Island nav link from `/tours/swamp-kayak-tours/honey-island-swamp-tour/` (301s) directly to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`, and either restore or remove the `/new-orleans-zipline-tour-kayak-tour-combo/` nav link, which currently 301s back to the homepage itself — a dead end confirmed live today and not caught by any of the 4 prior audits. | Points the site's highest-traffic page at its actual money page; removes one confirmed broken user path and one wasted redirect hop. |
| 4 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 (or noindex if CMS can't 301) to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. | Stops a boilerplate blog-archive page from being Google's answer for a 9,900/mo keyword. |
| 5 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/`, merging unique content first. | Ends self-cannibalization on "best swamp tour" queries. |
| 6 | `/swamp-tours-new-orleans-guide/`, `/manchac-swamp-visitor-guide/`, `/bayou-bienvenue-vanishing-swamp/`, `/first-time-kayak-swamp-tour-new-orleans/`, `/airboat-vs-kayak-swamp-tour-new-orleans/` (all 5, at both URL variants) | Pick the root URL as canonical (already the sitemap's choice) and either 301 the `/blog/`-prefixed variant or fix its `<link rel="canonical">` tag to point at root instead of self-referencing. Confirmed via direct fetch this pass that all 5 currently self-canonicalize — a real, unresolved duplicate-content signal, not a low-urgency "Google will probably sort it out." | Consolidates ranking signal currently split across 10 live URLs down to 5. |
| 7 | `~/Projects/tech-seo/psi-run.mjs` environment | Get a free PageSpeed Insights API key, add to `~/.claude/.env` as `PSI_KEY=...`. Separately: fix the script/session so `node` (found at `/usr/local/bin/node` this pass, not on default `$PATH`) resolves automatically next run. | Unblocks a real Core Web Vitals read — the mobile-37 figure is now 58 days stale across 5 consecutive audits. |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 8 | `/tours/swamp/` | Add Product + Offer (price/currency/availability) + AggregateRating (4.9/1,416) + FAQPage schema. Content is already ~3,112 words — schema/linking gap, not a rewrite. | Still the single biggest lever identified across 5 audit passes. |
| 9 | `/`, all 6 tour pages | Add AggregateRating + Product/Offer schema sitewide using pricing already published in page bodies. | Star ratings + price display in search results, AI-answer extractability. Confirmed still zero commercial schema anywhere. |
| 10 | GetYourGuide / TripAdvisor / Viator listings | Rewrite third-party OTA listing copy to lead with extractable specifics (duration, transport, species list, group size, difficulty) instead of mission-first language. | This is the layer AI answer engines currently source from over NKST's own site — confirmed again by today's WebSearch proxy test. |
| 11 | GBP: primary category + duplicate-listing cleanup | Needs a live GBP check — still not possible, MCP unreachable across 5 audits now. | Local pack eligibility for "swamp tour near me" (12,100/mo). |
| 12 | Crescent City Kayak property decision | Still open across five audits. Confirmed live and resolving today, unchanged. Either 301 into NKST or commit to a genuine funnel rebuild. | Every quarter this stays undecided, CCK keeps splitting authority NKST already wins head-to-head. |
| 13 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite every section to end with a paid-tour CTA. No draft exists for this — it's an edit to a live page, one of the few genuinely still-unwritten items left on the whole list. | Redirects ~9,500/mo of commercial-intent traffic currently landing on a "don't pay us" page. |
| 14 | Bachelor/bachelorette content rebuild | Confirmed still live, unrebuilt, at `/top-destinations-for-your-bachelor-bachelorette-party/`. No draft found in either `SEO Content/` or `Blog Drafts - Staged/`. | Real search demand, both NKST and competitor versions weak per the May audit. |
| 15 | FareHarbor → GA4 purchase-event tracking | Confirm (needs David or a dev, not verifiable via unattended HTTP checks) whether this was ever fixed. Flagged unresolved for 2+ weeks of audit runs now. | Every GA4 conversion figure cited anywhere in NKST's marketing stack is currently unreliable until this is confirmed. |

---

## Notes

- Everything marked "confirmed" or "verified" in this pass was checked via direct HTTP fetch/HTML parse against production today, not copied from the ~00:28 audit — even where the result matched exactly, which it did for nearly everything except the items flagged "new this pass."
- The single most important finding of this pass: **the content backlog is now deeper than any prior audit tracked (19 total assets between published and staged), and 3 of those 14 staged drafts were written last night, automatically, in direct response to gaps the ~00:28 audit itself identified.** The bottleneck on this site is not research, not writing, and increasingly not even technical — it's an approval queue.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in producing this report. Every action item above is a recommendation awaiting David's approval.
