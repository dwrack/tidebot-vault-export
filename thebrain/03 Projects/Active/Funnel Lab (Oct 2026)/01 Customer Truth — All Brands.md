# Customer Truth: All Brands (Funnel Lab, Oct 14 2026)

Built from raw Google reviews and OpenCX chat transcripts. Counts are real. Nothing was sent, posted or changed anywhere.

## Top table

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| NPB (NOLA Party Barge) | 2,850 / 3,944 | Friends celebrating, 12.5% of reviews. Top named occasion is birthday, 6.9% (bachelorette 6.0%) | "How much?" 52% of first questions (201 shopper chats) | Price and group fit. Price comes up in 62% of chats | 32% of reviews name a captain. "Worth every penny, the captain friendly and knowledgeable." |
| NKST (Swamp Tours) | 1,303 / 1,426 | Friends 6.6%, couples 5.6%. Visitors 13.7% vs locals 2.2% | "Where do we meet?" 29% of first questions (58 organic chats) | Getting to the swamp. Location or pickup in 43% of chats | 55% of reviews name a guide. "Highly recommend this tour, even for beginners!" |
| DCKT (Door County) | 912 / 1,015 | Families with kids, 7.2% (11.5% in last 12 months) | Kids, age, pets, 24% of first questions (110 shopper chats) | Can my kids, dog or heavier guest come. 42% of chats | 20% of reviews name Cave Point. "Great experience for the whole family!" |
| E&E (Portland floating sauna) | 115 / 125 | Friend groups 14.8%, couples 7.8% | No chat workspace exists. Proxy: how to get there and park, 17% of reviews | Thin. River current safety (3 reviews), day-of access (20 mention it) | 95.2% five-star in its first year. "Such a perfect way to end a river day." |
| LSKT + AKT (Austin) | 242 / 301 | Families 9.5%, friends 8.3%, couples 6.6% | "How much?" 26% (LSKT chats, 73 shoppers) | Beginner fit and what is included (22% ask what the tour is) | Bats are named in 31% of reviews. "The bats were amazing, a completely unique, must-do experience!" |
| HPB (Houston Pedal Barge) | 784 / 983 | Friend groups 18.0% (31% of the last 35 reviews) | "How much?" 27% (37 shopper chats, thin) | Weather cancels and slow refunds. 17 of 19 low-star reviews | 43% of reviews name a captain. "This is a must do when you're in Houston." |
| BBK (Buffalo Bayou) | 570 / 597 | Couples 10.0%, family 8.8%, friends 7.7% | Too thin. 8 shopper chats, 3 asked price | Dirty water. 14 of 27 low-star reviews, 6.7% of all | 70% of reviews name a guide. "Totally different view of the city from the water!" |

Total corpus: 10,900 reviews across 24 Google listings (18 brand keys), 8,658 with text. 981 OpenCX sessions across 6 workspaces.

## How to read this (method and limits)

- **Reviews**: GBP cache pulled Oct 14 2026. Percentages are of reviews with text. A review can match several segments. Matching is keyword regex, so treat every % as a floor, not a census.
- **Thin text**: NPB median review is 15 words. Only 24% of NPB reviews name a party type at all. HPB, DCKT and Austin are similar (17 to 28%). "Segment %" means "of all reviews", and I also give how many named any party type.
- **NPB skew**: 2,211 of 3,944 NPB reviews came in 2024 alone (a review-request push). Last 12 months is only 127 NPB reviews with text. Recent splits are flagged with n.
- **Chats**: OpenCX transcripts cover Apr 20 to Oct 6 2026. I removed spam (17 LSKT, 11 across DCKT, HPB and NPB), job seekers, post-booking issues and empty sessions before counting "shopper" questions.
- **No click data exists in the cache.** "Ended without a booking link or contact" is a proxy: no booking URL sent by the AI and no email or phone given by the shopper. A shopper could still have booked on their own.
- **Sources missing**: E&E, AKT and all sibling brands have no OpenCX workspace in the cache. Their question data is a review proxy and is labeled that way.
- **Guide-name shares** are first-name matches against names found in the reviews. Treat as an upper bound.
- **Austin**: LSKT reviews stop Jul 2024 and AKT starts Mar 2024. Treated as one Austin lane. The LSKT chat workspace is the only Austin chat source.
- Methods and scripts: `/private/tmp/claude-501/ct-scripts/` (rev.py, chatrun2.py, extras.py).

## Cross-brand patterns worth knowing first

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Almost nobody writes about fear | "Nervous / scared / first time kayaking" language: NKST 3.1%, DCKT 2.7%, BBK 4.2%, NPB 0.6%, HPB 0.5%. Beginners are a bigger group (BBK 9.1%, Austin 9.9%) than the fearful |
| Price is rarely mentioned in reviews, constantly in chats | Reviews mentioning price: NPB 2.8%, DCKT 2.7%, NKST 6.8%. Chats mentioning price: NPB 62%, LSKT 33%, NKST 28%, HPB 32%, DCKT 21% |
| Reviews skew visitors, not locals | Tourist language vs local language: NPB 7.2% vs 0.2%, NKST 13.7% vs 2.2%, DCKT 4.1% vs 0.3%. Exception: E&E talks like a local product (Portland mentioned in 21%, tourists 3.5%) |
| Low-star reviews are about operations, not the experience | Cancel, refund, no-show, weather, communication lead the low-star lists for NPB, HPB, BBK, DCKT and Austin |
| Shared staff across listings | Admire NOLA reviews name the same guides as NKST (Nick, Alex, Ryan). Hidden Adventure names NPB captains (Daddy, Badass, Pip). Austin Paddle Shack names the same guides as LSKT (Rives, Connor, Anne) |

