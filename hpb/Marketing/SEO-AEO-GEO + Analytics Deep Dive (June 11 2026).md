# SEO / AEO / GEO + Analytics & GSC Deep Dive (June 11, 2026)

**Data:** GSC Mar 13 - Jun 11 (domain property), GA4 last 90 days, live site crawl June 11.
**Prior docs:** `SEO Audit & Plan (June 2026).md` (Jun 7), `SEO Fixes — Paste-Ready Assets (June 2026).md`, `AI SEO Audit & Action Plan (May 2026).md` (May 9).

---

## The headline

Since the June 7 audit, schema finally shipped on the homepage. That's real progress, but it shipped with bugs: the phone number renders as `++8329740365` (double plus, invalid), `openingHoursSpecification` is an empty array, there's no `aggregateRating`, no `sameAs` links, and the business name is still "Houston Pedal Barge" with a kayak logo, four days after the decision to lead with Party Barge. An `llms.txt` also exists now (good for GEO), but it opens with "pedal-powered party barge," the exact framing we decided to kill.

Everything else from the June 7 plan is still unshipped, and it's all sitting pre-written in the Paste-Ready Assets file:
- Homepage title still "Clear Lake Party Boats | Houston Party Barge", meta still says "Seakbrook"
- Money page title still generic, meta still promises "you'll pedal"
- Zero FAQ blocks, zero FAQPage schema, no Product schema on the money page (just a BreadcrumbList)

And the biggest new finding from this pass: **GA4 has zero conversion events.** Not one. 21,000 sessions in 90 days and we cannot say which channel, page, or keyword produced a single booking. Every SEO decision is being made blind on the revenue side.

---

## 1. GSC: where the demand actually is

~1,810 organic clicks / 90 days. Brand is locked (houston pedal barge pos 2.7, houston party barge pos 1.0).

### Striking distance (pos 5-10, real volume): the near-term money

| Query | Pos | Impressions | CTR | Audience |
|-------|----:|------------:|----:|----------|
| houston party boats | 7.2 | 885 | 2.7% | Both |
| boat rides houston (+9 variants) | 6.6 | ~2,400 combined | ~3% | Visitors |
| paddle boat houston / paddle boat | 8.5 | 1,192 combined | 0.8% | Locals (mixed intent) |
| kemah boat ride (+variants) | 6.2 | ~725 combined | 1.5% | Visitors |
| booze cruise (+houston, near me) | 7-8 | ~780 combined | 1.5% | Both |
| party yacht rental houston | 8.0 | 265 | 4.2% | Locals |
| pedal boat houston | 8.0 | 295 | 1.4% | Locals |
| dinner cruise houston (+variants) | 7.9 | ~190 combined | 7% | Both |
| boat tours houston / in houston | 6.5-10.4 | ~340 | 2% | Visitors |
| yacht party houston | 8.4 | 119 | 3.4% | Locals |

### Page 2 hostages (pos 11-20, one push from page 1)

| Query | Pos | Impressions |
|-------|----:|------------:|
| party boat | 14.0 | 503 |
| party barge | 15.4 | 501 |
| boat rental houston (+5 variants) | 13.5-18.4 | ~480 combined |
| party boats | 11.9 | 165 |
| sunset cruise houston | 11.1 | 29 |
| barge party / barge boat party | 14.4 | 127 |

### The CTR bleed (unchanged since May)

| Page | Impressions | Clicks | CTR | Pos |
|------|------------:|-------:|----:|----:|
| /houston-party-barge-cruise/ | 11,311 | 50 | 0.44% | 8.0 |
| /corporate-group-event/ | 9,635 | 6 | 0.06% | 8.5 |
| /about/ | 9,173 | 3 | 0.03% | 6.2 |
| /contact/ | 8,712 | 2 | 0.02% | 6.1 |

~39,000 impressions producing 61 clicks. At a normal 3-5% CTR for those positions, that's 1,200-1,900 clicks a quarter being left on the table. The rewritten titles and metas are sitting in the Paste-Ready file.

### Search appearance check

The only rich result type Google shows us under is REVIEW_SNIPPET (2,558 impressions, pos 14). No FAQ rich results, no product snippets, confirming the schema gap on the money page.

