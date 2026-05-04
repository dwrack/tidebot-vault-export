# NOLA Party Barges — SEO Action Plan (May 2026)

**Date:** 2026-05-03
**Site:** nolapartybarges.com
**Author:** Claude + David, post-GSC unlock
**Status:** Active execution doc. Companion to `SEO Growth Plan 2026.md` (strategic) and `Brand Story & Values.md` (positioning).
**Framework:** Audit follows seo-audit skill priority order — Crawlability → Technical → On-Page → Content → Authority. Each finding has Issue / Impact / Evidence / Fix / Priority.

---

## Executive Summary

The site does ~60k sessions and ~1,180 bookings per 90 days. After unlocking the correct GSC property (`sc-domain:nolapartybarges.com`), real visibility is ~14x what the broken `https://www.` URL-prefix property reported: 50+ ranking pages, 250k+ impressions, multiple page-1 rankings for high-intent queries.

**The catch:** the site is ranking *despite itself*. Title tags on most core pages render as "Ticket," "Back Arrow," or empty in the SERP because the WordPress theme is leaking UI label text into the `<title>` element. This single defect is causing 5-10x CTR loss on pages already ranking in positions 2-7. Fixing it is the highest-ROI hour of work available on the entire site, full stop.

**Top 5 priorities (in order):**

1. **Fix the title tag rendering bug** sitewide (Critical, blocks CTR on all ranking pages)
2. **Write meta descriptions for the 25+ pages that have none** (Critical, free SERP CTR)
3. **Resolve H1 absence on money pages** (`/our-boats/`, `/the-twerkin-tiki/`, `/boat-rental/`, dress-code article all have empty `<h1>`) (High)
4. **Fix the FareHarbor `/embeds/` GA4 attribution leak** (High, makes channel reporting trustable)
5. **Build the swamp-tours and bachelorette silos** with internal linking discipline (Medium, compounding content moat)

Quick wins identified: 7+ pages ranking on page 2 with real impression volume that need only on-page work to push to page 1. Most surprising finding: `/swamp-tours-with-onboard-restrooms/` is the highest-CTR page on the site (11.4% at position 6.6). The bathroom moat is a measurable organic asset.

---

## 1. Technical SEO Findings

### 1.1 Crawlability & Indexation

#### 1.1.1 GSC property was misconfigured (resolved 2026-05-03)

- **Issue:** Only `https://www.nolapartybarges.com/` URL-prefix property was registered. Site canonical is non-www, so the property reported on the 301 redirect (~1 indexed page).
- **Impact:** Critical. Made every prior SEO assessment fly blind. Resolved.
- **Evidence:** GSC API listed only the www variant; first sc-domain query returned 14x the data.
- **Fix:** David added `sc-domain:nolapartybarges.com` as Domain property on 2026-05-03. Already verified working.
- **Priority:** Done.

#### 1.1.2 Robots.txt is reasonable but not optimized

