*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for E&E.*

# Funnel Lab: E&E, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for Ebb & Ember (Portland floating sauna): customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

E&E is on Periode, not FareHarbor, so there is no weather credit file (file 10), NPB chat file (12) or abandoned-bookings file (20) for this brand. File 11 (how did you hear about us) applies: E&E gets version B.

## Board cards for E&E

Board data read 2026-10-15 from the Funnel Lab Board. 'none yet (waiting)' means David has not picked. Status values are as on the board.

| Card id | Title | David's pick | Status | David's note | Claude's reply |
|:-|:-|:-|:-|:-|:-|
| c18 (file 30, decision 1) | Quiz style: find-your-tour vs personality [All brands] | both | approved | (none) | (none) |
| c19 (file 30, decision 2) | Quiz: when we ask for the email [All brands] | B | approved | (none) | (none) |
| c20 (file 30, decision 3) | Nurture: help first vs small offer early [All brands] | A | approved | (none) | (none) |
| c21 (file 30, decision 4) | Popup: quiz vs offer [All brands] | A | approved | (none) | (none) |
| c03 (04 card 3) | How we'll run on-site and email tests [All brands] | both | approved | do we do a pop up? | Yes. The popup becomes the quiz's front door: 'Not sure which tour? 30-second quiz' tested against today's '$25 off' popup. See the new popup card. It still needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT; DCKT and BBK use GTM, E&E the Squarespace footer. |
| c05 (04 card 5) | How did you hear about us? [All brands] | none yet (waiting) | waiting | (none) | (none) |
| c09 (04 card 9) | Open on the river jump vs the sauna | both | approved | (none) | (none) |
| c10 (04 card 10) | Booking page: reassure vs fake-choice | park | parked | (none) | (none) |
| c11 (04 card 11) | After the visit: bring a friend vs book your next | both | approved | (none) | (none) |

## Site and testing surface

Squarespace (ebbandember.com): Footer Code Injection can carry a split snippet today, client-side only. Booking is on Periode, not FareHarbor. Astro + Cloudflare Pages rebuild would allow an edge split. (03)

## Open questions

Gathered from 00, 04, 10, 11, 12, 30, 31 and 40 in the hub, plus the card notes above. Numbers in parentheses point to the source file.

1. What is the E&E bring-a-friend offer? Claude did not invent one. (00 open question 3; card 11)
2. Card 11: [VERIFY how visits reach AC] (Periode visit trigger) and [VERIFY plan tier supports split testing] in ActiveCampaign. (40, 04)
3. Card 9: Kimberlynn needs a [DATE] for the two 12-second cuts; the Slack draft is in 40 Launch Steps. David sends it. (40)
4. Card 10 (booking page) is parked; details to VERIFY: parking/transit, what to bring, towels provided, session length. (04)
5. E&E live FAQ says no staff on site, self-guided; hours 6am to 10pm live vs 7am to 9pm in the memory note (Claude updated memory). (31)
6. The add-on for the small-offer-early email at E&E: what is real? (31 final list, item 1)
7. Budget for card 9: IG trial reels first ($0), $10/day per arm only if boosted. David confirms before any go. (40)
8. How did you hear about us (card 5, still waiting on the board): E&E gets version B (one-tap question after they pay) because Periode does not take extra fields easily. (11)
9. Which brand goes first on the quizzes? Claude's pick: NPB, then NKST, then E&E. (30)
10. OK for the "still deciding?" email to come from a person's first name at the business (never David's name)? (30)

## Files in this folder

- [[01 Customer Truth — E&E]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — E&E]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — E&E]]: every A/B test card that names this brand, with David's board picks
- [[11 How Did You Hear About Us — E&E]]: how did you hear about us, two versions
- [[30 Quiz — E&E]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — E&E]]: what each approved card takes to launch, who, and what spends money

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/ebb.json`, `engine/copy/ebb_quiz.json`, previews `previews/quiz/ebb-A.html` and `previews/quiz/ebb-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
