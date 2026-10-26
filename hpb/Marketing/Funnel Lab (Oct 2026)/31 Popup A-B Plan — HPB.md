*Drafted 2026-10-15 by the HPB funnel session. DRAFT. Nothing deployed, nothing on the site. Board card c21: David's pick = A (quiz popup). Card c03: pick = both, note "do we do a pop up?".*

# Popup A/B plan: HPB, quiz popup vs offer popup

## Where it stands today (verified 2026-10-15)

| Item | State |
|:-|:-|
| Lead-engine widget on houstonpedalbarge.com | **Not on the site.** The homepage source has no engine script. It loads Elfsight, the OpenCX chat widget, jQuery and a Complianz cookie-consent manager, nothing of ours. |
| Engine config for hpb (brands.json, quiz branch) | enabled, offer wave CREW25 $25 off 2+ guests, expires 2026-10-31, sms_enabled false, quiz_enabled false |
| Leads in the engine table | 4 all-time (verified 2026-10-14). With no script on the site these are test or manual records, not visitor leads. |
| Quiz for hpb | A and B built in `engine/quiz/hpb.json` with 4 [VERIFY] holes: weather and refund wording, the over-26 result (blurb, tour, price), parking. Engine refuses to go live with any [VERIFY]. |
| Variant assignment | branch ab-variants, 36 tests, not merged, not deployed |
| Blocker | one FareHarbor header-script slot on HPB (card c03 open question). Someone already added Elfsight and OpenCX to this site, so the slot exists; we need the rep or whoever has access. |
| Traffic to test on | 4,528 sessions in 30 days, 93% mobile, 3,998 land on the homepage, 68% organic social at 9% engagement (02 Baseline) |

## The two arms, built both ways

Board picks that shape the quiz arm: c19 = B (email unlocks the result), c20 = A (help-first nurture, first ask on day 5, no day-2 add-on).

### Arm A: quiz popup (David's pick on c21)

HPB-specific angle. The #1 first question in chats is price (27%) and the #1 confusion is private barge vs public seats (16% of first questions, 35% of chats). So the popup promises the answer to both, not "find your tour".

| Field | Copy |
|:-|:-|
| Headline | Whole barge or just seats? |
| Sub | Four taps and you'll know what fits your crew and what it costs. |
| Button | Start the 30-second quiz |
| Mobile bottom bar (collapsed) | Whole barge or seats? 30-sec quiz |
| Alt headline to rotate later | Not sure which cruise? 30-second quiz. |

Flow: popup tap opens /quiz/hpb (A or B quiz style, 50/50 per c18) in the same tab. Four questions. Email gate before the reveal (c19 = B): "Where should we send your result?" Result page shows the fit, the live price line, one proof line, and the weather and refund rule in plain words (fear_answer, still [VERIFY]). Then the help-first drip from `engine/copy/hpb_quiz.json`.

### Arm B: offer popup (today's engine copy, written as the control)

| Field | Copy |
|:-|:-|
| Headline | Your crew's $25 is waiting. |
| Sub | Clear Lake's BYOB party barge. Fully captained, up to 26 people. Grab $25 toward your date. |
| Button | Send my $25 |
| Mobile bottom bar | Get $25 toward your party |
| Code | CREW25, good on 2+ guests. **Expires 2026-10-31**, so this arm needs a new wave code or an extended date before launch. [David] |

Flow: email, optional step 2 for SMS (sms is off, so step 2 should be hidden until HPB has a number), code emailed, existing offer drip.

### Shared mechanics (same in both arms so only the offer differs)

| Setting | Value | Why |
|:-|:-|:-|
| Trigger | 20 seconds on page, or scroll-up on mobile (exit intent) | 93% mobile; desktop exit-intent doesn't exist on phones |
| Pages | homepage and blog posts. Suppressed on /houston-party-barge-cruise, the FareHarbor embed, gift card page, contact page | don't interrupt someone already booking |
| Suppress when | the OpenCX chat window is open; the visitor already submitted either form; visitor arrived with ?ref=quiz or from the drip | one ask at a time |
| Frequency cap | once per 7 days per visitor after dismiss | review-safe |
| Assignment | visitor hash in w.js, 50/50, sticky for 30 days (ab-variants branch) | same visitor always sees the same arm |
| Consent | Complianz is on the site. The engine script must be registered as functional (or load before consent gating) or it never fires for most visitors. [VERIFY with whoever holds the slot] | |

## How we read it (not GA4; HPB has zero FareHarbor events there)

| Metric | Source | Arm A | Arm B |
|:-|:-|:-|:-|
| Primary: emails per 100 popup views | engine table (brand hpb, variant tag) | quiz completions with email | offer signups |
| Quiz completion rate | engine | yes | n/a |
| Bookings per 100 emails within 30 days | FareHarbor Advanced Bookings report, Online Booking Reference contains `quiz-hpb-A` | tag every quiz and drip link `?ref=quiz-hpb-A` | tag `?ref=popup-hpb-B` |
| Revenue per email | same report, gross | | |
| Sanity: homepage engagement rate | GA4 (page_view exists) | must not drop more than 20% vs the prior 30 days in either arm | |

Leakage warning: 64% of HPB online bookings carry a blank ref (20 Abandoned Bookings), so tagged counts are a floor. Read both arms the same way and the comparison still holds.

## Sample and timing

- 4,528 sessions a month. If the popup shows on about 70% of them, that is roughly 1,600 views per arm per month.
- To see 2% vs 3% emails per view you need about 2,000 views per arm, so call it **30 to 40 days** for the primary read. Bookings per email reads over a second month.
- Weather credit, quiz facts and the drip copy all have to be finished first; the popup is the front door, not the test.

## Pre-launch checklist (in order, nothing here goes live without David's go)

1. David: cancel window (72h or 48h), weather wording, address, over-26 answer. These fill the four [VERIFY] holes in hpb.json. Claude edits in the quiz-hpb worktree, runs the 219 tests, shows previews.
2. David: new offer code or extended CREW25 for Arm B. Code created in FareHarbor by the manager.
3. Connor (or the FH rep): header-script slot on houstonpedalbarge.com. Claude drafts the email; David OKs sending it (c03 open question).
4. Engine: merge ab-variants and quiz-funnels, set quiz_enabled true for hpb, deploy. Not this session; HPB is the engine's live regression brand, so the deploy gets its own go from David.
5. Complianz category confirmed so the script fires.
6. Day 1 check: both arms render on a phone, submissions land in the table with the right variant tag, ref tags show in a test booking.
7. Read at day 30 and day 60. One row per read on board card c21.

## If c21 "pick = A" means quiz popup only, not a split

Then Arm B is just today's offer popup kept as the control until Arm A is on the site, and the read is before vs after (weaker, seasonal noise). My recommendation stays the 50/50 split: same traffic, same month, half the ambiguity. David's call, see the numbered list.
