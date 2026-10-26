> **UPDATE 2026-10-22:** David: launch simple, newsletter only, NO discount codes until pricing is fixed and codes exist. Arm A ($10) is paused and the Mautic idea is dropped in favor of the existing lead engine. Live status in [[Website Standards — CRO + Opt-In (All Sites + Rebuild)]].

# Post-Price Opt-In Funnel: All Brands (Oct 2026)

Growth play #3 in [[Growth Plays Rollout — All Brands (Sept 2026)]]. It came out of [[Website Fix Plan — Tom Barnes CRO Lessons (Oct 2026)]]. Status: spec only, nothing built, nothing sends without David's tick.

**The idea:** prices stay visible. Only *after* someone has looked at prices and not booked, we offer one of two things for their phone or email:
- **"$10 off your first trip"** (needs a deadline), or
- **"Text me when Saturdays open"** (date alert, no discount).

Then a short nurture sequence timed to their trip date, ending in a FareHarbor link with a `ref=` so we can count the bookings.

## Pilot: NPB, then HPB, then the kayak brands
- NPB has the most traffic. The OpenCX widget and SMS (Twilio relay, review SMS) are already live there, and the SES win-back runner already exists on mbp-2.
- HPB is second because its sticker vs checkout gap (16%) makes the "$10 off" easy to justify.
- NKST, BBK, AKT and DCKT copy the winner. DCKT waits for the 2027 season. E&E runs on Période, not FH, so it needs its own build.

## Economics (rough, flag as a guess)
- NPB average booking: $224 (2025 boats). Public seat: $59.
- The $10 code is good on 2+ guests only, so a $118+ order pays $10 (8%). Don't give $10 off a single $59 seat.
- Break-even: if 5% of opt-ins book, each opt-in is worth about $11 in revenue (0.05 x $224). Ad cost per opt-in has to stay well under that. **Lead-to-book rate is unknown until the pilot runs.** Play #2 (put a dollar value on leads) uses this number.

## Who sees it, and when
- **Never** for someone who's on the FH lightframe or came from Google search with "book" in the query. High-intent people go straight to Book Now.
- **Show it** on a tour page after 30+ seconds and a scroll past the price, or on exit intent on mobile (back-swipe or tab switch). Show it once per visitor per 7 days.
- **Tool (corrected 2026-10-22): the existing fh-lead-engine, not Mautic.** It already has the popup widget, a hosted signup page (`/s?b=<brand>`), SES sending, one-click unsubscribe and suppression. NPB is live in `newsletter` mode (no codes). See [[Website Standards — CRO + Opt-In (All Sites + Rebuild)]].
  - OpenCX stays the chat and DM layer. It doesn't run the popup.


## Found 2026-10-20: NPB's current lead capture probably goes nowhere
On every NPB page, the top banner "Not ready to book yet? Get early access" links to `/new-orleans-booze-cruise-giveaway/` ("Win a Trip!" in the nav). That page embeds a **GoHighLevel form** (`api.leadconnectorhq.com/widget/form/4j807tEnDSik2z0bRnPU`, "Nola Pedal Bargen Optin Giveaway"). The form still loads (HTTP 200), but GHL was retired on 9/24. Entries most likely land in an account nobody checks. I couldn't check this without a GHL login.
- Fix: replace that iframe with the Mautic form. Keep the banner and the page, because they already get traffic.
- None of the other 5 FH sites has a GHL form or an early-access bar.

## Capture flow (3 taps, contact last)
1. "Planning a trip?" Pick a date: This weekend / Pick a date / Not sure yet, pick a month. Small print: "You can change this later."
2. "How many in your crew?" 2 / 3-6 / 7-15 / 16+ (16+ goes to the private charter quote flow instead).
3. "Where should we send your $10 code?" Phone (SMS) or email. Then the TCPA consent checkbox, STOP language and a link to the privacy policy.

On submit: show the code right away, with a Book button deep-linked to that date's FH calendar (`?full-items=yes&ref=optin-<brand>`).

## Nurture sequence (timed to the trip date, 4-5 touches max)

