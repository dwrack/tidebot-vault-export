# OpenCX DM Follow-ups — Redesign (Oct 2026)

*Built 2026-10-19 from live NPB OpenCX workflows. David's complaint: the bot's follow-ups after a guest answers our first question read as bot spam ("Are you still there?" 3 minutes later, "Still thinking it over?" 2 hours later).*

**CURRENT STATUS (verified 2026-10-19):**
- 3-minute "Are you still there?" nudge (`57746bc8`): **DEACTIVATED** 2026-10-19. It was a web-widget workflow from June 24 firing on every channel.
- 2h nudge (`93aff779`): **v2 ACTIVE** since 2026-10-19 21:30 (AI-written, context-aware). Canned v1 retired.
- 20h nudge (`76333efc`): **v3 ACTIVE** since 2026-10-19 21:45 (fun photo + 3 tap buttons). Text-only v2 retired. Activation hit a stuck 409 lock in the API; cleared after ~1 min of retries over REST.
- Only NPB has these nag workflows. NKST, DCKT, HPB, LSKT, BBK checked, nothing similar active.

## What a Messenger lead got before today
Ticket 1786, 2026-10-19: guest asked private barge price 17:38 → AI answered 17:38 → "Are you still there?" 17:41 → "Still thinking it over?" 19:38. Three bot messages, zero from him. Same on 1785 and 1787.

## The new sequence (inside the Meta 24h window)

| When | What | How |
|---|---|---|
| 0 | AI answers, asks one qualifying question | unchanged |
| +2h | ONE AI-written line that references what they said and offers something concrete (slot with seats, free hold, the answer they didn't get). Skips if their last message was a close or they booked/declined. | `ask-ai-about-ticket` → if `skip=false` → send |
| +20h | Fun boat photo + "no pitch" line + 3 buttons: Hold me a date / Text me open seats / Not this time | `outbound-reply-to-ticket` with attachment + quickReplySuggestions |

Hard cap: two touches per ticket, both inside the window. No "any more questions?" lines anywhere.

### 2h AI prompt (as saved)
Crew-member voice, under 25 words, must reference something specific they said, must offer one concrete useful thing, at most one exclamation mark. Banned: "just checking in", "still there", "still thinking", "let me know", "feel free", "happy to help", "any more questions", greetings, sign-offs.

### 20h copy (as saved)
> no pitch, this is just what last Saturday looked like out there. if you want I can pencil you in for a date, nothing to pay to hold it.

Photo: `Assets/Carousel Picks/npb-big-group-neon-wigs-costumes-party-boat.jpg` (uploaded to OpenCX storage `c85f6860`). Rotate the photo monthly so repeat lookers don't see the same shot.

## After the window closes: the "re-inspire" track David wants

Meta blocks any standard IG/Messenger send once the guest has been silent 24h. So spaced photo/reel touches need a channel we own. Three legit paths, in order:

1. **SMS (the "Text me open seats" button).** Guest taps → AI asks for a cell → number lands on the contact. Then a slow drip from the toll-free number: day 3 one photo, day 10 one reel link, then one new IG post link every ~2 weeks. Stop after 5 touches or on booking. This is the "super spaced reach-outs" channel. Needs a small cron workflow or a TideBot job once numbers start landing; copy to be drafted and approved first.
2. **Meta Marketing Messages opt-in** (strategy 5 in [[OpenCX Reengagement Strategies]]). Meta-native "get updates" button that re-opens the DM channel indefinitely. Ask OpenCX whether they support the opt-in template; if yes, add it to the 20h message in place of the SMS button.
3. **Comment-to-DM re-open** (strategy 8). Any reaction or comment on a new post re-opens that person's 24h window. Workflow on `contact-message-received`: if the contact has an old ghosted ticket, send one warm re-open with the post they just reacted to.

## Open items
- [x] David approved 2h + 20h drafts → both active 2026-10-19
- [ ] Test-fire the 20h draft on one internal Messenger thread to confirm the photo renders on IG and Messenger
- [x] Draft the SMS re-inspire drip copy (5 touches) for approval → [[NPB SMS Re-inspire Drip — Draft (Oct 2026)]] (2026-10-19, awaiting David). Note: the toll-free 888-618-9606 was rejected and released; the drip would send from the NPB main line 264-6046.
- [ ] Ask OpenCX about Marketing Messages opt-in support (outbound, needs David's OK)
- [ ] Re-measure reply rate on the 2h nudge after 14 days (baseline: canned line, see [[Why NPB Leads Ghost — OpenCX Data (Aug 2026)]])
