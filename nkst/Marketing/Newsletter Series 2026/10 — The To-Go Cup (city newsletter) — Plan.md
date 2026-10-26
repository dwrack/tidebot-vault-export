# The To-Go Cup: a New Orleans newsletter from the kayak crew

*Drafted 2026-10-16 from David's ask: "the larger to go cup newsletter email with more New Orleans local and visitor info so that we aren't just a kayak newsletter." DRAFT. Nothing built in code, nothing sent. Both versions are written out; David picks.*

## The idea in one line

Stop mailing people about kayaks twice a week. Mail them the city every other week, from the people who paddle it, and let the swamp be one section they look forward to.

## Who actually reads it (verified 2026-10-16)

| List | Size | Local vs visitor | Source |
|:-|-:|:-|:-|
| Past guests (SES list, warmed with em01 in June) | 28,905 mailable (31,599 raw, 2,694 suppressed) | **4.6% Louisiana area codes** (504: 859 phones). 90% US, then Canada 901, UK 770. Last booking spread 2015 to 2026. | `~/Projects/customer-audiences/data/neworleanskayakswamptours.csv`, `recipients.json` |
| Messenger lead form (May to Jul 2026) | 168 | **65% live in New Orleans**, 33% never kayaked | Funnel Lab file 01 |
| Quiz leads (not live yet) | 0 | Quiz asks "live here or visiting?" so every lead arrives tagged | Funnel Lab file 30 |

So today the newsletter audience is overwhelmingly people who visited once, often years ago. The local reader base only grows through the quiz and lead form. That decides the format question below.

What went out so far: em01 ("The bayou is glass at 8am") reached the whole list in June and July at about a 5% opt-out rate. Emails 02 to 16 of the summer series are built and never sent. The drip job on this laptop is disabled (`.disabled-dup-mbp2`); last run 2026-10-13 found nothing to send.

## Two versions, built out

### Version A: one edition, two lanes (my pick to start)

One email every other Thursday. Same issue to everyone. Two short labeled lanes inside it so each reader finds their part fast:

- **"In town this week"**: dated events, where to eat, one neighborhood thing. Written for a visitor, useful to a local.
- **"If you live here"**: the weeknight stuff, the free stuff, the thing that is only good if you can go on a Tuesday.

Pros: one build, one send, one list, reads per section via `utm_content`. Cons: locals (5% of the list) get a visitor-heavy email. Fine for now; they are 5%.

### Version B: two tracks

Visitor edition and Local edition, same skeleton, different lead story and events. Segment by phone area code (504, 985, 225) on the past-guest list, by the "live here" answer on quiz and lead-form leads.

Pros: locals get a newsletter that reads like it is for them, which is what the lead-form data says they are. Cons: two builds per issue, the local track goes to ~1,300 people until the quiz is live.

**Pick: A now. Flip to B when local leads pass about 2,000 (the quiz plus lead form can get there in a season).** Design A so the lanes can be lifted straight into B.

## Cadence and what happens to the summer series

- **Every other Thursday, 7:30 am Central.** Thursday is when people plan the weekend; biweekly keeps the unsub rate down after em01's 5%.
- **Retire the 2x/week promo cadence.** Emails 02 to 16 become source material: each To-Go Cup "On the water" section takes one of them (gators, first-timers, two swamps, plantation combo, gift cards for the holidays).
- The Funnel Lab quiz nurture (7 emails over 8 days, then monthly) is separate and stays separate. After q7, a lead drops into the To-Go Cup list. That is the "monthly series after q7" the quiz build notes say is not built yet.

## The skeleton (same every issue, 8 blocks)

| # | Block | What goes in it | Length |
|:-|:-|:-|:-|
| 1 | **The pour** | Two or three sentences of what the week feels like in the city. One voice, one opinion. | 60 words |
| 2 | **In town this week** | 4 to 6 dated events, two weeks out. Verified dates only, with the organizer link. | 6 lines |
| 3 | **Eat / drink** | One place, one specific order, one reason. No lists of ten. | 60 words |
| 4 | **The thing only locals know** | A neighborhood, a bridge, a bar night, a bakery, a bayou you can paddle in the city. | 80 words |
| 5 | **Swamp report** | What the guides saw this week (from the guide Slack logs), water temp or level, which tour time has the light. Real sightings or nothing. | 60 words + 1 photo |
| 6 | **On the water** | The booking block. One tour, one price, one button. Rotates through the old 02 to 16 angles. | 50 words + button |
| 7 | **Guide of the issue** | One guide, two lines, a photo. 55% of reviews name a guide. | 40 words |
| 8 | **Sister cities** | The DCKT / Austin band, visitors only (drop it in the local edition under Version B). | existing band |

Sign-off stays "The crew at New Orleans Kayak Swamp Tours". Never David's name. (Note: the Sept Growth Playbook names a guest-facing persona "Ray Fontaine"; the agent identity docs say "Magnolia". The newsletter has used "the crew" since June. Pick one if it matters.)

## Where the content comes from (so it does not cost a writer)

