# Guide Payroll — August 1-15, 2026

> **STATUS: READY TO PAY.** Pulled 2026-08-17. **$1,175 in tour pay across five guides, plus $130 to Alex Wallace under the $5/review bounty. $1,305 total.** Every rate and assignment is confirmed. Pay sheet with emails is below.
>
> **⚠️ Read the bounty section first.** Paying per review violates Google's policies and puts a ~1,365-review listing at risk. The $130 is not the problem; the program is.
>
> David confirmed 2026-08-17 that the unassigned 8/1 9:00am tour was **River Bourne**, closing both the missing tour credit and the stranded $65 card tip.
>
> **Read the review section before paying anything review-linked.** 26 new Google reviews landed in this period and all 26 name a guide who ran zero tours in it.

*Bi-monthly cycle: 1st-15th paid the 15th. Rates confirmed at $100 standard / $200 extended — see [[Operations/Guide Payroll — July 16-31 2026]] for how that was back-solved.*

**Sources**

```
cd ~/Projects/fareharbor-brief
node guide-payroll.mjs  neworleanskayakswamptours 2026-08-01 2026-08-15
node guide-gratuity.mjs neworleanskayakswamptours 2026-08-01 2026-08-15
```

Reviews via the `gbp` MCP, location `10129422728201342552` (New Orleans Kayak Swamp Tours), 50 most recent reviews covering 2026-04-24 → 2026-08-13.

> **Tooling note:** both scripts were dead on arrival this run — `page.goto` on the FareHarbor dashboard blew past its 30s default and threw. Fixed in place by switching to `waitUntil: 'commit'` with a 120s timeout. Only the session cookie is needed, not a full dashboard render. Both scripts run clean now.

---

## Payout table — Aug 1-15

| Guide | Standard | Extended | Tours | Guests | Rate | Reviews 8/1-8/15 | Tips | Owed |
|---|---|---|---|---|---|---|---|---|
| River Bourne | 3 | 0 | 3 | 25 | $100 | 0 | $65 | **$365** |
| Chelsea Hines | 1 | 2 | 3 | 12 | $110 / $200 ext | 0 | — | **$510** |
| Stephanie Lazensky | 1 | 0 | 1 | 3 | $100 | 0 | — | **$100** |
| Alexis Hingle | 1 | 0 | 1 | 11 | $100 | 0 | — | **$100** |
| Abbie Marks | 1 | 0 | 1 | 5 | $100 | 0 | — | **$100** |
| | | | **9** | **56** | | **0** | **$65** | **$1,175** |

All rates confirmed by David 2026-08-17. Extended is a flat $200 for everyone regardless of standard rate, so Chelsea is $110 + (2 × $200) = $510.

### 💵 Pay sheet — send these

| Guide | Email | **Send** |
|---|---|---|
| Chelsea Hines | Chelseabrooke503@gmail.com | **$510** |
| River Bourne | riverbourne.here@gmail.com | **$365** *(incl. $65 tip)* |
| Stephanie Lazensky | slazensky@gmail.com | **$100** |
| Alexis Hingle | alexishingle023@gmail.com | **$100** |
| Abbie Marks | abbiemarkswriting@gmail.com | **$100** |
| Alex Wallace | martinezwallace@gmail.com | **$130** *(26 reviews × $5, no tour pay)* |
| | | **$1,305** |

Michelle ran no tours this period and is owed nothing.

**No back-pay in this run.** David settled Chelsea's $20 and Michelle's $50 during the last pay period, so the 7/16-31 rate gap is already closed. Don't send it twice.

Emails pulled from FareHarbor user records 2026-08-17, so they're current.

### Rate card — corrected 2026-08-17

The July close assumed a flat $100 across the board. That was wrong. Rates are per-guide:

| Guide | Standard | Extended | Source |
|---|---|---|---|
| Michelle Healey | **$125** | ? | David, 2026-08-17 |
| Chelsea Hines | **$110** | ? | David, 2026-08-17 |
| Stephanie Lazensky | $100 | $200 | Back-solved from her $600 payout for 7/1-7/15 |
| River Bourne | $100 | ? | David, 2026-08-02 |
| Alexis Hingle | ? | ? | never confirmed |
| Abbie Marks | ? | ? | never confirmed |
| Nick Napoda | ? | ? | never confirmed (the ICA draft claimed $125) |

### The July 16-31 rate gap — already settled

That period was paid 2026-08-02 at a flat $100/tour, on the conclusion that the $125 figure in the ICA draft had no basis. David has since confirmed it does, and **he already paid the difference during that same pay period**: Michelle +$50, Chelsea +$20. Nothing carries into August. Real 7/16-31 total was $1,670, not the $1,600 recorded in that doc.

