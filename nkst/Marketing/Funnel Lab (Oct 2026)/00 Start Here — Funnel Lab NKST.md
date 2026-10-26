*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NKST.*

# Funnel Lab: NKST, start here

> **CURRENT STATUS (verified 2026-10-15, NKST session):**
> - Messenger lead form: 0 fills in the last 30 days, last one 2026-07-15. Meta lead campaign 6983621892296 is PAUSED ($52 for 27 leads Jul 1 to Oct 15). Card 7 has no traffic until it is turned back on.
> - NKST paid is dark: retargeting campaign 52555873581500 active but its only ad set paused ($0 in 30 days); Google campaigns paused (file 02).
> - Live FAQ still says $59 / $79 and "do not rely on Uber" (checked today). Tour page: $65 / $130, shuttle $25, 25 miles; FAQ says 30 miles.
> - Built as drafts: OpenCX workflow `482df656-3429-4c01-95d6-49e5e0b6413a` (inactive) for card 7; card 8 Meta build is a paste-ready spec (API refused); quiz "sunset" result reworded on branch `quiz-nkst`. Details: [[50 Launch Drafts — NKST (2026-10-15)]].
> - Open questions below: items 5 (drive time 30 to 40 min, verified) and the card 7 sample are now answered in file 50; the list is otherwise still open.

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for New Orleans Kayak Swamp Tours: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

## Board cards for NKST

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
| c07 (04 card 7) | Lead-form rescue | both | approved | (none) | (none) |
| c08 (04 card 8) | Locals who've never been vs visitors | both | approved | (none) | (none) |
| c16 (04 card 16) | Fix purchase tracking [NKST + HPB + NPB] | park | parked | (none) | (none) |

## Site and testing surface

FareHarbor WordPress site with no GTM (neworleanskayakswamptours.com). Needs one FareHarbor header-script slot. GA4 G-MXM09J7C5Y. (03)

## Open questions

Gathered from 00, 04, 10, 11, 12, 30, 31 and 40 in the hub, plus the card notes above. Numbers in parentheses point to the source file.

1. NKST live FAQ prices ($59 / $79) are stale vs the live tour page ($65 Manchac, $130 extended, shuttle +$25). Update the live FAQ. (31)
2. Uber to the swamp: live FAQ says don't, vault FAQ Complete says fine. Pick one, update both. (31)
3. Distance: live site says 25 miles in one place and 30 in another. (31)
4. "Sunset" tour is the 4:30pm start (golden hour in fall only, summer sunset is ~8pm). Reword the result title. (31)
5. Card 7: [VERIFY monthly form fills] to set the sample time. Card 8: [VERIFY drive time] for the locals hook. (04)
6. OK to email the FareHarbor rep for the header-script slot on NKST? (00 open question 2; card 3)
7. Budget for card 8: $15/day, 14-21 days. David confirms before any go. (40)
8. Weather credit (card 4) is parked on the board; NKST's FAQ still promises a full refund. (10)
9. Tracking fix (card 16) is parked: read NKST results from FareHarbor and the ad platforms, not GA4. (40)
10. How did you hear about us (card 5, still waiting on the board): optional or required, roll to all FareHarbor brands at once or NKST-only for 30 days first, and who flips the setting in each FareHarbor dashboard? (11)
11. Which brand goes first on the quizzes? Claude's pick: NPB, then NKST, then E&E. (30)
12. OK for the "still deciding?" email to come from a person's first name at the business (never David's name)? (30)


## David's answers (2026-10-16)

| # | Question | David | Done / next |
|:-|:-|:-|:-|
| 1 | Live FAQ prices | Yes, update to $65 / $130 / +$25 | In progress via wp-admin on mbp-2 |
| 2 | Uber to the launch | No, cost prohibitive. Live FAQ wording stands | Vault FAQ Complete section 7 to be corrected |
| 3 | Distance | 30 miles | Use "about 30 miles, 30 to 40 minutes" everywhere |
| 4 | Quiz "sunset" result | Confused what it referenced | It is the 30-second quiz result title; renamed to "The evening swamp paddle" on branch quiz-nkst |
| 5 | Weather refund wording | Leave both alone. Likes a cancellation-insurance add-on eventually | Idea parked here: FareHarbor-compatible booking protection add-on, revisit with card 4 |
| 7 | Card 7 traffic | Build an amazing cold-traffic funnel and drip first (guides, restaurants, city hype, To-Go Cup style, video, photos, no sales asks). Subscribe to great newsletters and watch how they do it | See [[60 Cold-Traffic Drip — NKST]]; benchmark signups running from info@ |
| 8 | Card 7 workflow dry run | Test and report, what is the best scenario | Dry run: week-parity and branching work; best scenario is the ai-response-requested trigger with the built-in reply suppressed (rebuilt inactive) |
| 9 | Card 8 Meta build | Wait until the funnel is better. Full funnel focus | Parked; spec stays in file 50 |
| 10 | Card 8 audiences | Two different audiences: travelers in New Orleans (fast) and travel-intent (slow) | Recorded on the board |
| 11 | FareHarbor header-script email | Probably, but design our own site first and do it that way | Not sending; popup and tests ride on the new site |
| 12 | How did you hear | Optional, in the quiz not checkout | Added to both NKST quizzes |
| 13 | Quiz order and add-on | Sure (NPB first, drop the dry-bag arm). Let quizzes reveal persona gaps; look at who they follow on IG via Apify | Follower-persona pass proposed as a session |
| 14 | Still-deciding sender | Michelle and Dylan are NOT managers; remove from memory and notes. Michelle still guides | Memory scrubbed 2026-10-16; email signs as the business |
| 15 | Postal address for the engine | Yes: 740 N Rampart St, New Orleans, LA 70116, 504-571-9975 | Needs the hub session to set brands.json (not an NKST-only file) |
| 16 | Read results from FareHarbor and Ads, never GA4 | "You sure?" | Yes for purchases: GA4 saw 4 purchase events vs 135 FareHarbor online bookings in the same window |

Also 2026-10-16: "work with NPB and NKST to build the To-Go Cup together." Message sent to the NPB Funnel Lab session; plan in `Marketing/Newsletter Series 2026/10`.

## Files in this folder

- [[01 Customer Truth — NKST]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — NKST]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — NKST]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — NKST]]: weather credit vs refund, both versions plus a live test
- [[11 How Did You Hear About Us — NKST]]: how did you hear about us, two versions
- [[20 Abandoned Bookings — NKST]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — NKST]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — NKST]]: what each approved card takes to launch, who, and what spends money
- [[50 Launch Drafts — NKST (2026-10-15)]]: what was verified live, the inactive OpenCX workflow, the paste-ready Meta build, the quiz reword

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/nkst.json`, `engine/copy/nkst_quiz.json`, previews `previews/quiz/nkst-A.html` and `previews/quiz/nkst-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
