# Launch Drafts: NPB (2026-10-15)

*Written 2026-10-15 by David's Claude (NPB funnel session). Everything here is PAUSED, DRAFT or INACTIVE. Nothing is live, nothing sent, nothing spent. Each piece flips on only after David says so in a turn.*

## Where NPB stands (verified 2026-10-15)

| Piece | State today | Source |
|:-|:-|:-|
| Approved cards | c01 (chat, pick B), c17 (five-way knockout, both), c06 (birthday vs bachelorette, both), c03 (test infra, both), c18 (quiz style, both), c19 (email gate, B), c20 (nurture, A), c21 (popup, A) | board read 2026-10-15 |
| Waiting on David | c02 cold social landing (no pick), c05 how did you hear (no pick) | board |
| Parked | c04 weather credit, c16 tracking fix | board |
| Live Meta ads | Gator Collision 4-way test, 4 ad sets at $40/day, ads already quote $59 / $1,200 (v1 ads checked 10/15) | fb_get_ads |
| Nolan's prices | Pricing instruction "Pricing questions, be friendly" still uses "only $63" as the example (live, read 10/15). Prompt block from the Oct 13 plan not applied | OpenCX search |
| Chat nudges live | 3-min nudge ON, 2h nudge ON (fixed text "Still thinking it over?"), 20h last-call ON; day 1/3/5/7/12 drip OFF | list_workflows |
| Quiz code | quiz-funnels branch, 219 tests pass; my worktree quiz-npb has one commit (below). NPB brand still enabled=false, quiz_enabled unset. Nothing deployed | repo |
| SMS | Cannot text: toll-free sender rejected 6/29, number released 9/24. Nurture is email only | prior audit, not re-checked |
| Party Queen capacity | Michael's call 2026-10-09: 22 shared seats / 26 private. Quiz and chat drafts use 22. David to confirm | Booze Removal file |

## 1. OpenCX: five price replies (cards c01 + c17), DRAFTS created

Five training scenarios exist in the NPB OpenCX workspace, folder Sales & Booking, every one `is_draft: true` (unpublished, Nolan does not see them). Titles start with `[FUNNEL LAB DRAFT, DO NOT PUBLISH]`.

| Version | Scenario id | Created |
|:-|:-|:-|
| A, straight shooter (control) | ef4250f7-7ce1-43d5-acc3-e5b8efdb1d1b | yes, draft |
| B, group math then the cell | **not created**: the permission layer refused it twice. Text is below, paste by hand or allow the tool | no |
| C, wisecrack | a279766e-f63d-4417-88b6-8fb69f5fb93c | yes, draft |
| D, decoy (three options) | 0ba17799-a7b3-471a-bec4-398fadd74a31 | yes, draft |
| E, real seats left + crowd proof | c60977a8-2804-4c55-b981-ca650e64b779 | yes, draft |

What each one does when published: on a first or second message that asks the price, Nolan answers with that version's template (price in sentence one), the live prices from FareHarbor 2026-10-13, one question back. E runs the FareHarbor availability action first and falls back to A if the check fails, so it never fakes a seat count.

**How the knockout runs (when David says go):** one version published per day, the other four unpublished. A small runner on mbp-2 (not built yet) publishes the day's version at 6am CT in a rotation that shifts one day each week, logs which version each day got, and the read is "chats that day ending with a booking link clicked or a contact captured". Week 4: drop the bottom two. Week 8: drop one more. Then head to head. Without the runner, a person flips publish/unpublish by hand each morning, which will not hold for 8 weeks.

**Before any of them runs:** fix "only $63" in the live Pricing instruction (question 2), decide the phone ask for B (question 3), confirm Party Queen capacity (question 1).

### Version B text (not yet in OpenCX)

> Seats are $59 a person. Bigger crews usually save by taking the whole boat: the Party Queen is $900, about $41 a head for 22. How many of you, and what's the occasion? Drop your cell and I'll text the link plus a summary you can paste straight into the group chat.

