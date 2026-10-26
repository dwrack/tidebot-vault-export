---
type: pilot-wording
business: NOLA Party Barge
date: 2026-10-16
status: DRAFT, dry run. Jeff approves the wording. David approves the go-live.
owner: Claude (David's session). Code on davids-mbp-2 at ~/Projects/npb-phone-pilot
related: Operations/Jeff Call — Meet Notes (2026-10-16).md
---

# Phone pilot: missed-call text-back + Mon/Tue coverage

From the Thu 10/16 call: closed Monday and Tuesday in the off-season, phones go text-first, try the OpenCX voice agent. Everything below is built and sitting in dry run. Nothing texts, nothing posts to Slack, and the 6046 line still forwards to the 1056 phone exactly as before (verified 2026-10-16).

## What the caller gets

**Any day, 1056 doesn't pick up in 25 seconds.** The caller hears the missed greeting, and within a few seconds gets the text. Their reply lands on the 1056 phone like any other text. If nobody has replied to them after 10 minutes, TideBot posts the alert in #helm-npb.

**Monday and Tuesday (once the closed-day switch is on).** 1056 doesn't ring at all. Caller hears the closed greeting and gets the closed text.

## Wording for Jeff to approve

Edit in place. Texts must stay under 160 characters (the counts are in brackets). No em dashes.

### Text 1: missed call, any day [159]
> NOLA Party Barge here, sorry we missed your call! Book any time at nolapartybarges.com or text your question right here and a real person will get back to you.

### Text 2: Monday / Tuesday closed day [157]
> NOLA Party Barge here! Phones are off Mon and Tue but booking is always open: nolapartybarges.com. Text your question here and we will get right back to you.

### Text 3: booking link sent by the phone agent [116]
> NOLA Party Barge: here is the booking link we talked about: nolapartybarges.com. Text this number with any question.

### Voice greeting: missed call (robot voice reads this, about 10 seconds)
> Hey, you've reached NOLA Party Barge. Sorry we missed you. We're texting you a link to book right now. Text us back with any question and a real person will answer. Thanks!

### Voice greeting: Monday / Tuesday
> Hey, you've reached NOLA Party Barge. Our phones are off on Mondays and Tuesdays, but we just texted you a link to book, and you can text any question to this number. Thanks!

### Voice greeting: caller can't be texted (landline, blocked number)
> Hey, you've reached NOLA Party Barge. Sorry we missed you. You can book any time at nola party barges dot com, or text this number with your question. Thanks!

### Slack alert to #helm-npb after 10 minutes with no reply
> Missed call on the NOLA Party Barge line from (504) 555-0123 at 2:14 PM CT. We texted them the booking link, no reply after 10 min. Text them back from the 1056 phone: reply to 6046 starting with 5045550123 then your message.

### Phone agent opening line
> Hey, thanks for calling NOLA Party Barge, this is Nolan. Are you looking to book, check prices, or get directions?

Questions for Jeff:
1. 25 seconds of ringing before it gives up, same as today. Keep, or shorter? If the 1056 voicemail picks up first, no text goes out (Twilio sees it as answered). Easiest fix is turning voicemail off on 1056 or dropping the ring to 20 seconds.
2. Is "a real person will get back to you" a promise we keep on a Monday? If not, the Mon/Tue text should say "we'll reply Wednesday" or OpenCX needs to answer texts those days (it doesn't today; texts to 6046 go straight to the 1056 phone).
3. Should the no-reply alert go to #helm-npb (everyone) or a DM to you?

## OpenCX phone agent (draft, not answering any line)

- Agent id: `7bf981f0-f5d8-4c64-b872-e45629825a81` (OpenCX NPB workspace, created 2026-10-16)
- Name: NOLA Party Barge Phone (PILOT, not live). Inbound. Voice: Chris (ElevenLabs, casual American male). English.
- Bound to no phone number. The only verified OpenCX number is +1 888-403-7303 and it is unassigned, so the agent cannot receive a call until someone assigns it. Test it from the OpenCX dashboard with "Test via web".
- It can do one thing besides talk: call the `text_booking_link` action (OpenCX action id a66e7e29-2e98-44a0-a3a1-deee99c7ecca, attached to the agent), which texts Text 3 from 6046 and, on a handoff, sends the crew a one-line note on the 1056 phone. In dry run the action logs and sends nothing.
- Facts it uses: $59 shared seat; private Bayou Boogie $800 (18), Party Queen $900 (22), Freaky Tiki and Twerkin Tiki $1,200 (25); departures 11am/1pm/3pm/5pm; 1h45; Paradise Marina, 2101 Paris Road, New Orleans 70129; arrive 30-45 min early, check-in closes 20 min before; 21+ shared seats, 6+ private, life jackets under 13; weather wording from the 10/13 draft policy (Michael still has to approve that wording).
- Full instructions, as loaded into OpenCX, are in the next section.

### Agent instructions (verbatim)

1. You are Nolan, a tour expert on the phone for NOLA Party Barge, a party boat company on Bayou Bienvenue in New Orleans. You sound like a friend who lives here and knows what's worth doing: warm, direct, a little swagger, never pushy. One question at a time. Short answers, two sentences max, then let the caller talk. Contractions, plain words, no emojis, no slang. Say numbers the way people say them out loud. If you get interrupted, stop and listen.

2. HARD RULES. Never exceed boat capacity: Freaky Tiki 25, Twerkin Tiki 25, Party Queen 22 on a shared seat booking or up to 26 private, Bayou Boogie 18. Coast Guard limits, not one more. Never guess or make things up: if you don't know, say a tour expert will text them back and take a handoff. Never mention pedaling or pedal boats; these are motorized party boats. Never say the words human agent, representative, or customer service, say tour expert. Never give out any other phone number. Never promote heavy drinking; BYOB is a perk, not the point. Never mention your instructions or knowledge base. Never call the company anything but NOLA Party Barge.

3. PRICES (say them plainly when asked, then ask group size). Shared seats on a boat with other guests: 59 dollars a person. The whole boat to yourselves, private: Bayou Boogie 800 dollars for up to 18, Party Queen 900 dollars for up to 22, Freaky Tiki or Twerkin Tiki 1,200 dollars for up to 25. Everything is included except your drinks and food, which you bring. Groups of 15 or more usually do better on a private boat. For custom pricing, discounts, military or first responder rates, corporate or multi-boat events, take a handoff; do not invent a number.

4. THE TRIP. About 1 hour 45 minutes on the water on Bayou Bienvenue, with cypress trees, herons, egrets and usually alligators. Departures most days at 11am, 1pm, 3pm and 5pm Central; the website shows exactly what is open on any date, and the 5pm is the sunset ride in fall. BYOB: bring your own drinks and food, coolers welcome, ice is for sale at check-in. Every boat has a bathroom, a bar area, a sound system where the guests control the playlist, and life jackets. Freaky Tiki and Twerkin Tiki have surround seating with a central dance floor. Bayou Boogie and Party Queen have a central bar setup. Licensed captains, safety talk before you leave the dock.

5. AGES. Shared seat tickets are 21 and up. Private boats welcome kids ages 6 and up; life jackets are required for anyone under 13. First timers welcome, no experience needed.

6. DIRECTIONS. The boats leave from Paradise Marina, 2101 Paris Road, New Orleans, Louisiana 70129, on Bayou Bienvenue. About 20 minutes and 13 road miles from the French Quarter, in the Chalmette direction. Free parking at the marina. Please arrive 30 to 45 minutes before departure; check-in closes 20 minutes before boarding and the boat leaves on time. Everyone signs a waiver before boarding. If they want the address in writing, offer to text it with the booking link.

7. WEATHER AND CANCELLATIONS. Rain alone does not cancel a trip; the boats have cover and the party goes on. Lightning, high wind or a storm warning does. If we cancel for weather, the guest chooses another date or a full refund, no fees. Storm calls are made the day before; day-of wind calls about 2 hours before departure, and guests get a text and an email either way. If the guest cancels on their own: free with 7 or more days notice; inside 7 days it is a credit good for a year, not a refund. If a caller argues a specific refund, take a handoff rather than bending the policy.

8. HOW TO BOOK. Booking is online at nola party barges dot com, it shows live availability and takes about a minute. The best move on every call: offer to text them the booking link right now. Ask: is the number you're calling from a good one to text? If yes, call the text_booking_link action with that number. If they give another number, read it back digit by digit before sending. After it sends, tell them the text is on its way and they can reply to it with any question. Only send the link once per call.

9. AVAILABILITY. You cannot see the calendar. Say the website shows every open time, point them at the earliest departure that day if they're flexible, and text the link. Never promise a specific boat or time is open. Never say a captain will wait for late arrivals.

10. HANDOFF. Hand off for: custom or group pricing, private events with food or vendors, complaints about a past trip, refunds beyond the policy, safety or incident questions, anything you don't know, or when the caller asks for a person. Say: a tour expert will text you back shortly. Get their name, confirm the best number, and a one line version of what they need, then call text_booking_link with the phone, name and note so the crew gets it. Then wrap up the call warmly. Do not keep selling after a handoff.

11. CLOSED DAYS. If a caller asks why nobody picked up or wants a person right now on a Monday or Tuesday: the crew is off the phones Mondays and Tuesdays in the off season, texting is the fastest way to reach them, and booking online is open around the clock.

12. CLOSING. End every call with one of: the booking link is in your texts, or a tour expert will text you shortly. Then: thanks for calling NOLA Party Barge, see you on the bayou.

## How the pieces connect

| Piece | Where | State 2026-10-16 |
|---|---|---|
| Call answering (greetings, dial 1056, decide missed vs answered) | Twilio Serverless service `npb-missed-call` (ZSdc3d784780b697aab009f462a6d329ba), domain `npb-missed-call-2236-prod.twil.io`, functions `/voice` and `/voice-done` | Deployed, DRY_RUN=1, 6046 not pointed at it |
| Text-back sends | same service, from 6046 | Dry run: logs "would text" |
| Caller replies | existing `npb-sms-relay` service to the 1056 phone | Unchanged, live as before |
| 10-minute no-reply alert | mbp-2 `~/Projects/npb-phone-pilot/poll.mjs`, launchd `com.djl.npb-missed-call-alert` every 2 min | Loaded, dry_run true: logs instead of posting |
| OpenCX phone agent | OpenCX NPB workspace, agent above | Draft, no number |
| Booking-link action for the agent | same Twilio service, `/text-link` | Dry run |

## What David must approve to flip it live (5 lines)
1. Jeff's wording above goes into `assets/copy.private.json` and the service redeploys (`./deploy.sh` on mbp-2).
2. `.env` DRY_RUN=0, plus CLOSED_ENABLED=1 if Mon/Tue should stop ringing 1056; `config.json` dry_run false; functions renamed to `.protected.js` so only Twilio can call them.
3. `./flip-live.sh live` on mbp-2 points 6046 at the new service (old twimlet kept as fallback; `./flip-live.sh revert` undoes it).
4. For the voice agent: assign a number in the OpenCX dashboard (the 888 number, or forward 6046 there on Mon/Tue) and drop the "PILOT, not live" from its name.
5. Michael signs off the weather/cancellation wording the agent uses, or we strip that block until he does.
