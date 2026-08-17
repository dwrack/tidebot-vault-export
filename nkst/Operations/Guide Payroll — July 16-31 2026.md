# Guide Payroll — July 16-31, 2026

> **STATUS: PAID — 2026-08-02. Period total $1,670, not $1,600.**
>
> **CORRECTION (2026-08-17):** the audit below concluded Michelle's $125 rate had no basis and recommended $100. David has since confirmed **$125 is correct**, and that **Chelsea is $110**, not $100. He paid both differences within this same pay period — Michelle +$50, Chelsea +$20 — so the table below understates what actually went out. Nothing is still owed. Rates are per-guide, not flat; see [[Operations/Guide Payroll — Aug 1-15 2026]] for the corrected rate card. Treat the "$125 claim" section below as superseded.
>
> **Carried into Aug 1-15:** the $65 card tip from 8/1 still needs passing through to whoever ran that tour, and that guide is still unidentified in FareHarbor.
>
> **Committed to guides 2026-08-02:** W-9s and contracts get reviewed and brought current before the next pay period closes.

*Pulled from FareHarbor crew assignments on 2026-08-02. Due on or before Jul 31 (bi-monthly: 1st-15th paid the 15th, 16th-EOM paid the last day).*

**Source:** `~/Projects/fareharbor-brief/guide-payroll.mjs` reads the FareHarbor calendar API and credits every `crew_member` assigned to a departure that actually ran (customer_count > 0, not cancelled). Re-run any period with:

```
cd ~/Projects/fareharbor-brief
node guide-payroll.mjs neworleanskayakswamptours 2026-07-16 2026-07-31
```

---

## Rate confirmed against a real payout

Stephanie Lazensky was paid **$600** for the 7/1-7/15 period. FareHarbor shows she ran 4 standard Manchac + 1 Extended Manchac in that window. 4 × $100 + $200 = $600, exact.

So the rate actually being paid right now is:

| Tour type | Rate |
|---|---|
| Standard 2hr Manchac / Honey Island | **$100** |
| Extended Manchac (4hr) | **$200** |
| Whitney Plantation Combo (8hr) | not documented, none ran in July |
| Bayou Kayak Rentals (self-guided) | assumed $0, no guide assigned |

This contradicts three places in the vault. `SOPs/NKST — Guide SOP Master` Part 9 says $100-125 informal, `SOPs/NKST — Crew Assignment & Minimum Headcount Policy` says ~$100-125, and `Legal/ICA Exhibit A` proposes a flat $110. The live number is $100 flat for standard. Fix those docs or finalize Exhibit A.

**Confirmed at $100/$200 so far:**

| Guide | How confirmed |
|---|---|
| Stephanie Lazensky | Back-solved from her $600 payout for 7/1-7/15 |
| River Bourne (riverbourne.here@gmail.com) | Confirmed directly by David, 2026-08-02 |

**Still unconfirmed:** Chelsea Hines, Alexis Hingle, Michelle Healey.

### The Michelle $125 claim — audited 2026-08-02, no basis found

There is **no signed contract for Michelle at any rate**. The `Legal/` folder holds only templates with blank signature lines.

The $125 figure traces to exactly two places, both drafts written the same week by the same hand, neither citing a source:

- `Legal/ICA Exhibit A` line 63, internal open-items: "Existing guides currently at $125 (Nick, Michelle)"
- `NKST — Operations Contractor Master Todo` line 245, restating the same claim

That's one unsourced assertion echoed twice, not two independent confirmations.

**Probable origin of the confusion:** `Legal/Operations Contractor Agreement` has two $125 line items in the Growth & Admin duty table — "Payroll $125" and "FareHarbor integration / ledger currency $125". Those are per-pay-period deliverable values inside the $800 Lane, not a per-tour guide rate. Michelle is the only person who holds both a contractor and a guide role, so a $125 in her comp doc reads like a tour rate if skimmed.

