# Quiz funnels + nurture: warm the lead before we ask for the booking

*Drafted 2026-10-14 by David's Claude after David's ask: "our leads are too cold and quick to choose, use funnel quizzes?" DRAFT. Nothing live.*

## The problem in one line

Cold traffic hits a FareHarbor checkout, doesn't book, and leaves no name. NPB paid social: 10,966 sessions, 8 purchases, 0 emails kept. We never get a second conversation.

## The fix

A 30-second quiz is the second conversation. It asks the questions shoppers are already asking us (price, who's it for, can beginners do it, where do we meet), gives a real answer and the right tour, then saves the result to their email or phone. From there a nurture sequence, timed to their trip date, answers their specific fear before it asks again.

```
Ad / bio link / popup / chat bot
        |
   Quiz (4-5 taps)  ---- tags: who, occasion, experience, fear, when
        |
   Result page: the right tour + price + their fear answered
        |
   Save it: email (and cell with its own unchecked SMS box)
        |
   Nurture drip (branches on tags, timed to trip date)
        |                         \
   Book (link carries ?ref=q-<id>)   Clicked Book, no booking in 24h
        |                              -> "still deciding?" branch (our own abandoned-booking flow)
   /booked stops the drip
```

## What already exists (so we're not starting over)

| Piece | Where | State |
|:-|:-|:-|
| NPB Group Chat Link: 3 taps -> boat + price -> save -> shareable crew page | `fh-lead-engine-capture` branch `capture-v2`, `engine/plan.py` | Built, 128 tests, not deployed |
| Trip-date drip with per-brand copy JSON | same branch, `engine/guide.py` + `engine/copy/npb_guide.json` | Built for NPB only |
| `/booked` (stops drips when a lead books), `/t` tap links, `/avail` live seats, consent, CAPI + GA4 events | same branch | Built |
| Popup widget `w.js` | engine | On no site yet; needs a FareHarbor header-script slot |
| Variant assignment for A/B tests | branch `ab-variants` (built tonight) | Built, 36 tests |
| DCKT ride quiz | live on doorcountykayaktours.com | Already running a 50/50 test |

So the quiz is the NPB planner generalized to every brand, plus a second quiz style to test against it.

---

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

---

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

---

## Per-brand quizzes

Questions are 4-5 taps, one per screen, phone first. Every option maps to a tag. Anything not verified is marked [VERIFY] and the engine refuses to go live with a [VERIFY] in it.

### NPB, NOLA Party Barge

**Quiz A** is the existing planner (how many / what are we celebrating / roughly when) plus one question:
4. What would make it perfect? *Music and dancing / Seeing gators / Chill and scenic / All of it*
Result: seats or the right whole boat with per-head math, then save + share to group chat.

**Quiz B: "What's your crew's party boat personality?"**
1. Your crew walks into a bar. Who orders? *The birthday person, obviously / Whoever's holding the group chat hostage / Nobody, we BYOB / We're still parking*
2. Pick a soundtrack. *Brass band / 2000s throwbacks / Zydeco / Whatever the captain plays*
3. Gator shows up. You... *Film it / Feed it a marshmallow (the captain does that) / Hide behind the bride / Name it*
4. How many in the crew? *2-6 / 7-14 / 15-24 / 25+*
5. When? *This month / Next 1-3 months / Later / Just looking*

Results:
- **The Second Line** (big crew, music): whole boat, Freaky or Twerkin' Tiki
- **The Birthday Takeover** (birthday + 7-24): Bayou Boogie or Party Queen with per-head math
- **The Bayou Bougie** (bachelorette or vibes): private tiki, decorations add-on
- **The Small but Mighty** (2-6): seats at $59, "you'll make friends on board"

Proof lines: "We did this boat tour for my friends 55th bday!" / "Our captain fed 2 different alligators marshmallows FROM HIS HAND." / "It rained some but it made it that much more fun!"

### NKST, New Orleans Kayak Swamp Tours

**Quiz A: "Which swamp tour fits you?"**
1. Ever kayaked? *Never / A couple times / I'm good at it*
2. Who's coming? *Just me / Me + partner / Friends / Family with kids*
3. You live here or visiting? *I live in the New Orleans area / Visiting*
4. What do you most want? *Gators / Birds and owls / Total quiet in the cypress / The history and stories*
5. When? *This weekend / This month / Later / Just looking*

Result: the right tour [VERIFY lineup: Manchac 2-hour, sunset, extended], with "where we meet + how to get there + shuttle from the Quarter [VERIFY]" right on the result (top question, 29% of first chats). Never-kayaked gets: "Highly recommend this tour, even for beginners!" Locals get: "You've lived next to this swamp your whole life. Time to meet it."

**Quiz B: "What kind of swamp creature are you?"**
- **Barred Owl:** quiet, watching everything. Sunset tour.
- **Sunbathing Gator:** here to chill. Classic 2-hour.
- **Great Egret:** came for the photos. Morning light tour.
- **River Otter:** can't sit still, wants the longest paddle. Extended tour.

Nurture fear answer (never kayaked): "Was definitely apprehensive of kayaking through the swamp, but PLEASE don't be!" plus stable sit-on-tops, life jacket on the whole time, guide in front.

### DCKT, Door County Kayak Tours (season opens 2027; build now, launch spring)

**Quiz A: "Which Door County trip fits your crew?"**
1. Who's coming? *Adults only / Kids under 12 / Teens / The dog too*
2. Paddling experience? *First time / Some / Lots*
3. Pick the view. *Cave Point cliffs and caves / Sunset / Shipwreck history / Rather ride an e-bike*
4. When are you up? *Summer / Fall / Not sure*

Result shows the real kid age minimum, pet rule and weight limit [VERIFY all three; 24% of first questions are about these]. Cave Point named in 20% of reviews leads the cliffs result.

**Quiz B: "What's your Door County summer?"** *The Cliff Jumper / The Sunset Chaser / The Shipwreck Nerd / The Family Admiral*

Note: the live DCKT ride quiz already runs a 50/50. Fold its winner into Quiz A instead of competing with it.

### BBK, Buffalo Bayou Kayak

**Quiz A: "Find your Buffalo Bayou paddle"**
1. Who's coming? *Date / Friends / Family / Solo*
2. Ever kayaked? *Never / Some / Lots*
3. Pick one. *Downtown skyline / The bat colony at Waugh Bridge / Sunset / Houston history*
4. Live in Houston or visiting?

Result includes the honest line (card 13, approved both ways, so this result page is variant A of that test): "This is a working urban bayou in the middle of Houston. The water's brown, the skyline's huge, and the herons don't mind." Couples are the top segment (10%), so the date result leads with "Totally different view of the city from the water!"

**Quiz B: "What's your Houston after-dark personality?"** *The Skyline Romantic / The Bat Watcher / The Bayou Historian / The First-Timer Who Surprised Everyone*

### LSKT + AKT, Austin

**Quiz A: "Which Austin paddle?"**
1. Ever kayaked or paddleboarded? 2. Who's coming? 3. Pick one: *The bats at sunset / Lady Bird Lake skyline / Just a calm paddle / Paddleboard instead* 4. When?
Result answers "what's included" up front (22% of LSKT chats ask what the tour even is). Bats only shown in bat season [VERIFY months].

**Quiz B: "What kind of Austin weekend are you?"** *Bat Night / Lake Day / The Calm One / Keep Austin Weird*

### HPB, Houston Pedal Barge

**Quiz A: "Plan your Houston party barge"** (same skeleton as NPB): how many / occasion / when / vibe.
Result puts the weather and refund policy in plain words right on the page. 17 of HPB's 19 low-star reviews are cancel or refund complaints, so the fear question is answered before they pay, not after.

### E&E, Ebb & Ember (Portland)

**Quiz A: "Find your session"**
1. Who's coming? *Just me / A date / Friends / A group or celebration*
2. Sauna experience? *Never / Sometimes / Every week*
3. The cold part? *Straight off the deck into the river / A cold rinse / I'll watch*
4. What's it for? *Time with friends / Date night / A reset / Celebrating something*
5. When? *Weeknight / Weekend / Not sure*

Result: social session or private sauna [VERIFY lineup and prices], plus getting here, parking and what to bring (what reviewers volunteer most). Proof: "Such a perfect way to end a river day." / "I was proud that my group all braved jumping into the river."

**Quiz B: "What's your sauna temperature?"**
- **The Polar Plunger:** deck to river, no hesitation
- **The Slow Burn:** top bench, long rounds
- **The Social Steam:** here for the conversation
- **The First Timer:** "I can't wait to go again and want to bring all my friends!"

Rules: never medical claims, never "wood-fired", never "a float", always "Ebb & Ember".

---

## Abandoned bookings, plainly (David's second question)

**What FareHarbor catches today (verified 2026-10-14, file 20).** The abandoned-cart email is on for all six FareHarbor brands: NPB and NKST since 9/25, BBK, HPB and LSKT since 10/8, DCKT since at least June. Online cart went live the same days. **Recovered bookings since then: zero at every brand** (NPB 196 online bookings in the window, NKST 73, LSKT 50, BBK 22, HPB 9). DCKT recovered 2 all of 2026 ($395). The windows are short (6 to 19 days), so re-check around 11/15, but the ceiling is low: one email, 2 hours after drop-off, not editable, only if they typed an email, and FareHarbor shows no count of emails sent.

**What it can't do.** One email, no follow-up, no text, no "who left" list we can see. Checkout is an iframe on fareharbor.com, so our own site never learns who started checkout.

**What closes the gap:**
1. **Capture before checkout.** The quiz (and popup) gets the email first. Then a Book tap with no booking within 24 hours is an abandoned booking we know about, and our "still deciding?" branch can follow up.
2. **Tag every booking link** with `?ref=q-<lead id>` so FareHarbor reports show which lead booked. That feeds `/booked` and stops the drip.
3. **Retarget the anonymous ones.** GA4 audience "view_book_form, no purchase in 7 days" synced to Google Ads, and Meta InitiateCheckout-no-Purchase. Works without any email. (Card 16 tracking fix is parked, so NKST/HPB audiences will be thin until it's done.)

---

## What gets built tonight (no deploy)

On a new branch `quiz-funnels` cut from `capture-v2`:
- `/quiz?b=<brand>&s=<A|B>`: one generic engine, quiz content in `engine/quiz/<brand>.json`
- Gate variant (result-first vs email-first) via the ab-variants experiment code
- Tags written to the lead, picked up by the guide drip
- Book links carry `ref=q-<id>`; Book taps logged; "still deciding?" step 24h after a tap without `/booked`
- `[VERIFY]` blocks a quiz from going live
- Static clickable previews of every brand's Quiz A and B for David (no backend)

## Questions for David

1. Which brand goes first? My pick: NPB (volume, and the planner is already built), then NKST, then E&E.
2. Decision 3 needs real add-ons for "small offer early." What can each brand give that costs little? (Ice, a dry bag, a photo, a playlist request, a towel?)
3. OK for the "still deciding?" email to come from a person's first name at the business (e.g. "Jeff at NOLA Party Barge")? It reads warmer than the brand. Never David's name.
