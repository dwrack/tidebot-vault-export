---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-14
status: REPORT ONLY — NO CHANGES APPLIED
---

# REPORT ONLY — no changes applied to live site, WordPress, GBP, or ads. Pending David's review.

This document was generated unattended via the `/seo-audit` and `/tech-seo` skills. Nothing here has been published, edited, redirected, or changed on the live site, WordPress, Google Business Profile, or any ad platform. Every item below is a recommendation awaiting David's sign-off.

---

## Data sources & gaps (read this first)

**Live-verified today (2026-08-14, this session):** robots.txt, sitemap.xml, homepage redirect chain, HTTP status on 30 site URLs (0 broken), JSON-LD schema types pulled directly from page source (Python regex against raw HTML, not a summarized fetch) on the homepage, `/tours/swamp/`, `/alligators-vs-crocodiles/`, and the Manchac tour page, internal-link presence check from the alligator page to the three target money pages, and the Honey Island archive's meta description.

**Not available this session, same as the prior same-day pass:**
- **GSC MCP** — `google-nkst` is configured in `.mcp.json` but no `gsc_*`/search-console tools loaded this session (checked via ToolSearch under multiple queries: gsc, search console, keywords, google-nkst). No fresh GSC pull was possible.
- **GA4 MCP** — same server, same result. No fresh GA4 session/conversion pull was possible.
- **GBP MCP** — not connected this session either. No live listing/category check.
- **PageSpeed Insights** — keyless quota returned `429 RESOURCE_EXHAUSTED` on a direct API call. No `PSI_KEY` on file at `~/.claude/.env`. Confirmed via direct `curl` against the PSI v5 endpoint, not just the runner script.

**What this report is built on instead — real data, no invented numbers:**

| Source | Date | What it gives us |
|---|---|---|
| Live checks run today, this session | 2026-08-14 | robots.txt, sitemap.xml, 30-URL status crawl, raw JSON-LD schema extraction on 4 key pages, internal-link check, meta description check |
| `Marketing/SEO + Tech SEO Audit — 2026-08-14.md` | Earlier today (13:27) | An earlier same-day pass with an identical data-availability picture (GSC/GA4/GBP/PSI all unavailable then too) — cross-checked against this session's independent live re-verification; findings match |
| `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md` | 2026-08-10 | Real GSC 90-day query/position/impression data, DataForSEO volume cross-check, live AI Overview/AI-search test, schema audit, GBP local-pack snapshot |
| `Marketing/SEO Audit 2026-05-04.md` | 2026-05-04 | Prior GSC pull, internal-linking recommendations, baseline |
| `Analytics Report — March 2026.md` | 2026-03-26 | Real GA4 data (property 401824264) — sessions, channel conversion, top pages, conversion-tracking gap |
| `Marketing/Competitor Content-Gap Analysis — Wild Louisiana (June 2026).md` | 2026-06-19 | Direct competitor content-gap research |
| `~/Projects/tech-seo/out/psi-20260619.json` | 2026-06-19 (56 days old) | Last successful PSI run — the only CWV/Lighthouse data point available, flagged stale below |

**Bottom line on freshness:** nothing has shipped since either the Aug 10 or the earlier-today (13:27) audit. This session independently re-pulled the four highest-priority pages' schema and link state directly from live HTML and confirmed every open item below is still open — this is not a copy of the earlier report, it's a re-verification that reached the same conclusion. Recommend re-running once the GSC/GA4/GBP MCP connections are fixed and a `PSI_KEY` is on file — until then, keyword position/impression/volume numbers below are sourced from the Aug 10 pull (4 days old) and GA4 figures from March (5 months old, directional only).

---

## Executive summary

NKST has real assets working against it structurally: 1,416 reviews at 4.9 stars, a 272k-impression/quarter alligator blog, and a page-1 win on the smaller version of its core keyword ("new orleans swamp tours," pos 7) — but the wrong pages are ranking for the money terms, zero commercial schema exists anywhere on the site, and a direct competitor (Wild Louisiana Tours) is winning the AI Overview answer for "best swamp tour New Orleans" with more extractable copy. Live re-verification today confirms nothing has moved: the alligator page's link block to `/tours/swamp/` is still missing, the two duplicate "best swamp tour" posts are both still live, `/tours/swamp/` still carries only BreadcrumbList schema, and the Honey Island blog-archive URL is still winning a 9,900/mo keyword over the real tour page with auto-generated boilerplate as its meta description.

