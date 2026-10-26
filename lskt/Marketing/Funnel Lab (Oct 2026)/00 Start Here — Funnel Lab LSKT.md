*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for LSKT.*

# Funnel Lab: LSKT, start here

## What this is

The working copy of the cross-brand Funnel Lab (Oct 2026) for Lone Star Kayak Tours and Austin Kayak Tours: customer truth, live funnel baselines, A/B tests, quiz design and launch steps, split out of TheBrain so this brand can be worked on in its own session. Everything is a draft; nothing was sent, posted, deployed or changed on any site, ad account, FareHarbor, OpenCX or ActiveCampaign.

Splits are verbatim copies. The TheBrain files are the cross-brand hub; edit the working copy here and note changes you want carried back.

This folder covers both Lone Star Kayak Tours (LSKT) and Austin Kayak Tours (AKT), which reads as one Austin lane. The Austin Kayak Tours vault has a one-file pointer to here.

## CURRENT STATUS (verified 2026-10-15, LSKT session, first turn)

- Board re-read 2026-10-15: c02 cold social = no pick (waiting), c05 how-did-you-hear = no pick (waiting), c04 weather credit = parked, c15 bats vs beginners = both (approved, March 2027), quiz cards c18 both / c19 B / c20 A / c21 A.
- New files: [[50 Cold Social Meta Drafts — LSKT (paused spec)]] (exact paused build, nothing created in Meta because c02 has no pick) and [[51 Bats vs Beginners 2027 — LSKT (staged)]].
- Correction: the Lone Star Google listing did NOT stop getting reviews. Two listings exist; the live one at 200 E Riverside has 527 reviews, 4.9 avg, latest 2026-10-12. The lab's cache read the legacy listing (157 reviews, last 2024-07-23). Details in 30 and 01.
- Meta act_638850950128825: all campaigns paused since 2026-10-07. FareHarbor purchase events carry no fbc/fbp or hashed email, so Meta cannot attribute bookings. Read ad tests by FareHarbor `?ref=` tag until that is fixed.
- Google Ads Austin (Oct 8-14): about $467 spend, about $2,812 value, roughly 6x. Bat spend winds down about Oct 25; bat tour closes Oct 31.
- Live site conflicts (re-fetched 2026-10-15): Skyline page 20 N IH-35 vs 200 E Riverside everywhere else (and the Austin Kayak Tours Google listing sits at 7 East Ave 78701); arrival 15 min (/faq/) vs 30 min (/things-you-should-know/); cancel window 24h (/faq/) vs 48h (/things-you-should-know/); Paddle Board Bat Tour card $50 ages 5+ vs body $59 ages 6+.
- Bat season verified on the live bat tour page (updated June 2026): colony present roughly March to early November, peak June to August; tour sells March 1 to October 31. The quiz blurb already says this; the only open call is whether the quiz hides the bat result Nov 1 to Feb 28.
- Quiz engine: 219 tests pass on `quiz-funnels` (run 2026-10-15). LSKT quiz still holds [VERIFY] markers on the calm-paddle result (tour, price, quote), the paddleboard proof quote and the day-2 add-on, so it refuses to serve live until David answers the questions below.

## Board cards for LSKT

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
| c15 (04 card 15) | 2027: bats-first vs beginners-first | both | approved | (none) | (none) |

## Site and testing surface

FareHarbor WordPress sites with no GTM (lonestarkayaktours.com, austinkayaktours.com). Needs one FareHarbor header-script slot per site. austinkayaktours.com books through the Lone Star FareHarbor shortname, has no Meta pixel and no OpenCX. (03)

## Open questions for David (one list, verified 2026-10-15)

