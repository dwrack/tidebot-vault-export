# Austin Kayak Tours — SEO + Tech-SEO Audit (2026-08-15, Pass 2)

**INTERNAL REPORT ONLY — dated 2026-08-15, second pass. No changes were made to the live site, WordPress, GBP, or any ad account. Everything below is a finding or a recommendation for David/Connor/dev to act on later.**

This is the third audit in three sessions (2026-08-14, 2026-08-15 AM, this one). It does not repeat findings already logged as open in the first two — see the reconciliation table below for status on everything already flagged. This pass focuses on what's genuinely new: a deep dive on the two competitor domains flagged "for a closer look" yesterday, a real broken-link/redirect crawl, and item-by-item verification of internal links assumed-but-not-confirmed in both prior audits.

## Data sources used this session

- **Live site crawl** — direct `curl` + Python parsing against `https://www.austinkayaktours.com` (homepage, robots.txt, all 3 sitemaps, FAQ, homepage schema, `/covid-19-info/`, `/affiliates-influencers/`, `/austin-walking-tours/`, `/rainey-street-walking-bar-tour/`, the two pillar-page 404s, both duplicate-URL pairs) plus HEAD-status checks on every homepage-linked URL, run today 2026-08-15, PM.
- **Redirect chain check** — `curl -sIL` on 4 protocol/subdomain variants of the root domain, the duplicate URL pairs, `/kayak-paddleboard-rental/`, and both `lonestarkayaktours.com` variants.
- **Internal-link verification** — for the first time, actually fetched all 7 blog posts named in the 2026-08-14 audit's "corrected internal linking" table and grepped each for a live link to its assigned money page, instead of assuming status. Results below — several were already wrong assumptions in both prior audits.
- **Competitor deep-dive** — full crawl (headers, title, meta, body text, outbound links, hosting headers) of `kayakaustintours.com` and `austinpaddle.com`, the two domains flagged yesterday as "new sightings, not fully profiled." Both are resolved this session — see Executive Summary.
- **WebSearch** — one query to corroborate `austinpaddle.com`'s real-world footprint (Yelp, TripAdvisor, Facebook, X/Twitter, address).
- **PageSpeed Insights API** — re-attempted via `~/Projects/tech-seo/psi-run.mjs`. Still HTTP 429 (quota exceeded). **Third consecutive audit blocked.**
- **MCP tool discovery** — ran `ToolSearch` against every server declared in this vault's `.mcp.json` (`google-austin`, `gbp`, `meta-organic`). Confirmed via direct inspection of `~/.claude/mcp-servers/google-personal/index.js` that the server *does* define `gsc_list_sites`, `gsc_search_analytics`, `gsc_top_queries`, `gsc_top_pages`, `gsc_keyword_opportunities`, `gsc_index_status`, `ga4_run_report`, `ga4_top_pages`, `ga4_traffic_sources`, `ga4_conversions`, `ga4_compare_periods`, and a `gmb_*` set — but none of those tools, nor any `gbp_*` or `meta-organic` tool, were discoverable via `ToolSearch` in this session, meaning the MCP connections were not live/loaded for this run. This is now the **third straight audit with zero GSC/GA4 data**, and the first time it's confirmed the tools exist and are configured (a token file for `austinkayaktours-at-gmail-com.json` exists locally) but simply weren't connected this session — worth a quick manual check of whether the MCP server needs to be restarted/re-authed rather than built from scratch.
- **Vault docs** — both prior audits, `SEO Action Plan & Blog Pipeline.md`, `Ranking Baseline 2026-06-07.md`, `AI-SEO-Bat-Tours-Action-Plan.md`, all 10 `SEO Content` cluster folders + Pillars, and `Blog Drafts - Staged/` (re-listed to catch anything added since this morning).

---

## Executive Summary

