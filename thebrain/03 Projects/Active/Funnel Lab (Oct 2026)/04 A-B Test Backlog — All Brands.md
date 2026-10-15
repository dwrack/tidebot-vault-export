# A/B Test Backlog: All Brands (Funnel Lab, Oct 14 2026)

*Written overnight 2026-10-14 by David's Claude from files 01 (customer truth), 02 (live funnel numbers) and 03 (what can split). DRAFT. Nothing is live, sent, or changed. Every card is on the Funnel Lab Board, where David picks A, B, or "split test both".*

## The three rules this backlog follows

1. **Measure where the volume is, not at the purchase.** At peak season NPB books about 16 online a day, BBK 2.7, NKST 1.8, HPB 1.7. A purchase-level test needs ~190 bookings per arm to see a 30% lift, so it takes NPB 23 days and NKST 211. So most tests here read **chat replies, lead signups, ad clicks, or Book-button taps**, which run 10x to 100x the volume. Purchases get checked at the end as a sanity check.
2. **Swing big.** Small tweaks (button color, one word) can't be read at our traffic. Every test changes the angle, the offer, or the order of the page.
3. **Fix the measuring stick first.** NKST and HPB send zero real purchase events to GA4, and NPB counts its own checkout as a referral. Card 16 fixes that. Until then those brands' tests are read from FareHarbor and the ad platforms.

## Priority order

| # | Brand | Test | Reads on | Can start | Days to read |
|:-|:-|:-|:-|:-|:-|
| 1 | NPB | Chat: price first, then what? | Chats ending with link or contact | Now (OpenCX) | ~60 |
| 2 | NPB, BBK, LSKT | Where cold social traffic lands | Cost per Book-form view / lead | Now (Meta A/B) | 14-21 |
| 3 | All | Testing build path | n/a (infrastructure) | Code built tonight | n/a |
| 4 | NKST, BBK, LSKT (+NPB, HPB) | Weather credit vs refund | Credit-take rate | Now | Season |
| 5 | All FH + E&E | How did you hear about us | n/a (measurement) | Now | n/a |
| 6 | NPB | Birthday vs bachelorette creative | Ad CTR, cost per Book-form view | Now (Meta) | 14 |
| 7 | NKST | Lead-form rescue | Reply rate to first message | Now (OpenCX) | ~30 |
| 8 | NKST | Locals who've never been vs visitors | Cost per lead / Book-form view | Now (Meta) | 14-21 |
| 9 | E&E | Open on the river jump vs the sauna | Reel hold rate, link taps | Now (IG/Meta) | 14 |
| 10 | E&E | Booking page: how-to-get-here vs fake-choice | Book taps per session | Now (Squarespace footer) | ~30 |
| 11 | E&E | Bring-a-friend vs book-your-next | Rebooks within 30 days | Now (ActiveCampaign) | 30-45 |
| 12 | BBK | Bat landing page rebuild vs straight to booking | Book-form views per session | Now (GTM) | 14-21 |
| 13 | BBK | Honest water line vs none | Book taps + low-star rate | Now (GTM) | Season |
| 14 | DCKT | Family-first vs Cave Point-first | Book-form views per session | May 2027 | 35 |
| 15 | LSKT/AKT | Bats-first vs beginners-first | Ad CTR, Book taps | Mar 2027 | 21 |
| 16 | NKST, HPB, NPB | Fix tracking: FareHarbor GA4 vs server bridge | n/a (measurement) | Now | n/a |

Cards 1, 2, 6, 7, 8 and 9 need no new code at all. Start there.

---

## 1. NPB: Chat, price first, then what?

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

**Evidence.** Last 30 days paid social sent NPB 10,966 sessions and 8 purchases (0.07%). BBK 4,823 sessions, 0. LSKT 373, 0. Engagement 9-31%. *(02 Baselines)*

