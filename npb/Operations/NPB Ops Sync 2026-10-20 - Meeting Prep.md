---
type: meeting-prep
business: NOLA Party Barge
meeting: Tue 2026-10-20, 8:30a PT / 10:30a CT ops sync
created: 2026-10-19 by Claude for David
sources: OpenCX live (pulled 2026-10-19), Jeff call notes 2026-10-16, Ops Plan 2026-10-13, David's Apple Note "Nkst" (2026-10-19)
---

# Ops Sync Tue 10/20: Meeting Prep

Three topics. Each ends with the decisions to make in the room.

---

## 1. OpenCX: do we just answer handoffs, or teach it too?

**Both. Answering is the one-time fix; teaching is the real job.** If the answer doesn't go back into OpenCX, the next guest who asks the same thing gets handed off again.

Live, Sep 19 to Oct 19 (checked 2026-10-19): 233 conversations, 88.4% handled by the bot, 28 handoffs. What the 28 were:

| Why it handed off | # | Fix | Status 10/19 |
|---|---|---|---|
| Didn't know a fact (season, winter/heat, ice/cups, one seat cancels, kayaks, party bus, night trips, 75-person group, smoking) | 10 | Write the answer into OpenCX once | 9 of 10 covered: winter, ice/cups, big groups live; one-seat-cancel + "things we don't offer" drafted, waiting on approval. Smoking is covered (live FAQ: no smoking, vaping allowed, verified 2026-10-20) |
| FareHarbor says "slot no longer available" when it's open | 7 | Not a knowledge problem. OpenCX support ticket | Open |
| Pitches: creator collab, ad agency, sculptor, promo video, school donation | 5 | One rule each so the bot answers instead of handing off | Not built |
| Bot crashed | 3 | OpenCX's problem | Report with the ticket above |
| Waiver link request | 1 | Give the bot the waiver link | Missing |
| Discount ask | 1 | Hands off by design | Fine |
| Booking link not clickable in chat | 1 | Same ticket | Open |

**The loop going forward (proposed):**
1. Whoever answers a handoff answers the guest, then drops the answer in #helm-npb starting with `teach:`.
2. Claude turns it into an OpenCX entry within 24 hours. One person ✅'s it, it publishes.
3. Rule: the same question handed off twice must be taught. No exceptions.
4. Monday, Claude posts one line: new gaps, taught, still repeating.

