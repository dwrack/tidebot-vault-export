# Buffalo Bayou Kayak — SEO / AEO / GEO Audit (June 2026)

Audited: buffalobayoukayak.com (15-page crawl, sitemap review, SERP research, ads account review). GSC and GA4 data unavailable, see Data Plumbing below.

## Executive Summary

BBK owns its brand SERPs and the core "buffalo bayou kayak tour" queries outright, and it has solid earned listings (Visit Houston, Downtown Houston, TripAdvisor, Peek, GetYourGuide). The problems are everything around that core: zero measurement plumbing (GSC, GA4, GBP all disconnected from the management account), all Google Ads campaigns for BBK paused, a blog that died in November 2023 and was written for nobody's actual searches, tour pages with no Product or FAQ schema (so AI engines have nothing structured to cite), and total absence from the discovery-layer content where tourists and locals actually start ("where to kayak in Houston", "Waugh Bridge bats", "things to do in Houston outdoors").

The single biggest opportunity is the **Waugh Bridge bat colony**. 250k bats, a famous free attraction, heavy informational search volume, and the proof is in your own ads account: the Austin bat campaign converts at 16-38x ROAS on identical query patterns. BBK has the only kayak-based bat experience in Houston and barely talks about it outside one 691-word tour page.

## Data Plumbing (fix first, blocks everything else)

| System | Status | Fix |
|--------|--------|-----|
| Google Search Console | buffalobayoukayak.com NOT in the connected account (20 other properties are) | Add the management Google account as a user on the GSC property, or verify the domain if no property exists |
| GA4 | No BBK property accessible | Same, grant access to the management account |
| Google Business Profile | Connected GBP account is an unverified personal account, no BBK location | Confirm who owns the BBK listing and grant access |
| Google Ads | Account 8497383499 reachable, but ALL BBK campaigns paused ([FH] Brand, [FH] Generic Local/National, TourPPC Buffalo Bayou x3) | Decide: reactivate at least Brand + a Bat-focused generic campaign |

Without GSC we cannot see striking-distance keywords or CTR problems. Re-run the keyword portion of this audit once connected.

## Keyword Landscape

No GSC data, so this is built from SERP research + the ads account + competitor analysis.

### What BBK already owns (defend)
- "buffalo bayou kayak tour", "buffalo bayou kayak rental" — #1-2, plus TripAdvisor/Peek listings stacking the SERP
- "houston bat bridge kayak tour" — #1 for the kayak-specific variant
- Brand queries

### Tier 1 — Bat queries (highest commercial upside)
Owned today by buffalobayou.org (Partnership), downtownhouston.org, TPWD, 365thingsinhouston, Yelp. BBK only ranks when "kayak" is in the query. Targets:
- waugh bridge bats / waugh drive bat colony
- where to see bats in houston / houston bat bridge time
- bats in houston tonight (the Austin account shows "time today" queries convert)
- The Partnership's boat tour is the substitute product ($30/person); BBK's angle: see the emergence FROM THE WATER.

### Tier 2 — Category queries (tourist + local, transactional)
- kayaking in houston / kayak houston (listicles + aggregators own top; BBK appears mid-page)
- kayak rental houston / paddle board rental houston
- sunset kayak houston, night kayaking houston, full moon kayak
- things to do on buffalo bayou