The July doc's audit section on the "$125 claim" is superseded. Its reasoning was sound given what was on paper; the paper was incomplete. The real lesson: **there is no written rate card anywhere in the vault, so payroll keeps getting reconstructed from drafts and memory.** `Legal/ICA Exhibit A` proposes a flat $110 and is unsigned. One signed sheet of per-guide rates ends this recurring problem, and it also fixes the year-end 1099 totals, which are currently only as good as whichever doc you read last.

Not one guide who actually ran a tour this period was named in a single review. See the review section — all 26 went to Alex Wallace, who ran nothing.

### Every departure, for checking

| Date | Time | Tour | Guests | Crew |
|---|---|---|---|---|
| 8/01 | 09:00 | Manchac Standard | 10 | River Bourne *(confirmed by David 8/17; never entered in FareHarbor)* |
| 8/04 | 09:00 | Manchac Standard | 4 | River Bourne |
| 8/07 | 08:30 | Manchac Extended | 4 | Chelsea Hines |
| 8/07 | 09:00 | Manchac Standard | 11 | Alexis Hingle |
| 8/08 | 08:30 | Manchac Extended | 2 | Chelsea Hines |
| 8/08 | 09:00 | Manchac Standard | 11 | River Bourne |
| 8/09 | 09:00 | Manchac Standard | 3 | Stephanie Lazensky |
| 8/12 | 17:00 | Manchac Standard | 5 | Abbie Marks |
| 8/15 | 09:00 | Manchac Standard | 6 | Chelsea Hines |

Plus 8 non-guided line items, 16 guests, no crew and no guide pay: six Bayou Kayak Rentals (8/4 ×2, 8/7, 8/9, 8/12, 8/14), one Gift Card (8/2), one Unlimited Monthly Pass (8/5).

The 8:30 starts on 8/7 and 8/8 are the heat protocol landing — see [[project_heat_early_start_protocol]].

---

## Gratuity: $65.00 → River Bourne

All 26 bookings in the period checked against `tip_receipt`, any custom field named Gratuity, and gratuity-purpose payments.

| Departure | Guest | Capture | Amount | Goes to |
|---|---|---|---|---|
| 8/01 9:00am | Rachel Ryan | custom field "Gratuity" = 20% | **$65.00** | River Bourne |

Every other departure: $0.00.

This is the same $65 flagged as carried forward out of the July 16-31 close, and it's now resolved — David confirmed 8/17 that River ran the 8/1 tour. It's a card tip, so FareHarbor is holding it in the merchant account; it does not reach him unless it's deliberately paid out on top of the tour fee. **Add it to River's payment, don't assume he got it.**

Cash and Venmo tips never touch FareHarbor and stay with the guide, per SOP Master Part 9.

---

## 💸 The $5/review bounty — $130 to Alex, and a much bigger problem

