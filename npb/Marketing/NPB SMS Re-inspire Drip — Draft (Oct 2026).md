# NPB SMS Re-inspire Drip — Draft (Oct 2026)

*Drafted 2026-10-19. Nothing here sends or is scheduled. Follows [[OpenCX DM Follow-ups — Redesign (Oct 2026)]] (the "Text me open seats" button on the 20h nudge) and sits beside [[NPB Lead Capture + Drip Plan (Oct 2026)]] (the email Countdown). This is the SMS lane for DM leads only.*

**STATUS: DRAFT, awaiting David's approval of the copy and the sender number.**

## What this is

A guest DMs us on IG or Messenger, asks a price, goes quiet. 20h later the bot sends the fun photo with three buttons. If they tap **Text me open seats**, the AI collects a cell with proper consent, and this drip takes over once Meta's 24h window has shut us out. Five texts over about seven weeks, each one carrying something worth looking at (a photo, a reel, a new post), never a "just checking in". Stops the moment they book, reply STOP, reply at all, or the five are done.

## 1. Sender number and compliance (verified 2026-10-19)

| Item | State |
|---|---|
| Number NPB texts from today | **+1 (504) 264-6046**, "NPB main", local 10DLC, SMS/MMS capable, inbound relays to the NPB phone via the `npb-sms-relay` Twilio Function. Live check 2026-10-19 via Twilio API. |
| Toll-free 888-618-9606 | **Gone.** Verification rejected and the number released (per [[../TheBrain/07 Reference/Twilio Account Audit (Sept 24 2026)]] and memory). The Redesign note's "toll-free" wording is stale. |
| A2P 10DLC (Twilio side) | Brand APPROVED. "Low Volume Mixed" campaign VERIFIED and holds all 11 live locals including 264-6046. The separate "Marketing A2P" campaign FAILED. State as of 2026-09-24 audit; re-confirm in the Twilio console before launch. |
| Is 264-6046 cleared for marketing SMS? | **Yes with a condition.** Low Volume Mixed covers marketing content as long as the registered opt-in matches reality. Before the first send, check the campaign's declared opt-in text in the console and, if it only lists booking form / waiver / contact form (like the May filing in [[A2P 10DLC Verification — NOLA Party Barge]]), add "direct inquiry via Instagram or Messenger where the guest requests texts" so the DM capture is on record. |
| OpenCX's own number | +1 (888) 403-7303 is verified in OpenCX (since 2026-05-02) but the May 10DLC filing through Mo at OpenCX was never confirmed and the SMS channel has had zero traffic. Treat it as not cleared for marketing until OpenCX confirms in writing. |

TCPA / CTIA rules this drip has to meet, and how each is met:

- **Prior express written consent** for marketing texts: the guest taps the button, then types their number after reading the disclosure (section 2). The tap alone is not consent. We record timestamp, channel, ticket, and the wording version.
- **Identify the sender** in every message: every text starts "NOLA Party Barge:".
- **Frequency disclosed and honored:** "a few over the next 2 months, 5 max." Five touches, hard cap.
- **STOP in every message**, HELP in the confirmation. Twilio honors STOP/UNSUBSCRIBE/CANCEL/END/QUIT on the number automatically and blocks further sends; the job also writes the suppression so no other NPB send ever reaches them.
- **"Msg & data rates may apply"** in the confirmation text.
- **Quiet hours:** sends only 11:00 to 19:00 America/Chicago, never before noon on Sunday.
- **Hosted unsubscribe, no reply-to-unsubscribe email:** STOP is the SMS-native hosted opt-out. No mailto anywhere.

## 2. How the number gets collected (OpenCX side)

**Where it lands.** OpenCX contacts have a top-level `phone_number` plus free-form `custom_data` (verified) and `non_verified_custom_data`. No structured fields exist on NPB yet (checked 2026-10-19). The workflow definitions include `Extract Contact Info` (with `extractPhone`), `Update Contact`, `merge-contact-custom-data`, `Contact Message Received`, `Cron Trigger`, `Wait`, and Sequences.

**Keying the drip.** A contact is eligible when ALL of these are true:
- `phone_number` is set (E.164)
- `custom_data.sms_opt_in_at` is set (ISO timestamp)
- `custom_data.sms_drip_status` is empty or `enrolled` (not `stopped`, `booked`, `done`, `human`)
- no FareHarbor booking matches the phone or the contact name since the DM

