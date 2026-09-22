# NPB Meta Ads Weekly Readout — Mon Sep 22, 2026

Window: Sep 15-21 (7d), Sep 8-14 (prior week), Aug 23-Sep 21 (30d). Account act_87863118. Source: Meta Marketing API via fb_get_insights.

## Active NPB campaigns

| Campaign | Ad set | Daily budget | Status |
|---|---|---|---|
| NPB \| Purchase \| Retargeting (6976231067696) | RT \| Video Viewers 75% | $20 | Active |
| NPB \| Messenger \| TOF (6978218386896) | Messenger \| Nightlife & Bars | $20 | Active |
| NPB TOF Prospecting (6976231037096) | - | $80 | Paused |
| NPB Creative Testing (6976231069696) | - | $25 | Paused |

Also active in the account but NOT NPB: "New Sales Campaign" (52560373835300) is the NKST "tag a friend to win a swamp tour" boost. $40/day budget, spending under $1/day. Excluded from everything below.

## Retargeting (purchase objective)

| Metric | This week (9/15-21) | Prior week (9/8-14) | 30d |
|---|---|---|---|
| Spend | $140.83 | $135.03 | $592.71 |
| Purchases | 15 | 9 | 34 |
| Revenue | $3,897.95 | $1,255.40 | $7,650.88 |
| ROAS | 27.7x | 9.3x | 12.9x |
| CPA | $9.39 | $15.00 | $17.43 |
| CTR | 9.14% | 7.95% | 8.56% |
| Frequency | 1.77 | - | 2.06 |
| Landing page views | 415 | 371 | 1,806 |

Single ad: "NPB | RT Video | Still Thinking". Has run since late April with no rotation.

## Messenger TOF (engagement objective, no purchase tracking)

| Metric | This week | Prior week | 30d |
|---|---|---|---|
| Spend | $138.41 | $137.91 | $592.89 |
| Conversations started | 56 | 41 | 192 |
| Cost per conversation | $2.47 | $3.36 | $3.09 |
| Reached 5+ messages | 10 | 10 | 32 |
| CTR | 5.22% | 4.95% | 5.13% |
| Frequency | 1.76 | - | 2.35 |
| Blocks | 3 | 0 | 5 |

Per ad this week:

| Ad | Spend | Convos | Cost/convo | CTR |
|---|---|---|---|---|
| Viral Video | $87.96 | 36 | $2.44 | 5.46% |
| Original Party Barge | $50.45 | 20 | $2.52 | 4.82% |

## Blended (NPB only)

- Spend $279.24, 15 tracked purchases, $3,898 revenue, 13.96x blended ROAS, $18.62 blended CPA.
- Messenger conversations are not attributed to purchases in Meta. Real blended is better than this if any of the 56 convos booked.

## Pixel health

Pixel 701301873334767 is firing. PageView every hour, Purchase events seen through Sep 22 14:00 UTC, InitiateCheckout + fareharbor-click firing. No escalation.

## SOP diagnosis

| Ad set | Spending? | CPA | Frequency | CTR trend | Verdict |
|---|---|---|---|---|---|
| RT Video Viewers 75% | Yes, full $20/day | $9.39 (under $20 target) | 1.77 (under 5.0) | Up 15% WoW | Winning |
| Messenger Nightlife & Bars | Yes, full $20/day | n/a ($2.47/convo) | 1.76 wk, 2.35 30d (near 2.5 line) | Up 5% WoW | Acceptable, creative aging |

Escalation triggers: none tripped. ROAS well above 2x, pixel live, no $50+/zero-purchase day (max daily spend is ~$40 combined), frequency under 3.0.

## Recommended moves (one per ad set, per SOP)

1. **RT: raise budget 20% to $24/day.** Winning by every threshold and spending its full budget. Retargeting pool is fed by TOF video views, so watch frequency after the bump. Cap at 5.0.
2. **TOF: queue one new creative.** 30d frequency is 2.35, threshold is 2.5. Viral Video is the stronger ad, keep it. Swap Original Party Barge for the next Creative Matrix pick. Don't touch targeting.
3. **RT: add a second creative.** "Still Thinking" is 5 months old. It's still converting so don't pause it, but add one alternate so there's a fallback when it fades.
4. **Creative Testing campaign is paused, and it flopped when it ran.** Apr-May 2026: $3,199 spend, 11 purchases, 0.5x ROAS. The Alligators video got a 16% CTR and 21,500 link clicks but only 3 purchases. Curiosity clicks, not buyers. Don't relaunch it as-is.
5. **Messenger to booking loop is unmeasured.** 192 conversations in 30d and no idea how many booked. OpenCX handles the DMs; pull its conversion count for ad-sourced convos before deciding whether TOF earns more budget.