### Quiet signals worth noting
- "bachelorette houston" showed us at position 2 the one time it surfaced. The demand is real (AI engines cite Gulf Coast Party Boats for Seabrook bachelorette queries, not us). We have zero bachelorette content.
- "4th of july boat fireworks" already surfaces us. July 4 is in 3 weeks and /4th-of-july-firework-spectacular/ had 15 pageviews in 90 days. Push it now or lose the season.
- "kemah boardwalk boat rides": 2 impressions, 2 clicks, 100% CTR. Tiny sample, but it's the visitor query in miniature.
- www vs non-www consolidation still settling (www homepage: 1,116 clicks pos 4.5; non-www: 654 pos 9.6). Canonical is correct; just watch it.

---

## 2. GA4: the analytics story

90-day channel mix (~21k sessions):

| Channel | Sessions | Bounce | Verdict |
|---------|---------:|-------:|---------|
| Facebook (all variants) | ~12,250 | 83-97% | Huge volume, near-zero engagement. Vanity traffic. |
| Instagram | ~3,140 | 94% | Same. |
| Organic search | 2,035 | 43% | Best-quality traffic on the site by far. |
| Direct | 1,942 | 75% | |
| Paid search | 1,006 | 42% | Engages well. |
| visithoustontexas.com | 54 | 50% | Small but high quality. Nurture this listing. |
| AI (ChatGPT + Gemini) | ~22 | ~50% | The GEO baseline. Track it. |

What this means:
1. **Zero conversion events configured.** No purchase, no book-button click, no FareHarbor handoff event. The FareHarbor → GA4 integration was never wired (known issue, `project_hpb_ga4_status`). This is the single most important analytics fix: until it's done, we can't prove SEO (or the $1k/90d of paid search) produces revenue.
2. The ~15k social sessions bouncing at 90%+ means the headline traffic number is mostly worthless clicks. Organic search is 10% of sessions but almost certainly the majority of bookings. More reason to fund SEO work over posting cadence.
3. Homepage holds 21k of 23k pageviews with 83% bounce and 21-second average. People land and leave. The money page, when people reach it, holds them 107 seconds at 27% bounce. Getting more landers onto tour pages (internal links, nav, deep-linked blog posts) is a conversion lever in itself.
4. /sms redirect still strips UTM (known): SMS clicks show up as Direct.

---

## 3. AEO / GEO: how we look to answer engines

**In place (credit where due):**
- llms.txt exists and is structured well
- robots.txt allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- Organization + LocalBusiness + WebSite JSON-LD on homepage
- Strong third-party graph: TripAdvisor, Yelp, Viator, Visit Houston, Giftory, Fever
- AI referrals already arriving (~22 sessions/90d)

**Broken or missing:**

| Item | Problem | Fix |
|------|---------|-----|
| LocalBusiness phone | `++8329740365` invalid | `+1-832-974-0365` |
| LocalBusiness rating | No aggregateRating, so AI can't say "rated 4.9" | Add real Yelp/FB/TripAdvisor numbers |
| openingHours | Empty array | Fill or remove |
| sameAs | Missing | FB, IG, Yelp, TripAdvisor URLs |
| Brand in schema | Still "Houston Pedal Barge", kayak logo | name "Houston Party Barge", alternateName "Houston Pedal Barge", correct logo |
| Money page schema | BreadcrumbList only | Product + Offer ($55/$800) + AggregateRating (in Paste-Ready file) |
| FAQPage | None sitewide, and we have the FAQ database ranked by email volume | Top 6 Q&As on money page (in Paste-Ready file) |
| llms.txt framing | Leads with "pedal-powered" | Rewrite first line to BYOB party boat framing; add price, capacity, duration facts |
| About page | ~150 words, no founding year, no numbers | AI can't cite what we never state |
| Reviews page | A redirect, not content | Real reviews on-page with schema |
| Freshness | Newest blog post Nov 2023 (one has slug /304/, untitled) | AI engines weight recency heavily |

