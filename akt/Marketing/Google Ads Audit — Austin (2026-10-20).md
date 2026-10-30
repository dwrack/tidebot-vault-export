# Google Ads Audit — Austin (2026-10-20)

Account: Lone Star Kayak Tour (Gravity Trails), CID 849-738-3499. This account is shared with BBK and HPB.
Window: Sep 20 – Oct 19, 2026 (last 30 days). Data was pulled from the Google Ads UI. **No account changes made.**

## Austin campaigns

| Campaign | Status | Budget | Spend/day | Cost | Conv | Value | ROAS | CPA |
|:-|:-|-:|-:|-:|-:|-:|-:|-:|
| TourPPC \| Lone Star – PMax – Local (22684341497) | Eligible | $45 | ~$40 | $1,192 | 37.0 | $4,390 | 3.68x | $32 |
| [FH] Search – Generic – Bat – Local (23641266373) | Limited by **search volume** | $30 (tROAS) | ~$14 | $433 | 12.0 | $1,519 | 3.51x | $36 |
| [FH] Search – Brand – lonestarkayaktours | **Paused** | $15 | — | $10 | 1.0 | $54 | — | — |
| **Austin total** | | | | **$1,636** | **50** | **$5,963** | **3.65x** | **$33** |

**Neither Austin campaign is budget-limited.** PMax spends ~$40 of its $45 budget, and the bat campaign spends ~$14 of $30 because it has run out of search volume. Raising either budget won't buy more traffic.

The only campaign in the account that is limited by budget is **BBK PMax**: $15/day, 3.55x ROAS, $31 CPA.

## PMax search terms by intent (visible terms only: $603 of $1,192)

| Bucket | Cost | Conv | CPA | Verdict |
|:-|-:|-:|-:|:-|
| Generic kayak ("kayaking austin", "lady bird lake kayaking", …) | $226 | 9.5 | $24 | **Best bucket.** Keep it. |
| Bat ("bat kayak tour austin", "bats in austin", …) | $196 | 2.0 | **$98** | Fat. The bat search campaign gets the same intent at $36. |
| Rental ("kayak rental austin", …) | $59 | 3.0 | $20 | Converts. Keep it. |
| Sunset / novelty (glow, neon, clear) | $44 | 1.0 | $44 | OK |
| SUP / canoe | $29 | 2.0 | $15 | Keep |
| Brand (lone star kayak tours) | $22 | 3.0 | $7 | Brand campaign is paused, so PMax is paying ~2x the CPC for brand clicks |
| Competitors (live love paddle, get up and go, congress kayaks, honey island) | $13 | 1.0 | $13 | Small. Leave it. |
| Off-area (lake travis, san antonio) | $12 | 0 | — | Negative these |

The hidden "Other search terms" cost $588 for 15.5 conversions ($38 CPA).

## Bat search campaign keywords

| Keyword | Cost | Conv | CPA |
|:-|-:|-:|-:|
| "austin kayak bats" | $161 | 3.5 | $46 |
| "bat kayak tour austin" | $51 | 2.4 | $21 |
| "kayak bat tour" | $36 | 3.1 | $12 |
| "sunset bat tour" | $15 | 2.0 | $8 |
| "kayak austin bats" | $4 | 1.0 | $4 |
| **"austin bat tour"** | **$40** | 0 | — |
| **"bat tour"** | **$25** | 0 | — |
| **"austin bats"** (464 impressions, 3.7% CTR, people looking for info) | **$23** | 0 | — |
| "austin bat kayak tour" | $22 | 0 | — |
| "kayak bats austin" | $21 | 0 | — |
| **"austin bat kayak rental"** | **$20** | 0 | — |

The bolded rows are generic bat-viewing searches, not kayak searches: $108 for 0 conversions. "Where/how to see the bats" and "bat bridge" queries are free-viewing info searches.

## Devices