**Decide tomorrow:**
- [ ] Publish the two drafts? (One-seat cancel says: refund or reschedule up to 7 days out, inside 7 days a friend can use the seat. Jeff confirms that's the real policy.)
- [x] **Heaters.** ANSWERED 2026-10-22 (David): boats get vinyl surrounds and heaters in winter, and we keep operating. OpenCX winter answer reworded to say vinyl surrounds, no longer says fully enclosed. (Original question: The winter answer went live today and tells guests "enclosed boats with heaters on board." Is that true this winter? If not, it gets pulled today. (Leteese Broussard was already told yes on 2026-10-20, David's call.))
- [ ] Smoking/vaping on board: live FAQ already says no smoking, vaping allowed (verified 2026-10-20). Still right?
- [ ] Price: the bot's profile says $63/person, FareHarbor sells at $59. One guest got quoted both. Which is right?
- [ ] Closed Mon/Tue in the off-season: the bot doesn't know yet. Start date?
- [ ] Donations: a form + automatic gift card (from David's 10/18 note), so the bot sends the form and nobody hand-handles it.
- [ ] Partnership/creator pitches: route to info@, bot says "we'll review it," no human handoff.
- [ ] Who owns the `teach:` step? Fits as one of Sophia's three things.

---

## 2. Getting Jeff on the business, not in it

**The hire and the phone flip are the plan.** Nothing else frees Jeff until those two land. Everything below is what happens once they do.

Where his week goes today (from 10/13 and 10/16): kayak schedule, kayak phones full-time, boat phones on weekends, van, property, crew, thin-day texting by hand every afternoon, about 3 hours a day at the desk. His words: "I certainly can't afford it."

| Task off Jeff's plate | Goes to | Unlock | Status |
|---|---|---|---|
| Phones + texts | Missed-call text-back + OpenCX; first mate on busy days | David flips the pilot (5 steps) | Built 10/16, dry run |
| Answering handoffs | Sophia answers, `teach:` loop shrinks it | Sophia's yes | Pitch due 10/20 |
| Thin kayak day texting | Revenue ladder bot | David OKs wording + GV sign-in | Built 10/13, gated off |
| Weather calls | One-command reschedule blast | Jeff's wind/rain cutoffs per boat | Waiting on cutoffs since 10/15 |
| 4th boat, guide call-out, van runs | Captain / ops lead hire | Hire | Target signed by 10/30 |
| Crew comms + pre-shift | Ops lead + TideBot | Hire | After hire |
| Schedule review | Sophia with Claude | Sophia's yes | Started 10/18? |

**Jeff's on-the-business job (his lane: brand, aesthetics, people, selling the vision):**
1. **Sell.** Corporate holiday parties (deck is built) and marina event hosting.
2. **Brand + content.** Footage board yay/nay, reels, Go-Cup local picks. He protected a 4.9 on 3,657 reviews; that's the asset.
3. **Build the team.** Hire and coach the ops lead and Sophia, one short 1:1 a week each.

**Make it stick:** Tuesday after the sync is his on-the-business block, phones on the bot (we're closed Tue anyway). Three numbers each week: hours on phones (should fall), handoffs he answered himself (should hit zero), event/corporate leads sent.

**Ask him tomorrow:** "If you got 15 hours a week back, what would you build first?" Let him pick the order. He'll own it if it's his list.

---

## 3. Captain / Ops Lead hire: who's the right person

**This is a different hire than the posting we drafted 10/13.** That one is a utility first mate on a day rate, a body for the 4th boat. What you described on 10/16 and in your note is an operations lead who also captains. Only the second one gets Jeff out of the weeds. Recommend we hire that one and retitle the posting. Draft v2: `Operations/Captain + Operations Lead - Job Posting v2 (DRAFT 2026-10-19).md`.

**The person, in one line (your note, 10/19):** logistics, scheduling, organized, and not afraid to vibe code.

**Must have (screen out without these):**
- USCG license that covers our boats, now. Jeff wants plug-and-play.
- Has run a schedule for a crew before: shift lead, bar manager, dispatcher, event ops, military NCO.
- Keeps their word. References confirm it.
- Comfortable on a computer and with AI tools. Will use FareHarbor, Slack, Claude daily.
- 3 to 4 days a week including weekends; flexible beats fixed hours.

**Nice to have:** TIPS, bar management (liquor license is coming), event sales, van + trailer. **Not needed:** boat mechanics.

**Where to look:** Max first (license, rate, availability were due at this sync). Then recent captain-school grads, bartenders and bar managers who hold a license, charter fishing mates who just upgraded, veteran transition boards.

**Interview (30 min, Jeff + David):**
1. Tell us about a day on the water that went sideways and what you did.
2. Saturday, 4 boats out. A captain calls out at 9am, a group of 12 is running late, wind is gusting near our cutoff. Walk us through your next hour.
3. You're the new person and the crew communicates five different ways. How do you get everyone on one?
4. Which days will you commit to even if nothing books? Which days won't you work? (from your note)
5. What would you have running by day 30?
6. Quick practical: here's a messy week of bookings and crew availability. Build the schedule with any AI tool you like, 15 minutes, while we watch.
7. Housekeeping on day one: license copy, driver's license, W9 before first pay.

**Then:** one paid working shift as mate with our best captain, then decide. Target: signed by Fri 10/30.

**First 90 days if hired:** day 30 runs the Saturday floor solo with pre-shift comms through TideBot. Day 60 owns the crew schedule, weather calls, and the handoff queue. Day 90 owns one project (liquor permit or the event pipeline).

**Decide tomorrow:**
- [ ] One role (captain + ops lead) or two (utility mate now, ops lead later)? Recommend one.
- [ ] Pay. A mate day rate won't land the ops-lead person. Day rate on captain days plus a weekly ops rate is one shape; your number.
- [ ] Is the old posting live? The draft still had blank rates as of 10/13. Swap in v2 either way.
- [ ] Max: did Jeff get the three answers?
- [ ] 1099 vs employee for a captain: the Jones Act question from May is still open. Worth one call with Michael before the offer goes out.

---

## 4. Crew scheduling: NKST + NPB

**NKST (plan drafted 10/19, nothing sent yet):** full doc at `New Orleans Kayak Swamp Tours/Guides/NKST — Guide Scheduling System (Oct 2026).md`. Short version:
- Guides pick next month's slots on the 10th, in "Crew Points" order (availability, backup/hard shifts taken, reliability, reviews, tenure capped). New guides start mid-pack with 2 shifts a month reserved so it doesn't scare them off.
- Every slot is 2 deep: Primary + Backup. Then a broadcast to all guides.
- A text goes out 48h before each tour from the NKST Google Voice line: "Reply Y." No reply means the Backup gets it, then everyone, then David at 18h.
- Slots stay open. A guest flex choice at booking (flexible / upgrade / can't reschedule = refund) covers weather, low turnout and guide gaps.
- Owners: David + Claude. **Jeff's role here is a question for tomorrow.**

**NPB: the weekend captain problem.** A captain calling out on a Saturday kills a whole boat and a group's party. Options, best first:

1. **Backup captain works crew on weekends (David's idea, recommended).** One licensed captain is scheduled as deckhand on each busy weekend day. They earn normal deckhand pay plus the existing "weekend lead" line item, and they're paid for real work, not standby. If a captain calls out, they step up and a deckhand moves over. Cost is about one weekend-lead add-on per weekend.
2. **The Captain + Ops Lead hire is the floater.** If we hire the role in section 3, they're the default backup captain on Saturdays. This stacks with option 1 and doesn't replace it.
3. **Grow a captain from inside.** Sponsor our best deckhand through the USCG license course with a 1-season commitment. Slow (months), but it's the only option that adds depth for 2027.
4. **On-call captain from another operator.** A licensed captain from a friendly charter at a day rate, only when needed. Good last resort, but it doesn't scale.
5. **Same 48h confirm + flex policy as NKST.** The crew confirm text comes from the NPB Google Voice line (504-264-1056). Private charters are harder to move, so the flex policy may only fit public cruises. Discuss.

**Ask Jeff:**
- [ ] How many captain call-outs or near-misses this season, and on which days?
- [ ] Which captains hold a license that covers every boat, and would any of them take weekend crew shifts as the backup?
- [ ] Is weekend-lead pay enough to make the backup-captain spot wanted, or does it need its own line item?
- [ ] Do the 48h confirms + flex policy work for NPB, or only for public cruises?
- [ ] NKST: does Jeff want a role in guide scheduling (approving the monthly grid?), or does it stay David + Claude?
- [ ] Captain doing deckhand work: any 1099 / Jones Act wrinkle? (Michael)
