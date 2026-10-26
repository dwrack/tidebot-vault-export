*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for E&E.*

# A-B Tests: E&E (split from file 04)

Every card from file 04 that names E&E, verbatim, with David's pick and note from the board (data read 2026-10-15) inserted under each heading. 'none yet (waiting)' means no pick on the board yet.

Cards 4 and 5 below point to files 10 and 11 of the hub. In this folder those are the 10 Weather Credit and 11 How Did You Hear About Us files (file 10 is a pointer at DCKT and absent at E&E).

## The three rules this backlog follows

1. **Measure where the volume is, not at the purchase.** At peak season NPB books about 16 online a day, BBK 2.7, NKST 1.8, HPB 1.7. A purchase-level test needs ~190 bookings per arm to see a 30% lift, so it takes NPB 23 days and NKST 211. So most tests here read **chat replies, lead signups, ad clicks, or Book-button taps**, which run 10x to 100x the volume. Purchases get checked at the end as a sanity check.
2. **Swing big.** Small tweaks (button color, one word) can't be read at our traffic. Every test changes the angle, the offer, or the order of the page.
3. **Fix the measuring stick first.** NKST and HPB send zero real purchase events to GA4, and NPB counts its own checkout as a referral. Card 16 fixes that. Until then those brands' tests are read from FareHarbor and the ad platforms.

## Priority order (rows for E&E)

| # | Brand | Test | Reads on | Can start | Days to read |
|:-|:-|:-|:-|:-|:-|
| 3 | All | Testing build path | n/a (infrastructure) | Code built tonight | n/a |
| 5 | All FH + E&E | How did you hear about us | n/a (measurement) | Now | n/a |
| 9 | E&E | Open on the river jump vs the sauna | Reel hold rate, link taps | Now (IG/Meta) | 14 |
| 10 | E&E | Booking page: how-to-get-here vs fake-choice | Book taps per session | Now (Squarespace footer) | ~30 |
| 11 | E&E | Bring-a-friend vs book-your-next | Rebooks within 30 days | Now (ActiveCampaign) | 30-45 |

## 3. All: The testing build path

**Board: pick = both / note = do we do a pop up?**

*Shared card: this applies to all brands, so the same card text sits in every brand folder.*

**Evidence.** Nothing can run a controlled split today except the DCKT ride quiz. Five FareHarbor sites (NPB, NKST, HPB, LSKT, AKT) have no way for us to add code. DCKT and BBK have GTM. E&E's Squarespace takes a footer snippet. *(03 Infrastructure)*

**Version A: Build our own.** Variant assignment inside the lead engine (built tonight on branch `ab-variants`, not deployed) plus one FareHarbor header-script slot per site that loads `ab.js`. Covers email, popup and on-site tests on every brand.
**Version B: Use only what's open now.** GTM on DCKT and BBK, Squarespace footer on E&E, Meta and Google native tests, OpenCX week-alternation. No FareHarbor ask.

**My pick: both.** B starts tomorrow. A is the real unlock and the same FareHarbor ask the lead popup is already waiting on, so it's one email to the FH rep, not two.

## 5. How did you hear about us (Growth Play 3)

**Board: pick = none yet (waiting) / note = (none)**

*Shared card: this applies to all brands, so the same card text sits in every brand folder.*

Full file: `11 Play 3 — How Did You Hear About Us, Two Versions.md`.
**Version A:** optional question at FareHarbor checkout. **Version B:** one-tap question in the confirmation email.
**My pick: A on FareHarbor brands, B on E&E.**

## 9. E&E: Open on the river jump vs the sauna

**Board: pick = both / note = (none)**

**Evidence.** The river jump or cold plunge is in 50% of reviews and is the differentiator. The sauna is in 70%. "Recovery" appears in 0 of 115 reviews. The research file found local-plans hooks hit 2,000+ likes while health explainers got 7-21. *(01; Sauna Viral Research 04)*

**Version A: The jump.** First 2 seconds: the jump off the deck into the Columbia, the gasp. On-screen: "sweat. jump. repeat."
**Version B: The sauna.** First 2 seconds: steam, river view through the glass, rain on the window. On-screen: "Portland's only floating sauna."

Same 12-second cut after the opener, same caption, same CTA. Proof line for both: "Such a perfect way to end a river day."

**Measure.** 3-second hold rate, link taps, Book taps on the landing page.
**Split.** Instagram trial reels (shown to non-followers) or Meta A/B with $10/day each. Kimberlynn cuts both from existing footage.
**My pick: A.** Cold gets the views, heat gets the bookings, and the jump is the hook only we have.

## 10. E&E: Booking page, how-to-get-here vs fake-choice

**Board: pick = park / note = (none)**

**Evidence.** 842 begin_checkout to 325 purchases (39%). 89% of sessions are mobile. Reviewers volunteer access, parking and what-to-bring more than anything else. *(01, 02)*

**Version A: Reassure.** A short block right above the Book button:
> Getting here: [address / parking / transit line, VERIFY]. Bring a swimsuit and a towel [VERIFY: towels provided?]. Sessions are [length, VERIFY]. You can jump in the river or stay on deck, your call.
**Version B: Fake-choice question (Growth Play 5).** Before prices show:
> What matters most for this visit? (A) The best time slot and the full ritual. (B) The lowest price.
> A routes to peak/private, B to off-peak. Copy already drafted in the E&E pricing survey doc.

**Measure.** Book taps (begin_checkout) per session, by variant. Periode purchase can't be tied to the variant yet [VERIFY whether Periode passes URL params through].
**Split.** Squarespace footer snippet (`ab.js`), 50/50 sticky per visitor.
**My pick: A.** It fixes what reviewers actually describe. B is a pricing play and fits better once the banya price survey is back.

## 11. E&E: Bring-a-friend vs book-your-next

**Board: pick = both / note = (none)**

**Evidence.** 29% of reviews mention coming back. Tourists are 3.5%. 58% of guests are repeat and they bring 67% of revenue (Periode sales analysis). *(01; memory: reference_periode_sales_analysis)*

**Version A: Bring a friend.** Post-visit email, day 3:
> Subject: who's coming next time?
> Your next session, bring someone who hasn't done it. [Offer: VERIFY with David, e.g. their first session at member price]. Book here: [link]
**Version B: Book your next.** Post-visit email, day 3:
> Subject: same time next week?
> The river's still cold and the sauna's still hot. Grab your next session: [link]

**Measure.** Rebooks (either the guest or a new email at the same booking) within 30 days.
**Split.** ActiveCampaign split send, 50/50 [VERIFY plan tier supports split testing].
**Decision for David.** What the friend offer is. I didn't invent one.
**My pick: A.** New guests from happy guests is the cheapest growth E&E has.

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

## What I need from David (file 04, items that touch E&E)

1. Pick on the board. Every card has A, B, or both.
4. Card 11: what the E&E bring-a-friend offer is.
