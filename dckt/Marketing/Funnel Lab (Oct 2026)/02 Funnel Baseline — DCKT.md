*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for DCKT.*

# Funnel Baseline: DCKT (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| DCKT | 2,012 | 151 / 28 | 18 ($1,030) | 0.89% (was 1.93% LY) | Off-season, no ads or Meta running, blog traffic converts 0 |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name DCKT

No cross-brand pattern in file 02 names DCKT. The brand section below is the full picture.

## DCKT (Door County Kayak Tours), GA4 property 320677015

Numbers (verified 2026-10-14, [GA4]):
- Sessions 2,012, engagement 54.7%, purchases 18, revenue $1,030.03, conv 0.89%.
- Prior year: 2,485 sessions, 48 purchases, $3,553.95 (1.93%). Sessions -19%, purchases -63%, revenue -71%. Door County is winding down for the season, so part of this is seasonal timing.
- Events: session_start 2,195; view_item_grid 150; view_calendar_single_item 296; view_book_form 151; view_search_by_date 115; add_to_cart 28; purchase 18; view_item_description 24.

Channels [GA4]:
| Channel | Sessions | Eng. | Purchases | Conv |
|:-|-:|-:|-:|-:|
| Organic Search | 1,237 | 68.1% | 14 | 1.13% |
| Direct | 633 | 28.0% | 3 | 0.47% |
| Referral | 53 | 50.9% | 1 | 1.9% |
| Organic Social | 48 | 62.5% | 0 | 0 |
| AI Assistant | 19 | 78.9% | 0 | 0 |
| Cross-network | 10 | 30.0% | 0 | 0 |
| Paid Search | 7 | 85.7% | 0 | 0 |

Top landing pages [GA4]: / 630 sessions, 63.3% eng, 16 purchases. /blog/7-of-the-best-hiking-trails-in-door-county 210, 72.9%, 0. /e-bike-tours 133, 71.4%, 1. /kayak-tours/cave-point-county-park 86, 51.2%, 0. (not set) 73, 0%, 0.

Devices [GA4]: mobile 1,152 sessions (57%), 59.4% eng, 10 purchases (0.87%). Desktop 834, 48.0% eng, 7 (0.84%). Mobile and desktop convert the same.

Paid: [Ads, account 8672151991] last 30d spend $0, 0 impressions (nothing running). [Meta act_10153674414451399] last 30d: no data returned (no spend). Pixel 421987437994175 [Meta, window 9/17-10/13]: PageView 10,191, Purchase 48 (last fired 2026-10-03 20:00 UTC), Contact 1. No InitiateCheckout, Lead or fareharbor-click events appeared in this window, and no Purchase in the last 10 days. Prior notes called this likely season-end rather than a break. Not resolved.

Drop-off: 2,012 sessions to 151 book form views (7.5 per 100) to 28 add_to_cart (18.5% of form views) to 18 purchases. Form to purchase = 11.9%.

Top leaks:
1. No paid demand capture in the off-season; 100% of purchases came from organic search (14) and direct (3).
2. Blog traffic is 210 sessions at 73% engagement and 0 purchases (no path from blog to booking evidenced here).
3. Direct traffic: 633 sessions at 28% engagement, 3 purchases.

Not tracked: Meta InitiateCheckout/Lead events not seen this window, lead capture (engine dckt enabled=false, Nov 10 go-live per rollout), Clarity.

## Lead capture status (rows for DCKT, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| DCKT | false | 0 |

## What I could not get (lines that touch DCKT, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
