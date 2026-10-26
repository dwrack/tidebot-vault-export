# Houston Pedal Barge — Meta Ads Audit (2026-10-21)

Source: Ads Manager CSV exports in this folder, lifetime. Read-only; nothing was changed in Meta.

## Accounts
| Account | ID | Notes |
|---|---|---|
| Buffalo Bayou/Houston | 1015419897308486 | 19 campaigns, 44 ads. Houston bat tour, HPB reboosts, pixel-tracked TourPPC sales ads, some NOLA posts. Data starts 2025-06-05. |
| Michael Fischer | 129111023833794 | 273 campaigns with data (397 total), **$91.7k lifetime**. Boosted posts and "Promoting" campaigns for HPB, NOLA and others. |

## What's running now
| Campaign / ad | Account | Spend (lifetime) | Result |
|---|---|---|---|
| Bat Tour VIDEO – The Spectacle (Bats from Kayak) | Buffalo Bayou | $3,063 | 31,482 link clicks, $0.097 each |
| Bat Tour VIDEO – Date Night (Pink Moon Bats) | Buffalo Bayou | $335 | 3,457 clicks, $0.097 each |
| Bat Tour VIDEO – Only in Houston (5 Reasons) | Buffalo Bayou | $101 | 782 clicks, $0.129 each |
| HPB Reboost – Swag Surfin Jun2023 | Buffalo Bayou | $465 | 118,834 post engagements |
| HPB Reboost – Party Started Feb2025 | Buffalo Bayou | $479 | 145,334 post engagements |
| Ongoing website promotion – HoustonPedalBarge.com ($10/day) | Michael Fischer | $1,609 | 13,926 landing page views, $0.116 each ("High performing") |
| Instagram post: "Get on a boat and do whatever ya…" ($15/day) | Michael Fischer | $431 | 7,262 link clicks, $0.059 each |
| Ongoing website promotion – NewOrleansKayakSwampTours.com ($25/day) | Michael Fischer | $4,376 | 13,803 landing page views — NOLA, not HPB; has Ad errors |

## Findings
1. **No purchase tracking on almost all Meta spend.** Of 273 campaigns in the Michael Fischer account, none reports a purchase or revenue value. In the Buffalo Bayou account, only the TourPPC pixel ads report purchases. Meta can't show which spend produced sales; FareHarbor bookings are the source of truth. This is the gap that most limits the audit.
2. **Purchase-optimized campaigns are all OFF.** The "ROAS reporting" view returns no active ad set. Only the TourPPC sales ads ever reported purchases, and none is delivering now.
3. **Best proven purchase ads (all paused):**
   - In-Market – Party Barge: $1,054 spent, 16 purchases, $3,940 value, 3.74x. Best ad on record, now not delivering.
   - RT – General Kayak & SUP Single Image 2: $327, 9 purchases, $936, 2.87x.
   - In-Market – Family Kayaks & SUPs: $1,037, 31 purchases, $1,196, 1.15x (most purchases, thin margin).
   - Weak and should stay off: POV Video 0.81x, General Kayaks & SUPs 0.13x, RT Single Image 1 0.91x.
4. **Biggest live spend is untracked traffic.** The Bat Tour spectacle video has spent $3,063 on clicks with no purchase event attached.
5. **Cheapest boosted posts and promotions for HPB (cost per link click):**
   - houstonboozecruise.com promos: $0.042–0.044.
   - HoustonPedalBarge.com promos ([08/27/2025], [7/28/2026]): $0.047–0.057.
   - Post "You can give us a call at (832) 974-0365…": $0.056 and $0.073, $500 each.
   - Post "Always a good time on the bayou at…": $0.061.
   Cheap clicks, not proven sales.
6. **Messaging campaigns** cost about $3.46–$8.93 per conversation started ("Delta Dream $59/person", "We got bookings going out every day", birthdays/special occasions, holiday party). Worth comparing against how many of those conversations booked.
7. **Cleanup:**
   - 66 campaigns are "not_delivering" and 6 "inactive".
   - The two not-delivering gift card and "Are your Boys/Girls in town" posts have ad set errors.
   - The "HPB | Engagement | Followers Reboost" campaign has Ad errors.
   - "Review and publish (6)" has unpublished drafts waiting.

## Recommended next steps
1. Turn In-Market – Party Barge back on, in a purchase-optimized campaign with the pixel purchase event, at a modest daily budget. Rebuild "RT General Kayak & SUP Single Image 2" as the retargeting ad.
2. Add a purchase event (or at least an Initiate Checkout event) to the Bat Tour campaign so its $3k+ of spend can be judged.
3. Ask FareHarbor which referral/UTM sources produced bookings, then weight Meta budget by real bookings, not clicks.
4. Fix the ad errors and the two post campaigns that can't deliver, or archive them.
5. Pull organic "best posts of all time" from Business Suite or the meta-organic connector once it's back, and boost the top three organic posts as new ads.

## Not covered
- Organic post performance (the meta-organic connector failed to connect).
- Gravity Trails and Lone Star ad accounts.
- FareHarbor booking data for sales attribution.
- The ad-level export for the Michael Fischer account (campaign names there are mostly post-based).