The competitive AEO reality: for "best party boat Clear Lake" AI engines cite us alongside [Gulf Coast Party Boats](https://gulfcoastpartyboats.com/) and [Houston Party Boats](https://houstonpartyboats.com/); for Seabrook bachelorette queries they cite Gulf Coast and skip us entirely. ([South Shore Boat Rental](https://www.southshoreboatrentallc.com/) owns the true "rental" intent with self-drive pontoons.)

---

## 4. Content plan: what to blog (demand-backed, visitors + locals)

The 50-post calendar stays shelved. One post a week, in this order, each one deep-linking to the money page with descriptive anchors:

| # | Post | Target queries (real GSC demand) | Audience |
|---|------|----------------------------------|----------|
| 1 | **Boat Rides in Houston: 7 Ways to Get on the Water (2026)** | boat rides houston cluster, ~2,400 imp | Visitors |
| 2 | **The Houston Bachelorette Party Boat Guide** | bachelorette houston, bachelorette party ideas near me | Both |
| 3 | **Things to Do in Kemah Beyond the Boardwalk** | kemah boat ride cluster ~725 imp, kemah boardwalk boat rides | Visitors |
| 4 | **Paddle Boat vs. Party Barge: What You're Actually Booking** | paddle boat houston 1,192 imp, pedal boat houston | Locals |
| 5 | **Sunset & Dinner Cruises on Clear Lake** | dinner cruise houston ~190 imp at 7% CTR, sunset cruise houston | Both |
| 6 | **Party Boat Rental in Houston: Options & Prices Compared** | boat rental houston cluster ~900 imp (honest comparison incl. South Shore; captures rental intent we currently waste) | Locals |
| 7 | **Corporate Team Building on the Water in Houston** | supports the 9,635-impression corporate page | Locals |
| 8 | Seasonal: July 4 fireworks cruise post (publish by June 18) | 4th of july boat fireworks | Both |

One coordination flag: the booze cruise cluster (~780 impressions) overlaps the separate Houston Booze Cruise brand. Decide which site owns "houston booze cruise" before either chases it, or they'll cannibalize each other.

Cleanup while in there: retitle or 301 the /304/ orphan post, update or noindex the 2023 "trends in 2024" post, and stop letting thin category archives (e.g. /category/houston-party-boats/, 298 imp at pos 12.6) be the thing Google ranks; the new pillar posts replace them.

---

## 5. Prioritized action plan

### This week (everything is already written in Paste-Ready Assets)
1. **Wire conversions in GA4** (~1-2 hrs): enable FareHarbor's GA4 integration in the FH dashboard so purchase events flow; until then add a `book_now_click` event on FareHarbor links and mark it a key event. Nothing else can be measured without this.
2. **Paste the 4 title/meta rewrites** (~1 hr). Fixes the 39k-impression CTR bleed. Fix "Seakbrook."
3. **Fix the homepage schema bugs** (~30 min): phone, rating, sameAs, hours, name/alternateName/logo.
4. **Add Product + FAQPage schema and the 6-question FAQ block to the money page** (~1.5 hrs). Validate live with JSON.parse after saving (CMS accepts broken JSON silently).
5. **Push the July 4 page** (~1 hr): retitle for "4th of july fireworks cruise houston / kemah", link from homepage hero, GBP post.

### This month
6. llms.txt rewrite to party-barge framing + hard facts (price, capacity, duration, address).
7. About page rebuild: founding year, guest counts, captain story, photos. It has 9,173 impressions waiting.
8. Reviews page: real review excerpts on-page.
9. Start the blog cadence above, posts 1-3.
10. Add UTM to /sms redirect.

### This quarter
11. Posts 4-8 + internal-link pass (every post → money page, money page → corporate/fireworks).
12. Settle booze-cruise brand ownership with Houston Booze Cruise.
13. Visit Houston / Visit League City / Visit Seabrook listing refresh (they already refer quality traffic).
14. Re-audit 30 days after items 1-5 ship: expect CTR on the four bleeding pages to move toward 2-4%, FAQ rich results to appear, and (finally) booking attribution in GA4.

### KPI baseline (for the 30-day check)
- Organic clicks: ~1,810/90d
- Money-page CTR: 0.44%
- AI referral sessions: ~22/90d
- GA4 conversions tracked: 0 (the number that matters most)
