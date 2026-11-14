# Meta Ads Review + Winter Budget Plan: HPB, Buffalo Bayou Kayak, Lone Star / Austin
Nov 12, 2026 – Feb 28, 2027 · Drafted 2026-11-12 by Claude for Michael · **Proposal only. Nothing was changed in any Meta account.**

Data: Ads Manager monthly campaign exports pulled 2026-11-12 (CSVs in this folder) for three ad accounts: Buffalo Bayou/Houston (1015419897308486, data from Jun 2025), Michael Fischer (129111023833794, from Oct 2023) and Lone Star Kayak Tours/Austin (638850950128825, from Oct 2023). Combined with the Oct 21 and Oct 31 audits, the 11/11 Google winter plan and the 9/24 FareHarbor forecasts.

## Bottom line

1. **Meta cannot tell us what winter spend earns, so cap it small and tie it to FareHarbor.** Only the Austin account's pixel ever recorded purchases (2024–25 season ROAS mostly 1.0–2.3x). The Houston-side accounts have no purchase tracking at all. Every Meta ROAS below is partial.
2. **Demand falls off a cliff.** FareHarbor forecast (Sep 24, zero-shot, "push, don't trust"): Austin $4.0k in Nov, $0.9k in Dec. BBK $2.6k Nov, $1.1k Dec. HPB about 2 bookings a week in Nov, 1 in Dec. Bat tours end Oct 31 in Austin.
3. **Past winters show the same shape.** Meta spend dropped to near zero in Nov–Feb 2024–25 (~$1.7k Houston-family, ~$33 in Dec). Winter 2023–24 spent about $11k on posts and boosts with no purchase tracking.
4. **Proposed Meta winter total: about $2,100 committed plus $450 conditional, versus about $4,400 if the Buffalo Bayou account keeps its October pace** (~$1,230/month).
5. **Stop these first (about $570 a month, no measurable return):** HPB Followers Reboost ($296/mo, $8.46 per page like) and the Initiate Checkout sales campaign ($272/mo, zero checkout events recorded).

## What the exports show

### Meta spend by month, all three accounts, brand assigned by campaign-name keywords

Rough: most campaigns are boosted posts, so a name-based split misfiles some. "Other" is posts I couldn't place. NOLA is shown only to explain the totals.

| Winter (Nov–Feb) | HPB | BBK | Austin/LS | Other | NOLA |
|:-|-:|-:|-:|-:|-:|
| 2023–24 | $6,549 | $0 | $0 | $4,768 | $899 |
| 2024–25 | $1,583 | $0 | $0 | $100 | $925 |
| 2025–26 | $1,014 | $0 | $33 | $1,558 | $5,256 |

Nov 1–12, 2026 so far: HPB $228, BBK $226, Other $283, NOLA $288.

Non-winter for scale (monthly, all brands): Jun–Aug 2025 averaged about $5.3k/month; Jul 2024 hit $10.3k, mostly the $10.9k lifetime "Promoting tel:+1832…" boost.

### Where Meta actually recorded purchases (Austin account only)

| Period | Spend | Purchases | ROAS |
|:-|-:|-:|-:|
| Apr–Jul 2024 | ~$10.3k | 77 | 0.8–2.3x |
| May–Oct 2025 | ~$8.3k | 113 | 1.1–2.2x |
| Nov 2025 | $33 | 2 | 6.5x (tiny) |
| Oct 2026 | $179 | 1 | 0.10x (GA4: 263 paid-social sessions, 0 purchases) |

Best lifetime ads (from the Oct 21 audit, Houston account): In-Market Party Barge $1,054 → 3.74x; RT General Kayak & SUP image 2 → 2.87x; Austin "Kayaks Awareness: In-Market" $1,651 → 4.1x. Worst: retargeting 0.66x, Buffalo Bayou awareness 0.83x, ~$2.6k of houstonboozecruise.com boosts with no tracked purchase.

### What is live today (Buffalo Bayou/Houston account, Ads Manager 11/12)

| Campaign | Status | Lifetime / recent spend | Verdict |
|:-|:-|:-|:-|
| Bat Bridge Kayak Tour – Traffic | Active, $20/day | $3,938 lifetime, $597 in Oct | Cheap clicks ($0.10), zero tracked bookings. Google's bat group runs 15.5x, so demand is real |
| HPB Engagement – Followers Reboost | Active | $1,164 lifetime, $296 in Oct | **Stop.** $8.46 per page like |
| Awareness – Sales [Initiate Checkout] | Active | $3,677 lifetime, $272 in Oct | **Stop.** No events fire |
| Retargeting – Sales [Purchase] | Active | $656 lifetime, 12 purchases lifetime | Keep tiny; only if pixel events work |
| HPB Purchase TOF / Retargeting / Creative Testing | All ads paused | $0 | Dublin, CA geo bug: fix before any un-pause |

