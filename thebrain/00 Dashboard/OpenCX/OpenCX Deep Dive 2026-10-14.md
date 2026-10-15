# OpenCX Deep Dive: every conversation, all 6 workspaces

**Pulled live 2026-10-14.** 2,842 conversations, Apr 20 to Oct 15, 2026. Every transcript was read (8 parallel reviewers), and the key claims were spot-checked against the raw data.

## Bottom line

**The bot half works. The human half doesn't exist.**

- The AI answers in about 15 seconds, gets the basics right most of the time, and books people when it sends a pre-filled FareHarbor link.
- It loses money in 4 ways:
  1. It quotes the wrong prices.
  2. It gets the time and date wrong.
  3. It makes promises it can't keep (texting, emailing, holds, resends).
  4. Every money, same-day or complaint case goes to a "tour expert" who almost never answers inside OpenCX.
- 356 handoffs total. 346 are still open. A human reply is recorded on 44.
- Nobody is watching. The handoff watcher (`com.djl.opencx-watch`, davids-mbp-2) has been off since Sept 8, when the bot posts were paused.

Caveat on every "no reply" below: staff may have answered by phone or in the Meta inbox, which OpenCX can't see. Several transcripts show that didn't happen, e.g. NKST #43 ("is there no one available?"), NPB #512, #516, #688 and #376 ("Nolan... does not follow up").

## Scorecard

| Business | Convos | Grade | Handoffs (open / human reply) | Biggest problem |
|---|---|---|---|---|
| NOLA Party Barge | 1,759 | C | 176 (168 / 24) | $63 vs $59 price, timezone bug, booking tool failing since Sep 25 |
| NKST | 468 | C+ | 50 (49 / 4) | ~290 lead-form/giveaway chats die at "What date?" |
| DCKT | 389 | C+ | 97 (86 / 14) | Bot replies to vendor email as David; phone line dead |
| Houston Pedal Barge | 72 | C+ | 21 (21 / 1) | $878.99 refund + BBB threat with no human reply; stale prices |
| Lone Star / Austin Kayak | 133 | B- | 20 (19 / 1) | Guests on-site with no confirmation, no one answered |
| Buffalo Bayou Kayak | 21 | C | 3 (3 / 0) | Stale prices; IG and Messenger not connected |

## Act now (open, last 2 weeks, no human reply recorded)

| Brand | Ticket | What | Why now |
|---|---|---|---|
| NKST | #468 | Amy Baxter, booking #385546218: move Extended Manchac from **Oct 16 to Oct 15**. Phone 267-912-1167 | Trip is tomorrow |
| LSKT | #133 (and #132) | Bat-tour guest complaint about red lights on the bridge ruining photos; #132 was never handed off | Tonight (10/14) |
| NKST | #466 | 290 lb guest asking about solo kayak options | Lead |
| NPB | #1702 | 12 people for Oct 10; booking tool failed | Lost unless someone calls |
| NPB | #1686 | 10 people for Oct 25; can extras pay on arrival? | Lead |
| NPB | #1753 | Creator (40K followers) pitching Mardi Gras Day | Your call |
| NPB | #1737, #1698, #1744 | January ops? Night tours? Kayak tours? | Knowledge gaps |

## Top 10 fixes, ranked by money and risk