**Top 3 priorities by impact:**
1. Ship the "more reading" internal-link block from `/alligators-vs-crocodiles/` to `/tours/swamp/` and `/swamp-tours-new-orleans-guide/` — confirmed live today that only the Manchac tour page gets a link from this 272k-impression/quarter page; recommended in May, recommended again in August, still not live.
2. Add Product + Offer + AggregateRating + FAQPage schema to the 6 tour pages and homepage — confirmed via raw HTML extraction today: zero commercial schema anywhere on the site despite 1,416 reviews at 4.9 sitting in plain text.
3. Fix the two duplicate-content problems: 301 `/which-is-the-best-swamp-tour-around-new-orleans/` into `/which-swamp-tours-are-the-best/`, and resolve the Honey Island URL collision where a blog category archive outranks the real tour page for a 9,900/mo term.

---

## 1. Keyword opportunity table

Source: GSC 90-day pull from the 2026-08-10 audit (window 2026-05-12 to 2026-08-09), volume cross-checked against DataForSEO. Page/position assignments re-verified live today where named.

| Keyword | Position | Volume/mo (corrected) | Tier | Recommended action |
|---|---|---|---|---|
| swamp tours new orleans | 15 (homepage ranks, not the money page) | ~1,100–4,000 | Page 2 hostage — biggest single opportunity | Build out `/tours/swamp/` as the real target; link to it from the alligator page and homepage |
| swamp tour new orleans | 21 | ~3,000–10,000 | Page 3 | Same fix; same money page |
| new orleans swamp tours | 7 | ~3,000–5,000 | Striking distance — only current page-1 commercial win | Reinforce with more internal links, don't disturb |
| new orleans swamp tour | 9 | ~3,000–5,000 | Striking distance | Same |
| honey island swamp tour | 22, on the wrong URL (blog category archive) | 9,900 | Page 2 hostage + URL collision | 301 or noindex the archive URL, push link equity to the real tour page |
| alligator tour new orleans | 51 (not ranking) | 2,900 | New territory | Build `/alligator-tour-new-orleans/`, bridges existing AI-Overview alligator authority to a bookable page |
| gator tour new orleans | 45 | 2,900 (same cluster) | New territory | Same page covers this |
| which is more dangerous alligator or crocodile | 6.4 | 10,210 impr/90d (info) | CTR fix — already actioned | Title/meta rewritten recently; monitor CTR on next GSC pull |
| alligator vs crocodile | 8.6 | 27,141 impr/90d (info) | CTR fix — already actioned | Same page, same fix, monitor |
| swamp tours in new orleans | 20, on `/3-free-swamp-walks-.../` | 1,900 | Commercial query landing on a "don't pay us" page | Rewrite every section to CTA to a paid tour |
| best new orleans swamp tours | 24, on `/which-swamp-tours-are-the-best/` (duplicate ranks #43) | 1,600 | Cannibalization | Merge duplicate pages, rebuild as a real comparison hub |
| swamp tour near me | not in top 100 organically | 12,100 (local-pack query) | Local pack, not organic | GBP category fix (see §6), not a content play |
| louisiana swamp tour | not in top 100 | 235–337 (corrected down from a 4,400 Google Ads mirage) | Withdrawn | Not worth a dedicated page at true volume |
| kayak swamp tour | 1 | 880 | Owned | No action — ceiling of the "kayak" framing |

---

## 2. On-page SEO issues (schema/links re-verified live today via raw HTML extraction)

| Page | Issue | Severity | Fix |
|---|---|---|---|
| `/tours/swamp/` | Confirmed today via direct JSON-LD extraction: only `BreadcrumbList`/`ListItem` present. No Product, Offer, AggregateRating, or FAQPage. This is the intended money page for the biggest keyword on the site (~1,100–4,000/mo "swamp tours new orleans") and it's currently invisible to both traditional ranking signals and AI-answer extraction. | Critical | Add Product + Offer (price/currency/availability) + AggregateRating (4.9/1,416) + FAQPage (4 confirmed PAA questions) schema. Expand to 2,000+ words: price, duration, drive time from the Quarter, wildlife list, airboat-vs-kayak, best time of year, what to bring. |
| `/` (homepage) | Confirmed today: `Organization, LocalBusiness, WebSite, WebPage, VideoObject, GeoCoordinates, PostalAddress, ContactPoint, SearchAction, ImageObject` present — no AggregateRating, no FAQPage. | High | Add AggregateRating + FAQPage schema. |
| `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | Confirmed today: `Organization, VideoObject, BreadcrumbList, ListItem, ImageObject` present — still no Product, Offer, or AggregateRating despite pricing listed in the page body. | High | Add Product + Offer + AggregateRating schema. |
| `/tours/kayak-tours/honey-island-swamp-tour/` | Confirmed today via direct meta tag pull: `<meta name="description" content="Click to view honey island swamp tour category posts in Blog \| Page 1 of 2">` — literal auto-generated blog-archive boilerplate, zero schema. This URL ranks #22 for a 9,900/mo keyword while the real tour page (`/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`) sits unranked/buried, both confirmed 200 live today. | Critical | 301 the archive URL to the real tour page (or noindex if a 301 isn't feasible via the CMS); update any internal links pointing at the archive URL. |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Both confirmed 200 live today, different H1s, same query intent, ranking #24 and #43-51 respectively. Textbook cannibalization. | High | 301 the weaker page into the stronger one, merge unique content, rebuild the survivor as a real Manchac vs. Honey Island vs. Bayou Sauvage comparison with schema. |
| `/alligators-vs-crocodiles/` | Confirmed today: JSON-LD is `Article, Organization, BreadcrumbList, ListItem, ImageObject` only — no FAQPage despite the page being full of Q&A content. Confirmed today via href scan: the page links to `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` and nothing else — zero links to `/tours/swamp/` or `/swamp-tours-new-orleans-guide/`. | Critical (linking), Medium (schema) | Add the "more reading" internal-link block (see §3, item 1). Add FAQPage schema for the alligator/crocodile Q&A pairs already in the copy. |
| `/3-free-swamp-walks-in-and-around-new-orleans/` | Confirmed 200 live today at the same URL, still ranking for ~9,500/mo of commercial-intent variants with a "see a swamp for free" thesis. | High | Rewrite every section to end with a paid-tour CTA; add a comparison callout. |
| `/7-of-the-best-things-to-do-in-february-in-new-orleans/` | Confirmed 200 live today at the full slug (the shorthand slug from the May audit 404s — always use the full URL). Ranking pos 13-16 on under-1,000 impressions per the Aug 10 pull. | Medium | Refresh for 2026, add FAQ schema, add a tour CTA. |
| `/tours/` | Confirmed 200 live today; meta description reads as a complete, non-truncated sentence. The truncation flagged in the May audit is not reproducing today. | Low | Optional: tighten copy to lead with "swamp tour" language, but not urgent. |

---

## 3. Internal linking opportunities

Sorted by priority. Link presence/absence for item 1-3 independently re-verified today via a direct href scan of the live page HTML (not just a prior audit citation).

| # | Source page | Target (money page) | Suggested anchor | Where to place | Priority | Verified status today |
|---|---|---|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | `/tours/swamp/` | "swamp tours in New Orleans" | New "More reading" block, top + conclusion | Critical | **Confirmed missing** — href scan found 0 links to this URL |
| 2 | `/alligators-vs-crocodiles/` | `/swamp-tours-new-orleans-guide/` | "our full New Orleans swamp tour guide" | Same block | Critical | **Confirmed missing** — href scan found 0 links |
| 3 | `/alligators-vs-crocodiles/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "kayak swamp tour in New Orleans" | Already has 1 in-body link (confirmed today); add 1 more prominent CTA above the fold | High | 1 link confirmed present, none above the fold |
| 4 | `/3-free-swamp-walks-in-and-around-new-orleans/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "guided Manchac swamp kayak tour" | After the free-walk list, in a "want a guided experience?" section | High | Page confirmed 200 live today; link not independently verified this pass |
| 5 | `/what-is-the-best-time-of-day-to-go-on-a-swamp-tour-in-new-orleans/` | `/tours/swamp-kayak-tours/` | "book a morning swamp tour" | In the "best time = morning" section | High | Page live (per Aug 10 pull, 7,967 impressions) |
| 6 | `/top-5-classic-new-orleans-style-homes/` | `/` (homepage) | "New Orleans kayak swamp tour" | Sidebar or closing CTA | Medium | Not re-verified this pass |
| 7 | `/tours/kayak-tours/honey-island-swamp-tour/` (archive) | `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (real page) | "Honey Island kayak swamp tour" | Site-wide — really a redirect/consolidation, not a link add | Critical | Both URLs confirmed 200 live today, still split |
| 8 | `/julie-white/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "book a tour with one of our guides" | End of bio | Medium | Not re-verified this pass |

**Orphan money pages (confirmed 200 live today, all zero-broken-link crawl passed):**

| Page | Notes |
|---|---|
| `/tours/swamp-kayak-tours/shell-bank-half-day-extended-bayou-adventure/` | 200 live today. Position 27.4, ~460 impressions per the Aug 10 pull. Link from `/3-free-swamp-walks/` and the Manchac page. |
| `/tours/swamp-kayak-plantation-tour/` | 200 live today. Ranks for "swamp and plantation tour new orleans" but thin internal-link support. |
| `/plantation-tour/` | 200 live today. Near-orphan. Link from the homepage tours menu. |

---

## 4. Content gap analysis

Primary competitor per the June 19 content-gap research and the Aug 10 AI-search test: **Wild Louisiana Tours** (wildlouisianatours.com, also surfaces as crescentcitykayak.com). Wild Louisiana beat NKST in a live AI Overview test for "best swamp tour New Orleans kayak eco tour 2026" — they led with extractable specifics (duration, transport, species list), NKST led with eco-mission language.

**High-priority gaps (topics Wild Louisiana structurally can't chase, per their own "education and safety, not folklore" positioning):**

1. **Manchac haunted-swamp cluster** — "The Legend of Julia Brown," "Is the Manchac Swamp Really Haunted?," sunset/night tour content. Real search demand, zero competitor coverage, fits NKST's existing brand latitude. Highest-leverage gap identified across three research passes.
2. **"Will I see an alligator?" / gator safety and season page** — the #1 fear/hope query for first-time bookers; competitor treats it as beneath them.
3. **Kayak vs. airboat comparison** — recommended in the May and August audits and independently in the competitor-gap research. Three separate passes, same gap, still unbuilt.
4. **Practical-anxiety cluster** — what to wear, mosquitoes/heat in summer, first-time nervous kayaker guide, bringing kids. Confirmed absent from the competitor and thin-to-absent on NKST.
5. **"How much does a swamp tour cost?" page** — highest commercial-intent PAA question on the SERP per the Aug 10 audit, nothing built for it yet.

**Also flagged, lower priority:** photography spot guide (competes with Wild Louisiana's paid workshop content using free how-to), bachelor/bachelorette guide rebuild (both NKST's and the competitor's version rank weakly).

---

## 5. Technical SEO checklist

All items marked "live today" were independently re-checked this session via direct curl/Python, not copied from the prior same-day pass.

| Check | Status | Details |
|---|---|---|
| Homepage redirect chain | Pass — live today | `https://neworleanskayakswamptours.com` → 200, 0 redirects, 0.16s response |
| robots.txt | Pass — live today | Sitemap correctly referenced. Blocks `/edit/`, `/fhbr-console/`, `/cdn-cgi/` (correct — admin/CDN paths). Blocks a long list of scraper user-agents (MegaIndex, Baiduspider, Yandex, Barkrowler, etc.) with `Disallow: /` per agent — intentional, not a mistake, but worth confirming legitimate crawlers (Bingbot etc.) never end up on that list. |
| sitemap.xml | Pass — live today | Valid sitemap index → 3 child sitemaps (page, activity, post), all reachable (200). |
| Broken-link crawl (30 same-domain URLs: homepage nav + every URL named across the Aug 10, May 4, and earlier-today audits) | Pass — live today | All 30 returned 200. No broken links found on this pass. |
| Duplicate content / cannibalization | Fail — live today | Two live pages target "best swamp tour": `/which-swamp-tours-are-the-best/` and `/which-is-the-best-swamp-tour-around-new-orleans/`. See §2. |
| URL collision (archive vs. real page) | Fail — live today | `/tours/kayak-tours/honey-island-swamp-tour/` (blog category archive, confirmed zero schema, confirmed boilerplate meta) outranks the real tour page. See §2. |
| Schema markup — homepage | Partial — live today | Organization, LocalBusiness, WebSite, VideoObject, etc. present. AggregateRating, FAQPage missing. |
| Schema markup — `/tours/swamp/` | Fail — live today | BreadcrumbList only, confirmed via raw JSON-LD extraction. |
| Schema markup — tour product pages | Fail — live today | Manchac page has VideoObject/Organization/BreadcrumbList; no Product/Offer/AggregateRating on any tour page checked. |
| Schema markup — `/alligators-vs-crocodiles/` | Partial — live today | Article, BreadcrumbList, Organization, ImageObject present. No FAQPage despite Q&A-formatted content. |
| Internal link: alligator page → `/tours/swamp/` | Fail — live today | Confirmed 0 links via href scan. |
| HTTPS | Pass — live today | Site fully on HTTPS. |
| Core Web Vitals / Lighthouse | **Stale data only** | Live PSI run blocked again today — direct `curl` against the PSI v5 endpoint returned `429`, confirming quota is still exhausted and no `PSI_KEY` is on file. Last successful run: 2026-06-19 (56 days old). See below. |
| GSC index status | **Not available** | GSC MCP not connected this session (confirmed via ToolSearch, no `gsc_*` tools loaded). No fresh indexed/discovered-not-indexed comparison possible. |

### Core Web Vitals (last available data: 2026-06-19, 56 days old — directional only)

| Strategy | Perf score | LCP (lab) | CLS (lab) | TBT (lab) | Field data (CrUX: LCP/CLS/INP) |
|---|---|---|---|---|---|
| Mobile | **37 (red)** | 16.2s (very poor) | 0.005 (good) | 1,600ms (poor) | FAST / FAST / FAST |
| Desktop | 54 (amber) | 2.5s (good) | 0.009 (good) | 620ms (needs improvement) | FAST / FAST / FAST |

The lab score (single throttled synthetic test) says mobile is a 16.2s LCP disaster; the field data (real visiting users, CrUX) says LCP/CLS/INP are all FAST. That gap usually means the lab test hit an unusually slow simulated device/network profile, or one heavy asset (likely the homepage hero `VideoObject`) tanks synthetic tests without affecting most real users on faster connections. Don't act on the 37 score alone — it's 56 days old and directionally contradicted by field data. Get a `PSI_KEY` (Google Cloud Console, not something to generate unattended) added to `~/.claude/.env` so the daily keyless quota stops blocking re-runs.

---

## 6. Local search / GBP (from the Aug 10 audit — not independently re-verified today, GBP MCP unavailable)

NKST's GBP (740 N Rampart St, 4.9 stars, 1,416 reviews) is not appearing in the "swamp tour near me" local pack (12,100/mo) despite outperforming the #2 pack result (Tour Big Easy, 729 reviews) on both volume and rating. Two likely causes, neither independently re-checked today:
- Primary GBP category is "Canoe & kayak tour agency" vs. pack winners' "Boat tour agency" / "Tour operator."
- Five David-controlled listings cluster within a few blocks of each other (NKST, Crescent City Kayak, Hidden Adventure, Admire New Orleans, and a listing at a fabricated "Swamp Tour Street" address), which can trigger Google's proximity diversity filter and suppress all of them. The fabricated-address listing is a standalone suspension risk independent of the SEO angle.

**Needs a live GBP check before acting** — carried forward, not confirmed today.

---

## 7. Competitor comparison

| Dimension | NKST | Wild Louisiana Tours / Crescent City Kayak | Cajun Encounters | Winner |
|---|---|---|---|---|
| GBP reviews / rating | 1,416 / 4.9 | Not directly comparable (CCK secondary property) | 12,000 / 4.9 | Cajun Encounters on volume, NKST close on quality |
| Local pack presence ("swamp tour near me") | Not in pack | N/A | In pack (#3) | Cajun Encounters |
| AI Overview commercial citations | 1 (rank 13) | Cited #1 by name in a live test with full trip specifics | Not tested | Wild Louisiana |
| Structured data (Product/Offer/Rating) | None found on any page checked — confirmed today via raw HTML | GetYourGuide listing carries verified reviews/structured specifics | Not tested | Wild Louisiana (via 3rd-party listing) |
| Content coverage — haunted/legend angle | Absent | Explicitly rejected in their own copy | Not tested | Open — first mover wins |
| Content coverage — practical anxiety (what to wear, kids, bugs) | Thin | Confirmed absent | Not tested | Open |
| Head-to-head organic position (kayak/swamp queries vs. own CCK property) | Wins every head-to-head listed in the May audit | CCK loses every one | — | NKST |

---

## 8. Traffic & conversion context (GA4, March 2026 — 5 months old, directional only)

No fresh GA4 pull was possible this session (MCP not connected). Most recent real data on file: the March 26, 2026 report (GA4 property 401824264, 90-day window).

- 11,848 sessions / 90d, +44% sessions and +59% conversions month-over-month at the time (spring seasonal ramp).
- **Paid Search converted at 19.8%** vs. 13.0% organic, 8.7% direct — flagged then as likely underspent.
- **Paid Social converted at 0.8%** — flagged as essentially wasted spend at the time.
- **Conversion tracking gap:** only 58 `ads_conversion_Purchase_1` events tracked in 90 days against 23,385 GHL contacts — FareHarbor booking confirmations were not firing a GA4 purchase event as of March. Treat all GA4 conversion-rate figures cited here as undercounting real bookings until this is confirmed fixed.
- Alligator blog: 831 pageviews, 60% bounce rate — consistent with the 0.32% CTR problem: people who click still leave without converting.

**Recommend confirming whether the FareHarbor → GA4 purchase event was ever fixed** — affects every conversion-rate figure in NKST's marketing stack, not just SEO.

---

## 9. Prioritized fix list

### Quick wins (this week — all under a few hours each)

| # | Page/URL | Exact change | Expected impact |
|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | Add a "More reading" internal-link block (top of post + conclusion) linking to `/tours/swamp/` and `/swamp-tours-new-orleans-guide/` (no `/blog/` prefix — confirmed that's the live URL), plus a more prominent CTA to the Manchac tour page above the fold. Confirmed today via href scan: currently links only to the Manchac page, and only once, mid-body. | Redirects a slice of a page doing 272k impressions/quarter toward the money pages Google currently can't find via this route. Directly addresses why `/tours/swamp/` sits at position 15 on the homepage instead of ranking itself. |
| 2 | `/alligators-vs-crocodiles/` | Add FAQPage schema wrapping the existing alligator-vs-crocodile Q&A content (markup only, no new writing). Confirmed today: current schema is Article/Organization/BreadcrumbList/ImageObject, no FAQPage. | AI Overview / rich-result eligibility on a page already getting 272k impressions/quarter at a 0.32% CTR — even a partial CTR lift here is the single biggest click opportunity on the site. |
| 3 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 redirect (or noindex if a 301 isn't feasible via the CMS) to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. Update internal links pointing at the archive URL. Confirmed today: meta description is literally `"Click to view honey island swamp tour category posts in Blog | Page 1 of 2"`. | Stops a boilerplate blog-archive page from being Google's answer for a 9,900/mo keyword ("honey island swamp tour," currently position 22); consolidates link equity onto a real, bookable page. |
| 4 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 redirect into `/which-swamp-tours-are-the-best/`, merging unique content first. Both confirmed 200 live today. | Ends self-cannibalization on "best swamp tour" queries (currently split across positions 24 and 43-51); the survivor has a real shot at page 1 once it's not competing with itself. |
| 5 | `/` (homepage) | Add AggregateRating (4.9, 1,416 reviews) schema. Confirmed today: homepage has Organization/LocalBusiness/WebSite/VideoObject schema but no AggregateRating. | Star-rating rich snippet in search results — pure CTR play, no content risk, applied to the highest-traffic page on the site. |
| 6 | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` and the other 5 tour pages | Add Product + Offer (price/currency/availability) schema using pricing already published in the page body. Confirmed today: Manchac page has zero Product/Offer schema despite listed pricing. | Price display in search results + AI-answer extractability, using content that already exists but isn't machine-readable. |
| 7 | `~/.claude/.env` | Get a free PageSpeed Insights API key (David generates this at Google Cloud Console; not something to do unattended) and add it as `PSI_KEY=...`. Confirmed today via direct curl: keyless quota is still returning `429`. | Unblocks a real, current Core Web Vitals read. The mobile perf score of 37 is 56 days stale and directionally contradicted by CrUX field data (FAST) — don't spend a day rebuilding the homepage hero video over a number this old without re-verifying it first. |

### Strategic work (this quarter)

| # | Page/URL | Exact change | Expected impact |
|---|---|---|---|
| 8 | `/tours/swamp/` | Rebuild as the true money page for "swamp tours new orleans" (highest-volume commercial cluster on the site, currently ranking via the homepage at position 15, not this page). Expand to 2,000+ words: price, duration, drive time from the French Quarter, wildlife list, airboat-vs-kayak comparison, best time of year, what to bring, booking CTA. Add full FAQPage schema for the 4 confirmed PAA questions. Link to it from the homepage, the alligator page, and all swamp-related blog posts. | Single biggest lever identified across three audit passes (May, Aug 10, today). Currently a page with only BreadcrumbList schema and ~1,200-1,400 words is the intended answer for a keyword worth ~1,100-4,000/mo — a real money page with real internal-link support is the only way to close that gap. |
| 9 | New page: `/alligator-tour-new-orleans/` | Build a dedicated commercial page targeting "alligator tour new orleans" / "gator tour new orleans" (2,900/mo combined, currently unranked at position 45-51, no page exists). | Bridges NKST's existing AI-Overview alligator authority (25 citations, mostly trivia) to an actual bookable page — that authority currently converts to zero commercial value. |
| 10 | New page: `/kayak-vs-airboat-swamp-tour/` | Build a long-form, honest comparison page. Independently identified in the May audit, the August audit, and the June competitor content-gap research — three separate passes, same conclusion, still unbuilt. | NKST's brand position is explicitly anti-airboat; owning the comparison query both ranks and converts on-brand. Wild Louisiana avoids naming the airboat alternative at all, leaving this fully open. |
| 11 | New cluster: Manchac haunted-swamp pillar (Julia Brown legend, "is Manchac really haunted," sunset/night tours) | 3-4 new pages per the June competitor-gap research, cross-linked into a pillar hub. | Real search demand with zero competitor coverage — Wild Louisiana's own copy explicitly rejects folklore content, structurally locking them out. Best available "first mover" opportunity found across all three audit passes. |
| 12 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite every section to end with a paid-tour comparison CTA instead of standing alone as a "don't pay us" post. Confirmed 200 live today, unchanged thesis. | Redirects roughly 9,500/mo of commercial-intent search traffic currently landing on a page whose entire thesis argues against booking. |
| 13 | New page: "How much does a swamp tour cost?" | Build a direct-answer page with a real price-comparison table across operators (the format AI engines quote, per the Aug 10 live AI-search test). | Highest commercial-intent PAA question on the "swamp tours new orleans" SERP with nothing built for it yet. |
| 14 | GetYourGuide / TripAdvisor / Viator listings | Rewrite third-party OTA listing copy to lead with extractable specifics (exact duration, transport, species list, group size, difficulty) instead of mission-first language — matching how Wild Louisiana's GetYourGuide listing is written, since that's the page a live AI search actually quoted over NKST's own site. | This is the layer AI answer engines are sourcing from right now, per the Aug 10 live test. Schema fixes (items 5-6, 8) won't fully close this gap without also fixing the OTA layer. |
| 15 | GBP: primary category + duplicate-listing cleanup | Needs a live GBP check first (not available this session) to confirm the Aug 10 findings still stand: category mismatch ("Canoe & kayak tour agency" vs. pack winners' "Boat tour agency"/"Tour operator") and 5 nearby David-controlled listings possibly triggering Google's proximity diversity filter, including one at a fabricated address ("Swamp Tour Street") that's a standalone suspension risk regardless of the SEO angle. | Local pack eligibility for "swamp tour near me" (12,100/mo, currently 0% organic presence — a 100% local-pack game). |
| 16 | Crescent City Kayak property decision | Still open across three audits. Either 301 the whole property into NKST (cleanest, captures ~600 clicks/quarter of split organic per the May pull) or commit to rebuilding it as a genuine funnel with a hard CTA back to NKST bookings. | Every quarter this stays undecided, CCK keeps splitting authority on queries NKST already wins head-to-head. |

---

## Notes

- Every item marked "confirmed today" or "live today" was independently re-checked this session via direct `curl`/Python HTTP requests and raw JSON-LD extraction against the production site on 2026-08-14 — not assumed from the earlier same-day pass or prior audits.
- Numbers not re-pulled this session (GSC positions/impressions, GA4 sessions/conversions, GBP category/listing status, Core Web Vitals) are dated to their source document above; none were guessed or extrapolated.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in producing this report. Every action item above is a recommendation awaiting David's approval.
