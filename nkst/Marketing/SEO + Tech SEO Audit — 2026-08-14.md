---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-14
status: REPORT ONLY — NO CHANGES APPLIED
---

# NKST SEO + Technical SEO Audit — 2026-08-14

> **REPORT ONLY. Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform.** This was generated in an unattended run with no live GSC/GA4/GBP MCP connection and no interactive approval step. Every recommendation below needs David's sign-off before anything gets touched. See "Data Sources & Gaps" for exactly what is live-verified today vs. pulled from recent prior audits.

---

## Data Sources & Gaps (read this first)

This run could not reach the Google Search Console or Google Analytics 4 MCP tools — `google-nkst` is configured in this vault's `.mcp.json`, but no `gsc_*` or `ga4_*` tools loaded in this session (unlike `higgsfield`, it wasn't flagged as needing OAuth either — it simply didn't expose tools this run). GBP MCP tools were likewise unavailable. PageSpeed Insights' keyless quota was also exhausted (`429 RESOURCE_EXHAUSTED`, 0 daily quota remaining) and no `PSI_KEY` is on file, so a fresh Lighthouse run wasn't possible today.

**What this report is built on instead — all real data, no invented numbers:**

| Source | Date | What it gives us |
|---|---|---|
| `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md` | **2026-08-10** (4 days old) | Full GSC query/position/impression data (90d window), DataForSEO rank + volume cross-check, live AI Overview / AI search testing, schema audit, GBP local-pack snapshot |
| `Marketing/SEO Audit 2026-05-04.md` | 2026-05-04 | Prior GSC pull, internal linking recommendations, baseline to measure drift against |
| `Analytics Report — March 2026.md` | 2026-03-26 | Real GA4 data (property 401824264) — sessions, channel conversion rates, top pages, conversion-tracking gap |
| `Marketing/Competitor Content-Gap Analysis — Wild Louisiana (June 2026).md` | 2026-06-19 | Direct competitor content-gap research vs. wildlouisianatours.com / crescentcitykayak.com |
| **Live checks run today (2026-08-14)** | Today | robots.txt, sitemap.xml, HTTP status on 40+ URLs, JSON-LD schema spot-checks on 5 key pages, title/meta spot-checks, redirect check on the homepage |
| `~/Projects/tech-seo/out/psi-20260619.json` | 2026-06-19 (56 days old) | Last successful PageSpeed Insights run — used as the only available CWV/Lighthouse data point, flagged as stale below |

**Confirmed data gaps in this report:** no fresh GSC query data pulled today (relying on the Aug 10 pull, which is close enough to be reliable but is not "today"); no fresh GA4 session/conversion data (relying on March, which is 5 months old — treat channel-mix and conversion-rate figures as directional, not current); no live GBP listing/category check (relying on Aug 10 findings); no fresh Core Web Vitals/Lighthouse run (relying on a 56-day-old cached run). **Recommend re-running `/seo-audit` and `/tech-seo` once the GSC/GA4 MCP connection is fixed and PSI quota resets**, ideally with a `PSI_KEY` added so the keyless daily cap stops being a blocker.

Everything else below — every URL, HTTP status, schema type, and title/meta string — was verified live against the production site today, 2026-08-14.

---

## Executive Summary

NKST has genuine SEO assets — 1,416 reviews at 4.9 stars, a 272k-impression alligator blog, and page-1 rankings on the smaller version of its core keyword — but is leaking commercial demand at every layer: the wrong pages rank for money terms, structured data is nearly absent on pages that need it most, and a direct competitor (Wild Louisiana Tours) is winning the AI Overview answer for "best swamp tour New Orleans" with more extractable copy. Nothing material has shipped since the August 10 audit: the alligator page's internal-link block is still missing, the duplicate "best swamp tour" posts are both still live, and `/tours/swamp/` still carries only BreadcrumbList schema. The one thing that has moved: the alligator page's title and meta description were rewritten sometime in the last 4 days into a sharp, question-answering format — a good sign that some of this list is already being worked.

