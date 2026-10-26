*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NPB.*

# Funnel Lab: NPB, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for NOLA Party Barge: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

## Board cards for NPB

Board data read 2026-10-15 from the Funnel Lab Board. 'none yet (waiting)' means David has not picked. Status values are as on the board.

| Card id | Title | David's pick | Status | David's note | Claude's reply |
|:-|:-|:-|:-|:-|:-|
| c18 (file 30, decision 1) | Quiz style: find-your-tour vs personality [All brands] | both | approved | (none) | (none) |
| c19 (file 30, decision 2) | Quiz: when we ask for the email [All brands] | B | approved | (none) | (none) |
| c20 (file 30, decision 3) | Nurture: help first vs small offer early [All brands] | A | approved | (none) | (none) |
| c21 (file 30, decision 4) | Popup: quiz vs offer [All brands] | A | approved | (none) | (none) |
| c01 (04 card 1) | Chat: price first, then what? | B | approved | can we make more split testing options, use some psychology, try using some wit | Done. Five versions now: straight, group math, wisecrack ('two Hurricanes and one bad decision'), decoy, and real-scarcity. At ~100 chats a month we run them as a knockout: all five for 4 weeks, drop the bottom two, then the top three. See the new card 'NPB chat: five-way knockout' and file 12. |
| c17 (file 12, card 1.5) | NPB chat: five-way knockout | both | approved | (none) | (none) |
| c02 (04 card 2) | Where cold social traffic lands [NPB + BBK + LSKT] | none yet (waiting) | waiting | (none) | (none) |
| c03 (04 card 3) | How we'll run on-site and email tests [All brands] | both | approved | do we do a pop up? | Yes. The popup becomes the quiz's front door: 'Not sure which tour? 30-second quiz' tested against today's '$25 off' popup. See the new popup card. It still needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT; DCKT and BBK use GTM, E&E the Squarespace footer. |
| c04 (04 card 4) | Weather cancel: credit instead of refund [NKST + BBK + LSKT] | park | parked | (none) | (none) |
| c05 (04 card 5) | How did you hear about us? [All brands] | none yet (waiting) | waiting | (none) | (none) |
| c06 (04 card 6) | Birthday vs bachelorette ads | both | approved | (none) | (none) |
| c16 (04 card 16) | Fix purchase tracking [NKST + HPB + NPB] | park | parked | (none) | (none) |

## Site and testing surface

FareHarbor WordPress site with no GTM (nolapartybarges.com). We cannot ship JS ourselves; needs one FareHarbor header-script slot. GA4 G-XXFJS3P16F. (03)

## Open questions

Gathered from 00, 04, 10, 11, 12, 30, 31 and 40 in the hub, plus the card notes above. Numbers in parentheses point to the source file.

1. Confirm live NPB prices and Party Queen capacity (chat says 22, site says 26). (00 open question 1; 04 card 1 and 12)
2. Fix the wrong prices in Nolan's knowledge base (seat $63 there vs $59 live) before any chat version runs. (12 Before it can run; 31)
3. Version E of the chat test needs the bot to call /avail (on the capture-v2 branch, not deployed); if the number isn't live, E can't run. (12)
4. NPB decorations add-on: is there one, and what does it cost? (31 final list, item 5)
5. NPB kids: live FAQ says public trips 21+, kids 6+ private only; vault says kids welcome. Pick one. (31)
6. OK to email the FareHarbor rep for the header-script slot on NPB (also NKST, HPB, LSKT, AKT)? (00 open question 2; card 3)
7. Budgets for cards 2 and 6: $20/day each test, 14-21 days, on top of current spend unless carved out. David confirms before any go. (40)
8. NPB can't text until the toll-free sender is re-verified (rejected 6/29). (30)
9. How did you hear about us (card 5, still waiting on the board): optional or required, roll to all FareHarbor brands at once or NKST-only for 30 days first, and who flips the setting in each FareHarbor dashboard? (11)
10. Which brand goes first on the quizzes? Claude's pick: NPB, then NKST, then E&E. (30)
11. OK for the "still deciding?" email to come from a person's first name at the business (never David's name)? (30)

## Files in this folder

- [[01 Customer Truth — NPB]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — NPB]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — NPB]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — NPB]]: weather credit vs refund, both versions plus a live test
- [[11 How Did You Hear About Us — NPB]]: how did you hear about us, two versions
- [[12 Chat — Five Price Replies]]: five price replies as a knockout test
- [[20 Abandoned Bookings — NPB]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — NPB]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — NPB]]: what each approved card takes to launch, who, and what spends money

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/npb.json`, `engine/copy/npb_quiz.json`, previews `previews/quiz/npb-A.html` and `previews/quiz/npb-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).

## Session log

- 2026-10-15: NPB session built the launch drafts for the approved cards (OpenCX price replies A, C, D, E as unpublished drafts; Meta birthday vs bachelorette spec; quiz branch quiz-npb). Nothing live. Status, what each draft does, and the single numbered question list: [[41 Launch Drafts — NPB (2026-10-15)]]. Answer those by number; the 11 questions above are folded into that list.