## NPB: NOLA Party Barge

**Data basis**: 3,944 reviews (2,850 with text), 4.92 average, 95.5% five-star, 1.6% at 3 stars or below. 252 chat sessions (201 real shoppers). Messenger is 85% of chat volume.

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=127) |
|:-|:-|:-|:-|
| Friends / group | 357 | 12.5% | 22.0% |
| Birthday | 198 | 6.9% | 7.1% |
| Bachelorette / bach / bridal | 170 | 6.0% | 9.4% |
| Family / kids | 126 | 4.4% | 8.7% |
| Couple / date | 37 | 1.3% | 0.8% |
| Corporate / team | 8 | 0.3% | 0.0% |
| Solo | 3 | 0.1% | 0.0% |

Only 693 reviews (24.3%) name any party type. First-timer language 1.4%, "second time / every year" 3.8%, intent to come back 11.6%. Visitors 7.2% vs locals 0.2%.

Chats tell the same story about occasions. Of 242 chat sessions with real text: birthday 24 (9.9%), bachelorette plus girls trip 4 (1.7%), corporate 1, wedding 1. Stated group size (n=61): median 10. 1 to 4 people 15%, 5 to 8 26%, 9 to 13 30%, 14 to 24 28%, 25+ 2%.

### Jobs to be done
- Make a milestone day easy to say yes to. The planner brings drinks. The captain, the music and the gators do the rest. Evidence: captain named in 32% of reviews, "party / vibe / drinks" 20%, music or dancing 9%, gators 10.6%, "would do it again" 15%.
- Give a visitor a New Orleans story that is not Bourbon Street. "Highlight of our trip" and "must do" read like trip reports.

### Top 5 questions and objections (chats, n=201 shoppers)

| Rank | Question | Chats mentioning it | As first question |
|:-|:-|:-|:-|
| 1 | How much / price / discounts | 124 (62%) | 105 (52%) |
| 2 | Group size and fit | 76 (38%) | 17 (8%) |
| 3 | How do I book / pay / deposit | 53 (26%) | 26 (13%) |
| 4 | Availability for a date | 42 (21%) | 23 (11%) |
| 5 | What is included / what is on the boat | 21 (10%) | 5 (2%) |

Next: private vs shared 17 (8%), duration 17 (8%), BYOB 13 (6%), location 10 (5%), kids or age 10 (5%), weather 5 (2%).

Low-star reviews (51 with text): cancel / refund / reschedule 11, price or value 11, weather 10, rude crew or office 5, late or wait 4, booking or location confusion 4.

### Fears that stop a booking
- Not knowing the price. The most common first message is two words: "How much".
- Not knowing if their group fits seats or a private boat.
- No answer. Of the 3 angry NPB sessions, 2 were about no reply or lost context ("no one contact me back yet").
- Rain with no clear refund rule (10 low-star reviews).
- Actual fear is small: nervous or scared in 0.6% of reviews, gator fear in 1 review.

### Funnel proxy (chats)
- 129 of 201 shopper chats (64%) ended with no booking link from the AI and no email or phone from the shopper. 27% did leave contact info. The AI sent a booking link in only 14% (29).
- 220 of 252 sessions (87%) later got a human message ("just circling back" or "I've got the AI agent turned off"). Only 13 got a customer reply after it (5.9%).
- 32% of shoppers sent one message and left.

### Headline seeds (real review phrases, internal use)
1. "Literally the best time I had my whole Trip!"
2. "Our captain fed 2 different alligators marshmallows FROM HIS HAND."
3. "We saw gators, it was BYOB, and fun tunes."
4. "Perfect blend of party but fun info from Captain Pip!"
5. "It rained some but it made it that much more fun!"
6. "Worth every penny, the captain friendly and knowledgeable."
7. "If you're visiting New Orleans this a must do!"
8. "Would highly recommend this trip for any bachelorette!"
9. "Our group had a blast seeing gators and dancing."
10. "We did this boat tour for my friends 55th bday!"
11. "I even think the alligators were rocking with us!"
12. "The Party Boat was the highlight of our trip."

Words they use: "great time" (368 reviews), "so much fun" (224), "highly recommend" (186), "captain [name]", "party boat", "tiki boat", "boat ride". 2.0% still say "Pedal Barge" (old name). The Freaky Tiki is named in 4.2%, Twerkin Tiki 1.9%, Party Queen 0.4%, Bayou Boogie 0.4%.

### Test hypotheses
1. **Birthday-first, not bachelorette-first.** Birthday is 6.9% of reviews and 9.9% of chats. Bachelorette is 6.0% and 1.7%. Test a "celebrating a birthday?" hero and ad set against the current seat-led hero.
2. **Show the price and the per-head math above the fold.** 52% of first questions are "how much" and 28% of stated groups are 14 to 24 people, the zone where a private boat can beat seats. Test a price strip plus a seats-or-whole-boat calculator.
3. **Fix the chat handoff.** The AI links to booking in 14% of shopper chats and the human nudge gets a 6% reply rate. Test asking for a phone number in reply 2 (27% already volunteer one) and texting the booking link.

