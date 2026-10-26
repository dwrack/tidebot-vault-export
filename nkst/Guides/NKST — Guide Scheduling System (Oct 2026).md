# NKST Guide Scheduling System (Oct 2026)

*Drafted 2026-10-19, revised same day with David's answers. Status: PLAN, nothing built or sent yet. Replaces the "ask the channel for availability" approach, which failed 4 times this summer (Jul 22, Aug 2, Aug 17 x2).*

Related: [[Guides/NKST — Guide Availability Grid (Aug 2026)]] · [[Guides/Guide Scheduling — Tour Time Pick Order (Aug 2026)]] · [[Guides/NKST — Guide Hiring Plan (Aug 2026)]] · [[Guides/NKST — Guide Onboarding Matrix]]

---

## The goal in one line

Every slot has a confirmed guide plus one named backup. If a slot still can't be staffed, the guest already knows they might get moved, and our reservation workflow moves them before it becomes a problem.

## Why the old way broke

- Open-ended "what's your availability?" got silence. Guides won't hold unpaid time for tours that might not book (river, Jul 20). David will not pay standby (Aug 17). Both stand.
- Slack-only asks get missed. Guides don't live in Slack.
- One guide (Stephanie) carried 4 days alone. When she left for a week, 4 days went dark.
- FareHarbor assignments drifted from reality (Ryan Carr assigned while in Montana).
- No owner, so nobody chased it.

---

## Owners

- **David + Claude.** No manager in the loop (Michelle and Dylan are not managers, 2026-10-16).
- Claude runs the calendar, texts, confirmations, FareHarbor entry and audits, all from mbp-2 so it runs when the laptop sleeps.
- David approves: the monthly grid before it locks, any guest-facing reschedule, any cancellation, and the wording of every new text template.

---

## The system: 6 layers, each one catches what the layer above drops

### Layer 1: Every slot is 2 deep

Each recurring slot (day + time) gets a **Primary** and a **Backup**. The all-guides broadcast in Layer 3 is the third line, so nobody has to be named for it.

| Rule | Why |
|---|---|
| Nobody is Primary on more than 3 days a week | Kills the Stephanie single point of failure |
| Every guide holds at least 1 Backup spot | Spreads the load, keeps everyone sharp |
| Backups aren't on standby and aren't paid to wait. They just get asked first, and taking one earns rank points (Layer 2) | Respects the no-standby decision and still rewards people who say yes |

### Layer 2: Monthly pick cycle, in rank order

Guides pick their own slots, best-ranked first. Picking feels different from being asked for availability, and the people who show up get rewarded for it.

**Calendar (every month, picking for next month):**

| Date | What happens |
|---|---|
| **10th** | Next month's slots go out (text + Slack). Each guide's line comes pre-filled from last month: "You had Sun/Mon 10am. Keep it?" |
| **10th-13th** | Rank #1 confirms or changes, then #2, and so on. 8-hour window each (clock pauses 9pm-7am), then it passes down. Silence means they keep last month's line |
| **14th-15th** | Open slots and Backup spots go to everyone, first come |
| **15th** | David reviews the grid (one message, approve or edit) |
| **16th** | Lock. Claude enters assignments in FareHarbor |
| **17th** | Final grid posted and pinned. That keeps FH 2 weeks out, which the roster doc already requires |

#### Ranking: "Crew Points," built so new guides can climb fast

Rolling 90-day window, recalculated monthly, everyone can see their own number.

| Input | Weight | How it's measured |
|---|---|---|
| **Availability offered** | 25 | Slots picked and kept, counted as hours per month |
| **Backup and hard-to-fill shifts taken** | 25 | Backup spots held, low-demand slots (weekdays, winter, Thu/Fri), last-minute pickups under 72h. Taking these is how anyone moves up fastest |
| **Reliability** | 20 | Confirms by T-36h, zero late drops, pre/post-tour logs posted |
| **5-star reviews naming the guide** | 20 | Last 90 days, and only for tours FH shows they actually ran (the Alex Wallace anomaly is why) |
| **Tenure** | 10 | Capped at 2 years so it can't lock new people out |

