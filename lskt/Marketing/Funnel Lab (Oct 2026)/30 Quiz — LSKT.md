*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for LSKT.*

# Quiz: LSKT (split from file 30, plus fact conflicts from file 31)

Shared design (problem, flow diagram, what already exists) is in the hub: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/30 Quiz Funnels + Nurture — Design.md`. The sections below are what this brand needs to stand alone.

## Board picks on the four quiz decisions (data read 2026-10-15)

| Card | Decision | Pick | Note |
|:-|:-|:-|:-|
| c18 | Decision 1: quiz style | both | (none) |
| c19 | Decision 2: email gate | B | (none) |
| c20 | Decision 3: nurture | A | (none) |
| c21 | Decision 4: popup | A | (none) |

## Per-brand quiz: LSKT

Questions are 4-5 taps, one per screen, phone first. Every option maps to a tag. Anything not verified is marked [VERIFY] and the engine refuses to go live with a [VERIFY] in it.

### LSKT + AKT, Austin

**Quiz A: "Which Austin paddle?"**
1. Ever kayaked or paddleboarded? 2. Who's coming? 3. Pick one: *The bats at sunset / Lady Bird Lake skyline / Just a calm paddle / Paddleboard instead* 4. When?
Result answers "what's included" up front (22% of LSKT chats ask what the tour even is). Bats only shown in bat season [VERIFY months].

**Quiz B: "What kind of Austin weekend are you?"** *Bat Night / Lake Day / The Calm One / Keep Austin Weird*

## The decisions, built both ways

### Decision 1: what kind of quiz

| | **A. "Find your tour"** | **B. "What kind of ___ are you?"** |
|:-|:-|:-|
| What it is | Practical matcher. Questions a guide would ask, result is a tour. | Personality quiz. Same data underneath, result is a fun identity plus the tour that fits it. |
| Wins on | Lead quality, booking rate | Completion rate, shares, cheap cold traffic |
| Risk | Feels like a form | Attracts browsers who never book |
| Example (NKST) | "Which swamp tour fits you?" | "What kind of swamp creature are you?" |

**Run both.** Cold social goes 50/50 to A and B. Measure completion, save rate, and bookings per 100 starts.

### Decision 2: when we ask for the email

| | **A. Result first, then save** | **B. Email unlocks the result** |
|:-|:-|:-|
| How | Show the tour and price, then "Want this sent to you / your group chat?" | "Where should we send your result?" before the reveal |
| Wins on | Trust, completion | Capture rate |
| Note | The NPB planner already works this way | Classic quiz-funnel play, captures more but annoys some |

**Run both** as a split inside each quiz. My bet: A for NPB (planners share), B for personality quizzes (people want to see their type).

### Decision 3: how the nurture sells

| | **A. Help first** | **B. Small offer early** |
|:-|:-|:-|
| Days 1-4 | Guide intro, their fear answered, where we meet, what to bring | Same, plus a small non-cash add-on on day 2 (e.g. NPB: free cooler of ice; NKST: free dry bag rental [VERIFY what's real]) |
| First ask | Day 5 | Day 2 |
| Wins on | Brand, margin | Speed to booking |

**Run both.** No percentage discounts in either. Add-ons protect price and still feel like a gift.

### Decision 4: the popup (David's note on card 3: "do we do a pop up?")

Yes, and the popup is the quiz's front door.

| | **A. Quiz popup** | **B. Offer popup** |
|:-|:-|:-|
| Copy | "Not sure which tour? 30-second quiz." | Today's HPB style: "$25 off your first trip" |
| Trigger | 20 seconds on page or exit intent on mobile scroll-up | Same |

**Run both.** Needs the FareHarbor header-script slot on NPB, NKST, HPB, LSKT, AKT. DCKT and BBK can use GTM. E&E can use the Squarespace footer.

## The nurture sequence (same skeleton every brand, copy per brand)

Timed off the "when" answer. A trip 3 days out gets a compressed version; "just looking" gets a slow monthly one.

| # | When | Job | Branches on |
|:-|:-|:-|:-|
| 1 | Instant | Your result, the tour, the price, the Book link, one guide photo | quiz result |
| 2 | +1 day | Kill their specific fear (the answer they gave) | fear tag |
| 3 | +2 days | Proof from someone like them (birthday crew, first-timers, families, couples) | who / occasion |
| 4 | +3 days | Meet your guide (55-70% of reviews name a guide; people book people) | brand |
| 5 | +4 days | The practical stuff: where we meet, parking, what to bring (the #1 organic question at NKST) | brand |
| 6 | +5 days, or 7 days before trip | Real availability for their date from `/avail`. Only true numbers. | when |
| 7 | +8 days | Last nudge, then drop to monthly | |
| S | 24h after a Book tap with no booking | "Still deciding?" one line, the link back, a human reply-to | Book tap, no `/booked` |

SMS only where there is consent AND a verified sender. NPB can't text until the toll-free sender is re-verified (rejected 6/29). HPB, LSKT have numbers in progress per the rollout notes [VERIFY].

## Fact conflicts for LSKT (rows from file 31)

> **CURRENT STATUS (verified 2026-10-15, live GBP API):** the "Lone Star listing has no reviews after 2024" row below is WRONG. There are two Lone Star Kayak Tours Google listings. The lab read the legacy one (`locations/11383026800789938857`, no storefront address, 157 reviews, last review 2024-07-23). The real listing at 200 E Riverside (`locations/3658611154412377613`) has 527 reviews, 4.9 average, latest 2026-10-12; its 50 most recent are all from 2026 and name Tristan 27 times. Quiz proof lines can quote this listing. Two more live-site conflicts found 2026-10-15: cancel window is 24 hours on /faq/ but 48 hours on /things-you-should-know/; the Skyline page still shows 20 N IH-35 while the Austin Kayak Tours Google listing sits at 7 East Ave 78701 (a third address). The table below is history.



*Found while sourcing every quiz fact from vault docs and the live sites. Live site wins in the quizzes unless marked. Several of these are wrong in front of customers today, not just in the quiz.*

| Brand | What | Says one thing | Says another | In the quiz now | Fix where |
|:-|:-|:-|:-|:-|:-|
| LSKT | Meeting address | Skyline page: 20 N IH-35 | Footer, FAQ, vault: 200 E Riverside | 200 E Riverside | Site |
| LSKT | Arrival | Live FAQ: 15 min | "Things you should know": 30 min | "15 to 30 minutes" | Site |
| LSKT | Paddleboard bat tour | Card: $50 | FAQ text: $59, ages 6+ | Not used | Site |
| LSKT | Google reviews | Lone Star listing has no reviews after 2024 | Austin Kayak Tours listing has them | AKT quotes | Worth a look at the LSKT listing |

## Still-open questions (from file 31 and file 30)

From file 31, "Still David's calls before the quizzes can go live" (original numbering kept):

1. The add-on for each brand's "small offer early" email (cooler of ice, dry bag, towel... what's real?).

From file 30, Questions for David (shared by all brands):

1. Which brand goes first? My pick: NPB (volume, and the planner is already built), then NKST, then E&E.
2. Decision 3 needs real add-ons for "small offer early." What can each brand give that costs little? (Ice, a dry bag, a photo, a playlist request, a towel?)
3. OK for the "still deciding?" email to come from a person's first name at the business (e.g. "Jeff at NOLA Party Barge")? It reads warmer than the brand. Never David's name.