## Weekly tracker row

| Week | Total Spend | Purchases | Revenue | Blended ROAS | Blended CPA | Top Ad Set | Top Creative | Notes |
|---|---|---|---|---|---|---|---|---|
| 9/15-9/21 | $279.24 | 15 | $3,897.95 | 13.96x | $18.62 | RT Video Viewers 75% | RT Video "Still Thinking" (27.7x) | RT best week in 30d; TOF 56 convos at $2.47; testing campaign paused since May (0.5x) |

## Follow-up (same day): which NPB ad to relist

Searched every campaign in act_87863118 back to 2021 (Meta caps insights at 37 months, so 2023 is Aug 23 onward).

**The one to bring back: "(unpause)Viral Video locals ad- renew creative and rerun"** (campaign 6288768838496, ad set 6288768838296). Archived Apr 26, 2026 during the account restructure. No spend in 2025.

| Period | Spend | Purchases | Revenue | ROAS | CPA |
|---|---|---|---|---|---|
| Aug 23-Dec 2023 | $7,790 | 187 | $34,093 | 4.4x | $42 |
| 2024 full year | $22,359 | 601 | $109,012 | 4.9x | $37 |

Setup that worked: link-clicks objective, New Orleans + 25 mi (home + recent), age 21-65, FB + IG all placements, $20/day, no interest targeting. Two ads on existing page posts:
- "ayeeeeeeee. It's almost the weekend!! $59/person to party!" (viral video, post 195245397959049_644819096335008)
- "It's always COOLER on Bayou Bienvenue. COVERED BOATS and coastal BREEZE 7 days a week" (post 195245397959049_955246548625593)

Caveats before relisting:
- Copy says $59/person, NolaPedalBarge.com and the 1056 phone. Confirm price and swap the URL/brand to nolapartybarges.com. A new post means a new ad (loses the social proof on the old post) unless we edit the old post text and reuse it.
- The same viral video in the spring Creative Testing campaign only did 1.7x. Different objective (purchase), different targeting (broad), no price hook. So the locals-radius + price-in-copy setup is the part to copy, not just the video.
- Link-clicks objective in 2024 got purchase credit via 7-day click attribution on a page with 89k fans. Expect the number to look softer under a purchase objective. Still worth it.

Recommended build: unpause the paused "NPB | Purchase | TOF Prospecting" shell (6976231037096, $80/day, only $44 ever spent), set it to $25/day, one ad set NOLA 25 mi 21-65 broad, and load both old posts as ads plus the current RT "Still Thinking" creative. Purchase objective so it feeds the pixel and the retargeting pool.

Runners-up (all much smaller): "Nola Pedal Barge Ad retargeting" Mar-Jun 2025, $87 spend, 16 purchases, $4,042 (retargeting, "Bourbon Street on the Bayou" copy). Every 2023-2024 "Post:" boost ($100-$900 each, "private party crew", "ship-faced before lace-faced", "Tropical island vibes") shows 0 tracked purchases. High CTR, no sales credit.

## Michael's boosts: not visible anywhere we can see

- No 2026 boosted-post campaigns in act_87863118 from the NPB page. The only 2026 boost in the account is the NKST "tag a friend to win a swamp tour" post from Jul 23 (campaign 52560373835300).
- The NPB page itself reports zero promoted posts (ads_posts is empty, every recent post's promotion_status is "inactive"). Same for the NKST page.
- So if Michael is boosting NPB, it's from the Instagram app or a personal ad account this token can't see.

To get conversions on boosts: boost from the Gravity Trails / Admire NOLA ad account (act_87863118). In the boost dialog, under Payment or Ad account, pick that account. The pixel is already attached, so purchases show in Ads Manager for the boosted post exactly like the RT campaign does (7-day click, 1-day view). Second option if he wants to keep boosting from his phone: put ?utm_source=fb&utm_medium=boost on the link and read bookings in GA4, but that only counts what GA4 sees and GA4 misses FareHarbor checkouts. Ad account is the real fix.
