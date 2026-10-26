*Staged 2026-10-15 by David's Claude (LSKT funnel session). STAGED ONLY. Nothing created in Meta. Board card c15, pick = both, status = approved, surface = Meta A/B from March 2027.*

# Card 15: Bats-first vs beginners-first (Meta A/B, March 2027)

## Why this test

- Bats are named in 31% of Austin reviews (74 of 242 with text). Visitors are 12% of reviews, locals under 1%.
- 22% of LSKT shopper chats open with "what is the tour / is it for beginners." 48% of first questions are price or what's included.
- Paid social Sep 28 to Oct 7 2026: $254, 319 link clicks, 1 attributed purchase. Clicks were fine (5.4% CTR on the Breakout Clip). The booking never got credited because FareHarbor's purchase events reach Meta without fbc/fbp or hashed email. So this test is read on CTR and Book taps, not on Meta purchases.

## The two arms

| | **A. Bats first** | **B. Beginners first** |
|:-|:-|:-|
| Hook (primary text, line 1) | 1.5 million bats leave the Congress Avenue Bridge at dusk. You're on the water underneath them. | Never kayaked? You won't be the only one on the water tonight. |
| Proof line (real review) | "The bats were amazing, a completely unique, must-do experience!" | "I highly recommend this guided tour for beginners." |
| Body | Sunset Bat Bridge Kayak Tour. 2 hours, guide and all gear included, $50 a person, ages 5 and up. Bats fly March through early November, biggest flights June to August. | Calm flat water on Lady Bird Lake. Sit-on-top kayaks that are hard to flip, life vest on before you launch, a guide an arm's length away the whole time. $50 a person, 2 hours. |
| Headline | The Bats, From A Kayak | Never Kayaked? Neither Had They. |
| Creative | Bat emergence at dusk from water level, kayaks in frame | Nervous paddler at the dock, then laughing on the water in golden light |
| Landing | /kayak/sunset-bat-bridge-kayak-tour/ with `?ref=meta-c15-bats` | Same page with `?ref=meta-c15-beginners` (or the quiz when it is live) |
| Season guardrail | Only while the bat tour is open (March 1 to October 31) | Runs year-round; the rest-of-year control |

Both arms: same ad set targeting, same budget, same placements, same landing page. Only the hook, proof line, body and creative change. Prices and dates re-verified against the live site in February 2027 before anything is built (bat tour price was $50 on 2026-10-15; the Paddle Board Bat Tour page already contradicts itself at $50 vs $59).

## Audience and settings (from the ad set that ran in 2025 at 4.1x ROAS)

- Account act_638850950128825 ("Lone Star Kayak Tours/Austin", shared with BBK and HPB). Page: Lone Star Kayak Tours (1165400366832095). Instagram: @austinkayaktours.
- Geo: Austin +15 mi, home and recent. Age 25 to 55. Interests: Outdoor recreation, Kayaking, Paddleboarding, Camping, Travel, TripAdvisor, Viator, Expedia, Airbnb, Booking.com, Austin Kayak. Exclude "30 Day Purchases" (120229818447250655).
- Objective: Traffic (landing page views) or Engagement, not Sales, until FareHarbor advanced matching is fixed. Purchase-optimized sets have nothing to learn from while attribution is broken.
- Budget: $10/day per arm, 21 days, Meta native A/B test with 50/50 split. Carve out of existing Austin spend rather than add on top (my pick).

## How it is read

| Metric | Source | Why |
|:-|:-|:-|
| CTR, cost per landing page view | Meta | Primary, enough volume in 21 days at $10/day each (about 2,000 to 3,000 clicks total at 2025 CPCs of about $0.28) |
| Book taps and bookings by arm | FareHarbor Advanced Bookings report, Online Booking Reference contains `meta-c15-bats` or `meta-c15-beginners` | Pixel attribution is broken; the ref tag survives into FareHarbor on most online bookings (38% blank at LSKT, so a floor) |
| Chats opening with "is it for beginners" | OpenCX LSKT workspace, tagged | Secondary: does arm B cut the question? |

Decision rule: pick the arm with the lower cost per Book tap after 21 days if the gap is 25% or more. Smaller gap: run A in bat season, B the rest of the year (the recommendation already on the board).

## Calendar

| Date | Step | Who |
|:-|:-|:-|
| 2027-02-15 | Re-verify prices, dates, age minimums, meeting address on the live site; rebuild LSKT lookalikes (all showed "too small" on 2026-10-15) | Claude |
| 2027-02-20 | Confirm FareHarbor Meta pixel fix (advanced matching, fbc/fbp, dedupe). If still broken, run as Traffic objective | Claude checks, David or Connor asks FareHarbor |
| 2027-02-25 | Build both ads PAUSED, show David the exact spec | Claude |
| 2027-03-01 | David flips on (bat tour opens) | David |
| 2027-03-22 | 21-day read, row on the board | Claude |

## Needed from David before Feb 2027

1. Reuse the existing bat creative (Breakout Clip, Bat Bridge Sunset Tour v2) or shoot new? Arm B has no first-timer footage in the account today.
2. OK to use the first-timer proof line from the Google review as written?
3. Budget: carve $20/day out of the current Austin Google Ads spend, or new money on top?
