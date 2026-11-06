# OpenCX Lost-Customer Study — All Brands

Started 2026-10-30. Goal: find where OpenCX drops people who wanted to book, size it in dollars per brand, fix the top leaks, and re-measure every week so it stays fixed.

Brands on OpenCX: NPB+NBB (opencx-npb), NKST (opencx-nkst), DCKT (opencx-dckt), HPB+HBC (opencx-hpb), LSKT+AKT (opencx-lskt), BBK (opencx-bbk).

## What we already know (two prior pulls)

| Brand | Pulled | Headline leak |
|---|---|---|
| NPB | 2026-08-27, 60 days | 580 Messenger sessions, 97% ended with our message hanging. Only 125 contacts had a phone, 85 an email. Paying ~$2.83 per started conversation. Fixes shipped: 2h + 20h in-window nudges, email-capture ask, short-DM playbook (Nolan v2). Never re-measured since. |
| DCKT | 2026-10-07, full season (385) | Follow-up Router failed 294 of 294 runs (variable bug), Nudge workflow sent 317 messages and got 0 replies, phone path dead since Aug 24, bot looped asking guests for a UUID, 53% of handoffs were "missing tools". Human reply after handoff: median 20 hours. |

Source notes: `NOLA Party Barge/Marketing/OpenCX Reengagement Strategies.md`, `Door County Kayak Tours/Operations/OpenCX Season Review 2026.md`.

Nobody has looked at NKST, HPB, LSKT, or BBK. And the NPB fixes from Aug 28 have never been checked against data.

## NPB results (pulled 2026-10-31, read-only)

Two 61-day windows, before and after the Aug 28 fixes (2h/20h nudges, Nolan short-DM playbook, email-capture ask).

| | Pre-fix Jun 28 to Aug 27 | Post-fix Aug 28 to Oct 31 |
|---|---|---|
| Real sessions (noise removed) | 765 | 485 |
| Ghosted after our message | 438 (57%) | 277 (57%) |
| Handed off, no human reply | 50 (7%) | 40 (8%) |
| Converted or correctly closed | 261 (34%) | 168 (35%) |
| OpenCX's own "automation rate" | 92.6% | 91.5% |
| Leaked sessions with booking intent | 483 | 306 |
| Rough dollars left on the table ($180 AOV x 30% close) | ~$26k | ~$16.5k |

**The Aug 28 fixes did not move the ghost rate.** Same 57% before and after. Volume fell 37%, the leak rate did not.

What the post-fix transcripts actually show (277 ghosted, keyword cut plus a sample read):