### Tier 3 — Question queries (AEO, very winnable, currently held by tiny niche blogs)
- is buffalo bayou safe to kayak (held by rapidsriders.net, kayakbase.com, mustangsurvival blog)
- are there alligators in buffalo bayou (BBK HAS this post; it's thin, vague, and buried at a dated URL)
- can you swim in buffalo bayou / how clean is buffalo bayou
- where to launch a kayak in houston / buffalo bayou launch points

### Tier 4 — Discovery layer (locals; rank OR get cited)
- things to do in houston outdoors / this weekend
- date ideas houston / sunset date ideas houston
- team building activities houston, bachelorette party ideas houston
- buffalo bayou park guide (parking, trails, launches)

## On-Page Issues

| Page | Issue | Severity |
|------|-------|----------|
| ALL tour/activity pages | Only BreadcrumbList JSON-LD. No Product, no FAQPage, no offers/price/duration in schema | Critical (AEO) |
| /faq/ | No FAQPage schema; only 783 words; no H2 structure | Critical (AEO) |
| /about/ | Meta description truncated to 66 chars: "…fun on Houston" — cut at an apostrophe (matches the known FareHarbor theme quote-stripping bug) | High |
| All tour pages | Thin: 625-740 words each | High |
| Blog (all 11 posts) | Orphaned: zero links from tour pages or /kayak-tours/ hub to any post; only homepage widget links in | High |
| /kayak-tours/houston-kayak-tour/ | Title says "Kayaking in Houston City Tours", H1 says "Houston Skyline Tour" — keyword/identity mismatch | Medium |
| /kayak-tours/houston-bat-bridge-kayak-tour/ | H1 is "Sunset Skyline Bat Bridge Kayak Tour" — burying the money phrase | Medium |
| Sitewide | First image on every page missing alt; remaining alts are auto-generated junk ("a river with a city in the background") | Medium |
| Blog URLs | Date-based (/2023/11/02/) — makes content look stale to users and AI | Low (don't migrate, fix going forward) |

## Technical

- robots.txt: fine. Junk bots blocked; AI crawlers (GPTBot, ClaudeBot, PerplexityBot) NOT blocked — correct for GEO. Note the trailing `Disallow: /fhbr-console/` lines sit after the last UA group; harmless but sloppy.
- Sitemaps: clean 3-index structure. Seasonal pages (NYE fireworks, Holiday Helpers) sit in the activity sitemap year-round.
- Canonicals + OG tags present everywhere. HTTPS fine.
- HTML weight 120-185KB per page, typical for the FH WP-VIP theme.

## GEO / AEO Findings

Where AI engines and answer boxes pull Houston kayaking info from: buffalobayou.org, downtownhouston.org, TPWD, Yelp, TripAdvisor, 365thingsinhouston, paddlingmag, niche kayak blogs.

BBK cited/listed on: Visit Houston, Downtown Houston, TripAdvisor (attraction + product), Peek, BucketListers, GetYourGuide, trailexpeditions.com.

**Missing from:** paddlingmag.com's "Guide to Kayaking Houston" (names Bayou City Adventures, Pinky's, Riva Row — not BBK), 365thingsinhouston bat article, Houstonia/Secret Houston style listicles, Yelp prominence is weak.

GEO levers in priority order:
1. Product + FAQPage schema on money pages (gives AI structured price/duration/meeting-point to cite)
2. Question-formatted content that directly answers Tier 3 queries
3. Earned mentions: pitch paddlingmag for inclusion, get into 365thingsinhouston's bat piece, Houston First/Houstonia outreach
4. Keep entity data consistent: GBP, TripAdvisor, Yelp, site all matching

## Competitors

- **Bayou City Adventures** (1520 Silver St) — still open, the name guides reach for. BBK outranks them on core SERPs now but BCA holds the legacy citations.
- **Buffalo Bayou Partnership** — not a kayak competitor but owns ALL bat authority and runs the $30 bat boat tour. Partner/coexist content-wise; their pages are the ones AI quotes.
- Riva Row Boathouse (Woodlands), Pinky's Kayak Rental, Armand Bayou Nature Center — adjacent geography, win "where to kayak in Houston" roundup queries by covering them honestly in a guide.

## Content Plan (12 briefs, roughly in order)

1. **Waugh Bridge Bat Colony: The Complete Guide** — emergence times by month, best viewing spots (platform vs water), season (Feb-Nov), FAQ schema. The GEO flagship. Link to bat tour page.
2. **Where to Kayak in Houston: Every Launch, Rental & Tour (2026)** — beat paddlingmag/kayakbase with genuinely better local detail. Cover competitors honestly.
3. **Is Buffalo Bayou Safe to Kayak?** — rewrite/expand the existing alligator post angle: water quality, swimming, gators, flood flow. Currently won by tiny blogs.
4. **Are There Alligators in Buffalo Bayou?** — upgrade existing 848-word post: direct answer up top, FAQ schema, internal links.
5. **Buffalo Bayou Park: Parking, Trails, Launches & What to Do** — local + tourist utility page.
6. **Houston Date Ideas on the Water** (sunset/full moon tours as the answer) — local.
7. **Things to Do Outdoors in Downtown Houston** — tourist discovery.
8. **Kayaking for Beginners in Houston: What to Wear & Expect** — converts nervous first-timers.
9. **Best Time of Year to Kayak in Houston** — seasonality + weather.
10. **Houston Skyline: Best Photo Spots (Including From the Water)** — link bait.
11. **Team Building in Houston: Why the Bayou Beats the Conference Room** — links corporate-events page.
12. **Full Moon Kayak Dates 2026** — update annually, captures "full moon tonight houston" adjacency.

Publishing: 2/month is enough. Every post links to 2+ tour pages with descriptive anchors, and tour pages get a "From the blog" block so posts are no longer orphaned.

## Prioritized Action Plan

**This week (quick wins):**
1. Get GSC + GA4 + GBP access connected (blocks all measurement)
2. Add Product + FAQPage JSON-LD to all 7 kayak tour pages + rental page via the Schema Markup ACF field (raw JSON, no script wrapper, no escaped inner quotes; verify live with JSON.parse after save)
3. Add FAQPage schema + expand /faq/ to 20+ questions with crawlable answer text
4. Fix /about/ meta description, fix bat-tour H1 to "Houston Bat Bridge Kayak Tour", align houston-kayak-tour title/H1
5. Reactivate [FH] Brand campaign + build a Bat-Local generic campaign modeled on the Austin one
6. Alt text pass on tour page images

**This quarter (strategic):**
1. Publish briefs 1-5 (bat guide first, before peak summer bat season attention)
2. Internal linking: blog block on tour pages, blog link in nav, hub interlinks
3. Earned-citation outreach: paddlingmag, 365thingsinhouston, Houstonia, Visit Houston content team
4. Re-run keyword audit with real GSC data after 4-6 weeks of collection
5. Refresh remaining 2023 history posts: merge the 8 thin history essays into one strong "History of Buffalo Bayou" pillar, redirect the rest