### Where existing docs disagree with the data
Compared with `NOLA Party Barge/Persona Funnels/01 Personas.md`:
- **Bachelorette as Persona 1 and "bread and butter."** Data says birthday is as big or bigger (reviews 6.9% vs 6.0%, chats 9.9% vs 1.7%). Bachelorette is stronger in the sibling party-boat listings (Booze Cruise 13.7%, Tiki 8.7%, Bike Bar 8.2%).
- **Office Party as build order #1.** Corporate is 0.3% of reviews and 1 of 242 chats. The Q4 holiday window is real, but this is an outbound list play, not a segment customers describe.
- **Small-crew seat buyers (2 to 6) as the volume engine.** True in the bookings CSV. Chat shoppers are planners: only 41% state 8 or fewer, median 10. Two audiences: seat buyers who book without chatting, and planners who chat.
- **Weather as the #2 bachelorette objection.** Weather is 2% of chats and bad-weather language is 1.7% of reviews. Price is the real #1.
- **The drive as the #1 seat-buyer objection.** Drive or downtown talk is 2.7% of reviews, location confusion 0.8%, location questions 5% of chats.
- **Seat price.** Doc says $59 after the 9/30 fix. In chats the AI quoted $63 per person in 151 sessions (May 1 to Jun 1 2026) and $59 in 10 (Apr 30 to May 13). Verify what is live now.
- **Party Queen capacity (doc open question).** The AI quoted 22 guests 64 times and called it the Coast Guard limit. Site subtitle says 26. Chat supports 22. Other quoted caps: Bayou Boogie 18, Freaky and Twerkin Tiki 25, Pontoon 6.
- **Cousin trip / 12-month booking window.** Only 2 of 252 chats mention 2027 or next year. Not enough to prove demand.
- **Agrees with the data**: dropping locals and date nights (locals 0.2%, couples 1.3%).

## NKST: New Orleans Kayak Swamp Tours

**Data basis**: 1,426 reviews (1,303 with text), 4.95 average, 97.4% five-star. 251 chat sessions: 168 are Messenger lead-form submissions, 58 are real organic shoppers.

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=129) |
|:-|:-|:-|:-|
| Friends / group | 86 | 6.6% | 4.7% |
| Couples | 73 | 5.6% | 5.4% |
| Family / kids | 61 | 4.7% | 7.0% |
| Solo | 14 | 1.1% | 3.1% |
| Corporate / team | 9 | 0.7% | 0.8% |
| Birthday | 5 | 0.4% | 0.8% |
| Bachelorette | 6 | 0.5% | 0.0% |

Only 226 reviews (17.3%) name a party type. Visitors 13.7% (179), locals 2.2% (29). First-timer 5.8% (75), repeat 3.7%, intent to return 6.1%.

**Lead-form data (the surprise)**: 168 Messenger form fills answered two questions. Do you live in New Orleans: yes 110 (65%), no 58 (35%). Have you been kayaking before: yes 112 (67%), no 56 (33%). Local first-timers 42 (25%). Out-of-town first-timers only 14 (8%). Of those 168 sessions, 121 (72%) ended after the AI's single reply.

### Jobs to be done
- See the real Louisiana wild with someone who knows it. Wildlife in 53% of reviews (birds 55%, gators 33%, snakes 3.5%), knowledge or learning language 63%, guide named 55%.
- Do it with no skill and no noise. Easy or stable 10%, quiet or peaceful 9%, safe 8%, "away from the city" 9%.
- For a visitor: the thing that was not Bourbon Street. "Highlight of our weekend" and "best experience in New Orleans."

### Top 5 questions and objections (organic chats, n=58)

| Rank | Question | Chats mentioning it | As first question |
|:-|:-|:-|:-|
| 1 | Where do we meet / pickup / parking / bathrooms | 25 (43%) | 17 (29%) |
| 2 | Group size | 17 (29%) | 4 (7%) |
| 3 | Price and discounts (military, veteran) | 16 (28%) | 12 (21%) |
| 4 | How to book / pay | 15 (26%) | 5 (9%) |
| 5 | What is included / what to expect | 12 (21%) | 5 (9%) |

Next: availability 12 (21%), weather 8 (14%), kids 4 (7%). Low-star reviews (19 with text): price or value 5, booking or location confusion 5, late 4, cancel 4, weather 4.

### Fears that stop a booking
- Logistics. "Can we drive ourselves?" "Is there a bathroom on a 4-hour tour?"
- Fear of the swamp itself is real but small: nervous or scared 3.1% (41), tipping over 1.0%, gator fear 0.8%, snakes 3.5% mention.
- Disappointment: "no gators" shows up in 2.2% of reviews. One low-star review blames winter timing with no warning at booking.
- A full-screen chat popup annoyed 2 visitors enough to be tagged angry.

### Funnel proxy (organic chats)
48% of 58 shopper chats ended with no booking link and no contact captured. The AI sent a link in 26%.

### Headline seeds
1. "Highly recommend this tour, even for beginners!"
2. "Was definitely apprehensive of kayaking through the swamp, but PLEASE don't be!"
3. "This is the best way to see the swamp."
4. "We got within feet of a sun-bathing gator twice!"
5. "A lovely way to see a different side of Louisiana!"
6. "It was by far our best experience in New Orleans."
7. "He made us feel comfortable as beginner kayakers."
8. "We saw alligators, barred owls, and so much more."
9. "The swamp tour was the highlight of our weekend!"
10. "It was great learning about the swamp ecosystem."
11. "Alex is the king of the swamp."
12. "This tour is a MUST if you're visiting New Orleans."

Words they use: "tour guide" (241 reviews), "highly recommend" (194), "kayak tour", "swamp tour", "flora and fauna", "learned a lot", "barred owls", "super knowledgeable". Guides named: Nick in 234 reviews (18%), Alex 136 (10%), Bingo 84, Ryan 50, Stephanie 45.

