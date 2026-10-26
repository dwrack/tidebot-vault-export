*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for HPB.*

# Funnel Lab: HPB, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for Houston Pedal Barge: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

## Board cards for HPB

Board data read 2026-10-15 from the Funnel Lab Board. 'none yet (waiting)' means David has not picked. Status values are as on the board.

| Card id | Title | David's pick | Status | David's note | Claude's reply |
|:-|:-|:-|:-|:-|:-|
| c18 (file 30, decision 1) | Quiz style: find-your-tour vs personality [All brands] | both | approved | (none) | (none) |
| c19 (file 30, decision 2) | Quiz: when we ask for the email [All brands] | B | approved | (none) | (none) |
| c20 (file 30, decision 3) | Nurture: help first vs small offer early [All brands] | A | approved | (none) | (none) |
| c21 (file 30, decision 4) | Popup: quiz vs offer [All brands] | A | approved | (none) | (none) |
| c03 (04 card 3) | How we'll run on-site and email tests [All brands] | both | approved | do we do a pop up? | Yes. The popup becomes the quiz's front door: 'Not sure which tour? 30-second quiz' tested against today's '$25 off' popup. See the new popup card. It still needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT; DCKT and BBK use GTM, E&E the Squarespace footer. |
| c04 (04 card 4) | Weather cancel: credit instead of refund [NKST + BBK + LSKT] | park | parked | (none) | (none) |
| c05 (04 card 5) | How did you hear about us? [All brands] | none yet (waiting) | waiting | (none) | (none) |
| c16 (04 card 16) | Fix purchase tracking [NKST + HPB + NPB] | park | parked | (none) | (none) |

## Site and testing surface

FareHarbor WordPress site with no GTM (houstonpedalbarge.com). Needs one FareHarbor header-script slot. Only brand with the lead-engine popup/drip enabled (4 leads ever). (03, 02)

## Open questions

Gathered from 00, 04, 10, 11, 12, 30, 31 and 40 in the hub, plus the card notes above. Numbers in parentheses point to the source file.

1. HPB: 48 or 72 hours cancellation window, and is the second barge still running? (31 final list, item 4)
2. OK to email the FareHarbor rep for the header-script slot on HPB? (00 open question 2; card 3)
3. HPB prices: live $55 seat, $800 whole barge (up to 26), $150 deposit vs vault $59-69, $800-950. Address 2515 E NASA Pkwy (footer) vs 2513 NASA Road 1 (booking page). Arrival 30 min to 1 hour (live) vs 15 min (vault). (31)
4. Numbers in progress for SMS at HPB [VERIFY]. (30)
5. Tracking (card 16) is parked: HPB has no FareHarbor events in GA4, so read results from FareHarbor and the ad platforms. (02, 40)
6. Weather credit (card 4) is parked; 17 of HPB's 19 low-star reviews are cancels and slow refunds. (10, 01)
7. How did you hear about us (card 5, still waiting on the board): optional or required, roll to all FareHarbor brands at once or NKST-only for 30 days first, and who flips the setting in each FareHarbor dashboard? (11)
8. Which brand goes first on the quizzes? Claude's pick: NPB, then NKST, then E&E. (30)
9. OK for the "still deciding?" email to come from a person's first name at the business (never David's name)? (30)

## Files in this folder

- [[01 Customer Truth — HPB]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — HPB]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — HPB]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — HPB]]: weather credit vs refund, both versions plus a live test
- [[11 How Did You Hear About Us — HPB]]: how did you hear about us, two versions
- [[20 Abandoned Bookings — HPB]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — HPB]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — HPB]]: what each approved card takes to launch, who, and what spends money
- [[12 Weather Cancel Texts — HPB (Version B drafts)]]: added 2026-10-15, eight paste-ready SMS templates plus the even/odd split, drafts only
- [[31 Popup A-B Plan — HPB]]: added 2026-10-15, quiz popup vs offer popup, triggers, how to read it without GA4, pre-launch checklist

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/hpb.json`, `engine/copy/hpb_quiz.json`, previews `previews/quiz/hpb-A.html` and `previews/quiz/hpb-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
