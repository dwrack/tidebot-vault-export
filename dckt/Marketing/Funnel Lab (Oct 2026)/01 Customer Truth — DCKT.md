*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for DCKT.*

# Customer Truth: DCKT (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| DCKT (Door County) | 912 / 1,015 | Families with kids, 7.2% (11.5% in last 12 months) | Kids, age, pets, 24% of first questions (110 shopper chats) | Can my kids, dog or heavier guest come. 42% of chats | 20% of reviews name Cave Point. "Great experience for the whole family!" |

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

## Cross-brand patterns that name DCKT (from file 01)

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Almost nobody writes about fear | "Nervous / scared / first time kayaking" language: NKST 3.1%, DCKT 2.7%, BBK 4.2%, NPB 0.6%, HPB 0.5%. Beginners are a bigger group (BBK 9.1%, Austin 9.9%) than the fearful |
| Price is rarely mentioned in reviews, constantly in chats | Reviews mentioning price: NPB 2.8%, DCKT 2.7%, NKST 6.8%. Chats mentioning price: NPB 62%, LSKT 33%, NKST 28%, HPB 32%, DCKT 21% |
| Reviews skew visitors, not locals | Tourist language vs local language: NPB 7.2% vs 0.2%, NKST 13.7% vs 2.2%, DCKT 4.1% vs 0.3%. Exception: E&E talks like a local product (Portland mentioned in 21%, tourists 3.5%) |
| Low-star reviews are about operations, not the experience | Cancel, refund, no-show, weather, communication lead the low-star lists for NPB, HPB, BBK, DCKT and Austin |

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
- **"800+ five-star reviews."** GBP now shows 1,015 reviews, 973 of them five-star. Vault docs fixed to "1,000+" on 2026-10-15; live site still to check (see Start Here).
- **Objection list** (never kayaked, rain, safe for kids and seniors, "worth $59"). Missing from it: pets, toddler-in-tandem, and weight limits, which top the chats.
- **Price weight.** The map treats "is it worth it" as a core objection. Price is 2.7% of reviews and 14% of first questions (3rd).
- **Wildlife hooks.** Not supported (1.5%).
- **Chatbot line** names a past vendor. Transcripts now come from OpenCX.
- **Agrees**: beginner reassurance matters (first-timer 6.9%).

## Related sibling listings (rows from file 01, Siblings and smaller listings)

These have no chat workspace. All numbers are from reviews only.

| Listing | Reviews with text / total | Top segments (% of reviews) | What stands out |
|:-|:-|:-|:-|
| Cave Point Paddle and Pedal (cppp) | 241 / 306 | Family 10.0%, first-timer 7.1%, friends 4.6%, couples 4.1% | Fun 28.6%, scenic 10.4%. Guide named 35%. Low-star: "long paddle with nothing to see" |
| Door County Detours | 33 / 43 | Too thin | Not analyzed further |

Sibling hypotheses worth a test that touch DCKT:
3. **Cave Point Paddle and Pedal is the family sibling of DCKT** (family 10.0% vs 7.2%). Test the DCKT kids, pets and weight answers on the CPPP page too.

## Data gaps that touch DCKT (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No click or conversion data from chats | Cannot say how many chats became bookings. Add a booking-link click event or tag in OpenCX |
| DCKT chat has 65 unclear sessions | Email form replies are mixed with staff replies. A cleaner export would sharpen the kids and availability counts |
