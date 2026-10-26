*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for LSKT.*

# Funnel Baseline: LSKT (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| AKT | 577 | 140 / 10 | 20 ($2,665) | 3.47% (was 2.40% LY) | Traffic is tiny and has no paid source; desktop converts 1.8% vs mobile 5.8% |
| LSKT | 1,920 | 433 / 24 | 62 ($7,937) | 3.23% (was 1.30% LY) | Paid social 373 sessions, 0 purchases; add_to_cart barely fires |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name LSKT

1. Paid social and boosted traffic is the biggest sink. NPB, BBK, LSKT and HPB all show cold social sessions with 9-31% engagement and near-zero last-click purchases. Meta claims far more purchases than GA4 credits it to, so some is attribution, but the landing pages are also weak.

## AKT (Austin Kayak Tours), GA4 property 380369645

Numbers (verified 2026-10-14, [GA4 via google-austin]):
- Sessions 577, engagement 53.6%, purchases 20, revenue $2,664.69, conv 3.47%.
- Prior year: 998 sessions, 24 purchases, $3,507.31 (2.40%). Sessions -42%, purchases -17%, conv rate up.
- Events: session_start 669; view_item_grid 96; view_item_description 52; view_calendar_single_item 113; view_book_form 140; add_to_cart 10; purchase 20; view_search_by_date 11.

Channels [GA4]:
| Channel | Sessions | Eng. | Purchases | Conv |
|:-|-:|-:|-:|-:|
| Organic Search | 267 | 64.8% | 8 | 3.0% |
| Direct | 224 | 35.3% | 5 | 2.2% |
| Referral | 71 | 70.4% | 5 | 7.0% |
| AI Assistant | 8 | 62.5% | 2 | 25% (tiny n) |
| Organic Social | 3 | 33% | 0 | 0 |
No paid search or paid social sessions at all.

Top landing pages [GA4]: / 273, 60.8%, 9 purchases. /austin-kayak-tours/sunset-bat-bridge-kayak-tour 120, 58.3%, 7. /rental 38, 76.3%, 0. /austin-kayak-tours/austin-skyline-tour 23, 43.5%, 1. /contact 19, 26.3%, 0.

Devices [GA4]: desktop 331 sessions (57%), 46.2% eng, 6 purchases (1.8%). Mobile 241 (42%), 63.1% eng, 14 purchases (5.8%). Mobile converts 3.2x desktop.

Paid: Google Ads account for AKT: not identified (not among the accessible accounts by name). Meta: "Lone Star Kayak Tours/Austin" act_638850950128825 is shared with LSKT, last 30d spend $254.48, 18,548 impressions, 909 clicks (319 link clicks, 269 landing page views), 1 pixel purchase worth $17.32, CPA $254.48. Not split by brand.

Drop-off: 577 sessions to 140 view_book_form to 20 purchases (14.3% of form views). add_to_cart (10) is lower than purchases (20), so it is unreliable.

Top leaks:
1. Volume. 577 sessions in a month; any test needs a long window.
2. Desktop: 57% of traffic, 1.8% conv vs 5.8% on mobile.
3. /rental and /contact landing pages produce 0 purchases (57 sessions).

Not tracked: AKT-specific paid data, lead capture (engine has no AKT block; only lskt/bbk), Clarity.

## LSKT (Lone Star Kayak Tours), GA4 property 322345532

Numbers (verified 2026-10-14, [GA4 via google-houston]):
- Sessions 1,920, engagement 56.5%, purchases 62, revenue $7,937.28, conv 3.23%.
- Prior year: 2,078 sessions, 27 purchases, $4,286.69 (1.30%). Sessions -8%, purchases +130%, revenue +85%.
- Events: session_start 1,954; view_item_grid 313; view_item_description 143; view_calendar_single_item 334; view_book_form 433; view_search_by_date 96; add_to_cart 24; purchase 62. Plus video_start 1,376, video_complete 1,229, video_progress 5,193.

Channels [GA4]:
| Channel | Sessions | Eng. | Purchases | Conv |
|:-|-:|-:|-:|-:|
| Cross-network (PMax) | 765 | 74.6% | 32 | 4.18% |
| Paid Social | 373 | 31.1% | 0 | 0 |
| Direct | 349 | 32.1% | 4 | 1.15% |
| Paid Search | 246 | 60.2% | 15 | 6.10% |
| Organic Search | 137 | 75.2% | 9 | 6.57% |
| AI Assistant | 19 | 89.5% | 0 | 0 |
| Organic Social | 17 | 47.1% | 1 | 5.9% |
| Referral | 11 | 81.8% | 1 | 9.1% |

Top landing pages [GA4]: /kayak/sunset-bat-bridge-kayak-tour 812, 48.9%, 26 purchases. / 576, 67.4%, 17. /kayak 226, 78.8%, 7. (not set) 56, 7.1%, 0. /kayak/paddle-board-bat-tour 47, 61.7%, 1.

Devices [GA4]: mobile 1,367 (71%), 55.9% eng, 40 purchases (2.93%). Desktop 545, 58.5% eng, 21 (3.85%). Tablet 12, 1.

Paid [Ads, account 8497383499 shared with HPB and BBK, last 30d, campaign split via ads_query]: LSKT campaigns total $1,505.58 spend, 48.0 conversions, $6,146 value, CPA about $31.4, ROAS about 4.1: "TourPPC Lone Star PMax Local" $1,056.74 (34.0 conv, $4,248), "[FH] Search Generic lonestarkayaktours Bat Local" $436.54 (13.0 conv, $1,844), Brand search paused ($12.31, 1 conv). Whole account: $3,103.74, 2,274 clicks, 85.04 conv, $12,649.81, CPA $36.50, ROAS 4.08. [Meta] Lone Star/Austin account: shared with AKT, $254.48 spend, 1 purchase.

Drop-off: 1,920 sessions to 433 view_book_form (22.6 per 100) to 62 purchases (14.3% of form views).

Top leaks:
1. Paid social: 373 sessions at 31% engagement and 0 purchases.
2. Direct: 349 sessions at 32% engagement, 4 purchases.
3. 22.6% of sessions open the booking form but only 14% of those purchase; add_to_cart (24) is clearly under-fired.

Not tracked: add_to_cart is unreliable; lead capture (engine lskt enabled=false, go-live Nov 10 per rollout); Meta spend not split from AKT; Clarity.

## Lead capture status (rows for LSKT, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| LSKT | false | 0 |
| AKT, E&E | no block | n/a |

## What I could not get (lines that touch LSKT, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- AKT-specific Google Ads and Meta.
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
