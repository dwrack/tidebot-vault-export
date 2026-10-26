# Launch Drafts: NKST (built 2026-10-15)

*Everything here is a draft. Nothing is live, sent, posted or spending. Each item says exactly what it would do once David says go.*

## What was verified live today (2026-10-15)

| Fact | Live source | Finding |
|:-|:-|:-|
| FAQ prices | neworleanskayakswamptours.com/faq/ | Still says $59 / $79 (and "1/2 day $199, combo $175"). Tour cards on the same page say From $65 / $130 / $195. Stale. |
| Tour page prices | /tours/swamp-kayak-tours/manchac-mystic-kayak-tour/ | $79 struck through, $65. Shuttle $25 round trip. Pickup 740 N Rampart, 1 hr 15 min before. |
| Distance | FAQ vs tour page | FAQ: 30 miles west. Tour page: 25 miles west. Vault FAQ Complete: 30 to 40 minutes. "Under an hour" in the locals hook holds. |
| Uber | FAQ vs vault | Live FAQ: "DO NOT RELY ON UBER." Vault FAQ Complete: Uber to the launch is fine, take the return shuttle. |
| Weather | FAQ | "If we call off a tour due to severe weather/cold and you are not able to reschedule, we do offer a full refund." Vault FAQ Complete: "full refund, no questions asked." Card 4 parked, so no change. |
| Sunset | Tour page | No sunset tour. 4:30 start, "golden hour and sunset opportunities" in autumn only. Quiz reworded (below). |
| Messenger lead form | OpenCX NKST, last 30 days | 0 Messenger sessions since 2026-09-15. Last Messenger session 2026-07-15. 18 sessions in 30 days, all web chat or phone. |
| Meta lead campaign | act_87863118, campaign 6983621892296 | PAUSED. Jul 1 to Oct 15: $52 spent, 27 leads, $1.93 per lead, 23 conversations replied. |
| Meta retargeting | campaign 52555873581500 | Campaign ACTIVE, its only ad set PAUSED, no insights in 30 days. NKST Meta spend is $0 right now. |
| Google Ads | file 02 | Both NKST campaigns paused (not re-pulled today). |

So: NKST has no paid traffic and no lead-form traffic today. Card 7 cannot be read until fills resume. Card 8 is the only NKST paid test with a path to volume.

---

## Card 7: Lead-form rescue (board: both, approved)

**Built:** one OpenCX workflow, INACTIVE, in the NKST workspace.
`DRAFT (inactive) Lead-form rescue A/B: Messenger lead form first reply (Funnel Lab card 7)`
workflow_id `482df656-3429-4c01-95d6-49e5e0b6413a` (OpenCX id 20677). Validated clean.

