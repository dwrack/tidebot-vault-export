# Austin Kayak Tours — SEO + Tech-SEO Audit (2026-08-14)

**This is a report only. No changes were made to the live site, WordPress, GBP, ads, or any file outside this document.** Everything below is a finding or a recommendation for David/Connor/dev to act on later.

## Data sources used this session

- **Live site crawl** — direct `curl` against `https://www.austinkayaktours.com` (homepage, all 13 activity pages, all 9 static pages, robots.txt, and all 3 sitemap files) run today, 2026-08-14.
- **Vault docs** — `Marketing/SEO Action Plan & Blog Pipeline.md` (2026-05-09), `Marketing/Ranking Baseline 2026-06-07.md`, `Marketing/SEO Content/01 - Title & Meta Rewrites.md`, `Marketing/SEO Content/02 - Schema Markup Library.md`, `Marketing/SEO Content/04 - Internal Linking Map.md`, `AI-SEO-Bat-Tours-Action-Plan.md` (2026-06-09), `Marketing/Blog Drafts - Staged/`.
- **Web search** — spot-check of current SERP for head terms and competitor landscape.
- **PageSpeed Insights API** — attempted, returned HTTP 429 (daily quota already exhausted on this Google Cloud project before this session ran). No fresh Core Web Vitals/Lighthouse numbers this session.

**GSC and GA4 were NOT available this session.** This vault's `.mcp.json` only has `google-austin`, `gbp`, `meta-organic`, `playwright`, `opencx`, and `clarity` — no Search Console or Analytics connector. Every position/impression/CTR number below is carried over from the `Ranking Baseline 2026-06-07.md` snapshot (itself pulled from GSC on 2026-06-07, sourced from the legacy `lonestarkayaktours.com` property before the rebrand) — it is **10 weeks stale**, not live. Treat the keyword table as directional, not current. Recommend connecting a GSC MCP before the next audit so this can be a real 90-day pull.

---

## Executive Summary

The biggest thing this audit found isn't a missing meta tag, it's that **the old brand domain, lonestarkayaktours.com, is still fully live, indexable, and self-canonicalizing** — it never got redirected to austinkayaktours.com despite the May 9 action plan calling for exactly that. It's showing up in live Google results next to the new domain right now. That's likely suppressing rankings on the new domain more than any on-page issue on this list. Fix that first.

Second finding: a lot of the May/June on-page work already shipped. Titles, meta descriptions, and the rental page H1 mostly match (or beat) what the vault docs proposed, and the bat tour page already has FAQPage schema live. Good progress, don't redo it.

Third finding: several of the vault's own SEO docs (the Internal Linking Map, some of the Title & Meta Rewrites) reference URLs that don't exist on the live site — guessed slugs like `/sunrise-tour/`, `/sunset-skyline-tour/`, `/about-us/`, `/paddle-board-lessons/` all 404, and the page called out as the "biggest link-equity leak" (`/blog/skyline/`) is actually a tag archive, not an editable blog post. Those docs need a reconciliation pass against the real site before anyone tries to execute them literally.

Top 3 priorities by impact: (1) resolve the lonestarkayaktours.com duplicate-domain problem, (2) fix the duplicate-URL/canonical issue on paddleboard-tour and corporate-events pages, (3) publish the internal-linking and schema fixes that are still genuinely outstanding (FAQ page schema, homepage LocalBusiness schema, the two pillar pages that are drafted but not live).

---

## Technical SEO Findings

### Critical

