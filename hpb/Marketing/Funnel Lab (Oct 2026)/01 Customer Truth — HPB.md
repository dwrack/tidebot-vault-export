*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for HPB.*

# Customer Truth: HPB (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| HPB (Houston Pedal Barge) | 784 / 983 | Friend groups 18.0% (31% of the last 35 reviews) | "How much?" 27% (37 shopper chats, thin) | Weather cancels and slow refunds. 17 of 19 low-star reviews | 43% of reviews name a captain. "This is a must do when you're in Houston." |

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

## Cross-brand patterns that name HPB (from file 01)

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Almost nobody writes about fear | "Nervous / scared / first time kayaking" language: NKST 3.1%, DCKT 2.7%, BBK 4.2%, NPB 0.6%, HPB 0.5%. Beginners are a bigger group (BBK 9.1%, Austin 9.9%) than the fearful |
| Price is rarely mentioned in reviews, constantly in chats | Reviews mentioning price: NPB 2.8%, DCKT 2.7%, NKST 6.8%. Chats mentioning price: NPB 62%, LSKT 33%, NKST 28%, HPB 32%, DCKT 21% |
| Low-star reviews are about operations, not the experience | Cancel, refund, no-show, weather, communication lead the low-star lists for NPB, HPB, BBK, DCKT and Austin |

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

## Data gaps that touch HPB (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
| NPB and HPB reviews are short (median 14 to 15 words) | Party type is hidden in 75% of reviews. A post-trip one-question survey ("who did you come with, what was the occasion") would fix this |