1. **Calm paddle result (quiz A and B):** which real product should it point to? Options: Austin City Skyline Tour ($50, 2 hours, guided) or a kayak rental ($20/hr single, $25/hr tandem, no guide). The quiz refuses to go live until this is filled. My pick: the Skyline Tour, with the rental as a one-line alternative in the blurb.
2. **Meeting address:** the Skyline page says 20 N IH-35, every other page and the Lone Star Google listing say 200 E Riverside, and the Austin Kayak Tours Google listing sits at 7 East Ave 78701. Is there a second launch site, or are two of these wrong? Who fixes the page (FareHarbor theme)?
3. **Arrival and cancel windows:** /faq/ says 15 minutes early and 24-hour cancellation; /things-you-should-know/ says 30 minutes and 48 hours. Which is policy?
4. **Paddle Board Bat Tour price:** card says $50 ages 5+, page body says $59 ages 6+. Which is right?
5. **Bat season in the quiz:** verified March 1 to October 31 for the tour, bats present roughly March to early November. Hide the bat result from November 1 to February 28, or show it with "opens March 1"?
6. **Google listings:** two Lone Star Kayak Tours listings exist. The live one (200 E Riverside) has 527 reviews. The legacy one (157 reviews, last 2024, no address) still shows in the account. Merge or close the legacy one? Also, the quiz proof quotes can now come from the live Lone Star listing instead of Austin Kayak Tours.
7. **Card c02 cold social:** no pick on the board. A, B, or both? Budget $10/day total carve-out (my pick) or $10/day per arm new money? Skyline landing for a November run, or bats for the 16 days left?
8. **FareHarbor Meta pixel fix:** ask FareHarbor to enable advanced matching and pass fbc/fbp? Until then Meta shows 0 purchases for any ad. Connor would send the ask.
9. **Card c05 how did you hear:** no pick on the board. Optional checkout field (A), confirmation-email tap links (B), or both?
10. **Header-script slot:** OK to email the FareHarbor rep for one header line on lonestarkayaktours.com and austinkayaktours.com? One ask covers the popup, the quiz and on-site tests.
11. **Guide names in the nurture:** Tristan is named 27 times in the 50 most recent Lone Star reviews, Julian and Greg follow. OK to name them in the "meet your guide" email?
12. **Day-2 add-on (card c20 is A, help first, so this only matters if B is ever tested):** what can LSKT give that costs little? A photo, a dry bag?
13. **Still-deciding email sender:** OK to come from a first name at Lone Star (never David's)? Whose?
14. **Low-star pattern worth a reply:** Sep and Oct 2026 one- and two-star reviews on the live listing mention the paid parking lot surprise, one guide for 10 to 12 boats, and no red light or thin narration on a bat tour. Want these addressed on the site FAQ and in the dock brief?

## Files in this folder

- [[01 Customer Truth — LSKT]]: who buys, what they ask first, what stops them, real phrases (reviews and chats)
- [[02 Funnel Baseline — LSKT]]: live GA4 / Ads / Meta numbers, last 30 days vs last year, biggest leak
- [[04 A-B Tests — LSKT]]: every A/B test card that names this brand, with David's board picks
- [[10 Weather Credit — LSKT]]: weather credit vs refund, both versions plus a live test
- [[11 How Did You Hear About Us — LSKT]]: how did you hear about us, two versions
- [[20 Abandoned Bookings — LSKT]]: what FareHarbor's abandoned-cart email catches
- [[30 Quiz — LSKT]]: this brand's quiz A and B, the four decisions built both ways, nurture sequence, fact conflicts
- [[40 Launch Steps — LSKT]]: what each approved card takes to launch, who, and what spends money

## Shared links

- Decision board: https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY
- Quiz code: `~/Projects/fh-lead-engine-quiz`, branch `quiz-funnels`. This brand's files: `engine/quiz/lskt.json`, `engine/copy/lskt_quiz.json`, previews `previews/quiz/lskt-A.html` and `previews/quiz/lskt-B.html`. (Quiz codes: npb, nkst, dckt, bbk, lskt, hpb, ebb.)
- Cross-brand hub (shared method docs): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` in the TheBrain vault. Start with `03 Testing Infrastructure — What Can Split Today.md` and the shared design section of `30 Quiz Funnels + Nurture — Design.md`; file `05 Per-Brand Folders.md` lists all seven brand folders.
- Code for variant assignment: `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (not merged, not deployed).