| Check | Status | Details |
|---|---|---|
| Legacy domain redirect | **FAIL** | `lonestarkayaktours.com` returns HTTP 200 with its own title ("Lone Star Kayak Tours \| Kayak Tours in Austin, TX"), own meta description, self-referencing canonical (`https://lonestarkayaktours.com/`), `<meta name="robots" content="index,follow">`, and its own `robots.txt` + `sitemap.xml`. It is a fully live, independently indexable duplicate of this business, not a parked domain. Confirmed via WebSearch: it appears as its own result in live Google search alongside austinkayaktours.com for branded/near-branded queries today. The 2026-05-09 action plan's Week-1 task #4 ("build per-page 301 map lonestarkayaktours.com → austinkayaktours.com") was never executed. |
| Duplicate URLs, same content | **FAIL** | `/paddleboard-tour/` and `/austin-kayak-tours/paddleboard-tour/` both return HTTP 200, each with its own self-referencing canonical tag (not a redirect pair). Same pattern on `/corporate-events/` vs `/austin-kayak-tours/corporate-events/`. Two live, independently indexable URLs per tour. |
| robots.txt | PASS | Valid, allows all major crawlers including AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended not blocked). Disallows `/edit/`, `/fhbr-console/`, `/cdn-cgi/`, and a long list of low-value scraper bots. References sitemap correctly. |
| sitemap.xml | PASS (structurally) | Valid sitemap index at `https://www.austinkayaktours.com/sitemap.xml` referencing `page-sitemap.xml` (9 URLs), `activity-sitemap.xml` (13 URLs), `post-sitemap.xml` (57 URLs). All spot-checked URLs returned 200. |
| Core Web Vitals / Lighthouse | **NOT AVAILABLE** | PageSpeed Insights API returned HTTP 429 (quota exceeded on the shared keyless project) both via direct API call and via `~/Projects/tech-seo/psi-run.mjs`. No `PSI_KEY` is configured in `~/.claude/.env`. Re-run tomorrow, or set up a PSI API key (free from Google Cloud Console) to stop this from blocking future audits. |
| GSC index status | **NOT AVAILABLE** | No GSC MCP connected this session. |

### Broken / dead URLs found