| Campaign | Mobile | Desktop |
|:-|:-|:-|
| PMax | $788 / 25 conv ($32) | $397 / 11 conv ($36) |
| Bat Search | $359 / 8.2 conv (**$44**) | $63 / 3.8 conv (**$17**) |

The bat campaign uses tROAS, so manual device bid adjustments are ignored. Mobile is the weak spot for bat search.

## Location

PMax targets Austin city plus 20 mi. 99.6% of its spend falls inside Austin city, so there is no geographic leak.

## Day of week (Bat Search; it runs 7:15 AM – midnight)

| Day | Cost | Conv | CPA |
|:-|-:|-:|-:|
| Sat | $102 | 3.0 | $34 |
| Fri | $80 | 2.5 | $32 |
| Sun | $88 | 2.0 | $44 |
| Thu | $64 | 2.3 | $28 |
| Tue | $42 | 2.0 | $21 |
| **Mon** | $32 | 0.2 | **$163** |
| **Wed** | $25 | 0 | — |

Google's top bidding signals for PMax are weekday desktop 6 AM–2 PM, weekends 9 AM–5 PM, and weekdays 4–6 PM. **Hour-of-day was not pulled**: the UI breakdown doesn't render while the browser pane is hidden.

## Conversion tracking

Purchase is the only goal used by all 23 campaigns. It has 3 primary actions, the GA4 purchase events for LSKT, BBK and HPB. LSKT GA4 purchase shows 49.99 conversions and $5,963 in value, which matches the Austin total, so there is no double counting. Because all three brands share the goal, a Lone Star ad click followed by a BBK booking would credit the Lone Star campaign. That's minor, but worth splitting with campaign-level goals later.

## Other findings

- PMax has 1 asset group with "Average" ad strength. One description mentions "San Marcos River". Confirm that tour is still offered.
- 6 dead Lone Star campaigns sit paused at $0 (Lonestar, [Search] Lonestar new, Branded – Local, Industry-Specific – Local, Generic National $1/day, Generic Local $1/day).
- Biggest waste in the account isn't Austin. **Search – Houston Pedal Barge** spent $782 for 7 conversions (1.96x ROAS, $112 CPA), and most of its ads are limited by policy. Keyword "pedal boat" (broad) cost $311 at a $124 CPA. "booze cruise" (broad, $35), "party cruise" (broad, $18) and "pedal boats houston" ($34) got 0 conversions. The LSKT vault rule also says never lead with "pedal".

## Changes applied 2026-10-20 (verified live in the account)

1. **Bat Search (23641266373):** paused "austin bat tour", "bat tour", "austin bats" and "austin bat kayak rental". Added campaign negatives: boat, refuge, "where to see", "how to see". cruise, cruises, boats and riverboat were already negatives.
2. **PMax (22684341497):** added campaign negatives "lake travis", "san antonio", "things to do", "lone star kayak" and "lonestar kayak".
   - **Bat negatives were NOT added.** Google's preview estimated a 31% loss of PMax conversion value. Most PMax bat conversions sit in hidden "other" search terms, and the bat search campaign is volume-limited, so it can't absorb them.
3. **LSKT Brand (23641266361):** enabled, budget cut from $15 to $10/day, still targeting the US. Added phrase keywords "lone star kayak" and "lonestar kayak" so it catches the brand traffic PMax now blocks. Google's preview estimated that traffic at ~8% of PMax value.
4. **BBK PMax budget:** **kept at $15/day per Michael.** The $25 change was never saved.
5. **HPB Search (20315555269):** paused "pedal boat" (broad), "booze cruise" (broad), "party cruise" (broad) and "pedal boats houston" (phrase). Added "pedal boat" (phrase), which was Pending review at the time of writing. An earlier Oct 15 cleanup had paused other keywords in this campaign.