David confirmed 2026-08-17 that he announced a **$5 per review** bounty in the guide Slack channel: any review naming a guide earns that guide $5. (The post itself couldn't be pulled — the Slack bot isn't a member of the private guide channel, so `conversations.info` on C0ATU09TDTP returns `channel_not_found`. Terms here are David's own restatement.)

**Alex Wallace: 26 reviews × $5 = $130**, on top of $0 in tour pay.

This reframes everything below. The earlier read in this doc — that no incentive existed — was wrong. There was one, and the review pattern is exactly what that incentive produces:

| | |
|---|---|
| Reviews, 14 weeks 4/24-7/31 | 24 |
| Reviews, 7/15 → 8/5 | **0** |
| Reviews, 8/6-8/13 | **26, all naming one guide** |

That's not a mystery anymore. That's a bounty being announced and one person working it hard.

### The real exposure isn't $130

**Paying for reviews violates Google's review policies.** Google's prohibited-content rules for Maps bar incentivized reviews outright: you cannot offer money, discounts, products, or anything of value in exchange for reviews. Enforcement runs from silently stripping the reviews, to demoting the listing, to disabling reviews on the profile entirely.

NKST has roughly **1,365 lifetime reviews.** That is the single most valuable asset this business owns. Every dollar of Google Ads spend, every SEO push, every map-pack ranking routes through that profile. A $5 bounty puts all of it on the table.

The 8/6-8/13 cluster is also close to the worst-case fact pattern for an automated review-spam filter: 26 five-star reviews in 8 days on a listing averaging under two a week, heavily repeating one name, several using an unnatural full-name construction, and reviewer display names that include a well-known NFL broadcaster.

### Recommendation

1. **Pay the $130.** David announced the terms publicly and Alex acted on them. Refusing now, before any conversation, means reneging on a stated deal in front of the crew — far more expensive in trust than $130. Pay it, and separate the money question from the conduct question entirely.
2. **End the bounty immediately and say why**, in the channel, in plain terms: it's against Google's rules and it risks the listing. Own it as a mistake in program design rather than framing it as anyone's misconduct.
3. **Then have the 1:1 with Alex** about whether he's been guiding unassigned shifts, which is still a genuinely open question and still might mean NKST owes him tour pay.
4. **Replace it with something legal.** Bounties on reviews are out. A bonus on *tours run*, on guest volume, or on the affiliate link (10% on real bookings, already built) are all fine, because they pay for work rather than for reviews.

> **Do not** ask anyone to delete the existing reviews. Mass deletion is its own spam signal, and if these are genuine guests it destroys real ones. Stop the incentive and let the profile settle.

---

## 🚩 26 reviews, all naming a guide who ran no tours

26 new Google reviews landed 8/6-8/13. All 5-star. **All 26 name Alex Wallace**, several by full name.

What FareHarbor says about Alex Wallace (username `alex`), May 1 → Aug 16:

| | |
|---|---|
| Tours in Aug 1-15 | **0** |
| Tours since May 1 | **2** (5/17, 5/24) |
| Guests served since May 1 | **13** |
| Last assigned departure | **2026-05-24** |

He is a real guide with a real FareHarbor account and he is on the active roster (Sundays only). He just hasn't guided anything in almost three months.

### Named-guide mentions, all 50 reviews (2026-04-24 → 2026-08-13)

| Guide | In period 8/1-8/15 | Since 4/24 | Tours since 5/1 | Last named |
|---|---|---|---|---|
| **Alex Wallace** | **26** | **27** | **2** | 8/13 |
| Stephanie Lazensky | 0 | 6 | 26 | 7/11 |
| Nick Napoda | 0 | 6 | 40 | 7/05 |
| Ryan Carr | 0 | 1 | 9 | 7/04 |
| Michelle Healey | 0 | 1 | 14 | 6/14 |
| MJ Hicks | 0 | 1 | 2 | 4/29 |
| Josh Smith | 0 | 1 | 16 | 4/24 |
| **River Bourne** | **0** | **0** | 9 | never |
| **Chelsea Hines** | **0** | **0** | 10 | never |
| **Alexis Hingle** | **0** | **0** | 6 | never |
| **Abbie Marks** | **0** | **0** | 4 | never |

The four guides carrying August have never been named in a review in this whole window, and River has run 9 tours since May. Meanwhile Alex has 27 mentions off 2 tours. Stephanie and Nick are the only guides whose mention counts track their tour volume the way you'd expect.

*Method note: a raw text search also flagged a "River" hit on 5/10, but that review reads "we had the river to ourselves" — the waterway, not the guide. Excluded. Only the 50 most recent reviews were pulled; NKST has ~1,365 lifetime, so these are trailing-window counts, not all-time.*

### Zero reviews in the period went to anyone else

Checked 8/17. On the NKST listing, **26 of 26** in-period reviews name Alex. All five stars, all with written text, no star-only ratings. There is no remainder.

Sibling listings on the same GBP account, same window:

| Listing | Reviews 8/1-8/15 | Newest review |
|---|---|---|
| New Orleans Kayak Swamp Tours | 26 (all Alex) | 8/13/26 |
| Honey Island Swamp Kayak Tours | 1 — **not ours, misposted** | 8/09/26 |
| Crescent City Kayak - Swamp Tours | 0 | 4/01/24 |
| Admire New Orleans | 0 | 9/04/25 |

The Honey Island one (8/9, Maxime Beckrich, "Jess" guiding and "Mike" on hotel pickup) **is not ours at all.** David confirmed 2026-08-17 that this guest paddled with a different operator and posted the review on our page by mistake. Jess doesn't appear in the NKST FareHarbor user list, which fits.

**That leaves zero.** Across every listing on the account, there was not one legitimate review of an NKST tour in the first half of August that named anybody other than Alex Wallace. The 26 are the entire review output for the period, and every one credits a guide who ran no tours.

Two follow-ups on the misposted review:

1. **Report it to Google for removal.** It's a review of another business sitting on our profile. It's 5 stars so there's no rush, but it's also a factual misattribution and it inflates a count we may need to defend if the Alex cluster gets scrutinized.
2. **It's the best argument in the vault for the Reddit and Facebook-group push.** That guest planned his entire New Orleans day off a Reddit thread, rode Amtrak across the country, and booked whoever showed up in that thread. It wasn't us. Somebody else's comment took that booking. It's now the anchor example in the guide Slack report.

**Why this doesn't add up:**

- 24 reviews arrived in the 14 weeks from 4/24 to 7/31. Then 26 in 8 days.
- There were **zero** reviews between 7/15 and 8/5, then the burst.
- Only ~40 guests went out on guided tours in the 8/4-8/13 window the reviews could plausibly refer to. 26 reviews against 40 guests is a 65% review rate.
- Not one of the five guides who actually ran tours in this period is named in a single review.
- Six reviews use the full name "Alex Wallace," which guests almost never know. Several read as instructions rather than experiences: "Ask for Alex Wallace for your tour guide," "Get him before he is famous."
- The reviewer names include Jay Jones, Casey Jones, katy jones, and Shannon Sharpe.

**What to do:** don't pay any review-linked bonus on these, and don't fold them into a guide scorecard until it's resolved. Ask Alex directly and without accusation — he may have been guiding under someone else's crew assignment, or covering shifts nobody entered, in which case the payroll gap is the real story and he's owed money. If instead these were solicited from people who didn't take a tour, Google's spam filter tends to strip clusters like this retroactively, which would drop the review count and could put the listing at risk.

Either answer changes what gets paid. Worth a phone call today while it's recent.

---

## Roster is out of date and it's costing accuracy

`Guides/Guide Roster 2026 — Active` was last touched in April. Against who actually guided:

| Person | Roster says | Reality Aug 1-15 |
|---|---|---|
| Chelsea Hines | **Inactive** — "in town for March 2026 only" | Top guide, 3 tours, $500 |
| Alexis Hingle | Not listed at all | 1 tour, 11 guests |
| Abbie Marks | Not listed ("Abbey from Marina" is a *different* FareHarbor user, `abbey` / Abbey Johnson) | 1 tour, 5 guests |
| Nick Napoda | Full-time, 5-6 tours/week | **0 tours.** 40 since May 1, then nothing after 7/15 |
| Alex Wallace | Active, Sundays | 0 tours, last one 5/24 |
| Josh Smith, MJ Hicks, River Umberger, Ryan Carr, Michelle Healey | Active | 0 tours |

Nick going from top guide to zero mid-July is the one worth asking about. Either he left, or he stopped getting assigned.

Alexis Hingle also still has the open question from July: she may be on the $200 management day rate, so confirm before paying her $100 as a guide.

---

## Still open from July, still not done

**W-9s.** Nobody has one. Chelsea Hines is at $700 across the last two periods and Stephanie is at $1,400 — both well past the $600 1099-NEC threshold with no TIN on file. Run `guide-payroll.mjs neworleanskayakswamptours 2026-01-01 2026-08-17` for a year-to-date list of who crosses it.

**Crew assignment hygiene.** 8/1 makes three guided departures in a month that ran with nobody assigned, and both of the sizeable ones needed David's memory to recover — 7/24 was 11 guests (Michelle), 8/1 was 10 (River). Crew assignment is the payroll source of truth; if it isn't filled in when a shift moves, tours fall out of payroll and card tips get stranded. Two for two on the biggest departures is not a coincidence, it's what happens when the schedule gets reshuffled last minute.

---

## Confirmation texts

Send before paying. Short, casual, one ask.

**Chelsea Hines** (no phone on file — still)
> Hey Chelsea, closing out 8/1-8/15. I've got you on three: the 8/7 and 8/8 extendeds plus the 8/15 9am. That's $500. Match your count?

**River Bourne** (407-310-7794)
> Hey River, doing the first-half-of-August payroll. Got you on three: 8/1 9am, 8/4 9am, 8/8 9am. That's $300, plus a $65 card tip from the 8/1 group that FareHarbor was holding. $365 total. Sound right?

**Stephanie Lazensky** (610-850-2910)
> Hey Stephanie, closing out 8/1-8/15. Just the one for you, 8/9 9am, $100. Sound right?

**Alexis Hingle** (alexishingle023@gmail.com)
> Hey Alexis, wrapping up 8/1-8/15. FareHarbor has you on the 8/7 9am Manchac. Same question as last month — do you want that as a $100 guide tour or is it covered under the day rate?

**Abbie Marks** (no contact on file — get one)
> Hey Abbie, doing payroll for the first half of August. I've got you on the 8/12 5pm Manchac, $100. That right?

**Alex Wallace** (401-241-7585) — call, don't text
> Ask what he's been running lately. FareHarbor has him at nothing since 5/24, but a couple dozen reviews came in this month with his name on them. Give him room to explain before drawing a conclusion.

---

*Related: [[Operations/Guide Payroll — July 16-31 2026]] · [[Guides/Guide Roster 2026 — Active]] · [[Legal/ICA Exhibit A — Compensation & Bonus Structure]] · [[SOPs/NKST — Guide SOP Master]]*