| URL tried | Status | Note |
|---|---|---|
| `/kayak-paddleboard-rental/` | 404 | Known bug, flagged in the May action plan (task #6), still not fixed. Real page is `/rental/`. |
| `/4th-of-july-fireworks-tour/` | 404 | Wrong slug — used in `01 - Title & Meta Rewrites.md` and `04 - Internal Linking Map.md`. Real live URL is `/austin-kayak-tours/fourth-of-july-tour/`. |
| `/sunrise-tour/` | 404 | Does not exist anywhere in the sitemap. There is no live "Sunrise Tour" product page at all — confirm with Connor/FareHarbor whether this is a real bookable product before writing any more content or schema for it. |
| `/sunset-skyline-tour/` | 404 | Does not exist. Likely conflated with the existing Austin Skyline Tour page, which already covers multiple daily time slots (10am/1pm/4pm per current copy). No separate sunset-specific landing page exists. |
| `/paddle-board-lessons/` | 404 | Does not exist yet. This is a "build it" item (month-3 plan), not a slug typo. |
| `/about-us/` | 404 | There is no About page on the live site at all — not at this slug or any other. Confirmed against the full 9-URL page-sitemap. This is a real trust/E-E-A-T gap, not just a broken link. |

### On-page audit of live pages (spot-checked directly, not from vault docs)

| Page | Title tag (live) | Meta description (live) | Notes |
|---|---|---|---|
| `/` | "Austin Kayak Tours on Lady Bird Lake \| From $50" | "Guided kayak tours of the downtown Austin skyline and the Congress Bridge bats, plus kayak and paddle board rentals from $20. Book Lady Bird Lake online." | Live, already updated since baseline. Homepage has 5 JSON-LD blocks (schema present, unlike what the May 9 audit assumed). H1 is "Austin Kayak Tours." |
| `/austin-kayak-tours/sunset-bat-bridge-kayak-tour/` | "Austin Bat Tour by Kayak \| See 1.5M Congress Bridge Bats" | Present, keyword-rich, includes price/season | FAQPage schema is live (confirmed: `FAQPage` string present in source). This matches Move 1 from the 2026-06-09 AI-SEO doc — it's done. |
| `/austin-kayak-tours/austin-skyline-tour/` | "Austin Skyline Kayak Tour \| Downtown from the Water" | Present, matches vault's proposed direction | H1 present: "Austin Skyline Tour." |
| `/rental/` | "Kayak & Paddle Board Rentals on Lady Bird Lake \| from $20" | Present | H1 now populated ("Kayak & Paddle Board Rentals on Lady Bird Lake") — the June baseline flagged this H1 as empty; it's fixed. |
| `/faq/` | "Frequently Asked Questions \| Austin Kayak Tours" | Present | **Zero FAQPage schema** despite real Q&A content on the page. This is the single highest-leverage schema gap left — bigger than the bat page ever was, because this page's entire content is FAQ pairs. |
| `/austin-kayak-tours/halloween-tour/` | "Halloween Kayak Tour in Austin \| Austin Kayak Tours" | Present | **Live money page with zero coverage anywhere in the vault's SEO docs** — not in the title/meta library, schema library, linking map, or the 50-post blog pipeline. |
| `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` | "All Day Skyline and Swimming Hole Tour \| Austin Kayak Tours" | Present | Same gap — a real, live, bookable product entirely absent from the SEO strategy. |

### "Biggest leak" page is not what the vault docs think it is

`Marketing/SEO Content/04 - Internal Linking Map.md` names `/blog/skyline/` as "8,965 imp/90d — biggest leak" and recommends adding mid-post CTA links "after the Frost Bank Tower paragraph." Live crawl shows `/blog/skyline/` is actually the **tag archive** page (title: "skyline Blog Tag \| Austin Kayak Tours \| Page 1 of 1") that lists every post tagged "skyline" — it is not a single editable article. You can't add a mid-post CTA to a tag archive the way WordPress renders it. If that page is genuinely pulling 8,965 impressions, the fix is different: either add an intro blurb block above the post list with a CTA link (some tag archive templates support this), or find whichever individual skyline-themed post is actually earning the impressions (candidate: `/blog/amazing-austin-architecture/`, which is in the live post-sitemap and matches the skyline/architecture topic) and treat that as the real target instead.

---

## Content & Keyword Findings

### Keyword opportunity table (source: GSC snapshot, 2026-06-07 — stale, directional only)

| Keyword | Position (6/7) | Impressions (90d) | Tier | Recommended Action |
|---|---|---|---|---|
| lady bird lake kayak rental | 46.7 | 10 | New Territory / weak | Rental page content was rebuilt June 7; re-pull GSC to see if this moved before investing more here |
| /rental/ page, all queries | 42.8 | 647 | Page 2 Hostage | Same — this is the page most likely to have moved since baseline; needs a fresh GSC pull before further action |
| austin bat tours (generic) | 23 | 3 | New Territory | Low impressions but generic term; bat-page rebuild (title/H1/FAQ/schema) shipped June 7 specifically to chase this — re-check |
| bat tours austin | 17 | 3 | New Territory | Same cluster, same caveat |
| austin bat kayak tour | 4.5 | 43 | Striking Distance (near top of page 1) | Already strong; protect with the FAQ schema now live |
| bat kayak tour austin | 4.6 | 62 | Striking Distance | Same |
| austin kayak tours | 2.5 | 124 | CTR Fix | Top 3 already; June baseline flagged CTR at half of benchmark — homepage title has since changed, worth re-checking CTR once GSC is connected |
| kayak austin | 6.3 | 442 | Striking Distance | High impressions, position 6 — a genuine near-term ranking opportunity if content/internal links are strengthened |
| austin kayak | 6.7 | 457 | Striking Distance | Same |
| austin kayaking | 10.4 | 438 | Page 2 Hostage | High impressions stuck just off page 1 |
| best place to kayak in austin | ~13 | 2,799 | **New Territory — biggest single opportunity on the list** | 2,799 impressions at position 13 with **zero clicks** as of the May 9 audit. No page currently targets this. The pillar page `/best-places-to-kayak-in-austin/` is drafted in the vault (`Pillars/01 - Best Places to Kayak in Austin.md`) but **not live on the site** — it doesn't appear in the page-sitemap. Publishing it is the single highest-ROI content move available. |

### Content gap recommendations

1. **Two pillar pages are fully drafted and not published.** `Marketing/SEO Content/Pillars/01 - Best Places to Kayak in Austin.md` and `Pillars/02 - Kayaking on Lady Bird Lake.md` exist in the vault, ready to go, targeting a combined 2,799+ impressions of unclaimed demand. Neither is in the live sitemap. This is publish-ready work sitting idle, not a content-creation gap.
2. **Cluster A is drafted (5 of 6 posts) and not published.** `Marketing/SEO Content/Cluster A - Lady Bird Lake/` has all 5 supporting posts written. None appear in the live post-sitemap (57 URLs checked, none match these titles/slugs).
3. **3 additional posts are staged outside the cluster folders** in `Marketing/Blog Drafts - Staged/` (bat bridge vs. water, Lady Bird Lake downtown guide, sunset kayaking in Austin) — also not live.
4. **No About page exists on the live site.** Zero E-E-A-T signal beyond the homepage. This matters more than usual because AI-answer engines and Google increasingly weight author/operator credibility — the `AI-SEO-Bat-Tours-Action-Plan.md` doc already flags "thin third-party presence" as the #1 long-term AI-citation gap, and having no About page compounds that on-site.
5. **Halloween Tour and All Day Skyline/Swimming Hole Tour have no supporting content, schema, or internal links anywhere.** Both are real bookable products getting zero SEO support.
6. **Competitive gap: clear/transparent kayak tours.** A WebSearch for "austin bat tour kayak lady bird lake best" surfaced multiple competitors (Get Up and Go Kayaking, and several TripAdvisor-listed operators) now offering "Clear Kayak Tours" / "Crystal Kayak Tours" on Lady Bird Lake — a trend AKT doesn't participate in or address in content. Even without adding the product, a comparison post ("clear kayak vs. regular kayak tour on Lady Bird Lake") could intercept that search interest and funnel it to AKT's existing tours.
7. **Competitor set (from live search + prior AI-SEO audit):** Live Love Paddle, Boats and Bats, Get Up and Go Kayaking, Congress Bridge Bats, and confusingly, **lonestarkayaktours.com competing against itself** (see Technical Findings above). Congress Bridge Bats shows no visible price on its bat tour page; AKT's bat page already beats it on that dimension. Boats and Bats and Live Love Paddle both have dedicated kayaking guide/blog content actively targeting the same head terms AKT is chasing.

### Internal linking — corrected recommendations

The vault's `04 - Internal Linking Map.md` is mostly sound but has two stale-URL issues corrected below. Everything else in that doc (dog-friendly post → rental, bachelorette post → corporate events, homepage "Learn More" CTA replacement, etc.) is still valid and not yet done — see Action Plan below.

| Source page (live, confirmed) | Target money page | Anchor | Status |
|---|---|---|---|
| `/blog/skyline/` is a tag archive, not a post — see Technical Findings | `/austin-kayak-tours/austin-skyline-tour/` | "guided Austin skyline kayak tour" | **Needs a different execution path than the vault doc describes** — target the archive intro block or retarget to `/blog/amazing-austin-architecture/` (verify which one carries the impressions once GSC is connected) |
| `/blog/some-reasons-to-check-out-the-south-congress-bat-colony/` (confirmed live, in post-sitemap) | `/austin-kayak-tours/sunset-bat-bridge-kayak-tour/` | "join our sunset bat kayak tour" | Valid, not yet done — go ahead |
| `/blog/why-team-building-is-great-on-kayaks/` (confirmed live) | `/austin-kayak-tours/corporate-events/` (use this exact URL, not the vault's bare `/corporate-events/`, to avoid adding a link into the duplicate-URL problem) | "book a corporate kayak event" | Valid, not yet done |
| `/blog/dog-friendly-austin-businesses/` (real slug — vault doc says `dog-friendly-activities-in-austin`, which 404s) | `/rental/` | "rent a kayak with your pup on Lady Bird Lake" | Valid concept, slug needs correcting when executed |
| `/blog/breakfast-ideas-in-austin/` (real slug — vault doc says `breakfast-places-in-austin`, which doesn't exist) | `/austin-kayak-tours/austin-skyline-tour/` | "morning skyline kayak tour" | Valid concept, slug needs correcting |
| `/blog/rainy-days-outdoor-eating-in-austin/` (real slug — vault doc says `outdoor-rainy-eating-in-austin`) | `/` and `/austin-kayak-tours/austin-skyline-tour/` | per vault doc | Valid concept, slug needs correcting |
| `/blog/austin-bachelorette-party-guide/` (real slug — vault doc says `top-5-bachelorette-party-ideas-in-austin`) | `/austin-kayak-tours/corporate-events/` and `/rental/` | per vault doc | Valid concept, slug needs correcting |
| `/blog/five-great-ideas-for-an-austin-vacation/` (confirmed live) | `/`, `/austin-kayak-tours/austin-skyline-tour/`, `/austin-kayak-tours/sunset-bat-bridge-kayak-tour/` | per vault doc | Valid, not yet done |

**Orphan pages confirmed still under-linked (per vault doc, and not contradicted by the crawl):** `/austin-kayak-tours/paddleboard-tour/`, `/austin-kayak-tours/corporate-events/`, `/rainey-street-walking-bar-tour/`, plus newly identified orphans this session: `/austin-kayak-tours/halloween-tour/` and `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` (zero internal linking strategy at all).

---

## Prioritized Fix List

### Quick Wins (this week, low effort / high leverage)

1. **Paste FAQPage schema onto `/faq/`.** Exact page: `https://www.austinkayaktours.com/faq/`. Exact change: mine the page's existing Q&A pairs into JSON-LD following the same pattern already live on the bat tour page (raw JSON, no `<script>` wrapper, no escaped inner quotes, per the ACF Schema Markup field), paste into that page's Schema Markup field in WordPress. Expected impact: this page's entire content is FAQ pairs with zero structured markup — highest schema ROI on the site, improves AI Overview / rich-result eligibility for every "does AKT..." / "how much does..." query.

2. **Paste the homepage LocalBusiness + Organization schema.** Exact page: `https://www.austinkayaktours.com/` (root). Exact change: use the JSON-LD already drafted in `Marketing/SEO Content/02 - Schema Markup Library.md`, but first replace the placeholder `reviewCount: 500` and `ratingValue: 5.0` with real current numbers from TripAdvisor/Google before pasting (the doc itself flags this as a placeholder). Expected impact: enables the Knowledge Panel / local pack eligibility and gives every AI engine a clean, structured entity definition to cite instead of parsing prose.

3. **Fix the `/kayak-paddleboard-rental/` 404.** Exact URL: `https://www.austinkayaktours.com/kayak-paddleboard-rental/`. Exact change: 301 redirect this URL to `/rental/` (or find and update whatever's still linking to it — check GBP, old ads, and any external backlinks first). Expected impact: recovers any inbound link equity currently hitting a dead page; this bug has been flagged since the May 9 audit and is still live.

4. **Publish the two ready-to-go pillar pages.** Exact pages/URLs to create: `/best-places-to-kayak-in-austin/` and `/kayaking-lady-bird-lake/`. Exact change: the full drafts already exist at `Marketing/SEO Content/Pillars/01 - Best Places to Kayak in Austin.md` and `Pillars/02 - Kayaking on Lady Bird Lake.md` — copy-paste into WordPress with the titles/metas from `01 - Title & Meta Rewrites.md`. Expected impact: "best place to kayak in austin" alone showed 2,799 impressions at position 13 with zero clicks as of the last GSC pull — no page on the site currently targets it. This is the single highest-traffic-potential item on this entire list and it's already written.

5. **Replace homepage "Learn More" CTAs with descriptive anchors.** Exact page: `https://www.austinkayaktours.com/` (homepage tour grid — confirmed 7 instances of literal "Learn More" text still live in the page source). Exact change: per `04 - Internal Linking Map.md` — "Skyline tour details," "Bat tour details," "Paddle board tour details," "Rental options & pricing," etc. Expected impact: descriptive anchor text carries keyword relevance to the linked money pages; generic "Learn More" passes zero topical signal.

6. **Add the internal links from the 4 confirmed-live blog posts** (`some-reasons-to-check-out-the-south-congress-bat-colony`, `why-team-building-is-great-on-kayaks`, `five-great-ideas-for-an-austin-vacation`, and the corrected-slug posts `dog-friendly-austin-businesses`, `breakfast-ideas-in-austin`, `rainy-days-outdoor-eating-in-austin`, `austin-bachelorette-party-guide`) to their target money pages, using the exact anchors in the table above. Expected impact: recovers link equity currently leaking from indexed, traffic-earning posts to under-linked money pages (paddleboard tour, corporate events, rental).

### Strategic Work (this quarter, higher effort)

1. **Resolve the lonestarkayaktours.com duplicate-domain problem.** Exact target: all of `lonestarkayaktours.com`. Exact change: this needs a dev/FareHarbor conversation, not a content edit — either (a) build the page-by-page 301 map from lonestarkayaktours.com to austinkayaktours.com that the May 9 plan called for and never shipped, or (b) if the two are meant to stay as sibling brands, add `rel="canonical"` cross-references and clearly differentiate the content so they're not near-duplicates. Right now it's neither — it's a live, self-canonicalizing, fully indexable duplicate with `index,follow` set. Expected impact: this is plausibly suppressing every keyword on the ranking table above; Google devalues sites competing against their own duplicate content, and the WebSearch results confirm both domains are already surfacing side by side today.

2. **Consolidate the duplicate URL pairs.** Exact targets: `/paddleboard-tour/` + `/austin-kayak-tours/paddleboard-tour/`, and `/corporate-events/` + `/austin-kayak-tours/corporate-events/`. Exact change: pick one canonical URL per tour (recommend the shorter, non-nested version per the May 9 plan's task #5 intent), 301 the other, and update every internal link/nav item to point only to the canonical version. Expected impact: stops the site from splitting its own link equity and ranking signals across two URLs for the same product.

3. **Reconcile the vault's SEO Content docs against the live site.** Exact targets: `01 - Title & Meta Rewrites.md`, `04 - Internal Linking Map.md`, and the schema library — specifically correct or remove references to `/sunrise-tour/`, `/sunset-skyline-tour/`, `/paddle-board-lessons/`, `/about-us/`, and `/4th-of-july-fireworks-tour/` (real slug: `/austin-kayak-tours/fourth-of-july-tour/`), and fix the blog slugs flagged in the Internal Linking table above. Expected impact: prevents whoever executes these docs next (David, Connor, or an AI agent) from wasting time trying to edit pages that don't exist, or shipping broken internal links.

4. **Decide whether Sunrise Tour and a standalone About page get built, or get dropped from the plan.** Exact targets: `/sunrise-tour/` and `/about-us/`. Neither exists anywhere on the live site or in any sitemap. Expected impact: if Sunrise is a real bookable product in FareHarbor just missing a dedicated landing page, building one closes a content gap; if it isn't real, every SEO doc referencing it should stop. A basic About page is a straightforward trust/E-E-A-T win regardless — guide bios, real photos, years in business, licensing — and directly supports the AI-SEO doc's flagged weakness around thin third-party/authority signals.

5. **Build SEO coverage for the two orphaned live products.** Exact targets: `/austin-kayak-tours/halloween-tour/` and `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/`. Exact change: add title/meta per the existing pattern, Product schema per the library format, and at least 3 internal links each from relevant blog posts (seasonal/fall content for Halloween, "full day itinerary" content for the all-day tour). Expected impact: two real revenue-generating tours currently invisible to the entire SEO strategy start accumulating rankings and internal link equity.

6. **Publish Cluster A (5 drafted posts) and the 3 staged blog drafts.** Exact targets: everything in `Marketing/SEO Content/Cluster A - Lady Bird Lake/` and `Marketing/Blog Drafts - Staged/`. Expected impact: this is already-written Tier-1 content sitting unpublished; each post is designed to link to 2 money pages and the pillar hub per the publishing discipline in the Action Plan, compounding the internal-linking fixes above.

7. **Set up a real Core Web Vitals baseline once PSI quota resets.** Exact target: full site, mobile + desktop, via `~/Projects/tech-seo/psi-run.mjs`. Consider adding a free PSI API key to `~/.claude/.env` as `PSI_KEY=...` so future audits and the monthly `tech-seo-watch` loop don't get blocked by the shared daily quota again. Expected impact: currently flying blind on LCP/CLS/INP — can't rule out a page-speed problem contributing to the CTR/ranking issues without this data.

8. **Connect a GSC (and ideally GA4) MCP for this vault.** Every keyword number in this report is a 10-week-old snapshot from a different domain's property. Expected impact: without live GSC data, it's impossible to confirm whether the June 7 bat-page/rental-page rebuild actually moved rankings, or size the real opportunity on "kayak austin" / "austin kayaking" accurately.

---

*Compiled 2026-08-14. No live-site, WordPress, GBP, or ad changes were made in the course of producing this report.*
