*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for E&E.*

# Customer Truth: E&E (split from file 01)

## Top table row

| Brand | Reviews analyzed (with text / total) | #1 buyer segment | #1 pre-booking question | #1 objection | Strongest proof line |
|:-|:-|:-|:-|:-|:-|
| E&E (Portland floating sauna) | 115 / 125 | Friend groups 14.8%, couples 7.8% | No chat workspace exists. Proxy: how to get there and park, 17% of reviews | Thin. River current safety (3 reviews), day-of access (20 mention it) | 95.2% five-star in its first year. "Such a perfect way to end a river day." |

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

## Cross-brand patterns that name E&E (from file 01)

| Pattern | Evidence |
|:-|:-|
| The guide is the product on the tour brands | Reviews that name a guide: BBK 70%, NKST 55%, DCKT 52%, Austin Paddle Shack 52%, HPB 43%, NPB 32%. E&E 0% (nobody to name) |
| Reviews skew visitors, not locals | Tourist language vs local language: NPB 7.2% vs 0.2%, NKST 13.7% vs 2.2%, DCKT 4.1% vs 0.3%. Exception: E&E talks like a local product (Portland mentioned in 21%, tourists 3.5%) |

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

## Data gaps that touch E&E (rows from file 01, Data gaps to fix)

| Gap | Why it matters |
|:-|:-|
| No OpenCX workspace for E&E, AKT, and the siblings | No pre-booking question data. E&E and AKT are the priority |
| E&E sample is 115 reviews | Re-run in 6 months |