Not re-verified today: whether the Party Barge ad set ($30/day, ages 21–44, restarted 10/21) is still delivering. It isn't in the campaign list above, so check where it lives before relying on it.

## Winter plan (Nov 12 – Feb 28, 109 days)

Budget ceilings, Meta only. Google is covered by the approved 11/11 plan.

### Houston Pedal Barge: about $935

| Dates | Daily | What |
|:-|-:|:-|
| Nov 12 – Dec 20 | **$15** | Holiday party angle: Christmas cruise ($59), office and group parties, private barge. One Sales campaign, Houston geo (20–25 mi incl. Kemah/Clear Lake), ages 21–44, 3–4 ads. No "pedal" copy |
| Dec 21 – Feb 28 | **$5** | Retargeting only (site visitors, engagers). Cold spend returns in March |

- Why: HPB books about 1–2 a week; one booking (~$250–$300) covers three weeks at $15. Holiday parties are the winter demand.
- Gate: every ad carries a `?ref=meta-<ad>` tag. If FareHarbor shows fewer than 2 Meta-tagged bookings by Dec 10, drop to $5.
- Do before spending: confirm the ad runs under the right Page (it currently runs under Buffalo Bayou Kayak Tours) and fix the Dublin, CA geo on the old HPB ad sets.

### Buffalo Bayou Kayak: about $1,090

| Dates | Daily | What |
|:-|-:|:-|
| Nov 12 – Dec 31 | **$10** | Bat Bridge Traffic, down from $20. Add 3–4 specific ads (date night, birthday, out-of-town visitors, team outing) so one video isn't carrying 87% of spend |
| Nov 20 – Dec 24 | **+$5** | Gift card ad to the gift cards page |
| Jan 1 – Feb 28 | **$7** | Hold only if ops confirms the bat tour runs all winter; otherwise Skyline/Sunrise tours only at $5 |

- Gate: BBK needs real checkout/purchase events, not just PageView. Until then judge it by `ref=` tags and GA4 `facebook / paid`.

### Lone Star / Austin: $70 committed, $450 conditional

- **Keep Meta off** (paused since Oct 7) until the FareHarbor header-script slot is approved and a pixel sits on austinkayaktours.com. October's $179 bought 0 purchases in GA4.
- Nothing bat-themed until March 2027; bats are gone.
- Feb 15 – Feb 28: **$5/day** retargeting seed ahead of bat season ($70).
- **Conditional:** once measurement is live, $10/day from Jan 15 for 12–20 blunt, specific ads (first-timer, bachelorette, date night, corporate, rentals). About $450 through Feb 28.

### Totals

| | Committed | Notes |
|:-|-:|:-|
| HPB | ~$935 | vs ~$3,270 at the $30/day Party Barge rate |
| BBK | ~$1,090 | vs ~$2,180 at $20/day |
| Austin | ~$70 (+$450 conditional) | vs $0 now |
| **Meta total** | **~$2,100 (+$450)** | ~ $4,400 if the October pace continued |
| Google (approved 11/11) | ~$5,140 | Whole account |

## Do first (no spend needed)

1. Pause Followers Reboost and the Initiate Checkout campaign (~$570/month).
2. Fix measurement: HPB pixel on the FareHarbor booking flow (the 2023 pixel is dead and in the wrong account), purchase/checkout events for BBK, pixel for Austin. Same FareHarbor header-script ask covers all three.
3. Fix the Dublin, CA geo on the paused HPB ad sets, archive the 12 expired 2025 campaigns and the 34 stale active ad sets in the Austin account.
4. Confirm with ops: does the bat tour run all winter, and is the Christmas cruise and fireworks date set?
5. Coordinate with whoever else edits HPB (Google was edited Nov 5 by another login).

## Caveats

- Brand split by campaign name is approximate; the $/month figures are directionally right, not to the dollar.
- Meta reporting changed Nov 5, 2026 (click-based attribution for website conversions), so pre- and post-change numbers aren't perfectly comparable.
- FareHarbor forecast is a base rate from your own history, 38–62% below last year in the same window. Treat it as a floor.
- Winter ROI by year for Meta can't be computed: no purchase column exists for HPB/BBK before this season. Pull FareHarbor bookings by `ref=`/UTM source for the same months to close that gap.
- Not covered: organic post performance, NOLA, Gravity Trails accounts.