1. **Wall off the email inbox.** The bot answers vendor, insurance and government email as if it were David.
   - DCKT #117: it told JB Truck Service to go ahead with the repair and promised a **$535.36 deposit** "today", signed "Cedar".
   - NPB #1040: it answered a Gallagher broker thread about the vessel insurance policy.
   - It also told the SES bounce sender how to remove suppressions (NPB #398), rejected a USA Today ad buy (#437) and declined insurance (#473).
   - Fix: skip non-guest senders, never approve, pay or decline anything, and route that mail to the owner.
2. **Make handoffs real.** Alert a named person on Slack for anything with money, same-day, on-site, angry, refund or "no confirmation", and set a reply-time target.
   - HPB and BBK have no handoff alert at all. LSKT has one, but it's switched off.
3. **One price source.**
   - NPB: the prompt hard-codes **$63** public and $900/$1,100/$1,250 private. Live checkout shows **$59** and $800/$900/$1,200. The bot uses both, sometimes in the same chat (#1492: "That said 59... You had me excited").
   - HPB: the bot quotes $55/$800 while live is $59.54/$866 (#71: "website says 800").
   - BBK quoted a July 4th $75 tour on Sept 23.
4. **Fix the clock.** The bot treats UTC as local time.
   - NPB #1580: at 6 PM it told a guest "it's already 11:00 PM".
   - At 1 PM it said the 6 PM trip "already passed" (#1380, #1438, #1495). About 10 same-day groups were turned away this way.
   - LSKT checked Oct 1 for a Sept 30 request (#128). Weekday errors happen everywhere.
5. **Link every time.** Once date plus headcount are known, send the pre-filled link in the same reply.
   - Only ~38 of 314 early NPB chats got one. HPB got ~5 of 72, LSKT ~7 of 133, BBK 1 of 21.
   - **NPB sends raw `<a href>` HTML in Messenger and IG, which customers can't click:** 143 sessions, **72 in September alone**, so it's still happening.
6. **Kill the false promises.** Remove:
   - "I just texted you the booking link" (NPB ~66 chats, no SMS exists)
   - "I can email you"
   - "I'll hold that slot"
   - "I've triggered a confirmation resend"
   - "we'll reach out before 8 pm today"
   - "book right here in chat"
7. **Fix the FareHarbor booking tool (NPB, since ~Sep 25).** It says "slot no longer available" while seats exist (#1632, #1646, #1660, #1679, #1702, #1718), and ready buyers become silent handoffs. Fallback: always send the plain date checkout link.
8. **Settle the policy conflicts.** The bot contradicts itself on:
   - **DCKT:** minimum age (4 vs 5 vs "OK if calm"), dogs (case-by-case vs people-only), and refunds ("we don't process refunds" vs the owner's 50% partials)
   - **NPB:** refund wording ("within 7 days of your tour" vs "up to 7 days before", which mean opposite things), deposit ("can vary" vs $350), and smoking
   - **NKST:** group cap (8 vs 12), and it said a self-guided rental is fine for 5-year-olds, "no age restriction" (#147), which is a liability
9. **Booking lookup by confirmation number or email,** not a UUID. Guests have their 9-digit FareHarbor number and the bot demands a UUID (NPB #712, #815, #1156). The "Update Contact" action throws 404s (NKST, HPB, LSKT).
10. **Fix or kill the drips and nudges.**
    - NPB's 5-step cold sequence went to 717 chats, and 18 replied (3%).
    - Steps 2 to 6 fired as **one batch on Aug 11** to leads from May to July, after their trips had passed. That included people who said "Stop" (#895) or "I have enough info" (#333). DCKT had the same batch (67 chats).
    - NPB's 3-minute "Are you still there?" nudge fired 1,566 times. 89 times, the customer replied within 2 minutes, so they were most likely still typing.

## Business by business

### NOLA Party Barge (1,759, grade C)
- **Works:** date plus size gets live seats, a pre-filled link and per-person math. Confirmed bookings: #1486, #1491, #1495, #1530, #1552. The 21+ rule is applied correctly. Honest sold-out answers. Spanish works. Asks happy guests for reviews.
- **Wrong:**
  - The $63 vs $59 price split, plus private-boat prices that shift by the day
  - Wrong weekdays, and a Sept **2027** link for a Sept 2026 ask (#1494)
  - Gave the phone as 504-254-1056 six times (correct is 264-1056)
  - Confirmed another party's boat and time to a stranger (#558)
  - Quoted a Bike Bar pub crawl for 60+ while it's paused (#472)
  - Said "kids included" on public tickets (#780)
- **Lost sales:**
  - ~130 "how much" chats end at the price, with no link
  - Pushes the 10 AM slot even when guests say it's too early
  - The $350 Pontoon (up to 6) only shows up from Aug 11; before that, small groups got a $900 quote
  - Never pitches private at 20+ guests, where private ($1,250) is about what public costs ($1,260)
- **Urgent history with no recorded reply:**
  - #1533: paid for 3, confirmation shows 1, tour next day
  - #1269: paid for 4 PM today, no confirmation
  - #487: family death, deposit refund for 22 guests
  - #1113/#1079: angry refund wait
  - #369 and #363: weather refunds
- **Noise:** ~70 email tickets are SES bounces, DMARC reports, Indeed and ZIP-only mail.

### NKST (468, grade C+)
- **Works:** accurate, fast, pre-filled slot links (#13, #106, #284). Directions and the plus code are consistent. The 48h refund and weather answers are consistent. #106/#108 reached Dylan in about 5 minutes.
- **Biggest leak:** ~290 Messenger lead-form and giveaway entries get one "What date?" and die. "Did I win?" gets no answer. Fix: open with price, the nearest open slot plus link, and a giveaway FAQ.
- **Wrong:**
  - Cross-brand bleed: tells rental guests to "search Nola Party Barge" for directions, and pitched the BYOB cruise to a family with kids (#136)
  - Pointed a lead to free parks instead (#136)
  - Gives the MILITARY code to anyone, and it fails at Apple Pay checkout (#215, #292)
  - Old pickup address, 405 Frenchmen St (#411)
  - Narrates "I saved your info" ~90 times
- **Urgent history:**
  - #43: booked for 2 PM, two missed calls from you, asked for a human, gave up
  - #72: booked the wrong product, no car
  - Weight questions: 540 lb couple (#457), 290 lb solo (#466)
  - #367: 5-year-old, trip two days out
  - #290: autistic son

### DCKT (389, grade C+)
- **Works:** best trip-planner of the six on web, IG and email. Handles Jacksonport vs Ellison Bay vs Baileys Harbor check-in well. Live 8 AM picks with links. Good safety answers (pregnancy, weight, PFDs). Booking lookup by email works (#126).
- **Phone agent is effectively dead:**
  - 79 calls: 72 with no caller speech and 0 bookings
  - 27 "Call setup failed" since Aug 24
  - Callers who did speak asked for the office, and the bot can't transfer
- **Bot acting as David:** the truck repair deposit (#117), confirmed a vendor shipping address (#73), and answered a fire reinspection (#124) and the town clerk (#175).
- **Other:** rental delivery to Cave Point ($25) promised, then retracted. The brochure link is a 2018 JPG.
- **Urgent history:**
  - #298/#309/#312: July 5 weather refund unpaid after 6 weeks
  - #88: guest wheezing on the water, partial refund mentioned
  - #194: charged $95 vs $75 advertised
  - #255: DNR report threat
  - #276: wallet and hotel keys left at the office
- **Season is over,** so fix this before spring, not now.

### Houston Pedal Barge (72, grade C+)
- **Works:** BYOB, bathroom, capacity and 8+ answers are consistent. #69 honestly steered a couple to a $55 seat instead of an $866 charter.
- **Wrong:**
  - Stale $55/$800 prices
  - Buffalo Bayou and Clear Lake share one FareHarbor item (414533), so #4 may have booked the wrong waterway. Verify.
  - **The prompt itself scripts a "pedaling conversation"**, and the bot brings up pedaling in ~40 chats unprompted. That breaks your no-pedal-marketing rule.
  - #60: the voice bot took a medical patient-portal call and a date of birth, which looks like a misrouted number
- **Urgent:**
  - #46 to #52: Alexandria Hall, June 6 weather cancel, **$878.99 refund** publicly promised, BBB threat, 7 identical "escalating" replies, no human
  - #43 to #45: 4 tickets for 10 PM that night, no address
  - #19: 52 guests tomorrow got "check TikTok"
- **Channels:** 0 Messenger, and volume fell after June. Messenger is probably not connected.

### Lone Star / Austin Kayak (133, grade B-)
- **Works:** the most consistent facts ($50/$55 tours, $20/$25 per hour rentals, 450 lb limit). Jobs get the application link instantly. Warns guests about phishing.
- **Wrong:**
  - UTC dates and weekday errors
  - "Open Saturday" despite a lake closure (#101)
  - Alcohol: handed off in one chat, "prohibited by ordinance" in another (#69, unverified legal claim)
  - Dodged "are you AI?" (#84)
  - Unverified "5,000+ tours, zero incidents" claim
  - Deflected a service-dog question (ADA)
- **Urgent:**
  - #118: guest at the meeting spot, "abandoned"
  - #125: 3 SUPs booked, waiting on site, no confirmation
  - #133: last night's complaint
- **Channel oddity:** Messenger had 0 chats, then ~45 in one week of June mentioning a "New Orleans party barge" and a "booze cruise" ad. A mismatched ad or page.

### Buffalo Bayou Kayak (21, grade C)
- Too little volume to judge. Only 1 link in 21 chats.
- Stale July 4th tour quoted in September (#19).
- Ali (#11, #12) waited 1.5 hours for a promised call.
- Both phone calls captured nothing.
- **0 Instagram or Messenger chats, so those channels almost certainly aren't connected.**

## Setup check (live 2026-10-14)

| | NPB | NKST | DCKT | HPB | LSKT | BBK |
|---|---|---|---|---|---|---|
| Actions (tools) | Update Contact | same | same | same | same | same |
| Help-center articles | 0 | 0 | 0 | 0 | 0 | 0 |
| SLA policies | 0 | 0 | 0 | 0 | 0 | 0 |
| Handoff alert to Slack | callback-only | on | on | **none** | **off** | **none** |
| Prompt size (words) | 3.6k (+2/3 HTML padding) | 11.8k | 12.2k | 6.3k (+2/3 padding) | 10.7k | 13.4k |
| Email domain | verified | verified | verified | verified | verified | verified |

Fixed since May: all 3 failed email domains are now verified.

Not fixed since May: 1 action per workspace, no knowledge base and no SLAs. The bot runs entirely on giant prompts, which is why the same facts come out differently in different chats.

## Decisions only you can make

1. **Real prices:** NPB public ($59 or $63?) and each private boat; HPB public and charter.
2. **DCKT rules:** minimum age, dogs, refund/weather policy.
3. **NKST:** public group cap (8 or 12) and the private-group price ($400 up to 8?).
4. **Who owns handoffs per brand,** and how fast they reply.
5. **DCKT phone agent:** fix it, or turn it off and forward to (920) 868-1400.

## Data and method

- Raw pulls, transcripts and per-section reviewer reports are in the session scratchpad and are not kept long-term. Re-pull with the REST API (keys at user scope, `OPENCX_API_KEY_<BRAND>` in `~/.claude/settings.json`).
- "Human reply" means a `human_agent` message inside OpenCX.
- Ticket numbers are per workspace.
