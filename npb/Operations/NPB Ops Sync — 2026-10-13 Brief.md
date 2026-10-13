# NPB Ops Sync, Tue Oct 13 2026, 10:30a CT (30 min)

Attendees: David, Michael, Jeff, JT
Built 2026-10-12 evening from live Meta, Google Ads, GA4 and GBP pulls, plus #helm-npb Oct 5-12. Extends the carousel agenda in `NPB Ops Sync — 2026-10-13 Agenda.md`.

## Agenda (30 min)

| Min | Topic | Lead | Outcome needed |
|---|---|---|---|
| 0-4 | Weekend recap | Jeff | Numbers + what the storm cost us |
| 4-10 | Jeff's load: what moves to JT this week | Jeff + JT | 2 named duties handed off, with a start date |
| 10-14 | Bathroom/septic | Jeff | Temp fix by Fri, permanent quote by Oct 20 |
| 14-18 | Weather/cancel policy | Michael | One policy, posted on site + OpenCX by Fri |
| 18-21 | Slack fatigue: new rules | Michael | 1 bot message/day, what JT posts |
| 21-27 | Carousels + ads | David | Halloween yes/no, ad calls below |
| 27-30 | 1-2 items per person | all | Read back owners + dates |

## 1. Weekend recap (Oct 9-11)

- Friday morning, on the books: **92 guests / 20 bookings / $12,368**. Same point last year: 120 guests / 33 bookings. That's **-23% pacing**.
- Friday was rescheduled for wind. Saturday ran only the 2 tikis because the pedal wheelers were too sketchy in the gusts. The boats were strapped down well (good job Jeff).
- Reviews: 4.9 on 3,644 reviews. 37 came in Oct 4-12, none under 4 stars. Guests named captains Eddie, Kelly, Mike and Jeffery.

