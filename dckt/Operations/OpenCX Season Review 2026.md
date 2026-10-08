# OpenCX Season Review 2026 (DCKT)

Pulled 2026-10-07, read-only, from the `opencx-dckt` workspace (385 sessions, Apr 25 to Oct 5). Nothing in OpenCX was changed.

## Bottom line

1. The "84 dropped handoffs" is really 86 today, and 23 of them were already resolved by staff. The Aug 10 "Nudge unbooked inquiries" workflow reopened them. True still-open money/complaint items: 12, and only 4 are urgent.
2. Urgent: Bobbi Tobalsky asked 3 times (Aug 11, 15, 18) for a July 5 weather refund and never got an answer in OpenCX. Also check Webster cancel (#370), Dawn Hernke partial refund after a medical turnaround (#88), and the $95 vs $75 overcharge complaint (#194).
3. The phone line routed through OpenCX is broken. Since Aug 24, about 37 calls show "call setup failed" or empty, and on Oct 2 a guest typed "tried to call but won't go through." With e-bike rentals still running, this is the one thing to fix this week.
4. The automated follow-up system never worked. The Router failed 294 of 294 runs on a variable bug, so no hot/warm/cool follow-up fired all season. The Aug 10 Nudge workflow then sent 317 generic messages to 67 people and got 0 replies.
5. Cedar answers in about 17 seconds and handles booking links, weight limits, ages and pregnancy routing well. It fails on booking lookups (asks for a UUID nobody has), simple policy gaps (dogs, e-bike limits) and internal email it should never have seen. Dropped leads cost roughly $900 in expected bookings. The broken phone and dead follow-ups cost more, but I can't measure it.

Recommendation counts for the 86 open tickets: **71 close, 3 reply, 12 needs David.**

---

## Urgent items (money, complaints, injury, fraud risk)

| # | Who | Issue | What to do |
|---|---|---|---|
| 298 / 309 / 312 | Bobbi Tobalsky, 920-750-2495 | July 5 weather cancel. She was offered a refund, asked 3 times in Aug ("my daily inquiry"), and got no reply in OpenCX | Check FareHarbor for the July 5 booking. If it wasn't refunded, refund it and text her. Highest priority |
| 370 | Brian/Brittney Webster, 715-499-0832 | Asked to cancel a Sep 27 kayak tour on Sep 26 at 9:49am CT. No reply | Check whether the cancel was processed and if they were charged. Refund if it was inside policy |
| 88 | Dawn Hernke, 920-659-1657 | Husband had cramping and wheezing, so they came back in minutes. Guide mentioned a partial refund. Closed Jun 14, reopened by workflow | Confirm the partial refund was actually issued. Treat this as an incident record (medical) |
| 194 | Austyn Patefield, 262-455-0106 (angry) | Charged $95/person vs $75 advertised for the shipwreck tour, saw no shipwrecks, felt misled. Cedar opened with "We don't process refunds" | Closed Jul 12, so verify a credit or refund went out. Pricing display issue worth checking for 2027 |
| 53 | "Madeline Ponder" from cinacarmarce@gmail.com | Asks how to change her payroll bank account | **Likely payroll-diversion phishing:** a guide's name sent from an unrelated Gmail. Confirm with Madeline directly that no banking change was made in Homebase/payroll |
| 221 | Pam Delfosse, 608-212-3395 | 3 people couldn't paddle (air quality), notified late. No reply | Decide on a credit or refund. Probably a gift certificate |
| 209 | Tom Hartigan, 720-312-2854 | SUP pickup missed, so the board was left on the Deck House front deck | Confirm the board and gear were recovered |
| 220 | Kathy Casper | Rental paddle bag had no paddle (full of sand). Asked not to be charged for the missing paddle | Make sure no missing-paddle charge hit her card |
| 130 | Adam Krueger, Future Urban Leaders | 501c3, asked to remove sales tax from the final bill (Jul 14 group of up to 20) | Check whether a tax adjustment is owed |
| 255 | IG user (anonymous) | "Planning on reporting your ass to the DNR," named Dave Rack | No reply. For awareness only, no details given |

---

## Season overview

### Volume by month and channel

| Month | Total | Email | Web | IG | Messenger | Phone | Handed off |
|---|---|---|---|---|---|---|---|
| Apr (from 4/25) | 11 | 0 | 5 | 6 | 0 | 0 | 3 |
| May | 21 | 0 | 11 | 8 | 2 | 0 | 6 |
| Jun | 124 | 81 | 20 | 21 | 2 | 0 | 44 |
| Jul | 125 | 57 | 21 | 12 | 13 | 22 | 32 |
| Aug | 72 | 0 | 27 | 5 | 1 | 39 | 9 |
| Sep | 19 | 0 | 6 | 5 | 3 | 5 | 3 |
| Oct (1-5) | 13 | 0 | 3 | 0 | 0 | 10 | 0 |
| **Total** | **385** | **138** | **93** | **57** | **21** | **76** | **97** |

- Email ran only Jun 1 to Jul 23, then stopped completely. That lines up with the bot-to-bot loop on Jul 23 (#244). Either someone unplugged the forward or it broke. Worth confirming which.
- Phone started Jul 8. Of the 76 phone sessions, nearly all are hang-ups, "no one is available," or (from Aug 24) "Call setup failed before agents could be rung." Fewer than 5 contain a real conversation.

### AI resolution vs handoff

| Measure | Value |
|---|---|
| OpenCX "automation rate" | 74.7% (flattering, see below) |
| Resolved (explicit) | 52 (31 are empty phone calls) |
| Assumed resolved (customer went quiet) | 183 |
| Handed off to a human | 97 |
| Handoff rate on real chat/email (non-phone) | about 31% (97 of 309) |
| Sentiment | 240 neutral, 93 happy, 6 angry |

The 74.7% counts dead phone calls and silent customers as wins. A fairer read: Cedar fully handled about 2 of every 3 real conversations and handed off 1 in 3.

### Response times

- **AI first reply:** median 17 seconds, 90th percentile 35 seconds. Fast every time.
- **Human after handoff:** only 43 of 97 handoffs got any human action inside OpenCX (assign, message or close). The median wait was 20 hours (75th percentile 40 hours). Only 16 sessions all season had a human type a reply inside OpenCX.
- Caveat: from Jul 16 the "CC internal on AI email replies" workflow copied emails to doorcountykayaking@gmail.com, and staff often answered by phone or Gmail (Lea and Vesper are referenced in guest replies). So a lot of "dropped" tickets were handled and just never closed in OpenCX. That's a process gap more than a service gap, but it makes the backlog useless as a signal.

### CSAT

None. CSAT is disabled on every channel and zero scores exist.

### Why the AI handed off (OpenCX handoff analytics, 97 handoffs)

| Reason | Share |
|---|---|
| Missing tools (couldn't look up/modify a booking, contact update failed) | 53% |
| Missing knowledge | 34% |
| Instructed to hand off (groups, refunds, partnerships) | 31% |
| Customer asked for a human | 7% |

(Handoffs can have more than one reason, so the shares add to more than 100%.)

### Top question categories (all 385)

1. **Booking and availability**, including group size over 12 (#96, #111, #129, #139, #226, #296) and same-day slots
2. **Brochure and giveaway forms** from the FareHarbor site (about 30 sessions, 9 of them handoffs)
3. **Kids, age and weight limits** (kayak and e-bike), about 25
4. **Dogs on tours and rentals**, about 12
5. **Changes to existing bookings** (reschedule, cancel, add or remove people, resend confirmation, waiver link), about 20
6. **Vendors, sponsorship asks, spam** (Meta "Blue V" scams, SEO pitches, donation galas), about 30
7. **Internal mail** that leaked into the bot: staff, payroll, truck mechanic, town inspector, hat vendor

### Where Cedar did well

- Live availability plus direct FareHarbor booking links in under a minute (#39 e-bike 10am slot, #256, #6, #160, #245)
- Weight limits stated correctly and consistently from late July (#275 550 lb tandem / 285 lb single, #280, #342)
- Pregnancy: steered a 31-week guest from Cave Point to Eco Estuary and sent a fresh link (#152)
- Correctly said Logan Creek is Peninsula Kayak Co's exclusive and pivoted to Eco Estuary (#227)
- Captured name and phone before handing off on nearly every web chat

### Where Cedar failed or gave wrong or bad info

| Problem | Examples |
|---|---|
| Demanded a FareHarbor "UUID" that guests never see, looping 3-4 times while they held booking numbers and confirmation codes | #25, #26 (guest canceling 8 people), #107, #194 |
| Led with "We don't process refunds" to an angry, overcharged guest | #194 |
| Phone agent read the caller's own number back as "the office number" and said there's no separate office number | #279 |
| Told a guest the Peninsula State Park e-bike tour is bookable online, then couldn't find it in the item list | #235 (also #24, Death's Door e-bike route "not showing") |
| Garbled e-bike age rule ("riders must be 14-18 with an adult"), inconsistent across chats | #248, #249, #379 |
| Handed off questions it should know: dogs, e-bike weight, own e-bike, fishing, neoprene, changing room, tipping a guide, claustrophobia (answered fine in May #18, handed off in Sep #362), a whitefish chowder restaurant | #20, #61, #62, #100, #123, #177, #54, #272, #287, #313, #362 |
| Replied as Cedar to internal or vendor email: told DCKT's own hat vendor twice she'd reached them "by mistake" (she worked out it was a chatbot); auto-replied to a truck mechanic, a town reinspection, staff resignations, payroll | #166, #81, #117, #124, #34, #53 |
| Bot-to-bot loop with a prospect's AI assistant (staff: "quite humorous seeing these 2 bots correspond") | #244 |
| Generic sales opener ("Cave Point... (A) yourself or (B) a group?") fired at people who came to cancel or chase a refund, once sent twice | #25, #298, #309, #312 |
| Contact-update tool errored (Cloudflare 521/526) on at least 6 sessions | #54, #133, #139, #148, #224, #305 |

### Dropped handoffs and what they likely cost

Of the 86 open:

- 23 were already resolved by staff and reopened by the Aug 10 Nudge workflow
- 9 are brochure requests, 14 are vendor, donation, job or internal items
- About 12 are existing-customer service issues (listed above)
- **About 11 are new-booking leads with no staff reply and no sign they booked anyway**

Conservative estimate for those 11:

| # | Lead | Likely value if booked |
|---|---|---|
| 226 | Elissa Coyer, 11 people, Cave Point, Jul 29 (site wouldn't let her book 12, private grayed out) | 11 x $72.80 = $801 |
| 362 | Miranda + friends, Cave Point (est. 4) | 4 x $72.80 = $291 |
| 62 | Carol Snyder, half-day with dog (est. 2) | 2 x $145 = $290 |
| 354 | Nelson Torres, 4 e-bike rentals + trailer | est. $300 |
| 20 | Christian, e-bike weight question (est. 2 on tour) | 2 x $104.44 = $209 |
| 123 | Eric, own e-bike on tour (est. 2) | $209 |
| 133 | Jill Taylor, 2 SUPs Mon to Thu | est. $200 |
| 299 | Danielle, e-bike rental + dog trailer (est. 2) | est. $150 |
| 256 | Pavel, 2 people Cave Point | 2 x $72.80 = $146 |
| 293 | Leyi Lin, military discount (est. 2) | $146 |
| 272 | Fishing on guided tour (est. 2) | $146 |
| **Total if all booked** | | **about $2,890** |

At a 30% close rate with a same-day answer, that's **about $870 in lost bookings** (call it $900). Small.

The bigger leaks can't be measured from OpenCX:

- **Dead follow-up system all season:** 294 quiet leads triggered the Router and none got a follow-up
- **Broken phone from Aug 24:** callers got dead air during late-season e-bike demand

If even 5% of those 294 leads would have booked a 2-person Cave Point tour, that's 15 x $146 = about $2,200. Treat that as a rough guess, not a measurement.

### Workflows: what worked and what didn't

| Workflow | Status | Verdict |
|---|---|---|
| Lead Follow-Up: Router (2h inactivity) | Active, **294 runs, 0 completed** | Broken all season. Step 1 fails with "ticketNumber: Invalid input" (uses `{{trigger.ticket.number}}`, the field is `ticketNumber`). Nothing downstream ever fired |
| Lead Follow-Up: Hot / Warm phase 1 | **Inactive** | Never ran |
| Lead Follow-Up: Cool / Warm P2 / Cool P2 | Active | Never triggered (depends on Router tags) |
| Notify Slack on Handoff (from Jun 24) | Active, about 50 posts to #handoffs | Worked mechanically. No evidence anyone acted on the thumbs-up loop |
| CC internal on AI email replies (from Jul 16) | Active, 52 runs | Worked. Also why staff answered in Gmail and never closed tickets |
| Nudge unbooked inquiries (created Aug 10) | Active, 131 runs | Harmful. Backfilled old sessions, reopened 23 resolved handoffs (inflating the TideBot count), and sent 317 identical no-context nudges with em dashes to 67 people. **0 replies** |

### Email DNS / native sending

- `doorcountykayaktours.com` now shows **verified** in OpenCX (DKIM `resend._domainkey`, SPF MX + TXT on `send` all verified). The memory note saying it failed is outdated.
- Nothing uses native email yet. The follow-up workflows still carry the SendGrid HTTP step (with the key inside the workflow config), and they never ran anyway.
- No OpenCX SMS number and no AI phone agent exist. The "SMS" nudges were only ever replies on the original channel.

### TideBot rollup note

The "money" flag is a loose regex (`people|group|rate|availab|cancel...`) on the handoff summary. It flags 46 of 86, including a hiring post ("$18" role) and vendor pitches. My read is 48 money-intent tickets (bookings, changes, charges), of which 9 still need David. Also, the count includes workflow-reopened tickets. It should exclude sessions whose last event is `system_reopened_session` with no new customer message.

---

## Fixes for 2027 (ranked)

1. **Fix or unplug the phone path now.** Find which published number forwards into OpenCX. Point it back to a real phone or voicemail until a tested phone agent exists. Never let the AI say there's no office number.
2. **One handoff owner and a 2-hour in-season SLA.** Handoffs ping the manager's phone (Slack DM, not a channel nobody watches). Whoever answers by phone or Gmail closes the ticket in OpenCX that day. TideBot counts only genuine opens.
3. **Rebuild follow-ups, small and tested.** Delete Nudge. Fix the Router variable, turn on Hot only, and send nudge 2+ via native email (domain is verified). Write messages from conversation context, no em dashes. Run `test_workflow` before May 1 and check a week of runs.
4. **Give Cedar a real booking lookup** by booking number or confirmation code plus name. Stop asking for UUIDs. Allow it to add a note, resend a confirmation and resend the waiver link. That alone covers about 20% of handoffs. Also fix the contact-update tool errors.
5. **Close the knowledge gaps** that caused easy handoffs: dog policy (tours and rentals), e-bike age/weight/trailer and own-bike rules, fishing, changing rooms/showers, neoprene, claustrophobia, wheelchair access, military discount, week-long rentals, private tour headcount, weather-cancel refund wording. Load these into the SOP doc and training.
6. **Split the email inbox.** Only guest-facing FareHarbor forms go to Cedar. Staff, payroll, vendor and municipal mail goes to humans. Add a no-reply rule for other bots and auto-responders. Brochure requests should auto-send the PDF and tag the giveaway, with no handoff.
7. **Refund and complaint protocol.** Never lead with "we don't process refunds." Angry, refund, injury or charge disputes get immediate escalation plus a stated callback time. Suppress the sales opener when the first message is a follow-up or complaint.
8. **Turn on CSAT** for web and email after close, so 2027 has a real satisfaction number.

## Off-season plan (e-bike only)

- **This week:** fix phone routing (item 1). Pause the Nudge workflow. Leave Router follow-ups off until rebuilt.
- **Update Cedar's instructions:** kayak tours are done for 2026 and 2027 booking opens [date]. E-bike rentals continue (hours, pickup spot, trailer/tag-along rules, ages). For anything it can't answer, give the business email and phone instead of promising a "tour expert" callback that won't come.
- **Route handoffs to David** (or whoever covers e-bikes) via Slack DM until spring staff are back.
- **Clean the backlog** once David OKs it: bulk-close the 71 marked close below, answer the 3 replies, and work the 12 needs-David items.
- **Late April:** run 20 test chats covering the gaps above. Confirm the Router runs green, phone rings a human, and email forms go to the right place.

---

## The 86 open tickets

Key: $ = real money intent (booking, payment, refund, charge). Status "Reopened 8/10" = staff had already resolved it, then the Nudge workflow reopened it. Rec: **C** close, **R** reply, **D** needs David.

| # | Date | Ch | Customer ask | $ | What the bot did | Why handed off | Actionable now? | Rec |
|---|---|---|---|---|---|---|---|---|
| 4 | 04-27 | IG | Colburn Creative pitching social content, wants a Meet | N | Asked for email, handed off | Partnership | No. Davey replied, offered trade | C |
| 10 | 04-30 | Web | Angry, can't see site, wants to close chat | N | Offered help, asked name/phone | User frustration | No | C |
| 20 | 05-17 | Web | E-bike weight limit (Christian, 608-340-2218) | Y | Handed off immediately | Missing knowledge | Stale lead | C |
| 24 | 05-19 | Web | Book Hwy 42 Death's Door e-bike ride Jul 28 (Kelly Nalley) | Y | Couldn't find item, took phone | Missing tool/item | No. Resolved 5/20, reopened 8/10 | C |
| 25 | 05-19 | Web | Cancel 4 of 8 (Dhaval Mehta, #339616866) | Y | Asked for UUID, then phone | Can't modify booking | No. Resolved 5/23, reopened 8/10 | C |
| 26 | 05-19 | Web | Cancel whole booking (same guest) | Y | Looped asking for UUID 3x | Can't modify booking | No. Resolved 5/23, reopened 8/10 | C |
| 28 | 05-25 | Web | Rent kayaks for a week | Y | Handed off | Missing knowledge | No. Staff gave email, reopened 8/10 | C |
| 32 | 05-31 | IG | Courtney Klang, social agency pitch | N | Pitched affiliate program, then took contact | Partnership | No | C |
| 33 | 06-01 | Email | Insurance cert receipt (Leavitt) | N | Handed off | Internal/vendor | No. Resolved 6/2, reopened 8/10 | C |
| 36 | 06-01 | Email | Brochure request (Katie Pollock) | N | Handed off | No brochure tool | No | C |
| 37 | 06-01 | Email | Brochure + giveaway (Katie Pollock, dup) | N | Handed off | No brochure tool | No | C |
| 39 | 06-03 | Web | E-bike tour tomorrow, then wheelchair access | Y | Gave slot + link, handed off on wheelchair | Missing knowledge | No. Guest said no need; resolved, reopened 8/10 | C |
| 42 | 06-03 | IG | David's own chats (B-roll list, Higgsfield, weather person) | N | Wrote B-roll list | Internal | No | C |
| 53 | 06-06 | Email | "Madeline Ponder" wants to change payroll bank account | N | Handed off | Internal/HR | **Yes. Likely phishing**, verify with Madeline | D |
| 54 | 06-06 | Web | Place to change at Cave Point (Susan Dachs) | N | Took phone, contact tool error 521 | Missing knowledge | No | C |
| 55 | 06-06 | Email | Brochure + giveaway (Deb Koch) | N | Handed off | No brochure tool | No | C |
| 61 | 06-07 | Web | Dog on quad bike, location | N | Handed off | Missing knowledge | No. Staff answered | C |
| 62 | 06-07 | Email | Dog on half-day kayak (Carol Snyder) | Y | Handed off | Missing knowledge | Stale lead | C |
| 65 | 06-08 | IG | WassupMinnesota wants raw clips for reels | N | Took contact | Partnership | No | C |
| 88 | 06-13 | Email | Husband cramping/wheezing, came back early, partial refund (Dawn Hernke) | Y | Empathy, handed off | Refund | **Yes. Verify refund issued** (resolved 6/14, reopened 8/10) | D |
| 91 | 06-14 | Email | 2 brochure requests (Sue Homes, Michelle Wauer) | N | Handed off | No brochure tool | No | C |
| 94 | 06-15 | Email | Weekly regular-bike rental (Heather Weiler) | Y | Handed off | Missing knowledge | No. Staff answered, reopened 8/10 | C |
| 95 | 06-15 | Email | Change 4 adults to 2 (Vrinda Johnson) | Y | Handed off | Can't modify booking | No. Done 6/17, reopened 8/10 | C |
| 96 | 06-16 | Email | 30-person nonprofit group, Cave Point (Adam Krueger) | Y | Handed off | Group over 12 | No. Group booked | C |
| 97 | 06-16 | IG | Job applicant, part-time front desk/photo | N | Gave pay/hours, handed off | Hiring | No | C |
| 100 | 06-16 | Email | Dog in tandem + private half-day headcount | Y | Handed off | Missing knowledge | No. Resolved 6/17, reopened 8/10 | C |
| 101 | 06-16 | Email | BBBS Dane County gala donation | N | None | Donation | No. Event past | C |
| 102 | 06-16 | Email | Same two inquiries as #100 | Y | Checked FH price, handed off | Missing knowledge | No. Resolved, reopened 8/10 | C |
| 103 | 06-16 | Email | WILC gala donation (Nov 7) | N | Handed off | Donation | Optional. David's call on donating | C |
| 107 | 06-17 | Web | Paid only $10 for e-bike tour, is that right? | Y | Asked for UUID, took phone | Can't look up booking | No. Resolved, reopened 8/10 | C |
| 111 | 06-18 | Email | Group Tue Jul 14 10-11am (Krueger) | Y | Checked FH, handed off | Group over 12 | No. Booked | C |
| 112 | 06-18 | Email | Add note: 6'9" guest | N | Handed off | Can't add booking note | No. Resolved, reopened 8/10 | C |
| 113 | 06-18 | Email | Workforce agency asking re part-time hiring | N | Handed off | Hiring | No. Resolved, reopened 8/10 | C |
| 118 | 06-22 | Email | Thorp House Inn wants free blog post + collab | N | Handed off | Partnership | No. Resolved, reopened 8/10 (lodging outreach) | C |
| 119 | 06-22 | Email | Family Services gala donation | N | Handed off | Donation | No. Resolved, reopened 8/10 | C |
| 123 | 06-23 | Web | Use own e-bike on tour (Eric, 920-750-0779) | Y | Took phone, handed off | Missing knowledge | Stale lead | C |
| 129 | 06-24 | Email | Group of 15, Jul 14 9am (Jerry Petersen) | Y | Handed off | Group over 12 | No. He booked 12+3 himself | C |
| 130 | 06-24 | Email | Waivers for 20 minors, deposit, nonprofit discount, tax-exempt bill | Y | Handed off | Instructions | **Check tax-exempt adjustment owed** | D |
| 132 | 06-24 | Email | Brochure (Jill Bradley Taylor) | N | Handed off | No brochure tool | No | C |
| 133 | 06-24 | Web | Rent 2 SUPs Mon-Thu, delivery? (Jill Taylor) | Y | Answered partly, contact tool error | Missing knowledge | Stale lead | C |
| 136 | 06-24 | Email | Animal rescue sponsorship | N | Took phone | Donation | No. Event past | C |
| 139 | 06-25 | Web | Private tour, 10 people, shipwreck + caves (Olivia Cathey) | Y | Took phone | Private/group pricing | No. Resolved same day, reopened 8/10 | C |
| 141 | 06-26 | Email | Brochure (Mandi Moore) | N | Handed off | No brochure tool | No | C |
| 148 | 06-29 | Email | Jake Buckner wants Homebase setup | N | Handed off, contact tool error | Internal/HR | No | C |
| 149 | 06-29 | Email | Brochure (Courtney Pleviak) | N | Handed off | No brochure tool | No | C |
| 152 | 06-30 | Email | 31 wks pregnant, switch to Eco Estuary (Kathleen Gardin) | Y | Recommended Estuary, sent links | Can't modify booking | No. Resolved 7/2, reopened 8/10 | C |
| 158 | 07-01 | Email | Reschedule e-bike tour for storms (Nathan Volkey) | Y | Showed open slots | Can't modify booking | No. Staff answered | C |
| 165 | 07-03 | Email | Blacksmith Inn: Where to Stay + guest post | N | Handed off | Partnership | No. Resolved, reopened 8/10 | C |
| 166 | 07-03 | Email | Hat Head vendor: names on hats, $6/hat | N | Told vendor it was a mistake (twice) | Internal/vendor | No. Lea handled. Check the hat invoice | C |
| 174 | 07-07 | Email | Brochure (Jakub Klocek) | N | Handed off | No brochure tool | No | C |
| 176 | 07-07 | IG | TripOutside comp creator tour; Aug 26 asks for fall clips | N | Took contact | Partnership | Optional marketing reply | R |
| 177 | 07-07 | Web | Neoprene rental? | Y | Handed off | Missing knowledge | No. Staff answered, reopened 8/10 | C |
| 185 | 07-09 | Email | Kids/tandem/$69 + Viator weather refund notice (Jim Stein) | Y | Handed off | Refund/OTA | No. Resolved 7/10, reopened 8/10 | C |
| 193 | 07-10 | Email | Gift codes won't apply, Jul 18 (Carrie Haak) | Y | Handed off | Can't apply codes | No. Staff said to call | C |
| 194 | 07-10 | Web | Charged $95 not $75, no shipwrecks, angry (Austyn Patefield) | Y | "We don't process refunds," UUID loop | Refund/complaint | **Verify credit/refund** (resolved 7/12, reopened 8/10) | D |
| 207 | 07-13 | Email | 2 brochure requests (Leyi Lin, Darin Williams) | N | Handed off | No brochure tool | No | C |
| 209 | 07-13 | Email | SUP pickup missed, board left at Deck House (Tom Hartigan) | N | Handed off | Ops | **Confirm gear recovered** | D |
| 215 | 07-14 | Email | Moms/toddlers meet at picnic spot (Adam Christenson) | Y | Handed off | Instructions | No. Handled via #224 | C |
| 217 | 07-15 | Email | Same + kayaks provided? (Sarah Whiting) | N | Handed off | Missing knowledge | No | C |
| 220 | 07-15 | Email | No paddle in bag, don't charge me (Kathy Casper) | Y | Apologized, handed off | Charge concern | **Make sure no paddle charge** | D |
| 221 | 07-15 | Email | 3 can't paddle, air quality, late notice (Pam Delfosse) | Y | Handed off | Cancel/credit | **Decide credit/refund** | D |
| 224 | 07-16 | Email | Switch to Cave Point half-day Aug 11 (Christenson) | Y | Gave slot + link | Can't modify booking | No. Guest confirmed | C |
| 226 | 07-16 | Email | Group 10-12, Cave Point Jul 29 (Elissa Coyer) | Y | Handed off | Group over 12 | No. Lost lead (~$800) | C |
| 227 | 07-16 | IG | Peninsula Pulse intern, Logan Creek | N | Answered correctly | Press wording | No | C |
| 235 | 07-19 | Msgr | Book PSP e-bike tour Aug 15 online | Y | Said yes, then couldn't find item | Missing item | No | C |
| 242 | 07-22 | Email | Add 1 person Aug 29 (Aubrey Silva) | Y | Handed off | Can't modify booking | No. Date past | C |
| 243 | 07-22 | Email | Company retreat e-bike Sep 16 (TJ) | Y | Handed off | Group/policy questions | No. Date past | C |
| 244 | 07-22 | Email | Same (bot-to-bot loop) | Y | Handed off | Group | No | C |
| 255 | 07-26 | IG | "Reporting you to the DNR," names Dave Rack | N | Handed off | Complaint/threat | Awareness only | D |
| 256 | 07-27 | Web | Bike + kayak today, 2 people (Pavel) | Y | Itinerary + link for tomorrow | Wanted a person | No. Lost lead (~$146) | C |
| 272 | 07-28 | Web | Fishing on guided tour? | Y | Asked for contact | Missing knowledge | No | C |
| 276 | 07-30 | Msgr | Left bag with ID/wallet in office (Adia Hopes) | N | Took phone | Ops | No. Next-day pickup | C |
| 277 | 07-30 | IG | SmartRez booking software pitch | N | Asked for contact | Vendor | No | C |
| 281 | 07-31 | Web | Resend confirmation (Danica Johnson) | Y | Took phone | Can't resend | No | C |
| 287 | 08-03 | Web | Wants to tip guide (Freya Irani) | N | Took phone | Missing knowledge | No | C |
| 289 | 08-05 | Web | Can't find waiver link (Mary Jane Langford) | Y | Took booking #/phone | Can't resend | No | C |
| 293 | 08-07 | Web | Military discount? (Leyi Lin) | Y | Took contact | Missing knowledge | No | C |
| 298 | 08-11 | Web | July 5 weather refund not received (Bobbi Tobalsky) | Y | Sales opener, then took phone | Refund | **Yes. URGENT** | D |
| 299 | 08-11 | Web | E-bike rental + 35 lb dog in trailer (Danielle, 630-337-6352) | Y | Took contact | Missing knowledge | Yes, e-bike lead | R |
| 305 | 08-14 | Web | Can't find confirmation (Anna Adl) | Y | Took email/phone, tool error | Can't resend | No. Tour past | C |
| 309 | 08-15 | Web | Same refund, 2nd ask (Bobbi) | Y | Sales opener, then took phone | Refund | **Yes. URGENT** (same as 298) | D |
| 312 | 08-18 | Web | Same, 3rd ask: "my daily inquiry" (Bobbi) | Y | Misread as gift cert | Refund | **Yes. URGENT** (same as 298) | D |
| 313 | 08-21 | Web | Which restaurant has whitefish chowder | N | Took phone | Missing knowledge | No | C |
| 354 | 09-02 | Web | E-bike trailer: does a 3-yr-old need a ticket? (Nelson Torres, 941-483-6107) | Y | Took phone | Missing knowledge | Yes, e-bike lead | R |
| 362 | 09-09 | Web | Claustrophobic, stay near cave entrance? (Miranda) | Y | Took phone | Missing knowledge | No. Season over | C |
| 370 | 09-26 | Web | Cancel tomorrow's tour (Webster, 715-499-0832) | Y | Took phone | Can't cancel | **Check charge/refund** | D |

Counts: 71 C, 3 R (#176, #299, #354), 12 D (#53, #88, #130, #194, #209, #220, #221, #255, #298, #309, #312, #370). Bobbi's three tickets are one action. Real money intent: 48 of 86 by my read. The TideBot regex flagged 46, but it misses some and hits vendor/hiring noise.
