# DCKT — GHL Automation Sequences
*Every message, every trigger — build-ready*
*Owner: David Rack (setup) · Bella Sgriccia (maintenance)*

---

## How to Use This Document

Each sequence below is ready to build in GHL's workflow builder. For each one:
1. Create a new Workflow in the DCKT sub-account
2. Set the trigger (noted for each sequence)
3. Add the actions in order (SMS/email, wait timers, conditions)
4. Test with a real booking before going live

**GHL DCKT Sub-Account:** use the DCKT location ID from the GHL reference doc.

---

## Sequence 1 — Missed Call Lead Nurture
*Trigger: incoming call not answered*
*Goal: recover the lead before they book with a competitor*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | Immediate | SMS | "Hi! Door County Kayak Tours here — so sorry we missed you! Can we help you plan something amazing? Check live availability at doorcountykayaktours.com or just text back 😊" |
| 2 | +24 hrs (if no reply) | SMS | "Hey — still thinking about getting out on the water? Cave Point is one of the most stunning spots in Wisconsin and you can only get there by kayak. Here's what guests say: [TripAdvisor link]. Spots fill fast on weekends!" |
| 3 | +72 hrs (if no reply) | SMS | "Last one from us! We have a few openings this weekend if you're still interested. No experience needed — we take care of everything. Book in 2 minutes: doorcountykayaktours.com 🌊" |

**Stop trigger:** Guest replies or books.

---

## Sequence 2 — Booking Confirmation + Upsell
*Trigger: new booking created in FareHarbor (webhook → GHL)*
*Goal: celebrate the booking, open the upsell conversation, set the tone*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | Immediate | SMS | "🎉 You're on! [Name], we just confirmed your [TOUR NAME] on [DATE] at [TIME] — we are SO excited to have you out there. Is this a special occasion? Let us know and we'll make it extra special." |
| 2 | +30 min (if no reply to occasion question) | SMS | "Quick question — have you considered going private? For your group size, it's only $[PRICE DIFF] more and you get the whole experience to yourselves — your pace, your guide, your adventure. Just reply 'private' and we'll upgrade you now." |
| 3 | +1 hr (if no upgrade) | SMS | "P.S. — we also run Lykke Sauna Co. right here in Door County. A post-paddle sauna is honestly the perfect ending to a day on the water. Ask us when you arrive or reply 'sauna' for details 🧖" |

**Branch:** If guest says "private" → manual flag for David/Bella to process upgrade.
**Branch:** If special occasion noted → add tag in GHL, flag for guide briefing.

---

## Sequence 3 — Anticipation Arc (Pre-Tour)
*Trigger: booking confirmed, runs on schedule leading up to tour date*
*Goal: build excitement, prepare the guest, arrive in a peak state*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | T-3 days | SMS | "Hey [Name]! 3 days until your Cave Point kayak tour 🌊 Did you know the sea caves there are only accessible by water? You're about to see something most people never get to experience up close. We can't wait to show you. Any questions before [DAY]?" |
| 2 | T-1 day (6pm) | SMS | "Tomorrow's the day, [Name]! Your guide [GUIDE NAME] is stoked to take you out. Weather looks [CONDITION] — perfect for the caves. Quick checklist: ✅ Hat + sunscreen ✅ Light layers (no cotton) ✅ Water shoes ✅ Camera 📸 — Meeting point: Schauer Park Boat Launch at [TIME]. See you there!" |
| 3 | Day-of (2 hrs before) | SMS | "Good morning [Name]! 🙌 Today's the day. [Guide Name] is heading to the launch now. Conditions look great. See you at [TIME] — look for the blue van. Get pumped!" |

**Note:** T-3 message should reference the specific tour (Cave Point vs Sunset vs Inland, etc.)

---

## Sequence 4 — Post-Tour Fan Creation
*Trigger: tour end time passed (FareHarbor → GHL)*
*Goal: capture the glow, get the review, plant the return*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | +1 hr after tour | SMS | "That was incredible, [Name]! It was so great having you with us today 🌊 We hope Cave Point blew your mind. If you got any great shots out there, tag us — we'd love to share them! @doorcountykayak" |
| 2 | +3 hrs | SMS | "Hey [Name] — one small favor? If [Guide Name] and the crew made your day, a quick Google review means the world to our small team and helps other families find us. Takes 2 min: [GOOGLE LINK] 🙏 Thank you!" |
| 3 | +24 hrs | SMS | "One more thing, [Name] — if you have friends or family visiting Door County this summer, we'd love to take care of them. Share this and they'll get $10 off their first tour, and we'll send you a little thank-you: [REFERRAL LINK]" |
| 4 | +7 days | SMS | "Hey [Name]! Hope you're still feeling that Door County magic ✨ You did the Cave Point tour — have you ever done the Sunset Tour? Completely different vibe, totally worth coming back for. Reply 'sunset' and we'll check availability for you." |
| 5 | October (end of season) | Email | "Hey [Name] — wrapping up an amazing season here at DCKT! We hope we made your Door County trip unforgettable. We open bookings for next summer in March — want us to reach out when spots go live? Just reply 'yes' and you'll be first in line 🙌" |