### Test hypotheses
1. **Locals who have never been.** 65% of lead-form fills live in New Orleans and 33% have never kayaked, while only 2.2% of reviews sound local. Test a locals-and-first-timers ad ("never been in your own swamp") against visitor creative, and split the lead form by answer.
2. **Put the meeting point and pickup answer first.** Location is the #1 organic question (29% first, 43% overall). Test a "where we meet, how to get there, shuttle from the Quarter" block above the booking button.
3. **Rescue the lead form.** 72% of form leads never reply to the AI's date question. Test a one-tap month picker plus the booking link in the first reply, then a text at 2 hours.

### Where existing docs disagree with the data
Compared with `NKST - Customer Journey Map.md`:
- **Stage 0 audience** is "planning a NOLA trip in 1 to 3 months, not locals." The lead form says 65% live in New Orleans.
- **"I've never kayaked / is it safe" as the lead consideration objection.** Fear language is 3.1% and first-timers 5.8%. The top real question is where to meet.
- **Motorized-boat comparison.** Map builds a "vs airboat / Cajun Pride" angle. Reviews compare against motor boats in only 3.1%.
- **Gator expectations.** Map says set honest expectations. Reviews: gators in 33%, "no gators" in 2.2%. The expectation risk is small.
- **Missing proof asset.** Map has no guide-led proof. 55% of reviews name a guide.
- **Agrees**: pickup logistics and price-vs-boat-tour appear in the data (pickup or shuttle 7.2% of reviews, "worth it" 4.6% vs "not worth" 0.5%).

## DCKT: Door County Kayak Tours

**Data basis**: 1,015 reviews (912 with text), 4.91 average, 95.9% five-star. 254 chat sessions: 110 real shoppers, 35 brochure requests, 13 job inquiries, 4 spam, 27 empty. Email is the biggest channel (46%), then web chat (24%), phone voice (12%), Instagram (11%).

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=104) |
|:-|:-|:-|:-|
| Family / kids | 66 | 7.2% | 11.5% |
| First-time kayaker | 63 | 6.9% | n/a |
| Friends / group | 54 | 5.9% | 5.8% |
| Couples | 35 | 3.8% | 1.9% |
| Bachelorette | 5 | 0.5% | 0.0% |
| Corporate | 2 | 0.2% | 0.0% |

Only 154 reviews (16.9%) name a party type. Visitors 4.1% vs locals 0.3%. Repeat language 3.3%, intent to return 6.1%.

### Jobs to be done
- The one guided outing of a Door County trip that works for the whole family. Cave Point or caves in 20.3% of reviews (185), scenic 15%, safe 8.6%, history or learning 27.7%, guide named 52%.
- Cave Point seen from the water. "It was so cool to see Cave Point from a different perspective."
- Not wildlife. Wildlife appears in only 1.5% of reviews. Do not borrow swamp hooks.

### Top 5 questions and objections (chats, n=110 shoppers)

| Rank | Question | Chats mentioning it | As first question |
|:-|:-|:-|:-|
| 1 | Kids, ages, toddlers, pets | 46 (42%) | 26 (24%) |
| 2 | Group size | 42 (38%) | 3 (3%) |
| 3 | Booking, payment, confirmations | 41 (37%) | 12 (11%) |
| 4 | Availability and dates | 38 (35%) | 22 (20%) |
| 5 | What is included | 28 (25%) | 7 (6%) |

Next: location 26 (24%), beginner and safety 25 (23%), price 23 (21%), duration 17 (15%), weather 11 (10%). Raw counts across all DCKT chats: 36 sessions ask about kids or ages, 16 about dogs or pets, 15 about weight limits or pregnancy.

Low-star reviews (21 with text): price or value 7, booking or location confusion 6, cancel 5, weather 3, "underwhelming, not enough caves" 3.

### Fears that stop a booking
- Can my toddler, dog, or heavier family member come? ("Can a couple bring a 21 month old in a tandem kayak?")
- Weight limits and pregnancy (15 sessions).
- Wind, waves, smoke or air quality cancelling the day (conditions or weather in 7.7% of reviews, 10% of chats).
- Fear of the kayak itself is 2.7% of reviews (25). First-time language is bigger at 6.9%.
- Low-star expectation gap: "just paddling along the shore for 2 hours" vs a cave-heavy promise.

### Funnel proxy (chats)
49% of 110 shopper chats ended with no booking link and no contact captured. AI sent a link in 15%. 50 of the 110 shopper chats were handed to a human. 14% of all sessions are brochure requests, 35 in total.

### Headline seeds
1. "It was our first time kayaking and this was the best tour ever."
2. "As a first time kayaker, highly recommend."
3. "Great experience for the whole family!"
4. "Exciting while still safe for the kids."
5. "The Cave Point Kayak tour is a must do!"
6. "It was so cool to see Cave Point from a different perspective."
7. "This was definitely the highlight of our visit to door county."
8. "He also took time to show our kids how to skip rocks."
9. "Let us cliff jump and took us into the caves."
10. "None of us had experience and it was good for beginners."
11. "This was the highlight of mine and my wife's honeymoon."
12. "The training was excellent, even for beginners like us."

Words they use: "tour guide" (144 reviews), "Cave Point" (92), "great guide" (88), "first time kayaking", "cliff jumping", "e-bike". Guides named in 52%: Evan 69, Jackson 48, Anders 39, Eli 38, Tabitha 33.

### Test hypotheses
1. **Family-first page and ads with the real kid, dog and weight policy up top.** Kids, age and pets is the #1 first question (24%) and families are the #1 and fastest-growing review segment (11.5% recent). Publish the actual limits, do not guess them.
2. **Lead with Cave Point by name.** 20% of reviews name it. Test a Cave Point landing page against the generic "kayak tours" page, and add an honest "what you will and will not see" line to cut the underwhelmed reviews.
3. **Answer in the first reply.** 46% of volume is email and 49% of shopper chats end with no link. Test an auto-reply that carries the availability link plus the age, pet and weight answers.

