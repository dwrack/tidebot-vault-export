# Revenue Breakdown & Forecast — Aug 2026

Built 2026-08-25 from Periode payments exports covering opening day through today (Nov 7 2025 – Aug 25 2026, the true financial record: 5,209 payments across two exports, deduped by Payment ID), GA4 property 524300531 (Feb 2026 onward, web checkouts only), and live Google Ads / Meta ad account pulls.

## Headline

**~$261K net revenue since opening** (Nov 7 – Aug 25), net of ~$18.3K refunds. Best month by far: January ($51.1K). But the story is August: **$33,076 actual through Aug 25, pacing ~$41K** — on track to be the second-best month ever, in what was supposed to be the seasonal floor. July's back half more than doubled its front half ($1,174/day vs $669/day); the summer slump reversed hard in mid-July and hasn't let up.

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
| Jul 2026 | **$27,802** | 547 | $51 | | 
| Aug 1-25 2026 | **$33,076** | 619 | $53 | |
| Aug full (pace) | ~$41,000 | ~770 | | |

July and August are actuals from the fresh export (transaction-date filter, deduped against the 7/18 export). July split: $11,372 in Jul 1-17 ($669/day) vs $16,430 in Jul 18-31 ($1,174/day) — the inflection is mid-July. August daily average: $1,323, with the last 7 days holding $1,100-2,150/day.

**Seasonality index (Jan = 100):** Nov(launch) 15 → Dec 39 → Jan 100 → Feb 62 → Mar 53 → Apr 46 → May 40 → Jun 36 → Jul 54 → Aug ~80. The "summer floor" thesis is dead: June was the bottom, and Aug is pacing to beat every month except January. What changed mid-July: Google Ads went live (7/18), the viral IG month (July: 2,388 GA4 sessions vs June's 1,239), the content push, punch pass relaunch. Growth this steep against seasonality means the winter comp should be aggressive, not cautious.

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

## Jul 18 – Aug 25 window detail (fresh export, 913 payments)

| Type | Amount |
|---|---|
| Booking items | $44,365 |
| Membership invoices | $2,826 |
| Gift cards | $2,359 |
| Punch passes | $1,853 |
| Refunds | -$2,046 (4.3% of gross — half the lifetime rate) |

Products in the window: Social Sauna $27,825, Private Sauna $12,126, Summer Sunset Sauna $1,910, Punch Pass $1,853 (finally selling after months at zero), Gift Cards $1,753, Ember 1+2 $2,975, Banya $862.

## Forecast (Sept 2026 – Jan 2027)

Assumptions: Aug lands ~$40-41K (actual pace, not estimate); the mid-July inflection (ads + IG + content) is at least partly durable; last year's seasonality still applies on top (Jan 2026 = 2.75x June 2026); Jan 2026 had launch-novelty/viral juice so the winter multiplier is discounted; memberships grind up slowly; V2 saunas NOT included — and capacity is now the live question, because Jan's $51K is the only proof of what the current boat can absorb, and Aug is already pacing 80% of that.

| Month | Conservative | Base | Upside |
|---|---|---|---|
| Sept | $32K | $37K | $43K |
| Oct | $34K | $41K | $48K |
| Nov | $36K | $44K | $52K |
| Dec | $38K | $47K | $56K |
| Jan 2027 | $45K | $55K | $68K |
| **5-mo total** | **$185K** | **$224K** | **$267K** |

Base case logic: hold Aug's ~$41K pace roughly flat through fall (conservative already assumes a ~20% giveback of the summer surge), then layer the winter ramp at a discounted multiplier. Even the conservative case has every month beating the same month's spring equivalent by 60%+. Dec includes the gift card surge (Dec 2025 sold $3.2K of gift cards on a customer base one-third the current size). The realistic cap on Base/Upside is capacity, not demand: if slots sell out, revenue plateaus wherever fill does — which is exactly the argument for V2 landing before January.

What would move it up: V2 capacity online before January; punch pass momentum continuing; membership count breaking 50 ($6K+ MRR floor); Google Ads scaling past a proven ROAS.
What would move it down: the summer surge proving to be a one-time viral spike; losing the IG engine in the Kimberlynn→Lemonade handoff (Sept-Oct is exactly when handoff risk and the seasonal ramp collide); capacity ceiling binding earlier than expected.

## Gaps to close

1. Kimberlynn rate + Early Bird retainer so the marketing P&L line is real.
2. Refund root-cause: pull the ~$18K of lifetime refunds by reason/weather (though the rate is improving: 4.3% in the last window vs 7.7% lifetime).
3. Fixed opex (moorage, insurance, gas, labor) lives outside this doc — this is revenue + marketing only. A true cash forecast needs those.
4. Capacity math: verify max weekly sellable seats against the winter schedule so the forecast ceiling is a number, not a guess.

## Data pipeline note

Fresh payments data can be pulled anytime via the Chrome bridge → merchant.periode.no → Reporting → CSV → Generate Sales CSV (transaction-date filter). Exports land in `Operations/Sales Data/`. Export small windows and dedupe by Payment ID against prior exports; a 10-month range crashes the tab.
