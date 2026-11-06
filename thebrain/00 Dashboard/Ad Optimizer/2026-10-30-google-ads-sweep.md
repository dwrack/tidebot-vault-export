# Google Ads Sweep — Thu Oct 30, 2026 (DIAGNOSE + PROPOSE only)

Read-only run across all 5 live accounts. **Nothing was applied.** Tick `- [x]` on anything you want and say so; each item maps to one MCP call. Money-movers are in block B. Daily spend recap is in the Monday optimizer file and the ad report, not repeated here.

## Scoreboard (verified live 2026-10-30)

| Account | Business | Spend 7d | ROAS 7d | ROAS 30d | Biggest leak |
|---|---|---|---|---|---|
| 4378232023 | NPB (NKST/Admire/Bike Bar all paused) | $1,009 | 2.37x | 3.73x | NPB National: $620 for $652 value since 10/21 (1.05x) |
| 8497383499 | LSKT + BBK + HPB | $600 | 4.04x | 4.08x | LSKT PMax $163, 0 conv this week (bat season ending) |
| 2372234368 | Ebb & Ember | $199 | 6.00x | 3.41x | "sauna near me" phrase/broad $69, 0 conv (exact converts) |
| 8672151991 | DCKT | $0 | n/a | n/a | None. Both campaigns hit a scheduled END DATE 9/7 (primary_status CAMPAIGN_ENDED). Not billing, not broken. |
| 2986009791 | HPB solo | $0 | n/a | n/a | None. PMax paused 9/18 on purpose (loop C-2). |

**Active waste over $50/wk:** NPB National (~$300/wk at the post-10/21 rate), NPB zero-conv keywords (~$115/wk), LSKT PMax + Bat search (~$60/wk this week, 0 conv).

---

## 4378232023 — NOLA (owner: Michael Fischer, in-house)

Michael touched this account 10/27 and 10/29 (criterion status x29 rows, National budget x2). Check his change list in the UI before applying anything in A-1..A-4; some may already be done.

What happened to NPB National (23480870878, $90/day, Max Conv Value, no tROAS):
- 10/16-10/20: $262 spend, 12 conv, $5,320 value (20x)
- 10/21-10/29: $620 spend, 5.9 conv, $652 value (1.05x), with $98-111/day on 10/19, 10/26, 10/28
- Local (23480870632) and PMax (24184656153, nolapartybarges.com) still convert, so tracking is fine. National is just spending its whole budget into a dead week.
- Sales-Performance Max-12 is NPB (asset group final URL nolapartybarges.com). 30d 5.54x, 7d 2.09x.

### A. Safe
- [ ] **A-1** Negative "airboat" (PHRASE) on NPB National + Local. "airboat tours new orleans" $13/30d, 0 conv, NPB has no airboats. -> `ads_mutate` campaignCriteria create, negative, PHRASE. expected: ~$13/mo saved.
- [ ] **A-2** Negative "trailer" (PHRASE) on NPB National + Local. "party trailer new orleans" $28/30d, 2 clicks at $14 CPC, 0 conv. -> `ads_mutate` campaignCriteria create. expected: ~$28/mo saved.
- [ ] **A-3** Negative "city park" (PHRASE) on NPB National + Local. "city park activities" $13/30d, 0 conv. -> `ads_mutate` campaignCriteria create. expected: ~$13/mo saved.
- [ ] **A-4** Pause 5 zero-conv NPB keywords (30d, $325 total): "booze cruise new orleans" PHRASE in Party ad group ($104, 0 conv; the Local copy of the same keyword converts, leave that one), "nola booze cruise" EXACT ($63, PHRASE version converts 9.2x, keep PHRASE), "party barge boats" EXACT ($56), "barge new orleans" PHRASE ($56), "new orleans party cruise" PHRASE ($47). -> adGroupCriteria update status PAUSED via `ads_mutate`. expected: ~$75/wk saved, no conv loss on 30d evidence.
- [ ] **A-5** Fix NKST conversion tracking: set "kayaknola - GA4 (web) purchase" to include_in_conversions_metric = true. NKST's only counted purchase action was REMOVED, so NKST campaigns structurally show 0 conv ($588 spent in Oct before Michael paused them). Needed before NKST is ever turned back on. -> `ads_mutate` conversionAction update. expected: NKST campaigns can be bid and graded on purchases.
- [ ] **A-6** Same for Admire: "admirenola.com (web) purchase" include_in_conversions_metric = true (currently enabled but not counted). -> `ads_mutate` conversionAction update.
- Google recs: 2x RESPONSIVE_SEARCH_AD on National, SEARCH_PARTNERS_OPT_IN on Local, USE_BROAD_MATCH on Local, 4x LEAD_FORM_ASSET, 2x DISPLAY_EXPANSION. Recommend: ignore all. Broad match and display expansion would widen a campaign that is already overspending; lead forms do not fit a booking funnel.