### Where existing docs disagree with the data
Compared with `Door County Kayak Tours/Playbook/02 - Customer Journey Map.md`:
- **"800+ five-star reviews."** GBP now shows 1,015 reviews, 973 of them five-star. Update the proof counter.
- **Objection list** (never kayaked, rain, safe for kids and seniors, "worth $59"). Missing from it: pets, toddler-in-tandem, and weight limits, which top the chats.
- **Price weight.** The map treats "is it worth it" as a core objection. Price is 2.7% of reviews and 14% of first questions (3rd).
- **Wildlife hooks.** Not supported (1.5%).
- **Chatbot line** names a past vendor. Transcripts now come from OpenCX.
- **Agrees**: beginner reassurance matters (first-timer 6.9%).

## E&E: Ebb & Ember (Portland floating sauna)

**Data basis**: 125 reviews (115 with text), 4.94 average, 95.2% five-star, Sep 28 2025 to Oct 12 2026. 102 are from the last 12 months. No OpenCX workspace and no chat data, so there is no first-question count. Small sample. Treat every % as directional.

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=102) |
|:-|:-|:-|:-|
| Friends / group | 17 | 14.8% | 13.7% |
| Couples / date night | 9 | 7.8% | 8.8% |
| Family / kids | 5 | 4.3% | 4.9% |
| Birthday | 3 | 2.6% | 2.9% |
| Corporate | 2 | 1.7% | 1.0% |
| Solo | 2 | 1.7% | 2.0% |

Only 32 reviews (27.8%) name a party type. Repeat or regular language 14.8% (17), intent to come back 28.7% (33). Visitors 3.5%, locals 0.9%, Portland or "city" mentioned 20.9%. This is a Portland product.

### What they actually write about
Sauna 69.6%, cold plunge or river dunk 50.4%, the Columbia River 47.8%, views 28.7%, roof deck 20.9%, relax / reset / unwind 44.3%, unique 26.1%, clean 16.5%, parking and access 17.4%, signage 14.8%, heated floors 7.8%, sunset or evening 13.0%, private or whole-sauna 5.2%.

### Jobs to be done
- A heat and cold ritual in a special place. The river dunk is the payoff, not the sauna interior.
- An occasion marker for two or for friends: date night, anniversary, birthday, "end of a river day."
- A local treat to repeat. 14.8% already talk like regulars.

### Top things reviewers volunteer (not objections, no chat source)

| Rank | Topic | Reviews | % |
|:-|:-|:-|:-|
| 1 | Changing, showers, lockers, towels | 23 | 20.0% |
| 2 | Getting there: parking, signs, finding the dock | 20 | 17.4% |
| 3 | Price or value | 5 | 4.3% |
| 4 | Social session etiquette ("social" mentioned) | 4 | 3.5% |
| 5 | River current and cold-water safety | 3 | 2.6% |

Low-star reviews: 2 with text. One booked a banya session where nobody showed, plus a bad transit walk from the MAX. One loud group in a social session. A 4-star review wished for human supervision at the river.

### Fears that stop a booking
- Evidence is thin. Nervous or hesitant language is 1.7% (2 reviews). "Will work up the courage to dunk next time" appears once.
- Real safety flags: three reviews mention strong current or no supervision. One family member was swept away upstream and needed a life ring.
- Getting there without a car. One reviewer tells others to take a Lyft.
- Not knowing what to bring: "bring two towels per person, bathrobes if chilly."

### Funnel proxy
None. No chat workspace exists for this brand. Add one before judging pre-booking questions.

### Headline seeds
1. "Such a perfect way to end a river day."
2. "It was the perfect mix of peaceful and luxurious."
3. "Worth every penny for a totally unique experience."
4. "Sweat, jump in the river to cool off and repeat!!"
5. "Jumping in the river directly from the sauna was the best part."
6. "A perfect date night or birthday idea."
7. "I was proud that my group all braved jumping into the river."
8. "So relaxing watching it rain outside and cold plunge!"
9. "There's no experience like this in PDX!"
10. "I can't wait to go again and want to bring all my friends!"
11. "This place is a hidden gem!"
12. "Best floating sauna experience I've had!"

Words they use: "cold plunge" (23 reviews), "floating sauna" (18), "Columbia River" (14), "can't wait", "unique experience", "jump off the roof", "cool off". Two reviews still call it "Elevated Tides."

### Test hypotheses
1. **Lead with the dunk, not the sauna.** The river jump is in about half of reviews and is the stated differentiator. Test creative that opens on the jump from the roof or deck against the interior-sauna shot.
2. **Locals and repeat visits before tourists.** Tourists are 3.5% of reviews and 29% mention coming back. Test a rebook prompt and a friends-bring-a-friend offer ahead of lodging referral outreach.
3. **Put "how to get here and what to bring" on the booking page.** Access and facilities are what reviewers volunteer, and the two negative themes are day-of: transit, noisy social sessions. Add river-current guidance and a bring-list.

### Where existing docs disagree with the data
Compared with `Marketing/Wellness Brand Targets - Affluent Member Persona (Sept 2026).md`:
- **"30 to 50 year old professional with real money."** Reviews carry no age or income. Unverified, not contradicted. What they do show: Portland locals, friend groups and couples.
- **Recovery-wearable brands (Oura, Whoop, Eight Sleep).** The doc already warns about health-claim language. Customers do not use it either: "recovery" appears in 0 of 115 reviews, "health" in 2, "wellness" in 4, sleep or biometric words in 1. They say reset, unique, views, plunge.
- **Hardware and aesthetic fit holds up.** Sauna in 70% and cold plunge in 50% supports the home-sauna and plunge brands. Sleek, spotless, intentional design language is 15.7%, which supports the quiet-aesthetic brands (Aesop style).
- **Lodging referral outreach** (a separate project) leans on visitors. Visitors are 3.5% of reviews.

