# Revenue Breakdown & Forecast — Aug 2026

Built 2026-08-25 from the Periode payments export (Nov 7 2025 – Jul 18 2026, the true financial record: 4,296 payments), GA4 property 524300531 (Feb 2026 onward, web checkouts only), and live Google Ads / Meta ad account pulls.

## Headline

**$211,705 net revenue in the first ~8.5 months** (Nov 7 – Jul 18), net of $16.3K refunds. Payment processing fees on top: $6,425. Best month by far: January ($51.1K). Summer floor: ~$19-20K. August is rebounding hard, tracking $26-30K.

## Monthly net revenue (Periode, net of refunds)

| Month | Net revenue | Payments | AOV | Unique customers |
|---|---|---|---|---|
| Nov 2025 (from 11/7) | $7,913 | 118 | $67 | 68 |
| Dec 2025 | $20,016 | 415 | $48 | 200 |
| Jan 2026 | $51,122 | 965 | $53 | 483 |
| Feb 2026 | $31,561 | 705 | $45 | 340 |
| Mar 2026 | $27,349 | 533 | $51 | 244 |
| Apr 2026 | $23,501 | 444 | $53 | 214 |
| May 2026 | $20,297 | 385 | $53 | 163 |
| Jun 2026 | $18,576 | 478 | $39 | 193 |
| Jul 1-18 2026 | $11,372 | 253 | $45 | 116 |
| Jul full (est) | ~$19,500 | ~430 | | |
| Aug 2026 (est) | ~$26-30K | | | |

July estimate: $11,372 over 18 days = $632/day pace. August estimate: GA4 shows $18,406 through Aug 25 in web checkouts alone; GA4 has historically captured 55-72% of true revenue (see calibration below), and it structurally misses membership renewals (~$2K/mo), punch passes, and some gift cards. True Aug 1-25 is likely $21-25K, full month $26-30K.

**Seasonality index (Jan = 100):** Nov(launch) 15 → Dec 39 → Jan 100 → Feb 62 → Mar 53 → Apr 46 → May 40 → Jun 36 → Jul ~38 → Aug ~55-60. The summer slide bottomed in June. August breaking back above April levels mid-summer is the anomaly worth noticing: that's the first month with Google Ads running all month, the attribution bridge live, and the content push.

## Revenue by type (all time, Nov–Jul 18)

| Type | Amount | Share |
|---|---|---|
| Booking items (Social + Private sessions) | $200,629 gross / $184,746 net of refunds | 87% |
| Gift cards sold | $12,659 | 6% |
| Membership invoices (Ember 1/2) | $10,701 | 5% |
| Punch passes / packs | $4,006 | 2% |
| Refunds (all types) | -$16,290 | -7.7% of gross |

Gift cards *redeemed* against bookings: $4,830 (liability being worked off).

## Product mix (all time)

| Product | Revenue |
|---|---|
| Social Sauna | $132,416 |
| Private Sauna | $48,838 |
| Gift cards (Social + Private) | $12,659 |
| Ember 1 + Ember 2 memberships | $10,452 |
| Social Packs + Punch Passes | $3,768 |
| Banya | $1,271 |
| Events (Summer Sunset, NYD Polar Plunge, Black Friday) | $2,459 |

Social Sauna is 63% of everything. Private is 23% at roughly 2.7x the AOV; it's the margin product.

## Memberships (MRR)

| Month | Invoice revenue |
|---|---|
| Nov | $149 |
| Dec | $476 |
| Jan | $1,289 |
| Feb | $1,002 |
| Mar | $1,537 |
| Apr | $1,190 |
| May | $1,735 |
| Jun | $2,082 |
| Jul 1-18 | $1,241 |

Live from the merchant API today: **28 active members** (13 Ember 1 @ $99, 15 Ember 2 @ $149) = **~$3.5K MRR**, plus 24 stopped subscriptions all-time (churn is real: 46% of everyone who ever subscribed has stopped). Punch pass relaunch (Z1zu4...) still at 0 sold.

## Customers

- 1,652 unique customers all-time
- 972 (59%) have paid 2+ times; repeat customers = **$140,027 = 66% of all revenue**
- Unique paying customers per month peaked at 483 (Jan) and bottomed at 116-163 (May-Jul)

## Refunds — watch this line