Other inputs worth adding later, once the data is clean: photo/video posted to the channel, guest-count-weighted tours (a 12-person tour counts more than a 2), positive mentions in guest replies to the review text.

**Penalty:** a no-show resets reliability to 0 for the 90-day window. A late drop with cover found costs nothing.

**What keeps it from scaring off new staff:**
1. **Start in the middle, not at the bottom.** New guides start at the roster median, not zero.
2. **Rookie lane, first 60 days.** Two shifts a month are reserved for them before the open round, so veterans can't pick them out.
3. **A visible ladder.** Every new guide sees their next step, e.g. "take 3 Backup spots and you move up 2 places." The fastest climb is saying yes to hard shifts, which helps the business most.
4. **Rolling 90 days.** A veteran who coasts slides down and a new guide who hustles passes them within a season. Nobody is permanently stuck.
5. **Frame it as picking order, not a grade.** The channel post calls it "Crew Points: who picks first." It never shows a ranked leaderboard, so each guide sees only their own number and place.

### Layer 3: Confirm every tour, auto-escalate silence

This is the main backstop. Runs from mbp-2.

| When | What fires | If no answer |
|---|---|---|
| T-48h | Text to the assigned guide: "You're on Sat 10am Manchac, 6 guests. Reply Y" | Second ping at T-36h |
| T-24h | Still no Y: offer goes to the Backup (2h window) | Broadcast to all guides |
| T-18h | Still nobody | Escalate to David (text + #helm-nkst) and start the guest reschedule (Layer 5) |

Confirmations are logged, so reliability scores build themselves.

### Layer 4: Drop and swap rules

- **72h+ notice:** post it in the swap thread and backups get first shot. No penalty.
- **Under 72h:** you find cover, or it counts against reliability. Covering someone else's late drop earns hard-shift points.
- **Sick the morning of:** text the Google Voice line AND post in Slack. Escalation starts immediately.
- Every swap gets mirrored in FareHarbor the same day. If it's not in FH, it didn't happen.

### Layer 5: Slots stay open, guests are pre-warned and moved early

David's call: don't close unstaffed slots in FareHarbor. Instead:

**A. Flex choice at booking.** Every booking picks one option up front, which tells the guest they might get moved and tells us exactly what to do if we have to move them. Draft wording, needs David's edit:

> **If we need to move your tour** (weather, low turnout, or guide availability), what works best for you?
> - **I'm flexible:** move me to another time that day or another day. *(You get first pick of the new time.)*
> - **Upgrade me:** move me into an Extended or combo tour, or a different day. *(Upgrade at a reduced difference.)*
> - **I can't reschedule:** if my tour can't run as booked, refund me in full.

- Built as a required custom field on every FareHarbor item, repeated in the confirmation email and the FAQ.
- **Viator/GYG bookings** can't see the field, so they default to "can't reschedule" and Magnolia texts them the choice after booking.
- Open decisions: the perk for "flexible" (first pick of time, or a $5-10 credit?), the upgrade discount, and whether a low-turnout minimum exists (currently none on file).

**B. Reservation workflow, triggered by Layer 3 at T-18h, or earlier if a slot has no Primary at lock:**
1. Consolidate into another departure that day if one is running with a confirmed guide.
2. Otherwise act on the guest's flex choice: flexible guests get offered the next staffed times, upgrade guests get the Extended/combo offer, can't-reschedule guests get a refund.
3. Magnolia (OpenCX) sends the guest text. David approves any refund or cancellation. Never the bot alone.

**C. Early warning.** At lock (16th), any slot with no Primary goes on a watch list. If it books, that guest gets the reschedule offer days ahead, not the night before.

### Layer 6: Depth (the real fix)

Rules don't create guides. Targets:
- **At least 2 trained guides per slot** before the Mar-Apr peak (the true NKST peak per the FareHarbor history).
- Onboarding takes 2-3 weeks, so hiring has to land by **mid-January**. The Aug hiring plan (3 fixed-day guides, $150 referral bounty) still applies. Its status is unknown, so check it.
- **Paperwork gate (Oct 17 note):** no driver's license and W-9 on file means no picks and no first shift. Collect both in the first conversation when anyone joins the channel.

---

## Texting: the NKST Google Voice line (504-571-9975)

David's call (2026-10-19): use the Google Voice line, not Twilio and not his personal iMessage.

| | |
|---|---|
| **Why it works** | Guides already know and save this number. David sees every reply in the Google Voice app. It runs from mbp-2's logged-in Chrome (bridge lane `mbp2`) around the clock |
| **How Claude sends** | Playwright through the Chrome bridge on mbp-2, using the same flow as the Ebb & Ember batch (voice.google.com) |
| **Rate limits (learned 2026-09-11)** | At least 5 wording variants, first name in every message, 60-90 seconds between sends, max 15/hour, stop on the first "not delivered." The monthly kickoff to about 10 guides fits in one session. Daily T-48h confirms are 1-4 texts a day, well under the limit |
| **Reading replies** | Claude checks the GV inbox every 30 min for messages from guide numbers and logs Y/N/corrections. Guest texts are left alone |
| **Known noise** | This line also gets guest texts and the forwarded "[NKST] +1..." replies from the review texter, so guide messages are filtered by phone number |

**Fallback chain if Google Voice fails** (logout, flagged, Chrome down):
1. **David's iMessage on mbp-2.** Checked 2026-10-19: Messages there is signed in and sent texts today, so it can send from David's number via AppleScript with no laptop needed.
2. **TideBot group DM** (David + guide + TideBot) in Slack.
3. **Alarm:** if no confirm goes out by 10am on a tour day, #helm-nkst gets a "confirmations didn't send" alert.

Every text says "reply here or in Slack, either works." A reply in either place counts.

**Never** send a blank "what's your availability" again. Always a pre-filled line the guide confirms or corrects. That's what got answers on Aug 17.

---

## Failure modes and what catches them

| What breaks | What catches it |
|---|---|
| Guide never replies to picks | Silence means they keep last month's line. If they had none, their slots go to open picks on the 14th |
| Guide confirms, then no-shows | T-48h confirm, then the backup chain, then escalation and guest reschedule at T-18h |
| Top guide quits or travels (Stephanie case) | Max 3 Primary days, a named Backup per slot, then the all-guides broadcast |
| A whole day has nobody | Watch list at lock, guests pre-warned by their flex choice and moved days ahead |
| Bad weather / 1-person tour | Same flex choice and reservation workflow |
| Google Voice logged out or flagged | iMessage on mbp-2, then the TideBot DM, then the #helm alarm |
| mbp-2 down | Laptop iMessage plus manual sends (lane fallback per CLAUDE.md). The #helm "nothing sent" alarm makes the outage visible |
| Slack down | Texts still go out |
| FH assignments drift from reality | Monday audit: FH assignments vs confirmations vs pre-tour logs. Mismatches go to David |
| Rank feels unfair, new guides discouraged | Median start, rookie lane, visible ladder, no public leaderboard, rolling 90 days |
| Reviews credited to the wrong guide | Only counted for tours FH shows they ran |
| New guide shows up with no paperwork | No DL and W-9 means no picks. Checked at lock |

---

**Timing decision 2026-10-22:** pick window tightened from 12h to 8h per guide. First Winter round kicks off Thu Oct 23 (8 guides, about 3 days worst case).

## Oct 22 call additions (David, Jeff, Stephanie)

Folded in from the call. These change or add to the layers above.

| Rule | What it means | Layer |
|---|---|---|
| **Combo tours go to newer guides first** | Rookie lane is combo tours. During the plantation half, the combo guide cleans the vans. That's how newer guides earn their way into the 2-hour and Extended tours. Checklist + photo proof: [[Combo Tour Van Reset SOP]] | 2 |
| **One Backup day a week is required, not optional** | Every guide names 1 Backup day per week: takes any extra tour booked that day, or covers if the Primary is sick. Won't hold one = drops in pick order. No exceptions for veterans | 1, 2 |
| **Speed counts inside the rank order** | Within each pick window, replying fast keeps your spot. Slow replies pass to the next guide sooner. Creates a little healthy demand | 2 |
| **Text nudge, Slack does the work** | Not everyone watches Slack. The pick request posts in Slack, then a short text: "Your schedule pick is up in Slack, first to reply gets first choice" | 2, Texting |
| **Optional paid backup day** | A Backup can be offered a paid day as backup receptionist at the marina (phones, help Jeff). Idea only, not decided | 1 |
| **Guides own the weather call** | Contractors decide if it's safe to go out (lightning etc.). We respect it, then Layer 5 moves the guests | 5 |
| **The system runs it, not a person** | Not Jeff, not Stephanie. Ranking is data, so nobody can be accused of favorites | Owners |
| **Lives on the NKST dashboard** | Grid, pick status, and Crew Points get a panel on the NKST dashboard | Build |

**FareHarbor crew assignments (Claude does it, David 2026-10-22):**
- No FH API, so it runs through the logged-in Chrome bridge on mbp-2 (Playwright), same as the existing FH scrape.
- **At season lock:** assign the Primary as crew on every availability in the season, and put the Backup's name in the availability note.
- **Daily sync (morning):** re-check the next 14 days. Swaps, sick calls, and Backup pickups from Layers 3-4 get mirrored in FH the same day. Any slot with no crew goes to #helm-nkst.
- **Monthly check (10th):** anyone who replied CHANGE gets their FH assignments updated before the 16th.
- Guides never edit FH crew. If it's not in FH, the guide isn't on it, so FH stays the source of truth for payroll and the dashboard.
- Before the first run: confirm which Chrome profile has the NKST FH login, and test it on 1 week before doing the whole season.

**Open from the call:**
- ~~Pick cadence~~ DECIDED 2026-10-22: monthly, not 2 weeks. Built around **standing season lines**:
  - **Winter line (Nov-Feb)** and **Spring line (Mar-May)**: each guide picks a fixed weekly line (Primary days + 1 Backup day) once per season, in rank order. That's the only real "pick" round.
  - **Monthly check (10th):** one text, "Your line stays Sun/Mon 10am + Backup Thu. Reply CHANGE if anything's different." Silence = keep. No re-picking.
  - Changes in between go through the swap rules (Layer 4), not a new round.
  - Next real pick round: late Feb for the Spring line, so the Mar-Apr peak is set 2+ weeks ahead.
- Text channel for the nudge: call said iMessage, doc says Google Voice 571-9975. GV keeps it off David's personal number.
- Ranking inputs the call named: tenure, reviews, tips, and saying yes. Tips isn't in Crew Points yet (needs a tip source per guide from FH).

---

## Rollout

| Step | When | Notes |
|---|---|---|
| 1. Confirm which Google account and Chrome profile owns 504-571-9975, and that it's logged in on mbp-2 | First | Needed before any send |
| 2. Verify the live roster: who actually guided Sep-Oct (FH), phones current | This week | Payroll config lists 8 active (Michelle, Nick, Chelsea, Stephanie, River B, Alexis, Abbie, Josh). Phone roster is from April |
| 3. Build the Nov-Dec grid, pre-filled per guide from their last stated availability | This week | Winter: no 9am Nov 1-Dec 25 |
| 4. Draft the 5+ kickoff text variants and the Slack post for David to approve | This week | Kickoff ask: confirm or correct your line, plus the Crew Points explainer |
| 5. Send the kickoff via Google Voice, log replies | After approval | |
| 6. Lock November in FH | Within 5 days of kickoff | First lock is late. Normal cycle starts Nov 10 for December |
| 7. Flex-choice field on FH items + confirmation email + FAQ copy | November | David approves the wording and perks |
| 8. Build the T-48h confirm/escalate loop + Monday audit on mbp-2 | November | Run /design-review before building |
| 9. Hiring push for 2+ guides | Dec-Jan | Solo-ready by early March |

---

## Still open for David

1. Perk for "I'm flexible" (first pick of time, or a $5-10 credit?) and the upgrade discount.
2. Is there a minimum guest count for a tour to run?
3. Crew Points weights OK as drafted?