**Ask:**
- How many guests did we actually lose to the storm, refunded vs rescheduled?
- Who tried to cancel and got kept on (JT's point)? Did any of them convert?

## 2. Jeff is overloaded (his Slack note this week)

He's now carrying the kayak schedule, kayak phones 7 days a week, van maintenance, weekend boat phones, property and ops. He put it "on record" and said the Slack feedback load adds to the stress.

**Proposal:**
- JT takes **weekend boat phones** starting this Sat (that's already tracker item #28) **plus the kayak schedule**.
- Jeff keeps property, crew and captains.

**Ask:**
- Jeff, if you could drop 3 things tomorrow, what are they?
- JT, which of those can you own starting this week?
- Who is the backup when JT is off?

Don't leave without names and a start date. If it stays vague, Jeff burns out in season.

## 3. Septic / bathrooms

The plumber says the septic well is cracked and lets bayou water in. When the water's high, the tank fills and toilets can't drain. The marina flow was "ironed out" in June, so this undoes the restroom win.

**Proposal:**
- Temp: a porta potty this week. Cap it, and remember the old one was $1,000/mo.
- Permanent: 2 quotes to replace the well.

**David's idea: a backflow (backwater) valve, about $1,000.** Ask the plumber this exact question: "Is the water getting in through the crack, or flowing back up the line?"
- **Flowing back up the line:** the valve helps.
- **Coming in through the crack:** the tank still floods. The valve then just shuts and the toilets still can't drain. It protects the building, not the bathrooms.
- Also ask what it costs to seal or line the crack (or add a riser and a sealed lid) vs replacing the whole well.

**Ask:**
- Did guests notice this weekend?
- Who's getting quotes, and by when?
- Does this touch the occupancy permit inspection that's still open?

## 4. Weather / hurricane policy (unclear last week)

Last week's thread went around in circles: credits vs refunds, pre-cancel or not.

**Proposal (Michael to confirm):**
- **We cancel for weather:** guest picks reschedule or full refund.
- **Guest cancels inside 7 days over a forecast we're still running in:** credit, not refund.
- **Call time:** 24h before for storms (or 2h for day-of wind), same as the Eco Tour rule.
- Owner posts it on the site FAQ + OpenCX by **Fri Oct 16**.

**Ask:** Is the pedal wheeler wind limit written anywhere? Saturday's call was a judgment call, and it should be a number.

## 5. Slack fatigue (Michael: "limit it to one message a day")

**Proposal:**
- Claude + TideBot post **one combined digest/day max** in #helm-npb, at 8am CT.
- Reddit focus mode **pauses**. The current thread has been stuck since ~Oct 6 waiting on Jeff and Michael.
- JT's daily update becomes **3 lines max**: plan, problem, photo. Or a 30-sec voice note.
- Everything else waits for Tue/Thu.

**Ask:**
- **Michael, what info is NOT important for Slack?** Which posts would you kill outright (Reddit nudges, review texter updates, weekend pacing, coaching)? Whatever's left is the daily digest.
- JT, what format will you actually do every day?
- Jeff, do you want Reddit at all, or drop it?

## 6. Ads (live numbers, pulled Oct 12)

| | Last 7 days (Oct 5-11) | Week before | Call |
|---|---|---|---|
| Meta, Gator Collision campaign | $1,122 / 14 purchases / **$80** each | $71 each | v1 ads alone Oct 10-11: **$40** each (8 purchases). Holding near the $36.50 target. Leave it a full week. |
| Meta, Planner's Win v1 | $153 / **0 purchases** | | Pause candidate |
| Google NOLA, all enabled | $1,862 / 16.8 conv / **$111** each | $73 each | Getting worse |
| Google, Local | $350 / 2 conv / $175 | $77 | Worst one |
| Google, PMax | $408 / 7 conv / $58 | $33 | Best one |

- The paused Google campaigns still burned **$355 this week** (0 conv) before the cuts landed.
- Boost Rebuild Meta campaign: still not live. **Decide:** publish it or kill it.

**Google brand audit (30 days, Sep 12-Oct 11, pulled Oct 12):**
- **Brand searches cost $1,507, which is 32% of spend.** CPC runs $0.93-$3.53, and the "freaky tiki" terms are the priciest at $2.62-$3.53. These are people already searching for us. With little competition, most of them would likely come in through organic for free, so the 8.6x ROAS overstates what we're actually gaining.
- **Brand terms are negated nowhere.** National, Local, PMax and the paused Brand campaign can all bid on our own name, and none of them has a cap. National and Local both run "Max conv value" with no target, which is the runaway part.
- **The real leak:** the 2 Nola-Kayak campaigns spent **$1,799 at 0 conversions** before they were paused.
- **7-day ROAS:** National 1.1x, Local 1.0x, PMax 4.3x. The storm weekend and conversion lag explain part of that, so don't panic-cut off one week.
- **Proposed setup:**
  1. Brand gets its own Search campaign, exact and phrase only, **max CPC cap about $1.00**, about $15-20/day.
  2. Negate brand terms in National and Local, and add a brand exclusion in PMax.
  3. National becomes non-brand only, with a tROAS of about 4x so it can't run away.
  4. Fold Local into National. It only gets 16% impression share.
  5. Check auction insights in the UI first (the API can't see them) to confirm nobody else bids on our name.
- **Expected saving:** roughly $800-1,000/month on brand, and National gets measured honestly.

**Ask Michael:**
- Who manages Google Ads weekly from here, with a written guardrail (target cost per conversion + weekly cap)?
- Pause Planner's Win v1?
- Shift Google Local money into PMax?

## 7. Quick hits (one line each, skip if short on time)

- **Weather plan (David: weather is a serious contender for our ability to make money).**
  - Idea 1: cut ad spend automatically 1-2 days before a bad forecast, then push spend into the next clear weekend.
  - Idea 2: market a "weather-proof booking" promise. Free reschedule if we call it, so storms stop scaring off bookings.
  - Ask: what's our wind limit per boat?
  - **Decide (yes/no each):**
    1. Do we want ad spend to cut automatically before bad-weather weekends? If yes, who approves the forecast rule? (Claude builds it this week.)
    2. Do we want to advertise the weather-proof booking promise on the site and in the ads?
    3. What wind and rain numbers cancel a trip, per boat (tikis vs pedal wheelers)? Jeff to set them.
    4. Who makes the weather call, and how far ahead? Proposal: 24h out, plus a day-of check 2h before.

- **New address 2105 Paris Road:**
  - What's the one official address? Then fix GBP, Apple Maps, Yelp, FareHarbor emails and the site.
  - Gas station photos still owed to "her." Jeff, who is that and when?
- **Captain Mike:** issue handled. Is the "next time = termination" in writing?
- **TIPS certs:** due Oct 9. Who's done, who's missing? (Insurance requires it.)
- **Captain's licenses:** David asked last week. Who's signing up?
- **Costume trunks:** JT, did they make Oct 10? Rental price?
- **Review texter:** turn on the first-name version for NPB? 10-min swap.
- **Review reply tone:** someone replied "hard to know how to improve without feedback" to a 5-star. Replies need to sound grateful, not defensive. Who replies to reviews now?
- **Win-back email w10 sends today (Oct 13).** FYI.

## 8. Carousels (from the original agenda)

- 10 NPB carousels are staged, plus 1 Halloween each for NPB, Booze Cruise and Admire. They need a yes this week to run before Sat Oct 31.
- **The price question is already settled:** FareHarbor, the site and Meta ads all say **$59 pp / $1,200 private** (fixed Sep 30 to Oct 1). Use that on every slide.
- Ask: does anything on the slides misstate BYOB rules, routes or what's included?

## Closing read-back (owners + dates)

| Person | Proposed 1-2 items this week |
|---|---|
| Jeff | Septic temp fix + quotes. Hand off weekend phones + kayak schedule to JT. |
| JT | Owns weekend phones from Sat. 3-line daily update. |
| Michael | Approve weather policy wording. Ad calls (Planner's Win, Google Local, Boost Rebuild). |
| David | Carousel review after Oct 15. Address cleanup across listings. |

## Questions to keep in your pocket

- "What's the one thing that would make next weekend easier?"
- "What's on fire that isn't on this list?"
- "Who's doing it, and by when?" Use this on anything that ends in "we should."
