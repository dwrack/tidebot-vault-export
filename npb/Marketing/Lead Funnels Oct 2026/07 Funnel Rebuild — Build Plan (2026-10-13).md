# Funnel Rebuild: cold lead to warm lead to booking (2026-10-13)

*Written 2026-10-13 by David's Claude after a live audit of the site, GA4, the lead engine and OpenCX. Build in progress. Nothing here is live until David says go. Supersedes nothing: it wires together 00-06 in this folder and the Sept 30 plan.*

## What the audit found (all verified 2026-10-13)

| Piece | State |
|:-|:-|
| Paid + organic social, last 30 days | 18,147 sessions, 15 purchases (0.08%). Cold traffic leaves with no email |
| Site banner "Get early access" | Still the dead GHL form titled "Nola Pedal Barge" |
| Lead engine (popup + drip) | Live for Houston only. NPB `enabled: false`, no code, $25 not $50, generic copy |
| OpenCX, last 60 days | 492 chats, 87% Messenger. About 249 asked price or availability. **0 emails saved** |
| OpenCX "Update Contact" action | Enabled on web, email, WhatsApp, SMS only. **Not on Messenger or Instagram** (93% of chats). Even a volunteered email is dropped |
| OpenCX nudges | 3-min "still there?" (8.7% reply), 2h and 20h generic. The day 1/3/5/7/12 drip sent 1,703 messages and got 0 replies, off since 9/1 |
| SMS | Consent can be collected now. Nothing can be texted until a new toll-free sender is verified (old one rejected 6/29, number released 9/24) |
| Win-back email | 33k sends a week, 41 GA4 sessions, 0 purchases in 30 days. Links need UTMs |
| **Prices Nolan quotes** | Wrong and high. Live FareHarbor (API, 10/13): seats $59 (Twerkin' 6pm $63), Bayou Boogie $800, Party Queen $900, Freaky/Twerkin' Tiki $1,200, pontoon $350. Nolan's prompt says $63 / $900 / $1,100 / $1,250. Fixed in the 09 prompt block; the knowledge base needs the same edit |

## The design

**Headline magnet: The Crew's Guide to New Orleans.** A curated, trip-timed guide written by the crew, not a PDF. Delivered as the NOLA Countdown drip (12 chapters, each a page on our site, Crew's Picks from the Sept 30 spots research). The $50 code, if David keeps it, lives in the P.S. only. Never the headline.

**Front door on pricing pages and in the bot: The Group Chat Link.** Three taps (how many, what are we celebrating, roughly when) show the right boat and the per-person price before we ask for anything. Then: "Want me to save this and send the message for your group chat? Drop your email." They get a shareable page where friends tap "I'm in" and the split updates live. Solves the planner's real problem (herding people and money), adds group proof, and starts the guide.

**Why this and not a discount:** 80% of chats open with "how much" and no date. Planners go cold at the moment they have to go sell it to their group. A code doesn't help with that. A paste-ready message and a tap-in page do.

**Chat-dropper play (OpenCX, inside the 24h window):** price answer always includes the per-person number and one line of what the day is like, then one ask with a reason: the Group Chat Link by email. No soft holds (David, 10/13). The 3-min nudge goes away. The 2h and 20h nudges reference their group size and date and offer the link.

**Identity ("fingerprints"):** one lead record per person, stitched across email, phone, Messenger PSID, Instagram ID, OpenCX contact, GA client id, Meta `_fbp`/`_fbc`, and later the FareHarbor booking. Lets us: stop nudging people who booked, fire Meta Lead events for better ad optimization, and see which door produced which booking. No third-party visitor de-anonymization vendors (consumer privacy risk, not worth it).

**SMS:** the form collects a separate, unchecked, TCPA-grade consent with the full disclosure and stores text version, time, IP and source. Sending stays off until the toll-free refile clears. The consent page doubles as the proof Twilio asked for.

## Personas the copy is written for (from 38 real chats + research, 10/13)

