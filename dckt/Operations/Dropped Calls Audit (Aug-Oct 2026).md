# Dropped Calls Audit (Aug 24 - Oct 3, 2026)

Audited 2026-10-07. Read-only, nothing was called, texted or changed.

**Bottom line: 0 of 9 callers got any follow-up I could find.** 45 failed calls from 9 numbers, all to the OpenCX toll-free line (844-699-5219). No callback, text, email or OpenCX message went to any of them.

## Summary by caller

Times are Central. "Calls" = failed OpenCX phone sessions. Every one lasted 0-1 seconds and closed unresolved.

| Caller | Dates (CT) | Calls | Follow-up | Later booked | Still worth a text |
|---|---|---|---|---|---|
| ...9728 | Aug 24, 4:25pm | 2 | No | Unknown | No, 6 weeks stale |
| ...2222 | Aug 25 12:48-1:32pm, Aug 26 8:52-9:51am | 20 | No | Unknown | Check first. 20 dials in 2 days looks like a robodialer or a very determined person |
| ...6628 | Aug 27 11:53am, Aug 31 11:34-11:38am | 6 | No | Unknown | Maybe. Called back 4 days later, so real intent |
| ...9739 | Aug 27, 1:55pm (also hung up Jul 28) | 2 | No | Unknown | No |
| ...5221 | Sep 3 2:57pm, Sep 5 1:29pm, Oct 2 4:43pm, Oct 3 10:57am (also Jul 14) | 4 | No | Unknown | **Yes.** Kept trying for a month, latest Oct 3 |
| ...7175 | Sep 24 2:13pm, Oct 1 9:26am | 4 | No | Unknown | **Yes** (e-bike season) |
| ...9719 | Sep 24, 2:27pm | 1 | No | Unknown | Maybe |
| ...6700 | Oct 1, 12:23pm | 2 | No | Unknown | **Yes** (e-bike season) |
| ...9694 | Oct 1 1:53pm, Oct 2 1:02pm (also Jul 27, Aug 14) | 4 | No | Unknown | **Yes.** 4 tries since July, never got through |

Odd pattern worth a look before any outreach: 4 of the 9 numbers are San Antonio (210) and the 844 line was never meant to be public (memory note May 12: "do NOT publish until activated"). Somebody is finding that number, and it may be a listing tied to the wrong brand or a dialer.

## Where I checked for follow-up

| Source | Result |
|---|---|
| OpenCX sessions (all channels) for these 9 numbers | None outside the failed calls. No outbound messages, no SMS sessions, no comments |
| DCKT Gmail (doorcountykayaking@ + info@ forward), any format of each number, Aug 23 on | 0 hits |
| iMessage/SMS on this Mac | No conversations with any of the 9 numbers |
| Twilio outbound SMS/calls | **Couldn't check.** The 844 number lives in OpenCX's Twilio account (AC72106b...), not one we hold keys for. The local Twilio key is the NOLA account and gets 401. DCKT's own Twilio account (AC41c1d7cf..., owner info@) has no local credentials |
| GHL conversations | **Couldn't check.** Saved GHL token returns 401 "Invalid Private Integration token" |
| FareHarbor (later booked) | **Couldn't check.** No FH Public API keys exist on mbp-2 yet (`api-keys.json` missing). Bookings are a manual search in FH by phone |

So "no follow-up" is solid for OpenCX, Gmail and iMessage. A staffer could still have called back from a personal cell, which none of these would show.

## Full call list (OpenCX tickets)

| Ticket | Time (UTC) | Caller | Status |
|---|---|---|---|
| 318, 319 | Aug 24 21:25 | ...9728 | Call setup failed before agents could be rung |
| 320-329 | Aug 25 17:48-18:32 | ...2222 | Call setup failed |
| 330-335, 337-340 | Aug 26 13:52-14:51 | ...2222 | Call setup failed |
| 343-345 | Aug 27 16:53-16:54 | ...6628 | Call setup failed |
| 346, 347 | Aug 27 18:55 | ...9739 | Call setup failed |
| 350-352 | Aug 31 16:34-16:38 | ...6628 | "Incoming call from", then nothing |
| 357 | Sep 3 19:57 | ...5221 | Incoming, dropped |
| 358 | Sep 5 18:29 | ...5221 | Incoming, dropped |
| 367, 368 | Sep 24 19:13 | ...7175 | Incoming, dropped |
| 369 | Sep 24 19:27 | ...9719 | Incoming, dropped |
| 373, 374 | Oct 1 14:26 | ...7175 | Incoming, dropped |
| 375, 376 | Oct 1 17:23 | ...6700 | Incoming, dropped |
| 377, 378 | Oct 1 18:53 | ...9694 | Incoming, dropped |
| 380, 381 | Oct 2 18:02 | ...9694 | Incoming, dropped |
| 382 | Oct 2 21:43 | ...5221 | Incoming, dropped |
| 383 | Oct 3 15:57 | ...5221 | Incoming, dropped |

Full numbers are in OpenCX under these ticket numbers.

## The Oct 2 "won't go through" guest

Web chat #379, Oct 2 10:12am CT, asking about e-bikes for her 10-year-old at Cave Point. She said twice she couldn't call. Cedar told her to try 920-868-1400 and then asked for a name and number, which she never gave. The chat was auto-closed as "assumed resolved." No phone session hit OpenCX around that time, so she may have been dialing a different number. She's anonymous, so there's no way to reach her.

## Why the calls fail (diagnosis only, nothing changed)

- **The OpenCX workspace has no phone agent.** `list_phone_agents` returns empty, and the 844 number shows no assigned agent or IVR. Calls arrive from Twilio, find nothing to ring, and die.
- **When it broke:** the last working AI call was Aug 17 (#310, "Voice call with OpenCX Agent, 11s"). The first failure was Aug 24 at 4:25pm CT. So the agent was deleted or unbound between Aug 17 and Aug 24. From Aug 31, sessions stop even logging an error and just show "Incoming call from."
- **Who did it:** unknown. The OpenCX audit log has no phone-agent events at all. The only outside login is Cody Sharkey (FareHarbor partner access) on Sep 29 and Oct 2, which is after the break.
- **Separate line still works:** 920-868-1400 is taking voicemails and texts (a guest on Oct 1 left 2 voicemails and a text there about rescheduling). So it's only the 844 OpenCX number that's dead.
- **Fix path, when you're ready:** recreate or re-attach a phone agent to +1-844-699-5219 in OpenCX (Channels > Phone), or point the number at a forward to 920-868-1400. Then find where the 844 number is listed publicly.