The single biggest finding this session reframes something both prior audits got wrong: **`austinpaddle.com` ("Austin Paddle Shack"), flagged yesterday as a new competitor, is not a competitor.** It is, with very high confidence, the same physical business as Austin Kayak Tours. Evidence, all confirmed live today: (1) its FareHarbor booking widget uses the exact same account slug, `fareharbor.com/embeds/book/lonestarkayaktours`, as both `austinkayaktours.com` and `lonestarkayaktours.com`; (2) it shares the identical WordPress VIP host-header (`a9130478a60e5f9135f765b23f26593b`) with `austinkayaktours.com` — same physical hosting instance; (3) its "About Us" page lists the meeting location as "200 E Riverside Dr, Austin, TX 78704," the exact address on file for AKT itself; (4) it lists the identical tour catalog at identical prices (Sunset Bat Bridge Kayak Tour $50, Austin Skyline Tour $50, 4th of July $85, Paddle Board tours); (5) it has its own `/affiliates-influencers/` page mirroring AKT's, suggesting the same site template/build. This means the "duplicate domain" problem flagged twice already isn't a 2-domain problem, it's a confirmed **3-domain problem** — `austinkayaktours.com`, `lonestarkayaktours.com`, and now `austinpaddle.com`, all live, independently indexable, and all pulling from the same tour inventory and the same address. Worse: `austinpaddle.com` has a real, separate social/review footprint (71 Yelp reviews, a TripAdvisor listing, its own Facebook/Instagram/X accounts per today's WebSearch) that's fragmenting review and citation equity that should be consolidating under one brand.

Second finding: **`kayakaustintours.com` is confirmed as an outside brand-hijack / affiliate doorway site, not a legitimate operator.** Its `<title>` tag literally reads "🛶 Austin Kayak Tours | Explore Lady Bird Lake..." — it puts our exact brand name in its own title tag. It runs on plain nginx/WordPress (not WP-VIP, not related infrastructure), links out to Expedia and VRBO affiliate programs, and cross-links a small network of sibling doorway sites (`funaustintours.com`, `iloveaustintours.com`, `austinbattours.com`, `austinpaddletours.com`, `texascapitoltours.com`) that all appear to be the same content-farm operator running city-specific SEO doorway pages. This is worth a Google spam/trademark report, not just "keep an eye on it."

Third finding: for the first time, the internal-link items both prior audits carried forward as "not re-verified, assume still open" were actually checked. **5 of 7 flagged blog-to-money-page links are already live**; the 2 that are genuinely still missing both point to the same target, `/corporate-events/` (`why-team-building-is-great-on-kayaks` and `austin-bachelorette-party-guide`). This narrows a vague "assume still open" item into a precise 2-link fix.

Fourth finding: `/covid-19-info/` is still live, still indexed in the 9-URL page sitemap, and still serving 2020-era pandemic-protocol copy in August 2026 — a stale-content/trust flag not previously called out by page name in either prior audit.

Fifth: nothing published since this morning. Sitemap counts are unchanged (57 posts, 9 pages), the FAQ page still has zero FAQPage schema, both pillar pages are still 404, and PSI is still 429 for a third straight day. The three new staged blog drafts created today (`halloween-kayak-tour-austin.md`, `all-day-skyline-swimming-hole-tour-austin.md`, `clear-kayak-tour-austin-comparison.md`) directly answer this morning's own content-gap recommendations — the pipeline is moving even though publishing isn't.

**Top 3 priorities by impact this pass:** (1) get a straight answer from Connor/David on whether `austinpaddle.com` is company-owned — if yes, this is now the highest-value strategic fix on the list, bigger than the `lonestarkayaktours.com` problem alone, because it's actively earning independent third-party reviews that should be consolidating under one brand; (2) file a Google spam/trademark report on `kayakaustintours.com` for using the exact brand name in its title tag; (3) ship the two now-precise corporate-events internal links (5-minute fix, no more guessing).

---

## What's still open vs. both prior audits (explicit reconciliation)

