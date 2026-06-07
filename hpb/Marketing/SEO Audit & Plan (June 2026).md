# Houston Pedal Barge — SEO Audit & Plan (June 2026)

**Date:** 2026-06-07
**Data source:** Google Search Console, last 90 days (Mar 9 - Jun 7), domain property `houstonpedalbarge.com`
**Prior plan:** `SEO Action Plan & Content Calendar.md` (May 9) and `AI SEO Audit & Action Plan (May 2026).md`

---

## The headline

The May plan was good. It just didn't ship. A month later, the one fix that mattered most (schema) still isn't live, the brand is still split between "Party Barge" and "Pedal Barge," and the meta description has a typo in it. The only Phase 1 item that got done is the canonical tag, which now correctly points to the non-www version sitewide.

So this isn't a "we need more analysis" problem. We have plenty of analysis. We have a 50-post content calendar nobody's started. What we need is to actually do the five things that move the needle, and stop pretending the rest matters until those are done.

The math that should bother you: four pages (the tour page, corporate, about, contact) pulled about **37,000 impressions in 90 days and converted them into roughly 52 clicks.** They rank fine, positions 6 to 8. Nobody clicks because the title and snippet Google shows are generic. That's not a ranking problem, it's a snippet problem, and it's fixable in an afternoon.

---

## What the data says

### Branded terms: we own them
| Query | Position | Clicks | Impressions | CTR |
|-------|---------:|-------:|------------:|----:|
| houston pedal barge | 2.6 | 129 | 404 | 31.9% |
| houston party barge | 1.0 | 67 | 422 | 15.9% |

Brand is locked. No work needed here except keeping it.

### Striking distance: positions 5-10 with real demand (the near-term money)
| Query | Position | Impressions | CTR | Note |
|-------|---------:|------------:|----:|------|
| houston party boats | 7.3 | 872 | 2.4% | Biggest non-brand prize. We're just below the top cluster. |
| paddle boat houston | 8.6 | 725 | 1.0% | High volume but mixed intent (paddle boat ≠ pedal barge). Worth a sentence that disambiguates. |
| boat rides houston | 6.6 | 720 | 2.8% | Generic but high intent. |
| kemah boat ride | 6.4 | 524 | 1.1% | Geographic, very fixable. Kemah is our backyard. |
| party boat houston | 3.8 | 440 | 12.7% | Already performing. Protect it. |
| party boat kemah | 5.4 | 351 | 8.3% | Performing. |

### Page 2 hostages: positions 11-20, one good push from page 1
| Query | Position | Impressions | CTR |
|-------|---------:|------------:|----:|
| party boat | 14.4 | 515 | 1.2% |
| party barge | 15.4 | 511 | 0.2% |
| boat rental houston | 13.1 | 195 | 0% |
| party boats | 12.6 | 169 | 0.6% |
| party boat rentals | 12.6 | 151 | 2.0% |

### The CTR bleed (this is the real story)
| Page | Impressions | Clicks | CTR | Avg Position |
|------|------------:|-------:|----:|-------------:|
| /houston-party-barge-cruise/ (the money page) | 10,828 | 43 | 0.40% | 8.0 |
| /corporate-group-event/ | 9,147 | 6 | 0.07% | 8.5 |
| /about/ | 8,782 | 2 | 0.02% | 6.2 |
| /contact/ | 8,356 | 1 | 0.01% | 6.1 |

These pages rank. They just don't get clicked. A page at position 6-8 should pull 3-6% CTR. We're at a tenth of that. The title tags and meta descriptions are doing nothing.

### www vs non-www
GSC shows both versions ranking as separate URLs: www at position 4.5 / 5.8% CTR, non-www at position 9.6 / 1.9% CTR. The canonical now points everything to non-www, which is correct and will consolidate over time. Nothing more to do here except let it settle. Note for later: the www version was actually the stronger performer, so watch that the consolidation doesn't drop us. If positions slide over the next 30 days, revisit.

---

## On-page check (live, June 7)

| Element | Current state | Problem |
|---------|---------------|---------|
| Homepage title | "Clear Lake Party Boats \| Houston Party Barge" | "Party Barge" not "Pedal Barge." No price, no rating hook. |
| Homepage meta desc | "Houston Party Barge offers private and public party boat tours and booze cruise boat bar rentals. Book now & see the beauty of Clear lake in Kemah & Seakbrook." | Typo "Seakbrook." Lowercase "Clear lake." Still "Party Barge." No CTA urgency. |
| Homepage H1 | "Houston Party Barge" + a second H1 (tagline) | Two H1s. Brand inconsistent. Should be one. |
| Money page title | "Houston Party Barge Cruise \| Houston Pedal Barge" | Generic. No price ($55), no "BYOB," no Clear Lake. |
| JSON-LD schema | **Zero on every page checked** | Single biggest miss, same as it was in May. No LocalBusiness, no Product, no FAQPage, no AggregateRating. |
| FAQ blocks | None | We have the questions ranked by email volume and still aren't using them. |
| Canonical | Present, non-www | Fixed. The one win. |
| Raw HTML title renders as "Pause" | Page title only loads via JS | Minor risk: title is client-side rendered. Google renders JS so likely fine, but worth confirming the rendered title in GSC's URL inspection. |

---

## The plan: five things, in order, then stop

Forget the 50-post calendar for now. It's Phase 3 work and we haven't done Phase 1. Here's the whole list. If we only do these five, organic clicks go up.

