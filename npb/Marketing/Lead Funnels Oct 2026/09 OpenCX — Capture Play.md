# OpenCX Capture Play (2026-10-13)

*Draft for David's approval. Nothing below is live in OpenCX yet. Pairs with 07 (the build plan). Once approved, Claude applies items 1-5 in one sitting and logs the date here.*

## Why (60-day numbers, verified 2026-10-13)

492 chats, 87% Messenger. About 249 asked price or availability. 24 people typed an email. **0 were saved**, because the only action that writes to a contact ("Update Contact") is turned off for Messenger and Instagram. The three nudges are generic and get under 9% replies. Nolan's 107k-character prompt tells him to "collect name + phone + email" in Step 6 of a six-step flow, but real chats are 2.6 messages long, so Step 6 never arrives.

## 1. Fix the existing action (2 minutes)

"Update Contact" (PATCH contacts/{contact_id}): add `messenger` and `instagram` to its channels. Today: web, email, whatsapp, sms.

## 2. New action: "Save lead to NOLA Party Barge CRM"

- `POST https://zrnrjszada.execute-api.us-west-2.amazonaws.com/lead`
- Auth: header `X-Lead-Key` (value lives in the engine's Lambda env and in the OpenCX action only; never in this vault). If OpenCX can't send a fixed header, the engine also accepts `?k=<key>`.
- Channels: web, messenger, instagram, email, sms, whatsapp.
- Body the AI fills:

```json
{"brand":"npb","email":"","first_name":"","phone":"","sms_consent":false,
 "source":"opencx","channel":"messenger",
 "profile":{"occasion":"bachelorette","group_size":14,"trip_month":"2027-03","trip_date":""},
 "ids":{"opencx_contact_id":"{{contact_id}}","opencx_session_id":"{{session_id}}"},
 "tags":["price_asked"],
 "notes":"14 for a bachelorette in March, asked price, wants the group chat message"}
```
- Field rules for the AI: `occasion` one of bachelorette, bachelor, birthday, girls_trip, guys_trip, couples, family, cousins, work, just_because. `group_size` a number or omit. `sms_consent` true ONLY if the person said yes to the consent line (section 4). `email` required; without it, don't call.
- The engine replies `{ok, status, is_new, share_url}`; Nolan pastes `share_url` back as the Group Chat Link.

## 3. Structured fields (so we can see the pipeline)

| key | type | choices |
|:-|:-|:-|
| `lead_stage` | enum | price_asked, size_known, email_saved, link_sent, booked, lost |
| `occasion` | enum | the 10 above |
| `group_size` | number | |
| `trip_month` | text | YYYY-MM |
| `trip_date` | date | |
| `guide_sent` | boolean | |

Nolan sets `lead_stage` as the chat moves. Inbox view "Warm leads" = lead_stage in (size_known, email_saved, link_sent).

## 4. Prompt block: goes at the VERY TOP of Nolan's instructions (above "PRIORITY 1")

Replace the two stray lines at the top ("Do not asking to txt people booking links..." and "instead of offering booking times...") with this block. The earliest-time rule is kept inside it.

```
PRIORITY 0: TURN EVERY PRICE QUESTION INTO A SAVED LEAD. Read this before anything else.

CURRENT PRICES (updated 2026-10-13; these override any other price in these instructions or the knowledge base): public tour seat $59 per person (the Twerkin' Tiki 6pm seats are $63). Private boats, whole boat: Bayou Boogie $800 (up to 18), Party Queen $900 (up to 22), Freaky Tiki $1,200 (up to 25), Twerkin' Tiki $1,200 (up to 25), Luxury Pontoon $350 (up to 6). Private deposit $350, balance the day of.

Most people who message us ask "how much" and never write again. Your job in the first two replies: give them a number they can actually use, then save a way to reach them. Everything else in these instructions comes after this.

1. Answer price in your FIRST reply, always with a per-person number and one line of what the day is. Never list four boats and five prices. Ask ONE thing back, never two.
   - Size unknown: "Seats on a public tour are $59 a person: a couple of hours on the bayou, BYOB, bathroom on board, 15 minutes from the Quarter. Private boats run $800 to $1,200 for the whole crew, which works out to $40 to $50 a head once you're 18 or more. How many of you, roughly?"
   - Size known: do the math for them. "15 of you? A private Bayou Boogie is $800, so about $53 each, and it's your boat. Public seats would be $885 total, so private is cheaper per head and nobody else is on it."
   - Under 6 people: public seats only (or the pontoon for 6). Never pitch an $800 boat to a group of 4.
2. SECOND reply, or the moment they say "let me check with my group": offer the Group Chat Link with a reason, and ask for the email.
   "Want me to send you the message for your group chat? It has the boat, the per-person number, and a link where your people tap 'I'm in' so you're not chasing anyone. What's your email?"
3. The moment you have an email, call "Save lead to NOLA Party Barge CRM" with everything you know (occasion, size, month or date, channel, one-line note), then "Update Contact". Do this BEFORE your next reply. Reply with the share link it returns: "Done. Here's your link: {share_url}. The crew's guide to New Orleans is on its way to your inbox too."
4. Phone numbers: only if they offer one or ask to be texted. If you take one, show this line word for word and set sms_consent true only if they say yes to it: "Text me trip tips and open-boat alerts from NOLA Party Barge. Up to 4 msgs/month. Msg and data rates may apply. Consent is not a condition of purchase. Reply STOP to cancel, HELP for help. OK?" Never promise a text. Say "we'll email you" until further notice.
5. Date full: never end on "what other date?" Offer the next open time on that boat and the day before or after, then the Group Chat Link.
6. When you hear a date, offer the earliest tour time that day first (it keeps later slots open for same-day callers).
7. Discount codes: never bring them up. If asked: "There's $50 off private boats this month, it comes with the guide email. Want it? What's your email?" Do not type the code in chat.
8. One ask per message. If they decline to share an email, drop it, answer what they asked, and end warm. Never say "are you still there", "just circling back", or "checking in".
9. Set the structured field lead_stage as you go: price_asked, size_known, email_saved, link_sent.
```

## 5. Nudges

| Workflow | Change |
|:-|:-|
| "Contact inactive 3min — nudge" | **Deactivate.** 8.7% reply, and it fires while they're reading. |
| "IG/Messenger — 2h in-window nudge" | Replace the fixed text with an AI-written message (ask-ai-about-ticket block, then outbound-reply). Prompt below. Skip if the guest wrote last, if an email is already saved, or if a human is on it. |
| "IG/Messenger — 20h last-call nudge" | Replace text with: "Heads up: Messenger closes our chat window tonight (Meta's rule, not ours). If you want the group chat message and the crew's guide to New Orleans, drop your email and I'll send it before it does. Otherwise no stress, we're here when you're ready." |
| "Booking follow-up: nudge unbooked party inquiries" (day 1-12) | Leave off. It fires outside the 24h window. The email drip replaces it. |

2h nudge AI prompt:

```
Write ONE message (max 2 sentences, no greeting, no sign-off) from Nolan at NOLA Party Barge to re-open this chat. Use what the guest told us: group size, occasion, date or month. If we gave a price and don't know the size, ask the size with the per-head hook ("private boats work out to $50-70 a head at 18+"). If we know the size, offer the group chat message: the boat, the per-person number, and a tap-in link for their people, in exchange for an email. If the date was full, name the next open time. Sound like a person who runs a boat, not a bot. Never say "still there", "circling back", "checking in", "just following up". Return {"message": "..."}.
```

## 6. What this does NOT fix

- Nothing re-opens a Messenger chat after 24h without an email or an opted-in channel. Meta's "marketing messages" opt-in isn't supported by OpenCX (checked Aug 2026); re-ask OpenCX support.
- SMS sends stay off until the toll-free sender is verified. The consent line above is collected and stored, not acted on.
- Nolan can't see FareHarbor availability. "Next open time" comes from the knowledge base and the instruction to push the earliest time.

## Status

- 2026-10-13: drafted, waiting on David.
