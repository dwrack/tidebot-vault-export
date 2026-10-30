# Social Analytics Snapshot, 2026-10-29

Last 28d = Oct 1 to 28, 2026. Prior 28d = Sep 3 to 30, 2026. Pulled 2026-10-29, read-only.

## 1. Instagram headline (@ebbandember, IG ID 17841472096789045)

| Metric | Last 28d | Prior 28d | Change |
|---|---|---|---|
| Followers | 9,527 now | n/a | +382 net in Oct (daily values, Sep 30 to Oct 26 PT). Prior window not available, API only serves the last 30 days |
| Reach (account, de-duplicated) | 33,376 | 17,546 | +90% |
| Views (sum of post-level views) | 77,474 | 58,023 | +34% |
| Profile visits | 1,827 | 1,775 | +3% |
| Website link taps | 543 | 663 | -18% |
| Accounts engaged | 2,528 | 1,897 | +33% |
| Interactions (likes + comments + saves + shares, posts) | 3,274 | 1,943 | +68% |

Views and interactions are sums across posts published in each window. The IG API does not serve account-level views or impressions for this account.

## 2. Top 5 IG posts by reach, last 28d

| Date | Type | Gist | Reach | Likes | Comments | Saves | Shares |
|---|---|---|---|---|---|---|---|
| 10/26 | Reel | Friday sunrise river swim with @swimlearnthrive, sauna after | 21,976 | 804 | 48 | 307 | 498 |
| 10/05 | Reel | "name a better combo" sauna plus cold plunge, book-link CTA | 5,945 | 246 | 11 | 80 | 136 |
| 10/14 | Reel | Two new saunas being built at Ebb & Ember | 4,607 | 325 | 16 | 7 | 57 |
| 10/03 | Reel | "stop waiting for the right time," social from $49, buyouts up to 10 | 3,684 | 103 | 5 | 16 | 41 |
| 10/25 | Reel | "some things you just can't replicate," people on the water | 3,216 | 60 | 1 | 13 | 15 |

## 3. Facebook Page (Ebb & Ember Floating Saunas, ID 633573899839067)

- Post engagements (28d rolling): 106 vs 189, -44%
- Page views (28d rolling): 155 vs 150, +3%
- Reach and impressions: not returned. The FB API rejected page_impressions, page_impressions_unique and page_impressions_organic.
- Fans: 281 now. Change over the period not available (page_fans rejected).

## 4. YouTube (youtube-ebb, whole channel; the tool has no Shorts filter)

- Views: 12,770 vs 6,478, +97%
- Avg view duration: 10s vs 9s
- Subscribers: net +6 (gained 7, lost 1) vs net +1 (gained 2, lost 1)

## 5. Takeaways

- The October lift is mostly one post. Reach through Oct 25 was 18,643 on the rolling window, about +6% over the prior window. The Oct 26 collab reel added roughly 15,000 more reach and about 160 follows in the next two days.
- Reels with a save or share hook carry the account. Carousels sit at 1.1k to 2.4k reach, including the Oct 22 collab carousel (2,395 reach, 26 shares).
- Website taps fell 18% while profile visits held flat. Attention is not turning into site clicks, so the link path (bio, booking CTA) is the thing to check.
- Facebook is sliding: post engagements down 44%.

## Errors and gaps

- IG impressions, views and total_interactions: rejected by the tool or API. Replaced with post-level sums (labeled above).
- IG profile visits, website taps, accounts engaged and follower count: rejected at days_28. Pulled daily and summed (total_value).
- IG follower change for the prior window: API only serves the last 30 days.
- FB reach, impressions, fans change: rejected by the FB API (see section 3).
- IG reach is the API's rolling 28-day series. Last window ends Oct 27, prior ends Sep 29, so each is one day off the exact calendar window.
