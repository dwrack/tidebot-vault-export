*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NKST.*

# A-B Tests: NKST (split from file 04)

Every card from file 04 that names NKST, verbatim, with David's pick and note from the board (data read 2026-10-15) inserted under each heading. 'none yet (waiting)' means no pick on the board yet.

Cards 4 and 5 below point to files 10 and 11 of the hub. In this folder those are the 10 Weather Credit and 11 How Did You Hear About Us files (file 10 is a pointer at DCKT and absent at E&E).

## The three rules this backlog follows

1. **Measure where the volume is, not at the purchase.** At peak season NPB books about 16 online a day, BBK 2.7, NKST 1.8, HPB 1.7. A purchase-level test needs ~190 bookings per arm to see a 30% lift, so it takes NPB 23 days and NKST 211. So most tests here read **chat replies, lead signups, ad clicks, or Book-button taps**, which run 10x to 100x the volume. Purchases get checked at the end as a sanity check.
2. **Swing big.** Small tweaks (button color, one word) can't be read at our traffic. Every test changes the angle, the offer, or the order of the page.
3. **Fix the measuring stick first.** NKST and HPB send zero real purchase events to GA4, and NPB counts its own checkout as a referral. Card 16 fixes that. Until then those brands' tests are read from FareHarbor and the ad platforms.

## Priority order (rows for NKST)

| # | Brand | Test | Reads on | Can start | Days to read |
|:-|:-|:-|:-|:-|:-|
| 3 | All | Testing build path | n/a (infrastructure) | Code built tonight | n/a |
| 4 | NKST, BBK, LSKT (+NPB, HPB) | Weather credit vs refund | Credit-take rate | Now | Season |
| 5 | All FH + E&E | How did you hear about us | n/a (measurement) | Now | n/a |
| 7 | NKST | Lead-form rescue | Reply rate to first message | Now (OpenCX) | ~30 |
| 8 | NKST | Locals who've never been vs visitors | Cost per lead / Book-form view | Now (Meta) | 14-21 |
| 16 | NKST, HPB, NPB | Fix tracking: FareHarbor GA4 vs server bridge | n/a (measurement) | Now | n/a |

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

## 7. NKST: Lead-form rescue

**Board: pick = both / note = (none)**

**Evidence.** 168 Messenger lead-form fills. 72% never answer the AI's "what date?" question. 65% live in New Orleans. 33% have never kayaked. *(01)*

**Version A: One tap, link up front.** First reply carries the booking link and a month picker.
> Hey [first name], thanks for reaching out! Here are open tours: [link]. When are you thinking? Tap one: This weekend / Next weekend / Later this month / Just looking

**Version B: Local and first-timer first.** First reply speaks to who they actually are, then asks.
> Hey [first name]! Lots of folks who live here have never paddled their own swamp, and most of our guests are first-timers. Calm water, stable kayaks, a guide the whole way. Want me to send this weekend's open times?

**Measure.** Reply rate to the first message, then link clicks. Book matches by name/phone within 14 days.
**Split.** Alternate weeks in the OpenCX workflow.
**Sample.** Reading 28% vs 45% reply needs ~120 per arm. At current lead-form volume, about a month each [VERIFY monthly form fills].
**My pick: A.** Fewer words, one tap. B's insight goes into card 8's ads instead.

## 8. NKST: Locals who've never been vs visitors

**Board: pick = both / note = (none)**

**Evidence.** Same as 7. The journey map targets visitors planning 1-3 months out. The lead form says locals.

**Version A: Locals.**
> Hook: "You live under an hour from this swamp. Ever paddled it?" [VERIFY drive time]
> Proof: "Was definitely apprehensive of kayaking through the swamp, but PLEASE don't be!"
**Version B: Visitors.**
> Hook: "The best thing we did in New Orleans wasn't on Bourbon Street."
> Proof: "It was by far our best experience in New Orleans."

**Measure.** Cost per lead, cost per Book-form view.
**Split.** Meta A/B with A geo-targeted to the metro, B to travel-intent audiences. Note: NKST has no working purchase event (card 16), so read bookings from FareHarbor by date.
**My pick: run both.** Different audiences, so both can win.

## 16. Fix tracking: FareHarbor GA4 vs server-side bridge

**Board: pick = park / note = (none)**

*Multi-brand card (HPB, NKST, NPB): the same card text sits in each of those brand folders. Board card c16, brand field on the board: NKST + HPB + NPB.*

**Evidence.** NKST GA4 has 4 purchase events and $0 revenue for 20,774 sessions. HPB has no FareHarbor events at all. NPB counts nolapartybarges.com checkout returns as a referral (1,802 sessions, 77 purchases). *(02)*

**Version A: Fix FareHarbor's own GA4 link.** In each FH dashboard, re-enter the right GA4 measurement ID and enable ecommerce events. Add nolapartybarges.com (and fareharbor.com) to GA4's unwanted-referrals list for NPB.
**Version B: Server-side bridge.** Same pattern as the E&E Periode bridge: FareHarbor webhook or nightly booking pull sends purchase events to GA4 Measurement Protocol and Meta CAPI.

**My pick: A first** (one setting per brand). If FH's GA4 link keeps dropping events through checkout (the DCKT test on 2026-05-12 found it does), build B for NPB, NKST and HPB.

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

## What I need from David (file 04, items that touch NKST)

1. Pick on the board. Every card has A, B, or both.
3. Card 3: OK to email the FareHarbor rep for the header-script slot on NPB, NKST, HPB, LSKT, AKT? (One ask covers the popup and the tests.)