| Block | Source | Who |
|:-|:-|:-|
| Events | neworleans.com calendar, WWOZ Livewire, organizer sites. Dates checked against the organizer page the day before send. | Claude, with a [VERIFY] on anything not confirmed on the organizer's own site |
| Eat / drink, locals' thing | A standing list of 40 places and spots, each used once a year | Claude drafts, David or a guide adds the "I actually go here" line |
| Swamp report | Guide Pre/Post-Tour Slack posts (parsed by nkst-log-watch on mbp-2) | Claude pulls, no invention |
| On the water | emails 02 to 16 angles, seasonal campaigns doc | Claude |
| Guide of the issue | Guide Cards folder, review quotes naming the guide | Claude, guide's OK |

## Tracking (same pattern as the summer series)

- Every link: `?ref=tgc<NN>_<key>` for FareHarbor plus `utm_source=newsletter&utm_medium=email&utm_campaign=togocup&utm_content=tgc<NN>_<block>`.
- Bookings: FareHarbor Advanced Bookings report, Online Booking Reference contains `tgc`.
- Which blocks get read: GA4 landings by `utm_content` for links that land on our site. Event and restaurant links are external, so wrap them through the lead engine's `/t` go-link (it already logs taps) if we want section-level click counts. Otherwise we only see on-site clicks.
- No SES open tracking (David declined it in June; not re-pitching).
- Watch: opt-out rate per issue vs em01's 5%, replies to the email, FareHarbor `tgc` bookings, Extended share.

## Tests to run inside it (Funnel Lab style)

| Test | A | B | Reads on |
|:-|:-|:-|:-|
| Subject line | City first ("What's good in New Orleans this week") | Swamp first ("The gators are still out, and so is Po-Boy Fest") | On-site landings per send (no opens) and replies |
| Block order | City blocks first, swamp report mid, booking block last | Swamp report first | Clicks on the booking block |
| Send day | Thursday 7:30 am | Sunday 8:00 am | Landings per send |

Split the list in half by email hash per test; one test at a time; two issues per test.

## Production path

1. Add a `layout: "togocup"` template to `~/Projects/nkst-tools/newsletter-2026/build.mjs` (one new renderer next to `feature`; the cards and partners pieces already exist). About an afternoon.
2. Content per issue lives in `emails.mjs` as today, with `events[]`, `eat`, `local`, `swamp`, `guide` fields.
3. Photos: guest and guide photos from the tour logs, resized with `sips -Z`, uploaded to the `nkst-email-assets` bucket, version-stamped.
4. Same review gate as the summer series: build, screenshot at 390 and 680 px, live test to David, then the list. First issue goes in two waves (5k, then the rest) because the list has not been mailed since July.
5. Issues 1 and 2 are drafted in this folder: [[11 — To-Go Cup Issue 1 (draft, Oct 22)]] and [[12 — To-Go Cup Issue 2 (draft, Nov 5)]].

## Open questions for David

1. Version A (one edition, two lanes) now, B (two tracks) later: agree?
2. Every other Thursday, and retire the 2x/week summer promo cadence (02 to 16 become section material)?
3. Name: "The To-Go Cup" as the newsletter name and the subject prefix, e.g. "The To-Go Cup: Po-Boy Fest, gator weather, and a bakery in the East"?
4. Who adds the one "I actually go here" line per issue: you, a guide, or nobody (Claude writes it straight)?
5. First send date: Thursday Oct 22 (issue 1 covers Oct 24 to Nov 8)? That needs the template built and a live test by Oct 21.
6. Sign-off: "the crew" (current), Magnolia, or Ray Fontaine?

## Template status and what it needs next (2026-10-20)

Built, not sent. `layout: "togocup"` renderer is in `~/Projects/nkst-tools/newsletter-2026/build.mjs`; issue 1 is `n: 101, slug: "togocup-01"` in `emails.mjs`; output `out/em101-togocup-01.html` + `.txt`. Screens at 390 and 680 px: `screens/togocup-01-390.png`, `screens/togocup-01-680.png`. The 16 summer emails rebuild byte-identical.

- Every `[VERIFY ...]`, `[FILL ...]` and `[NPB BLOCK ...]` renders highlighted plus a red DO-NOT-SEND banner listing them (18 open on issue 1). `send-ses.mjs` refuses `--go` while the banner is there (`--test` still works). The banner disappears once the last marker is gone.
- Tracking as planned: `ref=tgc01_<tour>`, `utm_campaign=togocup`, `utm_content=tgc01_<block>`; sister band `ref=nkst_tgc01`.

What it needs next:
1. **Photo for block 5 (swamp report):** a real shot from this week's guide logs, `sips -Z 1600`, upload to `nkst-email-assets`, set `swamp.img`. Same slot pulls the sightings line from the Pre/Post-Tour logs.
2. **Photo for block 7 (guide of the issue):** Nick from the Guide Cards folder, with his OK on name, quote and photo; set `guide.img`.
3. **NPB blocks:** boat trip (title, ~50 words, price, button URL with `ref=tgc01_npb`) and the NPB captain (name, two lines, review quote, photo). Placeholders are in `npbWater` and `npbCaptain`. Not in files 11/12 yet and no NPB note in the shared notes folder as of 2026-10-20.
4. **NPB sender and list decision:** does issue 1 go only from NKST to the 28.9k NKST list (NPB rides as a block), or also to the NPB list from an NPB sender? Decides the sign-off (marker 18), the footer address, and whether NPB needs its own build/unsub setup.
5. The event, Parkway and rental-link `[VERIFY]` checks the day before send, and the Bayou St. John blog post published so its link can go in.
