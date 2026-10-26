*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for LSKT.*

# A-B Tests: LSKT (split from file 04)

Every card from file 04 that names LSKT, verbatim, with David's pick and note from the board (data read 2026-10-15) inserted under each heading. 'none yet (waiting)' means no pick on the board yet.

Cards 4 and 5 below point to files 10 and 11 of the hub. In this folder those are the 10 Weather Credit and 11 How Did You Hear About Us files (file 10 is a pointer at DCKT and absent at E&E).

## The three rules this backlog follows

1. **Measure where the volume is, not at the purchase.** At peak season NPB books about 16 online a day, BBK 2.7, NKST 1.8, HPB 1.7. A purchase-level test needs ~190 bookings per arm to see a 30% lift, so it takes NPB 23 days and NKST 211. So most tests here read **chat replies, lead signups, ad clicks, or Book-button taps**, which run 10x to 100x the volume. Purchases get checked at the end as a sanity check.
2. **Swing big.** Small tweaks (button color, one word) can't be read at our traffic. Every test changes the angle, the offer, or the order of the page.
3. **Fix the measuring stick first.** NKST and HPB send zero real purchase events to GA4, and NPB counts its own checkout as a referral. Card 16 fixes that. Until then those brands' tests are read from FareHarbor and the ad platforms.

## Priority order (rows for LSKT)

| # | Brand | Test | Reads on | Can start | Days to read |
|:-|:-|:-|:-|:-|:-|
| 2 | NPB, BBK, LSKT | Where cold social traffic lands | Cost per Book-form view / lead | Now (Meta A/B) | 14-21 |
| 3 | All | Testing build path | n/a (infrastructure) | Code built tonight | n/a |
| 4 | NKST, BBK, LSKT (+NPB, HPB) | Weather credit vs refund | Credit-take rate | Now | Season |
| 5 | All FH + E&E | How did you hear about us | n/a (measurement) | Now | n/a |
| 15 | LSKT/AKT | Bats-first vs beginners-first | Ad CTR, Book taps | Mar 2027 | 21 |

## 2. NPB, BBK, LSKT: Where cold social traffic lands

**Board: pick = none yet (waiting) / note = (none)**

*Multi-brand card (BBK, LSKT, NPB): the same card text sits in each of those brand folders. Board card c02, brand field on the board: NPB + BBK + LSKT.*

**Evidence.** Last 30 days paid social sent NPB 10,966 sessions and 8 purchases (0.07%). BBK 4,823 sessions, 0. LSKT 373, 0. Engagement 9-31%. *(02 Baselines)*

**Version A: Send cold traffic to a lead step, not a checkout.** Cold ads link to a one-question page ("What are you celebrating?" for NPB, "Who's paddling?" for BBK/LSKT) that shows the right tour and price, then asks for an email or cell to save it. Optimize the ad set for Lead. Retarget leads with booking ads.
**Version B: Cold traffic watches, warm traffic books (Growth Play 4).** Cold budget goes to ThruPlay Reels only ($5-10/day). 50% and 95% viewers get the booking ads. No cold booking ads at all.