1. **"How much?" then silence is the whole game.** 116 ghosts end on a price we quoted, 71 of those were a one-message "how much" ask. Nolan's reply is now good (one number, one question, short), but on Messenger the customer never answers the follow-up question. 99 of 277 ghosts sent exactly one message. The bot is answering well and still losing them, so the fix is not more prompt polish.
2. **Contact capture is broken at the record level.** 0 of 277 ghosted sessions have a phone or email on the contact record. Checked three sessions where the guest typed their phone and email in the chat (#1822, #1831, #1832): the OpenCX contact record still shows name, email and phone all empty. The "never end without a way to reach them" rule is being obeyed in the chat and lost in the database, which is why no SMS or email follow-up can ever happen.
3. **The nudges are still the old generic text.** 449 of 486 sessions got a workflow nudge. 411 of them got "Hi — just checking in. Are you still there?" (em dash and all) and 370 got "Still thinking it over?". The Oct 19 "AI-written context nudge" produced about 5 real context messages. 32% of nudged sessions did get a reply after the nudge, 14 ended confirmed resolved, so nudging works even when the copy is bad. Better copy is cheap upside.
4. **Every handoff goes to Jeffrey and dies.** All 40 post-fix no-reply handoffs are assigned to Jeffrey Chitek via the "support" team (least-busy, one member). Several are same-week money: #1822 private boat for 10 on Oct 31 (Aditya, 774-502-4433, asked for a discount and a 3pm slot, waited 6 days), #1849 "trying to book for tomorrow" this morning, #1832 ten people who gave an email for a quote on Oct 27 and never got it. The bot's "I'll email you the quote" promise hands off to a human and the email is never sent.
5. **Email into OpenCX died Aug 5.** 93 email sessions pre-fix, zero since 2026-08-05. Same failure shape as DCKT's Jul 23 email stop. Unverified why; check the forward from the NPB inbox.
6. **Big groups (12+) are 22 of the ghosts** and get told "two boats" with no human pick-up. These are the $1,000+ conversations.
7. Instagram is now small (34 sessions post-fix, 21 closed fine). Web chat handoffs are the worst ratio: 10 of 31 web sessions handed off with no reply.

Full per-session tables: `NOLA Party Barge/_Study Output/npb-opencx-study-2026-10-31.md` (post-fix) and `npb-opencx-study-2026-08-27.md` (pre-fix).

### Update 2026-10-31 afternoon (David's direction + deeper read)

David: don't reroute handoffs, remove the reasons for them; the bot sends the quote email itself; Slack stays. Fix plan with approve boxes: `NOLA Party Barge/OpenCX Fix Plan — Fewer Handoffs, Real Follow-Up (Nov 2026).md`.

New facts from the live config:
- Nudge reply rate: canned nudges 34% (139 of 404, Aug 28 to Oct 18); AI-written 2h nudge live since Oct 19 is 9% (4 of 43). The AI lines don't ask anything.
- 11 sessions hit a FareHarbor availability-validation failure (lists slots, then says gone). 8 became handoffs. Tool bug.
- Global profile says "collect name, phone, email before handing off" and "if you don't know, hand off"; a scenario says "never collect phone numbers"; the contact-save scenario calls an action disabled 10/27. Those three contradictions explain most no-answer handoffs and the empty contact records.
- Sending domain nolapartybarges.com is verified in OpenCX; send-email-template and update-contact workflow actions exist. The quote email is buildable today.
- 4 handoffs were OpenCX crashes ("unexpected error, handing off as fallback").

### Fixes, ranked by dollars per hour of work

1. **Handoff owner + 2-hour SLA.** Route the support team to whoever actually answers (Michael or David during the Jeff transition), Slack DM on every handoff, and a daily "open handoffs older than 2h" ping. Also answer #1822, #1849, #1832 today.
2. **Make the quote-by-email actually send.** Either give the AI a native email send (domain verify in OpenCX, like DCKT's) or drop the promise and give the FareHarbor link plus "text us at ..." instead. Promising and not delivering is worse than not asking.
3. **Fix contact persistence.** Find out why typed phone/email never lands on the record (tool error, missing action, or the instruction never calls it). Until it works, the 24-hour Meta window is the only shot we get.
4. **Rewrite the two nudges.** Kill "Hi — just checking in." Replace with a context line from the conversation plus one concrete offer (hold a date, send photos, locals price), no em dashes, no question mark at the end of both.
5. **Restore the email channel** (verify the inbox forward) and add a 12+ group rule: any group 12 or more pings a human immediately with the thread summary.

Then re-run `opencx-study-pull.py npb --days 14` two weeks after each change. Target: ghost rate under 45% by end of November.

## The six leak types (classify every session into one)

1. **Ghosted after our message.** Customer asked something, we answered, they never came back. Biggest bucket by count. Sub-tag the drop reason: price shock, date unavailable, group logistics, rate-card dump, just browsing.
2. **Handed off, no human reply.** AI gave up, nobody answered inside the SLA. Pure staff leak, highest dollar per session.
3. **Wrong or bad answer.** Bot said something false (UUID loop, "we don't process refunds", garbled age rule) and the customer left.
4. **Dead channel.** Phone call that never rang anyone, SMS that could not send, email loop with another bot.
5. **Follow-up never fired.** A workflow was supposed to nudge and did not (DCKT Router), or fired after the Meta 24h window closed (NPB old Day 1 / Day 3).
6. **Converted or correctly closed.** Booking link clicked or booking confirmed in the thread, or a real answer to a non-sales question. Not a leak.

Anything that is spam, vendor pitch, or internal mail gets tagged `noise` and excluded from the denominator.

## How we measure

Script: `TheBrain/Scripts/opencx-study-pull.py`. One brand per run, read-only.

- Pulls every session in the window (`GET /chat/sessions` with pagination) plus full history per session (`/history`), the impact report, and handoff analytics.
- Caches raw JSON under `~/.cache/opencx-study/<brand>/` so re-runs and re-reads are free.
- Auto-classifies with simple rules: who spoke last, whether a human agent ever replied after handoff, whether a FareHarbor link or booking confirmation appears, phone call empty, etc. Prints a scoreboard by channel and writes `_Study Output/<brand>-<date>.md` into the brand's vault with the per-session table for a manual read.
- Dollar estimate: leaked sessions with booking intent x brand average order value x 30% close rate. Same formula every brand so the numbers compare.

Then a human (me, on Opus) reads the ghosted and handed-off transcripts and tags the drop reason. That read is where the fixes come from. The rules only sort the pile.

## Rollout order

| Order | Brand | Why | Window |
|---|---|---|---|
| 1 | NPB | Highest volume, paid traffic feeding it, fixes shipped Aug 28 that nobody re-measured | Aug 28 to Oct 30 (post-fix), compared with Jun 28 to Aug 27 (pre-fix) |
| 2 | NKST | Second NOLA brand, year-round, same team as NPB so fixes transfer | Last 90 days |
| 3 | HPB + HBC | Houston season | Last 90 days |
| 4 | LSKT + AKT, BBK | Texas | Last 90 days |
| 5 | DCKT | Already done 10/07. Re-run in April before the season as the regression check | Apr 2027 |

## Weekly loop once baselines exist

- Monday: run the pull for each brand for the prior 7 days. Post one line per brand: sessions, leak rate, handed-off-with-no-reply count, estimated dollars leaked.
- Any session in bucket 2 older than 2 hours during business hours goes to the brand manager's phone as a Slack DM, not a channel.
- Tag every workflow change in OpenCX with a date so the next pull can read before and after.
- Matches against FareHarbor by name or email monthly so "converted" stops being a guess.

This is the "watcher for OpenCX for each business" from the Oct 14 Apple Note.

## Blocked right now (2026-10-30)

- **Decision 2026-10-30 (David):** NPB first. Create a dedicated OpenCX API key per brand (Settings > Access) with read + write scopes: chat-sessions, contacts, tags, insights, handoff-analytics, impact-report, workflows. Store at `~/.config/opencx/<brand>.key` on dckt-guide-mac via `TheBrain/Scripts/Set OpenCX Key.command` (hidden prompt, local-only). Write scope is for fixing follow-up workflows and tagging sessions later; nothing live changes without David's OK.
- **2026-10-31 status:** David created NPB key "claudia 2" in platform.open.cx at 7:50am PT but it was never delivered to this Mac (shown once, not recoverable). Tried to create one from this Mac's signed-in Chrome: Google forced a password challenge and the only account here is the DCKT Google, not the NPB admin (dwrack81@gmail.com). Next: create a new key on wavey and run `TheBrain/Scripts/Set OpenCX Key.command` there (it pushes the key here), then revoke claudia 2.
- **UNBLOCKED 2026-10-31 9:10am PT:** all six brand keys now at `~/.config/opencx/<brand>.key` on dckt-guide-mac (pushed from wavey by the installer). API verified. Note: api.open.cx sits behind Cloudflare and 403s the bare python-urllib agent (error 1010); the script identifies itself as `opencx-study-pull/1.0`. This session is on dckt-guide-mac (user doorcountykayaktours). The opencx-* servers and keys live on wavey and davids-mbp-2 in `~/.claude.json`, and SSH from here to mbp-2 is not authorized. The script is written to run on either of those Macs unchanged.
- Toll-free SMS verification (888-618-9606) still pending per FareHarbor ticket #5796065, so every SMS-based recovery idea is parked.
- CSAT is off on every brand. No satisfaction signal exists anywhere.

## Fixes already queued from prior reads (do not re-discover)

- NPB: Messenger Marketing Messages opt-in (blocked on Meta page config), click-to-Messenger retarget audience, comment-to-DM re-trigger job on mbp-2, add Instagram to the Nolan short-DM instruction (71 sessions, 89% ghost, currently excluded).
- DCKT: fix the Router variable (`ticketNumber`), delete Nudge, real booking lookup by confirmation code, split internal mail out of the bot inbox, refund/complaint protocol, turn CSAT on.
- All brands: the 24h Meta window means every Messenger and IG conversation must end with a cell, an email, or an opt-in. Audit each brand's prompt for that rule.