**What it does when activated**
1. Fires on the first message of a conversation, only if channel = Messenger and the text contains "New Orleans" (the lead form's "Do you live in New Orleans?" field).
2. Picks the arm from the ISO week: even weeks A, odd weeks B. Writes `leadform_rescue_arm` and `leadform_rescue_week` into the ticket custom data so reply rate can be counted per arm.
3. Sends the first reply:
   - **A (link first, one tap):** "Hey, thanks for reaching out! Here are the open Manchac swamp tours: [tour page ?ref=fbform-rescue-A] When are you thinking? Tap one:" with buttons This weekend / Next weekend / Just looking. (Messenger allows 3 buttons, so "Later this month" was dropped.)
   - **B (locals and first-timers):** "Hey! Lots of folks who live here have never paddled their own swamp, and most of our guests are first-timers. Calm water, stable sit-on-top kayaks, a guide in front the whole way, about 35 minutes from the Quarter. Want me to send this weekend's open times?" with buttons Yes, this weekend / A different date / Just looking.
4. Waits 2 hours. Asks the AI whether the guest replied (or a human took over, or they opted out). If not, one nudge on Messenger with price, where we meet and the tagged link. No SMS: there is no SMS consent on a lead form.
5. Booking links carry `?ref=fbform-rescue-A` / `-B`, which FareHarbor appends to the Online Booking Reference (file 20), so bookings per arm come from the Advanced Bookings report.

**Known risk, test before activating:** the AI agent also replies to the first message, so a lead may get two replies. Test path: `test_workflow` on a synthetic Messenger payload sends a REAL reply to that ticket, so run it on a test ticket only. If the double reply shows up, switch the trigger to `ai-response-requested` with "Ignore Automated AI Response" on, which lets this workflow be the only first reply.

**Sample:** 120 per arm to read 28% vs 45%. At the old $1.93 per lead that is about $460 of lead ads, roughly 60 days at $8/day. Today's volume is zero.

---

## Card 8: Locals who've never been vs visitors (board: both, approved)

**Not built in Meta.** Both API paths failed from this session: campaign create returned "Invalid parameter" twice and then was blocked by the auto-mode classifier as a real-world transaction; image upload returned "Application does not have the capability". Below is the paste-ready build for Ads Manager. Claude can build it via the Chrome bridge on mbp-2 (Profile 14) if David prefers.

**Campaign:** `NKST | TEST | Locals vs Visitors | Oct 2026`. Objective Traffic, optimize for Landing Page Views (no working purchase event, card 16 parked). Advantage+ campaign budget OFF (ad set budgets). Special ad category: none. Status PAUSED.

**Budget:** $15/day total, $7.50 per ad set, 14 to 21 days. My pick: carve it out of the $20/day retargeting campaign (52555873581500), whose only ad set is already paused, so total NOLA spend does not move.

**Read:** cost per landing page view and link CTR in Ads Manager; bookings per arm from FareHarbor Reports > Advanced > Bookings, Online Booking Reference contains `meta-locals-oct26` or `meta-visitors-oct26`. Check day 7, call it day 14 to 21.

### Ad set A: Locals
- Location: New Orleans, LA +25 mi, people living in this location (home only). Optional add: LaPlace, Slidell.
- Age 25 to 65, all genders. Advantage audience off, no interest narrowing.
- Placements: Facebook and Instagram feeds, Stories, Reels.
- Landing URL: `https://neworleanskayakswamptours.com/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/?ref=meta-locals-oct26&utm_source=meta&utm_medium=paid&utm_campaign=locals-vs-visitors&utm_content=locals`
- Image: the couple in the blue kayak under the big cypress (site photo IMG_1965.jpg, 4032x3024; 4:5 crop for IG from `Assets/Carousel Picks/new-orleans-manchac-swamp-kayak-tour-0204-4x5.jpg` or similar). Social platform: use originals, no compression.
- Primary text:
  > You live under an hour from this swamp. Ever paddled it?
  >
  > "Was definitely apprehensive of kayaking through the swamp, but PLEASE don't be!" (Google review)
  >
  > Manchac is 30 to 40 minutes from the Quarter. Stable sit-on-top kayaks, a guide in front the whole way, and most of our guests have never kayaked. $65 a person, tours year-round.
- Headline: `Your swamp. 40 minutes away.`
- Description: `Manchac kayak tours from $65`
- CTA: Book Now. Page: New Orleans Kayak Swamp Tours (1412223302323097).

### Ad set B: Visitors
- Location, my pick: New Orleans, LA +25 mi, **people traveling in this location** (catches visitors already in town, who book 1 to 3 days out). Alternative: United States, interests Adventure travel + Ecotourism + Kayaking, behavior Frequent travelers (the audience the old lead campaign used).
- Age 25 to 65. Same placements.
- Landing URL: `https://neworleanskayakswamptours.com/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/?ref=meta-visitors-oct26&utm_source=meta&utm_medium=paid&utm_campaign=locals-vs-visitors&utm_content=visitors`
- Image: red kayaks under blue sky, square (site photo New-Orleans-Swamp-Tour.jpg, 2448x2448).
- Primary text:
  > The best thing we did in New Orleans wasn't on Bourbon Street.
  >
  > "It was by far our best experience in New Orleans." (Google review)
  >
  > A guided kayak paddle through the Manchac cypress swamp: 2 hours, small group, $65 a person. Round-trip shuttle from the French Quarter is $25 more.
- Headline: `The swamp tour you'll still be talking about`
- Description: `Shuttle from the French Quarter`
- CTA: Book Now.

Both ads avoid "safe" wording (never assure safety). Both quotes are verbatim from NKST Google reviews (file 01 headline seeds).

---

## Quiz (cards c18 both, c19 B, c20 A, c21 A)

**Done in worktree** `~/Projects/fh-lead-engine-quiz-nkst`, branch `quiz-nkst`, commit 697f1ae. 219 tests pass, previews rebuilt (`previews/quiz/nkst-A.html`, `nkst-B.html`). Not deployed, not merged.

- Quiz A result "The sunset swamp paddle" is now **"The evening swamp paddle"**: "The last tour of the day: low light on the water, birds heading home and the owls waking up. In fall the 4:30 start runs into golden hour." Tour line: "Manchac swamp kayak tour, 4:30 pm start (times change by season)". Quiz B's Barred Owl result got the same tour line.
- `python3 engine/quiz.py check nkst`: 0 quiz items to verify. 2 email items remain, both the day-2 add-on line (free dry bag rental). David picked A (help first) on card c20, so the `offer_early` arm will not run for NKST; those two [VERIFY]s only block the arm nobody picked.
- Before the NKST quiz can serve: `brands.json` nkst has empty `address` and `phone` (engine refuses to send email without a postal address), `enabled` and `quiz_enabled` are false, and the card c19 pick (B, email first) means `quiz_gate_nkst` should ship with `email_first` as the default rather than as a running test.

---

## Open questions for David (also in 00 Start Here)

See the numbered list in the session message of 2026-10-15; the Start Here file carries the same list.