**Measure.** Cost per Book-form view and cost per booking over 21 days, same total budget.
**Split.** Meta native A/B test in Ads Manager, 50/50 budget (the facebook MCP can't create an A/B study, so David or Claude sets it in the UI).
**Note.** Version A needs a lead page. Until the FareHarbor header slot exists, A can use a Meta Instant Form (no site code). NPB already has the Group Chat Link designed (`NOLA Party Barge/Marketing/Lead Funnels Oct 2026/07`).
**My pick: run both.** They're different bets on why social fails (no intent vs no trust), and this test tells us which.

## 3. All: The testing build path

**Board: pick = both / note = do we do a pop up?**

*Shared card: this applies to all brands, so the same card text sits in every brand folder.*

**Evidence.** Nothing can run a controlled split today except the DCKT ride quiz. Five FareHarbor sites (NPB, NKST, HPB, LSKT, AKT) have no way for us to add code. DCKT and BBK have GTM. E&E's Squarespace takes a footer snippet. *(03 Infrastructure)*

**Version A: Build our own.** Variant assignment inside the lead engine (built tonight on branch `ab-variants`, not deployed) plus one FareHarbor header-script slot per site that loads `ab.js`. Covers email, popup and on-site tests on every brand.
**Version B: Use only what's open now.** GTM on DCKT and BBK, Squarespace footer on E&E, Meta and Google native tests, OpenCX week-alternation. No FareHarbor ask.

**My pick: both.** B starts tomorrow. A is the real unlock and the same FareHarbor ask the lead popup is already waiting on, so it's one email to the FH rep, not two.

## 4. Weather credit vs refund (Growth Play 1)

**Board: pick = park / note = (none)**

*Multi-brand card (BBK, HPB, LSKT, NKST, NPB): the same card text sits in each of those brand folders. Board card c04, brand field on the board: NKST + BBK + LSKT.*

Full file: `10 Play 1 — Weather Credit, Two Versions + Live Test.md`.
**Version A:** credit by default, refund on request (DCKT 2027 model, needs policy change + legal read).
**Version B:** guest chooses refund or a 120% credit (no policy change, can test now on even/odd booking numbers).
**My pick: B now as the test, A for 2027 once we know the real credit-take rate.** HPB belongs here too: 17 of its 19 low-star reviews are about cancels and slow refunds.

## 5. How did you hear about us (Growth Play 3)

**Board: pick = none yet (waiting) / note = (none)**

*Shared card: this applies to all brands, so the same card text sits in every brand folder.*

Full file: `11 Play 3 — How Did You Hear About Us, Two Versions.md`.
**Version A:** optional question at FareHarbor checkout. **Version B:** one-tap question in the confirmation email.
**My pick: A on FareHarbor brands, B on E&E.**

## 15. LSKT/AKT: Bats-first vs beginners-first (spring 2027)

**Board: pick = both / note = (none)**

**Evidence.** Bats are named in 31% of Austin reviews. "Beginner fit / what's the tour" is 22% of LSKT chat questions. LSKT paid social: 373 sessions, 0 purchases.
**Version A:** "The bats were amazing, a completely unique, must-do experience!" bat-season creative.
**Version B:** First-timer creative: calm water, all gear, guide the whole way.
**Measure.** CTR and Book taps. Meta A/B from March 2027 when bat season starts.
**My pick: A in bat season, B the rest of the year.** Park until March.

## Board-only cards (not in file 04)

These board cards were added after file 04 was written. Their full text is in file 12 (NPB chat) and file 30 (quizzes). Board data below is as written.

### c18: Quiz style: find-your-tour vs personality (file 30, decision 1)

**Board: pick = both / note = (none)**

Brand: All. Status: approved. Surface: /quiz pages on the lead engine (being built tonight). Metric: Completion, save rate, bookings per 100 starts. Sample: Cold social 50/50.

- A, Find your tour: The questions a guide would ask (who's coming, ever kayaked, what you want to see, when). Result: the right tour, price, your fear answered.
- B, What kind of ___ are you?: Same data, fun identity result plus the tour that fits ('What kind of swamp creature are you?', 'What's your sauna temperature?').
- Why: Your ask: leads are too cold and pick too fast. A 30-second quiz is the second conversation. Cold social: NPB 10,966 sessions, 8 purchases, 0 emails kept.

### c19: Quiz: when we ask for the email (file 30, decision 2)

**Board: pick = B / note = (none)**

Brand: All. Status: approved. Surface: Quiz engine. Metric: Emails per 100 starts, then bookings per email. Sample: Split inside every quiz.

- A, Result first, then save: Show the tour and price, then 'Want this sent to you or your group chat?'
- B, Email unlocks the result: 'Where should we send your result?' before the reveal.
- Why: Asking first captures more. Showing first builds trust and gets shared. The NPB planner already shows first.

### c20: Nurture: help first vs small offer early (file 30, decision 3)

**Board: pick = A / note = (none)**

Brand: All. Status: approved. Surface: Lead engine drip. Metric: Bookings per lead within 30 days. Sample: Split per lead.

- A, Help first: No ask until day 5. Pure usefulness: guide intro, what to bring, where we meet.
- B, Small add-on on day 2: Same sequence plus a cheap non-cash add-on on day 2 (ice, a dry bag, a towel). No percentage discounts. You pick what each brand can give.
- Why: 7 emails timed to the trip date: result, their fear answered, proof from people like them, meet your guide, where we meet, real availability, last nudge. Plus a 'still deciding?' email 24h after a Book tap with no booking.

### c21: Popup: quiz vs offer (file 30, decision 4)

**Board: pick = A / note = (none)**

Brand: All. Status: approved. Surface: w.js via FareHarbor header slot, GTM (DCKT/BBK), Squarespace footer (E&E). Metric: Emails per 100 visitors, bookings per email. Sample: Site traffic 50/50.

- A, Quiz popup: 'Not sure which tour? 30-second quiz.' After 20 seconds or on mobile scroll-up.
- B, Offer popup: Today's HPB style: '$25 off your first trip' for an email.
- Why: Your note on card 3. The popup is built but on no site yet. It is the cheapest way to send site visitors into the quiz.

## What I need from David (file 04, items that touch LSKT)

1. Pick on the board. Every card has A, B, or both.
3. Card 3: OK to email the FareHarbor rep for the header-script slot on NPB, NKST, HPB, LSKT, AKT? (One ask covers the popup and the tests.)