Size known: do the math for their number. Under 6: seats only. 6 to 18: Bayou Boogie $800. 19 to 22: Party Queen $900. 23 to 25: a Tiki $1,200. One ask per message; if they decline the cell, answer, send the link, end warm. Never promise a text time (no verified sender yet).

Conflict: three live instructions say "never ask for a phone number". B cannot run until that rule is lifted on B days or the ask becomes an email for the Group Chat Link.

## 2. Meta: birthday vs bachelorette (card c06), NOT created

The ad tool refused to create the campaign (permission layer). Also found: the Meta tool only builds image creatives, and this test needs the existing 9x16 video with a hook swap. So the shell can be built by tool once allowed, but the two ads must be duplicated from the Gator Collision ad in Ads Manager by hand. Spec:

| | Setting |
|:-|:-|
| Campaign | `NPB | TEST PAUSED | Birthday vs Bachelorette | Oct 2026`, Sales objective, PAUSED |
| Ad sets (2, both PAUSED) | Same targeting as Gator Collision: New Orleans +50 mi, 24 to 65, Nightlife interest, Advantage audience on. Optimize for Purchase, pixel 701301873334767. $20/day each, 14 to 21 days |
| Ads (2, PAUSED) | Same video as "NPB Gator Collision v1 9x16" (creative 3678636142274793). Only the primary text changes |
| Measure | CTR, cost per view_book_form, cost per purchase. Read at day 14 |

**Ad A, Birthday.** Primary text:

> Turning 30? Do it on a tiki boat with gators.
>
> BYOB, your playlist, and a captain who knows the bayou. Seven miles from the French Quarter, back before dinner.
>
> "We did this boat tour for my friends 55th bday!"
>
> $59 a seat, or the whole boat for your crew from $800. Pick a date and we'll see you at the dock.

Headline: `Birthdays on the bayou`

**Ad B, Bachelorette.** Primary text:

> The bachelorette everyone will still talk about.
>
> BYOB, your playlist, and a captain who knows the bayou. Seven miles from the French Quarter, back before dinner.
>
> "Would highly recommend this trip for any bachelorette!"
>
> $59 a seat, or the whole boat for your crew from $800. Pick a date and we'll see you at the dock.

Headline: `The bachelorette boat`

Both quotes are real review phrases (01 Customer Truth). Budget is new spend unless David carves it out of the $160/day Gator Collision test (my pick: carve it out, total spend does not move).

Ads Manager warning from Michael's 10/01 row: the primary text field corrupts when scripted. Type by hand, click into the field before Cmd+A.

## 3. Quiz (cards c18, c19, c20, c21)

Branch `quiz-npb` in `~/Projects/fh-lead-engine-quiz-npb` (worktree off quiz-funnels). One commit: the Bayou Bougie result no longer claims a decorations add-on (none is live; Add-On Menu lists a $40 decor package as an idea only). Previews rebuilt: `previews/quiz/npb-A.html`, `npb-B.html`. 219 tests pass. Not deployed, not merged.