## LSKT + AKT: Austin Kayak

**Data basis**: LSKT 158 reviews (137 with text, 2016 to Jul 2024), AKT 143 (105 with text, Mar 2024 to Sep 2026). Combined 242 with text, 4.81 average. Chats exist for LSKT only: 131 sessions, 73 real shoppers, 17 spam, 11 empty. Recent 12 months is only 18 reviews, so no recent split.

### Segments (% of reviews with text, n=242)

| Segment | Reviews | % of all |
|:-|:-|:-|
| Family / kids | 23 | 9.5% |
| Friends / group | 20 | 8.3% |
| Couples | 16 | 6.6% |
| Corporate / team | 8 | 3.3% |

Only 56 reviews (23.1%) name a party type. First-timer 9.9% (24). Visitors 12.0% vs locals 0.8%. LSKT alone: family 13.1%, couples 8.0%, friends 9.5%.

### Jobs to be done
- See the city's signature spectacle, the Congress Avenue bats, from the water. Bats in 30.6% of reviews (74), skyline 15.7%, sunset 6.2%.
- Do it guided so a beginner can. Easy or simple 14.5%, learning 39%, guide named 35%.
- A visitor's Austin trip highlight ("one of the highlights of my Austin trip").

### Top 5 questions and objections (LSKT chats, n=73 shoppers)

| Rank | Question | Chats mentioning it | As first question |
|:-|:-|:-|:-|
| 1 | Price, rates, military discount | 24 (33%) | 19 (26%) |
| 2 | What is included / what is the tour | 20 (27%) | 16 (22%) |
| 3 | Booking and payment | 19 (26%) | 9 (12%) |
| 4 | Availability | 15 (21%) | 7 (10%) |
| 5 | Group size and duration (tied) | 13 (18%) each | 3 (4%) and 1 (1%) |

Next: parking and location 11 (15%), beginner suitability 7 (10%). The earlier VOC pull also flagged "is the tour suitable for beginners" 3 times. Low-star reviews (13 with text): cancel or reschedule 4, "no bats / disappointing" 4, price 3, dirty 3.

### Fears that stop a booking
- Will the bats show? ("bats were too cold and wet to come out.")
- Is it a beginner trip, and are life jackets required? (chat questions)
- Cancellation and weather policy. Four low-star reviews.
- Day-of meeting point confusion: one chat reports an "abandoned" meeting spot.

### Funnel proxy (LSKT chats)
78% of 73 shopper chats ended with no booking link and no contact. 44% were a single message. Instagram DMs are 41% of chat volume, Messenger 31%, web 28%.

### Headline seeds
1. "The bats were amazing, a completely unique, must-do experience!"
2. "We had perfect weather and enjoyed the sunset and bats!"
3. "What a wonderful experience to check off our bucket list."
4. "It was honestly the highlight of our trip!"
5. "One of the highlights of my Austin trip."
6. "I highly recommend this guided tour for beginners."
7. "Perfect for beginner level kayakers or a fun family activity to do."
8. "The bats and skyline were really cool to see."
9. "Had a great trip to see the bats for my friend's 60th birthday."
10. "My husband and I took this tour on our anniversary."

Words they use: "bat tour" (14 reviews), "skyline tour", "see the bats", "Lady Bird Lake", "first time kayaking", "easy to book".

### Test hypotheses
1. **Make the bats the lead product for visitors.** 31% of reviews name them and visitors are 12% of reviews. Test a bat-season landing page and "watch the bats from a kayak" ads against the generic kayak page.
2. **A what's-included and beginner panel with a flat price.** Price and "what is the tour" are 48% of first questions combined. Test a single block: price, what you get, no experience needed.
3. **Link in the first reply on Instagram DMs.** 78% of chats end with nothing captured and IG is the top channel. Test a booking link and the beginner answer in the first auto-reply.

### Where existing docs disagree with the data
- No Austin persona doc was provided, so nothing to reconcile. Note for the file: LSKT and AKT share the same guides in reviews, which supports treating them as one brand in funnels.
- Existing Austin voice-of-customer file is from chat noise (spam and dating-bot messages were mined as "themes"). Do not use `voc/lskt.json` themes without cleaning.

## HPB: Houston Pedal Barge

**Data basis**: 983 reviews (784 with text), 4.91 average, 96.8% five-star, 18 one-star reviews total. 72 chat sessions: 37 real shoppers, 10 post-booking issues, 12 empty, 5 spam. Small chat sample.

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=35) |
|:-|:-|:-|:-|
| Friends / group | 141 | 18.0% | 31.4% |
| Birthday | 62 | 7.9% | 5.7% |
| Family / kids | 59 | 7.5% | 14.3% |
| Bachelorette / bridal | 18 | 2.3% | 5.7% |
| Couples | 15 | 1.9% | 5.7% |
| Corporate / team | 4 | 0.5% | 5.7% |

Only 222 reviews (28.3%) name a party type. Visitors 5.0%, locals 0.8%. Repeat 3.6%, intent to return 15.1% (118).

In chats, corporate or work events show up in 9 of 59 sessions (15%), far above the 0.5% in reviews. Stated group size median is 8 (n=14, thin).

### Jobs to be done
- Turn a birthday or group hangout into a shareable event on the water: drinks, music on their Bluetooth, nobody has to drive. Party or vibe language 14%, music 5.5%, BYOB 4.3%, safe or smooth 8.8%.
- A "Houston thing to do" for visitors and friends: "must do when you're in Houston."