Everything actually verifiable says $100: Stephanie's $600 payout back-solves exactly to 4 × $100 + $200, and River Bourne confirmed $100/$200 directly.

**Countervailing point worth raising with her.** The same Operations Contractor Agreement, Section 4 (Two-Person Tour Policy): "If no combination is possible that day: Contractor personally guides it, covered under Base Pay, no separate fee." The 7/24 tour fits that exactly — David condensed the day's tours to the 2hr Manchac, Michelle couldn't get her shift covered and took it out. If that Agreement is in force for her, 7/24 may be worth **$0**, not $100. It's an unsigned template though, and NKST has been through two managers since (per the LDWF thread, 2026-07-27), so her current standing is unclear.

**Recommendation:** pay $100/tour ($200), and confirm both the rate and whether she's still under the ops-contractor arrangement before the next period. Do not pay $125 on the strength of a draft note.

---

## Payout table — July 16-31

| Guide | Standard | Extended | Tours | Guests | Paid |
|---|---|---|---|---|---|
| Stephanie Lazensky | 5 | 1 | 6 | 32 | **$700** |
| River Bourne | 4 | 0 | 4 | 26 | **$400** |
| Michelle Healey | 2 | 0 | 2 | 15 | **$200** |
| Chelsea Hines | 2 | 0 | 2 | 8 | **$200** |
| Alexis Hingle | 1 | 0 | 1 | 6 | **$100** |
| | | | **15** | **87** | **$1,600** |

Paid 2026-08-02 via PayPal. Michelle's two are 7/24 9am (11 guests) and 7/31 9am (4 guests), paid at $100.

Plus 2 Bayou Kayak Rentals departures (7/30, 7/31, 3 guests total) with no crew assigned. Self-guided, no guide pay.

### Gratuity: $0.00

Checked all 41 bookings in the period against `tip_receipt`, any custom field named Gratuity, and gratuity-purpose payments. Zero.

This is a real zero, not a detection miss, and it's been verified two ways:

1. `is_gratuity_enabled` is **true** on both Manchac Swamp Wildlife and Extended Manchac, the only two tour types that ran, so guests had the option and nobody used it.
2. Running the same script over **2026-08-01** returns **$65.00** (Rachel Ryan, custom field "Gratuity" = "20%", on the 8/1 9:00am). The detector fires on a real tip, so the July zero is a true negative rather than a broken query.

Consistent with SOP Master Part 9: "Tips are yours to keep. Cash and Venmo are the most common formats." Cash and Venmo tips never touch FareHarbor and belong to the guide anyway.

**But card tips are different and need passing through.** The $65 on 8/1 was collected by FareHarbor, which means it sits in the merchant account until it's deliberately paid out to the guide. That one belongs to the Aug 1-15 period. Any period with card gratuity has to add it on top of tour fees or the guide silently loses it.

Worth noting `is_gratuity_enabled` is **false** on the Whitney Combo, Honey Island Extended, Bayou Kayak Rentals, and the fishing charter. If you ever want tips captured at checkout on those, they need switching on per item.

Pull it again for any period with:

```
node guide-gratuity.mjs neworleanskayakswamptours 2026-08-01 2026-08-15
```

---

## Three things to resolve before you pay

**1. ~~The 7/24 tour has no guide in FareHarbor.~~ RESOLVED — it was Michelle.** FareHarbor's `crew-members/` endpoint is empty for that departure (nobody was ever assigned), but Slack `#new-orleans-kayak-swamp-tours` settles it:

> **7/23 6:43pm, Michelle Healey:** "I don't think anyone besides me can pick up tomorrow since i couldn't get the shift covered. But i will take out the 9am 2.5 hour"
> **7/24 12:16pm, Michelle Healey:** "Pre and post tour log" + audio clip attached

David independently confirmed via the FareHarbor activity log showing Michelle checking guests in. Credited to her above.

