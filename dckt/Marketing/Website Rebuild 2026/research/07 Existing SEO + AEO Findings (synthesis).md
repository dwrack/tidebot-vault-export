# 07 Existing SEO + AEO Findings (synthesis)

Compiled 2026-10-16 for the Astro rebuild of doorcountykayaktours.com (same URLs). Read-only synthesis of the DCKT vault docs. Nothing here was checked against the live site today; every status is "as of the source doc's date".

## Source key

Real filenames use an em dash after the number; written here with a hyphen.

| Code | File |
|---|---|
| A1 | Marketing/AI SEO Audit 2026-05-09.md |
| A2 | Marketing/AI SEO Action Plan 2026-05-09.md |
| A3 | Marketing/SEO Audit 2026-05-04.md (multi-domain, GSC) |
| A4 | SEO Content/2026-08-16 SEO + Technical Audit - DCKT.md (live crawl, no GSC/PSI that day) |
| K | SEO Content/Cave Point/00 - Keyword Map.md (snapshot 2026-04-26) |
| T | SEO Content/Towns/00 - Keyword Map.md (snapshot 2026-04-30) |
| S0 to S6 | SEO Content/AI SEO Action Plan May 2026/ files 00 README, 01 Schema Drop-In Pack, 02 Tour Page Copy Rewrites, 03 Pregnancy Post Update, 04 Outreach Drafts, 05 New Pages, 06 WordPress Publish Brief |
| B | SEO Content/_old-blog-audit-and-linking-matrix.md (2026-05-04) |
| CG | Marketing/Competitor Content-Gap Analysis - Peninsula Kayak Company (June 2026).md |
| FS | Marketing/Cave Point + Whitefish Dunes Fact Sheet (Oct 2026).md (researched 2026-10-14) |
| SI | SEO Content/_publish-batch-may-2026/00 - Sprint Index.md |
| MEM | Claude memory project_town_pillars_buildout.md (status update 2026-06-07), project_ai_seo_action_plan_may_2026.md |

## Read this first (conflicts between docs)

