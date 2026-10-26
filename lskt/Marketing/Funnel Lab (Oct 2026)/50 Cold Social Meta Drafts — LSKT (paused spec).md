*Drafted 2026-10-15 by David's Claude (LSKT funnel session). **BUILT PAUSED in Meta on 2026-10-16** after David picked both on card c02 (Skyline landing, $10/day total carve-out). Nothing is on. See the BUILT section first; the spec below it is what was planned.*


## BUILT 2026-10-16 (verified against the Graph API right after creation, zero active campaigns in the account)

| Object | Name | Status | ID |
|:-|:-|:-|:-|
| Campaign A | TEST c02-A LSKT Cold Social Lead Step (OUTCOME_LEADS, $5.00/day, lowest cost) | PAUSED | 120254403874180655 |
| Campaign B | TEST c02-B LSKT Cold Social Watch then Book (OUTCOME_ENGAGEMENT, $4.00/day) | PAUSED | 120254403874400655 |
| Ad set B1 | c02-B1 Austin cold, ThruPlay (destination on-video) | PAUSED | 120254403939400655 |
| Ad B1-1 | Breakout Clip (bat video, pull Oct 31), creative 1560756072407520 | PAUSED | 120254403940080655 |
| Ad B1-2 | Kayaks video (skyline, year-round), "Never Kayaked? Neither Had They.", creative 1723270305401915 | PAUSED | 120254403940520655 |
| Campaign B2 | TEST c02-B2 LSKT Warm Viewers Book (OUTCOME_TRAFFIC, $1.00/day) | PAUSED | 120254403872860655 |
| Ad set B2 | c02-B2 Warm viewers, Traffic (landing page views, Lone Star Website Visitors 60d) | PAUSED | 120254403899070655 |
| Ad B2 | Book the skyline paddle (image, Book Travel CTA), creative 1474021444632777 | PAUSED, in Meta review | 120254403917840655 |

Budgets sit at campaign level (the MCP needs one there), so Meta runs them as campaign budgets: A $5, B $4, B2 $1, $10/day total when switched on. All three campaigns were created with Meta's default bid cap and then set to lowest cost without cap.

Targeting as built: Austin +15 mi (home and recent), ages 25 to 55, Facebook and Instagram, Advantage audience OFF. Cold interests: Outdoor recreation, Kayaking, Paddleboarding, Camping, Travel, TripAdvisor, Viator, Expedia, Airbnb, Booking.com. Meta retired the "Austin Kayak" interest from the 2025 set, so it is gone. Exclusion on every set: "30 Day Purchases" (120229818447250655). B2 includes "Lone Star Website Visitors - 60Days" (120230785191000655).

Landing URLs: cold ads `/kayak/austin-skyline-tour/?ref=meta-c02b-cold`, warm ad `?ref=meta-c02b-warm`. Read bookings by those refs in the FareHarbor Advanced Bookings report.

**Two blockers before David can flip anything on:**

1. **Arm A has no ad set or ad yet.** Meta refused the lead ad set: neither the Lone Star Kayak Tours page nor the Austin Kayak Tours page has accepted Meta's Lead Ads Terms of Service (`leadgen_tos_accepted` is false on both). A page admin accepts them once at business.facebook.com (Page settings, or the first time a lead form is created in Ads Manager). After that: create the ad set per the spec below with the page as promoted object, build the Instant Form "Who's paddling? (LSKT)" in Ads Manager (privacy URL is https://lonestarkayaktours.com/privacy-statement-us/, the old /privacy-policy/ redirects there), and add the one ad.
2. **B2's video-viewer audiences do not exist yet.** The ad set runs on the 60-day website visitors only. In Ads Manager, add two engagement audiences (50% and 95% viewers of the B1 videos, 30 days) to ad set 120254403899070655 before or just after B1 starts. Nothing to view until B1 runs, so this is not urgent.

Smaller notes: the ad account has no access to the @austinkayaktours Instagram account (17841403859908622), so all ads run from the Lone Star Kayak Tours page with page-backed Instagram placement. Assigning that IG account to act_638850950128825 in Business Settings fixes it. The B1 ad set was created once without a promoted object and once with destination on-video; the empty first one was deleted.

# Card 2 for LSKT: where cold social traffic lands (Meta, both arms, PAUSED)

## What we know going in (verified 2026-10-15)

