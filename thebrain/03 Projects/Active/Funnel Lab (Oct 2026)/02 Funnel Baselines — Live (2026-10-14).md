# Funnel Baselines, Live (2026-10-14)

Pulled read-only on 2026-10-14. Window = last 30 days (2026-09-14 to 2026-10-13) unless noted. Prior year = 2025-09-14 to 2025-10-13. Every number below is "verified 2026-10-14" and tagged with its source tool. GA4 timezone is the property's own (Pacific for NPB/E&E/BBK, Central for the rest).

Source key: [GA4] = google-*__ga4_run_report / ga4_traffic_sources / ga4_conversions. [Ads] = google-ads__ads_account_summary / ads_query. [Meta] = facebook__fb_get_insights / fb_get_pixel_stats. [Engine] = fh-lead-engine brands.json + DynamoDB scan. Clarity was queried and failed (see end).

## Summary table

| Brand | Sessions 30d | Booking intent (book form views / add_to_cart) | Purchases (GA4) | Conv rate (purchase / session) | Biggest leak |
|:-|-:|:-|-:|-:|:-|
| NPB | 27,845 | 3,881 / 286 | 313 ($79,764) | 1.12% (was 2.32% LY) | 10,966 paid social sessions yield 8 purchases (0.07%); boost pages 5-8% engagement |
| NKST | 20,774 | not tracked | 4 true purchase events ($0 revenue) | not measurable | 14,883 t.co sessions at 89% bounce; FareHarbor events not firing |
| DCKT | 2,012 | 151 / 28 | 18 ($1,030) | 0.89% (was 1.93% LY) | Off-season, no ads or Meta running, blog traffic converts 0 |
| E&E | 1,639 | begin_checkout 842 | 325 ($18,544), server-side | n/a (events not session-tied) | 842 begin_checkout to 325 purchase (39%); mobile 89% of sessions with 54% engagement |
| AKT | 577 | 140 / 10 | 20 ($2,665) | 3.47% (was 2.40% LY) | Traffic is tiny and has no paid source; desktop converts 1.8% vs mobile 5.8% |
| LSKT | 1,920 | 433 / 24 | 62 ($7,937) | 3.23% (was 1.30% LY) | Paid social 373 sessions, 0 purchases; add_to_cart barely fires |
| HPB | 4,528 | not tracked | 0 (not tracked) | not measurable | GA4 has no FareHarbor events at all; 3,091 organic social sessions at 9% engagement |
| BBK | 7,560 | 773 / 22 | 87 ($7,200) | 1.15% (was 5.02% LY) | 4,823 paid social sessions, 0 purchases, 10% engagement on one landing page |

"Booking intent" = FareHarbor GA4 events view_book_form (opened the booking form) and add_to_cart. add_to_cart is clearly under-fired on every FH site (NPB 286 add_to_cart vs 313 purchases), so use view_book_form and purchase as the real funnel anchors. [GA4 ga4_conversions]

## Cross-brand patterns (evidence in the brand sections)

1. Paid social and boosted traffic is the biggest sink. NPB, BBK, LSKT and HPB all show cold social sessions with 9-31% engagement and near-zero last-click purchases. Meta claims far more purchases than GA4 credits it to, so some is attribution, but the landing pages are also weak.
2. Mobile is 88-93% of sessions at NPB, NKST, HPB, BBK, E&E, and desktop converts 1.6x at NPB and BBK. The mobile booking path is the test surface.
3. Lead capture is essentially absent. Only HPB has the popup/drip enabled, and only 4 leads exist in the engine table ever. [Engine]
4. FareHarbor to GA4 tracking is broken or partial on NKST (purchase event missing) and HPB (no FH events). Any A/B test there must be read from FareHarbor or Google Ads, not GA4.
5. Self-referral leak on NPB: nolapartybarges.com shows up as a referral source with 1,802 sessions and 77 purchases. That is checkout return traffic not excluded as a referral, so Direct/Referral/Paid purchase attribution is distorted.

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## Lead capture status across brands

Verified 2026-10-14 from ~/Projects/fh-lead-engine/engine/brands.json and a DynamoDB scan of fh-leads:
| Brand | Engine enabled | Leads in table |
|:-|:-|:-|
| HPB | true | 4 (all-time, brand hpb) |
| NPB | false | 0 |
| NKST | false | 0 |
| DCKT | false | 0 |
| BBK | false | 0 |
| LSKT | false | 0 |
| AKT, E&E | no block | n/a |
Meta shows 2 leads for the NOLA ad account in the last 30 days (act_87863118). OpenCX and email capture details for NPB come from the 2026-10-13 build plan (0 emails saved from 492 chats), not re-verified today.

## What I could not get

- Clarity (all 12 project IDs from vault memory): dashboard, problem_pages and project_info calls returned "Error while retrieving data" codes 100 and 101 on NPB, NKST and E&E projects. No dead click, rage click or scroll depth data. Consistent with the 2026-09-19 note that the script was never confirmed on FareHarbor sites.
- E&E Meta ads and pixel (facebook MCP excludes Ebb & Ember and Elevated Tides).
- Prior-year data for E&E (empty response).
- Clean NPB vs NKST Meta split (shared account).
- AKT-specific Google Ads and Meta.
- Pixel IDs for BBK, HPB, LSKT, AKT were not looked up. Meta pixel stats only pulled for NPB/NKST shared pixel and DCKT.
- Meta pixel returned window began 2026-09-17, not 2026-09-14, so pixel counts cover about 27 days.
- OpenCX chat data and email list sizes were not re-pulled; relying on the 2026-10-13 audit where noted.