| Persona | Private fear | What moves them |
|:-|:-|:-|
| Bachelorette MOH | Picking the dud activity | Per-person price + the paste-ready group message |
| Birthday organizer | Chasing friends for money | Split shown up front, friends tap in |
| Cousin/family planner | Group never agrees | A page the family can tap |
| Same-day tourist | "No availability" dead end | Next open slot, offered, not asked |
| Office planner | Looking unprepared | Forwardable one-pager with headcount math |

## Build list

| # | Piece | Where | Owner | Status 10/13 |
|:-|:-|:-|:-|:-|
| 1 | Engine v2: `/lead` auth + rate limit, identity fields, phone index, merge rule, consent record, `/plan` tool + share page, answer-tap links, trip-date scheduling, NPB brand block, Meta CAPI Lead, STOP webhook, tests | `~/Projects/fh-lead-engine-capture` (branch `capture-v2`), not deployed | Claude | building |
| 2 | The Crew's Guide: 12 chapters + occasion variants, Crew's Map, group-chat paste templates, share-page copy | this folder, `08 The Crew's Guide — Copy.md` + JSON for the engine | Claude, David approves | drafting |
| 3 | OpenCX: new "Save lead" action (all channels), fix Update Contact channels, structured fields (trip date, group size, occasion, stage), instruction block at top of Nolan's prompt, rewrite 2h + 20h nudges, retire 3-min | OpenCX, after David approves copy | Claude | drafting, see `09 OpenCX — Capture Play.md` |
| 4 | Site: banner to the Group Chat Link, popup script line in header, `/plan/` and `/guide/` pages (iframe to engine), privacy policy SMS lines | WordPress (wp-admin) | David/Michael paste, Claude preps | pending #1 |
| 5 | FareHarbor: create CREW50-NOV (exp 11/30) and CREW50-DEC (exp 12/31), private boats only, test $50 off total not deposit, check the usage-cap setting | FareHarbor dashboard | David | pending decision |
| 6 | Win-back email links get UTMs | mbp-2 runner | Claude | quick, separate |
| 7 | Crew milestone rewards on the "I'm in" page (David, 10/13): 6 taps unlock the Crew's Map, 12 unlock a free crew photo + captain's shoutout, 18 bump $50 to $100 off. Personal referral link per lead; referred signups count as taps. Rate-limited, deduped | engine `capture-v2` + guide copy | Claude | added to both builds |
| 8 | Lifted from marclou/mailcheap (SES newsletter tool, same stack as our engine): SES bounce/complaint webhook + shared suppression list; auto-pause a brand at >2% bounces or >0.08% complaints; pre-send checks (unsub link, postal address, <100 KB); guide chapters as public web pages with share images; dormant-reader cleanup on the 33k win-back list (one "still want this?" email, then stop) | engine `capture-v2` (webhook, pause, checks, archive); win-back runner on mbp-2 (cleanup, UTMs, send-in-steps) | Claude | engine parts in build; win-back parts queued |

## Decisions for David

1. Keep the $50 code as a P.S. with expiry, or drop money entirely and let the guide carry it? My call: keep it in the P.S. only, per-door codes so FareHarbor's promo report shows which door books.
2. Public name of the guide: "The Crew's Guide to New Orleans" (my pick) or keep "The NOLA Countdown".
3. Who signs the emails (a crew first name with their OK, else "the crew at NOLA Party Barge").
4. FareHarbor codes: I could not verify the campaign settings (help articles are login-only). What I expect: flat amount, item restriction, valid date range, and a total-uses cap. No per-person unique codes and no API to create them. If the cap exists, set it (e.g. 100 uses) so a leaked code can't run away. Verify in Dashboard > Campaigns when creating CREW50-NOV.

## Order of operations

1. Engine v2 passes tests and David clicks through `/plan` on a test URL.
2. David approves guide copy (chapters 1, 1b, 2 first; the rest can land over two weeks since the drip is timed).
3. OpenCX copy approved, then: action + fields + prompt block + nudges go live. Same day: Update Contact channel fix.
4. FareHarbor codes created and tested.
5. Flip `npb.enabled = true`, deploy, paste the script line and banner link. Kill the GHL form.
6. Week 1 readout: signups by source, taps, Messenger emails saved, bookings by code.