**Watch items:**
- HPB still has broad "water pedal boat", "pedal boat rentals", "pedal boat rentals near me", "pedal boating near me" and "houston booze cruise" running. They had $0 spend in the last 30 days, but they target people looking to rent a pedal boat.
- Re-check the brand campaign and PMax after about a week, around Oct 27.
- Pause bat search on Oct 31.

## Paused campaign review (2026-10-20)

**Question:** were any paused campaigns once held back by budget and worth relaunching?

**Method:** compared all-time (Feb 2017 – Oct 20, 2026) against 2026 YTD. Columns used: ROAS (conv. value / cost), CPA, Search lost IS (budget) and Search lost IS (rank). Pause dates come from change history.

| Paused campaign | When it ran | Cost | Conv | ROAS | CPA | IS lost to budget | Verdict |
|:-|:-|-:|-:|-:|-:|-:|:-|
| **[FH] Brand – houstonpedalbarge** | Mar 9–23, 2026 (Michael paused it Mar 23) | $551 | 12.5 | **6.6x** | $44 | **39%** | Throttled and profitable, but it overlaps HPB Search, which already owns "houston pedal barge" (8x). All ads are limited by policy. Test it only if HPB Search stops covering brand terms. |
| **[FH] Generic – buffalobayoukayak – National** | 2026 | $81 | 9 | **11.5x** | $9 | **30%** | **Best relaunch candidate.** Small sample, cheap test. |
| **[FH] Generic – lonestarkayaktours – Bat – National** | 2026 | $525 | 16.7 | 3.5x | $31 | 12% (38% to rank) | Seasonal. Relaunch with bat season in Mar 2027, not now (the season ends Oct 31). |
| [FH] Generic – houstonpedalbarge – Local | Mar 2026 | $275 | 2 | 3.6x | $138 | 43% | Too few conversions; $138 CPA |
| [FH] Generic – houstonpedalbarge – National | 2026 | $133 | 1.5 | 2.3x | $87 | 33% | No |
| Lonestar (tCPA, $50/day) | before 2026 | $53,831 | 551 | 1.27x | $98 | **65%** | Heavily throttled but unprofitable. Older conversion setup. No. |
| [Search] Lonestar – new | before 2026 | $18,362 | 244 | 1.95x | $75 | 16% | No |
| Houston Pedal Barge (old) | 2021–23 | $26,177 | 73 | 0.65x | $359 | 17% | No |
| Houston Kayak | 2022–24 | $1,703 | 0 | 0 | — | 67% | No |
| TourPPC Lone Star – Industry-Specific | before 2026 | $1,941 | 19 | 1.15x | $102 | 29% | No |
| TourPPC BBK – Industry-Specific | ≤2026 ($81 in 2026, 0 conv) | $1,849 | 49 | 2.5x | $38 | 26% | No; [FH] BBK Generic Local covers this at 7.3x |
| TourPPC Lone Star Branded / BBK Branded | before 2026 | $328 / $535 | 11 / 70 | 4.4x / 8.7x | | <2% | Replaced by the [FH] brand campaigns |
| [FH] Generic – lonestarkayaktours – Local / National | never spent | $0 | — | — | — | — | Empty shells ($1/day, all ads paused) |
| ATX Pedal Barge PMax | — | $4,123 | 1 | 0.01x | — | — | No (all asset groups disapproved) |

**Context:** of the live campaigns, only BBK PMax is "Limited by budget" now (kept at $15 per Michael). [FH] BBK Brand lost 15% IS to budget YTD but is volume-limited in the last 30 days.

**Applied 2026-10-20 (Michael approved):** relaunched [FH] Search – Generic – buffalobayoukayak – National (campaign 23641266229) as a test.
- **Budget:** its shared budget "buffalobayoukayak - Max Clicks" (used only by this campaign) went from $24 to $10/day.
- **Bidding:** Maximize clicks. **Targeting:** United States.
- **Keywords:** paused "kayaks for sale houston" and "kayak for sale houston tx" before launch. Those searchers are buying a kayak, not booking a tour.
- **What's live:** 7 phrase keywords in "BBK - Kayak Tours" are eligible. The 2 "BBK - Bat Bridge" keywords show low search volume, and the "BBK - Paddle" ad group was already paused.
- **Watch for:** overlap with [FH] BBK Generic Local on Houston-area searches, and Max-clicks CPCs.

