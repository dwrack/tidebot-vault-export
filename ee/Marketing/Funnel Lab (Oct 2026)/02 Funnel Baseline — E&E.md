*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for E&E.*

# Funnel Baseline: E&E (split from file 02)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table row

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| E&E | 1,639 | begin_checkout 842 | 325 ($18,544), server-side | n/a (events not session-tied) | 842 begin_checkout to 325 purchase (39%); mobile 89% of sessions with 54% engagement |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns that name E&E

2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.

## E&E (Ebb & Ember, Portland), GA4 property 524300531, booking on Periode

Numbers (verified 2026-10-14, [GA4 via google-ebb]):
- Sessions 1,639, engagement 57.2%. Purchase events 325, purchase revenue $18,544. begin_checkout 842.
- Purchases are sent by the server-side Periode bridge (per vault memory), so they are not tied to web sessions: 121 purchases sit under channel "Unassigned"/landing "(not set)". Do NOT quote 325/1,639 (19.8%) as a conversion rate. A usable on-site proxy: begin_checkout 842 to purchase 325 = 38.6% checkout completion.
- Prior year: the query returned no rows (property had no data for 2025-09-14 to 2025-10-13 or it is outside the property's history). Not available.
- Events: page_view 2,017; session_start 1,494; user_engagement 1,249; begin_checkout 842; click 775; first_visit 642; purchase 325; scroll 313.

Channels [GA4]:
| Channel | Sessions | Eng. | Purchases |
|:-|-:|-:|-:|
| Organic Search | 769 | 56.2% | 85 |
| Direct | 504 | 63.7% | 75 |
| Referral (mostly minside.periode.no) | 299 | 47.2% | 40 |
| Organic Social | 24 | 83.3% | 0 |
| AI Assistant | 14 | 64.3% | 0 |
| Unassigned (server-side) | 14 | 14.3% | 121 |
| Paid Search | 12 | 91.7% | 4 |
Only 12 paid search sessions and 24 social sessions; the site is almost entirely organic and direct.

Top landing pages [GA4]: / 1,392 sessions, 59.8% eng, 192 purchases. /faq 110, 49.1%, 8. /memberships 60, 65%, 2. (not set) 48, 2.1%, 121. /wellness 21, 42.9%, 1.

Devices [GA4]: mobile 1,454 sessions (89%), 53.9% eng, 122 purchases. Desktop 187 sessions, 83.96% eng, 202 purchases. Desktop has 11% of sessions and 62% of purchases, so it is the main booking device even though mobile drives the visits (note some server-side events may be assigned to desktop; treat as directional).

Paid: [Ads, customer 2372234368 = E&E 237-223-4368, last 30d] spend $57.60, 565 impressions, 53 clicks, CPC $1.09, 2 conversions ($147 value), CPA $28.80, all-conversions 14. Account recently restarted, so spend is tiny. [Meta]: not available (facebook MCP excludes Ebb & Ember). Pixel stats: not available.

Drop-off: 1,639 sessions to 842 begin_checkout (0.51 per session, includes repeat and Periode-side checkout steps) to 325 purchases (39% of begin_checkout).

Top leaks:
1. Checkout completion: 517 of 842 begin_checkout events do not end in a purchase event.
2. Mobile: 89% of sessions with 54% engagement vs 84% on desktop.
3. Almost no top-of-funnel paid or social volume, so there is nothing to A/B test on cold traffic yet; tests have to run on organic/direct homepage visits (1,392 landing sessions).

Not tracked: server-side purchases not session-tied (attribution to channels is partial), no prior-year data in this property, no Meta data via tool, lead capture on the site not verified today (not available), Clarity not available.

## Lead capture status (rows for E&E, from file 02)

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| AKT, E&E | no block | n/a |

## What I could not get (lines that touch E&E, from file 02)

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- E&E Meta ads and pixel (facebook MCP excludes Ebb & Ember and Elevated Tides).
- Prior-year data for E&E (empty response).
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
