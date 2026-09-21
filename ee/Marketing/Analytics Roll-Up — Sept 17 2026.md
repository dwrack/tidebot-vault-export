# Analytics Roll-Up: Sept 17, 2026

Window: last 28 days (Aug 20 to Sep 16) vs the prior 28 (Jul 23 to Aug 19). GSC lags, so its window is Aug 18 to Sep 14 vs Jul 21 to Aug 17.

## Headline

Revenue held flat at ~$34K while every top-of-funnel number fell 10 to 75%. Guests served jumped 42%. The business is running on repeat customers and direct demand right now, not discovery.

## Periode (sales export, transaction date)

| | Prior 28 | Last 28 | Change |
|---|---|---|---|
| Net revenue | $35,181 | $34,084 | -3% |
| Payments | 634 | 748 | +18% |
| Unique customers | 262 | 284 | +8% |
| Guests served (service date) | 468 | 663 | +42% |
| Refunds | $540 | $3,047 | 5.6x |

- August closed at $39,721 net. September is at $19,392 through the 17th, pacing ~$34K.
- Weekly net: peaked $10.6K week of Aug 17, since then $8.2K, $7.7K, $8.6K.
- Mix last 28: Social $20.4K, Private $7.8K, Ember 1 $1.4K, Ember 2 $1.3K, Sunset $1.2K, Banya $0.9K, Punch Pass $0.8K, gift cards $0.4K.
- Refunds are ~8% of gross, up from 4.3% in the Aug 25 read. Spread across many days (biggest: Aug 20 $451, Sep 8 $413, Sep 1 $411), almost all Social Sauna. No single event explains it.
- Memberships (API): Ember 1 = 17 active, 6 new in the last 28 (vs 1 prior). Ember 2 = 18 active, 4 new (vs 4). 35 active members total. Stopped all-time: 15 Ember 1, 9 Ember 2.
- Export filed: `Operations/Sales Data/Periode Sales Export 2026-07-23 to 2026-09-17.xlsx`. Note Periode changed the export flow: "Generate Sales CSV" now queues a report, and a Download link appears in a table below the button.

## Website (GA4)

| | Prior 28 | Last 28 | Change |
|---|---|---|---|
| Sessions | 2,281 | 1,721 | -25% |
| Users | 1,489 | 1,010 | -32% |
| New users | 1,197 | 671 | -44% |
| Engagement rate | 59.5% | 56.3% | |
| Purchases | 284 | 322 | +13% |
| Purchase revenue | $18,922 | $21,948 | +16% |

Sources, last 28: Google organic 779 sessions, direct 584, Periode referral 231, Google Ads 35, Instagram 20, ChatGPT 15, Yahoo 11, Bing 6, DuckDuckGo 6.

- Instagram sends 20 site sessions against 625 IG link taps. Most of those taps go straight to Periode booking and never touch the site, so GA4 undercounts IG badly.
- Google Ads shows only 35 sessions in 28 days because the account has been paused since Aug 23 (see Google Ads section).
- ChatGPT referrals (15) now beat Bing.

## Google Ads (account 237-223-4368)

**The account has been paused since Aug 23.** Google's banner: "Your verification deadline has passed. To restart your ads, complete advertiser verification." Zero impressions for 25 days. Campaigns, ads and billing are all fine, it's only the unverified-advertiser hold.

| | Prior 28 | Last 28 | Change |
|---|---|---|---|
| Clicks | 823 | 93 | -89% |
| Impressions | 8,123 | 910 | -89% |
| Spend | $736 | $68 | -91% |
| Conversions | 13 | 8 | |
| Conv. value | $1,345 | $1,239 | |

- All 93 clicks in the last 28 came from Aug 20 to 22. Before the pause the account ran ~30 clicks/day at ~$26/day.
- Core Search: 621 clicks at $1.14 CPC prior, 64 clicks last 28. Tourist Awareness: 202 clicks at $0.14 prior, 29 last 28.
- CTR was healthy at ~10% on both campaigns.
- The Aug 27 near-me overhaul (15mi radius, location-insertion ad group, sitelinks) has never served a single impression. It went live four days after the pause.
- This explains most of the GA4 new-user drop (-44%) and part of the GSC/GBP softness: ~800 clicks a month of paid discovery went to zero.
- Fix: Google Ads → the "Fix it" button on the red banner → complete advertiser verification (legal business name, EIN 39-2506659 docs, sauna@ owner). Usually clears in a few business days once submitted.