| Fact | Source |
|:-|:-|
| Account act_638850950128825 "Lone Star Kayak Tours/Austin" is shared with Buffalo Bayou and Houston Booze Cruise. All 77 campaigns paused. Last spend $11.14 on Oct 7. | Meta API, 2026-10-15 |
| Sep 28 to Oct 7: $254 spent, 909 clicks, 319 link clicks, 269 landing page views, 1 attributed purchase ($17.32). Breakout Clip ad hit 5.4% CTR. | Meta insights last_30d |
| Why 1 purchase: FareHarbor sends Purchase to Meta with no fbc/fbp and no hashed email or phone. Pixel has never fired ViewContent, AddToCart or InitiateCheckout. Meta cannot connect a booking to an ad click. Not fixed as of 2026-10-15. | `Austin Kayak Tours — Ad Campaigns.md`, 10/09 walkthrough and 10/15 audit |
| GA4 agrees: paid social 373 sessions, 31% engagement, 0 purchases (last 30 days to 10/13). PMax and Search convert at 4 to 6%. | 02 Funnel Baseline |
| Bat tour closes Oct 31. Season reopens March 1. | Live site |
| All LSKT lookalikes show "too small." | 10/15 audit |

**What this means for the test:** neither arm can be optimized for Purchase and read on Meta purchases. Arm A optimizes for on-platform Leads (Meta counts those itself). Arm B optimizes for ThruPlay, then retargets viewers with Traffic ads. Bookings for both arms are read in FareHarbor by `?ref=` tag, the same way the npb-winback and austinwelcomecenter tags already show up in the Advanced Bookings report.

**Timing:** 16 days of bat season are left. My pick is to build both arms paused now, but point them at the Austin City Skyline Tour (year-round, $50) so the test can run its full 21 days in November without a season cliff. Bat creative goes back in March 2027 (see file 51). If David wants bats now, swap the landing URL and creative; everything else stays.

## Shared settings (both arms)

| Setting | Value |
|:-|:-|
| Ad account | act_638850950128825 |
| Page | Lone Star Kayak Tours, 1165400366832095 |
| Instagram | @austinkayaktours (17841403859908622) |
| Pixel | LSKT Pixel 1559188957448084 (for audiences only, not optimization) |
| Geo | Austin, TX +15 mi, home and recent (same as the 2025 set that did 4.1x) |
| Age | 25 to 55 |
| Interests | Outdoor recreation, Kayaking, Paddleboarding, Camping, Travel, TripAdvisor, Viator, Expedia, Airbnb, Booking.com, Austin Kayak (the 2025 list, ids in the account) |
| Exclude | custom audience "30 Day Purchases" 120229818447250655 |
| Placements | Advantage+ placements, Reels and Stories allowed |
| Budget | $5/day per arm ($10/day total), 21 days, Meta native A/B test, 50/50. File 40 suggested $10/day for the card; the whole account spent $254 in its last 10 live days, so $10/day total is the carve-out level. David sets the number. |
| Status on creation | PAUSED at campaign, ad set and ad level |
| Attribution | 7-day click, 1-day view (for what Meta can see) |

## Arm A: cold traffic goes to a lead step (Meta Instant Form)

Campaign `[TEST c02-A] LSKT Cold Social Lead Step` , objective OUTCOME_LEADS, PAUSED.

Ad set `c02-A Austin cold, Lead form`, optimization LEAD_GENERATION (Instant Form), billing impressions, destination_type ON_AD (Instant Form), promoted_object page 1165400366832095, PAUSED.

Instant Form `Who's paddling? (LSKT)`:
- Intro: "30 seconds. We'll send the right paddle and the price, nothing else."
- Question 1 (multiple choice): **Who's paddling?** Just me / Me and a date / Friends / Family with kids
- Question 2 (multiple choice): **Ever kayaked before?** Never / A few times / Plenty
- Fields: email (required), phone (optional)
- Privacy policy URL: https://lonestarkayaktours.com/privacy-policy/ [VERIFY the page exists before creating the form]
- Thank-you screen: "Done. Here's the paddle that fits: Austin City Skyline Tour, 2 hours, $50 a person, guide and gear included. Never kayaked? Lady Bird Lake is flat water and the guide covers the basics before you launch." Button: **See open dates** to https://lonestarkayaktours.com/kayak/austin-skyline-tour/?ref=meta-c02a-lead
- Form type: "More volume" (fewer taps). Switch to "Higher intent" if the first week is spam.

Ad `c02-A Who's paddling` (one ad, two creatives rotated by Meta):
- Primary text: "Not sure which Austin paddle is yours? Two taps and we'll tell you. Skyline at golden hour or the bats at dusk, both 2 hours, $50 a person, guide and all gear included. Never kayaked? Most of our guests hadn't either."
- Headline: Which Austin Paddle Is Yours?
- Description: 2 taps, then the tour and the price
- CTA: Get Offer? No. **Learn More** (no discount exists; never imply one).
- Creative 1: existing "Video Ad - Kayaks" (creative 1252666892882407), skyline footage, works year-round.
- Creative 2: existing "Bat Bridge Sunset Tour v2" image (creative 1405243090758883) only while the bat tour is open; pull Oct 31.

Lead handling (nothing to build until leads exist): Meta leads download or the Leads Center. Each lead gets the LSKT quiz nurture (file 30) once the engine is live for lskt; until then, Connor or the dock team texts the Skyline link within a day. Leads are also the seed for the retargeting audience "LSKT c02 leads" for booking ads at $2 to $3/day.

