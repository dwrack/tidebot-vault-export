*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NKST.*

# Customer Truth: NKST (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| NKST (Swamp Tours) | 1,303 / 1,426 | Friends 6.6%, couples 5.6%. Visitors 13.7% vs locals 2.2% | "Where do we meet?" 29% of first questions (58 organic chats) | Getting to the swamp. Location or pickup in 43% of chats | 55% of reviews name a guide. "Highly recommend this tour, even for beginners!" |

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

## Cross-brand patterns that name NKST (from file 01)

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Almost nobody writes about fear | "Nervous / scared / first time kayaking" language: NKST 3.1%, DCKT 2.7%, BBK 4.2%, NPB 0.6%, HPB 0.5%. Beginners are a bigger group (BBK 9.1%, Austin 9.9%) than the fearful |
| Price is rarely mentioned in reviews, constantly in chats | Reviews mentioning price: NPB 2.8%, DCKT 2.7%, NKST 6.8%. Chats mentioning price: NPB 62%, LSKT 33%, NKST 28%, HPB 32%, DCKT 21% |
| Reviews skew visitors, not locals | Tourist language vs local language: NPB 7.2% vs 0.2%, NKST 13.7% vs 2.2%, DCKT 4.1% vs 0.3%. Exception: E&E talks like a local product (Portland mentioned in 21%, tourists 3.5%) |
| Shared staff across listings | Admire NOLA reviews name the same guides as NKST (Nick, Alex, Ryan). Hidden Adventure names NPB captains (Daddy, Badass, Pip). Austin Paddle Shack names the same guides as LSKT (Rives, Connor, Anne) |

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

## Related sibling listings (rows from file 01, Siblings and smaller listings)

These have no chat workspace. All numbers are from reviews only.

| Listing | Reviews with text / total | Top segments (% of reviews) | What stands out |
|:-|:-|:-|:-|
| Admire NOLA (4 listings) | 428 / 569 | Friends 6.8%, family 4.7%, birthday 4.2%, couples 3.7% | Gators 17.1%, wildlife 28%, learning 37%. Guides named: Nick 41, Alex 26, Ryan 15, the same people as NKST. Recent n=17, too thin for a recent split |
| Honey Island Swamp Kayak Tour | 12 / 14 | Too thin to call | Visitors 5 of 12, guide Jess in 4. Learning language in 10 of 12 |
| Crescent City Kayak (cck) | 82 / 96 | Family 6.1%, couples 2.4%, friends 2.4% | Reviews end Apr 2024. Gators 30.5%, wildlife 50%, scenic 18%. Nick named in 34 (a NKST guide again) |

Sibling hypotheses worth a test that touch NKST:
2. **Shared guides mean shared proof.** NKST, Admire NOLA and Crescent City name Nick and Alex. NPB, Hidden Adventure and Tiki name the same captains. Pool testimonials across listings (with the guide's OK) to lift the thinnest brands.

## Data gaps that touch NKST (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