| # | Item (from 08-14 / 08-15 AM) | Status this session |
|---|---|---|
| FAQPage schema on `/faq/` | **Still open.** Reconfirmed: zero "FAQPage" occurrences in page source. |
| Homepage LocalBusiness/Organization schema — thin | **Still open, unchanged.** `reviewCount: "4"`, `ratingValue: "5"` still live on the `Product`/`Review` blocks; no `sameAs` array present. **New this pass: the real sameAs URLs are now confirmed** (see On-Page Issues table) — this is now a copy-paste fix, not a "go find the links" task. |
| `/kayak-paddleboard-rental/` 404 | **Still open.** Reconfirmed 404. |
| Two pillar pages not published | **Still open.** Both 404, not in page-sitemap (still 9 URLs). |
| Homepage "Learn More" CTAs | **Confirmed still open** (not just assumed, as in both prior audits) — exact count re-verified: 7 instances of literal "Learn More" text still live in the page source today. |
| Internal links from the 7-post table (08-14 audit) | **Partially resolved — new precision this pass.** 5 of 7 are actually live: `some-reasons-to-check-out-the-south-congress-bat-colony` → bat tour (linked), `dog-friendly-austin-businesses` → `/rental/` (linked), `five-great-ideas-for-an-austin-vacation` → skyline tour (linked), `breakfast-ideas-in-austin` → skyline tour (linked), `rainy-days-outdoor-eating-in-austin` → skyline tour (linked). **Still missing:** `why-team-building-is-great-on-kayaks` → `/corporate-events/` (0 mentions) and `austin-bachelorette-party-guide` → `/corporate-events/` (0 mentions). Both prior audits treated all 6-7 of these as one undifferentiated "still open" line item; that was imprecise — most of this work already shipped. |
| `lonestarkayaktours.com` duplicate domain | **Still open, and now understood to be worse than reported** — see Executive Summary. A third domain (`austinpaddle.com`) is doing the same thing. |
| Duplicate URL pairs (`paddleboard-tour`, `corporate-events`) | **Still open.** Both pairs reconfirmed HTTP 200/200, no redirect, on both. |
| Halloween / All Day Skyline-Swimming Hole — schema + linking gap | **Still open**, not re-crawled at the schema level this session (already confirmed twice); **new this pass:** the two staged drafts for these topics exist as of today (see below), so content is coming even if the live-page schema fix isn't done yet. |
| Cluster A + staged drafts not published | **Still open.** Sitemap re-pulled: still exactly 57 post URLs, unchanged from both prior sessions today. |
| PSI / Core Web Vitals baseline | **Still blocked — third consecutive day.** 429 again, confirmed via a fresh run this session. |
| GSC/GA4 MCP connection | **Still not usable this session** — see Data Sources note above; now confirmed the tools exist server-side but aren't loading, which is a smaller fix than "connect from scratch." |
| kayakaustintours.com / austinpaddle.com — "not fully profiled, flag for closer look" | **Resolved this session.** See Executive Summary — one is a brand-hijack doorway site, the other is very likely a sibling domain of AKT itself. |

---

## New findings this session (not in either prior audit)

1. **`austinpaddle.com` is very likely a third AKT-operated domain, not a competitor.** Full evidence chain in the Executive Summary. This needs a direct question to Connor: "Do we operate Austin Paddle Shack / austinpaddle.com?" If yes, it should be added to every future audit's own-property list, not the competitor table, and its reviews/social accounts should be evaluated for consolidation or explicit cross-linking.

2. **`kayakaustintours.com` confirmed as a brand-hijacking affiliate doorway site**, not an independent operator, with concrete evidence: title tag containing our exact brand name, Expedia/VRBO affiliate links, and links to a 5-site doorway network (`funaustintours.com`, `iloveaustintours.com`, `austinbattours.com`, `austinpaddletours.com`, `texascapitoltours.com`). Confirmed on plain nginx hosting, unrelated to AKT's WP-VIP infrastructure — i.e., a genuine outside actor, unlike `austinpaddle.com`.

3. **Real `sameAs` social URLs captured live from the homepage/footer**, ready to paste into the schema fix that's been flagged twice: `https://www.facebook.com/austinkayaktours/`, `https://www.instagram.com/austinkayaktours`, `https://www.tripadvisor.com/Attraction_Review-g30196-d11876981-Reviews-Austin_Kayak_Tours-Austin_Texas.html`, `https://www.yelp.com/biz/austin-kayak-tours-austin`.

4. **`/covid-19-info/` is live, indexed, and stale.** Title "Covid-19 Info | Austin Kayak Tours," meta description about "steps we are taking to help protect the health and safety of our customers and staff during Covid-19." Consumes one of only 9 static-page sitemap slots on a 2026 tour-booking site. Low urgency but a real freshness/trust flag, and an easy one to fix (redirect or update).

5. **`/austin-walking-tours/` and `/rainey-street-walking-bar-tour/` — both real, live money pages with only a `BreadcrumbList` schema block, no `Product` schema.** Both were previously spot-checked for HTTP 200 only ("money pages spot-checked healthy" in the 08-15 AM audit) but never checked for schema depth. Same gap pattern as the already-flagged Halloween and All Day Skyline/Swimming Hole pages — this is a 4-page pattern now, not 2.

6. **Redirect-chain measurement done for the first time.** `http://austinkayaktours.com` (no www, no https) takes 2 hops to reach `https://www.austinkayaktours.com/`; `http://www.austinkayaktours.com` and `https://austinkayaktours.com` each take 1 hop. Not broken, but worth collapsing to a single 301 per entry point if a dev touches redirect rules for the `lonestarkayaktours.com` work anyway — free crawl-budget cleanup bundled into work that's happening regardless.

