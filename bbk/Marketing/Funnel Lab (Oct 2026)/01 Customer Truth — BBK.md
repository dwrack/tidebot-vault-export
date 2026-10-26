*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for BBK.*

# Customer Truth: BBK (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| BBK (Buffalo Bayou) | 570 / 597 | Couples 10.0%, family 8.8%, friends 7.7% | Too thin. 8 shopper chats, 3 asked price | Dirty water. 14 of 27 low-star reviews, 6.7% of all | 70% of reviews name a guide. "Totally different view of the city from the water!" |

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

## Cross-brand patterns that name BBK (from file 01)

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Almost nobody writes about fear | "Nervous / scared / first time kayaking" language: NKST 3.1%, DCKT 2.7%, BBK 4.2%, NPB 0.6%, HPB 0.5%. Beginners are a bigger group (BBK 9.1%, Austin 9.9%) than the fearful |
| Low-star reviews are about operations, not the experience | Cancel, refund, no-show, weather, communication lead the low-star lists for NPB, HPB, BBK, DCKT and Austin |

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
