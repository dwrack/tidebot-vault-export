# Lead Funnels (Oct 2026): start here

*Written 2026-10-08 by David's Claude. Everything in this folder is a draft. Nothing is sent, posted, published, committed, or deployed. It builds on `Marketing/NPB Lead Capture + Drip Plan (Oct 2026).md` (the NOLA Countdown) and the lead engine at `~/Projects/fh-lead-engine`.*

## What this is

A survey contest funnel as a new front door into the lead engine: an organic post asks "What do you love most about New Orleans?", five taps and an email enter people in a monthly drawing for a free private tiki boat, and their answers drive a branching warm-up drip. Plus the lead magnet plan and a ranked menu of the other funnel variations.

| File | What it is | Read it when |
|:-|:-|:-|
| **01 Blueprint** | The design: survey, tags, contest mechanics with dates, the 18-email map, the block library, three worked entrants, suppression, hand-offs, build list, metrics, 14 decisions | First. It is the spec everything else follows |
| **02 Emails** | All 23 emails written out, three fully rendered samples, 17 block families (158 versions), the tap questions and small pages, the open [VERIFY] list | Approving copy |
| **03 Rules + Compliance** | Draft Official Rules, compliance checklist with sources, paste-ready disclosures, winner handling, 6 questions for counsel | Before the lawyer call |
| **04 Posts + Survey Page** | The survey page copy, 5 launch post concepts for Facebook, Instagram and TikTok with disclosures baked in, comment and DM replies, link plan, two-week calendar | Approving posts |
| **05 Lead Magnet Plan** | 11 magnets ranked, the 3 to build first, which goes on which page, how each one tags the lead | Planning the next door |
| **06 Funnel Variations** | 12 lead funnels ranked by bookings per hour of work, top 5 specced, launch order Oct 2026 to Feb 2027, what not to do | Planning the quarter |
| `previews/survey-prototype.html` | Clickable survey, demo mode, phone sized. Open it in a browser | Feeling the survey |
| `previews/emails/index.html` | 31 emails rendered by the real engine for Kayla, Marcus and Dee, day by day | Seeing the branching |

## Three things that block launch

1. **A lawyer reads 03.** Six questions in its section 6, plus the sponsor's legal entity name. Counsel also decides whether unsubscribed entrants stay in the drawing and whether mail-in cards must arrive by the close.
2. **Prize terms.** The default is one private tiki charter, winner plus up to 24 guests, $0 to the winner, Sunday through Thursday, blackouts Nov 25 to 29, Dec 31 to Jan 1, Feb 5 to 9, ask 14 days ahead, ride within 6 months. Say yes or change it.
3. **The survey page itself.** The engine branch serves the confirm and tap pages, but the survey, result and rules pages are not built yet (the prototype is a static demo). Also not done: the `/win` redirects on the site, `BAYOU50-NOV` and `BAYOU50-DEC` in FareHarbor, and the Countdown going live.

## Dates (all CT)

| | Round 1 (November) | Round 2 (December) |
|:-|:-|:-|
| Go or no-go | **Mon Oct 19** | |
| Entries open | Thu Oct 22 (quiet). Launch post **Sat Oct 24, 4pm** | Mon Nov 16 |
| Entries close | Sun Nov 15, 11:59pm | Sun Dec 13, 11:59pm |
| Draw | **Mon Nov 16, noon** | Mon Dec 14, noon |
| $50 code dies | Mon Nov 30 | Thu Dec 31 |

Nothing contest-related sends on a Tuesday (the past-guest emails go Oct 27 and Nov 17).

## Decisions, with my call

| # | Decision | My call |
|:-|:-|:-|
| 1 | Go on Oct 19 if 2 and 3 above land | Go |
| 2 | Lawyer, CPA (no 1099 under $2,000 in 2026, confirm), sponsor entity name | All three, now |
| 3 | Prize terms as listed above | Adopt |
| 4 | Confirm-to-enter, 5 entries max, no referral entries (Meta bans rewarding people for publicizing a promotion), 5-day winner reply, $50 held until the draw with early release for hot leads and next-30-days riders, pontoon out of the code | Yes to all |
| 5 | Contest-only codes `BAYOU50-NOV` and `BAYOU50-DEC` next to the popup's `CREW50` codes. Private boats only, test that $50 comes off the total not the deposit | Yes |
| 6 | Who signs the emails | A crew member's first name with their OK. Until then "The crew at NOLA Party Barge" |
| 7 | Film the winner's ride | Ask, never require |
| 8 | Site: the "Win a Trip!" nav item goes to the survey and gets relabeled "Win a Boat Ride" (the prize includes no travel); old giveaway URL 301s to the survey; top banner stays with the Countdown | Yes |
| 9 | Locals list sends first dibs on open boats only, 2 a month max, no new discount | Yes |
| 10 | TikTok in round 1 | Skip unless the account is clean |
| 11 | Someone already in the contest hits the $50 popup before the draw | Refuse it. One live code per person |
| 12 | Not blocking: crew photo roles (captain shoots, deckhand uploads), holiday one-pager out by Oct 17 or parked, gift cards, referral sender reward (thank-you only) | See 05 and 06 |

## Build status (2026-10-08)

Engine work is on a separate copy, never the live checkout: `~/Projects/fh-lead-engine-survey`, branch `survey-contest`, uncommitted, 106 tests passing, not deployed. The live Houston flow has its own regression tests there and still passes. Read `BUILD-NOTES.md` in that folder before touching it.

| Done | Not done |
|:-|:-|
| Survey capture (5 answers, 21+ box, dedupe, merge, 500 a day cap), signed confirm and tap links with scanner filters, entry ledger capped at 5, hot-lead counter and manager alerts, two-layer schedule (contest dates plus warm-up days, one a day, quiet Tuesdays, contest wins the day), every email as data with a renderer that refuses non-ASCII, missing address, missing unsubscribe, winner wording to non-winners; auditable draw tool (frozen list, public seed, 3 alternates); winner flow and re-entry; the real copy ported in; 31 previews | Survey, result and rules pages that POST to the engine; `/win` redirects; bounce and complaint handler; result-email batching; daily `/booked` from FareHarbor; shared unsubscribe list with the weekly reel; weekly report; a 2027-01 round in `brands.json` |

## Loose ends to settle before Oct 19

- SC-13 (the hot-lead early code): the copy only sends it when the code is still locked; the engine also sends it to next-30-days riders whose code is already live. Follow the copy.
- SC-09 (winner notice) carries two [VERIFY] flags on prize terms that the engine strips. Do not enable until decision 3 is final.
- Facts the crew owes: two outdoor picks for the gator version of the local picks, one real guest review, the rain policy, what FareHarbor adds at checkout, ages on the pontoon and eco tour.
- The Countdown is not live, so the visitor hand-off (SC-17) is a bare link for now.
- Email deliverability: SPF on nolapartybarges.com lists only Amazon and there is no DMARC on the old pedal barge domain the weekly email uses. There is a separate check queued for that.

## Where the working files are

Reviews (facts, lint, compliance, branch logic, code), the copy source files, recovery scripts: `~/Projects/npb-lead-funnels/work`. Not in the vault on purpose.
