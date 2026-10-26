*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NPB.*

# Funnel Baseline: NPB (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| NPB | 27,845 | 3,881 / 286 | 313 ($79,764) | 1.12% (was 2.32% LY) | 10,966 paid social sessions yield 8 purchases (0.07%); boost pages 5-8% engagement |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name NPB

1. Paid social and boosted traffic is the biggest sink. NPB, BBK, LSKT and HPB all show cold social sessions with 9-31% engagement and near-zero last-click purchases. Meta claims far more purchases than GA4 credits it to, so some is attribution, but the landing pages are also weak.
2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.
5. Self-referral leak on NPB: nolapartybarges.com shows up as a referral source with 1,802 sessions and 77 purchases. That is checkout return traffic not excluded as a referral, so Direct/Referral/Paid purchase attribution is distorted.

## NPB (NOLA Party Barge), GA4 property 322288940

Numbers (verified 2026-10-14, [GA4]):
- Sessions 27,845, engagement rate 29.6%, purchases 313, purchase revenue $79,763.76, conv rate 1.12%.
- Prior year same 30 days: 20,050 sessions, 465 purchases (2.32%). Sessions +39%, purchases -33%.
- Funnel events (event counts): session_start 30,288; view_item_grid 2,865; view_item_description 290; view_calendar_single_item 3,179; view_book_form 3,881; add_to_cart 286; purchase 313. Also video_start 5,564, video_complete 4,824, scroll 5,344, click 121.

Channels (sessions, engagement, purchases, conv rate), [GA4]:
| Channel | Sessions | Eng. | Purchases | Conv |
|:-|-:|-:|-:|-:|
| Paid Social | 10,966 | 13.4% | 8 | 0.07% |
| Organic Social | 7,213 | 13.6% | 7 | 0.10% |
| Direct | 2,727 | 43.6% | 55 | 2.02% |
| Referral | 2,314 | 78.7% | 96 | 4.15% |
| Paid Search | 2,152 | 61.2% | 92 | 4.28% |
| Organic Search | 1,341 | 67.0% | 17 | 1.27% |
| Cross-network (PMax) | 985 | 61.0% | 30 | 3.05% |
| Email | 64 | 73.4% | 0 | 0 |
| AI Assistant (chatgpt, gemini, claude, copilot) | 40 | n/a | 2 | n/a |

Top 5 landing pages [GA4]: / 11,566 sessions, 29.8% eng, 71 purchases. /the-freaky-tiki 6,548, 25.4%, 63. /boost-ig 2,655, 5.1%, 0. /boost 2,095, 7.6%, 0. /pedal-bike-barge-cruise 466, 56.9%, 12.

Devices [GA4]: mobile 25,686 sessions (92%), 26.4% eng, 275 purchases (1.07%). Desktop 2,135, 64.9% eng, 37 purchases (1.73%). Tablet 182, 1 purchase.

Paid [Ads, account 4378232023 "Gravity Trails | NOLA", last 30d]: spend $8,791.35, 5,808 clicks, 114.12 conversions, conv value $32,726, CPA $77.04, ROAS 3.72. This account also holds NKST campaigns (the NKST ones are PAUSED but spent about $1,545 with 0 conversions in the window). NPB-tagged live campaigns: Search National $3,251 (64.2 conv, $18,522 value), PMax "Sales-Performance Max-12" $1,625 (33.4 conv, $9,931; brand tag not shown), Search Local $1,367 (16.5 conv, $4,273).
[Meta, act_87863118 "Gravity Trails / Admire NOLA", last 30d]: spend $4,555.38, reach 165,503, 19,802 clicks (link clicks 7,936, landing page views 5,798), 71 pixel purchases worth $15,791.89, CPA $64.16, ROAS 3.47, 2 leads, 180 messaging replies. Account is shared across brands, so NPB vs NKST split is not available.
Pixel 701301873334767 [Meta fb_get_pixel_stats, returned window 2026-09-17 to 2026-10-13]: Purchase 402 events (last 2026-10-13), InitiateCheckout 206 (last 10/12), fareharbor-click 167, Lead 2, PageView 133,650. Purchase pixel is firing.

Drop-off (sessions to purchase):
1. 27,845 sessions
2. 3,881 view_book_form events (about 14 per 100 sessions; many are repeat views)
3. 286 add_to_cart (under-fired)
4. 313 purchases (1.12% of sessions)
Cold social is the problem: paid + organic social is 18,179 sessions (65%) and 15 purchases.

Top leaks:
1. Cold social to homepage and boost pages. 10,966 paid social sessions at 13% engagement. /boost and /boost-ig take 4,750 sessions with 0 purchases at 5-8% engagement. (GA4 landing report.)
2. Attribution leak. Meta credits 71 purchases, Google Ads 114, GA4 313 total, with 96 under Referral (1,802 of those sessions are nolapartybarges.com itself) and 55 under Direct. Last-click GA4 cannot be used to judge social tests without fixing the referral exclusion.
3. Mobile: 92% of sessions, desktop converts 1.6x and engages 2.5x longer in rate terms.

Not tracked / gaps:
- Lead capture: none live. Lead engine NPB block is enabled=false. [Engine]. Per the 2026-10-13 audit (carried over, not re-verified today): banner "Get early access" is the dead GHL form, OpenCX saved 0 emails in 60 days, win-back email sent about 33k a week with 41 GA4 sessions.
- Email channel is 64 sessions, 0 purchases (UTMs missing on win-back links per the 10/13 plan).
- Clarity: not available (see end).
- No cross-domain/self-referral exclusion for the FareHarbor checkout domain.

## Lead capture status (rows for NPB, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| NPB | false | 0 |
Meta shows 2 leads for the NOLA ad account in the last 30 days (act_87863118). OpenCX and email capture details for NPB come from the 2026-10-13 build plan (0 emails saved from 492 chats), not re-verified today.

## What I could not get (lines that touch NPB, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- Clean NPB vs NKST Meta split (shared account).
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