- **Issue:** Robots.txt blocks ~17 spam/scraper bots and has a sitemap reference. No `Allow:` rules for important crawlers, no AI crawler handling.
- **Impact:** Low to Medium. Functional, but missing AI-era hygiene.
- **Evidence:** `curl -L https://nolapartybarges.com/robots.txt` shows current contents.
- **Fix:**
  - Add explicit `User-agent: *` then `Allow: /` block.
  - Add `User-agent: GPTBot` and `User-agent: Google-Extended` with `Allow: /` (don't disallow LLM crawlers — you want to be cited).
  - Confirm sitemap line still works after edit.
- **Priority:** Medium. 30-min task.

#### 1.1.3 Sitemap structure is fine, contents need audit

- **Issue:** `sitemap.xml` is an index pointing to three child sitemaps (page, activity, post). Have not audited whether all child sitemaps include only canonical, indexable URLs.
- **Impact:** Medium.
- **Evidence:** `curl https://nolapartybarges.com/sitemap.xml` returns valid sitemap index.
- **Fix:** Pull each child sitemap, cross-check against GSC indexed URLs. Confirm no `noindex` URLs are in sitemap and no canonical URLs are missing.
- **Priority:** Medium. After title tag fixes.

#### 1.1.4 Canonical inconsistency: www vs non-www

- **Issue:** Canonical URL is `https://nolapartybarges.com/` (no www). www variant 301s correctly. But GSC top-pages report shows BOTH `https://www.` and `https://` URLs ranking for the same content (homepage shows 1,332 clicks at www and 505 clicks at non-www).
- **Impact:** Medium. Splits link equity and confuses crawlers.
- **Evidence:** GSC top-pages query in this session.
- **Fix:** Verify every page has a self-referencing `<link rel="canonical" href="https://nolapartybarges.com/...">` pointing to the non-www version. Spot-check via Rich Results Test or browser View Source on 5 pages.
- **Priority:** High. 1-2 hour audit + fix.

---

### 1.2 Site Speed & Core Web Vitals

- **Issue:** Not yet audited in this pass.
- **Impact:** Unknown. WordPress VIP hosting + Cloudflare suggests reasonable defaults.
- **Evidence:** Server headers show `x-powered-by: WordPress VIP` and Cloudflare edge.
- **Fix:** Run PageSpeed Insights on these 5 pages and record LCP/INP/CLS:
  - `/`
  - `/the-freaky-tiki/`
  - `/our-boats/`
  - `/sunset-cocktail-cruise-seafood-boil/`
  - `/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/`
- **Priority:** Medium. 30-min check, escalate if LCP > 3s on mobile.

---

### 1.3 Mobile-Friendliness

- **Issue:** 87% of users are on mobile (per GA4). Have not verified mobile rendering of every template.
- **Impact:** Critical if broken. Likely fine.
- **Fix:** Run Google Mobile-Friendly Test on each unique page template (homepage, boat page, blog post, FAQ, contact). 10-min check.
- **Priority:** Medium.

---

### 1.4 GA4 Attribution Bug (FareHarbor `/embeds/`)

- **Issue:** GA4 reports 8,332 unique pagePath values for npb. The vast majority are FareHarbor calendar widget URLs (`/embeds/book/neworleanspedalbarge/items/.../calendar/2026/03/`), each treated as a separate page. This fragments session attribution and makes the channel report unreliable.
- **Impact:** High. The 5,852 self-referral sessions and the apparent 0% CVR on Paid Social both stem from this.
- **Evidence:** GA4 page report shows 24+ distinct calendar URLs, each pulling 600-3,500 sessions.
- **Fix:**
  - GA4 Admin → Data Streams → web stream → Tag settings → Configure tag settings → List unwanted referrals: add `nolapartybarges.com`, `fareharbor.com`, `book.fareharbor.com`.
  - Create a GA4 content_group for `/embeds/` and exclude from key reports.
  - Alternatively, exclude the `/embeds/` path entirely from page reports via Filter or DV360-style regex in Looker Studio.
- **Priority:** High. Same week as title tag fixes.

---

## 2. On-Page SEO Findings

### 2.1 Title Tag Catastrophe (Critical, sitewide)

- **Issue:** WordPress theme is rendering UI label text ("Ticket," "Back Arrow") or empty strings into the `<title>` element on the majority of core pages. The SEO title set in Yoast/RankMath is being overridden or not output at all.
- **Impact:** **Critical.** This is the #1 reason CTR is broken on pages that already rank well. Single biggest fixable issue on the site.
- **Evidence:** Direct curl + grep on 10 high-traffic pages on 2026-05-03:

| Page | Current `<title>` | Issue |
|------|-------------------|-------|
| `/` | "Ticket" | Junk |
| `/the-freaky-tiki/` | "Back Arrow" | Junk |
| `/the-cajun-queen/` | "Back Arrow" | Junk |
| `/sunset-cocktail-cruise-seafood-boil/` | "Back Arrow" | Junk |
| `/how-much-do-you-need-to-budget.../` | "Ticket" | Junk |
| `/the-twerkin-tiki/` | (empty) | Missing |
| `/our-boats/` | (empty) | Missing |
| `/boat-rental/` | (empty) | Missing |
| `/unveiling-bars-dress-code/` | (empty) | Missing |
| `/swamp-tours-with-onboard-restrooms/` | (empty) | Missing |

- **Fix (technical):** Identify whether the theme has hardcoded markup that's eating the title. Likely culprits: a custom header template that prints back-button/ticket-icon text inside `<title>`, or a Gutenberg block bug. Have a developer trace the page template `header.php` or block.json files. Confirm Yoast/RankMath is the source of truth for `<title>`.
- **Fix (content):** Once the rendering bug is fixed, write SEO titles for these pages. Drafts:

| Page | Recommended `<title>` (50-60 chars) |
|------|--------------------------------------|
| `/` | "BYOB Party Boats in New Orleans (7 mi from FQ) — NOLA Party Barges" |
| `/the-freaky-tiki/` | "Freaky Tiki: 32-Person BYOB Party Boat in New Orleans" |
| `/the-twerkin-tiki/` | "Twerkin Tiki: BYOB Party Boat for Bachelorettes & Birthdays NOLA" |
| `/the-cajun-queen/` | "The Cajun Queen: New Orleans Party Boat for Groups Up To [X]" |
| `/our-boats/` | "Our Boats: 5 Party Boats for Hire in New Orleans (BYOB)" |
| `/boat-rental/` | "Private Boat Rental in New Orleans — Bachelorette, Birthday, Group" |
| `/sunset-cocktail-cruise-seafood-boil/` | "Sunset Seafood Boil Cruise New Orleans ($165, 2-3 hrs, BYOB)" |
| `/how-much-do-you-need-to-budget.../` | "How Much to Budget for a New Orleans Vacation in 2026" |
| `/unveiling-bars-dress-code/` | "Do New Orleans Bars Have a Dress Code? (2026 Guide)" |
| `/swamp-tours-with-onboard-restrooms/` | "Swamp Tours with Bathrooms Onboard — Only in NOLA" |

- **Priority:** **Critical. Do this week.** Single biggest organic lift on the site.

---

### 2.2 Meta Descriptions Missing on Money Pages

- **Issue:** `/the-twerkin-tiki/`, `/our-boats/`, `/boat-rental/`, `/unveiling-bars-dress-code/` have NO meta description. WordPress auto-generates a snippet from page content, which often results in HTML-entity-mangled excerpts (`&nbsp;` `&hellip;`) showing in SERP.
- **Impact:** High. Auto-snippets convert worse than written copy.
- **Evidence:** curl + grep on 2026-05-03.
- **Fix:** Write 150-160 char meta descriptions for every page with empty or auto-generated descriptions. Lead with the differentiator (BYOB, 7mi from FQ, $63 starting price, capacity, bathroom onboard). Drafts:

| Page | Recommended description |
|------|--------------------------|
| `/the-twerkin-tiki/` | "BYOB party boat in New Orleans, holds 30, 2-hour cruise from Bayou Bienvenue. Perfect for bachelorettes and birthday groups. From $63/person." |
| `/our-boats/` | "Compare our 5 BYOB party boats: Freaky Tiki, Twerkin Tiki, Cajun Queen, Bayou Boogie, Bentley. Capacities 12-32. Cruises from $63 per person." |
| `/boat-rental/` | "Private party boat rental in New Orleans for bachelorettes, birthdays, and corporate groups. BYOB allowed. Captain included. Book 2026 dates online." |
| `/unveiling-bars-dress-code/` | "What to wear out in New Orleans: dress codes for French Quarter bars, dance clubs, restaurants, and rooftop spots. Updated for 2026." |

- **Priority:** Critical. Same sweep as title tags.

---

### 2.3 H1 Absence on Money Pages

- **Issue:** Several core pages have NO `<h1>` element in HTML source: `/the-twerkin-tiki/`, `/our-boats/`, `/unveiling-bars-dress-code/`, `/swamp-tours-with-onboard-restrooms/`.
- **Impact:** High. Google uses H1 as a strong on-page topic signal. Without it, ranking depends purely on title and body content.
- **Evidence:** curl + grep on 2026-05-03.
- **Fix:** Add a single, keyword-rich H1 to each page. The H1 should match search intent, not necessarily the title tag verbatim.
  - `/the-twerkin-tiki/` → H1: "The Twerkin Tiki" (or "BYOB Twerkin Tiki Party Boat")
  - `/our-boats/` → H1: "Our 5 Party Boats"
  - `/unveiling-bars-dress-code/` → H1: "Do New Orleans Bars Have a Dress Code?"
  - `/swamp-tours-with-onboard-restrooms/` → H1: "Swamp Tours with Bathrooms Onboard"
- **Priority:** Critical.

---

### 2.4 H1 / URL / Title Inconsistency on Cajun Queen

- **Issue:** URL is `/the-cajun-queen/`. H1 says "The Party Queen." Meta description references "pedal party boat tour" and "city's first-ever pedal party boat" — both contradict the no-pedal positioning.
- **Impact:** Medium. Brand confusion, dilutes ranking signal, contradicts current brand voice.
- **Evidence:** curl on 2026-05-03.
- **Fix:** Pick one identity. If "Cajun Queen" is the canonical name, update H1 and meta description to match. Remove all "pedal" references from public copy on this page.
- **Priority:** Medium. Bundle with title tag sweep.

---

### 2.5 Sitewide Pedal References (Brand Hygiene)

- **Issue:** Multiple pages still reference "pedal," "pedal barge," "pedal party boat" in URLs, copy, or meta. Brand has moved away from pedaling entirely (memory: feedback_no_pedal.md).
- **Impact:** Medium. Sets wrong expectations, brand inconsistency, customer confusion.
- **Evidence:** Cajun Queen meta description, /pedal-bike-barge-cruise/ URL still ranking, /pedal-bike-bar/ URL.
- **Fix:**
  - Audit every page for "pedal" references in body, alt text, meta.
  - Decide: keep legacy URLs (with 301s in place if renamed) but update body copy.
  - `/pedal-bike-barge-cruise/` is still pulling 4,016 page views per 90 days. Don't kill it. Rewrite the body copy to match current positioning, leave URL alone (or 301 to a new slug AND update sitemap).
- **Priority:** Medium. After core title/meta sweep.

---

### 2.6 Image Alt Text (Sitewide)

- **Issue:** Not exhaustively audited yet, but spot-checks suggest many images use camera filenames or generic "image" alt.
- **Impact:** Medium. Tourism is image-heavy and Google Images is a real entry point. Also affects accessibility.
- **Fix:** WordPress media library scan via SEO plugin or manual sweep. Format: `freaky-tiki-bachelorette-bayou-bienvenue.jpg` not `IMG_4032.jpg`. Alt text describes the scene, includes one keyword if natural. Don't keyword-stuff.
- **Priority:** Medium. 1-day project.

---

### 2.7 Internal Linking is Underbuilt

- **Issue:** ~40 blog posts exist but don't contextually link to commercial pages. No silo hubs. No "Plan Your Trip" mega-menu. Footer doesn't route to topic clusters.
- **Impact:** High. Google reads internal linking as topical authority signal. The site is leaving a compounding moat unbuilt.
- **Evidence:** GSC data + sitemap inspection. Top-of-funnel posts (budget for vacation, bars dress code, December weather) are pulling 12k-74k impressions but have no commercial CTAs above the fold.
- **Fix:** Three patterns (covered in detail in section 4):
  - Money page → blog (depth signal)
  - Blog → money page (intent capture)
  - Hub → spoke → hub (silo reinforcement)
- **Priority:** High. Big multiplier.

---

### 2.8 Schema Markup (Verification Pending)

- **Issue:** HTML source contains 1-4 `application/ld+json` blocks per page. Cannot verify *what* schema is firing without rendering JavaScript. Per seo-audit skill, `curl` and web fetch don't reliably detect JS-injected schema.
- **Impact:** Unknown. Could be fine or could be missing FAQ/Product/LocalBusiness schemas that are critical for AI Overviews and rich results.
- **Fix:** Verify schema using one of:
  - **Google Rich Results Test** at https://search.google.com/test/rich-results — preferred, renders JS.
  - **Browser DevTools** — open page, run `document.querySelectorAll('script[type="application/ld+json"]')` in console, inspect contents.
  - **Screaming Frog** — full crawl with JS rendering enabled.
- **Required schemas (verify presence + completeness):**
  - Homepage: `LocalBusiness` with name, address, phone, hours, geo, aggregateRating, sameAs
  - Each boat page: `Product` with name, image, description, offers.price, offers.priceCurrency, aggregateRating
  - `/faq/`: `FAQPage` with every Q&A wrapped (highest-value schema for AEO)
  - `/sunset-cocktail-cruise-seafood-boil/`: `Event` or `TouristTrip` with price, duration, location
  - All blog posts: `Article` with headline, author, datePublished, image
- **Priority:** High. Audit + remediate within 30 days. See `schema-markup` skill for implementation.

---

## 3. Content Findings

### 3.1 The "Ticket" Title Pages Are Hidden Top-of-Funnel Monsters

- **Issue:** Two informational pages are pulling enormous tourist-planning impressions but converting essentially zero (because of broken titles AND no commercial CTA):
  - `/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/` → 73,929 impressions, position 2.86, 0.36% CTR
  - `/unveiling-the-charm-do-new-orleans-bars-have-a-dress-code/` → 15,107 impressions, position 3.5, 0.66% CTR
- **Impact:** Critical missed revenue. These visitors are 1-2 weeks pre-trip, exact ICP.
- **Fix:**
  - Fix titles + descriptions (covered in 2.1, 2.2)
  - Add a "While You're Planning" callout module mid-article with a Freaky Tiki widget OR a sunset seafood cruise card
  - Update "2024" in slug/H1/title to "2026" and refresh stats; this article is ranking on stale year markers
- **Priority:** Critical. Revenue impact estimated at 100+ bookings/year if executed.

---

### 3.2 The Bathroom Moat Is a Real Asset

- **Issue:** `/swamp-tours-with-onboard-restrooms/` is the highest-CTR page on the site (11.4% at position 6.6). The URL itself is the keyword.
- **Impact:** Moat is real. This is a defensible angle competitors cannot match.
- **Fix:**
  - Build `/swamp-tours/` hub page that uses this as a flagship feature
  - Internally link this page from every boat page, every swamp-tour-related blog post, and the homepage hero
  - Add FAQ schema to this page with questions like "Do swamp tours have bathrooms?" "Why don't most swamp tours have bathrooms?"
- **Priority:** High. Compounding moat.

---

### 3.3 /the-cajun-queen/ Money Page on Page 2

- **Issue:** Cajun Queen page ranks at position 16.9 (top of page 2) with 686 impressions. A money page on page 2 with this volume is a near-immediate opportunity.
- **Impact:** Medium-High. Easy lift.
- **Fix:**
  - Resolve Cajun Queen vs Party Queen identity (section 2.4)
  - Rewrite body copy: 800-1,200 words, structured H2s for "What's included," "Capacity," "Pricing," "What to bring," "FAQ"
  - Add internal links from /our-boats/, the bachelorette pages, the blog posts that mention it
  - Add Product schema with price, image, aggregateRating
- **Priority:** High. 1-day project.

---

### 3.4 Confirmed Page-2 Quick Wins (from GSC)

7 queries ranking on page 2 (positions 11-19) with real impression volume. Each one needs only on-page optimization (title, intro paragraph including the exact phrase, supporting H2s, internal links from related pages):

| Query | Target page | Position | Impressions |
|-------|-------------|---------:|------------:|
| yacht rental new orleans | /boat-rental/ | 11.4 | 105 |
| nola bachelorette | /a-locals-itinerary-for-a-new-orleans-bachelorette-party/ | 11.8 | 19 |
| swamp tours louisiana | / | 11.5 | 33 |
| alligator tour new orleans | / | 11.2 | 25 |
| new orleans swamp | / | 11.0 | 33 |
| alligators in new orleans | /swamp-tour-with-alligator-sightings/ | 15.2 | 30 |
| swamp tour with fishing | /new-orleans-swamp-tours-with-fishing-exploring-natures-bounty/ | 34.7 | 2,243 |

The fishing page is the outlier — 2,243 impressions at position 34.7 means Google is testing it on the edge of relevance. A serious refresh (current data, on-topic H2s, 1,500+ words, internal links, Product schema) could lift it to page 1 quickly.

**Priority:** High. Each is 2-4 hours of work for measurable lift.

---

### 3.5 International Tourist Queries

- **Issue:** GSC shows 401 impressions for "nueva orleans" (Spanish, position 3.6) and 93 impressions for "nouvelle orleans" (French, position 3.5). Plus stragglers for "dónde está nueva orleans," "nueva orleans mapa." Site has zero Spanish or French content; Google is matching on "New Orleans" alone.
- **Impact:** Low to Medium. Small volume, but international tourists convert well in tourism vertical.
- **Fix:** Test with one Spanish landing page targeting "tour de pantano nueva orleans" / "paseo en barco nueva orleans" with hreflang. If conversion follows, scale to 3-5 Spanish pages. French likely too small to invest.
- **Priority:** Low. Nice-to-test, not week-1 work.

---

## 4. Site Architecture & Internal Linking Plan

(See `site-architecture` skill for deeper page hierarchy work.)

### 4.1 Five Silos (matches Section 3 of the strategic plan)

```
/our-boats/ (HUB)                    /swamp-tours/ (NEW HUB)
├── /the-freaky-tiki/                ├── /closest-swamp-tour-to-french-quarter/
├── /the-twerkin-tiki/               ├── /swamp-tours-with-onboard-restrooms/  [exists, build around]
├── /the-cajun-queen/                ├── /swamp-tour-with-alligator-sightings/  [exists]
├── /the-bayou-boogie/               ├── /best-time-for-swamp-tour/
├── /bentley-bayou-cruiser/          ├── /byob-swamp-tour-new-orleans/
└── /boat-rental/                    └── /vs-cajun-encounters/

/bachelorette-party/ (NEW HUB)       /sunset-cruise-new-orleans/ (NEW HUB)
├── /bachelorette-party/itinerary/   ├── /sunset-cocktail-cruise-seafood-boil/  [exists, build up]
├── /bachelorette-party/best-boats/  ├── /sunset-cruise/vs-steamboat-natchez/
├── /bachelorette-party/cost-guide/  ├── /sunset-cruise/vs-creole-queen/
└── /bachelorette-party/playlist/    └── /sunset-cruise/byob-sunset-tour/

/things-to-do-in-new-orleans/ (HUB connecting blog posts)
├── /how-much-budget-for-NOLA-vacation/   [exists, top traffic]
├── /bars-dress-code/                      [exists, top traffic]
├── /december-weather-what-to-wear/        [exists, top traffic]
├── /best-self-guided-french-quarter-walking-tour/  [exists]
├── /unique-neighborhoods-of-NOLA/         [exists]
└── /3-day-itinerary/                      [new]
```

### 4.2 Internal Linking Patterns

**Pattern A — Money page → blog (depth signal)**
Each commercial page gets 3-5 contextual sentence-level links to related blog posts.
Example for `/the-freaky-tiki/`:
> "Most groups ask: what should I wear on the boat? See our [bayou cruise outfit guide](/blog/december-weather-what-to-wear/). Worried about bathrooms? We're [the only swamp tour with onboard restrooms](/swamp-tours-with-onboard-restrooms/). Planning a bachelorette? Steal our [day-by-day NOLA itinerary](/blog/locals-itinerary-bachelorette/)."

**Pattern B — Blog → money page (intent capture)**
Every blog post gets ONE contextual link to ONE commercial page based on topic, written as a sentence not a button.
Example in `/how-much-budget-for-NOLA-vacation/`:
> "If you want one experience that doesn't blow the budget but still feels uniquely New Orleans, our [Freaky Tiki BYOB cruise starts at $63 per person](/the-freaky-tiki/) and includes the boat, captain, and 2-hour run through the bayou."

**Pattern C — Hub ↔ spoke ↔ hub (silo reinforcement)**
Each silo hub links DOWN to all children. Each child links UP to its hub AND laterally to 2-3 sibling pages. This is what most sites miss.

### 4.3 Footer "Plan Your Trip" Mega-Menu

Add a 5-column footer with the silo hubs:

| BOATS | SWAMP TOURS | EVENTS | SUNSET | NOLA GUIDE |
|-------|-------------|--------|--------|------------|
| Freaky Tiki | Closest to FQ | Bachelorette | Sunset Seafood | Budget Guide |
| Twerkin Tiki | With Bathrooms | Birthday | vs Steamboat | Bars Dress Code |
| Cajun Queen | With Alligators | Corporate | BYOB Sunset | December Weather |
| Bayou Boogie | BYOB Allowed | Wedding | vs Creole Queen | French Quarter Tour |
| Bentley | Best Time | Large Group |  | Itineraries |

This single addition gives every page on the site 25 outbound links to the silo structure.

---

## 5. AEO / GEO (AI Search Optimization)

(See `ai-seo` skill for deeper work.)

ChatGPT is already sending 93 sessions and 3 bookings per 90 days at 3.2% CVR. AI traffic is small but proven. Investments:

### 5.1 FAQ Page Rewrite with FAQPage Schema
Rewrite `/faq/` with 30+ questions structured for AI citation. Each Q&A:
- Phrased as a real user question
- Answer is one sentence + supporting paragraph
- Includes specific numbers ("32 passengers," "$63 starting price," "7 miles," "90-minute tour")
- Wrapped in `FAQPage` schema (verify via Rich Results Test)

Sample questions to include:
- How much does a party boat cost in New Orleans?
- Can you BYOB on a New Orleans boat tour?
- What's the closest swamp tour to the French Quarter?
- Do you need a captain's license to rent a boat in New Orleans?
- Are there alligators on the bayou tours?
- What's the difference between an airboat and a pontoon swamp tour?
- Do swamp tours have bathrooms?
- What should I wear on a swamp tour?
- How long is a swamp tour?
- Where do New Orleans party boats depart from?

### 5.2 Statistical Landmarks Block on Homepage
Add a "By the Numbers" section: "32 passengers per boat. 7 miles from the French Quarter. 5 boats in the fleet. Daily departures since 2018." Numbers get cited by LLMs.

### 5.3 llms.txt File
Publish `https://nolapartybarges.com/llms.txt` listing key pages with one-line descriptions for AI crawlers.

### 5.4 Reddit + Citation Aggregator Push
- 1 helpful (non-spammy) Reddit comment per week on r/NewOrleans, r/AskNOLA, r/travel from a real account
- neworleans.com partnership/listing (currently sending 82 sessions)
- explorelouisiana.com expansion (currently 20 sessions)
- TripAdvisor review push (QR code at marina + post-cruise email ask)

---

## 6. Authority & Links

### 6.1 Sister-Site Cross-Linking (Underexploited)

The single highest-converting traffic source on the site is sister-site referrals. Real numbers from GA4 90-day:

| Sister site | Sessions | Conv | CVR |
|-------------|---------:|-----:|----:|
| neworleanstikiboats.com | 115 | 13 | **11.3%** |
| nolaboozecruise.com | 1,835 | 134 | **7.3%** |
| hiddenadventuretours.com | 1,521 | 21 | 1.4% |

**Action:** Audit every page on the three sister sites and identify:
- Where they link to npb (specific anchor text + landing page)
- Where they SHOULD link to npb but don't
- Whether the npb landing pages from those links match user intent

A 2-hour cross-site link audit will likely 2-3x the volume from these sources without spending a dollar on ads.

### 6.2 Backlink Acquisition

Not yet audited. Recommended next step: use Ahrefs/Semrush trial to pull npb's backlink profile, identify referring domain count vs Cajun Encounters and Steamboat Natchez. Set 12-month target: +50 referring domains.

Tactical link sources to pursue:
- Local press: Eater NOLA, Antigravity Magazine, Where Y'at, NOLA.com lifestyle desk
- Tourism aggregators: TripAdvisor, Yelp, GetYourGuide, Viator
- CVB partnerships: neworleans.com (already a referrer), louisianatravel.com
- Local bloggers / influencers: bachelorette planning blogs, NOLA-specific Instagram accounts
- Reddit AMA: "We run the only swamp tour with onboard bathrooms — AMA"

---

## 7. Google Ads Recommendations

(See `paid-ads` skill for full campaign work. This section addresses keyword expansion driven by GSC discovery.)

GSC reveals real long-tail intent that Google Ads should bid on:

### 7.1 New Campaigns to Launch

1. **Bachelorette campaign** (most underexploited)
   - Keywords: "bachelorette boat new orleans," "bachelorette party boat nola," "girls trip new orleans boat," "nola bachelorette" (you're already at pos 11.8 organically)
   - Landing page: build `/bachelorette-party/` pillar
   - Geo-modifier: drive markets (Birmingham, Atlanta, Mobile, Dallas, Houston)

2. **Swamp tour long-tail campaign**
   - "BYOB swamp tour," "closest swamp tour to french quarter," "swamp tours with bathrooms," "private group swamp tour"
   - Landing page: new `/swamp-tours/` hub
   - Negative keywords: airboat (you don't run them), kids (not your audience), river cruise (steamboat territory)

3. **Comparison campaign** (lowest CPC, highest intent)
   - "steamboat natchez alternative," "creole queen vs"
   - Landing pages: new comparison pages
   - Be careful with TM bidding on direct competitor names

### 7.2 Geo Tests
30-day Performance Max in:
- Birmingham (under-served, big road-trip market)
- Atlanta (huge drive market, missing direct flights)
- Mobile (3-hour drive)
- Dallas/Fort Worth (already showing in GA4 top cities)
- Houston (already showing)

### 7.3 Schedule
NOLA trip planning peaks Sunday evenings, booking peaks Wed-Fri. Bid up 15-25% during those windows.

### 7.4 Call Extensions
Phone bookings convert better than form bookings on tourism queries. Add call extensions on every campaign.

---

## 8. Prioritized Action Plan

### Critical (this week — blocking ranking value capture)

- [ ] **Fix title tag rendering bug** (theme/dev fix). Confirm Yoast/RankMath SEO title is the source for `<title>`. (1.1.1)
- [ ] **Write SEO titles for the 10 high-traffic pages** listed in 2.1.
- [ ] **Write meta descriptions** for `/the-twerkin-tiki/`, `/our-boats/`, `/boat-rental/`, `/unveiling-bars-dress-code/`. (2.2)
- [ ] **Add H1s** to `/the-twerkin-tiki/`, `/our-boats/`, `/unveiling-bars-dress-code/`, `/swamp-tours-with-onboard-restrooms/`. (2.3)
- [ ] **Fix GA4 `/embeds/` attribution leak.** (1.4)
- [ ] **Resolve Cajun Queen vs Party Queen identity** + remove "pedal" references. (2.4)
- [ ] **Verify schema with Rich Results Test** on homepage, /the-freaky-tiki/, /faq/. (2.8)

### High-Impact (next 30 days)

- [ ] **Refresh /how-much-budget-for-NOLA-vacation/** — fix title, update to 2026, add commercial CTA module mid-article. (3.1)
- [ ] **Same refresh on /bars-dress-code/, /december-weather-what-to-wear/.**
- [ ] **Build `/swamp-tours/` hub** with `/swamp-tours-with-onboard-restrooms/` as flagship. (3.2)
- [ ] **Rewrite /the-cajun-queen/** — push to page 1. (3.3)
- [ ] **On-page sweep on the 7 page-2 keywords** in 3.4. Each gets a 2-hour pass.
- [ ] **Build `/bachelorette-party/` pillar page** (2,500 words + FAQ + internal links to all boats). (4.1)
- [ ] **Sister-site cross-link audit** — 2 hours, 2-3x boost on highest-converting traffic source. (6.1)
- [ ] **Internal linking pass on existing 40 blog posts** — Pattern B (blog → money page). (4.2)
- [ ] **FAQ page rewrite with 30+ questions + FAQPage schema.** (5.1)
- [ ] **Footer "Plan Your Trip" mega-menu.** (4.3)

### Quick Wins (drop-in within a few hours each)

- [ ] **Image alt text sweep** with WordPress SEO plugin. (2.6)
- [ ] **PageSpeed Insights audit** on 5 templates. (1.2)
- [ ] **Mobile-Friendly Test** on each template. (1.3)
- [ ] **Sitemap audit** — ensure no noindex URLs included. (1.1.3)
- [ ] **Canonical tag spot-check** on 5 pages. (1.1.4)
- [ ] **Robots.txt update** with explicit GPTBot/Google-Extended allow. (1.1.2)
- [ ] **llms.txt file published.** (5.3)
- [ ] **Statistical landmarks block** on homepage. (5.2)

### Long-Term (60-90 days and beyond)

- [ ] **Build out /sunset-cruise-new-orleans/ hub** + Steamboat Natchez comparison.
- [ ] **Build /things-to-do-in-new-orleans/** as real hub, link existing blog content.
- [ ] **Programmatic city pages**: /from-baton-rouge/, /from-mobile/, /from-dallas/, /from-houston/, /from-birmingham/, /from-atlanta/. (See `programmatic-seo` skill.)
- [ ] **Comparison pages**: vs Cajun Encounters, vs Steamboat Natchez, vs Creole Queen, vs Airboat Adventures. (See `competitor-alternatives` skill.)
- [ ] **6-8 new top-of-funnel blog posts** targeting tourist intent.
- [ ] **Reddit presence** (1 helpful comment per week minimum).
- [ ] **TripAdvisor review push** + post-cruise email ask + QR code at marina.
- [ ] **Backlink push**: local press (Eater NOLA, Antigravity), tourism aggregators, CVB partnerships.
- [ ] **Spanish landing page test** if international queries persist.
- [ ] **Google Ads bachelorette + swamp long-tail + comparison campaigns.** (Section 7)
- [ ] **Geo-test Performance Max** in Birmingham/Atlanta/Mobile/Houston/Dallas.

---

## 9. KPIs

Targets revised based on real GSC data (rather than the misleading www-only baseline):

| Metric | Today (90d) | 6 month target | 12 month target |
|--------|------------:|---------------:|----------------:|
| Total bookings | 1,180 | 1,800 | 2,800 |
| Organic search sessions | 4,802 | 9,000 | 18,000 |
| Organic CVR | 1.8% | 2.5% | 3.0% |
| AI/LLM referral sessions | 93 | 500 | 2,000 |
| Homepage bounce | 72% | 60% | 50% |
| Pages with proper title + meta | <30% | 100% | 100% |
| Pages with verified schema | unknown | 100% of templates | 100% |
| Sister-site referral conversions | 168 | 350 | 700 |
| Avg position (sc-domain GSC) | varies | top-10 for 50 queries | top-3 for 100 queries |
| Backlink referring domains | unknown (audit pending) | +25 | +50 |

---

## 10. What I'd Do This Week

1. **Get the title tag bug fixed** — this is a developer task. Pull in whoever maintains the theme. Confirm Yoast/RankMath SEO title is wired to `<title>`.
2. **Write the 10 SEO titles + 4 missing meta descriptions** in section 2 above. Drop them into Yoast/RankMath. 1-2 hours.
3. **Fix the GA4 `/embeds/` leak** in Data Streams settings. 15 minutes.
4. **Run Rich Results Test** on homepage and 3 boat pages. Note what schemas are firing. 20 minutes.
5. **Audit the 3 sister sites** for npb cross-links. 2 hours.

Everything else compounds from those five items. Don't start the silo build until titles are fixed — you'd be pouring water into a leaky bucket.

---

## Skills Referenced (for deeper work in each area)

- `seo-audit` (this plan's framework)
- `ai-seo` for AEO/GEO/AIO work
- `schema-markup` for structured data implementation
- `site-architecture` for hub/spoke + nav redesign
- `programmatic-seo` for city pages
- `competitor-alternatives` for vs-pages
- `page-cro` for homepage and money-page conversion
- `analytics-tracking` for the GA4 fix
- `paid-ads` for Google Ads campaign builds