- **Town pillars are live, but on the OLD blog slugs, not the planned slugs.** MEM: all three were published 2026-06-07 in place at `/blog/7-reasons-fish-creek-is-the-best-town-to-stay-at-in-door-county/` (post 2863), `/blog/7-reasons-why-baileys-harbor-is-the-best-town-in-door-county/` (3816), `/blog/7-reasons-why-ephraim-is-the-best-town-to-stay-at-in-door-county/` (3577), with new title tags, H1s, FAQ/TouristDestination/BreadcrumbList JSON-LD. A4 (2026-08-16) correctly reports `/baileys-harbor-door-county/`, `/fish-creek-door-county/`, `/ephraim-door-county/` as 404 and says the 301 plan never ran. Both are true. For a same-URL rebuild: the town pages live at the `/blog/...` slugs; the planned 301s from B are moot for those three.
- **$4 Cave Point park fee.** K, the polished Cave Point drafts, S1 FAQ JSON-LD and S2 all say "$69 + $4 park fee". FS found NO official fee statement ("free appears true today, UNVERIFIED as an official statement"; the county's draft 2026-2030 plan budgets a pass system at Cave Point for 2027). Cave Point outline 07 even says "fees (free!)". Resolve before shipping any price copy or schema text.
- **"Guiding since 2013" vs founded 2002.** Cave Point HUB and tour polished drafts say 2013 at this shoreline; brand facts and S1 say 2002. The tour draft's "Why book with DCKT" section says owner on the water since 2002.
- **Review proof.** "4.9 stars, 240+ reviews" (K, T, tour drafts) vs "2,000+ five-star reviews" (S1 aggregateRating, reviewCount 2000) vs Egg Harbor Tripadvisor listing 615 reviews (S0). Pick one verified number and source before shipping aggregateRating.
- **Meeting point.** S1/S2 FAQs: meet at Schauer Park. Polished tour draft: meet at the Jacksonport shop (6329 WI-57) and get shuttled to the launch. FS geocodes 6329 State Hwy 57 as the shop and 5360 Schauer Road, Jacksonport as the park.
- **Address.** A2 first said Fish Creek 8442 State Hwy 42 (legal). S0 default, "confirmed by David 2026-05-10": 6329 Highway 57, Sturgeon Bay, WI 54235 for web schema and listings; Fish Creek stays the legal address only. Polished HUB writes the park as "Sturgeon Bay, WI 54235"; FS says Jacksonport.
- **Sunrise/sunset tours.** Cave Point outlines 11/12 and the polished tour page mention sunrise and sunset kayak tours; T says DCKT does NOT run a sunset tour ("do not use sunset paddle as a CTA"). Treat as not offered until confirmed.
- **Article author Person.** S0/S1/S3/S5 use "Drifty" (confirmed 2026-05-10); MEM index still says Ashley Hasstedt. S0 is later.
- **E-bike guided tour.** K/S1/S2: $99 guided. 02b (2026-10-07): guided slots ran only to Oct 12, none in November, so fall copy sells the $30/hr rental only.
- **Door Bluff / Death's Door are one product** (S6 batch 8, MEM). Flagship draft wants a new URL `/deaths-door-shipwreck-kayak-tour/`; S6 says redirect `/kayak-tours/deaths-door-shipwreck-bluff/` (404) to `/kayak-tours/door-bluff-county-park-shipwreck/` instead of building a separate page.
- **Live tour URL structure** (A4, MEM): `/kayak-tours/cave-point-county-park/`, `/kayak-tours/cave-point-whitefish-dunes-half-day-kayak-tour/`, `/kayak-tours/door-bluff-county-park-shipwreck/`, `/kayak-tours/door-bluff-shipwreck-1-2-day-kayak-tour/`, `/kayak-tours/eco-estuary-tour/`, `/kayak-tours/cana-island-lighthouse-kayak-tour/`, `/activities/cave-point-fat-tire-e-bike-tour/`, `/activities/e-bike-rental/`, `/e-bike-tours/`. The idealized slugs in the drafts (`/cave-point-kayak-tour/` etc.) were 404 on 2026-08-16. The full live URL list is in `Marketing/Website Rebuild 2026/inventory/`.

---

## 1. Open recommendations never shipped

Status key: **shipped** (doc says so), **not shipped** (doc says so, with date), **unknown** (no doc after the plan confirms it). Later docs (02b on 2026-10-07, CG note) say staged WP fixes were blocked at WP login/2FA, so treat "unknown" for May schema work as probably not shipped.

### 1a. On-site schema and AEO structure

| # | Recommendation | Source | URL(s) | Status |
|---|---|---|---|---|
| 1 | Replace homepage LocalBusiness block with a corrected @graph (Organization + LocalBusiness + WebSite): add aggregateRating, openingHoursSpecification, sameAs, image, description, areaServed, knowsAbout, founder, foundingDate | A1, A2, S1 1.1 | `/` | unknown. A2 found Organization, LocalBusiness, WebSite, WebPage already present but incomplete and with the Jacksonport/Sturgeon Bay address |
| 2 | Align canonical address across schema, footer, GBP, Yelp, Tripadvisor | A2, S0 | sitewide | decided 2026-05-10 (6329 Hwy 57, Sturgeon Bay 54235); shipped unknown |
| 3 | Add TouristTrip + Offer + FAQPage (+ BreadcrumbList) to every tour page via @graph | A1, A2, S1 1.2 to 1.8, S6 batch 2 | `/kayak-tours/cave-point-county-park/`, `/kayak-tours/cave-point-whitefish-dunes-half-day-kayak-tour/`, `/kayak-tours/door-bluff-county-park-shipwreck/`, `/kayak-tours/door-bluff-shipwreck-1-2-day-kayak-tour/`, `/kayak-tours/eco-estuary-tour/`, `/kayak-tours/cana-island-lighthouse-kayak-tour/`, `/e-bike-tours/` | unknown. As of 2026-05-09 tour pages had only BreadcrumbList. A4 spot-checked title, meta, canonical only |
| 4 | Rewrite first paragraph of every tour page as a 40 to 60 word definition block (name, duration, launch point, town, 2 to 3 landmarks, skill level, inclusions, price; no marketing adjectives) | A1, A2 2.1, S2 | same 7 tour URLs | unknown |
| 5 | Add a visible FAQ section matching the FAQPage JSON-LD 1:1 | A2 2.2, S2, S6 | same 7 tour URLs | unknown |
| 6 | Cana Island price: confirm; $145 is a placeholder | S0, S6 | `/kayak-tours/cana-island-lighthouse-kayak-tour/` | not shipped (open question) |
| 7 | Fix pregnancy post Article schema (ISO 8601 dates, Person author, unescaped entities, mainEntityOfPage, publisher, image, ACOG citation) and add FAQPage (6 to 7 Qs) | A1, A2 1.2, S3 | `/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/` | unknown |
| 8 | Insert ACOG citation paragraph (link `https://www.acog.org/womens-health/faqs/exercise-during-pregnancy`) and a visible FAQ block with H3 questions, update "Last updated" line | A1, A2 2.4, S3 | same | unknown |
| 9 | Article + FAQPage (some + HowTo or ItemList) on the top 9 blogs | A1, A2 1.4, S1 1.9a to 1.9i | `/blog/how-far-can-a-kayak-hang-out-of-a-truck/`, `/blog/different-types-of-kayaks-pros-and-cons/`, `/blog/7-reasons-fish-creek-is-the-best-town-to-stay-at-in-door-county/`, `/blog/7-reasons-why-baileys-harbor-is-the-best-town-in-door-county/`, `/blog/7-reasons-why-ephraim-is-the-best-town-to-stay-at-in-door-county/`, `/blog/door-county-bike-routes/`, `/blog/boy-scout-girl-scout-kayaking-merit-badge-requirements/`, `/blog/how-to-kayak-and-prevent-blisters/`, `/blog/7-must-do-winter-activities-in-door-county/` | town three: shipped in different form on 2026-06-07 (MEM). Rest unknown |
| 10 | Visible FAQ on those blogs must match the schema or Google rejects the rich result | S6 batch 4 | same | unknown |
| 11 | HowTo schema on truck-overhang, merit badge, blisters; ItemList + comparison table on kayak-types; ItemList of routes on bike-routes | A1 page-level table | those blog URLs | unknown |
| 12 | BreadcrumbList on every page | A1 | sitewide | partly there (theme outputs one; MEM notes pillar pages ended up with two nodes) |
| 13 | Service schema for sauna (price is "[CONFIRM PRICE]") | S1 1.10, A3 (sauna pos 2.3, 22% CTR, add internal links and homepage CTA) | `/sauna-experience/` | not shipped (price unconfirmed) |
| 14 | Show publish + last-updated dates on every blog post AND blog index; add excerpts and author names to the index | A1 | `/blog/` and all posts | unknown |
| 15 | Author/guide bio pages with Person schema, verified credentials only (never claim ACA certification), referenced from Article.author | A1, A2 3.1 | new pages, blog posts | not shipped (no bio pages in the docs) |
| 16 | Add verified stats, external citations, named guide quotes, real numbers (water temp, cave counts, distances) on tour pages | A1 (Princeton GEO levers) | tour pages | unknown |
| 17 | Visible "Updated for 2026 season" + dateModified on homepage and tour pages | A1 | `/`, tour pages | unknown |
| 18 | Homepage H1 is brand-only ("Door County Kayak Tours" with TM); not query-targeted | A1 | `/` | unknown |
| 19 | Verify sitemap.xml is current and includes any new page | A1, A2 1.5 | `/sitemap.xml` | shipped/verified: A4 2026-08-16 sitemap index OK, 3 children return 200 (page 35, activity 32, post 54 URLs) |
| 20 | Cave Point keyword-map schema plan: tour pages TouristTrip + Product + AggregateRating; FAQPage on Q&A; hub TouristAttraction + Organization; ImageObject with contentLocation 44.9263 N, 87.1817 W (coordinates not verified in FS) | K | Cave Point cluster | not shipped (cluster not live) |
| 21 | Town pillars: TouristDestination (geo), FAQPage, BreadcrumbList Home > Door County > Town, optional tour Product + AggregateRating | T | three town URLs | shipped for the 3 live blog slugs 2026-06-07 (MEM) |

### 1b. New pages and content never built

| # | Recommendation | Source | URL(s) | Status |
|---|---|---|---|---|
| 22 | Publish Cave Point HUB (polished, ready) | K, A4, SI, B | `/cave-point/` (planned slug). Live `/cave-point/` is a thin WP category archive titled "Cave Point Blog Category" | not shipped (A4 2026-08-16) |
| 23 | Publish Cave Point Kayak Tour pillar | K, A4, SI | `/cave-point-kayak-tour/` | not shipped, 404 (A4) |
| 24 | Publish Cave Point E-Bike pillar (or the 02b fall rental version) | K, A4, 02b | `/cave-point-ebike-tour/` | not shipped, 404 (A4); 02b "NOT YET PUBLISHED: blocked at WP 2FA" (2026-10-07) |
| 25 | Publish Sea Caves, Best Time, Kayak Rental spokes | K, SI | `/cave-point-sea-caves/`, `/best-time-cave-point-county-park/`, `/cave-point-kayak-rental/` | not shipped (SI live-URL column empty; A4 did not test these three) |
| 26 | Draft and publish 11 Cave Point supporting pages (outlines only) | K, outlines doc | see section 4 | not shipped, not drafted |
| 27 | New pages flagged "NEW needs page" in K | K | `/cave-point-half-day-kayak-tour/`, `/cave-point-private-kayak-tour/` | not shipped |
| 28 | Death's Door flagship page, or redirect `/kayak-tours/deaths-door-shipwreck-bluff/` to the Door Bluff page | A1, A2 2.3, S6 batch 8, flagship draft | `/deaths-door-shipwreck-kayak-tour/` (draft) vs `/kayak-tours/deaths-door-shipwreck-bluff/` (404) | not shipped (A4: draft slug 404) |
| 29 | Death's Door naming history blog (Potawatomi + Ho-Chunk) | SI, S2 | `/blog/deaths-door-name-history/` | BLOCKED on Ho-Chunk cultural review (outreach emailed 2026-05-06); not shipped |
| 30 | Things-to-Do hub with TravelGuide + FAQPage | A1, A2 4.4, S5 A | `/things-to-do-in-door-county/` | not shipped (new) |
| 31 | DCKT vs Lakeshore Adventures comparison (fair table; no outbound link to Lakeshore; fill "[confirm]" cells first) | A1, A2 4.2, S5 B | `/door-county-kayak-tours-vs-lakeshore-adventures/` | not shipped (new) |
| 32 | Sit-on-top explainer; may replace the kayak-types post, in which case inherit that slug | SI, Blog Polished | `/blog/different-types-of-kayaks-pros-and-cons/` or new slug | unknown, slug decision open |
| 33 | Publish the 10 competitor-gap articles (see section 7) | CG | new | not shipped |
| 34 | Fall e-bike rental post (02b) and fall color ride post | 02b, Fall Color draft | `/blog/cave-point-ebike-tour/` (02b) and `door-county-fall-color-e-bike-ride` (draft, "do not publish" until [VERIFY] items clear) | not shipped |
| 35 | Lautenbach's partner post | Local Partners draft | `/blog/lautenbachs-cherries-half-day-picnic/` (suggested) | not shipped |
| 36 | `/things-to-do-in-door-county/`-style sleeper queries: Cana Island refresh, Whitefish Dunes refresh | A2 4.4 | Cana Island tour page; Whitefish Dunes blog | unknown |

### 1c. Fixes, consolidation, cleanup

| # | Recommendation | Source | URL(s) | Status |
|---|---|---|---|---|
| 37 | Delete or noindex the test page, remove from sitemap (title "Claude Ads MCP 2", generic meta, index,follow) | A4 | `/claude-ads-mcp-2/` | not shipped (A4). Do not carry into Astro |
| 38 | Rewrite title/meta of the `/cave-point/` archive until the HUB ships (current meta is WP boilerplate) | A4 | `/cave-point/` | not shipped |
| 39 | CTR rewrite of the Cave Point tour title (pos 4.6, 6.6% CTR). Suggested test: "Cave Point Kayak Tour: Sea Caves & Cliffs (4.9 star, 240+ Reviews)". Current title per A4: "Cave Point County Park Kayak Tour \| Door County, Wisconsin" | A3 | `/kayak-tours/cave-point-county-park/` | not shipped as of A4 |
| 40 | Title/meta rewrite for the 3 town pages | A3 | three town slugs | shipped 2026-06-07 (MEM) |
| 41 | 301 old listicles to new pillars | B, A3, A4 | `/blog/7-reasons-...` x3 to town slugs | superseded: pages rewritten in place, slugs kept (MEM) |
| 42 | 301 `/blog/cave-point-county-park/` and `/blog/7-reasons-why-whitefish-bay-dunes-state-park-is-a-must-visit/` to the Cave Point HUB once it exists | B | those two blogs, `/cave-point/` | not shipped |
| 43 | Run the full internal-link matrix (anchors per old post into HUB, tour, e-bike, town, shipwreck, Eco Estuary, sauna pages) | B, A4 | the 9 KEEP+POLISH posts plus others | not shipped (A4: "ready to execute the moment the new pages publish") |
| 44 | Quick links: pregnancy post to Cave Point tour; `/blog/door-county-bike-routes/` to `/e-bike-tours/`; kayak-types post to `/kayak-tours/`; sauna page more internal links and a homepage CTA | A3 | those pages | not shipped as of A4 |
| 45 | Polish 9 KEEP posts (pregnancy, truck overhang, bike routes, kayak types, blisters, rainy-day kids, bachelorette, Ephraim Fyrball, Sister Bay cheese curds) and 13 POLISH-tier posts | B, Blog Polished | see section 5 | unknown, drafts exist |
| 46 | Deindex/kill ~18 to 20 stale or off-brand posts (list in B) | B | e.g. alligator, celebrities tweet, Houston/Austin kayak posts, photography guide, kayak-and-paddleboard-sale, half-marathon, T-shirts, wine tasting, gift promo | unknown. "NEEDS DAVID INPUT" items (Clark Lake tours, paddleboard product, Father's Day repost, Whistling Swan, Barmuda bars) were unanswered since May per A4. Blog Polished folder later verified Whistling Swan and Barmuda bars as operating |
| 47 | Fix or noindex low-position pages: `/kayak-rentals/` (pos 33.5), `/ice-shack-rental/` (pos 37, deprioritize); promote `/kayak-tours/eco-estuary-tour/` (pos 41.1), half-day (pos 29.1), Door Bluff (pos 24, losing click) | A3 | those URLs | not shipped |
| 48 | Check 1.17s TTFB on the Baileys Harbor blog vs 0.35 to 0.38s baseline (one sample only) | A4 | `/blog/7-reasons-why-baileys-harbor-is-the-best-town-in-door-county/` | not shipped; irrelevant after static rebuild |
| 49 | Cave Point cluster: pick one winner (DCKT main vs cavepointpp.com) and 301 the other | A3 | other domains | unknown. K says differentiate; A3 says consolidate |
| 50 | Sunset doorcountykayak.com via 301s (old multisite `/sites/7030/`); diagnose dcdetours.com (zero GSC data) | A3 | other domains | unknown |
| 51 | Keep the half-day ($145) upsell above the fold, mid-page and in the sidebar on Cave Point and Door Bluff content | SI, MEM | Cave Point and Door Bluff pages | content rule, applies to rebuild |

### 1d. Off-site and measurement (not URL-bound)

| # | Recommendation | Source | Applies to | Status |
|---|---|---|---|---|
| 52 | Wikipedia neutral edit to Door County article (not from DCKT IP) | A1, A2 3.2, S4 | off-site | unknown |
| 53 | Consolidate Tripadvisor listings into Egg Harbor `d1036732` (615 reviews); merge Ellison Bay `d12545584` and Sturgeon Bay `d10319552` | A1, A2 3.3, S0, S4 | off-site | unknown |
| 54 | Refresh Travel Wisconsin and Destination Door County listing copy with definition format and 2026 pricing | A2 3.4, S4 | off-site | unknown |
| 55 | One guide-led Reddit AMA (r/wisconsin), not promotional | A1, A2 3.5, S4 | off-site | unknown (MEM index shows a separate Reddit presence project) |
| 56 | FAQ-style GBP posts (6 to 8), outdoor publication pitch per quarter | A2 3.6, 4.3, S4 | off-site | unknown |
| 57 | YouTube descriptions: 60 word summary, facts table, timestamps, FAQ | A1, A2 4.1 | YouTube | unknown |
| 58 | Monthly AI-visibility check of 20 priority queries (list in A1) in a sheet; evaluate Otterly, Peec or ZipTie after 3 months | A1, A2 | tracking | unknown |
| 59 | Restore GSC/GA4 access; add a PSI API key so real Core Web Vitals can be pulled | A4 | tooling | not shipped. No CWV numbers exist anywhere |
| 60 | Keep robots.txt AI crawlers allowed (GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, anthropic-ai, Google-Extended, Bingbot, CCBot) | A1 | `/robots.txt` | OK as is; carry over |

---

## 2. Technical findings

Schema
- Homepage has Organization, LocalBusiness, WebSite, WebPage JSON-LD but LocalBusiness lacks aggregateRating, openingHours, sameAs, image, description, areaServed. A1 first said "zero JSON-LD"; A2 corrected this after pulling raw HTML. [A1, A2]
- Tour pages (Cave Point, Eco Estuary, Door Bluff, Cana Island, e-bike pages) carried only BreadcrumbList on 2026-05-09. No TouristTrip, Product, Offer or FAQPage. Lakeshore, CPPP and Kayak Guide Justin have the same gap. [A2]
- Pregnancy post: BlogPosting/Article schema has non-ISO dates ("December 18, 2023"), Organization as author, unescaped `&#8217;` in the headline, no FAQPage. [A1, A2]
- Schema address on homepage was "Sturgeon Bay 54235, 6329 Wisconsin 57", not the legal Fish Creek address. [A2]
- Theme already outputs its own BreadcrumbList; the 2026-06-07 pillar JSON-LD added a second one on each town page. [MEM]
- WP field quirks (not relevant to Astro): raw JSON only, no script wrapper, no escaped inner quotes. [S0]

Speed
- No Core Web Vitals data exists. PSI returned 429 with quota 0 on 2026-08-16. [A4]
- Proxy TTFB: homepage 0.38s, Cave Point tour page 0.35s, Baileys Harbor blog 1.17s (single sample). [A4]

Indexing, sitemap, robots, noindex
- robots.txt is healthy, declares `Sitemap: https://www.doorcountykayaktours.com/sitemap.xml`, blocks only scraper bots (MegaIndex, MauiBot, BLEXBot, Baiduspider, Barkrowler, Yandex, SeznamBot, etc.). AI crawlers are not blocked. [A1, A4]
- sitemap.xml is an index of 3 children, all 200: page-sitemap (35 URLs), activity-sitemap (32 tour/activity URLs), post-sitemap (54 posts), about 121 URLs. [A4] Note the activity sitemap implies tours live under a custom post type (`/kayak-tours/`, `/activities/`).
- `/claude-ads-mcp-2/` is live, indexable, in the sitemap, title "Claude Ads MCP 2 | Door County Kayak Tours". Scratch page. [A4]
- `/cave-point/` is a default WP category archive: title "Cave Point Blog Category | Door County Kayak Tours | Page 1 of 1", meta "Click to view cave point category posts in Blog | Page 1 of 1". [A4]
- GSC property gotcha: API works only for `https://www.doorcountykayaktours.com/` (with www and trailing slash). [B]
- dcdetours.com returned zero GSC data (verified property, nothing indexed or no traffic). [A3]
- Memory index (not in assigned files, unverified): an I-9 PDF was once publicly indexable; check the rebuild does not expose it.

Canonicals, redirects, hosts
- Apex to www is two clean single 301 hops; `robots.txt` and `sitemap.xml` on the apex also 301 to www. Tour-page canonical correct. Use `https://www.doorcountykayaktours.com/` as canonical host. [A4]
- `/privacy-policy/` 301s to `/privacy-statement-us/`. Keep. [A4]
- Cross-domain cannibalization: cavepointpp.com beats the main site on "cave point kayak tour" (3.8 vs 4.6) and "cave point county park kayaking" (3.6 vs 3.7); doorcountykayak.com (old multisite) wins nothing. [A3]
- Same-intent duplicates on-domain for "cave point county park": tour page, old `/blog/cave-point-county-park/`, thin `/cave-point/` archive. [A4]
- 301 plan for old listicles never executed as of 2026-08-16; superseded by in-place rewrites on 2026-06-07. [A4, MEM]

Titles and meta
- Homepage H1 is brand only. [A1]
- Cave Point tour title not earning CTR at pos 4.6 (6.6%); current "Cave Point County Park Kayak Tour \| Door County, Wisconsin"; meta ends "Book your tour online!". [A3, A4]
- 2026-06-07 live town titles: "Fish Creek, Door County: Things to Do in the Walkable Town", "Baileys Harbor, Door County: Things to Do on the Quiet Side", "Ephraim, Door County: Things to Do in the White Village". [MEM]
- First paragraph of Cave Point tour page was flowery prose ("Pictures can hardly do justice to the crystal waters...") with no time, distance or price in extractable form. [A1]

Images
- No image defects were reported by any audit. Polished drafts specify per-page alt text; optimized Cave Point images are staged in `SEO Content/Cave Point/staged-images/` (hero 1920x1440 about 697KB, inline 1600px 300 to 490KB). Cave Point drafts quote file names like `cave-point-county-park-aerial-cliffs-kayaks.jpg`. [_publish-artifacts]
- Schema pack image URLs are placeholders (`/wp-content/uploads/sites/2281/...`). Replace with real assets.

Internal links
- Dead-end high-traffic posts: pregnancy (about 127 clicks per quarter), bike routes (90), kayak types (35), none funnel to money pages. [A3]
- Planned linking rules: every Cave Point page links up to the hub, hub links to all; informational pages link to the tour as primary CTA and e-bike as secondary; vary anchors, never repeat the exact primary keyword more than once per linking page; town pillars link to each other, the Cave Point hub and tours; no competitor links (Bayshore, Lakeshore, Peninsula Kayak Co). [K, T]
- Full anchor matrix per new page is in B (hub, kayak tour, e-bike, three towns, Death's Door flagship, history blog, Eco Estuary, sauna).
- Half-day tours are under-promoted: half-day page pos 28 to 29. [A1, A3]
- Blog index shows no dates, authors, excerpts. [A1]

Content structure
- Death's Door page `/kayak-tours/deaths-door-shipwreck-bluff/` 404s while AI answers name it as a DCKT offering. [A1]
- A4: 4 months of finished content unpublished while GSC page-2 terms sit on thin pages.

---

## 3. Schema plan already drafted (S1 Schema Drop-In Pack)

Per page type. Placeholders to resolve are listed after the blocks.

| Page type | URLs | @types | Key properties |
|---|---|---|---|
| Homepage | `/` | @graph: Organization, LocalBusiness, WebSite | Organization: @id `#organization`, name, alternateName, url, logo ImageObject, founder Person, foundingDate 2002, sameAs (Instagram, Facebook, Tripadvisor Egg Harbor, Travel Wisconsin, doorcounty.com). LocalBusiness: @id `#localbusiness`, telephone, priceRange "$$", image, description, PostalAddress (6329 Highway 57, Sturgeon Bay, WI 54235), GeoCoordinates 44.9805, -87.1844, openingHoursSpecification (daily 08:00 to 19:00, validFrom 2026-05-15, validThrough 2026-10-15), aggregateRating 4.9 / 2000, areaServed AdministrativeArea, founder, foundingDate, knowsAbout. WebSite: publisher references #organization |
| Tour pages (7) | see section 1 row 3 | @graph: BreadcrumbList, TouristTrip, FAQPage | TouristTrip: name, description, image, touristType, itinerary (ItemList of ListItem), offers (Offer: price, priceCurrency USD, availability InStock, validFrom, validThrough, url), provider `{"@id": "...#localbusiness"}`. Door Bluff also has alternateName "Death's Door Shipwreck Tour". FAQPage 4 to 7 Questions per page (Cave Point 7, half-day 5, Door Bluff 6, Door Bluff half-day 4, Eco Estuary 5, Cana 5, e-bike 4) |
| Offers by page | | | Cave Point 2-hr $69; Cave Point half-day $145; Door Bluff 2-hr $69; Door Bluff half-day $145; Eco Estuary $65; Cana Island $145 (placeholder); e-bike guided $99 (rental $30/hr per S2) |
| Blog posts (9) | see section 1 row 9 | @graph: Article (+ FAQPage, + HowTo or ItemList on some) | Article: headline, datePublished, dateModified, author Person "Drifty" (description, worksFor #organization), publisher #organization, mainEntityOfPage WebPage, image. 3 to 5 Questions each; HowTo with HowToStep on truck-overhang |
| Pregnancy post | `/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/` | Article + FAQPage (S3) | ISO dates (datePublished 2023-12-18), Person author, ImageObject 1000x1000, `citation` ACOG URL; 7 FAQ questions per S6 |
| Sauna | `/sauna-experience/` | Service | provider #localbusiness, areaServed, description, Offer (price "[CONFIRM PRICE]") |
| Hub: Things to Do | `/things-to-do-in-door-county/` | TravelGuide, BreadcrumbList, FAQPage (S5) | datePublished/dateModified, about Place, 5 Questions |
| Comparison page | `/door-county-kayak-tours-vs-lakeshore-adventures/` | Article, BreadcrumbList, FAQPage (S5) | 3 Questions in schema (6 on page) |
| Town pillars | three town URLs | TouristDestination, FAQPage, BreadcrumbList (T, polished drafts) | name, geo, containedInPlace Place "Door County, Wisconsin", 3 Questions each in JSON-LD |
| Cave Point cluster (K, not in S1) | HUB: TouristAttraction + Organization + FAQPage; tours: TouristTrip + Product + AggregateRating (4.9 / 239 or 240+ reviews); photos: ImageObject with contentLocation | | HUB polished draft also lists Parking, Hiking trail, Picnic area, Vault toilets as amenity items |

### Verbatim: Organization + LocalBusiness + WebSite (S1 1.1)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.doorcountykayaktours.com/#organization",
      "name": "Door County Kayak Tours",
      "alternateName": "Door County Kayak Tours LLC",
      "url": "https://www.doorcountykayaktours.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/dckt-logo.png"
      },
      "founder": {
        "@type": "Person",
        "name": "David Rack"
      },
      "foundingDate": "2002",
      "sameAs": [
        "https://www.instagram.com/doorcountykayaktours/",
        "https://www.facebook.com/DoorCountyKayakTours/",
        "https://www.tripadvisor.com/Attraction_Review-g59850-d1036732-Reviews-Door_County_Kayak_Tours-Egg_Harbor_Wisconsin.html",
        "https://www.travelwisconsin.com/outdoors/on-the-water/door-county-kayak-tours",
        "https://www.doorcounty.com/business-directory/water-activities/door-county-kayak-tours"
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://www.doorcountykayaktours.com/#localbusiness",
      "name": "Door County Kayak Tours",
      "url": "https://www.doorcountykayaktours.com",
      "telephone": "+1-920-868-1400",
      "priceRange": "$$",
      "image": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/dckt-hero.jpg",
      "description": "Guided kayak, e-bike, and paddleboard tours across Door County, Wisconsin since 2002. Beginner-friendly tours of Cave Point sea caves, Death's Door shipwrecks, Cana Island Lighthouse, and Eco Estuary wetlands. Tandem sit-on-top kayaks, paddles, and PFDs included.",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "6329 Highway 57",
        "addressLocality": "Sturgeon Bay",
        "addressRegion": "WI",
        "postalCode": "54235",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "44.9805",
        "longitude": "-87.1844"
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
          "opens": "08:00",
          "closes": "19:00",
          "validFrom": "2026-05-15",
          "validThrough": "2026-10-15"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "2000",
        "bestRating": "5",
        "worstRating": "1"
      },
      "areaServed": {
        "@type": "AdministrativeArea",
        "name": "Door County, Wisconsin"
      },
      "founder": {
        "@type": "Person",
        "name": "David Rack"
      },
      "foundingDate": "2002",
      "knowsAbout": [
        "Kayak Tours",
        "Sea Cave Kayaking",
        "Shipwreck Kayak Tours",
        "E-Bike Tours",
        "Lake Michigan Paddling",
        "Door County Wisconsin Tourism"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.doorcountykayaktours.com/#website",
      "url": "https://www.doorcountykayaktours.com",
      "name": "Door County Kayak Tours",
      "publisher": {"@id": "https://www.doorcountykayaktours.com/#organization"}
    }
  ]
}
```

House rule from the vault: never put David Rack's name on outward-facing business contact material. The `founder` Person in this block names him; decide whether to keep it for the rebuild.

### Verbatim: Cave Point tour, BreadcrumbList + TouristTrip with Offer + FAQPage (S1 1.2)

S1 has no standalone `Product` block. The TouristTrip with its `offers` Offer is the drafted equivalent; K separately asks for Product + AggregateRating on tour pages.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": "https://www.doorcountykayaktours.com/kayak-tours/", "name": "Kayak Tours"},
        {"@type": "ListItem", "position": 2, "item": "https://www.doorcountykayaktours.com/kayak-tours/cave-point-county-park/", "name": "Cave Point County Park"}
      ]
    },
    {
      "@type": "TouristTrip",
      "name": "Cave Point Kayak Tour",
      "description": "A 2-hour guided sit-on-top kayak tour of the limestone caves and 30-foot bluffs at Cave Point County Park along Lake Michigan in Jacksonport, Wisconsin. Beginner-friendly. Tour covers approximately 4 miles. Tandem sit-on-top kayaks, paddles, and PFDs included.",
      "image": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/2019/03/cave-point-county-park.jpg",
      "touristType": ["Beginner paddlers", "Families", "Couples", "First-time kayakers"],
      "itinerary": {
        "@type": "ItemList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Check-in and orientation at Schauer Park"},
          {"@type": "ListItem", "position": 2, "name": "On-water paddle technique lesson"},
          {"@type": "ListItem", "position": 3, "name": "Paddle north along the Lake Michigan shoreline"},
          {"@type": "ListItem", "position": 4, "name": "Explore accessible sea caves at Cave Point (weather permitting)"},
          {"@type": "ListItem", "position": 5, "name": "Pause at Whitefish Dunes for photos"},
          {"@type": "ListItem", "position": 6, "name": "Return paddle to launch"}
        ]
      },
      "offers": {
        "@type": "Offer",
        "price": "69.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "validFrom": "2026-05-15",
        "validThrough": "2026-10-15",
        "url": "https://www.doorcountykayaktours.com/kayak-tours/cave-point-county-park/"
      },
      "provider": {"@id": "https://www.doorcountykayaktours.com/#localbusiness"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "How long is the Cave Point kayak tour?", "acceptedAnswer": {"@type": "Answer", "text": "Two hours on the water, covering roughly 4 miles of Lake Michigan shoreline. Plan on 2.5 hours total including check-in and orientation at Schauer Park."}},
        {"@type": "Question", "name": "Do I need kayaking experience for the Cave Point tour?", "acceptedAnswer": {"@type": "Answer", "text": "No. The tour is built for first-time paddlers. We use sit-on-top tandem kayaks, which are stable and easy to learn. Your guide handles route choice and weather calls."}},
        {"@type": "Question", "name": "Is the Cave Point kayak tour safe for kids?", "acceptedAnswer": {"@type": "Answer", "text": "Yes for kids age 8 and up paired with an adult in a tandem. Younger kids should look at the Door Bluff Shipwreck Tour from Garrett Bay, which has a minimum age of 4. Lake Michigan stays cold even in July, and PFDs are required."}},
        {"@type": "Question", "name": "What's included with the Cave Point tour?", "acceptedAnswer": {"@type": "Answer", "text": "Sit-on-top tandem kayak, paddle, and PFD are included. There is a 4 dollar Cave Point County Park vehicle fee paid at the entrance, separate from the tour price. Dry bags and phone dry bags are sold separately at our shop. Spray skirts are not used on sit-on-top tours."}},
        {"@type": "Question", "name": "What if the weather is bad?", "acceptedAnswer": {"@type": "Answer", "text": "We monitor wind and wave forecasts every morning. If conditions are unsafe at Cave Point, we move to a calmer route, reschedule, or refund. Free cancellation up to 24 hours before your tour."}},
        {"@type": "Question", "name": "Where do we meet for the Cave Point tour?", "acceptedAnswer": {"@type": "Answer", "text": "Schauer Park, just south of Cave Point County Park in Jacksonport, Wisconsin. Address and parking instructions are sent in your booking confirmation."}},
        {"@type": "Question", "name": "Can I do the Cave Point caves on a half-day instead?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The Cave Point Half-Day Kayak Tour is 4 hours and includes more time inside the caves, a longer paddle, and a shoreline picnic break. Strong recommendation for guests who can spare the morning."}}
      ]
    }
  ]
}
```

Issues inside this block before reuse: "$4" fee (see conflicts), "30-foot bluffs" (polished HUB says 40 to 60 feet; FS has no cliff height), "Schauer Park" meet point, "approximately 4 miles", validFrom/validThrough are 2026 season dates (stale for 2027), image path is a placeholder.

### Other placeholders called out in the pack

- reviewCount "2000": update to the real current count. Logo and hero image paths: use real assets. Opening hours validity: set to the 2027 season.
- Cana Island $145 is a placeholder; sauna price "[CONFIRM PRICE]"; Lakeshore comparison cells "[confirm]".
- Lead guide name for Person author: unresolved in A2, set to "Drifty" in S0.
- Sources: the pack says to validate every block in Google Rich Results Test and validator.schema.org.

---

## 4. Per-URL keyword targets already decided

"Not stated" means no doc gives it; nothing was invented. Titles and metas are quoted from the polished drafts, which were the intended versions. Slugs marked (planned) did not exist live as of 2026-08-16.

### 4a. Existing live URLs

| URL | Primary keyword | Secondary keywords | H1 | Title tag | Meta description |
|---|---|---|---|---|---|
| `/` | door county kayak tours (pos 4 to 5.5, branded #1) [B, A3] | door county kayaking (pos 8 to 9.8), kayak door county (3.8), kayaking door county (8.3 to 10.3), kayaking in door county (14.5), abandoned shipwreck kayak tour (homepage pos 18 at the time) [A3, B] | Current "Door County Kayak Tours" with TM; no new H1 stated | Not stated | Not stated |
| `/kayak-tours/cave-point-county-park/` | cave point kayak tour (pos 4.6, 271 imp) [A3] | cave point county park (1,453 imp, pos 16.4), cave point county park kayaking, kayak cave point [A3, B] | Not stated. S2 definition opener replaces first paragraph | Current "Cave Point County Park Kayak Tour \| Door County, Wisconsin"; A3 test idea "Cave Point Kayak Tour: Sea Caves & Cliffs (4.9 star, 240+ Reviews)" | Current ends "Book your tour online!" (full text not in docs) |
| `/kayak-tours/cave-point-whitefish-dunes-half-day-kayak-tour/` | cave point half day kayak tour [K] | 4 hour kayak tour, longer cave point tour [K] (840 imp, pos 28.3 [A1]) | Not stated | Not stated | Not stated |
| `/kayak-tours/door-bluff-county-park-shipwreck/` | abandoned shipwreck kayak tour (pos 17.6 to 24, 76 to 112 imp) [flagship draft, A3, B] | death's door shipwreck tour, door county shipwreck kayak tour, fleetwing shipwreck door county [polished flagship focus keywords] | Not stated | Not stated | Not stated |
| `/kayak-tours/door-bluff-shipwreck-1-2-day-kayak-tour/` | Not stated | Not stated | Not stated | Not stated | Not stated |
| `/kayak-tours/eco-estuary-tour/` | Not stated (pos 41.1; AI answers cite it for beginner kayaking) [A1, A3] | Not stated | Not stated | Not stated | Not stated |
| `/kayak-tours/cana-island-lighthouse-kayak-tour/` | cana island lighthouse tours (94 imp, pos 11.8) [B] | Cana Island (1,378 imp, pos 10.8) [A2] | Not stated | Not stated | Not stated |
| `/e-bike-tours/` and `/activities/cave-point-fat-tire-e-bike-tour/`, `/activities/e-bike-rental/` | Not stated on live pages | cave point e-bike tour family is under the planned pillar | Not stated | Not stated | Not stated |
| `/sauna-experience/`, `/airstream-sauna-rental/` | door county sauna / sauna door county (pos 2 to 2.3, 19 to 86 clicks) [A3, B] | airstream sauna (3.6) [B] | Not stated | Not stated | Not stated |
| `/kayak-rentals/` | door county kayak rental (pos 3.5) / kayak rentals door county (3) [B]; A3 shows the page itself at avg pos 33.5 | cave point kayak rental belongs to the planned `/cave-point-kayak-rental/` | Not stated | Not stated | Not stated |
| `/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/` | is kayaking safe during pregnancy / can i kayak while pregnant / kayaking while pregnant (pos 1.8 to 2.6) [B] | Not stated | Kayaking While Pregnant: What's Actually Safe (From Guides Who've Paddled With Hundreds of Expecting Moms) [polished] | Kayaking While Pregnant: What's Safe (Guide-Tested) | Is kayaking safe during pregnancy? Real guidance from Door County guides on what's safe, what's not, and which tours work for expecting paddlers. |
| `/blog/7-reasons-fish-creek-is-the-best-town-to-stay-at-in-door-county/` (live Fish Creek pillar) | things to do in fish creek [T]; fish creek / fish creek wi (2,730 / 2,649 imp, pos 11.3 to 11.7) [B] | fish creek wisconsin, fish creek door county, kayaking fish creek, peninsula state park kayak, fish creek restaurants [pillar focus keywords] | Live: "Fish Creek, Door County: The Walkable Bay Town" (polished and MEM) | Live (MEM): Fish Creek, Door County: Things to Do in the Walkable Town. Polished draft: Fish Creek: Door County's Most Walkable Bay Town | Polished: Fish Creek is the busiest, most walkable town on Door County's bay side. Where to eat, what to skip, and where to actually paddle. |
| `/blog/7-reasons-why-baileys-harbor-is-the-best-town-in-door-county/` (live Baileys pillar) | things to do in baileys harbor [T]; baileys harbor (2,287 imp, pos 11.8) [B] | baileys harbor wisconsin, baileys harbor door county, baileys harbor kayak, what to do in baileys harbor | Baileys Harbor, Door County: Where Repeat Visitors Pick | Live (MEM): Baileys Harbor, Door County: Things to Do on the Quiet Side. Polished draft: Baileys Harbor: Door County's Quiet Lake-Side Town | Baileys Harbor is the lake-side Door County town repeat visitors pick. Where to paddle, eat, and stay, from guides who run tours out of town. |
| `/blog/7-reasons-why-ephraim-is-the-best-town-to-stay-at-in-door-county/` (live Ephraim pillar) | things to do in ephraim [T]; ephraim wi (1,801 imp, pos 11.3) [B] | ephraim wisconsin, ephraim door county, kayaking ephraim, eagle harbor kayak, ephraim restaurants | Ephraim, Door County: The White Village on Eagle Harbor | Live (MEM): Ephraim, Door County: Things to Do in the White Village. Polished draft: Ephraim: The White Village on Door County's Eagle Harbor | Ephraim is Door County's white-buildings village on Eagle Harbor. Where to paddle, eat, and stay, from guides who tour the peninsula daily. |
| `/blog/how-far-can-a-kayak-hang-out-of-a-truck/` | Not stated (pos 2.8 to 2.9, 14,910 imp) | Not stated | Not stated | Not stated | Not stated |
| `/blog/different-types-of-kayaks-pros-and-cons/` | kayak pros and cons (pos 1.3) [B] | Not stated | Not stated | Not stated | Not stated |
| `/blog/door-county-bike-routes/` | Not stated (pos 7.2 to 7.5) | Not stated | Not stated | Not stated | Not stated |
| `/blog/cave-point-county-park/` (old "7 activities" post) | cave point county park | Not stated | Not stated | Not stated | Not stated |
| `/blog/door-county-guide-favorite-things-to-do/` | things to do in door county (615 imp, pos 19.5) [B] | Not stated | A Door County Guide's Favorite Things to Do (After 20+ Seasons Here); trimmed: A Door County Guide's Favorite Things to Do | Things to Do in Door County: A Guide's Favorites | A Door County guide's short list of favorite things to do. Real picks, real reasons, no AI listicle. Tours, towns, restaurants, and the stuff most visitors miss. |
| Other `/blog/...` slugs with polished title/meta | see section 5 | | | | |

### 4b. Planned Cave Point cluster (K, polished drafts, outlines). All slugs are planned, none confirmed live.

| URL (planned) | Primary keyword | Secondary keywords | H1 | Title tag | Meta description |
|---|---|---|---|---|---|
| `/cave-point/` (HUB) | cave point county park (5,815 imp per quarter at pos 16.6 on sister site) [K] | cave point, cave point door county, cave point wisconsin, what to do at cave point [polished focus keywords] | Cave Point County Park: What Locals Know About Door County's Sea Caves | Cave Point County Park: Local Guide to Door County Sea Caves | Wisconsin's only true sea caves sit inside Cave Point County Park. Here's everything you need: cliffs, caves, parking, and the one tour worth booking. |
| `/cave-point-kayak-tour/` | cave point kayak tour | tours, kayaking cave point door county, sea cave kayak tour, cliffs kayak tour, guided kayak tour cave point wisconsin [K]; polished adds cave point kayak tours, cave point sea cave kayak tour | Cave Point Kayak Tour: Paddle Into Door County's Sea Caves | Cave Point Kayak Tour: Inside Door County's Sea Caves | Paddle straight into the sea caves at Cave Point. 2-hour guided tour $69, half-day $145 (most guests upgrade). 4.9 stars from 240+ reviews. |
| `/cave-point-half-day-kayak-tour/` | cave point half day kayak tour | 4 hour kayak tour, longer cave point tour; $145, 4 hr [K] | Not drafted | Not drafted | Not drafted |
| `/cave-point-kayak-rental/` | cave point kayak rental | DIY, self-guided [K]; polished: kayak rental door county, cave point self-guided kayak, sea kayak rental cave point, kayak rental wisconsin | Cave Point Kayak Rental: What You Need to Know Before You Paddle | Cave Point Kayak Rental: $110/Day, Self-Guided Paddling | Cave Point kayak rental: $110/day. The honest take on launching solo, conditions to look for, and when to skip the rental and book a guided tour instead. |
| `/cave-point-sunrise-kayak-tour/` | cave point sunrise kayak tour | none | Cave Point Sunrise Kayak Tour | Cave Point Sunrise Kayak Tour: First Light on the Caves | Watch the sun come up over Lake Michigan from a kayak inside the Cave Point sea caves. 5:30am launch, 2 hours, limited dates. |
| `/cave-point-sunset-kayak-tour/` | cave point sunset kayak tour | none | Cave Point Sunset Kayak Tour | Cave Point Sunset Kayak Tour: Golden Hour at the Cliffs | Paddle the Cave Point cliffs as the sun drops over Door County. 6pm launch, 2 hours, photo-friendly small groups. (T says DCKT does not run a sunset tour) |
| `/cave-point-private-kayak-tour/` | cave point private kayak tour | private group kayak tour; custom by group size [K] | Not drafted | Not drafted | Not drafted |
| `/cave-point-ebike-tour/` | cave point e-bike tour | ebike rental, cave point to whitefish dunes ebike, fat tire rental [K]; polished: cave point ebike rental, fat tire bike rental cave point, door county e-bike tour | Cave Point E-Bike Tour: The Best Ride in Door County | Cave Point E-Bike Tour: The Best Ride in Door County | Ride a fat-tire e-bike from Cave Point through Whitefish Dunes State Park. Curvy roads, beach overlooks, 2-hour guided loop or self-guided rental. $99/rider. (FS: motor assist inside the state park is unconfirmed; 02b says not permitted) |
| `/cave-point-ebike-tour/` fall version (02b), proposed live path `/blog/cave-point-ebike-tour/` | cave point e-bike rental | cave point ebike, door county e-bike rental, fat tire bike rental cave point, jacksonport e-bike | Cave Point by E-Bike: The Easy Fall Ride from Jacksonport | Cave Point E-Bike Rental: Easy Fall Ride in Door County | Ride a fat-tire e-bike from our Jacksonport shop to Cave Point and Whitefish Dunes. Pedal assist does the hills. Rentals $30/hr, open daily this fall. |
| `/cave-point-winter-ebike-ice-caves/` | winter ebike tour cave point ice caves | cave point ice caves winter; price TBD [K] | Cave Point Winter E-Bike Tour: Ice Caves & Frozen Cliffs | Cave Point Ice Caves Winter E-Bike Tour | When Lake Michigan freezes the cliffs into ice castles, we take you out on studded fat-tire e-bikes. December through March, weather permitting. |
| `/best-time-cave-point-county-park/` | best time to visit cave point county park | polished focus: when to visit cave point, cave point season, cave point ice caves season, cave point parking | The Best Time to Visit Cave Point County Park (From Someone Who Lives Here) | Best Time to Visit Cave Point County Park: Month by Month | A local's guide to the best time to visit Cave Point County Park. Crowds, weather, ice caves, paddling conditions, and what to skip. |
| `/cave-point-county-park-parking-hours/` | cave point county park parking | hours, fees [K] | Cave Point County Park: Parking, Hours, and Entrance Fee | Cave Point County Park Parking, Hours & Entrance Fee | Cave Point County Park parking lot fills early in summer. Here's parking info, hours, fees (free!), overflow lots, and how to skip the lot entirely. |
| `/things-to-do-cave-point-door-county/` | what to do at cave point door county | none | Things to Do at Cave Point County Park | 9 Things to Do at Cave Point County Park (Local's Guide) | Cliff jumping, sea caves, hiking, kayaking, photography, picnicking. A local's guide to everything to actually do at Cave Point County Park. |
| `/cave-point-cliff-jumping-safety/` | cave point cliff jumping | swimming safety, is it safe [K] | Cave Point Cliff Jumping: What You Need to Know Before You Jump | Cave Point Cliff Jumping: Heights, Depths, Safety Guide | Cave Point cliff jumping is a Door County rite of passage. Heights, water depth, what to check before you jump, and the injury list nobody talks about. |
| `/how-to-get-to-cave-point/` | how to get to cave point | directions [K] | Directions to Cave Point County Park | How to Get to Cave Point County Park (From Anywhere in Door County) | Driving directions to Cave Point County Park from Sturgeon Bay, Fish Creek, Sister Bay, Bailey's Harbor, and Green Bay. Plus the road you don't want to miss. |
| `/dogs-at-cave-point-county-park/` | dogs at cave point county park | pet friendly [K] | Dogs at Cave Point County Park | Are Dogs Allowed at Cave Point County Park? (Yes, With Rules) | Cave Point County Park is dog-friendly with leash rules. Where they can go, where they can't, and what to know about the cliff trail with a dog. |
| `/cave-point-sea-caves/` | cave point sea caves | caves inside, what the caves look like [K]; polished: cave point caves inside, what cave point caves look like, sea caves wisconsin, sea caves lake michigan | Cave Point Sea Caves: A Look Inside Door County's Best-Kept Secret | Cave Point Sea Caves: What's Inside & How to See Them | The sea caves at Cave Point, carved by Lake Michigan over thousands of years. What's inside, how to see them, and the best way to actually paddle in. |
| `/cave-point-vs-whitefish-dunes/` | cave point vs whitefish dunes | none | Cave Point vs Whitefish Dunes State Park | Cave Point vs Whitefish Dunes: Which Should You Visit? | Cave Point and Whitefish Dunes share a parking road but offer totally different experiences. Cliff vs sand dune, kayak vs swim, free vs state park sticker. The real comparison. (FS: they do not share a parking lot; entrance to the state park is off Clark Lake Road) |
| `/cave-point-vs-peninsula-state-park-kayaking/` | cave point vs peninsula state park kayaking | none | Cave Point vs Peninsula State Park: Which to Kayak | Cave Point vs Peninsula State Park: Where to Kayak in Door County | Both are iconic Door County paddles, but they're nothing alike. Cave Point is sea caves and cliffs, Peninsula is sheltered bays and shipwrecks. Here's how to choose. |
| `/best-place-to-kayak-door-county/` | best place to kayak in door county | none | The Best Places to Kayak in Door County | The Best Place to Kayak in Door County (And Why) | A working list of the best Door County kayak spots, ranked by experience. Cave Point, Cana Island, Peninsula, Garrett Bay, Sister Bay, Sturgeon Bay. Where to go and why. |

Cave Point hub outline in K: embedded map, photos, "things to do at Cave Point" overview, links to all tours. Hub FAQ in the polished draft has 8 Qs (free?, swim, vs Whitefish Dunes, go inside the caves, cliff jumping legal, dogs, trail time, 2-hour vs half-day).

### 4c. Planned shipwreck, new, and supporting pages

| URL (planned) | Primary keyword | Secondary keywords | H1 | Title tag | Meta description |
|---|---|---|---|---|---|
| `/deaths-door-shipwreck-kayak-tour/` (S6 says use `/kayak-tours/door-bluff-county-park-shipwreck/` instead) | abandoned shipwreck kayak tour | death's door shipwreck tour, door county shipwreck kayak tour, garrett bay shipwreck kayak, fleetwing shipwreck door county, kayak shipwrecks lake michigan | Death's Door Kayak Tour: Sit Above a Real 1888 Shipwreck | Death's Door Kayak Tour: Paddle Over a Real Shipwreck | Paddle over a real 1888 shipwreck in clear, shallow water. 2-hour guided tour from Garrett Bay, Door County's most storied coast. Half-day with bluff hike $145. |
| `/blog/deaths-door-name-history/` | why is it called death's door | death's door legend, porte des morts history, death's door wisconsin name origin, death's door potawatomi | Before the Shipwrecks: The Battle That Named Death's Door | (SEO title) How Death's Door Wisconsin Got Its Name: A 1600s Legend | Why is it called Death's Door? A storm, a battle between the Potawatomi and Ho-Chunk in the 1600s, and a name the French heard and kept. The full story. |
| `/things-to-do-in-door-county/` | things to do in Door County (689 imp, pos 17) | Door County Wisconsin things to do (128 imp, pos 13.3), Door County family vacation, Door County in spring | Things to Do in Door County, Wisconsin: A Local Guide | Not stated | Not stated |
| `/door-county-kayak-tours-vs-lakeshore-adventures/` | Door County kayak tour vs Lakeshore Adventures | Lakeshore Adventures vs Door County Kayak Tours, best Door County kayak tour company | Door County Kayak Tours vs Lakeshore Adventures: An Honest Comparison | Door County Kayak Tours vs Lakeshore Adventures: Honest Comparison (2026) | Honest comparison of Door County's two biggest kayak tour companies, written by DCKT. Where Lakeshore wins, where DCKT wins, and where it's a toss-up. |
| `/door-county-itinerary/`, `/door-county-towns/` (T "Phase 2") | where to stay in door county, best door county town to stay in, bay side vs lake side door county, door county family vacation, door county weekend itinerary, where to kayak in door county [T secondary pool] | | Not stated | Not stated | Not stated |
| `/blog/lautenbachs-cherries-half-day-picnic/` (suggested) | Lautenbach's Orchard Country | Door County dried cherries, Door County tart cherry juice, Fish Creek orchard, half-day kayak tour Door County | Why We Pack Lautenbach's Cherries on Our Half-Day Picnic | Lautenbach's Cherries on Our Door County Kayak Picnic | Lautenbach's Orchard Country supplies the dried cherries and tart cherry juice on our half-day kayak picnic. Here's the family behind them. |
| `door-county-fall-color-e-bike-ride` (slug only) | door county fall colors bike ride | door county e-bike rental, fall color ride door county, jacksonport e-bike, cave point fall | A Fall Color E-Bike Ride on Door County's Quiet Side | Door County Fall Color E-Bike Ride from Jacksonport | An easy fall e-bike loop from our Jacksonport shop to Clark Lake, Cave Point, and Whitefish Dunes. Pedal assist does the hills. Rentals from $30/hr. |

Other tracked queries not tied to a page in the docs: A1's 20 priority queries (best kayak tours Door County, Cave Point kayak tour, Door County kayak tour for beginners, Door County shipwreck kayak tour, Death's Door kayak tour, kayaking while pregnant, kayaking merit badge requirements, types of kayaks pros and cons, things to do in Door County, Door County family vacation, Fish Creek Wisconsin things to do, Baileys Harbor things to do, Ephraim Wisconsin things to do, Door County kayak rental, Door County e-bike rental, Door County sauna, Door County in spring, best Door County tour company, kayak Cave Point safe for kids, Door County bachelorette ideas). Competitor-owned SERPs to avoid fighting on price: Bayshore Outfitters owns "ephraim kayak tour" at $50 [T].

---

## 5. Copy already written and polished

"Live?" is from MEM/A4/SI as of their dates. Quality flags refer to the fact conflicts at the top and to FS. All polished drafts carry paste-ready FAQ JSON-LD and a sticky-sidebar HTML block and have had a /copy-mentors pass (2026-05-05). Slugs in the drafts are planned slugs.

### 5a. Cave Point cluster (`SEO Content/Cave Point/`)

| File | Target URL | H1 | What it is | Live? / flags |
|---|---|---|---|---|
| 01a Cave Point HUB (POLISHED), 350 lines | `/cave-point/` | Cave Point County Park: What Locals Know About Door County's Sea Caves | Destination hub: where/how to get there, what's at the park, things to do, when to visit, parking/fees/dogs, what you'll see, why kayak, FAQ (8), schema | Not live (A4). Flags: "$4 fee", "400-million-year-old", "only true sea caves", "since 2013", "about 19 acres", cliffs "40 to 60 feet", water "glows turquoise / clear to 30 feet" (see section 6). The older "(DESTINATION)" file is the pre-polish draft |
| 01 Cave Point Kayak Tour (POLISHED), 276 lines | `/cave-point-kayak-tour/` (live product page is `/kayak-tours/cave-point-county-park/`) | Cave Point Kayak Tour: Paddle Into Door County's Sea Caves | Pillar tour page: above-fold 2-hr vs half-day, what you do, why half-day, who it's for, included, bring/buy, tour times (8:30, 11:00, 1:30, 4:00), why book with DCKT, FAQ (8 Qs) | Not live. Flags: $4 fee, 4.9/240+ reviews, "only Cave Point tour with 200+ five-star reviews", sunrise/sunset links, min age 8 |
| 02 Cave Point E-Bike Tour (POLISHED), 210 lines | `/cave-point-ebike-tour/` | Cave Point E-Bike Tour: The Best Ride in Door County | Guided/self-guided e-bike pillar with half-day kayak cross-sell | Not live (404). 02b lists claims cut as unverified ("nobody else runs", "most photographed pavement", "ridden 200 times") |
| 02b Cave Point E-Bike (Fall 2026 Publish Version), 104 lines | proposed `/blog/cave-point-ebike-tour/` | Cave Point by E-Bike: The Easy Fall Ride from Jacksonport | Rental-first fall rewrite: $30/hr, $60/2hr, $90/3hr, route notes, motor-off in state park. Built 2026-10-07 | Not live, "blocked at WP 2FA". Distance "about 4.5 miles" is long vs FS 4.1 |
| 03 Cave Point Sea Caves (POLISHED), 184 lines | `/cave-point-sea-caves/` | Cave Point Sea Caves: A Look Inside Door County's Best-Kept Secret | What caves look like, how they formed, from land, how to go inside, FAQ | Not live. Geology line "Niagara Escarpment dolomite, 400+ million years" and "10,000 years since the glaciers retreated" |
| 04 Best Time to Visit Cave Point (POLISHED), 199 lines | `/best-time-cave-point-county-park/` | The Best Time to Visit Cave Point County Park (From Someone Who Lives Here) | Short answer, month by month, time of day, cliff jumping, caves, FAQ. Says water "rarely cracks 72F", mid-50s in May | Not live. Water temps not in FS |
| 05 Cave Point Kayak Rental (POLISHED), 205 lines | `/cave-point-kayak-rental/` | Cave Point Kayak Rental: What You Need to Know Before You Paddle | Honest rental page; $110/day confirmed 2026-05-05; delivery to park still an open question | Not live |
| 06 Supporting Pages (Outlines), 11 outlines | see section 4b | see section 4b | Outlines with URL, title, meta, H1, H2 list; not drafted copy | Not live |
| 07 Backlink Outreach Plan; `_publish-artifacts.md`; `_publish-session-prep.md` | n/a | n/a | Process docs | Reference only |

### 5b. Town pillars (`SEO Content/Towns/`)

| File | Target URL | H1 | What it is | Live? / flags |
|---|---|---|---|---|
| 01 Baileys Harbor (POLISHED), 278 lines | planned `/baileys-harbor-door-county/`; live at `/blog/7-reasons-why-baileys-harbor-is-the-best-town-in-door-county/` | Baileys Harbor, Door County: Where Repeat Visitors Pick | Sections: Why people pick, What to do, Where to eat and drink, Where to stay, When to come, How to get there, Bay side or lake side, What to bring, FAQ (8) | Published in place 2026-06-07 (about 2,020 words). Backup of old post in `Towns/_backups/` |
| 02 Fish Creek (POLISHED), 260 lines | live at `/blog/7-reasons-fish-creek-is-the-best-town-to-stay-at-in-door-county/` | Fish Creek, Door County: The Walkable Bay Town | Same pattern plus "Is the drive to Cave Point worth it?"; FAQ (7); pitches e-bike rental plus a drive east to Cave Point | Published in place 2026-06-07 (about 1,635 words). Draft references `/fish-creek-fat-tire-e-bike-rental/` which does not exist; live is `/activities/e-bike-rental/` |
| 03 Ephraim (POLISHED), 251 lines | live at `/blog/7-reasons-why-ephraim-is-the-best-town-to-stay-at-in-door-county/` | Ephraim, Door County: The White Village on Eagle Harbor | Same pattern plus "rent in Ephraim or drive to Cave Point"; FAQ (8, incl. Wilson's, dry village referendum 2016) | Published in place 2026-06-07 (about 1,805 words) |
| PILLAR files (01, 02, 03) | | | Earlier drafts, superseded | History |

### 5c. Shipwreck and history (`SEO Content/Shipwreck Tour/`)

| File | Target URL | H1 | What it is | Live? / flags |
|---|---|---|---|---|
| 01 Death's Door Shipwreck Kayak Tour (POLISHED), 272 lines | `/deaths-door-shipwreck-kayak-tour/` (map to `/kayak-tours/door-bluff-county-park-shipwreck/`) | Death's Door Kayak Tour: Sit Above a Real 1888 Shipwreck | Flagship tour page; corrected to Potawatomi + Ho-Chunk; meta duration bug fixed | Not live (404). The (FLAGSHIP) file (429 lines) is an earlier draft with a VERIFY section |
| 03 Death's Door Potawatomi History (BLOG), 235 lines | `/blog/deaths-door-name-history/` | Before the Shipwrecks: The Battle That Named Death's Door | Story-led naming-legend post | Blocked on Ho-Chunk Nation review (emailed 2026-05-06) |
| 02 WordPress Publish Brief | n/a | n/a | Process | Reference |

### 5d. Blog Polished (`SEO Content/Blog Polished/`)

| File | Target URL | H1 | One line | Live? |
|---|---|---|---|---|
| embracing-kayaking-during-pregnancy (POLISHED) | `/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/` | Kayaking While Pregnant: What's Actually Safe (From Guides Who've Paddled With Hundreds of Expecting Moms) | Top traffic post, light polish, links to Cave Point, Eco Estuary, half-day | unknown |
| door-county-things-to-do (POLISHED) | `/blog/door-county-guide-favorite-things-to-do/` | A Door County Guide's Favorite Things to Do | Operator-voice picks plus heavy internal linking, aims at "things to do in door county" | unknown |
| how-many-days-in-door-county (POLISHED) | `/blog/how-many-days-do-i-need-in-door-county/` | How Many Days Do You Actually Need in Door County? | Decision tree: 2 days floor, 4 sweet spot, 7 | unknown |
| best-hiking-trails-in-door-county (POLISHED) | `/blog/7-of-the-best-hiking-trails-in-door-county/` | The Best Hiking Trails in Door County (From Someone Who Lives Here) | Trail picks tied to town pillars | unknown |
| eagle-trail-peninsula-state-park (POLISHED) | `/blog/discover-peninsula-state-parks-eagle-trail-the-ultimate-hiking-experience-for-adventure-seekers/` | Eagle Trail in Peninsula State Park: The Honest Hiker's Guide | Real trail description, links Fish Creek pillar | unknown |
| winter-activities-door-county (POLISHED) | `/blog/7-must-do-winter-activities-in-door-county/` | Winter in Door County: What's Actually Worth the Trip | Links ice-caves e-bike (not a live product per 02b), sauna, towns | unknown |
| sauna-rentals-over-bar-hopping (POLISHED) | `/blog/discovering-door-county-the-health-benefits-of-sauna-rentals-over-bar-hopping/` | Why a Door County Sauna Beats Another Night Bar Hopping | Reinforces pos-2 sauna rankings, links sauna pages | unknown |
| 4th-of-july-door-county (POLISHED) | `/blog/door-county-fireworks-4th-of-july/` | 4th of July in Door County: The Real Fireworks Schedule | Annual repost; dates must be refreshed each year | unknown |
| barmuda-triangle (POLISHED) | `/blog/the-barmuda-triangle-husbys-the-bowl-jjs-la-puerta/` | Sister Bay's Barmuda Triangle: Husby's, the Bowl, and JJ's | Three Sister Bay bars verified operating 2026-05-04 | unknown |
| whistling-swan (POLISHED) | `/blog/whistling-swan/` | The Whistling Swan: A Fish Creek Restaurant Worth the Reservation | Verified operating 2026-05-04 (4192 Main St, Tue-Sat 5-9pm) | unknown |
| clark-lake-logan-creek (POLISHED) | `/blog/clark-lake-logan-creek/` (keep slug) | Clark Lake & Logan Creek vs. Rieboldt Creek: The Door County Wetland Paddle Comparison | Pivots page-2 "clark lake door county" traffic to the Eco Estuary tour; Logan Creek is exclusive to Peninsula Kayak Company | unknown |
| best-summer-job-door-county (POLISHED) | `/blog/door-countys-best-summer-job/` | The Best Summer Job in Door County: Kayak Guide | Recruiting post, links `/jobs/` | unknown |
| kiteboarding-door-county (POLISHED) | `/blog/kiteboarding-door-county/` | Kiteboarding in Door County: Where, When, and Who's Teaching | Niche informational, DCKT sells no kite product | unknown |
| sup-paddleboarding-door-county (POLISHED) | `/blog/what-are-the-best-places-to-sup-in-door-county/` | Where to Paddleboard in Door County (And Where Not To) | SUP spots; paddleboard product status unconfirmed | unknown |
| why-sit-on-top-kayaks (POLISHED) | slug open: inherit `/blog/different-types-of-kayaks-pros-and-cons/` or new | Why We Run Sit-On-Top Kayaks (And Why You'll Be Glad We Do) | Story post on the sit-in incident and fleet switch | not live (SI) |
| fish-creek-listicle (REDIRECT-ONLY) | n/a | n/a | Decision note: redirect, do not polish; superseded by in-place rewrite | history |
| _light-touch-edits | 9 posts: pregnancy, truck overhang, bike routes, kayak types, blisters, rainy-day kids, bachelorette, Ephraim Fyrball, Sister Bay cheese curds | n/a | Mechanical edits only (strip em dashes, add 2 to 3 internal links) | unknown |

### 5e. Other publish-ready or near-ready copy

| File | Target URL | H1 | What it is | Live? |
|---|---|---|---|---|
| AI SEO Action Plan / 02 Tour Page Copy Rewrites | 7 tour URLs (section 1 row 3) | n/a (definition openers, 40 to 60 words) | Opener + softened existing prose + visible FAQ HTML for each tour | unknown |
| AI SEO Action Plan / 03 Pregnancy Post Update | pregnancy post | n/a | ACOG paragraph, FAQ H3 block (7 Qs), "Last updated" line | unknown |
| AI SEO Action Plan / 05 New Pages | `/things-to-do-in-door-county/` and `/door-county-kayak-tours-vs-lakeshore-adventures/` | Things to Do in Door County, Wisconsin: A Local Guide; Door County Kayak Tours vs Lakeshore Adventures: An Honest Comparison | Hub = structure + 5 FAQ; comparison = near-complete copy with table, "where Lakeshore wins / DCKT wins / equivalent", 6 FAQ | not live; comparison has "[confirm]" cells |
| AI SEO Action Plan / 04 Outreach Drafts | off-site | n/a | Wikipedia, Tripadvisor merge, Travel Wisconsin / DDC listing copy, Reddit AMA, GBP FAQ posts, outdoor pitch | not for the site |
| Fall Color E-Bike Ride from Jacksonport (DRAFT) | `/blog/door-county-fall-color-e-bike-ride/` | A Fall Color E-Bike Ride on Door County's Quiet Side | Rental-only fall post with [VERIFY] items | not live, "do not publish" |
| Local Partners / 01 Lautenbachs Orchard Country (DRAFT) | `/blog/lautenbachs-cherries-half-day-picnic/` | Why We Pack Lautenbach's Cherries on Our Half-Day Picnic | Partner post, first in a "Picnic Partners" series (443 lines) | not live; partner review first |
| Backlink Outreach / 02 Guest Blog Post (Door County Activities) | off-site (offered to partners) | n/a | Linkable asset with 3 contextual links | off-site |

---

## 6. Facts and claims to carry over

From FS (researched 2026-10-14). Anything the sheet marks UNVERIFIED is flagged. Use "about" for all acreage. Do not carry the unverified items as fact.

### Cave Point County Park (county land, not part of the state park)
- Size: 18.6 acres with 900 ft of shoreline (county page); draft 2026-2030 Parks Plan says 19.3. **Say "about 19 acres".**
- Address: 5360 Schauer Road, Jacksonport. County-owned since gifts from three families in 1943 and 1945.
- Next door to Whitefish Dunes State Park. Say "next door to", not "inside" (Wikipedia calls it an enclave; DNR does not).
- Hours: all Door County parks open 1/2 hour before sunrise to 11:00 PM unless posted. Not seasonal per the county rules page.
- **Fee: no entry fee on any official page; "free" is inferred, UNVERIFIED.** The county draft plan budgets a "Park pass collection system" at Cave Point ($35,000, 2027); re-check before any 2027 evergreen says free or $4. Call Facilities and Parks, 920-746-9959. Do not use the state park sticker for Cave Point.
- Geology: Niagara Escarpment dolomitic limestone ("dolostone"), the rock ridge under all of Door County (DNR). Age safe wording: "about 400 million years old (Silurian)". **425 million is UNVERIFIED as an exact DNR quote.**
- Sea caves: formed by wave action working along joints in the rock; frost probably helps enlarge them (Wisconsin Geological and Natural History Survey). Most entrances are at water level, perpendicular to shore; one cave has three entrances and runs about 100 ft parallel to shore. WGNHS: "Most of these are best seen from the water."
- Facilities: restrooms (the county's first solar-powered one), picnic tables, grills, a gazebo/shelter. Bike rack: not mentioned by any official source, UNVERIFIED, do not promise. Winter restroom status: UNVERIFIED.
- Safety: weather changes rapidly; rocks slippery when wet or icy (county page). No lifeguard, swim at your own risk. Cliff jumping: no written county rule, but Door County Emergency Services (director Aaron LeClair, July 2022) urged against it: "There have been deaths there over the years"; shallow water, big waves, swift currents; a woman was injured jumping about 20 ft into about 6 ft of water; six or seven injury/distress calls per year. Winter ice wording from doorcounty.com is UNVERIFIED (search summary only).
- Cave Point also lists bow hunting as a current use (draft plan). The "cave closed Oct 1 to May 15 for bats" in the county plan is Horseshoe Bay Cave at Frank E. Murphy park, not the Cave Point sea caves.
- Not in FS (do not infer): cliff heights, water clarity or depth at Cave Point, water temperature, "only sea caves in Wisconsin" claim, 44.9263 N / 87.1817 W coordinates, parking lot size, "a mile south of Whitefish Dunes".

### Whitefish Dunes State Park
- 867 acres (DNR history page); some sources say 865. Say "about 865 acres" or 867. The State Natural Area is 256 acres on a different DNR page; 230 acres were designated in 1982. Do not mix them up.
- Old Baldy: tallest dune in the park, 93 feet above lake level, with an observation platform over Lake Michigan and Clark Lake. "Tallest in Wisconsin" is inconsistent across DNR pages; safest: tallest dune in the park, and the park's dunes are the highest on Lake Michigan's western shore.
- Fragile dunes: stay on boardwalks, stairs and trails; do not climb the dunes. Old Baldy boardwalk not maintained in winter.
- Hours: open year-round 6 a.m. to 8 p.m., main gate opens 8 a.m. (DNR info page). Open in November.
- Trails: 14.5 miles of hiking trails and 1.5 miles of sandy beach. Black Trail 2.1 mi (1.2 mi short loop), Brachiopod Trail 1.5 mi interpretive accessible loop, Green 1.8, Yellow 3.7, Yellow Spur 0.6, Red 1.2 out and back to Old Baldy, Red Pine 0.25, Clark Lake Spur 0.3, Whitefish Creek Spur 0.3 (winter page says 0.4). Which hiking trail connects to Cave Point: UNVERIFIED.
- Beach: no lifeguards, dangerous rip currents possible; if caught, swim parallel to the shore.
- Admission for cyclists: rules are written for motor vehicles, so exemption is an inference; **UNVERIFIED as plain DNR statement.** Confirm with park office, 920-823-2400. State trail pass for Whitefish Dunes bike routes: UNVERIFIED.
- Biking allowed on designated bike trails only (Red Trail near the office to S. Cave Point Drive, Third Beach access to Clark Lake Road, office to Schauer Road); not on beach, dunes or hiking trails. FS says do not tell guests to ride the Red Trail to Old Baldy.
- **E-bike motors inside the state park: UNVERIFIED.** Statewide rule NR 45.05(3)(em): class 1 and 3, under 15 mph, only on listed or posted e-bike trails. Whitefish Dunes is not on the DNR e-bike table FS loaded. Class 2 is not in the rule. FS safer phrasing: "Motor off inside the state park". Get written confirmation from 920-823-2400 before stating as fact.
- Hunting: Nov 15 to Dec 15 window on a third-party map from 2014, UNVERIFIED against the current DNR map.
- History: DNR says evidence of eight separate occupations from 100 B.C. to the late 1800s; North Bay people (100 B.C. to A.D. 300), Heins Creek about A.D. 500 to 750, Oneota about A.D. 900; National Register of Historic Places; fishing a major reason for repeated occupation. Respectful wording: "people lived and fished here for roughly 2,000 years". Replica wigwam settlement is from doorcounty.com, not DNR.
- Clark Lake: 865 acres, max depth 25 ft, very clear water (DNR lake page); formed when drifting sand closed off Clark Bay. Entrance to the state park is on Clark Lake Road; DNR says there is no access to the state park entrance from South Cave Point Drive.

### Distances and dates
- Shop (6329 State Hwy 57, Jacksonport) to Cave Point lot by bike: about 4.1 miles one way, roughly 26 minutes (OpenStreetMap router, map-derived, not ridden): Hwy 57 0.56 mi, Lake Shore Road 0.91, Cave Point Drive 1.08, Schauer Road 1.49. **Safe line: "about 4 miles one way."** Drafts that say 4.5 are slightly long.
- Researched 2026-10-14; the draft county plan is dated 2026-02-12.

### FS's "safe to say" list (verbatim intent, 20 items)
Cave Point about 19 acres with 900 ft of shoreline; Niagara Escarpment dolomite; caves carved by waves along cracks, frost helps widen; county land so the state sticker does not apply; parks open 30 min before sunrise to 11 p.m.; restrooms, tables, grills, first solar restroom; slippery rocks and fast weather; officials say do not cliff jump; no lifeguards at county parks; Whitefish Dunes about 867 acres, open year-round 6 a.m. to 8 p.m.; Old Baldy 93 ft with observation platform; highest dunes on Lake Michigan's western shore; dunes are fragile; 14.5 miles of trail and 1.5 miles of beach; Brachiopod Trail 1.5 mi loop; occupation from about 100 B.C. to the late 1800s, Oneota about A.D. 900, NRHP; Clark Lake 865 acres, up to 25 ft deep, cut off by drifting sand; no lifeguards and rip currents at the Whitefish beach; biking only on designated routes; about 4 miles one way from the Jacksonport shop.

### Other facts used in the SEO docs (not in FS, treat as business facts to re-verify)
- Prices: Cave Point 2-hr $69, half-day $145; Door Bluff 2-hr $69, half-day $145; Eco Estuary $65; Cana Island $145 (placeholder); guided e-bike $99; e-bike rental $30/hr; kayak rental $110/day.
- Ages: Cave Point 8+, Door Bluff 4+, Eco Estuary 6+ (polished town/tour drafts) with S1 saying 1.5 to 2 hours. Policy: free cancellation up to 24 hours; sit-on-top tandems only; dry bags sold separately; no spray skirts; no ACA certification claim.
- Death's Door history: strait named in the mid-1600s after a Potawatomi and Ho-Chunk battle and storm, both sides lost warriors; Schooner Fleetwing sank in 1888; verified wrecks named in S2: Fleetwing (1888), A.P. Nichols, Forest, J.E. Gilmore (1892). Ho-Chunk review pending (Bill Quackenbush, THPO).
- Local color verified in memory: Wilson's Restaurant & Ice Cream Parlor (since 1906); Ephraim Moravian founding 1853; Ephraim dry until 2016 referendums (56% and 68%); Peninsula Players founded around 1936; Ridges Sanctuary 1937 first land trust in Wisconsin. All need the "verify local details" pass before reuse.

---

## 7. Competitor gaps (Peninsula Kayak Company, CG dated 2026-06-19)

Caveat: CG is a content-gap read of peninsulakayakcompany.com, not a ranking export. It does not list queries PKC ranks for. It names topics PKC leaves uncovered, which are DCKT opportunities. Other competitor ranking facts come from A1/A3/T.

PKC profile (CG): based on Logan Creek near Cave Point / Whitefish Dunes; tours: Cave Point, Eagle Bluff, Wetland, Sunset, Fireworks, Ephraim Historical, plus SUP and e-bikes; short sales blurbs; blog, FAQ, Meet the Team; FAQ covers age 4+, weight limits 40 to 250 lb, "no experience needed", weather refunds; name-drops "Niagara Escarpment", "425 million years", "dolostone" without explaining.

What PKC leaves open (CG gaps) and what content would close each. None of the pages below exist yet per the docs. "Partial draft" means a vault draft covers part of it.

| CG gap | Query the doc names | Page or section that closes it | Status |
|---|---|---|---|
| 1 Fear and safety dodged (swimming, tipping, cold) | "should I even book this" anxiety search | Idea 1 "Do I Need to Know How to Swim to Kayak in Door County?"; idea 2 "What Actually Happens If Your Kayak Tips Over (And Why It Rarely Does on a Guided Tour)"; query "what if I flip kayak Lake Michigan" | not drafted |
| 2 Cave Point geology named but not taught | "how were Cave Point caves formed" | Idea 6 "How the Cave Point Caves Were Made: A Plain-English Guide to Dolostone and the Niagara Escarpment". Partial draft: "How they formed" section in Sea Caves polished. Use FS for the facts | partial draft |
| 3 Shipwrecks and Death's Door history absent | "Fleetwing shipwreck / kayak over shipwreck"; "why is it called Death's Door Wisconsin" | Idea 4 "The Fleetwing Shipwreck: Kayaking Over a 19th-Century Schooner in Death's Door"; idea 5 "Why Is It Called Death's Door? The Real History Behind Porte des Morts". Partial draft: Shipwreck flagship POLISHED + Potawatomi history BLOG (blocked on Ho-Chunk review) | partial draft, not live |
| 4 Water temp and seasonality is one vague line | "Lake Michigan water temperature June Door County"; "best month to kayak Door County" | Idea 3 "How Cold Is Lake Michigan? Door County Kayak Water Temps by Month (May-October)"; idea 9 "Best Time of Year to Kayak Door County: A Month-by-Month Honest Breakdown". Partial draft: Best Time polished (month by month, water temps unverified in FS) | partial draft |
| 5 Photography implied, never coached | "Cave Point photography / kayak photo tips" | Idea 10 "How to Photograph the Cave Point Caves From a Kayak (Without Dropping Your Phone)" | not drafted |
| Kids and age readiness | "kayak tour with kids / minimum age" | Idea 7 "Can Kids Kayak at Cave Point? An Honest Age and Readiness Guide for Door County" (PKC says only "ages 4+") | not drafted |
| First-timer expectations | "first time kayaking what to expect" (PKC answers "NONE") | Idea 8 "First-Time Kayaker's Survival Guide to a Door County Tour (What Nobody Tells You)" | not drafted |

CG's build order: ideas 4, 5, 6 first (shipwreck, Death's Door, geology: DCKT's moat; PKC structurally will not follow). Ideas 1 to 3, 7, 8 are the bigger traffic play (high-anxiety searches every operator avoids). Link each answer page to the matching tour. CG note: fold into the same push once WP login is restored.

Other competitor gaps from the audits
- **Lakeshore Adventures** leads "best kayak tours Door County" and "Door County kayak vs Lakeshore Adventures"; flagship is a clear-bottom shipwreck tour at Baileys Harbor. Closing pages: comparison page and the Death's Door/clear-bottom positioning (lead with the wreck story, not the hull). Lakeshore, CPPP, Kayak Guide Justin and Door County Adventure Center all lack TouristTrip + Offer + FAQ schema: a clean lead if shipped [A1, A2, S5].
- **Bayshore Outfitters** owns "ephraim kayak tour" and several Sister Bay / Sturgeon Bay rental SERPs at $50. Do not compete on price; Ephraim pillar says honestly "rent locally, or drive 30 minutes east for Cave Point" [T].
- **cavepointpp.com (sister brand)** currently beats the main site on the highest-value Cave Point commercial queries; also owns kayak sizing (79 clicks), stay dry in sit-on-top (52), calories burned kayaking (50) informational posts [A3]. Differentiation plan in K: 4.9 stars / 200+ TripAdvisor reviews (CPPP about 17 on the same product), longest-running operator, real guide names and faces. Decide whether to consolidate [A3] or differentiate [K].
- **Broad "things to do / family vacation" queries** go to Destination Door County, Travel Wisconsin and Tripadvisor; DCKT has no hub page. Closing page: `/things-to-do-in-door-county/` [A1, S5].
- **AI-search presence**: DCKT is cited for Cave Point, beginner kayaking (Eco Estuary named), shipwreck, pregnancy queries; absent from Wikipedia's Door County article; Tripadvisor listings fragmented across four; thin Reddit. Fixes are off-site (section 1d) [A1].
- **Peninsula Kayak Company exclusive**: Logan Creek access. DCKT answers with the Eco Estuary on Rieboldt Creek via the Clark Lake / Logan Creek polished post [Blog Polished].
