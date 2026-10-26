*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for DCKT.*

# Funnel Lab: DCKT, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for Door County Kayak Tours: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

DCKT has its own weather and cancellation analysis already: `DCKT — 2026 Cancellation Analysis.md` in this vault. File 10 here is just a pointer to it.

## Board cards for DCKT

Board data read 2026-10-15 from the Funnel Lab Board. 'none yet (waiting)' means David has not picked. Status values are as on the board.

| Card id | Title | David's pick | Status | David's note | Claude's reply |
|:-|:-|:-|:-|:-|:-|
| c18 (file 30, decision 1) | Quiz style: find-your-tour vs personality [All brands] | both | approved | (none) | (none) |
| c19 (file 30, decision 2) | Quiz: when we ask for the email [All brands] | B | approved | (none) | (none) |
| c20 (file 30, decision 3) | Nurture: help first vs small offer early [All brands] | A | approved | (none) | (none) |
| c21 (file 30, decision 4) | Popup: quiz vs offer [All brands] | A | approved | (none) | (none) |
| c03 (04 card 3) | How we'll run on-site and email tests [All brands] | both | approved | do we do a pop up? | Yes. The popup becomes the quiz's front door: 'Not sure which tour? 30-second quiz' tested against today's '$25 off' popup. See the new popup card. It still needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT; DCKT and BBK use GTM, E&E the Squarespace footer. |
| c05 (04 card 5) | How did you hear about us? [All brands] | none yet (waiting) | waiting | (none) | (none) |
| c14 (04 card 14) | 2027: family-first vs Cave Point-first | both | approved | (none) | (none) |

## Site and testing surface

FareHarbor WordPress with GTM (doorcountykayaktours.com, GTM-PPSHWZB). GTM holds no Custom HTML tags yet; who has publish access is unverified. The DCKT ride quiz (dckt-quiz) is the one live A/B. (03)

## Live surfaces check (verified 2026-10-15)

- Google listing "Door County Kayak Tours": 1,011 reviews, 4.9 average (GBP API, live). The lab's Oct 14 cache said 1,015 / 973 five-star. "1,000+" is safe copy.
- Vault docs: every "800+" fixed to "1,000+" on 2026-10-15 (Cedar identity doc, Brand Story, Journey Map, Master OS, Sales Process, 6 staged blog drafts, 1 ad-research log).
- Live website: all 121 URLs in the page, activity and post sitemaps scanned (visible text, JSON-LD, meta, alt). None says "800+" reviews. No review count appears on the site at all.
- Live Cedar bot (OpenCX AI profile, the prompt customers actually get): still says "800+ reviews" in 12 places. Same prompt also sells a "Sunset Tour" (15 mentions; DCKT runs no sunset kayak tour), says "ACA-trained guides" (not true, see memory), quotes $59 pricing, and says kids "as young as 4" in one spot and "as young as 5" in the others. Changing it is a live bot change: needs David's OK.
- Live site kid age: "All Ages" on Cave Point 2h and the home page tiles; "Ages: 4+" on the half-day pages. No weight limit on any kayak page. E-bike page says "Young adults ages 14-18" only.

## David's answers (2026-10-16) and what is still open

Answered:
1. Weight limit: depends on the boat. Fleet ratings looked up 2026-10-16: Perception Rambler 13.5T 550 lb, Tribe 13.5T 500 lb, Tribe 11.5 single 350 lb. A Rambler can be paddled solo, but a very heavy guest is a re-entry hazard even when the boat can carry them. Numbers used everywhere: tandem 500 combined, single 285. Confirmed by David 2026-10-16.
2. Kids: 4 and up on all kayak tours. Bike trailers (rentals and tours): 2 and up.
3. Dogs: all tours, as long as it is calm.
4. Sunset: dropped from both quizzes and from Cedar. No sunset kayak tour exists.
8. Cedar: David said "just publish." Corrected prompt published 2026-10-16 (1,000+ reviews, no sunset tour, no ACA claim, current pricing, kids 4+, dogs when calm, half-day upsell instead of sunset, photo package removed, Schauer Park removed, tandem 500 lb). The vault copy `DCKT Agent Identity — Cedar.md` got the same edits.
9. GTM: moot. David wants a new static Astro site with the same URL layout, swapped the week of Oct 19. Own session started 2026-10-16 (see Shared links).
10. "Still deciding?" sender: sign as "Cedar at Door County Kayak Tours." (The question was only the from-name and sign-off on the nurture emails.)
11. Door Bluff: 2 hours (live). Meeting point: Garrett Bay boat launch, 1310 Garrett Bay Rd, Ellison Bay (David confirmed keep 1310, 2026-10-16).
12. Ride quiz: keep both, learn from both.

Still open:
5-6. Credit policy decisions 1 and 2: PARKED 2026-10-16. David: guests pick a weather option at FareHarbor checkout (4 options, live on the Cave Point page), usually move the tour once, then get a refund. The credit-by-default draft is reference only. Next step: pull the option mix from the FareHarbor bookings custom-field column and nudge toward option 4.
7. Resolved 2026-10-16: the 3 (actually 4) weather options are already installed on the FareHarbor checkout.
10b. How did you hear about us: David picked A (optional dropdown at checkout) on 2026-10-16. Launch step: Claude writes the field spec (name, options), someone with FareHarbor dashboard access adds it to the 39 items; board card c05 pick still needs David to click it on the board.
11b. Resolved: keep 1310 Garrett Bay Rd (David, 2026-10-16).
14. Resolved: tandem 500 lb, single 285 lb (David, 2026-10-16).
15. The OpenCX draft had an unpublished suggestion dated earlier ("Owner update: allow 3-year-olds on kayak tours"). Published version uses 4. Was 3 ever the intent?
16. Cancellation policy: David's call, already set in FareHarbor and on the site. Do not raise the 24h/48h question again (David, 2026-10-19). Leave Cedar's cancellation lines as they are unless David asks.

## Files in this folder

- [[01 Customer Truth — DCKT]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — DCKT]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — DCKT]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — DCKT]]: pointer to DCKT's own cancellation analysis
- [[11 How Did You Hear About Us — DCKT]]: how did you hear about us, two versions
- [[20 Abandoned Bookings — DCKT]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — DCKT]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — DCKT]]: what each approved card takes to launch, who, and what spends money

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- DCKT quiz worktree: `~/Projects/fh-lead-engine-quiz-dckt` (branch `quiz-dckt`), edited 2026-10-16 with David's facts; not committed, not deployed.
- Website rebuild (Astro, same URL layout): its own session, started 2026-10-16; working folder `Marketing/Website Rebuild 2026/` and code at `~/Projects/dckt-site`.
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/dckt.json`, `engine/copy/dckt_quiz.json`, previews `previews/quiz/dckt-A.html` and `previews/quiz/dckt-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