**Version A: Send cold traffic to a lead step, not a checkout.** Cold ads link to a one-question page ("What are you celebrating?" for NPB, "Who's paddling?" for BBK/LSKT) that shows the right tour and price, then asks for an email or cell to save it. Optimize the ad set for Lead. Retarget leads with booking ads.
**Version B: Cold traffic watches, warm traffic books (Growth Play 4).** Cold budget goes to ThruPlay Reels only ($5-10/day). 50% and 95% viewers get the booking ads. No cold booking ads at all.

**Measure.** Cost per Book-form view and cost per booking over 21 days, same total budget.
**Split.** Meta native A/B test in Ads Manager, 50/50 budget (the facebook MCP can't create an A/B study, so David or Claude sets it in the UI).
**Note.** Version A needs a lead page. Until the FareHarbor header slot exists, A can use a Meta Instant Form (no site code). NPB already has the Group Chat Link designed (`NOLA Party Barge/Marketing/Lead Funnels Oct 2026/07`).
**My pick: run both.** They're different bets on why social fails (no intent vs no trust), and this test tells us which.

## 3. All: The testing build path

**Evidence.** Nothing can run a controlled split today except the DCKT ride quiz. Five FareHarbor sites (NPB, NKST, HPB, LSKT, AKT) have no way for us to add code. DCKT and BBK have GTM. E&E's Squarespace takes a footer snippet. *(03 Infrastructure)*

**Version A: Build our own.** Variant assignment inside the lead engine (built tonight on branch `ab-variants`, not deployed) plus one FareHarbor header-script slot per site that loads `ab.js`. Covers email, popup and on-site tests on every brand.
**Version B: Use only what's open now.** GTM on DCKT and BBK, Squarespace footer on E&E, Meta and Google native tests, OpenCX week-alternation. No FareHarbor ask.

**My pick: both.** B starts tomorrow. A is the real unlock and the same FareHarbor ask the lead popup is already waiting on, so it's one email to the FH rep, not two.

## 4. Weather credit vs refund (Growth Play 1)

Full file: `10 Play 1 — Weather Credit, Two Versions + Live Test.md`.
**Version A:** credit by default, refund on request (DCKT 2027 model, needs policy change + legal read).
**Version B:** guest chooses refund or a 120% credit (no policy change, can test now on even/odd booking numbers).
**My pick: B now as the test, A for 2027 once we know the real credit-take rate.** HPB belongs here too: 17 of its 19 low-star reviews are about cancels and slow refunds.

## 5. How did you hear about us (Growth Play 3)

Full file: `11 Play 3 — How Did You Hear About Us, Two Versions.md`.
**Version A:** optional question at FareHarbor checkout. **Version B:** one-tap question in the confirmation email.
**My pick: A on FareHarbor brands, B on E&E.**

## 6. NPB: Birthday vs bachelorette creative

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

## 7. NKST: Lead-form rescue

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

## 9. E&E: Open on the river jump vs the sauna

**Evidence.** The river jump or cold plunge is in 50% of reviews and is the differentiator. The sauna is in 70%. "Recovery" appears in 0 of 115 reviews. The research file found local-plans hooks hit 2,000+ likes while health explainers got 7-21. *(01; Sauna Viral Research 04)*

**Version A: The jump.** First 2 seconds: the jump off the deck into the Columbia, the gasp. On-screen: "sweat. jump. repeat."
**Version B: The sauna.** First 2 seconds: steam, river view through the glass, rain on the window. On-screen: "Portland's only floating sauna."

Same 12-second cut after the opener, same caption, same CTA. Proof line for both: "Such a perfect way to end a river day."

**Measure.** 3-second hold rate, link taps, Book taps on the landing page.
**Split.** Instagram trial reels (shown to non-followers) or Meta A/B with $10/day each. Kimberlynn cuts both from existing footage.
**My pick: A.** Cold gets the views, heat gets the bookings, and the jump is the hook only we have.

## 10. E&E: Booking page, how-to-get-here vs fake-choice

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

## 12. BBK: Bat landing page rebuild vs straight to booking

**Evidence.** The bat-bridge landing page took 4,898 sessions at 10.8% engagement and produced 4 purchases. Site-wide Book-form views run ~10% of sessions. *(02)*

**Version A: Rebuild the bat page.** Price, next three bat tour times, and the Book button in the first screen on a phone. One proof line: "Totally different view of the city from the water!"
**Version B: Skip the page.** Bat ads and links go straight to the FareHarbor bat tour booking flow.

**Measure.** Book-form views per session and purchases per session.
**Split.** GTM on BBK can redirect 50% of bat-page visitors to the booking flow (B) while the other 50% see the rebuilt page (A). Needs GTM publish access [VERIFY who has it].
**My pick: run both.** At 4,900 sessions a month this reads in 2-3 weeks.

## 13. BBK: Honest water line vs none

**Evidence.** Dirty water is 14 of 27 low-star reviews (6.7% of all). One reviewer: "10/10 it's Houston so you can't expect perfection regarding the bayou."

**Version A: One honest line near Book.**
> This is a working urban bayou in the middle of Houston. The water's brown, the skyline's huge, and the herons don't mind.
**Version B: No line** (today).

**Measure.** Book taps (A may lose a few) and the share of new reviews at 1-3 stars that mention water (A should drop).
**Split.** GTM, 50/50. Read over a season.
**My pick: A.** Filtering out the wrong guest is cheaper than a 1-star review.

## 14. DCKT: Family-first vs Cave Point-first (2027 season)

**Evidence.** Kids, age and pets are the #1 first question (24%). Families are 11.5% of recent reviews. Cave Point is named in 20%. The journey map still says "800+ five-star reviews" (now 1,015, 973 five-star). *(01)*

**Version A: Family-first.** Homepage block above Book: real age minimum, pet policy, weight limit [VERIFY all three, don't guess], plus "Exciting while still safe for the kids."
**Version B: Cave Point-first.** Hero names Cave Point, with one honest "what you will and won't see" line.

**Measure.** Book-form views per session.
**Split.** DCKT has GTM and an already-running ride-quiz split. Launch May 2027.
**My pick: A.** Fix the "800+" number on every surface now regardless.

## 15. LSKT/AKT: Bats-first vs beginners-first (spring 2027)

**Evidence.** Bats are named in 31% of Austin reviews. "Beginner fit / what's the tour" is 22% of LSKT chat questions. LSKT paid social: 373 sessions, 0 purchases.
**Version A:** "The bats were amazing, a completely unique, must-do experience!" bat-season creative.
**Version B:** First-timer creative: calm water, all gear, guide the whole way.
**Measure.** CTR and Book taps. Meta A/B from March 2027 when bat season starts.
**My pick: A in bat season, B the rest of the year.** Park until March.

## 16. Fix tracking: FareHarbor GA4 vs server-side bridge

**Evidence.** NKST GA4 has 4 purchase events and $0 revenue for 20,774 sessions. HPB has no FareHarbor events at all. NPB counts nolapartybarges.com checkout returns as a referral (1,802 sessions, 77 purchases). *(02)*

**Version A: Fix FareHarbor's own GA4 link.** In each FH dashboard, re-enter the right GA4 measurement ID and enable ecommerce events. Add nolapartybarges.com (and fareharbor.com) to GA4's unwanted-referrals list for NPB.
**Version B: Server-side bridge.** Same pattern as the E&E Periode bridge: FareHarbor webhook or nightly booking pull sends purchase events to GA4 Measurement Protocol and Meta CAPI.

**My pick: A first** (one setting per brand). If FH's GA4 link keeps dropping events through checkout (the DCKT test on 2026-05-12 found it does), build B for NPB, NKST and HPB.

---

## What I need from David

1. Pick on the board. Every card has A, B, or both.
2. Card 1: confirm the live NPB prices and Party Queen capacity (chat says 22, site says 26).
3. Card 3: OK to email the FareHarbor rep for the header-script slot on NPB, NKST, HPB, LSKT, AKT? (One ask covers the popup and the tests.)
4. Card 11: what the E&E bring-a-friend offer is.
5. Card 12/13: who has GTM publish access on BBK and DCKT?