**Fields the capture workflow writes to the contact**

| Field | Value |
|---|---|
| `phone_number` | E.164, from Extract Contact Info |
| `custom_data.sms_opt_in_at` | ISO timestamp of the message containing the number |
| `custom_data.sms_opt_in_source` | `ig-20h-button` or `messenger-20h-button` |
| `custom_data.sms_opt_in_ticket` | ticket number |
| `custom_data.sms_opt_in_wording` | `v1` (the disclosure text below, versioned so a later edit can be told apart) |
| `custom_data.sms_drip_status` | `enrolled` |
| `custom_data.sms_drip_step` | `0` |

**Trigger.** The 20h button is a plain quick reply, so the tap arrives as the guest's message "Text me open seats". A `Contact Message Received` workflow on IG/Messenger matching that exact text (or an AI classifier for "text me" / "send me texts") runs the ask below. The AI handles the back-and-forth; the workflow runs Extract Contact Info on the reply and writes the fields.

**What the AI says (add to the Nolan DM/text instruction `90c4b364`, scoped to instagram + messenger):**

> When the guest taps or says "Text me open seats", reply in one message, nothing else:
> "what's a good cell? I'll text you when seats open up plus the occasional boat photo, a few times over the next couple months, 5 max. msg & data rates may apply, reply STOP any time."
> When they send a number, confirm in one line ("got it, you'll hear from me when something opens up") and do not ask anything else. If they send something that is not a number, ask once more, then drop it. Never promise a date or a price in this exchange.

The confirmation text (T0 below) then goes out from 264-6046 within a minute, so the guest sees the number that will be texting them while the DM is still open. T0 is the consent receipt and does not count toward the five.

## 3. The five touches (verbatim)

All under 160 characters, no em dashes, one link each, brand first, STOP last. Days count from `sms_opt_in_at`. The `ref=` values are what we match in FareHarbor's referral report (same pattern as the barge auto-text, no UTMs).

**T0, immediately on capture (consent receipt, not one of the five)**
NOLA Party Barge: you asked for open seat texts. a few over the next 2 months, 5 max. reply STOP to opt out, HELP for help. msg & data rates may apply

**T1, day 3, MMS with photo `Assets/Carousel Picks/npb-friends-arms-up-party-boat-sunset.jpg`** (different shot from the 20h neon-wigs photo so they do not see the same image twice; rotate monthly from Carousel Picks)
NOLA Party Barge: no pitch, this was sunday's sunset run. if a weekend opens up for your crew, seats are here: nolapartybarges.com/?ref=sms-d1  STOP to opt out

**T2, day 10, reel link** (IG Library: `2026-05-10_1393L_new-orleans-is-a-magical-place`, 1,393 likes, the cleanest high performer of 2026; alternate is `2026-05-16_3738L_warm-air-gentle-breeze` at 3,738 likes but the caption is cruder than a first text should be)
NOLA Party Barge: the reel people send their group chat: instagram.com/reel/DYLEllDRyaC  halloween and holiday weekends are filling up. STOP to opt out

**T3, day 24, newest reel on the feed at send time** (the job pulls the latest VIDEO post from the IG Graph API and swaps the link in; fallback if nothing new in 14 days: `2026-07-16_0085L_have-you-ever-seen-the-lake-borgne-surg`, the Great Wall of Louisiana reel, shown below)
NOLA Party Barge: new one from the bayou this week: instagram.com/reel/Da3LE75RwkX  7 miles from the quarter, 15 min uber, nobody pedals. STOP to opt out

**T4, day 38, newest carousel or photo post, seasonal if there is one** (fallback: the staged `halloween-weekend-new-orleans-locals-plan` or `thanksgiving-family-in-town-bayou-afternoon` carousel from `Marketing/Carousels - Staged`, whichever is live; the `instagram.com/p/XXXXXXXXXXX` below is the placeholder the job fills)
NOLA Party Barge: instagram.com/p/XXXXXXXXXXX  if your people come for the holidays, the private boats go first. want one held? just reply. STOP to opt out

**T5, day 52, the warm exit, newest post at send time** (fallback shown: `2026-08-26_0086L_get-on-a-boat-and-do-whatever-ya-like`, the "weekends fill up quick" reel)
NOLA Party Barge: last one from me, promise: instagram.com/reel/Dcgf4l2RxNv  if the trip's still on, reply with a date and I'll handle it. STOP to opt out

