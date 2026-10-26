*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for HPB.*

# Funnel Baseline: HPB (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| HPB | 4,528 | not tracked | 0 (not tracked) | not measurable | GA4 has no FareHarbor events at all; 3,091 organic social sessions at 9% engagement |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name HPB

1. Paid social and boosted traffic is the biggest sink. NPB, BBK, LSKT and HPB all show cold social sessions with 9-31% engagement and near-zero last-click purchases. Meta claims far more purchases than GA4 credits it to, so some is attribution, but the landing pages are also weak.
2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.
3. Lead capture is essentially absent. Only HPB has the popup/drip enabled, and only 4 leads exist in the engine table ever. [Engine]
4. FareHarbor to GA4 tracking is broken or partial on NKST (purchase event missing) and HPB (no FH events). Any A/B test there must be read from FareHarbor or Google Ads, not GA4.

## HPB (Houston Pedal/Party Barge), GA4 property 370616603

Numbers (verified 2026-10-14, [GA4 via google-houston]):
- Sessions 4,528, engagement 21.6%, purchases 0, revenue $0.
- Prior year: 11,155 sessions, 0 purchases, $0. Sessions -59%.
- 30-day event list contains only page_view, session_start, first_visit, user_engagement. No FareHarbor events, no purchase, no conversions. HPB booking funnel is invisible in GA4.

Channels [GA4]: Organic Social 3,091 sessions (68% of traffic), 9.0% eng, 0 purchases. Paid Search 504, 55.6% eng. Direct 435, 29.2%. Organic Search 397, 59.2%. Referral 55. AI Assistant 38, 50% eng. Cross-network 13. Paid Social 10.

Top landing pages [GA4]: / 3,998 sessions, 18.6% eng. /houston-party-barge-cruise 173, 41.6%. /2026/06/30/boat-rides-in-houston 53, 41.5%. /2026/07/14/things-to-do-in-kemah-besides-the-boardwalk 38, 52.6%. /firework-show-and-party-barge 36, 61.1%.

Devices [GA4]: mobile 4,209 (93%), 19.3% eng. Desktop 321, 48.9% eng.

Paid [Ads]: HPB's own campaign "Search - Houston Pedal Barge" lives in account 8497383499: $808.65 spend, 495 clicks, 8.99 conversions, $3,523.51 value, CPA about $89.9, ROAS 4.36. Solo account 2986009791 "Houston Party Barge" (PMax): $122.37 spend, 128 clicks, 5 conversions, $200 value, CPA $24.47, ROAS 1.63, all-conversions 158 (includes non-purchase actions). Ads see purchases that GA4 on this property does not, so a GA4 purchase pipe is still not on the HPB property (verified today). [Meta]: HPB-specific account not available. The "Buffalo Bayou/Houston" account (act_1015419897308486) may carry HPB boosts but is labeled BBK; split not available.

Lead capture: HPB is the only brand with the popup/drip enabled (CREW25, $25 off 2+ guests, expires Oct 31). DynamoDB fh-leads has 4 records total, all brand hpb (scan Count 4, verified 2026-10-14; created dates not pulled, so 30-day count not available). Sessions to leads: about 4 leads against 4,528 sessions this month at most.

Drop-off: not measurable in GA4.

Top leaks:
1. Tracking. Zero FH events and zero purchases in GA4 mean no web funnel baseline.
2. 3,091 organic-social sessions at 9% engagement (probably story or link-in-bio taps), which is 68% of all traffic.
3. 93% mobile with 19% engagement on the homepage that receives 3,998 sessions.

Not tracked: purchase and booking events on the HPB GA4 property, Meta HPB account, popup conversion counts beyond 4 stored leads, Clarity.

## Lead capture status (rows for HPB, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| HPB | true | 4 (all-time, brand hpb) |

## What I could not get (lines that touch HPB, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