What Arm A measures: cost per lead (Meta), leads per 100 link clicks, then bookings with ref `meta-c02a-lead` in FareHarbor over 30 days.

## Arm B: cold traffic watches, warm traffic books (ThruPlay plus retargeting)

Campaign `[TEST c02-B] LSKT Cold Social Watch then Book`, objective OUTCOME_ENGAGEMENT (video views), PAUSED. Two ad sets.

Ad set B1 `c02-B1 Austin cold, ThruPlay`, optimization THRUPLAY, $4/day of the arm's $5, same targeting as above, PAUSED.
- Ad `c02-B1 Breakout Clip`: reuse the Breakout Clip video (creative 1749047879383139, the 5.4% CTR ad) through Oct 31, then the Video Ad - Kayaks (1252666892882407). No link, no CTA pressure. Primary text: "Two hours on Lady Bird Lake. The skyline from the water, turtles and herons along the bank, a guide the whole way. $50 a person, gear included." Headline: Austin, From The Water.
- Optional second ad for a real test of hooks: same video, primary text swapped for the beginner line "Never kayaked? You won't be the only one on the water tonight."

Ad set B2 `c02-B2 Warm viewers, Traffic`, objective inside the same campaign is not allowed for a different outcome, so B2 lives as a second campaign `[TEST c02-B2] LSKT Warm Viewers Book`, objective OUTCOME_TRAFFIC, optimization LANDING_PAGE_VIEWS, $1/day to start (rises as the viewer audiences fill), PAUSED.
- Audiences (create first, they are empty until B1 runs): video viewers 50% of B1 videos, 30 days; video viewers 95%, 30 days; plus the existing "Lone Star Website Visitors - 60Days" 120230785191000655. Exclude "30 Day Purchases".
- Ad `c02-B2 Book the skyline paddle`: single image Bat Bridge Sunset Tour v2 through Oct 31, then a skyline still. Primary text: "You watched it. Here's the booking page. Austin City Skyline Tour, 2 hours, $50 a person. 10 a.m., 1 p.m. and 4 p.m. most days." Headline: See Open Dates. CTA: Book Now. URL https://lonestarkayaktours.com/kayak/austin-skyline-tour/?ref=meta-c02b-warm

What Arm B measures: cost per ThruPlay and 50%/95% viewer counts (Meta), cost per landing page view in B2, then bookings with ref `meta-c02b-warm` in FareHarbor over 30 days.

## Reading the test (day 21)

| | Arm A | Arm B |
|:-|:-|:-|
| Cheap signal | Cost per lead | Cost per 95% view, cost per B2 landing page view |
| Money signal | FareHarbor bookings tagged `meta-c02a-lead` per $100 | Bookings tagged `meta-c02b-warm` per $100 |
| Also watch | Lead quality: how many reply to the text | Frequency on B2 (cap at 3 a week) |

Decision rule: whichever arm books more per $100 after 21 days wins the cold budget for 2027. If both book zero, the problem is not the landing but the account's match data, and the FareHarbor pixel fix comes first.

## Exactly what gets created when David says go (MCP calls, in order)

1. `fb_create_campaign` x3: c02-A (OUTCOME_LEADS), c02-B (OUTCOME_ENGAGEMENT), c02-B2 (OUTCOME_TRAFFIC), all status PAUSED, no CBO (budgets at ad set level).
2. `fb_create_adset` x3 with the targeting above, daily budgets 500 / 400 / 100 cents, status PAUSED. The Instant Form itself has to be made in Ads Manager (the MCP has no lead-form call), so Arm A's ad set is created first and the form attached in the UI.
3. `fb_create_ad_creative` x3 reusing existing creative ids where possible (1749047879383139, 1252666892882407, 1405243090758883) with the new primary text, headlines and tagged URLs.
4. `fb_create_ad` x4, all PAUSED.
5. In Ads Manager: wrap A and B in one A/B test (the MCP cannot create a split test), create the two video-viewer audiences, attach the Instant Form.
6. Nothing turns on. David flips the two campaigns to ACTIVE himself, or tells Claude to in that turn.

## Needed from David

1. Pick on card c02 (A, B, or both). The build above assumes both.
2. Budget: $10/day total as a carve-out of Austin spend, or the $10/day per arm from file 40 as new money?
3. Skyline tour as the landing for a November run, or bats now and accept a 16-day test?
4. OK to reuse the three existing creatives? Nothing new has to be shot.
5. Who handles Instant Form leads day to day until the lskt nurture is live (Connor, the dock team)?
6. Should the FareHarbor pixel fix (advanced matching, fbc/fbp) be asked of FareHarbor before this test runs? It is the single biggest reason Meta shows 0 purchases.
