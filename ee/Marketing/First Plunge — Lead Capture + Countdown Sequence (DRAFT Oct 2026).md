# First Plunge: lead capture + 7-day countdown (DRAFT)

Status: DRAFT 2026-10-13, nothing built. Launches with the 11/1 pricing change.
Offer per Jonah's #pricing-revamp proposal (10/11): 3 visits in 30-45 days for $99. **Price and window not final. Confirm before build.**
Owner to build: L (ActiveCampaign + Periode code) and Jess (Squarespace banner/popup).

## How it works

1. Visitor sees the banner (every page) or popup (once per visitor) and taps it.
2. Form asks for first name, email, optional phone with a text-consent checkbox.
3. ActiveCampaign tags them `first-plunge-lead` and stamps a custom date field `fp_expires` = signup date + 7 days.
4. They get the code right away and a 7-day countdown series. Every email shows a live countdown timer to *their* `fp_expires`.
5. The moment they buy, they exit the sequence (see "Exit" below). Day 7 ends it either way.

## Build notes (the parts that need decisions)

- **Countdown timer in email:** ActiveCampaign has no native per-person timer. Use a countdown GIF service that takes the deadline in the image URL, so the URL is built from the `fp_expires` merge field. MailTimers and Sendtric are the usual ones; L should confirm whichever she picks supports a per-contact end date before building around it.
- **Making the code actually expire:** Periode codes can be limited by valid-until date, product, uses and seats (L confirmed in #pricing-revamp), but we can't mint codes per person by API. Simplest honest setup: one code per weekly cohort, e.g. `PLUNGE-1101` valid 14 days. The email deadline is 7 days; the extra week is a quiet buffer so nobody gets an error at checkout. After that, the code is dead.
- **Exit on purchase:** Periode doesn't send punch-pass purchases to ActiveCampaign (L, July). Until that's fixed, the daily sync has to check redeemers of the cohort code and remove them, or buyers keep getting "last chance" emails. This is the one must-have before launch.
- **Texts:** the two SMS touches only go to people who ticked the consent box. Twilio's 10DLC approval was last known IN_PROGRESS (June 3), unverified since, so check before relying on it. If it's not approved, skip the texts and the emails still run.
- Use the Discount Template + internal note for the code so it rolls up in L's discount tracking.

---

## 1. Banner (Squarespace announcement bar)

A/B:
- **A:** First time on the river? 3 sessions for $99. Get the offer →
- **B:** New here? Your first 3 sessions, $99. Offer runs 7 days →

## 2. Popup (once per visitor: 20s on mobile, exit-intent on desktop)

**Headline:** Your first three sessions, $99.
**Body:** Heat, the river, then do it again. Three visits in [30] days, and the offer's yours for 7 days after you sign up.
**Fields:** First name · Email · Phone (optional)
**Checkbox:** Text me the code and a reminder before it expires. Msg & data rates may apply. Reply STOP to opt out.
**Button:** Send my code
**Small print:** One per person, first-time guests only.

**Thank-you state:** Check your inbox, your code's on the way. The clock starts now: 7 days.

## 3. Email sequence (all signed "Ebb & Ember", reply-to davey@ per house rule)

Every email: countdown timer at the top, button above the fold, code in plain text under the button.

**Email 1: immediately**
- Subject A: your three sessions are waiting
- Subject B: here's your code (7 days)
- Body: Here's your code: **[CODE]**. Three sessions for $99, use them within [30] days of your first one. Book your first by [fp_expires, e.g. Sunday Oct 26]. [Button: Book my first session]
- PS: First time in a floating sauna? Here's what to bring. [link to FAQ]

**Email 2: day 2**
- Subject A: what actually happens in a session
- Subject B: never done a sauna and a river plunge?
- Body: Short walkthrough: arrive, change, heat, river, repeat, lounge. Who it's for (first-timers welcome, go at your own pace). [Button: Pick a time] Countdown: 5 days left.

**Email 3: day 4**
- Subject A: what people say after their first one
- Subject B: [one real guest quote, short]
- Body: 2 or 3 real Google reviews. **Pull actual reviews from GBP. Do not write these.** [Button: Use my code] Countdown: 3 days.

**Email 4: day 6 (24 hours left)**
- Subject A: your $99 offer ends tomorrow
- Subject B: 24 hours left on your three sessions
- Body: Two lines. Code, deadline, button. Mention the slow weekday slots so it feels easy to find a time.

**Email 5: day 7, morning (last day)**
- Subject A: last day for your code
- Subject B: this ends tonight at midnight
- Body: One line, the button, the timer. That's it.

## 4. Texts (consented phones only)

- **Day 5:** Ebb & Ember: your 3-for-$99 code [CODE] expires in 2 days. Book here: [link] Reply STOP to opt out.
- **Day 7, ~10am:** Ebb & Ember: last day for your 3 sessions at $99. Code [CODE] ends at midnight. [link]

## 5. After the deadline

- Didn't buy: drop into the general newsletter list (they opted in on the form). No more First Plunge pushes for 60 days.
- Bought: hand off to Jonah's retention plan (day-10 rebook text after visit 1).

## Open questions for the team

1. Final price and use-within window (30 or 45 days)?
2. 7-day deadline OK, or 5?
3. Who owns the "remove buyers from the sequence" sync, L?
4. Popup on all pages, or skip the booking pages?