### Top 5 questions and objections (chats, n=37 shoppers)

| Rank | Question | Chats mentioning it | As first question |
|:-|:-|:-|:-|
| 1 | Booking, payment, gift cards | 15 (41%) | 4 (11%) |
| 2 | Group size / capacity | 14 (38%) | 1 (3%) |
| 3 | Private boat vs public seat | 13 (35%) | 6 (16%) |
| 4 | Price | 12 (32%) | 10 (27%) |
| 5 | Occasion (birthday, party) fit | 9 (24%) | 1 (3%) |

Next: what is included 8 (22%), location 7 (19%), availability 7 (19%), duration 6 (16%), BYOB 4 (11%).

Low-star reviews (19 with text): cancel or refund 17, "disappointing" 10, rude 8, weather 8, communication 7, late 6. On Jun 6 2026, 8 reviews landed in one day (9 one-stars since Jun 1), all about a storm trip. That is 9 of the 35 reviews from the last 12 months. 6 of the 72 chat sessions are the same event, tagged angry: refund promised in a public reply, not received, no answer in private follow-up.

### Fears that stop a booking
- Weather cancels with a slow or unclear refund. The mined chat themes agree: refund delay 8, weather cancellation 8, gift card inconvenience 7.
- Private vs seat confusion for groups.
- "Is the captain really there?" One recent review: arrived after a 45 minute drive, no captain.
- Fear of the activity is almost nil (0.5% nervous).

### Funnel proxy
76% of 37 shopper chats ended with no booking link and no contact captured. AI sent a link in 19%. 32% were one-message sessions.

### Headline seeds
1. "Hook your music to their Bluetooth, and Vibe out."
2. "Book right before the sunset, you won't regret it!"
3. "This is a must do when you're in Houston."
4. "First time on a booze cruise but it won't be my last!!"
5. "It was so much fun and beginner friendly!"
6. "I had an amazing time on my girls trip."
7. "Loved The Experience With My Cousins On Our Cousins Trip"
8. "Bella was amazing and made my mother's birthday !!!"
9. "Great way to chill with family and friends."
10. "We were comfortable, brought our own food, drinks and music."
11. "Boat ride was amazing and the birthday girl enjoyed herself!"

Words they use: "great time" (92 reviews), "so much fun", "boat ride", "pedal barge", "captain [name]". Guides named in 43%: Bella 78, Tom 71, Abby 53, Don 44, Zach or Zack 60.

### Test hypotheses
1. **Post a plain weather and refund rule at booking and in the confirmation email.** 17 of 19 low-star reviews are cancel or refund. Test a three-line policy ("lightning means we cancel, here is when your money moves") plus an automatic refund-status message. This protects conversion and reviews.
2. **Friend-group and birthday hero with BYOB and Bluetooth music.** Friends are 18% (31% recent), birthday 7.9%. Test a birthday-first hero against the generic hero.
3. **Private vs public chooser plus a team-event page.** Private vs shared is 16% of first questions and 35% of chats. Corporate shows up in 15% of chats vs 0.5% of reviews. Test a "pick your boat by headcount" tool and a one-page team event offer.

### Where existing docs disagree with the data
- No HPB persona or journey doc was in the provided set. Nothing to reconcile.
- Flag from the data: the NPB persona doc treats bachelorette as the lead. HPB bachelorette is 2.3%. Do not copy NPB personas to Houston.

## BBK: Buffalo Bayou Kayak

**Data basis**: 597 reviews (570 with text), 4.78 average, 91.5% five-star, 5.0% at 3 stars or below (the highest of the core brands). 21 chat sessions, only 8 real shoppers. Chat data is too thin to rank questions. 137 reviews in the last 12 months.

### Segments (% of reviews with text)

| Segment | Reviews | % of all | Last 12 months (n=137) |
|:-|:-|:-|:-|
| Couples | 57 | 10.0% | 13.1% |
| Family / kids | 50 | 8.8% | 6.6% |
| Friends / group | 44 | 7.7% | 8.0% |
| School / org | 8 | 1.4% | 2.2% |
| Corporate | 8 | 1.4% | 0.7% |

Only 136 reviews (23.9%) name a party type. First-timer 9.1% (52), repeat 6.5% (37), intent to return 12.5% (71). Visitors 6.1%, locals 2.6%.

### Jobs to be done
- See Houston from a side almost nobody sees, with a guide who tells the story. Skyline or downtown 16.3%, Houston history 12.1%, learning 32%, wildlife 14.6% (turtles, birds, bats 6.3%).
- The guide is the product: 70% of reviews name one. Blake is in 146 reviews (25.6%), David 73, Josh 56, Kaleb 55, Chad 30.
- Rental and paddleboard days appear in 13.9%.

### Top questions and objections
Chat shoppers (n=8): price 3, weather or cancel 2, beginner 1, kids 1, location 1. Too few to rank.

Reviews, low-star (27 with text): dirty water or trash 14, cancel or reschedule or no-show 13, booking or parking confusion 6, price 5, "no wildlife / disappointing" 5, rude 4. Across all reviews: dirty or smelly water 6.7% (38), parking or finding the place 6.5%, weather 8.4%, cancel or high water 2.8%.

### Fears that stop a booking
- The water. "The water legitimately looks like sewer water." Reviewers who were warned by the guide forgive it ("Water was dirty but the people were nice").
- Cancellations and no-shows by the operator (staffing, construction, weather). Several low-star reviews say they drove an hour for nothing.
- First-timer nerves, softened by guides: "As a first timer, she absolutely eased my anxiety."
- Fear language overall 4.2% (24).