Board picks that still need an engine change (shared files, outside this session's lane, handed to the hub):
- c19 = B (email unlocks the result). The engine's control is result_first and a draft test gives everyone the control. Needs a per-brand forced arm in `engine/experiments.json` or `experiments.py` so NPB serves email_first to 100% of visitors.
- c20 = A (help first). Already the control, so nothing changes, but the `nurture_npb` test should stay draft or be stopped with help_first as winner so it never flips on by accident.
- c21 = A (quiz popup). `engine/widget.js` only knows the guide popup. A quiz mode ("Not sure which boat? 30-second quiz" linking to /quiz) is a shared widget change for all brands.

Still blocking NPB go-live in the engine: `npb.enabled` is false, the quiz copy has one `[VERIFY add-on]` line in the day-2 email (only used by the offer_early arm David did not pick), and the FareHarbor header-script slot does not exist.

Popup copy for A, ready for the widget once it exists:
- Bar: `Not sure which boat? 30-second quiz`
- Headline: `Which boat fits your crew?`
- Sub: `Four taps. You get the boat, the per-person price and the dates, before we ask for anything.`
- Button: `Start the quiz`

## 4. FareHarbor header-script ask (card c03), DRAFT email, not sent

To: the FareHarbor account rep (memory says Kevin Schmitt is the account manager). From: info@nolapartybarges.com. Signed Jeffrey Chitek, Manager. Plain ASCII.

> Subject: Header script slot for nolapartybarges.com
>
> Hi Kevin,
>
> Quick ask on nolapartybarges.com. We want to run a small lead-capture script (one async script tag, ours, hosted on AWS) in the site header. The theme has no spot for us to add it ourselves.
>
> Could your team add this line to the site head, or point us at the field where we can?
>
> <script async src="https://zrnrjszada.execute-api.us-west-2.amazonaws.com/w.js?b=npb"></script>
>
> Same ask applies to our sister sites on your platform (New Orleans Kayak Swamp Tours, Houston Pedal Barge, Lone Star Kayak Tours, Austin Kayak Tours) once this one is in. Happy to send those separately.
>
> Thanks,
> Jeffrey Chitek
> Manager, NOLA Party Barge
> info@nolapartybarges.com

Note (from the HPB session, 2026-10-15): nolapartybarges.com runs the Complianz cookie-consent manager (Michael's 9/30 row), which can hold a script until the visitor consents. Ask the rep to add it as a functional (not marketing) script, or the popup never fires for people who ignore the banner.

Note: the script URL is the lead engine's API base. Verify the `w.js?b=npb` path is what the deployed engine serves before sending; the engine is not deployed with the NPB block on yet, so the tag would load nothing until it is.

## 5. Things I did not build, and why

- OpenCX nudge rewrites (2h, 20h, kill 3-min) from the Oct 13 capture play: not an approved board card, so not cloned.
- Card c02 and c05: no pick yet.
- Weather credit, tracking fix: parked.

## Open questions (one list, answer by number)

1. Party Queen capacity for the per-head math: 22 (chat, Coast Guard per the bot) or 26 (site, Michael's 10/09 call is 22 shared / 26 private)?
2. OK to change "only $63" to "only $59" in the live OpenCX Pricing instruction now? (Blocks every chat version.)
3. Chat version B asks for a cell. Lift the live "never ask for a phone number" rule on B days, or switch B's ask to an email for the Group Chat Link?
4. OK to build the daily rotation runner on mbp-2 for the chat knockout? It stays off until a separate go.
5. Meta test: (a) allow the campaign tool so I build the PAUSED shell and you duplicate the two ads by hand, or (b) Michael builds both ad sets in Ads Manager from section 2? And budget: carve $40/day out of Gator Collision, or add on top?
6. OK to send the FareHarbor header-script email in section 4 (from info@, signed Jeffrey)?
7. Quiz picks c19=B and c21=A need shared engine files (experiments.json, widget.js). Hand to the hub session, or OK for this session to edit those shared files in its worktree?
8. Decorations add-on: is there one, and what does it cost? (Quiz says "bring the decorations" until told otherwise.)
9. Kids: live FAQ says public trips 21+, kids 6+ on private boats only; the vault says kids welcome. Which is true?
10. "Still deciding?" email signer: a first name ("Jeff at NOLA Party Barge") or "the crew at NOLA Party Barge" (current)?
11. Cards c02 (where cold social lands) and c05 (how did you hear) still need a pick on the board.
12. Version B of the chat test could not be created by tool. Paste section 1's text into OpenCX as a draft yourself, or add a permission rule for `mcp__opencx-npb__create_training_scenario` and say so, and I will create it.