## Search Console

| | Prior 28 | Last 28 | Change |
|---|---|---|---|
| Clicks | 1,689 | 1,518 | -10% |
| Impressions | 6,872 | 6,107 | -11% |
| Avg position | ~6 | ~6 | flat |

- Still almost all brand. "ebb and ember" alone: 428 clicks (535 prior). The dip is brand demand cooling after the July viral reel, not a ranking loss.
- Non-brand movers up: "sauna boat portland" 5 to 19 clicks, "sauna cold plunge portland" 3 to 11 (pos 3.6 to 2.5), "floating sauna portland" 67 to 78 clicks.
- Watch: "portland floating sauna" average position slid 1.3 to 8.4, and "floating sauna portland" 1.4 to 2.7. Same click volume so far, but someone is contesting the head term.
- Biggest untapped: "sauna portland" 321 impressions at position 7.5, 4% CTR. "portland sauna" 140 impressions at 8.3. "cold plunge portland" dropped out of the top 25.
- /faq, /memberships, /shop, /wellness each show ~1,700 to 2,000 impressions at position ~3 with under 1.2% CTR. Those are sitelink impressions under brand searches, not real opportunities.

## Google Business Profile

| | Prior 28 | Last 28 | Change |
|---|---|---|---|
| Impressions (search + maps) | 4,178 | 3,009 | -28% |
| Website clicks | 719 | 630 | -12% |
| Direction requests | 382 | 293 | -23% |
| Calls | 15 | 18 | +20% |

- Reviews: 116 total, 4.9 average (94 on Jun 16, so +22 in three months). 12 new in the last 28 days, 11 five-star, one four-star.
- 4 reviews unanswered: Carolyn Lee (Sep 16), Jessi Sells (Sep 14), Andrew Vasquez (Sep 14), Lisa Woldin (Sep 11).
- The `gmb_get_insights` MCP tool is dead (Google retired the v4 reportInsights endpoint). These numbers came from the Business Profile Performance API using the sauna@ token directly.

## Instagram

| | Prior 28 | Last 28 |
|---|---|---|
| Reach (sum of daily) | 134,390 | 32,343 |
| New follows | n/a | 286 |
| Profile visits | n/a | 1,872 |
| Link taps | n/a | 625 |

- The -76% is the tail of the Jul 17 "something different to do with friends" reel (2,164 likes) rolling off. There was no Meta ad spend in either window, so that was organic.
- Best of the last 28: "other river" reel Aug 27 (311 likes), Fall Equinox reel Sep 10 (270), Member Night recap Sep 16 (159 likes in under a day, and 71 new follows across Sep 15 to 16).
- Reels carry the account. Carousels and static posts land at 30 to 100 likes.
- 8 posts in 28 days.

## TikTok (Studio, last 28 vs prior 28)

| | Last 28 | Change |
|---|---|---|
| Video views | 5.1K | -30% |
| Profile views | 104 | -18% |
| Likes | 129 | -58% |
| Shares | 14 | -58% |
| Comments | 1 | |
| Net followers | +20 | 1.4K total |

- 83.5% For You, 11.1% search. Search queries are all "things to do in Portland" variants: group activities, rainy day ideas, where to take a visiting friend.
- Audience 71% female, 25 to 44 is 72%.
- TikTok is idling. It needs the Lemonade PDX handoff to land before it moves.

## What I'd do

1. Complete Google Ads advertiser verification today. The account has been dark since Aug 23.
2. Dig into the refund jump. 8% of gross is $3K a month.
3. Reply to the 4 open Google reviews.
4. Ship the sauna pillar page work. "sauna portland" at position 7.5 with 321 impressions a month is the one non-brand term with real volume, and brand search is softening heading into fall.
5. More reels in the "other river" and event-recap style. Those are the only formats breaking 150 likes.
