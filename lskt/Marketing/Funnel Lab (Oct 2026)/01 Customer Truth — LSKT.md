*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for LSKT.*

# Customer Truth: LSKT (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| LSKT + AKT (Austin) | 242 / 301 | Families 9.5%, friends 8.3%, couples 6.6% | "How much?" 26% (LSKT chats, 73 shoppers) | Beginner fit and what is included (22% ask what the tour is) | Bats are named in 31% of reviews. "The bats were amazing, a completely unique, must-do experience!" |

## How to read this (method and limits)

> **CURRENT STATUS (verified 2026-10-15, live GBP API):** "LSKT reviews stop Jul 2024" below came from the legacy Lone Star listing (157 reviews). The live Lone Star Kayak Tours listing at 200 E Riverside has 527 reviews (4.9 avg, latest 2026-10-12) and was not in the lab's cache, so every Austin review percentage in this file is a floor computed on 242 of roughly 670 Austin reviews with text. Recent LSKT low stars (Sep-Oct 2026): paid parking lot surprise, one guide for 10-12 boats, thin narration and no red light on a bat tour.



- **Reviews**: GBP cache pulled Oct 14 2026. Percentages are of reviews with text. A review can match several segments. Matching is keyword regex, so treat every % as a floor, not a census.
- **Thin text**: NPB median review is 15 words. Only 24% of NPB reviews name a party type at all. HPB, DCKT and Austin are similar (17 to 28%). "Segment %" means "of all reviews", and I also give how many named any party type.
- **NPB skew**: 2,211 of 3,944 NPB reviews came in 2024 alone (a review-request push). Last 12 months is only 127 NPB reviews with text. Recent splits are flagged with n.
- **Chats**: OpenCX transcripts cover Apr 20 to Oct 6 2026. I removed spam (17 LSKT, 11 across DCKT, HPB and NPB), job seekers, post-booking issues and empty sessions before counting "shopper" questions.
- **No click data exists in the cache.** "Ended without a booking link or contact" is a proxy: no booking URL sent by the AI and no email or phone given by the shopper. A shopper could still have booked on their own.
- **Sources missing**: E&E, AKT and all sibling brands have no OpenCX workspace in the cache. Their question data is a review proxy and is labeled that way.
- **Guide-name shares** are first-name matches against names found in the reviews. Treat as an upper bound.
- **Austin**: LSKT reviews stop Jul 2024 and AKT starts Mar 2024. Treated as one Austin lane. The LSKT chat workspace is the only Austin chat source.
- Methods and scripts: `/private/tmp/claude-501/ct-scripts/` (rev.py, chatrun2.py, extras.py).

## Cross-brand patterns that name LSKT (from file 01)

| Pattern | Evidence |
|:-|:-|
| Price is rarely mentioned in reviews, constantly in chats | Reviews mentioning price: NPB 2.8%, DCKT 2.7%, NKST 6.8%. Chats mentioning price: NPB 62%, LSKT 33%, NKST 28%, HPB 32%, DCKT 21% |
| Shared staff across listings | Admire NOLA reviews name the same guides as NKST (Nick, Alex, Ryan). Hidden Adventure names NPB captains (Daddy, Badass, Pip). Austin Paddle Shack names the same guides as LSKT (Rives, Connor, Anne) |

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

## Related sibling listings (rows from file 01, Siblings and smaller listings)

These have no chat workspace. All numbers are from reviews only.

| Listing | Reviews with text / total | Top segments (% of reviews) | What stands out |
|:-|:-|:-|:-|
| Austin Paddle Shack (+ Austin Party Barge) | 341 / 408 | Friends 10.9%, family 4.7%, couples 3.5% | First-timer 10.6%, easy 11.4%, guide named 52% (Rives 40, Connor 23, Adam 19). Same guides as LSKT |

Sibling hypotheses worth a test that touch LSKT:
2. **Shared guides mean shared proof.** NKST, Admire NOLA and Crescent City name Nick and Alex. NPB, Hidden Adventure and Tiki name the same captains. Pool testimonials across listings (with the guide's OK) to lift the thinnest brands.

## Data gaps that touch LSKT (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
| No OpenCX workspace for E&E, AKT, and the siblings | No pre-booking question data. E&E and AKT are the priority |
