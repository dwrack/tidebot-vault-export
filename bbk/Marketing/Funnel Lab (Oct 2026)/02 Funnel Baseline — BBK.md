*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for BBK.*

# Funnel Baseline: BBK (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| BBK | 7,560 | 773 / 22 | 87 ($7,200) | 1.15% (was 5.02% LY) | 4,823 paid social sessions, 0 purchases, 10% engagement on one landing page |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name BBK

1. Paid social and boosted traffic is the biggest sink. NPB, BBK, LSKT and HPB all show cold social sessions with 9-31% engagement and near-zero last-click purchases. Meta claims far more purchases than GA4 credits it to, so some is attribution, but the landing pages are also weak.
2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.

## BBK (Buffalo Bayou Kayak), GA4 property 370861451

Numbers (verified 2026-10-14, [GA4 via google-houston]):
- Sessions 7,560, engagement 25.5%, purchases 87, revenue $7,200.47, conv 1.15%.
- Prior year: 3,167 sessions, 159 purchases, $9,909.20 (5.02%). Sessions +139%, purchases -45%, revenue -27%.
- Events: session_start 7,440; view_item_grid 538; view_item_description 111; view_calendar_single_item 596; view_search_by_date 329; view_book_form 773; add_to_cart 22; purchase 87.

Channels [GA4]:
| Channel | Sessions | Eng. | Purchases | Conv |
|:-|-:|-:|-:|-:|
| Paid Social | 4,823 | 10.1% | 0 | 0 |
| Direct | 893 | 38.7% | 23 | 2.58% |
| Organic Search | 518 | 69.3% | 14 | 2.70% |
| Cross-network (PMax) | 475 | 61.1% | 14 | 2.95% |
| Paid Search | 309 | 68.0% | 19 | 6.15% |
| Referral | 177 | 67.2% | 4 | 2.26% |
| Organic Social | 152 | 67.1% | 11 | 7.24% |
| AI Assistant | 21 | 71.4% | 1 | 4.8% |

Top landing pages [GA4]: /kayak-tours/houston-bat-bridge-kayak-tour 4,898 sessions, 10.8% eng, 4 purchases. / 944, 69.0%, 22. /kayak-tours 513, 66.3%, 14. /monthly-clean-up 155, 57.4%, 19. /watersports-rental 96, 44.8%, 4.

Devices [GA4]: mobile 6,566 (88%), 23.2% eng, 72 purchases (1.10%). Desktop 838, 47.4% eng, 15 (1.79%). Tablet 58, 0.

Paid [Ads, account 8497383499 shared]: BBK campaigns $789.50 spend, 28.0 conversions, $2,979.80 value, CPA about $28.2, ROAS about 3.8 (PMax Local $439.70 / 12.0 conv; FH Search Local $199.63 / 7.0 conv; Brand search $150.18 / 9 conv). [Meta act_1015419897308486 "Buffalo Bayou/Houston", last 30d]: spend $899.03, 217,629 impressions, 15,817 clicks, 5,683 link clicks, 3,425 landing page views, CPC (link) $0.158, 112,974 video views. No purchase, lead, or checkout actions appear in the insights at all (the account does not report a pixel purchase). Pixel stats: not pulled (pixel ID for BBK not found).

Drop-off: 7,560 sessions to 773 view_book_form (10.2 per 100) to 87 purchases (11.3% of form views).

Top leaks:
1. The bat-bridge landing page: 4,898 sessions (65% of all traffic) at 10.8% engagement and 4 purchases. This is where the paid social traffic lands (4,823 paid social sessions, 0 purchases).
2. Year over year, sessions +139% while purchases -45%: paid social traffic is inflating sessions and diluting the rate from 5.0% to 1.15%.
3. Mobile 88% of traffic at 23% engagement.

Not tracked: Meta purchase conversion (none reported), BBK pixel stats, lead capture (engine bbk enabled=false, go-live Nov 10 per rollout), Clarity.

## Lead capture status (rows for BBK, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| BBK | false | 0 |

## What I could not get (lines that touch BBK, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