$16,290 refunded all-time (7.7% of gross). Worst months: Feb $4,135, Jan $2,976, Jun $2,987 (incl. a $159 straight refund). At ~$2-3K/month this is a real cost line; worth a look at whether it's weather cancellations (policy question) or no-show disputes.

## GA4 vs reality (calibration)

GA4 purchase tracking captures only web checkouts and only started Feb 2026:

| Month | GA4 | Periode actual | GA4 capture |
|---|---|---|---|
| Feb | $12,827 | $31,561 | 41% |
| Mar | $17,036 | $27,349 | 62% |
| Apr | $15,197 | $23,501 | 65% |
| May | $11,264 | $20,297 | 55% |
| Jun | $13,290 | $18,576 | 72% |

Capture is improving (attribution bridge live Aug 1) but **never use GA4 as the revenue number**. It's directionally useful month-over-month, that's it. The fix for real-time actuals: either a monthly export from Periode admin, or read/write API access from Erik (requested 2026-06-21, still pending — payments endpoint does not exist on the current key; only products/subscriptions).

## Marketing spend (actual, full year)

| Line | Nov-Jun | Jul | Aug (thru 25) |
|---|---|---|---|
| Google Ads | $0 | $364 | $576 (~$714 pace) |
| Meta paid | $0 | $0 | $0 |

Total paid media for the entire fiscal year to date: **~$940.** Meta ad account act_1425635901791284 confirms zero delivery Nov–Aug. Everything else has been organic IG + PR + email.

Google Ads August: 661 clicks, 19 conversions recorded. If even half those conversions are real bookings at ~$50 AOV that's ~$475 revenue on $576 spend on last-click alone; with the attribution bridge now feeding Periode purchases back, September is the first month a real ROAS read is possible. Decision point Sept 1: scale, hold, or kill.

People costs (the actual marketing budget):
- Lemonade PDX (Hannah Kang): $3K/mo scope, starts with Sept handoff
- Kimberlynn: through Sept 15 — rate not on file
- Early Bird PR (Mack/Jordan): retainer not on file
- ActiveCampaign: plan cost not on file (est. $50-150/mo)
- Ours Here (Jess): fixed-fee per scope, mostly site work

Once Lemonade starts, marketing runs ~$3.7-4K/mo before PR — versus ~$600/mo now. That's the step-change to budget for.

## Forecast (Sept 2026 – Jan 2027)

Assumptions: Aug lands ~$27K net; fall/winter is the season (Jan 2026 = $51K proves demand); Jan 2026 had launch-novelty and a viral IG month in it, so don't bank a repeat at full value; memberships keep grinding up ~$150-300 MRR/mo; V2 saunas NOT included (capacity currently caps Social Sauna revenue — if V2 ships mid-winter the upside case gets bigger).

| Month | Conservative | Base | Upside |
|---|---|---|---|
| Sept | $22K | $25K | $28K |
| Oct | $25K | $29K | $34K |
| Nov | $27K | $32K | $38K |
| Dec | $28K | $34K | $42K |
| Jan 2027 | $38K | $46K | $58K |
| **5-mo total** | **$140K** | **$166K** | **$200K** |

Base case logic: Aug momentum (+45% over July) carried into the strongest 5 months of the calendar, discounted from a naive "last year + growth" because Jan 2026's $51K likely had one-time launch/viral juice in it. Dec includes the gift card surge (Dec 2025 sold $3.2K of gift cards on a customer base one-third the current size).

What would move it up: V2 capacity online before January; punch pass actually selling; membership count breaking 50 ($6K+ MRR floor); Google Ads scaling past a proven ROAS.
What would move it down: refund/cancellation rate staying at 8%; losing the IG engine in the Kimberlynn→Lemonade handoff (Sept-Oct is exactly when the handoff risk and the seasonal ramp collide).

## Gaps to close

1. Fresh Periode export (Jul 18 → today) to replace the Aug estimate with actuals — 5-minute admin task, or chase Erik for API payments access.
2. Kimberlynn rate + Early Bird retainer so the marketing P&L line is real.
3. Refund root-cause: pull the ~$16K of refunds by reason/weather.
4. Fixed opex (moorage, insurance, gas, labor) lives outside this doc — this is revenue + marketing only. A true cash forecast needs those.