### B. Moves money — review carefully
- [ ] **B-1 (recommended)** Set Target ROAS 4.0 on NPB National (23480870878). Current: Max Conv Value, no target. 30d ROAS 4.24x, 7d 0.82x. With no target, Google spends the full $90 regardless of returns. -> `ads_set_target_roas` validateOnly first, then real. Rollback: remove target. expected: spend drops on dead days, 30d ROAS back above 4x. Alternative if Michael prefers a budget lever: cut $90 -> $55/day (`ads_mutate` campaignBudgets, prior 90.0).
- [ ] **B-2** Decline Google's CAMPAIGN_BUDGET rec on National ($90 -> $99). Raising the budget on a campaign running 1x this week is the wrong direction. No call needed, just do not apply.
- [ ] **B-3** Hold PMax Sales-PM-12 budget at $52 (Google rec says $63). 7d 2.09x, 30d 5.54x. Revisit after the Halloween/early Nov weekend data lands. No call.

---

## 8497383499 — LSKT / BBK / HPB (shared)

Weekly trend (cost / conv / value):
- LSKT PMax 22684341497 ($37.50/day): 9/28 $318/6/$773, 10/5 $310/15.5/$1,819, 10/12 $311/6/$677, 10/19 $297/13/$1,364, 10/26-29 $163/0/$0. Budget-lost 13%.
- LSKT Bat search 23641266373 ($30/day): $171 -> $121 -> $49 -> $14 this week, 0 conv this week. Rank-lost 80%. Zero-conv terms are bridge-bat-viewing intent ("austin bat tour", "austin bats", "bat tour"), not kayak.
- BBK PMax 22706227845 ($15/day): 30d 7.11x, 7d 11.6x, budget-lost 10.3%. Google has a FORECASTING_CAMPAIGN_BUDGET rec on it.
- HPB Search 20315555269 ($42/day): 30d 3.33x, 7d 3.87x, rank-lost 84%. Pedal boat ad group (tROAS override 3.0 from C-5) 4.04x on $301. "Party Barge - No Alcohol Test" ad group $30/30d, 0 conv. Booze cruise ad group $33/30d, 0.5 conv.
- AKT: no campaigns in this account. The "Bat Local" campaign points at lonestarkayaktours.com, so it is LSKT, not AKT.

### A. Safe
- [ ] **A-7** Pause 3 LSKT bat keywords, 0 conv 30d: "austin bat tour" PHRASE ($42, QS8), "austin bats" PHRASE ($23, QS5), "bat tour" PHRASE ($18). Kayak-intent bat keywords ("kayak bat tour", "austin kayak bats") keep converting, leave them. -> `ads_mutate` adGroupCriteria status PAUSED. expected: ~$20/wk saved.
- [ ] **A-8** Pause HPB ad group "Party Barge - No Alcohol Test" (202554367618): $30/30d, 0 conv, "party boat houston" PHRASE $29 0 conv. -> `ads_set_ad_group_status` PAUSED. expected: ~$7/wk saved. Brand terms "houston party barge"/"pedal barge houston" sit in other groups and are untouched.
- [ ] **A-9** Pause HPB keyword "booze cruise" BROAD in Booze cruise ad group ($20/30d, 24 clicks, 0 conv). The PHRASE/brand paths still cover it. -> `ads_mutate` adGroupCriteria PAUSED.
- [ ] **A-10** Google IMPROVE_PERFORMANCE_MAX_AD_STRENGTH recs on both PMax campaigns (LSKT 22684341497, BBK 22706227845): review asset suggestions in the UI, apply only if copy passes the brand check (no "pedal" headlines on HPB; LSKT/BBK copy must not name David). -> `ads_apply_recommendation` after preview.
- Google recs to ignore: SEARCH_PARTNERS_OPT_IN x5, DISPLAY_EXPANSION x4, USE_BROAD_MATCH x3, RSA recs on paused BBK Industry campaign, MARGINAL_ROI_BUDGET on a paused campaign.

