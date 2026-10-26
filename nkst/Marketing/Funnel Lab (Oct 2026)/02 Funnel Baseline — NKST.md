*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NKST.*

# Funnel Baseline: NKST (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| NKST | 20,774 | not tracked | 4 true purchase events ($0 revenue) | not measurable | 14,883 t.co sessions at 89% bounce; FareHarbor events not firing |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name NKST

2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.
4. FareHarbor to GA4 tracking is broken or partial on NKST (purchase event missing) and HPB (no FH events). Any A/B test there must be read from FareHarbor or Google Ads, not GA4.

## NKST (New Orleans Kayak Swamp Tours), GA4 property 401824264

Numbers (verified 2026-10-14, [GA4]):
- Sessions 20,774, engagement 17.5%. Purchase revenue $0.
- GA4 "conversions" = 359, but 352 of those are the micro event lp_micros___3__pages (a landing-page micro conversion, landing page shows as "(not set)"), 3 are lp_micros___brochure_page, and only 4 are ads_conversion_Purchase_1. There is NO standard purchase event and none of the FareHarbor ecommerce events (view_book_form, add_to_cart, etc.) in the 30-day event list. True purchase rate is not measurable here.
- Prior year same 30 days: 2,554 sessions, 299 "conversions" (also mostly micro events).

Channels [GA4]:
| Channel | Sessions | Eng. | "Conversions" |
|:-|-:|-:|-:|
| Organic Social | 17,540 | 11.9% | 55 |
| Direct | 1,623 | 35.2% | 120 |
| Organic Search | 1,057 | 63.7% | 120 |
| Paid Search | 260 | 71.2% | 42 |
| Referral | 86 | 76.7% | 15 |
| Paid Social | 23 | 30.4% | 0 |
| AI Assistant | 21 | 71.4% | 5 |
Of Organic Social, t.co (Twitter/X) alone is 14,883 sessions at 88.8% bounce with 13 conversions. Without it the site has about 5,900 sessions, in line with last year's 2,554 plus growth. Treat the 20,774 as inflated.

Top landing pages [GA4]: / 19,244 sessions, 15.1% eng, 5 conv. (not set) 418, 0%, 352 conv (the micro event). /alligators-vs-crocodiles 244, 44.3%, 0. /tours/swamp-kayak-tours/manchac-mystic-kayak-tour 242, 48.8%, 0. /tours 115, 59.1%, 0.

Devices [GA4]: mobile 18,950 (92%), 15.0% eng. Desktop 1,620, 45.6% eng. (Conversion counts per device not used because they are dominated by the micro event.)

Paid [Ads, account 4378232023]: NKST campaigns "Nola-Kayak National" ($941, 227 clicks) and "Nola-Kayak Local" ($603, 122 clicks) are PAUSED, 0 conversions in the window, plus "LP Kayak NO - A" paused ($36). No active NKST paid search right now. [Meta]: shares the NOLA account above, split not available. Pixel is the same shared pixel 701301873334767, which is firing.

Drop-off: 20,774 sessions, 0 FH funnel events visible, 4 purchase events. The funnel is blind in GA4.

Top leaks:
1. Traffic quality. 72% of sessions come from one t.co referral source at 89% bounce, which swamps every engagement and conv-rate number.
2. Tracking. No purchase event, no FH events, so there is no on-site baseline for a test. Real bookings must be pulled from FareHarbor (existing note: GA4 does not capture NKST bookings).
3. Mobile engagement 15% on the homepage (19,244 sessions land on /, 15.1% engagement).

Not tracked: purchases/revenue in GA4, FH funnel events, lead capture (engine nkst enabled=false, [Engine]), Clarity.

## Lead capture status (rows for NKST, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| NKST | false | 0 |
Meta shows 2 leads for the NOLA ad account in the last 30 days (act_87863118). OpenCX and email capture details for NPB come from the 2026-10-13 build plan (0 emails saved from 492 chats), not re-verified today.

## What I could not get (lines that touch NKST, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- Clean NPB vs NKST Meta split (shared account).
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
