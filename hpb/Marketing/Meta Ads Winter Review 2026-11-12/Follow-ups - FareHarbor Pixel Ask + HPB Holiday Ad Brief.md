# Follow-ups from the Meta winter review (2026-11-12). Drafts only, nothing sent or launched.

## 1. FareHarbor header-script / pixel request (DRAFT, not sent)

To: FareHarbor support (via Connor or David, whoever owns the account contact). Covers HPB, Buffalo Bayou Kayak and Lone Star/Austin.

> Hi FareHarbor team. We run paid social for houstonpedalbarge.com, buffalobayoukayak.com and austinkayaktours.com and can't see which bookings come from Meta. Could you help with two things?
> 1. Enable a custom header script slot (or your Meta pixel / Conversions API field) on each of our three FareHarbor accounts so we can install our own Meta pixel on the booking flow.
> 2. Confirm which booking-flow events we can fire: ViewContent (item page), InitiateCheckout (booking step reached) and Purchase, and whether Purchase can carry order value, plus fbc/fbp or hashed email.
> Also: is there a `ref` / UTM pass-through in the booking report so we can match bookings to ad clicks? Thanks!

Needs: who sends it (Connor / David / Michael) and which three FareHarbor shortnames. Also ask David before touching the shared pixel 381452300055179 (it is shared across brands).

## 2. HPB holiday-party Meta ad: brief (NOT built; needs 3 answers first)

Plan: $15/day Nov 12 – Dec 20, then $5/day retargeting only. One Sales campaign, one ad set, Houston geo (20–25 mi incl. Kemah/Clear Lake), ages 21–44, 3–4 ads.

Blockers to clear before building:
1. **Page:** HPB ads currently run under the Buffalo Bayou Kayak Tours Page. Decide whether to launch under that Page or the HPB Page.
2. **Pixel/optimization:** no working HPB purchase event exists. Until the pixel ask above lands, optimize to the deepest event that fires (likely landing page view / Initiate Checkout on the BBK pixel), and judge results by FareHarbor `ref=` tags.
3. **Facts to confirm:** Christmas cruise dates and price ($59 on the site), fireworks date, 72-hour cancellation, $800 / up to 26.

Tracking: every ad URL gets `?ref=meta-hpb-<ad>` (plus `utm_source=facebook&utm_medium=paid&utm_campaign=holiday_party&utm_content=<ad>`).

Draft ad copy (no "pedal", no alcohol words per the Google rule; check against your NOLA note, which keeps alcohol terms for NOLA only):
- **Office party:** "Skip the restaurant. Take the whole team out on a private party barge this December. A captain drives, you bring the playlist. $800 for the whole boat, up to 26." Headline: "Holiday party on the water."
- **Christmas cruise:** "Lights, music and your crew on the bayou. Christmas cruises from $59 a seat. Pick your night." Headline: "Christmas Cruise, Houston."
- **Friends' night out:** "Group chat can't pick a plan? Pick the boat. Private barge for up to 26, $800 total. Split it and it's about $40 a head." Headline: "$800 for the whole barge."
- **Retargeting (from Dec 21):** "Still thinking about that boat night? Dates are filling. Book your crew's cruise." Headline: "Your boat is waiting."

Geo fix: the old HPB ad sets target "Dublin, California, 50 miles". Build the new ad set fresh; don't un-pause those.

## 3. Done in Meta today (2026-11-12, Buffalo Bayou/Houston account 1015419897308486)

| Change | Before | After |
|:-|:-|:-|
| HPB Engagement – Followers Reboost | Active | **Off** |
| Awareness – Sales [Initiate Checkout] – TourPPC | Active | **Off** |
| Bat Bridge Kayak Tour – Traffic daily budget | $20 | **$10** (published) |
| Austin account | all paused since Oct 7 | unchanged (stays off) |

Roll back: toggle the two campaigns back on, set Bat Bridge to $20. Re-check Bat Bridge on ~Nov 26 (14 days of post-change data) and the HPB `ref=` booking gate on Dec 10.
