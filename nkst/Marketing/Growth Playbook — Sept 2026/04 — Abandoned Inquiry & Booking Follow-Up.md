# 04 — Abandoned Inquiry & Booking Follow-Up

*Growth Playbook, September 2026. Facts come from [[00 — Fact Sheet & Open Questions]]. If a number changes there, change it here too.*

**Status: DRAFT.** Nothing here is live. GHL, FareHarbor, OpenCX (Magnolia) and SMS changes all need David's sign-off before anything is built. Items marked **PROPOSED** are ideas, not decisions.

**Builds on:** [[NKST — Sales Process & SMS Playbook]] (Sections 2, 4, 5), [[NKST — Chatbot & SMS Script v2]], [[Marketing/NKST — Lead Nurture Strategy]], [[NKST — Customer Journey Map]] (Stages 2–3), [[A2P 10DLC Verification — NOLA Kayak Swamp Tours]], [[Operations/Private Tour Rate Card]].
**Supersedes:** the nurture copy in Sales Playbook Section 2 and the matching messages in Chatbot & SMS Script v2, for the five segments below. The sequence structure (immediate, 2–4 hrs, day 2, day 4, day 7 break-up) is kept. The copy is replaced because it breaks current facts and voice rules. See [Section 11](#11-contradictions-found-and-what-this-file-supersedes).

---

## 0. Shared build rules (these apply to files 04, 05 and 10)

### 0.1 Sender identity
- **Email from-name:** `Ray at New Orleans Kayak Swamp Tours`. Sign-off: `Ray` on the first line, `New Orleans Kayak Swamp Tours · (504) 571-9975` on the second.
- **SMS sign-off:** `- Ray` or `- Ray, New Orleans Kayak Swamp Tours`.
- Never use David's name in anything a guest or partner sees. Internal routing notes, like "over 20 guests goes to David," stay internal.
- Replies go to one shared inbox that Ray (the ops contractor on duty) watches. Every reply pauses the automation (see 0.4).

### 0.2 SMS rules (contractor: build these as global settings, not per message)
| Rule | Spec |
|---|---|
| Brand name | The **first SMS of every sequence** includes "New Orleans Kayak Swamp Tours". Use the full name. The A2P samples say "NOLA Kayak Swamp Tours", which may not match the registered DBA (see §11). |
| Opt-out | The first SMS of every sequence ends with `Reply STOP to opt out.` Later SMS in the same sequence can leave it off. STOP and HELP are handled at platform level. |
| Quiet hours | **Nothing sends 9:00 PM–8:00 AM Central.** A message that comes due in that window waits until 8:30 AM. Set this in GHL at the workflow level ("Send window" on every SMS action), not just the account default. |
| Length | Aim for under 160 characters. The character counts shown after each SMS assume a branded link of about 24 characters and a first name of 8. |
| Encoding | Plain GSM-7 characters only: straight apostrophes, hyphens and no emoji. One emoji or curly quote switches the message to UCS-2, which drops the segment limit from 160 to 70 characters and triples the cost. (Emoji in the old playbook copy are dropped for this reason.) |
| Links | **No public link shorteners** (bit.ly, tinyurl and so on). Carriers filter them. Use a branded link domain the business owns. The GHL "Trigger Links" feature, with a custom tracking domain, works for this. The placeholders `{link:...}` below mean branded links. **Open item:** pick the domain. A short owned domain is best. `go.neworleanskayakswamptours.com` works but is long. |
| Consent | SMS goes only to contacts with a consent source on file: FareHarbor booking, waiver, or an inbound text or call they started (the A2P opt-in workflow). **An unfinished checkout is not consent** (see Segment A). |
| Frequency | No more than **1 marketing SMS per contact per day**, and no more than **4 per rolling 7 days** across all workflows. Transactional texts about a booked tour don't count. |

### 0.3 Email rules
- Send marketing email from a marketing subdomain and transactional email from a separate one, as the Lead Nurture Strategy deliverability section says. (Its example domain `nolakakyaktours.com` has a typo. Use the real domain.)
- Every email carries an unsubscribe link and a physical postal address, which CAN-SPAM requires. **Open item:** choose which address. The A2P brand address is in Milwaukee, and the guest-facing address is 740 N Rampart St, which is a pickup point. David to confirm.
- Write the preview text on purpose for every email. It's given below for each one.
- Plain-text style: one column, no hero banner, one link per idea, and it should read like Ray wrote it. That matches the "friendly local expert" tone in the Lead Nurture doc.

### 0.4 Global exit and suppression logic (build once, reference in every workflow)
| Event | Action |
|---|---|
| FareHarbor `booking.created` for this contact (matched on email or phone) | Tag `booked`. **Remove from every workflow in this file** (use a GHL goal event). Start the post-booking flow if one exists. |
| Contact replies (SMS or email) | Tag `replied`. Pause the workflow. Create a task for Ray: "Reply within 5 min in business hours." Resume only if Ray sets `resume-nurture`. |
| STOP / unsubscribe | GHL DND on that channel. The other channel keeps going only if its own consent exists. |
| Contact tagged `do-not-market`, `refund-dispute` or `staff`/`partner` | Suppress. |
| Contact is already in another workflow in this file | Newest trigger wins, and the older workflow exits. Never run two of these at once. |
| Requested tour date passes | Exit. Hand the contact to the "just exploring" long-term list (Segment E, step E3). |

### 0.5 Merge fields and custom values (set once in GHL)
| Placeholder | Source | Fallback text |
|---|---|---|
| `{{first_name}}` | Contact | "there" |
| `{{tour_name}}` | FareHarbor item, or chatbot intent | "the swamp tour" |
| `{{tour_date}}` | FH availability, or the chatbot date entity | leave the sentence out (use GHL `if` branch) |
| `{{party_size}}` | FH / quote | leave out |
| `{{review_count}}` | **GHL custom value, updated weekly** from GBP (currently 1,401) | "hundreds of" |
| `{link:book_manchac}` etc. | Branded link to the specific FH item, not the homepage (SLAP rule "P") | — |

Keep the review count in a custom value so it never goes stale again. The old playbooks still say "384+".

### 0.6 Infrastructure dependencies (resolve before building; otherwise the workflows fire into nothing)
1. **Which system sends SMS from (504) 571-9975?** The A2P registration was filed through **OpenCX/Telnyx**. The Sales Playbook assumes GHL sends SMS, and it also recommends TourOpp GO. A number can only have one sending platform, and each platform needs its own 10DLC campaign. **Decision needed from David:** one SMS system of record for this number. If it's OpenCX, the SMS steps below get built there and GHL is used for email and logic only.
2. **FareHarbor abandoned-checkout data.** Confirm with Kevin Schmitt (FareHarbor) (a) whether our FH plan has native abandoned-checkout recovery, and (b) whether contact details typed before payment reach us by webhook or API. If neither, Segment A falls back to the website-side capture described there.
3. **OpenCX to GHL contact sync.** Magnolia conversations need to create or update GHL contacts with tags (`src-magnolia`, intent, requested date, party size). Confirm with Mo at OpenCX.
4. **FareHarbor to GHL booking webhook.** This is the exit trigger for everything. The Sales Playbook says the webhook is available. Test it before any workflow goes live, because a nurture message sent to someone who already booked is the worst failure here.

---

## 1. Segment overview

| Seg | Who | Trigger | Channel | Length | Exit |
|---|---|---|---|---|---|
| **A** | Started FareHarbor checkout, didn't pay | FH abandon event, or site-side capture | Email (SMS only if consent) | 3 steps / 3 days (compressed if tour date is close) | Booked · date passed · unsubscribe |
| **B** | Magnolia chat or SMS inquiry, no booking | OpenCX conversation closed + no FH booking in 2 hrs | SMS + email | 5 steps / 7 days | Booked · reply · STOP |
| **C** | Asked the price by phone or text, then went quiet | Tag `asked-price` + no reply in 24 hrs | SMS-led | 4 steps / 6 days | Booked · reply · STOP |
| **D** | Private/group quote sent, not accepted | GHL opportunity stage "Quote Sent" | Email + SMS + Ray call task | 5 steps / 10 days | Booked · marked lost · date passed |
| **E** | "Just exploring" / trip 60+ days out | Chatbot intent "exploring", or trip date ≥ 60 days | Email (hands off to Lead Nurture) | 2 bridge steps, then the existing Insider Guide sequence | Booked · unsubscribe |

**Routing rule when a contact fits more than one:** D beats A beats C beats B beats E. A group quote is the highest-value conversation. An abandoned checkout shows the highest intent.

---

## 2. The one-time offer rule (PROPOSED — needs David)

Offers train people to abandon on purpose. So the default is **no offer**. The sequences are built to win on answers, not discounts.

**The rule:**
1. **One offer per contact per rolling 12 months**, across all of 04, 05 and 10. Stamp `offer_used_date` on the contact when an offer is sent, and check it before sending another.
2. **Only one step per sequence may carry it.** That's the next-to-last step, never the first.
3. **Value-add before discount.** The approved list, in order of preference:
   - **Free round-trip shuttle upgrade** for the party (a $25/person value, capped at 4 guests = $100). It fixes the logistics objection and costs a seat that's already running. This is the default.
   - For guests who are driving: **PROPOSED** waterproof phone pouch at check-in (the Journey Map idea, $10 retail). This needs the item to exist first.
   - For private groups: **no price cut**. The rate card says private is an upsell, not a discount. Offer a free shuttle for up to 4 guests, or a flexible date change. Nothing off the rate.
4. **Only on dates with open inventory.** The requested departure must have **4 or more open seats** and not be a peak Saturday in Sept–Nov. Don't give value away on dates that sell themselves.
5. **Never stacked** with a partner or referral code (see 10). Stacking would pay commission on a discounted booking.
6. **Expires in 72 hours**, single use, tied to the contact (a FareHarbor promo code per contact, or one per segment per month).
7. **Holdout.** 20% of eligible contacts randomly get the same step **without** the offer, so we can measure whether the offer adds bookings or just gives away margin (see A/B test 1).

**Open item for Kevin Schmitt (FH):** can a promo code set the shuttle add-on to $0? If not, the fallback is a $25/person-off code limited to the party size. Or Ray comps it by hand on the manifest.

---

## 3. Segment A — Abandoned FareHarbor checkout

### Trigger
- **Primary:** FareHarbor abandoned-checkout event (if available, see 0.6 #2) with email captured. Wait 45 minutes, then check `booking.created` for the same email. No booking means enter the workflow.
- **Fallback (no FH data):** a GHL tracking event when a site visitor with a known GHL contact cookie (for example, from Magnolia or a form) clicks a FareHarbor "Book" button and no booking follows within 2 hours. It catches fewer people but costs nothing to add.

### Consent and channel
- **Email only by default.** The A2P opt-in says "Submission constitutes consent," and an abandoned checkout was never submitted. Don't text these contacts unless they are already SMS-consented from an earlier inquiry or booking (`sms_consent = true`). If they are, the optional SMS A-S1 goes out at step 1.

### Timeline
| Step | Standard timing | If the tour date is under 72 hrs away | Objection handled |
|---|---|---|---|
| A1 | +1 hr after abandon | +1 hr | Logistics, and it's the link back in |
| A2 | +24 hr | +6 hr (within the send window) | Weather + gators (trust) |
| A3 | +72 hr | Skip, or send 12 hrs before tour time if seats remain | Price/value + kids. **Offer step** (only if §2 allows) |

Hard stop 12 hours before the tour time on the abandoned date, or as soon as that departure sells out.

### A1 — email (+1 hr)
**Subject:** Your {{tour_date}} spot isn't held yet
**Preview:** No pressure. Here's the link back in, plus the one thing people forget.

> Hi {{first_name}},
>
> Looks like you started booking the {{tour_name}} for {{tour_date}} and didn't quite finish. Nothing's held until checkout goes through, so here's the link straight back to that date:
>
> **{link:resume_checkout}**
>
> The thing people most often forget is **getting there.** The launch is in the Manchac swamp, about 35 minutes from the French Quarter. You've got two options:
>
> - **Ride with us.** Round-trip shuttle from 740 N Rampart St, +$25/person. The van leaves 1 hr 15 min before tour time.
> - **Drive yourself** and meet us at the launch in LaPlace. Parking's free.
>
> Please don't plan on an Uber out there. There's no ride back.
>
> If something in the checkout tripped you up, just reply to this email. It comes to me.
>
> Ray
> New Orleans Kayak Swamp Tours · (504) 571-9975

**Optional SMS A-S1 (only if `sms_consent = true`):**
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Your {{tour_date}} spot isn't held until checkout finishes: {link:resume_checkout} Reply STOP to opt out.
```
*(~150 chars)*

### A2 — email (+24 hr)
**Subject:** Two honest answers before you book
**Preview:** What happens if it rains, and whether you'll see alligators.

> Hi {{first_name}},
>
> Two questions come up more than any others, so here are the straight answers.
>
> **"What if it rains?"** We paddle in light rain. Honestly, the swamp is beautiful in it. We only cancel for lightning or severe weather, and when we cancel, you get a full refund. Free cancellation on your end up to 48 hours before your tour.
>
> **"Will we see alligators?"** At Manchac, from spring through fall, they're common, not guaranteed. They're wild, and we don't bait them or promise them. What you'll see every time is the second-largest bald cypress swamp in the country, from a silent kayak at water level, with a trained naturalist who knows where to look. When it's cold (under about 65°F), the gators go quiet and the migratory birds take over.
>
> That honesty is a big part of why we're at 4.9 stars on Google from {{review_count}} reviews since 2013.
>
> Your date's still here if you want it: **{link:resume_checkout}**
>
> Ray

### A3 — email (+72 hr) — value + kids, with the offer only if §2 allows
**Subject:** What's included on the swamp tour
**Preview:** Guide, gear, and 2 hours in the cypress. Plus who it's right for.

> Hi {{first_name}},
>
> Last note on this, promise. Here's what the {{tour_name}} includes, because it's more than a kayak rental:
>
> - A trained naturalist guide, with 12 guests max on public tours
> - Stable tandem sit-on-top kayaks, paddles and USCG life jackets
> - A safety briefing before launch. Guides are CPR-certified.
> - About 2 hours on flat water with no current. No experience needed.
>
> **Bringing kids?** The minimum age is 8, and anyone under 16 paddles tandem with an adult. Most kids end up being the ones who spot wildlife first.
>
> [**OFFER BLOCK: include only if §2 conditions pass. Otherwise delete.**]
> *If you book by {{offer_expiry}}, the round-trip shuttle from 740 N Rampart is on us for up to 4 guests. Use code {{offer_code}} at checkout.*
>
> **{link:resume_checkout}**
>
> If the timing's just not right, no worries. We run year-round.
>
> Ray

---

## 4. Segment B — Magnolia (chat) or SMS inquiry that didn't book

### Trigger
- An OpenCX/Magnolia conversation, or an inbound SMS thread, closes with intent = `booking_inquiry` or `pricing` or `availability`. The contact has a phone or email. **No FH booking within 2 hours.**
- GHL tag `inquiry-no-booking` (the tag named in Sales Playbook §2, kept on purpose). Also store `requested_date`, `party_size`, `has_kids` and `tour_interest` if Magnolia captured them.
- **Skip B1** if a human (Ray) already replied in that thread within the last 2 hours. Start at B2.

### Timeline
| Step | Timing | Channel | Objection |
|---|---|---|---|
| B1 | +2 hr (in send window) | SMS | Logistics: "what's the next step" |
| B2 | Day 1, 9:30 AM | Email | Gators + safety (trust) |
| B3 | Day 3, 10:00 AM | SMS | Weather or kids (branch on `has_kids`) |
| B4 | Day 5, 9:30 AM | Email | Price/value. **Offer step** if §2 allows |
| B5 | Day 7, 11:00 AM | SMS | Break-up (the highest-reply message) |

### B1 — SMS (+2 hr)
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Want me to check {{requested_date}} for you, or is it easier to book here: {link:book_manchac} Reply STOP to opt out.
```
*(~160 chars. If `requested_date` is empty, use: "Want me to check a date for you, or is it easier to book here: ...")*

### B2 — email (Day 1)
**Subject:** Is a kayak swamp tour safe? The honest answer
**Preview:** What the guides do, what the gators do, and why beginners are fine.

> Hi {{first_name}},
>
> Thanks for chatting with us yesterday. Here's the answer to the question most people don't quite ask out loud: is this safe?
>
> - **The water's calm.** It's flat swamp with no current. Most of our guests have never kayaked before.
> - **The boats are stable.** Tandem sit-on-top kayaks, rated to 400 lbs combined.
> - **The guides are trained.** CPR-certified naturalists. Everyone gets a safety briefing and a USCG life jacket before launch.
> - **The gators aren't interested in you.** Alligators are common at Manchac from spring through fall, not guaranteed. They keep their distance from a quiet group of kayaks. Your guide explains how to watch them before you launch.
>
> We use silent kayaks, not airboats, and that's the whole point. No engine means the wildlife stays put and you hear the swamp.
>
> 4.9 stars on Google from {{review_count}} reviews since 2013. Guests mention their guides by name all the time.
>
> **{link:book_manchac}**. The Manchac Swamp Wildlife Tour, from $65/person.
>
> Ray
> *Just reply if you've got a question. It comes to me.*

### B3 — SMS (Day 3). Branch on `has_kids`
**If `has_kids = true`:**
```text
{{first_name}}, quick note for families: kids 8+ are welcome, under-16s paddle tandem with an adult. Flat water, no current. {link:book_manchac} - Ray
```
*(~150 chars)*

**Otherwise (weather):**
```text
{{first_name}}, if weather's the worry: we paddle in light rain and only cancel for lightning. If we cancel, full refund. {link:book_manchac} - Ray
```
*(~148 chars)*

### B4 — email (Day 5) — price/value, with the offer if §2 allows
**Subject:** Why the kayak tour costs what it does
**Preview:** $65 buys a guide, the gear, and a swamp most visitors never see.

> Hi {{first_name}},
>
> Fair question if you're comparing: why $65 a person?
>
> Because you're not a seat on a boat of 30. You're one of **12 guests max**, in your own kayak, with a trained naturalist who's been paddling this swamp for years. That covers the gear, the life jackets, the safety briefing, and about 2 hours in the Maurepas Swamp, the second-largest bald cypress swamp in the country.
>
> Here's what it looks like:
> - **Manchac Swamp Wildlife Tour** · 2 hrs · from $65/person. The most popular one.
> - **Extended Manchac** · 4 hrs · $130/person. Better for photographers and serious wildlife watchers.
> - Add the **round-trip shuttle** from 740 N Rampart for +$25/person, or drive to the launch yourself.
>
> [**OFFER BLOCK. Only if §2 passes:** *Book by {{offer_expiry}} with code {{offer_code}} and the shuttle's on us for up to 4 guests.*]
>
> **{link:book_manchac}**
>
> Ray

### B5 — SMS (Day 7) — break-up
```text
{{first_name}}, last text from me. If the swamp doesn't fit this trip, no worries. If it does, here's the link: {link:book_manchac} - Ray
```
*(~135 chars)*

---

## 5. Segment C — Asked the price by phone or text, then went quiet

### Trigger
- Ray (or Magnolia) sends a price by SMS or on a call and applies the tag `asked-price`. Magnolia can tag it automatically on a pricing intent.
- **No inbound reply within 24 hours**, and no FH booking. Then enter.
- Covers the missed-call auto-text flow (Sales Playbook §1) when the lead replied once with a price question and then stopped.

### Timeline
| Step | Timing | Channel | Objection |
|---|---|---|---|
| C1 | +24 hr after the price was sent | SMS | Price: what's included |
| C2 | Day 3 | SMS | Logistics: shuttle vs. driving |
| C3 | Day 3 (only if email is on file) | Email | Trust + gators |
| C4 | Day 6 | SMS | Break-up. **Offer step** if §2 allows |

### C1 — SMS (+24 hr)
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. The $65 covers your guide, kayak, gear and ~2 hrs in the swamp. 12 guests max. Reply STOP to opt out.
```
*(~160 chars)*

### C2 — SMS (Day 3)
```text
{{first_name}}, easiest way out: round-trip shuttle from 740 N Rampart, +$25/pp. Or drive 35 min to the launch. Want me to check a date? - Ray
```
*(~144 chars. It asks a question on purpose, because questions get replies.)*

### C3 — email (Day 3, if email on file)
Reuse **B2** (safety and gators) with this first line instead: "Thanks for calling about the swamp tour. Here's the question most people don't quite ask out loud: is this safe?"

### C4 — SMS (Day 6)
**Without offer:**
```text
{{first_name}}, last one from me. If the swamp fits your trip, book here: {link:book_manchac} If not, enjoy New Orleans. - Ray
```
*(~128 chars)*

**With offer (only if §2 passes):**
```text
{{first_name}}, last one from me. Book by {{offer_expiry}} with code {{offer_code}} and the shuttle's on us (up to 4): {link:book_manchac} - Ray
```
*(~150 chars)*

---

## 6. Segment D — Group or private quote sent, not accepted

### Trigger
- The GHL opportunity in pipeline **"Private & Groups"** moves to stage **Quote Sent**. Required fields: `party_size`, `requested_date`, `tour_name`, `quote_total`, `quote_link` (a FareHarbor private-tour item link or an invoice link).
- Quote from [[Operations/Private Tour Rate Card]]. **Quote the total, not the per-head, for parties of 4 and up.** Over 20 guests is an internal escalation, not an automated quote.

### Exit
Booked (FH booking or deposit) · opportunity marked Won or Lost · `requested_date` passes · the contact asks to stop.

### Timeline
| Step | Timing | Channel | Objection |
|---|---|---|---|
| D1 | +24 hr | Email | Logistics: what happens next, and who drives |
| D2 | +48 hr | SMS + Ray call task if party ≥ 13 | "Any questions from the group?" |
| D3 | Day 5 | Email | Mixed ability, kids, and "will everyone like it" (trust) |
| D4 | Day 7, or 14 days before the date if that's sooner | Email + SMS | Date hold / real availability. **Offer step** if §2 allows (no price cut) |
| D5 | Day 10 | SMS | Break-up, then Ray marks Won or Lost |

### D1 — email (+24 hr)
**Subject:** Your private swamp tour quote for {{requested_date}}
**Preview:** {{quote_total}} for your group of {{party_size}}. Here's how the day works.

> Hi {{first_name}},
>
> Here's your quote again so it's easy to find: **{{quote_total}} for your group of {{party_size}}** on the {{tour_name}}, {{requested_date}}. The swamp's yours. No other guests.
>
> **How the day works**
> - **Getting there:** Round-trip shuttle from 740 N Rampart St for +$25/person, leaving 1 hr 15 min before tour time. Or your group can drive to the launch in LaPlace, about 35 minutes from the French Quarter.
> - **On the water:** A safety briefing, then about 2 hours paddling (4 on the Extended) with a trained naturalist guide.
> - **Weather:** We paddle in light rain. If we cancel for lightning or severe weather, you get a full refund.
>
> **To lock it in:** {link:quote_link}
>
> Questions from the group? Forward this to them, or just reply. It comes to me.
>
> Ray
> New Orleans Kayak Swamp Tours · (504) 571-9975

### D2 — SMS (+48 hr)
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Any questions from the group on the {{requested_date}} private tour? Happy to call. Reply STOP to opt out.
```
*(~160 chars)*
**Internal:** if `party_size ≥ 13`, also create a GHL task: "Call {{first_name}} today, and send the quote link by text after the call."

### D3 — email (Day 5)
**Subject:** "Will everyone in the group be OK?"
**Preview:** Beginners, kids, and the one friend who's nervous about gators.

> Hi {{first_name}},
>
> When a group's deciding, there's usually one person with a question they haven't asked yet. Here are the usual ones:
>
> - **"I've never kayaked."** Most of our guests haven't. The water is flat with no current, and the tandem kayaks are very stable.
> - **"I'm nervous about alligators."** Totally normal. They're common at Manchac from spring through fall, not guaranteed, and they keep their distance from a quiet group. Your guide covers it at the briefing.
> - **"Can kids come?"** Ages 8 and up. Anyone under 16 paddles tandem with an adult.
> - **"What about size?"** Tandems hold 400 lbs combined. Solo paddlers are most comfortable under 250. Let me know the group and I'll set up the boats.
>
> Your quote: **{{quote_total}} for {{party_size}}.** {link:quote_link}
>
> Ray

### D4 — email + SMS (Day 7, or 14 days before the date if sooner)
Only say "holding" if Ray actually is. Otherwise use the version without it.

**Email subject:** Checking on {{requested_date}}
**Preview:** Private dates go first in the fall. Want me to keep yours open?

> Hi {{first_name}},
>
> Quick check-in on your private tour for {{requested_date}}. Private tours need a guide crew assigned, so dates can close up, especially weekends from September through November.
>
> {{#if hold_active}}I'm holding that date for your group until **{{hold_expiry}}**.{{/if}}
>
> [**OFFER BLOCK. Only if §2 passes:** *If you confirm by {{offer_expiry}}, the shuttle's on us for 4 of your guests.* No discount on the private rate.]
>
> **{link:quote_link}**
>
> Ray

**SMS:**
```text
{{first_name}}, checking on {{requested_date}} for your group. Want me to keep that date open? Link to confirm: {link:quote_link} - Ray
```
*(~140 chars)*

### D5 — SMS (Day 10) — break-up
```text
{{first_name}}, I'll close out your quote for now. If plans change, reply here and I'll recheck the date. - Ray
```
*(~115 chars)*
**Internal:** 48 hrs after D5 with no reply, Ray marks the opportunity Lost with a reason (price / date / went elsewhere / no reply). Those reasons feed the KPI table.

---

## 7. Segment E — "Just exploring" / far-future dates

### Trigger
- Magnolia intent = `exploring`, or `requested_date` is 60 or more days out, or the guest says something like "just looking," "next year" or "not sure when."
- Also: contacts who exit A–D because their date passed.

### Why this segment is different
These people aren't going to book this week, and pushing them wastes the relationship. [[Marketing/NKST — Lead Nurture Strategy]] already has the right answer: the **Insider Guide** sequence (2 emails a week, no pitch in the first 3, CTAs keyed to trip date at 6, 3 and 1 weeks out). **Don't build a second nurture.** Segment E is a two-step bridge into that one.

### Timeline
| Step | Timing | Channel | Objection |
|---|---|---|---|
| E1 | Immediate | Email | None. Give value and set expectations |
| E2 | Day 2 | Email | Trust: "who are these people?" |
| E3 | Day 4 → | Enrolls in the existing Insider Guide sequence (Lead Nurture email 2 onward) | Per that doc |
| E4 | 21 days before `trip_month` start (if SMS consent) | SMS | Logistics + timing |

### E1 — email (immediate)
**Subject:** No rush. Here's how to plan the swamp part.
**Preview:** When to go, what to book first, and a free local's guide to the city.

> Hi {{first_name}},
>
> Sounds like you're early in planning. Good. That's when the best dates are still open. Three things worth knowing now:
>
> 1. **Fall is the best season, and it books up first.** Mild temperatures, active wildlife, fewer bugs.
> 2. **Summer is hot**, so the 9:00 AM tour is the one to grab.
> 3. **Winter still runs** (40s–60s°F). Alligators go quiet below about 65°F, but the migratory birds come in.
>
> While you plan, we put together a free **New Orleans Insider Guide**: neighborhoods, food and the stuff locals do. There's no sales pitch in it. **{link:insider_guide}**
>
> When you know your dates, reply with them and I'll tell you honestly which tour and time fits.
>
> Ray

### E2 — email (Day 2)
**Subject:** Who we are (and what we won't promise you)
**Preview:** Since 2013. Silent kayaks, not airboats. Honest about wildlife.

> Hi {{first_name}},
>
> Quick intro, since you'll be hearing from us now and then.
>
> We've been paddling guests through the Manchac swamp since 2013. Silent kayaks, not airboats. 12 guests max. Trained naturalist guides. We're 4.9 stars on Google from {{review_count}} reviews, and TripAdvisor gave us a Travelers' Choice award.
>
> One thing we don't do is promise alligators. At Manchac they're common from spring through fall, not guaranteed. We'd rather you trust us than feel oversold.
>
> Next up, I'll send you the neighborhoods we think are worth leaving the French Quarter for.
>
> Ray

### E4 — SMS (21 days before the trip month, SMS-consented only)
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Your trip's coming up. Want me to check swamp tour dates for you? Reply STOP to opt out.
```
*(~150 chars)*

---

## 8. Objection coverage map

Each objection is handled at least once per segment, in the order people tend to raise it.

| Objection | A | B | C | D | E | Source fact |
|---|---|---|---|---|---|---|
| **Price** | A3 | B4 | C1, C4 | D1 (total), D4 | — | From $65; 12 max; guide + gear included |
| **Weather** | A2 | B3 | — | D1 | E1 (seasons) | Light rain OK; lightning cancels; full refund when we cancel |
| **Gators** (fear or disappointment) | A2 | B2 | C3 | D3 | E2 | "Common, not guaranteed"; spring–fall; quiet below 65°F |
| **Kids** | A3 | B3 (branch) | — | D3 | — | Minimum age 8; under 16 paddles tandem |
| **Logistics** | A1 | B1 | C2 | D1 | E4 | Shuttle from 740 N Rampart +$25, leaves 1 hr 15 min before; 35 min drive; no Uber |
| **Trust** | A2 | B2 | C3 | D3 | E2 | 4.9★, {{review_count}}, since 2013, Travelers' Choice, CPR-certified guides |

---

## 9. KPIs

Measure weekly. Report monthly next to the review scorecard in [[05 — Review Engine]].

| Metric | Definition | Target (first 90 days) | Note |
|---|---|---|---|
| Abandoned checkout recovery (A) | Bookings within 7 days ÷ contacts entered | **10%** | The Sales Playbook's 15–25% benchmark assumes SMS within 30–60 minutes. Segment A is email-first for consent reasons, so the target is lower. |
| Inquiry → booking (B) | Bookings within 14 days ÷ contacts entered | **12%** | |
| Price-ghost recovery (C) | Bookings within 14 days ÷ contacts entered | **8%** | The Sales Playbook's 5-message benchmark is 3–8% |
| Private quote close rate (D) | Won ÷ quotes sent | **35%** | Track the lost reasons too |
| Exploring → booked (E) | Booked by trip date ÷ contacts entered | **5%** | Long cycle. Measure by cohort. |
| Reply rate (SMS) | Replies ÷ SMS delivered | 20%+ | Replies go to Ray. That's the point. |
| Opt-out rate (SMS) | STOP ÷ delivered, per message | **< 2% per message** | Any single message over 3%: pull it and rewrite |
| Email unsubscribe | Unsubs ÷ delivered | < 0.5% | |
| Offer rate | Contacts sent an offer ÷ contacts entered | **< 25%** | If it climbs, the rule in §2 is leaking |
| Offer incrementality | Booking rate with offer − holdout | > 3 pts, or cut the offer | See A/B 1 |
| Sent to already-booked | Nurture messages delivered after `booked` | **0** | Any non-zero is a bug. Fix it the same day. |
| Revenue recovered | Sum of FH booking value attributed to these workflows | Report only | Attribution is last touch within 7 days |

---

## 10. A/B test ideas (one at a time per segment, at least 100 contacts per arm)

1. **Offer vs. no offer (holdout).** In A3, B4, C4 and D4, 80% get the §2 offer and 20% get the same message without it. This decides whether the offer stays.
2. **A1 timing:** +1 hr vs. +3 hr after abandon.
3. **Plain text vs. light design:** Ray's plain-text A1 vs. the same copy with one guide photo.
4. **Trust proof in B2:** "4.9 stars from {{review_count}} reviews" vs. "since 2013" vs. a one-line guest quote naming a guide.
5. **B1 format:** a question ("Want me to check a date?") vs. a direct link. Measure replies and bookings.
6. **Subject line on A2:** "Two honest answers before you book" vs. "Rain, gators and refunds."
7. **C1 price framing:** "$65 covers your guide, kayak, gear" vs. "12 guests max, trained naturalist, ~2 hrs."
8. **D1 total vs. per head** for parties of 4+. The rate card says the total closes better, so test it.
9. **Send-time tests on emails:** 6:30 AM vs. 8:00 PM local to the contact (Lead Nurture deliverability item 4).

---

## 11. Contradictions found and what this file supersedes

| # | Where | What it says | What this file does |
|---|---|---|---|
| 1 | Sales Playbook §2 Msgs 2, 3, 5; §3 examples; §4; Chatbot & SMS Script v2 | "384+ five-star reviews," "400+ tours without a single guest harmed," "almost every tour sees live alligators," "alligators almost guaranteed," "we'll make it right" if no gator | **Superseded.** The review count is now 1,401 and held in a custom value. The safety count isn't verified (and 400 tours looks far too low for a business running since 2013). Gator claims break "common, not guaranteed." A make-good for no gators is an implied promise. |
| 2 | Sales Playbook §3 (SLAP): "NEVER lead with the company name" | vs. the SMS rule that the first message must include the brand | **Superseded for first messages only.** The brand goes in the first SMS as "Ray at New Orleans Kayak Swamp Tours," right after the first name, so the hook still comes first. Later messages follow SLAP. |
| 3 | Sales Playbook and Chatbot v2 use emoji; "Spots fill up fast" | Voice rules (few exclamation marks) and GSM-7 cost | Emoji removed. Scarcity is only stated where it's real (fall weekends). |
| 4 | Sales Playbook links to "NolaKayakTours.com" | The fact sheet site is neworleanskayakswamptours.com | Use branded links on an owned domain. David to confirm whether NolaKayakTours.com still resolves. |
| 5 | Sales Playbook §4 Obj. 5: "50% if under 48 hours" | FAQ: no refund inside 48 hrs | Uses only "Free cancellation up to 48 hours before your tour" (Fact Sheet open question 2). |
| 6 | Sales Playbook Flow B: "our max-8 tours"; Journey Map: "10 people max" | The fact sheet says 12 max | Uses 12. |
| 7 | Sales Playbook Flow A: pickup "in the Marigny"; Journey Map: "door to door" | Pickup is 740 N Rampart St, the edge of the Quarter. It's not door-to-door. | Uses 740 N Rampart St. Never says door-to-door. |
| 8 | Sales Playbook Flow C: "we can arrange hotel pickup" for private groups | Not in the fact sheet or the rate card | Not claimed. **Open question for David.** |
| 9 | A2P samples: "NOLA Kayak Swamp Tours:" prefix; "Launch from Reserve, LA"; "8:30 AM" launch | The registered DBA is "New Orleans Kayak Swamp Tours"; the launch is LaPlace; the times are 9:00/11:30/2:00/4:30 | Uses the full DBA name. **Flag:** the A2P sample messages may need to be refiled to match what actually sends. Carriers compare live traffic to the samples. |
| 10 | A2P filed on OpenCX/Telnyx; the Sales Playbook assumes GHL SMS and also recommends TourOpp GO | One number can have only one SMS platform | Blocking decision (0.6 #1). |
| 11 | Sales Playbook KPI: 15–25% abandoned recovery "within 30–60 min" by SMS | An unfinished checkout isn't SMS consent under the A2P opt-in | Segment A is email-first. Target lowered to 10%. |
| 12 | Lead Nurture deliverability: `nolakakyaktours.com` | Typo | Flagged. Use the real domain. |
| 13 | Fact Sheet "Private tours: more than 20 guests, call David" | Correct internally, but it must never reach a guest | Kept internal only. Guests always hear from Ray. |

---

## 12. Contractor build checklist

- [ ] Resolve the 0.6 dependencies (SMS system of record, FH abandon data, OpenCX sync, FH booking webhook tested)
- [ ] Create tags: `inquiry-no-booking`, `asked-price`, `booked`, `replied`, `resume-nurture`, `src-magnolia`, `src-phone`, `src-fh-abandon`, `seg-a` … `seg-e`
- [ ] Create custom fields: `requested_date`, `party_size`, `has_kids`, `tour_interest`, `sms_consent`, `offer_used_date`, `offer_code`, `offer_expiry`, `quote_total`, `quote_link`, `hold_active`, `hold_expiry`, `trip_month`
- [ ] Create custom value `review_count`, plus a weekly task for Ray to update it from GBP
- [ ] Set up the branded link domain and create `{link:...}` trigger links for each FH item
- [ ] Build workflows A–E with the global goal event (`booked` exits all) and the SMS send window 8:00 AM–9:00 PM Central
- [ ] Build the frequency cap (1 marketing SMS a day, 4 a week)
- [ ] Build the §2 offer eligibility check (a custom field plus an availability check done by hand in phase 1)
- [ ] Set up the 20% holdout split on offer steps
- [ ] QA: run a test contact through each segment, then book in FH mid-sequence and confirm the exit fires within 5 minutes
- [ ] Get David's sign-off on the copy, then go live one segment at a time. Start with B (the most volume, least risk) and do A last (it depends on FH).