### 1. Rewrite the title + meta on the four bleeding pages (THIS WEEK, ~2 hrs)
This is the highest-ROI hour of work available. These pages already rank. Better snippets = more clicks with zero new content and zero new links.

**Homepage**
- Title: `Houston Pedal Barge | Clear Lake Party Boat Cruise in Seabrook, TX`
- Meta: `BYOB party boat cruise on Clear Lake near the Kemah Boardwalk. Public tickets from $55, private charters up to 26 guests. Book your Seabrook, TX cruise online.`

**Money page (/houston-party-barge-cruise/)**
- Title: `Party Boat Cruise on Clear Lake | BYOB, from $55 | Houston Pedal Barge`
- Meta: `Cruise Clear Lake on a 26-passenger pedal barge. BYOB, ages 8+, 1 hour 45 minutes, captained. Public tickets $55 or private charter $800. Book online now.`

**Corporate (/corporate-group-event/)**
- Title: `Corporate & Group Boat Events in Houston | Up to 26 Guests | Pedal Barge`
- Meta: `Team building, holiday parties, and client outings on Clear Lake. Private charters up to 26, BYOB, captained. Get a quote for your Houston group event.`

**About (/about/)**
- Title: `About Houston Pedal Barge | Clear Lake's BYOB Party Boat`
- Meta: `The story behind Houston's pedal-powered party boat on Clear Lake in Seabrook. Captained cruises, BYOB, up to 26 guests since [founding year].`

Keep all meta under 160 characters, plain ASCII, no em dashes, no curly quotes (per CLAUDE.md). Fix the "Seakbrook" typo wherever it lives.

### 2. Add JSON-LD schema to the homepage, money page, and contact page (THIS WEEK, ~2 hrs)
Same ask as May. Paste raw JSON into the ACF Schema Markup field, no `<script>` wrapper, no escaped inner quotes (`\"` breaks it on render per CLAUDE.md). Validate live after saving.

- Homepage: `LocalBusiness` (name, address 2515 E NASA Pkwy Seabrook TX, phone, geo, priceRange, openingHours, sameAs to FB/IG/Yelp/TripAdvisor) + `AggregateRating` from real Yelp/FB/TripAdvisor review counts.
- Money page: `Product` with `offers` (price 55, private 800), `aggregateRating`, image, description.
- Contact: `LocalBusiness` with NAP.

This is the thing that makes AI Overviews and rich results possible. Everything in the AI audit depends on it. It has now sat undone for a month.

### 3. Settle the brand: Party Barge wins, drop "pedal" (THIS WEEK, 1 decision + 1 hr)
**Decision made (June 7):** lead with "Houston Party Barge" and remove "pedal" from all customer-facing copy. Nobody wants to pedal, and "do I have to pedal?" is a top objection. We already rank #1 for "houston party barge" (67 clicks, 422 impressions), so this loses nothing. The H1, title, and brand voice consolidate to Party Barge / party boat / BYOB booze cruise. Keep the "houston pedal barge" brand-term ranking (129 clicks/90d) quietly via the unchanged domain + a schema `alternateName: "Houston Pedal Barge"`. Fix the duplicate H1 on the homepage while you're in there (one H1 per page).

### 4. Ship one FAQ block with FAQPage schema on the money page (THIS WEEK, ~1.5 hrs)
We already ranked the top customer questions by email volume in the May AI audit. Take the top 6, write 40-60 word answers (most of these answers already exist in our email replies and OpenCX), drop them on /houston-party-barge-cruise/ with FAQPage schema. Start here:
1. How much does it cost? ($55 public / $800 private up to 26)
2. Do I have to pedal? (No, captain + motor handle it)
3. Can we bring our own drinks/food? (Yes, BYOB and BYO food, cans not glass)
4. Where do we meet? (2515 E NASA Pkwy, Seabrook)
5. Age/group limits? (Ages 8+, up to 26 guests)
6. How long is the cruise? (1 hour 45 minutes)

### 5. Then, and only then, start the content calendar at 1 post/week (ONGOING)
The 50-post plan is fine. The cadence in it is fantasy. We've published zero in the month since it was written. Realistic target given Connor's bandwidth: **one post per week, picked from the bachelorette and FAQ clusters first** (highest commercial intent, easiest to write). Use the seo-blog-writer skill. Two posts to start, both targeting striking-distance demand we already see:
- "The Ultimate Houston Bachelorette Party Boat Guide" (captures the bachelorette intent we lose to Gulf Coast)
- "How a Pedal Barge Actually Works (And Why You Don't Have to Pedal)" (kills the top objection, targets "paddle boat houston" confusion)

---

## What I'd ignore for now
- Wikipedia mentions, Reddit seeding, the comparison pages, the backlink campaign. All real, all Phase 3. None of it matters if the money page still converts 10,000 impressions into 43 clicks.
- The full 50-post calendar as a batch. One a week or it won't happen.

## How we'll know it worked (check in 30 days)
- CTR on the four bleeding pages moves from ~0.1% toward 2-4%. That alone roughly 10x's their clicks.
- Rich results / FAQ appear in SERP for the money page (check GSC search appearance).
- "houston party boats" and "boat rides houston" move from position 6-8 into the top 5.
- Total organic clicks up. Baseline this quarter: roughly 1,800 clicks/90 days across the property.

---

*Bottom line: we don't have an SEO knowledge problem, we have an execution problem. Five fixes, most of them an afternoon each, all flagged a month ago. Ship items 1-4 this week before writing a single blog post.*