---

## Sequence 5 — Returning Guest (2nd Visit+)
*Trigger: booking detected where contact has prior booking history*
*Goal: make them feel known, deliver something different, deepen the relationship*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | Immediately at booking | SMS | "Welcome back, [Name]! 🙌 We noticed this isn't your first time out with us — and we love that. Your guide knows you've been before. We've got something a little different planned for you this season. Can't wait." |
| 2 | T-1 day | SMS | "Tomorrow's the day, [Name]! Since you've been out with us before, your guide is going to show you something a little different — something we don't show first-timers. You've earned it. See you at [TIME] at Schauer Park." |
| 3 | +1 hr after tour | SMS | "Always great having you back, [Name]. Seriously — repeat guests are what this whole thing is about. Did [Guide] show you [the thing]? Hope it was worth coming back for. See you next time. 🌊" |
| Alumni: after 3rd visit | Manual trigger | Personal SMS from David | "Hey [Name] — I just saw you've now been out with us 3 times. That genuinely means a lot to me. You're part of this place now. Thank you." |

---

## Sequence 6 — Weather Cancellation
*Trigger: manual activation by David/Bella when cancelling due to weather*
*Goal: retain the customer, make the disappointment feel handled*

| Step | Timing | Channel | Message |
|---|---|---|---|
| 1 | As soon as decision made | SMS | "Hey [Name] — we have to make the call to cancel today's tour due to [wind/conditions]. I know that's disappointing and I'm sorry. Your booking is fully protected — here's how to reschedule: [LINK]. If you need anything, reply here and I'll personally help you find a new date." |
| 2 | +1 hr (if no reschedule) | SMS | "Hey — just checking in. Were you able to find a date that works? If the calendar isn't showing what you need, just reply and I'll see what we can do. We really want to get you out there." |
| 3 | +24 hrs (if still no reschedule) | SMS | "Last check-in, [Name]. Your booking credit is saved and never expires. Whenever Door County calls you back — we'll be here. Just text this number to book: doorcountykayaktours.com" |

---

## Sequence 7 — End of Season / Winter Reactivation
*Trigger: annual automation, runs October + March*
*Goal: stay top of mind, capture early season bookings*

**October (closing season):**
> Email to all past guests (past 2 years):
> Subject: "One last thing before we wrap up the season..."
> "Hey [Name] — we just wrapped up another incredible season on the water. Hope you made it out this year. If you did — thank you. If you didn't — next year. We open bookings for the 2027 season in March. Reply 'notify me' and you'll be first to know when spots go live. See you on the water. — David & the DCKT crew"

**March (season opening):**
> Email to all "notify me" replies + past guests:
> Subject: "We're back — and spots are already filling"
> "Hey [Name] — it's that time of year. Cave Point is waiting. We officially open for the 2027 season [DATE] and early bookings are already coming in. Here's your early access link: [LINK]. Weekends fill fast — grab your date before it's gone."

---

## Sequence 8 — Gift Card Push (Holiday)
*Trigger: November 15 → December 20 annual automation*

> Email + SMS to all past guests:
> "Know someone who needs a Door County adventure? Our gift cards make the perfect gift — they never expire and can be used for any tour, e-bike rental, or sauna session. [BUY NOW: link]"
> "P.S. — last day to guarantee delivery before Christmas is [DATE]."

---

## Build Priority Order

1. ✅ Missed Call Auto-Reply (Sequence 1 — Step 1 only, 10 min to build)
2. Booking Confirmation (Sequence 2 — Step 1, wire FareHarbor webhook first)
3. Anticipation Arc (Sequence 3 — all 3 steps)
4. Post-Tour Review + Referral (Sequence 4 — Steps 1–3)
5. Weather Cancellation (Sequence 6)
6. Upsell at Booking (Sequence 2 — Steps 2–3)
7. Returning Guest (Sequence 5)
8. End of Season (Sequence 7)
9. Gift Card Push (Sequence 8)
10. Post-Tour Re-engagement (Sequence 4 — Steps 4–5)

---

## FareHarbor → GHL Webhook Setup

To trigger sequences from FareHarbor bookings:
1. GHL → DCKT sub-account → Settings → Integrations → Webhooks
2. Copy the inbound webhook URL
3. FareHarbor → Settings → Webhooks → add GHL URL
4. Map fields: customer name, email, phone, tour name, tour date/time
5. Test with a manual booking

**Fields needed from FareHarbor:** first_name, last_name, email, phone, item_name (tour), start_time, booking_count (for returning guest detection)

---

*Related: [[Playbook/00 — Master Business Operating System]]*
*Related: [[Playbook/02 — Customer Journey Map]]*
*Related: [[DCKT — Sales Process Upgrade (Tony Robbins Framework)]]*