### B. Moves money — review carefully
- [ ] **B-4 (recommended)** BBK PMax 22706227845 budget $15 -> $20/day. 30d 7.1x, 7d 11.6x, 10% impressions lost to budget. Prior: 15.0. -> `ads_mutate` campaignBudgets amountMicros 20000000. expected: +$150-250/mo conv value at 6x+.
- [ ] **B-5 (recommended)** LSKT PMax 22684341497 budget $37.50 -> $25/day until bats are gone for the season (0 conv on $163 this week). Prior: 37.5. -> `ads_mutate` campaignBudgets amountMicros 25000000. expected: ~$85/wk saved, little conv loss. Net with B-4: spend down ~$50/wk, value up.
- [ ] **B-6** LSKT Bat search 23641266373: pause for the season when the last bat tour date is set (Lone Star calendar), or now if the last tour has already run. $14 this week, 0 conv. -> `ads_mutate` campaign status PAUSED. Prior: ENABLED, $30/day.
- [ ] **B-7** Decline FORECASTING_SET_TARGET_ROAS rec on LSKT PMax; a tROAS set from bat-season data would be wrong for November.

---

## 2372234368 — Ebb & Ember (Portland sauna)

- Core Search 24049713079 ($15/day): 30d 2.42x, 7d 4.30x. Rank-lost 49%, budget-lost 20%.
- Tourist 24049713082 ($7/day, actually delivering ~$14/day): 30d 5.83x, 7d 7.71x. Rank-lost 73%, budget-lost 12%. Caveat: 5 of its 11 conv came from the brand term "ebb and ember" matching through "things to do in portland" BROAD, so non-brand Tourist ROAS is lower than it looks.
- Conversion action "EbbandEmber (web) purchase" is the only counted one and has real values. Good.
- Ad strength: 2 EXCELLENT, 1 GOOD, 6 AVERAGE. The AVERAGE "Sauna Near Me (LI)" ad (822464549685) is $137/30d at 1.43x.

### A. Safe
- [ ] **A-11** Pause "sauna near me" PHRASE ($45, 0 conv, QS4), "sauna near me" BROAD ($11, 0 conv, QS4), "saunas near me" BROAD ($13, 0 conv, QS3) in Core / Sauna Near Me (LI). Keep "sauna near me" EXACT (2 conv, 2.55x). -> `ads_mutate` adGroupCriteria PAUSED. expected: ~$16/wk saved.
- [ ] **A-12** Pause "sauna portland" BROAD in Core / Sauna Portland ($21, 0 conv). PHRASE (5.88x) and EXACT stay. -> `ads_mutate` adGroupCriteria PAUSED. expected: ~$5/wk saved.
- [ ] **A-13** Negative "vancouver" is NOT proposed (the ad group is intentional). But flag: Sauna Vancouver WA ad group $18/30d, 0 conv. Leave for now, re-check 11/30.
- [ ] **A-14** Add brand EXACT keywords to the Tourist campaign too, or move brand capture out of "things to do" BROAD: today brand searches ride a broad tourist keyword. Low priority. Manual.
- Google recs to ignore: PERFORMANCE_MAX_OPT_IN (no), SET_TARGET_CPA on Tourist (computed on a brand-inflated window), USE_BROAD_MATCH, 14 KEYWORD recs (text not exposed by API; review in UI only).

### B. Moves money — review carefully
- [ ] **B-8 (recommended)** Tourist 24049713082 budget $7 -> $12/day. 5.8x/7.7x, 12% lost to budget, 73% lost to rank. Prior: 7.0. -> `ads_mutate` campaignBudgets amountMicros 12000000. expected: +$100/wk value if it holds 5x+; watch the brand share.
- [ ] **B-9** Core 24049713079: hold at $15 until A-11/A-12 land and 2 weeks of clean data exist. No call.

---

## 8672151991 — DCKT
Both ENABLED campaigns (PMax 22652566458, Brand Search 23949326344) show serving_status ENDED / primary_status CAMPAIGN_ENDED: they ran to a scheduled end date on 9/7. Billing is fine. The morning-brief "DCKT ads look broken" lines from mid-Sept were wrong; this file is the correction.
- [ ] **A-15** Reminder for ~Apr 1 2027: reopen DCKT campaign end dates (or set to none) before the season. No action now.

## 2986009791 — HPB solo
PMax 20980073958 PAUSED since 9/18 (loop C-2). Zero spend, zero recs. Nothing to do. HPB's live spend is campaign 20315555269 in 8497383499 above.

---

## Grading the last run
- HPB C-5 (Pedal boat ad group tROAS 3.0, set 9/21): ad group now 4.04x on $301/30d, up from 2.0-2.9x in Sept. Improved, still under the 5x floor. Leave it; revisit at 5x.
- HPB C-2 (PMax pause): still zero spend, no purchase signal lost. Holds.
- HPB C-3 (Clear lake ad group pause): $0, holds.
- NPB G-NPB-2 (Aug budget raise on National): the campaign has since gone from 20x to 1x in a week; the Aug raise was fine, the Oct collapse is new. See B-1.
- DCKT G-DCKT-2 (Aug budget raise): moot, campaigns ended 9/7.
