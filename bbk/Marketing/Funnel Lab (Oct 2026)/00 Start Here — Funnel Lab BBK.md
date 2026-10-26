*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for BBK.*

# Funnel Lab: BBK, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for Buffalo Bayou Kayak: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

## Board cards for BBK

Board data read 2026-10-15 from the Funnel Lab Board. 'none yet (waiting)' means David has not picked. Status values are as on the board.

| Card id | Title | David's pick | Status | David's note | Claude's reply |
|:-|:-|:-|:-|:-|:-|
| c18 (file 30, decision 1) | Quiz style: find-your-tour vs personality [All brands] | both | approved | (none) | (none) |
| c19 (file 30, decision 2) | Quiz: when we ask for the email [All brands] | B | approved | (none) | (none) |
| c20 (file 30, decision 3) | Nurture: help first vs small offer early [All brands] | A | approved | (none) | (none) |
| c21 (file 30, decision 4) | Popup: quiz vs offer [All brands] | A | approved | (none) | (none) |
| c02 (04 card 2) | Where cold social traffic lands [NPB + BBK + LSKT] | none yet (waiting) | waiting | (none) | (none) |
| c03 (04 card 3) | How we'll run on-site and email tests [All brands] | both | approved | do we do a pop up? | Yes. The popup becomes the quiz's front door: 'Not sure which tour? 30-second quiz' tested against today's '$25 off' popup. See the new popup card. It still needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT; DCKT and BBK use GTM, E&E the Squarespace footer. |
| c04 (04 card 4) | Weather cancel: credit instead of refund [NKST + BBK + LSKT] | park | parked | (none) | (none) |
| c05 (04 card 5) | How did you hear about us? [All brands] | none yet (waiting) | waiting | (none) | (none) |
| c12 (04 card 12) | Bat landing page: rebuild vs skip it | both | approved | (none) | (none) |
| c13 (04 card 13) | Honest water line vs none | both | approved | (none) | (none) |

## Site and testing surface

FareHarbor WordPress with GTM (buffalobayoukayak.com, GTM-TKMN5XSX). GTM holds no Custom HTML tags yet; who has publish access is unverified. (03)

## Status 2026-10-15 (BBK session, live checks)

CURRENT STATUS, verified 2026-10-15. The "Open questions" list below is history from the split; this block is what is true now.

- **Meta is NOT paused.** "Bat Bridge Kayak Tour - Traffic" is ACTIVE at $20/day (link clicks), $597 spent last 30 days, 3,385 landing page views, 0 reported purchases. The bat tour sold 6 bookings / $769 in the same window (FareHarbor). The May memory note "all BBK ads paused" was stale.
- **Bat season (Q1):** Texas Parks and Wildlife says bats occupy the Waugh Bridge every month of the year, peak summer and early fall; TPWD's own biologist avoids "non-migratory". Freezes have killed bats under the bridge in Feb 2021 and Dec 2022, so they are there in winter. A Feb 2026 Google review describes a bat tour that saw bats. Honest wording: year-round colony, biggest emergences summer to early fall, thinner in deep winter, never guaranteed. David confirms wording.
- **Bat tour length (Q3):** still 2 hours (Quick Details) vs 3-hour (body) on the live page. FareHarbor item is named "Bats & Kayaks Tour" (id 619305); the site says "Houston Bat Bridge Kayak Tour"; the press release says "Sunset Skyline Bat Bridge Tour". David picks the length, Connor fixes the page.
- **History paddle (quiz):** no such tour exists. Options: point the result at the Houston Skyline Kayak Tour ($55, 2 hours, history talk is part of it) or the Downtown Houston Walking History Tour ($59 adult / $39 child, 2 hours, walking). My pick: Skyline paddle, it is a kayak quiz.
- **Guide roster (Q4):** vault lists Dulce Delgado and Axel Johnson (added 2026-05-12). 2026 reviews name Josh (~30), Chad (~26), Ian (~19); Blake is in 146 reviews all-time. Ask Connor for the current roster in the next batch.
- **GTM (Q2):** GTM-TKMN5XSX loads on every page; no Custom HTML tags. Publish access still unverified; David checks tagmanager.google.com with his Google logins or asks Connor.
- **Pixels:** the site fires 381452300055179 (33 Purchase events 9/17 to 10/14). Pixel 1559188957448084 is shared with HPB and LSKT (356 Purchases in the window, mixed brands). Use 381452300055179 for BBK optimization.
- **Drafts written:** `50 Approved Builds — BBK.md` (bat page A/B copy, GTM tags, water line tag, c02 Meta drafts both arms, all PAUSED/unpublished).
- **Quiz code:** worktree `~/Projects/fh-lead-engine-quiz-bbk` on branch `quiz-bbk` created, no edits yet (waiting on bat season and history-paddle calls).

## Open questions

Gathered from 00, 04, 10, 11, 12, 30, 31 and 40 in the hub, plus the card notes above. Numbers in parentheses point to the source file.

1. BBK: are bats year-round? Press release and agent doc say yes; ad research scripts say bats leave in winter. (31 final list, item 3)
2. Who has GTM publish access on BBK (and DCKT)? Cards 12 and 13 need it. (00 open question 4; 04)
3. BBK bat tour length: live page says 2 hours and 3 hours in the same page text. (31)
4. Guide roster in the vault (Dulce and Axel) vs 2026 reviews (Josh, Chad, Ian). (31)
5. Budget for card 2: $10/day, 21 days. David confirms before any go. (40)
6. Weather credit (card 4) is parked on the board. (10)
7. How did you hear about us (card 5, still waiting on the board): optional or required, roll to all FareHarbor brands at once or NKST-only for 30 days first, and who flips the setting in each FareHarbor dashboard? (11)
8. Which brand goes first on the quizzes? Claude's pick: NPB, then NKST, then E&E. (30)
9. OK for the "still deciding?" email to come from a person's first name at the business (never David's name)? (30)

## Files in this folder

- [[01 Customer Truth — BBK]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — BBK]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — BBK]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — BBK]]: weather credit vs refund, both versions plus a live test
- [[11 How Did You Hear About Us — BBK]]: how did you hear about us, two versions
- [[20 Abandoned Bookings — BBK]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — BBK]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — BBK]]: what each approved card takes to launch, who, and what spends money
- [[50 Approved Builds — BBK]]: paste-ready bat page copy (A and B), GTM tags for c12 and c13, PAUSED Meta drafts for c02, added 2026-10-15

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/bbk.json`, `engine/copy/bbk_quiz.json`, previews `previews/quiz/bbk-A.html` and `previews/quiz/bbk-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