**Top 3 priorities by impact:**
1. Ship the internal-link block from `/alligators-vs-crocodiles/` (272k impressions/quarter of untapped authority) to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, and the Manchac tour page — recommended twice now (May and August) and still not live.
2. Add Product + Offer + AggregateRating + FAQPage schema to the 6 tour pages and homepage — confirmed still zero commercial schema anywhere on the site despite 1,416 reviews at 4.9 stars sitting in plain text.
3. Kill the cannibalization: 301 `/which-is-the-best-swamp-tour-around-new-orleans/` into `/which-swamp-tours-are-the-best/`, and fix the Honey Island URL collision where a blog category archive (`/tours/kayak-tours/honey-island-swamp-tour/`) outranks the real tour page for a 9,900/mo keyword.

---

## 1. Keyword Opportunity Table

Source: GSC 90-day pull from the 2026-08-10 audit (window 2026-05-12 to 2026-08-09), cross-checked against DataForSEO US volume. Position/page columns re-verified live today where the target page is named.

| Keyword | Position | Volume/mo (corrected) | Tier | Recommended Action |
|---|---|---|---|---|
| swamp tours new orleans | 15 (homepage ranks, not the money page) | ~1,100–4,000 | Page 2 hostage — biggest single opportunity | Build out `/tours/swamp/` as the real target, link to it from the alligator page and homepage |
| swamp tour new orleans | 21 | ~3,000–10,000 | Page 3 | Same fix as above; same money page |
| new orleans swamp tours | 7 | ~3,000–5,000 | Striking distance — only current page-1 commercial win | Reinforce with more internal links, don't disturb |
| new orleans swamp tour | 9 | ~3,000–5,000 | Striking distance | Same |
| honey island swamp tour | 22, on the wrong URL (blog category archive) | 9,900 | Page 2 hostage + URL collision | Noindex or 301 the archive URL, push link equity to the real tour page |
| alligator tour new orleans | 51 (not ranking) | 2,900 | New territory | Build `/alligator-tour-new-orleans/`, bridges existing AI-Overview alligator authority to a bookable page |
| gator tour new orleans | 45 | 2,900 (same cluster) | New territory | Same page covers this |
| which is more dangerous alligator or crocodile | 6.4 | 10,210 impr/90d (info) | CTR fix — already actioned | Title/meta rewritten in last 4 days; monitor CTR next pull |
| alligator vs crocodile | 8.6 | 27,141 impr/90d (info) | CTR fix — already actioned | Same page, same fix, monitor |
| swamp tours in new orleans | 20, on `/3-free-swamp-walks-.../` | 1,900 | Commercial query landing on a "don't pay us" page | Rewrite that post so every section CTAs to a paid tour |
| best new orleans swamp tours | 24, on `/which-swamp-tours-are-the-best/` (and a duplicate ranks #43) | 1,600 | Cannibalization | Merge duplicate pages, rebuild as a real comparison hub |
| swamp tour near me | not in top 100 organically | 12,100 (local-pack query) | Local pack, not organic | GBP category fix (see §6), not a content play |
| louisiana swamp tour | not in top 100 | 235–337 (corrected down from a 4,400 Google Ads mirage) | Withdrawn | Not worth a dedicated page at true volume |
| kayak swamp tour | 1 | 880 | Owned | No action — this is the ceiling of the "kayak" framing |

---

## 2. On-Page SEO Issues

Verified live on 2026-08-14 (title, meta, H1, schema pulled directly from page source).

| Page | Issue | Severity | Fix |
|---|---|---|---|
| `/tours/swamp/` | Only `BreadcrumbList` schema present. No Product, Offer, AggregateRating, or FAQPage. This is the intended money page for the biggest keyword on the site and it's under-built for both traditional SEO and AI answer extraction. | Critical | Add Product + Offer (price/currency/availability) + AggregateRating (4.9/1,416) + FAQPage (4 PAA questions) schema. Expand to 2,000+ words covering price, duration, drive time from the Quarter, wildlife list, airboat-vs-kayak, best time of year, what to bring. |
| `/` (homepage) | Has VideoObject, Organization, LocalBusiness, WebSite, WebPage schema — but no AggregateRating or FAQPage. Confirmed live today: `PostalAddress, ContactPoint, LocalBusiness, VideoObject, GeoCoordinates, WebSite, SearchAction, Organization, WebPage, ImageObject` — no rating, no FAQ. | High | Add AggregateRating + FAQPage schema. |
| `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | Has VideoObject + Organization + BreadcrumbList schema, confirmed live today — but still no Product, Offer, or AggregateRating despite listed pricing in the body. | High | Add Product + Offer + AggregateRating schema. |
| `/tours/kayak-tours/honey-island-swamp-tour/` | Confirmed live today: title renders as "Honey Island Swamp Tour" but meta description is literally `"Click to view honey island swamp tour category posts in Blog | Page 1 of 2"` — auto-generated blog category archive boilerplate, zero schema. This URL ranks #22 for a 9,900/mo keyword while the real tour page (`/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`) sits unranked/buried. | Critical | Noindex the archive URL or 301 it to the real tour page; consolidate all internal links to the real URL. |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Confirmed both live today, different H1s ("New Orleans swamp tour reviews" vs "What is the best Swamp Tour near New Orleans?"), same query intent, ranking #24 and #43-51 respectively. Textbook cannibalization — neither will rank while both exist. | High | 301 the weaker page (`/which-is-the-best-swamp-tour-around-new-orleans/`) into the stronger one, merge any unique content, then rebuild the survivor as a real Manchac vs. Honey Island vs. Bayou Sauvage comparison with schema. |
| `/alligators-vs-crocodiles/` | Title/meta **already rewritten** since the Aug 10 audit — now reads "Alligator vs Crocodile: Which Is More Dangerous?" with a meta that answers directly. Good. But confirmed live today: zero links to `/tours/swamp/` or `/swamp-tours-new-orleans-guide/` (only 2 in-body links to the Manchac tour page), and schema is Article/BreadcrumbList/Organization/ImageObject only — no FAQPage despite the page being full of Q&A content. | Critical (linking), Medium (schema) | Add the "More reading" internal-link block (see §3, item 1). Add FAQPage schema for the alligator/crocodile Q&A pairs already in the copy. |
| `/3-free-swamp-walks-in-and-around-new-orleans/` | Confirmed still live at the same URL, ranking for ~9,500/mo of commercial-intent variants ("swamp tours in new orleans," "swamp tours of new orleans," etc.) with a thesis of "see a swamp for free." | High | Rewrite every section to end with a paid-tour CTA; add a comparison callout ("want a guided version? here's what you get"). |
| `/7-of-the-best-things-to-do-in-february-in-new-orleans/` | Confirmed live and correctly URLed (note: the shorthand slug used in the May audit, `/7-of-the-best-things-to-do-in-february/`, 404s — always use the full slug). Ranking ~pos 13-16 for "new orleans in february" on under-1,000 impressions. | Medium | Refresh for 2026, add FAQ schema, add a tour CTA. |
| `/tours/` | Meta description is a complete sentence at 135 characters as of today ("Come experience a fun kayak or cycle boat tour with us. If you are in Louisiana, you can't miss this! Book your New Orleans tour today!") — the truncation flagged Aug 10 is **not reproducing today**; leaving as a low-priority polish item rather than a broken fix. | Low | Optional: tighten copy to lead with "swamp tour" language for keyword relevance, but this is not urgent. |

---

## 3. Internal Linking Opportunities

Sorted by priority. Source page authority figures are from the Aug 10 GSC pull; link presence/absence re-verified live today.

| # | Source Page | Target (Money Page) | Suggested Anchor | Where to Place | Priority | Verified Status Today |
|---|---|---|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | `/tours/swamp/` | "swamp tours in New Orleans" | New "More reading" block, top + conclusion | Critical | **Confirmed missing** — 0 links found |
| 2 | `/alligators-vs-crocodiles/` | `/swamp-tours-new-orleans-guide/` | "our full New Orleans swamp tour guide" | Same block | Critical | **Confirmed missing** — 0 links found |
| 3 | `/alligators-vs-crocodiles/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "kayak swamp tour in New Orleans" | Already has 2 in-body links; add 1 more prominent CTA above the fold | High | Partially done — 2 links exist, none above the fold |
| 4 | `/3-free-swamp-walks-in-and-around-new-orleans/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "guided Manchac swamp kayak tour" | After the free-walk list, in a "want a guided experience?" section | High | Not verified fixed — recommend re-check on next content pass |
| 5 | `/what-is-the-best-time-of-day-to-go-on-a-swamp-tour-in-new-orleans/` | `/tours/swamp-kayak-tours/` | "book a morning swamp tour" | In the "best time = morning" section | High | Confirmed page live (200), link not verified |
| 6 | `/top-5-classic-new-orleans-style-homes/` | `/` (homepage) | "New Orleans kayak swamp tour" | Sidebar or closing CTA | Medium | Confirmed page live (200), link not verified |
| 7 | `/tours/kayak-tours/honey-island-swamp-tour/` (archive) | `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (real page) | "Honey Island kayak swamp tour" | Site-wide — this is really a redirect/consolidation, not a link add | Critical | Confirmed both URLs live and split today |
| 8 | `/julie-white/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "book a tour with one of our guides" | End of bio | Medium | Page confirmed live (200) |

**Orphan money pages (from the May 4 audit, not independently re-crawled today — worth a follow-up crawl):**

| Page | Notes |
|---|---|
| `/tours/swamp-kayak-tours/shell-bank-half-day-extended-bayou-adventure/` | Confirmed 200 live today. Position 27.4, ~460 impressions per the May pull. Link from `/3-free-swamp-walks/` and the Manchac page. |
| `/tours/swamp-kayak-plantation-tour/` | Confirmed 200 live today. Ranks for "swamp and plantation tour new orleans" but thin internal-link support. |
| `/plantation-tour/` | Confirmed 200 live today. Position ~27, near-orphan. Link from the homepage tours menu. |

---

## 4. Content Gap Analysis

Primary competitor per the June 19 content-gap research and the Aug 10 AI-search test: **Wild Louisiana Tours** (wildlouisianatours.com, also surfaces as crescentcitykayak.com). Wild Louisiana beat NKST in a live AI Overview test for "best swamp tour New Orleans kayak eco tour 2026" — they led with extractable specifics (duration, transport, species list), NKST led with eco-mission language.

**High-priority content gaps (topics Wild Louisiana structurally cannot chase, per their own "education and safety, not folklore" positioning):**

1. **Manchac haunted-swamp cluster** — "The Legend of Julia Brown," "Is the Manchac Swamp Really Haunted?," sunset/night tour content. Real search demand, zero competitor coverage, fits NKST's existing brand latitude. Highest-leverage gap identified.
2. **"Will I see an alligator?" / gator safety and season page** — the #1 fear/hope query for first-time bookers; competitor treats it as beneath them.
3. **Kayak vs. airboat comparison** — recommended in both the May and August audits and again independently in the competitor-gap research. Three separate research passes landed on the same gap; build it.
4. **Practical-anxiety cluster** — what to wear, mosquitoes/heat in summer, first-time nervous kayaker guide, bringing kids. All confirmed absent from the competitor and thin-to-absent on NKST.
5. **"How much does a swamp tour cost?" page** — highest commercial-intent PAA question on the SERP (per Aug 10 audit), nothing built for it yet.

**Also flagged, lower priority:** photography spot guide (competes with Wild Louisiana's paid workshop content using free how-to), bachelor/bachelorette guide rebuild (both NKST's and the competitor's version rank weakly, real opportunity if done well).

---

## 5. Technical SEO Checklist

All items verified live today, 2026-08-14, unless marked otherwise.

| Check | Status | Details |
|---|---|---|
| Homepage redirect chain | Pass | `https://neworleanskayakswamptours.com` → 200, 0 redirects, 0.87s response |
| robots.txt | Pass, with one thing to watch | Sitemap correctly referenced. Blocks `/edit/`, `/fhbr-console/`, `/cdn-cgi/` (all correct — admin/CDN paths). Blocks a long list of specific bot user-agents (MegaIndex, Baiduspider, Yandex, Barkrowler, etc.) with a blanket `Disallow: /` for each — this is intentional scraper-blocking, not a mistake, but worth confirming Bingbot/legitimate crawlers aren't accidentally on that list next time it's edited. |
| sitemap.xml | Pass | Valid sitemap index → 3 child sitemaps (page, activity, post). Activity sitemap correctly lists all 6+ tour/product pages with weekly changefreq and 0.8-0.9 priority. |
| Broken-link crawl (40+ URLs checked: homepage nav links + all URLs named in the Aug 10 and May 4 audits) | Pass, 1 false alarm caught | All 40+ URLs returned 200 except: `/7-of-the-best-things-to-do-in-february/` returns 404 — **but this is a shorthand slug used in the old audit, not the real URL.** The real live page (`/7-of-the-best-things-to-do-in-february-in-new-orleans/`) is 200. No actual broken links found on the site itself in this pass. |
| Duplicate content / cannibalization | Fail | Two live pages target "best swamp tour": `/which-swamp-tours-are-the-best/` and `/which-is-the-best-swamp-tour-around-new-orleans/`. See §2. |
| URL collision (archive vs. real page) | Fail | `/tours/kayak-tours/honey-island-swamp-tour/` (blog category archive, zero schema, boilerplate meta) outranks the real tour page. See §2. |
| Schema markup — homepage | Partial | Organization, LocalBusiness, WebSite, VideoObject present. AggregateRating, FAQPage missing. |
| Schema markup — `/tours/swamp/` | Fail | BreadcrumbList only. |
| Schema markup — tour product pages | Fail | VideoObject/Organization present on Manchac page; no Product/Offer/AggregateRating on any tour page checked. |
| Schema markup — `/alligators-vs-crocodiles/` | Partial | Article, BreadcrumbList, Organization, ImageObject present. No FAQPage despite Q&A-formatted content. |
| HTTPS | Pass | Site fully on HTTPS, no mixed-content indicators in the homepage source. |
| Core Web Vitals / Lighthouse | **Stale data only** | Live PSI run blocked today (quota exhausted, no API key on file). Last successful run: 2026-06-19 (56 days old). See below. |
| GSC index status | **Not available** | GSC MCP not connected this session. No fresh indexed/discovered-not-indexed comparison possible today. |

### Core Web Vitals (last available data: 2026-06-19, 56 days old — treat as directional only)

| Strategy | Perf Score | LCP (lab) | CLS (lab) | TBT (lab) | Field data (CrUX: LCP/CLS/INP) |
|---|---|---|---|---|---|
| Mobile | **37 (red)** | 16.2s (very poor) | 0.005 (good) | 1,600ms (poor) | FAST / FAST / FAST |
| Desktop | 54 (amber) | 2.5s (good) | 0.009 (good) | 620ms (needs improvement) | FAST / FAST / FAST |

**Read this carefully:** the lab score (synthetic, single throttled test) says mobile performance is bad — 16.2s LCP is a real problem if it's reproducible. But the field data (actual CrUX data from real visiting users) shows FAST across LCP, CLS, and INP. That gap usually means the lab test hit an unusually slow simulated network/device profile, or there's a specific heavy asset (probably the homepage VideoObject / hero video) that tanks synthetic tests without hurting most real users on faster connections. **This needs a fresh PSI run before acting on it** — don't rebuild the homepage hero based on a 56-day-old single data point when the field data disagrees. Get a `PSI_KEY` set (`~/.claude/.env`, `PSI_KEY=...`) so the daily quota stops blocking re-runs.

---

## 6. Local Search / GBP (from Aug 10 audit — not independently re-verified today, GBP MCP unavailable)

NKST's GBP (740 N Rampart St, 4.9 stars, 1,416 reviews) is not appearing in the "swamp tour near me" local pack (12,100/mo) despite outperforming the #2 pack result (Tour Big Easy, 729 reviews) on both volume and rating. Two likely causes flagged in the Aug 10 audit, neither independently re-checked today:
- Primary GBP category is "Canoe & kayak tour agency" vs. pack winners' "Boat tour agency" / "Tour operator."
- Five David-controlled listings cluster within a few blocks of each other in the same proximity radius (NKST, Crescent City Kayak, Hidden Adventure, Admire New Orleans, and a listing at a fabricated "Swamp Tour Street" address), which can trigger Google's diversity filter and suppress all of them.

**This needs a live GBP check before acting** — flagging it here as carried-forward, not confirmed today.

---

## 7. Competitor Comparison

| Dimension | NKST | Wild Louisiana Tours / Crescent City Kayak | Cajun Encounters | Winner |
|---|---|---|---|---|
| GBP reviews / rating | 1,416 / 4.9 | Not directly comparable (CCK secondary property) | 12,000 / 4.9 | Cajun Encounters on volume, NKST close on quality |
| Local pack presence ("swamp tour near me") | Not in pack | N/A | In pack (#3) | Cajun Encounters |
| AI Overview commercial citations | 1 (rank 13) | Cited #1 by name in live test with full trip specifics | Not tested this pass | Wild Louisiana |
| Structured data (Product/Offer/Rating) | None found on any page checked | GetYourGuide listing carries verified reviews/structured specifics | Not tested this pass | Wild Louisiana (via 3rd-party listing) |
| Content coverage — haunted/legend angle | Absent | Explicitly rejected in their own copy ("education and safety, not folklore") | Not tested this pass | **Open — first mover wins** |
| Content coverage — practical anxiety (what to wear, kids, bugs) | Thin | Confirmed absent | Not tested this pass | Open |
| Head-to-head organic position (kayak/swamp queries vs. own CCK property) | Wins every head-to-head listed in the May audit | CCK loses every one | — | NKST |

---

## 8. Traffic & Conversion Context (GA4, March 2026 — 5 months old, directional only)

No fresh GA4 pull was possible this session. The most recent real data on file is the March 26, 2026 report (GA4 property 401824264, 90-day window). Treat these as directional, not current:

- 11,848 sessions / 90d, +44% sessions and +59% conversions month-over-month at the time (spring seasonal ramp).
- **Paid Search converted at 19.8%** vs. 13.0% organic, 8.7% direct — the ads report flagged this as likely underspent.
- **Paid Social converted at 0.8%** — flagged as essentially wasted spend at the time.
- **Conversion tracking gap:** only 58 `ads_conversion_Purchase_1` events tracked in 90 days against 23,385 GHL contacts — FareHarbor booking confirmations were not firing a GA4 purchase event as of March. This directly affects how much confidence to put in any GA4-sourced conversion-rate figure, including the two above; if it's still unfixed, treat all GA4 conversion numbers in this vault as undercounting real bookings.
- Alligator blog: 831 pageviews, 60% bounce rate (matches the GSC-side 0.16-0.32% CTR problem — people who do click are still leaving without converting).

**Recommend confirming whether the FareHarbor → GA4 purchase event was ever fixed** — this affects every conversion-rate number cited anywhere in NKST's marketing stack, not just SEO.

---

## 9. Prioritized Fix List

### Quick Wins (this week — all under a few hours each)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | Add a "More reading" internal-link block (top of post + conclusion) linking to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/` (no `/blog/` prefix — confirmed that's the live URL), and a more prominent CTA to the Manchac tour page above the fold. | Redirects a slice of 272k quarterly impressions toward money pages Google currently can't find via this route. Directly addresses why `/tours/swamp/` isn't ranking. |
| 2 | `/alligators-vs-crocodiles/` | Add FAQPage schema wrapping the existing alligator-vs-crocodile Q&A content (no new writing needed, just markup). | AI Overview / rich-result eligibility on a page already getting 272k impressions/quarter. |
| 3 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 redirect (or noindex, if 301 isn't feasible via the CMS) to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. Update any internal links pointing at the archive URL to point at the real tour page. | Stops a boilerplate blog-archive page from being Google's answer for a 9,900/mo keyword; consolidates link equity onto a real, sellable page. |
| 4 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 redirect into `/which-swamp-tours-are-the-best/`, merging any unique content first. | Ends self-cannibalization on "best swamp tour" queries; the survivor page has a real shot at moving from position 24 toward page 1 once it's not splitting signal with itself. |
| 5 | `/` (homepage) | Add AggregateRating (4.9, 1,416 reviews) schema. | Star-rating rich snippet in search results — a pure CTR play with no content risk, applies to the highest-traffic page on the site. |
| 6 | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` and the other 5 tour pages | Add Product + Offer (price/currency/availability) schema using pricing already published in the page body. | Price display in search results + AI-answer extractability; this is content that already exists, just not machine-readable. |
| 7 | `~/Projects/tech-seo/psi-run.mjs` environment | Get a free PageSpeed Insights API key and add it to `~/.claude/.env` as `PSI_KEY=...` (David can generate this at the Google Cloud Console; not something to do unattended). | Unblocks the ability to get a real, current Core Web Vitals read — the mobile perf score 37 finding is 56 days stale and needs re-verification before anyone spends a day rebuilding the homepage hero over it. |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 8 | `/tours/swamp/` | Rebuild as the true money page for "swamp tours new orleans" (highest-volume commercial cluster on the site). Expand to 2,000+ words: price, duration, drive time from the French Quarter, wildlife list, airboat-vs-kayak comparison, best time of year, what to bring, booking CTA. Add full FAQPage schema for the 4 confirmed PAA questions. Link to it from the homepage, the alligator page, and all swamp-related blog posts. | This is the single biggest lever identified across three audit passes (May, Aug 10, today). Currently the homepage — not this page — is what ranks, at position 15-21. A real money page with real internal-link support is the only way to close that gap. |
| 9 | New page: `/alligator-tour-new-orleans/` | Build a dedicated commercial page targeting "alligator tour new orleans" / "gator tour new orleans" (2,900/mo combined, currently unranked at position 45-51, no page exists). | Bridges NKST's existing AI-Overview alligator authority (25 citations, mostly trivia) to an actual bookable page — currently that authority converts to zero commercial value. |
| 10 | New page: `/kayak-vs-airboat-swamp-tour/` | Build a long-form, honest comparison page. This exact gap was independently identified in the May audit, the August audit, and the June competitor content-gap research — three separate passes, same conclusion. | NKST's whole brand position is anti-airboat; owning the comparison query both ranks and converts on-brand. Wild Louisiana avoids naming the airboat alternative at all, leaving this fully open. |
| 11 | New cluster: Manchac haunted-swamp pillar (Julia Brown legend, "is Manchac really haunted," sunset/night tours) | 3-4 new pages per the June competitor-gap research, cross-linked into a pillar hub. | Real search demand with zero competitor coverage — Wild Louisiana's own copy explicitly rejects folklore content, structurally locking them out. Best available "first mover" opportunity found in this audit. |
| 12 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite every section to end with a paid-tour comparison CTA instead of standing alone as a "don't pay us" post. | Redirects roughly 9,500/mo of commercial-intent search traffic currently landing on a page whose entire thesis argues against booking. |
| 13 | New page: "How much does a swamp tour cost?" | Build a direct-answer page with a real price-comparison table across operators (the format AI engines quote, per the Aug 10 live AI-search test). | Highest commercial-intent PAA question on the "swamp tours new orleans" SERP with currently nothing built for it. |
| 14 | GetYourGuide / TripAdvisor / Viator listings | Rewrite third-party OTA listing copy to lead with extractable specifics (exact duration, transport, species list, group size, difficulty) instead of mission-first language — matching how Wild Louisiana's GetYourGuide listing is written, since that's the page a live AI search actually quoted over NKST's own site. | This is the layer AI answer engines are sourcing from right now, confirmed by the live test in the Aug 10 audit. Site-level schema fixes (items 5-6, 8) won't fully close this gap without also fixing the OTA layer. |
| 15 | GBP: primary category + duplicate-listing cleanup | Needs a live GBP check first (not done today) to confirm the Aug 10 findings still stand: category mismatch ("Canoe & kayak tour agency" vs. pack winners' "Boat tour agency"/"Tour operator") and 5 nearby David-controlled listings possibly triggering Google's proximity diversity filter, including one at a fabricated address ("Swamp Tour Street") that's a standalone suspension risk regardless of the SEO angle. | Local pack eligibility for "swamp tour near me" (12,100/mo, currently 0% organic presence — this is 100% a local-pack game). |
| 16 | Crescent City Kayak property decision | Still open across three audits now. Either 301 the whole property into NKST (cleanest, captures ~600 clicks/quarter of split organic) or commit to rebuilding it as a genuine funnel with a hard CTA back to NKST bookings. | Every quarter this stays undecided, CCK keeps splitting authority on queries NKST already wins head-to-head. |

---

## Notes

- All URLs, HTTP status codes, schema types, and title/meta strings marked "confirmed live today" or "verified today" were checked directly against the production site on 2026-08-14 via HTTP requests — not assumed from prior audits.
- Numbers not re-pulled this session (GSC positions/impressions, GA4 sessions/conversions, GBP category/listing status, Core Web Vitals) are clearly dated to their source document above; none were guessed or extrapolated.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in the production of this report. Every action item above is a recommendation awaiting approval.