7. **The 3 new staged drafts created today directly answer this morning's own content-gap list.** `Blog Drafts - Staged/2026-08-15 - halloween-kayak-tour-austin.md`, `2026-08-15 - all-day-skyline-swimming-hole-tour-austin.md`, and `2026-08-15 - clear-kayak-tour-austin-comparison.md` map 1:1 to gap items #1, #2, and #3 from the 08-15 AM audit. Good sign the content pipeline is being worked; still nothing published, so this doesn't change the "zero live changes today" bottom line, but it's forward motion worth noting so nobody re-assigns those topics as still-open gaps.

---

## Content gap recommendations — status update

All 5 gaps from the 08-15 AM audit are unchanged in terms of live-site impact, but 3 of 5 now have drafts (see finding #7 above). Remaining genuinely open, undrafted gaps:
- **Brand-disambiguation / About page content** — more urgent than ever given today's findings. With `kayakaustintours.com` (hijack), `lonestarkayaktours.com` (legacy dupe), and now `austinpaddle.com` (likely sibling) all live and indexable under variations of the same brand, a real About/ownership page is now a defensive necessity, not a nice-to-have.
- **Austin Paddle Shack comparison content** — **retract this recommendation.** Yesterday's audit suggested a future "competitor comparison" post against Austin Paddle Shack. Given today's finding that it's very likely the same business, do not write competitor-comparison content against your own second brand — flag this to whoever owns the content calendar so it doesn't get assigned.

---

## On-page issues table (new/updated items only — see prior audits for the full carried-forward list)

| Page | Issue | Severity | Recommended Fix |
|---|---|---|---|
| `/` (homepage) | `sameAs` still missing from `LocalBusiness` schema, but the real URLs are now on hand (see New Findings #3) | High | Paste the 4 confirmed URLs into the `sameAs` array of the existing `LocalBusiness` JSON-LD. No more research needed, this is copy-paste. |
| `/covid-19-info/` | Live, indexed, 2020-era COVID protocol content in 2026 | Medium | Either 301 this to `/faq/` or homepage, or replace with current health/safety info if still relevant (life vests, weather policy). Recovers one of 9 static-page sitemap slots for something useful. |
| `/austin-walking-tours/` | Only `BreadcrumbList` schema, no `Product` schema | Medium | Add `Product` schema per the existing library pattern — same fix already scoped for Halloween/Skyline-Swimming pages, just extend to this page too. |
| `/rainey-street-walking-bar-tour/` | Only `BreadcrumbList` schema, no `Product` schema | Medium | Same fix. |
| `/blog/why-team-building-is-great-on-kayaks/` | Zero links to `/austin-kayak-tours/corporate-events/` despite being the exact planned source page | Medium | Add 1 contextual link with anchor "book a corporate kayak event," per the original 08-14 plan — this specific link never shipped. |
| `/blog/austin-bachelorette-party-guide/` | Zero links to `/austin-kayak-tours/corporate-events/` | Medium | Same fix, same target page. |
| `austinpaddle.com` (third-party-looking domain) | Very likely company-owned but operating as an independent, fully indexed competitor to the main domain for identical tour terms | Critical (pending confirmation) | Get a direct yes/no from Connor. If confirmed company-owned: either consolidate into one domain via 301s, or explicitly cross-link/canonical the two so Google stops treating them as unrelated competing sites for the same queries. |
| `kayakaustintours.com` (outside site) | Brand-hijacking title tag using our exact business name, funnels to Expedia/VRBO affiliate links | High | File a trademark/spam report with Google (Search Console "report spam" tool, or a formal trademark complaint if the brand is registered). Not fixable on our own site — flagging for a business decision, not a content edit. |

---

## Technical SEO Checklist — delta from prior sessions

| Check | Status | Details |
|---|---|---|
| Redirect chains | **New this session — PASS with a minor note** | Root domain variants resolve to the canonical `https://www.` URL in 0-2 hops. No broken chains. The 2-hop bare-http path is a minor cleanup candidate, not urgent on its own. |
| Broken-link crawl (homepage, depth 1) | **New this session — PASS** | All 12 same-domain links reachable from the homepage returned HTTP 200. No new 404s found beyond the already-known `/kayak-paddleboard-rental/`. |
| Sitemap counts | **Unchanged** | 57 post URLs, 9 page URLs — identical to both prior audits today. Confirms zero publishing since this morning. |
| Core Web Vitals / PageSpeed | **Still blocked, 3rd consecutive day** | Re-ran `psi-run.mjs mobile` this session — HTTP 429 on every one of the 8 domains checked, not just AKT. This is a shared-quota project problem across all of David's sites, not AKT-specific. |
| GSC/GA4 MCP | **Still not connected this session**, but now confirmed the server code and a token file both exist — likely a live-connection issue, not a from-scratch setup. Worth a 5-minute check before assuming this needs a new integration. |
| robots.txt | **PASS, unchanged** | Reconfirmed valid, sitemap referenced, no AI-crawler blocks. |

---

## Prioritized Fix List

### Quick Wins (this week, low effort / high leverage)

1. **Paste the confirmed `sameAs` URLs into the homepage `LocalBusiness` schema.** Exact page: `https://www.austinkayaktours.com/`. Exact URLs to add: `https://www.facebook.com/austinkayaktours/`, `https://www.instagram.com/austinkayaktours`, `https://www.tripadvisor.com/Attraction_Review-g30196-d11876981-Reviews-Austin_Kayak_Tours-Austin_Texas.html`, `https://www.yelp.com/biz/austin-kayak-tours-austin`. This was flagged twice before as "needs research"; the research is done, it's now a straight copy-paste. Expected impact: proper entity linking for Knowledge Panel and AI-citation eligibility.
2. **Add the 2 still-missing internal links to `/corporate-events/`.** Exact pages: `https://www.austinkayaktours.com/blog/why-team-building-is-great-on-kayaks/` and `https://www.austinkayaktours.com/blog/austin-bachelorette-party-guide/`. Exact change: add one contextual link each to `/austin-kayak-tours/corporate-events/` (use the nested URL, not the bare duplicate) with descriptive anchor text. Confirmed today these are the only 2 of 7 planned links that never shipped. Expected impact: closes the corporate-events link gap precisely, no more guessing which of the 7 are done.
3. **Fix or retire `/covid-19-info/`.** Exact page: `https://www.austinkayaktours.com/covid-19-info/`. Exact change: 301 to `/faq/` (or update the content if there's a real current health/safety policy worth keeping). Expected impact: removes a stale-content flag from one of only 9 indexed static pages, minor trust/freshness signal improvement.
4. **Add `Product` schema to `/austin-walking-tours/` and `/rainey-street-walking-bar-tour/`.** Same schema-library pattern already scoped for the Halloween and All Day Skyline/Swimming Hole pages — bundle all 4 into one schema pass instead of doing it twice.
5. **Get a direct answer on `austinpaddle.com` ownership** (not a content task — a one-line question to Connor). This gates whether item #1 in Strategic Work below is "consolidate our own domain" or "monitor a competitor," and it's cheap to resolve immediately.

### Strategic Work (this quarter, higher effort)

1. **Resolve the (now 3-domain) duplicate-property problem: `austinkayaktours.com`, `lonestarkayaktours.com`, and likely `austinpaddle.com`.** If `austinpaddle.com` is confirmed company-owned, this becomes the single highest-priority item across all three audits — it means real third-party review equity (71 Yelp reviews, a TripAdvisor listing) is currently split across brands that should be one. Decide: consolidate to one domain with 301s and merged reviews/citations, or keep both but stop them from independently targeting the same search terms (differentiate content, cross-canonical).
2. **File a spam/trademark report on `kayakaustintours.com`.** Concrete evidence gathered this session (title tag using the exact brand name, affiliate-network links) is enough to support a Google Search spam report and/or a trademark complaint if "Austin Kayak Tours" is a registered mark. This is a business/legal action item, not a content fix.
3. **Build the About/ownership page**, now more urgent given 3 confirmed brand-confusion-adjacent domains in the landscape (`kayakaustintours.com`, `lonestarkayaktours.com`, `austinpaddle.com`). Still not live anywhere on the site, still flagged in all three audits this week.
4. **Everything carried forward and unchanged from the prior two audits** — FAQ schema, pillar page publishing, Halloween/Skyline-Swimming Hole full schema + linking build-out, Cluster A + staged draft publishing, PSI key setup, GSC/GA4 MCP reconnection. Not re-litigated here; see the 2026-08-15 AM audit's Strategic Work section, all 8 items are still open.

---

*Compiled 2026-08-15, Pass 2. REPORT ONLY — no live-site, WordPress, GBP, or ad changes were made in the course of producing this report.*
