*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NPB.*

# A-B Tests: NPB (split from file 04)

Every card from file 04 that names NPB, verbatim, with David's pick and note from the board (data read 2026-10-15) inserted under each heading. 'none yet (waiting)' means no pick on the board yet.

Cards 4 and 5 below point to files 10 and 11 of the hub. In this folder those are the 10 Weather Credit and 11 How Did You Hear About Us files (file 10 is a pointer at DCKT and absent at E&E).

## The three rules this backlog follows

1. **Measure where the volume is, not at the purchase.** At peak season NPB books about 16 online a day, BBK 2.7, NKST 1.8, HPB 1.7. A purchase-level test needs ~190 bookings per arm to see a 30% lift, so it takes NPB 23 days and NKST 211. So most tests here read **chat replies, lead signups, ad clicks, or Book-button taps**, which run 10x to 100x the volume. Purchases get checked at the end as a sanity check.
2. **Swing big.** Small tweaks (button color, one word) can't be read at our traffic. Every test changes the angle, the offer, or the order of the page.
3. **Fix the measuring stick first.** NKST and HPB send zero real purchase events to GA4, and NPB counts its own checkout as a referral. Card 16 fixes that. Until then those brands' tests are read from FareHarbor and the ad platforms.

## Priority order (rows for NPB)

| # | Brand | Test | Reads on | Can start | Days to read |
|:-|:-|:-|:-|:-|:-|
| 1 | NPB | Chat: price first, then what? | Chats ending with link or contact | Now (OpenCX) | ~60 |
| 2 | NPB, BBK, LSKT | Where cold social traffic lands | Cost per Book-form view / lead | Now (Meta A/B) | 14-21 |
| 3 | All | Testing build path | n/a (infrastructure) | Code built tonight | n/a |
| 4 | NKST, BBK, LSKT (+NPB, HPB) | Weather credit vs refund | Credit-take rate | Now | Season |
| 5 | All FH + E&E | How did you hear about us | n/a (measurement) | Now | n/a |
| 6 | NPB | Birthday vs bachelorette creative | Ad CTR, cost per Book-form view | Now (Meta) | 14 |
| 16 | NKST, HPB, NPB | Fix tracking: FareHarbor GA4 vs server bridge | n/a (measurement) | Now | n/a |

## 1. NPB: Chat, price first, then what?

**Board: pick = B / note = can we make more split testing options, use some psychology, try using some wit**

**Evidence.** 52% of shopper chats open with "how much" (105 of 201). 64% end with no booking link and no contact. The AI links to booking in only 14% of chats. Human nudges get a 6% reply rate. 27% of shoppers volunteer a phone number anyway. *(01 Customer Truth, NPB)*

**Version A: Price, then the link.** Answer the price in the first line, then one tap to open dates. No questions first.
> Seats are $59 a person (the Twerkin' Tiki 6pm is $63). Whole boats run $800 to $1,200 for your crew. Here's what's open: [booking link]. How many are you bringing? I'll point you to the best boat.

**Version B: Price, then the group math, then the phone.** Answer price, show per-head math for their group size, then ask for a cell to text the link and a group-chat-ready summary.
> Seats are $59 a person. For bigger crews a whole boat is usually cheaper: the Party Queen is $900, about $41 a head for 22 [VERIFY capacity, site says 26]. How many are you, and what are you celebrating? Drop your cell and I'll text you the link plus a summary you can paste in the group chat.

**Measure.** % of chats that end with a booking link sent AND clicked, or an email/phone captured. Secondary: bookings matched by email/phone within 14 days.
**Split.** OpenCX has no native split. Alternate whole weeks (A week 1, B week 2, repeat) so weekday mix evens out. Fix the wrong prices in the knowledge base first (Oct 13 plan, item 09).
**Sample.** ~100 shopper chats a month. To read 36% vs 55% "ended with link or contact" needs ~100 per arm: about 8 weeks.
**My pick: B.** Planners are the chatters (median group 10), and the phone gets around the dead Messenger email capture. But it's genuinely close, so run both.

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

*The board brand field for this card lists NKST + BBK + LSKT; file 04 (priority table) and file 10 also include NPB and HPB.*

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

## 6. NPB: Birthday vs bachelorette creative

**Board: pick = both / note = (none)**

**Evidence.** Birthday is 6.9% of reviews and 9.9% of chats. Bachelorette is 6.0% and 1.7%. The persona doc leads with bachelorette. Bachelorette is much stronger on the sibling listings (Booze Cruise 13.7%). *(01)*

**Version A: Birthday.**
> Hook: "Turning 30? Do it on a tiki boat with gators."
> Body: BYOB, music, a captain who knows the bayou. Seats $59 or the whole boat for your crew.
> Proof line: "We did this boat tour for my friends 55th bday!"

**Version B: Bachelorette.**
> Hook: "The bachelorette everyone will still talk about."
> Body: Same.
> Proof line: "Would highly recommend this trip for any bachelorette!"

**Measure.** CTR, cost per Book-form view, cost per booking. Same budget, same video base, only the hook text and proof line change.
**Split.** Meta native A/B. NPB volume reads in ~14 days.
**My pick: A** (birthdays happen every month, bachelorettes cluster), but run both because the persona doc bet the other way.

## 16. Fix tracking: FareHarbor GA4 vs server-side bridge

**Board: pick = park / note = (none)**

*Multi-brand card (HPB, NKST, NPB): the same card text sits in each of those brand folders. Board card c16, brand field on the board: NKST + HPB + NPB.*

**Evidence.** NKST GA4 has 4 purchase events and $0 revenue for 20,774 sessions. HPB has no FareHarbor events at all. NPB counts nolapartybarges.com checkout returns as a referral (1,802 sessions, 77 purchases). *(02)*

**Version A: Fix FareHarbor's own GA4 link.** In each FH dashboard, re-enter the right GA4 measurement ID and enable ecommerce events. Add nolapartybarges.com (and fareharbor.com) to GA4's unwanted-referrals list for NPB.
**Version B: Server-side bridge.** Same pattern as the E&E Periode bridge: FareHarbor webhook or nightly booking pull sends purchase events to GA4 Measurement Protocol and Meta CAPI.

**My pick: A first** (one setting per brand). If FH's GA4 link keeps dropping events through checkout (the DCKT test on 2026-05-12 found it does), build B for NPB, NKST and HPB.

## Board-only cards (not in file 04)

These board cards were added after file 04 was written. Their full text is in file 12 (NPB chat) and file 30 (quizzes). Board data below is as written.

### c17: NPB chat: five-way knockout (file 12, card 1.5)

**Board: pick = both / note = (none)**

Brand: NPB. Status: approved. Surface: OpenCX, day rotation. Metric: Chats ending with link clicked or contact captured. Sample: 8-12 weeks total.

- A, Run all five as a knockout: Straight / Group math / Wisecrack / Decoy / Real scarcity, rotating by day. Drop the bottom two at week 4, the next one at week 8, then head to head.
- B, Just the top two bets: Group math vs Wisecrack only. Cleaner read, faster, but we never learn if the decoy or scarcity would have beaten them.
- Why: Your note on card 1: more options, psychology, wit. All five answer the price in line one, because hiding it is the one thing we know loses.

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

## What I need from David (file 04, items that touch NPB)

1. Pick on the board. Every card has A, B, or both.
2. Card 1: confirm the live NPB prices and Party Queen capacity (chat says 22, site says 26).
3. Card 3: OK to email the FareHarbor rep for the header-script slot on NPB, NKST, HPB, LSKT, AKT? (One ask covers the popup and the tests.)