| # | When | Channel | What |
|---|---|---|---|
| 1 | Instantly | SMS or email | The code, the date they picked, and a Book link. |
| 2 | +1 day | Email | Proof: 3 short reviews + a guest photo. One line on rain ("covered boats, it runs rain or shine"). |
| 3 | 7 days before their date, or +3 days if they picked "not sure" | SMS | "Saturday the 24th has X spots left" (only if it's true, from FH availability). |
| 4 | 48 hrs before the code expires | Email | Reminder that the code ends, plus free reschedule up to 72 hrs out. |
| 5 | The day after their trip date, if they didn't book | Email | "Missed this one? Here's next month." Then they leave the sequence. |

**"Text me when Saturdays open" variant:** only touch #1 (confirmation) runs at first. A text goes out when FH adds or frees Saturday slots, then touches #2 and #4 run. No discount needed.

Rules:
- Every email gets a hosted one-click unsubscribe (RFC 8058 URL header, never mailto).
- Opt-outs are suppressed across every brand.
- SMS quiet hours: 9pm-9am local.
- Sign as the business, not a person.
- Stop the sequence the moment their email or phone shows up on an FH booking.

## Tracking
- FH `ref=optin-npb-sms`, `ref=optin-npb-email`, `ref=optin-npb-satalert` on every link (David prefers FH ref over UTMs).
- Count opt-ins by brand, by source page and by mobile vs desktop.
- Fire a Meta Lead event and a GA4 `generate_lead` with the value from play #2 once the lead-to-book rate is known.

**Benchmarks:**
- Opt-in rate: 3%+ of people shown the offer.
- Lead-to-book: 5%+ within 30 days.
- If opt-ins come in under 1%, change the offer before adding anything else.

## Blockers to clear first
1. **SMS marketing consent and A2P:** "$10 off" is marketing. The "Marketing A2P" campaign FAILED, and the only verified campaign is Low Volume Mixed. Check whether marketing texts are allowed on it. If not, re-file before any promo SMS goes out. Email can start first.
2. **Email reputation:** the SES complaint rate was 0.158% on 10/13 (Amazon's review line is 0.1%), and it's shared by NPB, HPB and DCKT. Send pilot email from a separate subdomain or through SendGrid, and keep volume small.
3. **OpenCX capability check** (above).
4. **Fix the surprise fee first** (website plan, week 2). A $10 code doesn't help if checkout still adds $14.45 at the last step.

## A/B test (3 arms, updated 2026-10-20)
Same trigger and pages on NPB, split evenly three ways, run for 4 weeks (three arms need more traffic than two):
- **A:** "$10 off your first trip (2+ guests)"
- **B:** "Text me when Saturdays open"
- **C:** "Win a private weekday party boat for your crew" (giveaway)

**Winner:** the most FH bookings by `ref` within 30 days of sign-up. Not the most sign-ups. C will win on sign-ups because giveaways always do. The question is whether those people ever book.

**Arm C rules (it's a sweepstakes, so it needs real rules):**
- **Prize:** one private weekday charter (Mon-Thu, non-holiday, booked within 90 days). It uses empty weekday slots, so the real cost is fuel and crew. Put the ARV in the rules (use the current private weekday price, David to set).
- **No purchase necessary.** Add official rules on the giveaway page with: entry period, eligibility (21+ if the boat is BYOB, US residents), how the winner is picked (random draw), odds, ARV, sponsor = the business name, and void where prohibited.
- Under $5k ARV means no NY/FL registration or bonding needed. LA and TX have no registration either. Not legal advice; have the rules read once before launch.
- **One winner per month.** Announce it publicly (with permission) so it's clearly real.
- **Every non-winner gets a consolation offer** in the same email: "You didn't win this month, but here's $10 off for 2+ guests through [date]." This is where C makes its money.
- **Bonus entries** for sharing a personal referral link, not for following or tagging. That keeps it clear of Meta's promo rules and brings in friends who might book.
- **Kayak brands' version:** "Win a private kayak tour for 4" (NKST, BBK, AKT; DCKT in 2027).

## Pilot copy (draft, staged, nothing live)
- **Widget opener A:** "Still deciding? Grab $10 off for 2+ guests. Takes 3 taps."
- **Widget opener B:** "Saturdays sell out first. Want a text when one opens up?"
- **SMS #1 (A):** "NOLA Party Barge: here's your $10 code, BARGE10, good for 2+ guests through [date]. Book your [date] here: [link] Reply STOP to opt out."
- **SMS #1 (B):** "NOLA Party Barge: you're on the Saturday list. We'll text you the minute a spot opens. Reply STOP to opt out."
- **Widget opener C:** "Win a private weekday party boat for you and your crew. New winner every month. Enter in 3 taps."
- **SMS #1 (C):** "NOLA Party Barge: you're entered to win a private weekday boat for your crew. We draw [date]. Want extra entries? Share your link: [link] Reply STOP to opt out."
- **Non-winner email (C):** subject "You didn't win this month, but here's $10 off". Body: "Our [month] private boat went to [first name, city]. You're still in for next month's draw. In the meantime, here's $10 off any public cruise for 2 or more, good through [date]: [link]"