Root cause worth fixing: the crew assignment never got entered when the schedule was reshuffled the night before. It happened on the largest departure of the period.

**And it's a pattern, not a one-off.** Unassigned departures in a ten-day stretch: 7/24 (11 guests, resolved to Michelle), 7/30 and 7/31 Bayou rentals (self-guided, fine), and **8/1 9:00am (10 guests, still unknown)** — which also carries a $65 card tip. If crew assignment is the payroll source of truth, it has to be filled in whenever a shift moves, or tours keep falling out of payroll. Worth asking who ran 8/1 while it's still recent.

**2. Chelsea Hines and Alexis Hingle aren't on the active guide roster.** `Guides/Guide Roster 2026 — Active` lists Chelsea under Inactive ("was in town for March 2026 only") and doesn't list Alexis at all — Alexis shows up in the July manager-agreement thread, so she may be getting the $200 management day rate instead of, or on top of, guide pay. Confirm before paying her as a guide.

**3. Nobody has a W-9. Not one guide.** `Guides/Guide Roster & Compliance Tracker 2026` states it outright: "W-9s are not collected. Compliance is via signed ICA only." And every ICA status in that table is ❓ (unverified), with 2-3 known missing.

This is a 1099 problem, not a paperwork nit. Stephanie cleared $600 in a single half-month, so she is well past the $600/year 1099-NEC threshold, and likely so are several others. No W-9 means no TIN on file, which means those 1099-NECs can't be filed at year end. `Legal/ICA Exhibit A` A-6 does require a W-9 before first payment, but it's an unsigned draft and therefore not in force.

Recommend collecting W-9s from every guide who ran a tour in 2026 before the next payout, and pulling a year-to-date total per guide to see exactly who crosses $600. The payroll script can total any date range, so a 2026-01-01 → today run gives that list.

---

## Also worth noticing

Six of the nine guides on the active roster ran **zero** tours July 16-31: Nick Napoda, Alex Wallace, Josh Smith, MJ Hicks, River Umberger, Ryan Carr. Nick ran 6 tours in the first half of July and 0 in the second half — either he stopped, or he's not being assigned.

Volume for all of July: 37 departures, 180 guests. That's thin for peak-adjacent season. Worth a look next to the same window last year.

---

## Guide confirmation texts

Send these before paying. Casual, short, one ask.

**Stephanie Lazensky** (610-850-2910)
> Hey Stephanie, closing out the 7/16-7/31 pay period. I've got you at 6 tours: 7/16 9am, 7/17 5pm, 7/19 9am, 7/26 5pm, 7/27 9am, plus the 7/28 extended. That's $700. Look right to you?

**River Bourne** (407-310-7794)
> Hey River, wrapping up 7/16-7/31 pay. I've got 4 tours for you: 7/16 5pm, 7/17 9am, 7/18 9am, 7/26 11:30am. $400 total. Sound right?

**Chelsea Hines** (no phone on file — get one)
> Hey Chelsea, closing out the second half of July. I've got you on 7/23 9am and 7/30 5pm, so $200. That match your count?

**Alexis Hingle** (alexishingle023@gmail.com)
> Hey Alexis, doing 7/16-7/31 payroll. FareHarbor has you guiding the 7/25 9am Manchac. Want to make sure that's counted as a guide tour and not rolled into the management day rate. How do you want it handled?

**Michelle Healey** (216-262-3865) — she's the only one whose rate still moves the total
> Hey Michelle, closing out 7/16-7/31. I've got you on two: the 7/24 9am you picked up when nobody could cover, and the 7/31 9am. Want to confirm you're at $100/tour so I've got the right number. Also heads up, the 7/24 never got you assigned as crew in FareHarbor, so it almost got missed.

---

*Related: [[Legal/ICA Exhibit A — Compensation & Bonus Structure]] · [[SOPs/NKST — Guide SOP Master]] · [[Guides/Guide Roster 2026 — Active]]*