### Headline seeds
1. "Totally different view of the city from the water!"
2. "As a first timer, she absolutely eased my anxiety."
3. "Definitely a must do on your Houston bucket list."
4. "Highly recommend for beginners and experienced kayakers alike!"
5. "It was worth every penny and every sore muscle."
6. "A must do for locals and visitors alike!"
7. "This was a hidden gem."
8. "Josh is the highlight of the trip."
9. "10/10 it's Houston so you can't expect perfection regarding the bayou."
10. "Good way to experience downtown Houston from a different perspective."
11. "This was our first time kayaking but it was very easy actually."
12. "Water was dirty but the people were nice."

Words they use: "tour guide" (73), "Buffalo Bayou", "first time kayaking", "Houston skyline", "Houston history", "bat tour", "sunset tour".

### Test hypotheses
1. **Set the water expectation before checkout.** Dirty water is the #1 low-star theme. Test one honest line ("this is an urban bayou, here is what you'll see") against none, and track the 1 to 3 star rate.
2. **Guide-led creative.** 70% of reviews name a guide and one guide is in a quarter of all reviews. Test "paddle with Blake" ads and guide cards on the booking page.
3. **Couples sunset and skyline for two.** Couples are the top segment (10.0%, 13.1% recent) and skyline plus sunset are strong themes. Test a date-night angle for Houston locals against the general hero.

Also an ops risk, not a test: cancellations and no-shows are half the low-star list. Fix day-of messaging before spending more on ads.

### Where existing docs disagree with the data
- No BBK persona or journey doc was in the provided set. Nothing to reconcile.

## Siblings and smaller listings

These have no chat workspace. All numbers are from reviews only.

| Listing | Reviews with text / total | Top segments (% of reviews) | What stands out |
|:-|:-|:-|:-|
| Admire NOLA (4 listings) | 428 / 569 | Friends 6.8%, family 4.7%, birthday 4.2%, couples 3.7% | Gators 17.1%, wildlife 28%, learning 37%. Guides named: Nick 41, Alex 26, Ryan 15, the same people as NKST. Recent n=17, too thin for a recent split |
| Honey Island Swamp Kayak Tour | 12 / 14 | Too thin to call | Visitors 5 of 12, guide Jess in 4. Learning language in 10 of 12 |
| Crescent City Kayak (cck) | 82 / 96 | Family 6.1%, couples 2.4%, friends 2.4% | Reviews end Apr 2024. Gators 30.5%, wildlife 50%, scenic 18%. Nick named in 34 (a NKST guide again) |
| Cave Point Paddle and Pedal (cppp) | 241 / 306 | Family 10.0%, first-timer 7.1%, friends 4.6%, couples 4.1% | Fun 28.6%, scenic 10.4%. Guide named 35%. Low-star: "long paddle with nothing to see" |
| Austin Paddle Shack (+ Austin Party Barge) | 341 / 408 | Friends 10.9%, family 4.7%, couples 3.5% | First-timer 10.6%, easy 11.4%, guide named 52% (Rives 40, Connor 23, Adam 19). Same guides as LSKT |
| Hidden Adventure | 343 / 540 | Friends 10.2%, birthday 7.9%, family 6.4%, bachelorette 4.4% | Gators 15.5%, party or vibe 18%, music 12.8%. Names NPB captains (Barry 15, Daddy 11, Badass 9, Pip 7), so it is partly the same party-boat product |
| The Freaky Tiki (tiki) | 127 / 140 | Friends 16.5%, birthday 11.0%, bachelorette 8.7% | BYOB 12.6%, gators 11.8%, 97.9% five-star. One low-star about being left stranded after a shutdown |
| NOLA Booze Cruise (nbc) | 117 / 214 | Friends 14.5%, bachelorette 13.7%, birthday 9.4% | Highest bachelorette share of any listing. Visitors 16.2%. Listing ends Apr 2025 |
| NOLA Bike Bar (nbb) | 158 / 179 | Friends 15.2%, bachelorette 8.2%, birthday 7.6% | Drinks or BYOB 19%, guide named 46%. Low-star: noisy or rowdy other guests 4, rude 3. Ends Jun 2025 |
| Door County Detours | 33 / 43 | Too thin | Not analyzed further |

Sibling hypotheses worth a test:
1. **Bachelorette lives in the booze-cruise and bike-bar framing, not in the NPB listing.** NBC 13.7%, Tiki 8.7%, Bike Bar 8.2%, NPB 6.0%. If bachelorette ads are wanted, run them on the booze-cruise or tiki framing and send birthdays to NPB.
2. **Shared guides mean shared proof.** NKST, Admire NOLA and Crescent City name Nick and Alex. NPB, Hidden Adventure and Tiki name the same captains. Pool testimonials across listings (with the guide's OK) to lift the thinnest brands.
3. **Cave Point Paddle and Pedal is the family sibling of DCKT** (family 10.0% vs 7.2%). Test the DCKT kids, pets and weight answers on the CPPP page too.

## Data gaps to fix

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
| No OpenCX workspace for E&E, AKT, and the siblings | No pre-booking question data. E&E and AKT are the priority |
| E&E sample is 115 reviews | Re-run in 6 months |
| NPB and HPB reviews are short (median 14 to 15 words) | Party type is hidden in 75% of reviews. A post-trip one-question survey ("who did you come with, what was the occasion") would fix this |
| DCKT chat has 65 unclear sessions | Email form replies are mixed with staff replies. A cleaner export would sharpen the kids and availability counts |
| Seat price $59 vs $63 in NPB chats | Verify the live price, then update persona doc and AI instructions |