**Original recommendation:**
- Relaunch [FH] BBK Generic National as a $10/day test.
- Schedule [FH] Bat National for March 2027.
- Leave everything else paused.

## Original proposals

1. **Bat Search:** pause the zero-conversion generic keywords "austin bat tour", "bat tour", "austin bats" and "austin bat kayak rental" (~$108/30 days). Add negatives: "where to see", "how to see", "refuge", "boat", "cruise".
2. **PMax:** add negatives "lake travis", "san antonio", "things to do". Add bat-term negatives to PMax so bat intent goes to the Search campaign ($36 vs $98 CPA). This only makes sense while the bat campaign is live.
3. **Brand:** re-enable the LSKT Brand search campaign at $5–10/day and add a brand exclusion to PMax.
4. **Budget:** raise BBK PMax from $15 to $25/day, since it's the only campaign limited by budget. Leave the Austin budgets as they are.
5. **HPB Search:** pause "booze cruise" and "party cruise" (broad) and "pedal boats houston". Switch "pedal boat" from broad to phrase match.
6. **Season:** wind the bat campaign down around Oct 25 and pause it Oct 31, per the 10/15 plan. After that, move the bat budget into PMax only if PMax becomes budget-limited.

## One-week check (2026-10-27)

Pulled from the Google Ads UI (Michael's Chrome) for **Oct 20–26, 2026**, compared with **Oct 13–19**. Prior-week values are back-calculated from the UI's % change column, so they may be off by a cent or a rounding step. Nothing in the account was changed during this check.

| Campaign | Status / flags (now) | Cost | Conv | Value | ROAS | CPA |
|:-|:-|-:|-:|-:|-:|-:|
| PMax (Lone Star) | Eligible; 8.9% IS lost to budget (was ~17%) | $321 → **$307** | 9.0 → **10.0** | $1,066 → **$975** (−8.6%) | 3.32 → **3.17** | $36 → **$31** |
| Bat search | Eligible (Limited by search volume) | $116 → **$56** | 2.0 → **1.0** | $162 → **$217** | 1.40 → **3.84** | $58 → **$56** |
| Brand (LSKT) | Eligible, serving | $0 → **$2.18** | 0 → **0** | $0 → **$0** | — | — |
| HPB search | Eligible (Limited: most ads limited by policy) | $64 → **$48** | 3.0 → **1.0** | $676 → **$302** | 10.5 → **6.28** | $21 → **$48** |
| BBK National test | **Paused** (by Michael, Oct 26 9:40 AM) | $0 → **$58.25** | 0 → **0** | $0 → **$0** | 0 | — |
| BBK Generic Local | Eligible (Limited by search volume) | $32 → **$21** | 3.5 → **2.0** | $254 → **$260** | 8.0 → **12.5** | $9 → **$10** |
| BBK PMax (for reference) | Limited by budget ($15/day) | $107 → **$85** | 5.7 → **2.0** | $717 → **$1,125** | 6.7 → **13.2** | $19 → **$43** |

All of these are 1–10 conversions per week, so week-to-week swings are mostly noise.

### Findings
- **Brand is serving, but at very low volume.** It had 18 impressions, 6 clicks, $2.18 spend, a **$0.36 CPC** and 0 conversions. Search terms were "lone star kayak tours" (4 clicks, $1.84), "lonestar kayak tours" (2 clicks, $0.34), "lone star kayak" and "lone star kayak tours reviews" (impressions only). It is far from its $10/day budget.
- **Brand terms in PMax are mostly gone.** One click on "lone star kayak tours" still went through PMax ($1.82 CPC, five times Brand's CPC), and "lone star bat tour austin" got 1 click ($0.45). Check that the PMax negative list holds the "lone star kayak" / "lonestar kayak" phrase negatives as intended.
- **PMax value fell 8.6%, inside the ~10% threshold.** Conversions rose from 9 to 10, and CPA improved from $36 to $31. Brand did not pick up the lost value (0 conversions), but the drop is small and within noise. IS lost to budget fell from ~17% to 8.9%. The largest zero-conversion PMax terms were "austin kayaking" ($22) and "bat kayak tour austin" ($18), both on-intent.
- **Bat search:** all 4 keywords are still **Paused** ("austin bat tour", "bat tour", "austin bats", "austin bat kayak rental"). "austin bat tour" spent $2.60 on Oct 20, before the noon pause. No new search term reached $10 with 0 conversions; the largest was "kayak bat tour austin" at $5.68. The keyword "austin kayak bats" spent **$32.45 with 0 conversions**, mostly on hidden search terms. Spend halved to $8/day, and ROAS rose from 1.4x to 3.8x on 1 conversion. Change history also shows a "Budget changed" entry on this campaign on Oct 26 at 9:42 AM by Michael. The budget still shows $30/day, and I did not open the entry's detail.
- **HPB "pedal boat" phrase** is **Eligible**, which means it is approved, but it got only 3 impressions and 0 clicks, so there is **no CPA yet** to compare with the old broad keyword's $124. The old broad "pedal boat", "booze cruise", "party cruise" and "pedal boats houston" are all Paused. Most HPB spend went to "houston pedal barge" (broad): $38.81 for 1 conversion, $302 value. Small leftovers: "houston booze cruise" ($2.02) and "booze cruise kemah" ($0.34, out of area). On Oct 26, Michael added a new ad group, "Party Barge – No Alcohol Test", with new RSAs and target ROAS changes, plus a target ROAS cut on the "Pedal boat" ad group. Judge HPB again after those changes have a week of data.
- **BBK National test failed, and Michael already paused it on Oct 26.** It spent $58.25 for 21 clicks at a **$2.77 CPC** with **0 conversions**, 11.8% IS lost to budget. Junk or off-target terms: "kayak the woodlands waterway" ($5.05, different area), "bumper boats and kayaks at discovery green" ($4.29) and "kayaking discovery green" ($2.95), which point to a different attraction. Overlap terms: "kayaking houston" ($4.25), "kayak houston" ($3.09), "kayaking near houston" ($2.31) and "houston kayak tours" ($1.61), all Houston-local searches that BBK Generic Local already covers.
- **Possible cannibalization:** BBK Generic Local's conversions fell from 3.5 to 2.0 and its cost from $32 to $21 while National was running, but its value held at $260. That fits mild overlap, though the sample is too small to prove it.

### Reminder
**Bat season ends Oct 31.** Pause "[FH] Search – Generic – Shname_lonestarkayaktours – Bat – Local" then, per the 10/15 plan.

### Recommended changes (awaiting Michael's approval; none applied)
1. **Pause Bat search on Oct 31.** Optionally pause the "austin kayak bats" keyword now ($32, 0 conversions this week).
2. **Leave BBK National paused.** Do not relaunch it as is. Any retest should exclude Houston-local terms, or add negatives (woodlands, discovery green, bumper boats), so it stops overlapping BBK Local.
3. **Brand:** no change. Keep it at $10/day and review after 30 days.
4. **PMax:** no change. Only check that the brand phrase negatives cover "lone star kayak tours", since one click still went through.
5. **HPB:** no keyword changes this week. Let Michael's Oct 26 ad group and target ROAS changes collect data, then check the "pedal boat" phrase again around Nov 3. Optional: add "kemah" as a negative.
6. **BBK PMax:** keep it at $15/day (ROAS 13x, but only 2 conversions; no strong signal to raise it).
