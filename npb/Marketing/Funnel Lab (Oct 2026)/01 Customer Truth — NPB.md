*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NPB.*

# Customer Truth: NPB (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| NPB (NOLA Party Barge) | 2,850 / 3,944 | Friends celebrating, 12.5% of reviews. Top named occasion is birthday, 6.9% (bachelorette 6.0%) | "How much?" 52% of first questions (201 shopper chats) | Price and group fit. Price comes up in 62% of chats | 32% of reviews name a captain. "Worth every penny, the captain friendly and knowledgeable." |

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

## Cross-brand patterns that name NPB (from file 01)

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

## Related sibling listings (rows from file 01, Siblings and smaller listings)

These have no chat workspace. All numbers are from reviews only.

| Listing | Reviews with text / total | Top segments (% of reviews) | What stands out |
|:-|:-|:-|:-|
| Hidden Adventure | 343 / 540 | Friends 10.2%, birthday 7.9%, family 6.4%, bachelorette 4.4% | Gators 15.5%, party or vibe 18%, music 12.8%. Names NPB captains (Barry 15, Daddy 11, Badass 9, Pip 7), so it is partly the same party-boat product |
| The Freaky Tiki (tiki) | 127 / 140 | Friends 16.5%, birthday 11.0%, bachelorette 8.7% | BYOB 12.6%, gators 11.8%, 97.9% five-star. One low-star about being left stranded after a shutdown |
| NOLA Booze Cruise (nbc) | 117 / 214 | Friends 14.5%, bachelorette 13.7%, birthday 9.4% | Highest bachelorette share of any listing. Visitors 16.2%. Listing ends Apr 2025 |
| NOLA Bike Bar (nbb) | 158 / 179 | Friends 15.2%, bachelorette 8.2%, birthday 7.6% | Drinks or BYOB 19%, guide named 46%. Low-star: noisy or rowdy other guests 4, rude 3. Ends Jun 2025 |

Sibling hypotheses worth a test that touch NPB:
1. **Bachelorette lives in the booze-cruise and bike-bar framing, not in the NPB listing.** NBC 13.7%, Tiki 8.7%, Bike Bar 8.2%, NPB 6.0%. If bachelorette ads are wanted, run them on the booze-cruise or tiki framing and send birthdays to NPB.
2. **Shared guides mean shared proof.** NKST, Admire NOLA and Crescent City name Nick and Alex. NPB, Hidden Adventure and Tiki name the same captains. Pool testimonials across listings (with the guide's OK) to lift the thinnest brands.

## Data gaps that touch NPB (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
| NPB and HPB reviews are short (median 14 to 15 words) | Party type is hidden in 75% of reviews. A post-trip one-question survey ("who did you come with, what was the occasion") would fix this |
| Seat price $59 vs $63 in NPB chats | Verify the live price, then update persona doc and AI instructions |