Rules across all five:
- One message per touch, no stacking, no retries on a failed send (log it, move on).
- A reply of any kind pauses the drip and relays to the NPB phone through the existing SMS relay; a human (or Nolan on the SMS channel, once OpenCX's number is cleared) takes it from there.
- If T4 lands inside the week before a holiday (Halloween, Thanksgiving, NYE), the holiday word in the text is swapped to match.
- Photos are originals, not web-optimized (MMS re-encodes anyway).

## 4. Mechanism: where the drip runs

**Pick: a job on davids-mbp-2 (TideBot family, launchd, every 15 minutes), with OpenCX as the capture point only.**

Why not an OpenCX cron workflow:
- OpenCX can only text from its own number, 888-403-7303, and that number is not confirmed for marketing SMS. 264-6046 is the number that is verified today, and it is Twilio-side, so only our job can send from it.
- The booking stop condition needs FareHarbor data. The daily FH update pipeline already lands on mbp-2; OpenCX has no FareHarbor lookup.
- The STOP suppression list and the Twilio creds (`~/.config/twilio/sms.env`) already live on mbp-2. One suppression list, one sender, one place to audit.
- OpenCX stays useful for what it is good at: the DM conversation, the number capture, and the contact record the job reads.

Keep OpenCX Cron Trigger + Sequences as the fallback plan if OpenCX confirms 888-403-7303 for marketing and David would rather the whole thing live in one tool.

**How the job works**
1. Every 15 min, pull OpenCX contacts updated since the last run (`list_contacts`), keep the eligible ones (section 2).
2. For each, compute the next touch from `sms_drip_step` and `sms_opt_in_at`. If it is due and inside the send window, send via Twilio from +15042646046 (MMS for T1, SMS otherwise), then write `sms_drip_step`, `sms_drip_last_sent` back to the contact and append to a local JSONL log.
3. Before every send, run the stop checks below. Any hit flips `sms_drip_status` and the contact is never touched again.
4. Daily at 09:00 CT, post a one-line count to the usual Slack channel only if something changed (sends, stops, bookings), per the change-gated rule.

**Stop conditions (checked before every send)**
| Stop | How it is detected | Status written |
|---|---|---|
| Booked in FareHarbor | phone (E.164) or exact contact name appears in the daily FH booking export dated after `sms_opt_in_at` | `booked` |
| STOP or any opt-out keyword | Twilio inbound webhook on 264-6046 (the relay already sees every inbound); also Twilio's own opt-out block | `stopped`, phone added to the shared suppression file |
| Any other reply | same inbound hook; relay forwards it to the NPB phone, drip pauses | `human` |
| 5 touches sent | `sms_drip_step` == 5 | `done` |
| Human takeover in OpenCX | ticket assigned to a person or `Not this time` tapped later | `human` / `stopped` |
| Send error (30006 landline, 30005 unknown) | Twilio error code on send | `stopped` |

Volume guard: never more than 50 drip sends per day across all steps, so a backlog can never blast like the August 1,703 incident.

## 5. Measurement

- FareHarbor referral report, filter `ref=sms-d1` through `sms-d5`, weekly.
- Per touch: sends, STOPs, replies, bookings. Kill any touch at zero replies and zero bookings after 6 weeks of data.
- Opt-in rate on the 20h button: contacts with `sms_opt_in_at` / tickets where the 20h nudge fired.

## 6. Decisions and open items

**The one decision for David:** send from the NPB main line 264-6046 now (recommended), or hold the drip until OpenCX confirms 888-403-7303 for marketing SMS and run it inside OpenCX instead.

Open before anything sends:
- [ ] David approves the six texts above (or edits)
- [ ] Twilio console: confirm Low Volume Mixed is still verified and its opt-in description mentions DM capture
- [ ] Add the capture lines to the Nolan instruction `90c4b364` and build the `Contact Message Received` workflow (write fields, no send)
- [ ] Build the mbp-2 job (reads OpenCX, sends via Twilio, FH stop check, suppression), test on David's cell end to end, STOP included
- [ ] Rotate T1 photo and the T2 reel monthly; the job reads the choice from a small config so no code edit is needed
