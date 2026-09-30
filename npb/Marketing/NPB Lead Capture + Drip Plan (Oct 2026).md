# NPB Lead Capture + Drip Plan (Oct 2026)

*Written 2026-09-30, revised same day. Replaces the GHL plans ([[Abandoned Cart - GHL Sequence Plan]], [[GHL Copy Review — Rawgrowth]], the Rawgrowth "Lead Capture" sequence). The engine is our own: `~/Projects/fh-lead-engine`.*

**The one-line version:** make `fh-lead-engine` the one CRM. Swap the dead giveaway for **"The NOLA Countdown"**, a party planning guide delivered as a drip timed to *their* trip date. Every chapter is a blog post on our site, featuring local spots we actually like. A **$50 off a private boat** code rides along in the P.S. with a hard expiry.

---

## 1. What exists today

| # | Piece | State |
|---|---|---|
| 1 | **Top banner** "Not ready to book yet? Get early access" → `/new-orleans-booze-cruise-giveaway/` | **Still live, still a GHL form.** No prize listed, says "Nola Pedal Barge", 18+ terms, no follow-up. 8,023 impressions, 1 click. |
| 2 | **fh-lead-engine** (popup, capture API, DynamoDB `fh-leads`, 15-min drip runner, SES, per-brand unsub) | Built Sep 29. NPB `enabled: false`, generic placeholder copy. Target **Oct 20**. |
| 3 | **Weekly winback reel email** (SendGrid, info@nolapedalbarge.com, 36,621 past guests) | Running on davids-mbp-2. Sends Oct 6, 13, 20, 27, Nov 17. **Separate unsub list.** |
| 4 | **OpenCX chat** | 986 sessions / 90 days, ~6% of non-email chats leave contact info. Nudge v2 waiting on approval. |
| 5 | **hpb-customer-db** (Supabase) | Never committed. Overlaps the engine. Retire it. |
| 6 | **Old lists** (36,621 CSV, 3,749 MailerLite contest, GHL form signups) | Spread across 3 tools. |

**Gaps:** no booking sync (FH Public API key not created), two unsubscribe lists, two sender domains, no MAIL-FROM/DMARC on nolapartybarges.com, and **wp-admin is down** (siteurl -dummy host bug, FH tickets open).

---

## 2. Where it's going

```
 Banner / popup / guide site / OpenCX ─► engine /capture ─► fh-leads (one CRM)
                                                              │  lead → booked → guest → lapsed
 FareHarbor bookings ── daily sync ───────────────────────────┘
                                                              ▼
                        The NOLA Countdown (trip-date drip) → weekly reel newsletter
```
One table, one unsubscribe list, one sender domain (nolapartybarges.com). Retire hpb-customer-db.

---

## 3. The offer: $50 off a private boat, with an expiry

**Can FareHarbor do it? Yes, it should, and we confirm it in the dashboard before we build around it.** FareHarbor discount codes live under Campaigns and let you set:
- a **flat amount** ($50),
- **which items** it works on (limit it to the private charters so it never touches $63 public seats),
- **valid dates** for when it can be redeemed, which is the expiry, plus blackout dates (Mardi Gras, NYE if we want),
- a redemption cap.

(FareHarbor's help articles on this are login-only, so read "Reference: Discount code settings" while signed in to confirm.)

**Two things to test before launch:**
1. **Deposits.** Private charters take a $350 deposit with the balance due on the day. Book a test to confirm the $50 comes off the total and not something odd with the deposit.
2. **The luxury pontoon** ($350, up to 6). $50 off that is 14%. Leave it out of the code unless you want it in.

**How "they can't sit on it" works:**
- FareHarbor codes are shared, not one per person. So we run **rolling codes**: a new code each month (`CREW50-NOV`, `CREW50-DEC`...), each with a hard end date in FareHarbor. Once it's dead, it's dead.
- Every lead gets whichever code has 14+ days left. The engine already supports this ("waves" in `brands.json`, `min_days_left`).
- The email always says the date: "Good on any private boat booked by Nov 30. Ride any date." They have to book by then, but the trip can be months later.
- **Early planners (trip 45+ days out) don't get the code up front.** It shows up 45 days before their trip, so the clock starts when they're actually ready to decide.
- Gift cards aren't included in this version. That's a separate holiday offer if you want one.

Engine change: `gift_amount: 50`, the terms say private charters only, and `waves` gets the monthly codes.

---

## 4. The NOLA Countdown (the drip)

**The idea:** they're excited about their trip, so give them something to look forward to. It's not a PDF and it's not a pitch. It's a countdown to *their* weekend, written by locals, one chapter at a time. Every email should be worth opening even if they never book a boat.

**Every email looks the same, so people learn it:**
1. **The countdown:** "23 days till New Orleans" (from the trip date they gave us).
2. **One chapter:** 3-5 short lines, funny, local, specific, with a "read the full chapter" link to a blog post on nolapartybarges.com.
3. **Crew's Pick:** one local business we love and why, in one line ("Best po'boy within a 5-minute walk of the Quarter"), linking to them.
4. **The boat, in one line.** Never the main event.
5. **P.S.** the $50 code and its end date, only while it's live.

Signed by a real crew member, not "Team". Short enough to read at a red light.

**The chapters.** They're timed to the trip date. Early planners get the first few spaced weekly, then the countdown kicks in.

| # | When | Subject line (draft) | Chapter | Links (✅ = exists, 🆕 = write, 🔄 = refresh) |
|---|---|---|---|---|
| 1 | Right after signup | "You're going to New Orleans." | Short welcome + **3 tap-to-answer questions** (see 4b). Nothing else. | none |
| 1b | +1 day | "Paste this in the group chat" | **The group chat paste**, personalized with what they told us | 🆕 First-Timer's 48 Hours |
| 2 | +2 days | "How many days is enough? (and what it costs)" | Days and budget, honestly | ✅ /1253-2/ (How many days), ✅ /how-much-do-you-need-to-budget.../ (our #1 post, 41k impressions) |
| 3 | +5 days | "Where to crash with a crew" | Neighborhoods for groups: Marigny, Lower Garden District, near-Quarter | 🆕 Where to Stay in New Orleans With a Group |
| 4 | 6 weeks out | "What's happening the weekend you're here" | Festivals, parades, games, second lines, **for their month** | 🆕 New Orleans Events by Month (evergreen, update yearly), 🔄 Krewe of Endymion 2023 → Mardi Gras 2027 parade guide (14k impressions, 1 click) |
| 5 | 4 weeks out | "The boat day, hour by hour" | What happens out there: BYOB, bathroom onboard, 7 miles from the Quarter, sunset vs afternoon. **Code reminder.** | ✅ /bayou-party-cruise-new-orleans-what-to-expect/, ✅ /what-time-of-day-is-best.../, ✅ /closest-alligator-swamp-tour-french-quarter.../ |
| 6 | 3 weeks out | "Eat like you live here" | Crew's picks: brunch that takes 12+, po'boys, late-night | 🔄 Best Restaurants in New Orleans for 2020 → 2027, 🆕 Brunch Spots That Take Big Groups |
| 7 | 2 weeks out | "What to wear (it's not what you think)" | Weather for their month, dress codes, shoes for cobblestones | ✅ /exploring-december-weather.../ (40k impressions), ✅ /unveiling-the-charm-do-new-orleans-bars-have-a-dress-code/, 🆕 What to Wear in New Orleans, Month by Month |
| 8 | 10 days out | "Bourbon is the appetizer" | Frenchmen vs Bourbon, where locals actually go out, daiquiri shops ranked | 🆕 Frenchmen vs Bourbon: A Local's Night Out, 🆕 Daiquiri Shops Ranked, ✅ /beyond-bourbon-street.../ |
| 9 | 7 days out | "The pack list" | What to bring, the BYOB boat list, matching shirts, what to leave home | ✅ /byob-what-to-pack-new-orleans-booze-cruise/, 🆕 Bachelorette Themes That Aren't Tacky (+ local shirt printers) |
| 10 | 3 days out | "Your New Orleans forecast" | Their actual forecast, the rain plan, getting around (streetcar, Uber, how far the boat is) | 🆕 Rainy Day Plan for New Orleans, 🆕 Getting Around New Orleans With a Group |
| 11 | Arrival morning | "Welcome home, sort of" | Day-one plan, hangover cures, emergency beignets | 🆕 The New Orleans Hangover Recovery Guide |
| 12 | 2 days after the trip | "How'd we do?" | Share photos, tag us, the review ask if they rode, "tell a friend who's planning one" | none |
| then | Monthly | Weekly reel newsletter | Long nurture until they're back or unsubscribe | none |

**Branching (the engine handles it):**
- **Occasion tag** from email 1 swaps in the right post: bachelorette → ✅ /a-locals-itinerary-for-a-new-orleans-bachelorette-party/, bachelor → ✅ /bachelor-party-booze-cruise-new-orleans-bayou/, birthday → ✅ /milestone-birthday-private-party-boat-new-orleans/, girls' trip → ✅ /girls-weekend-party-boat-new-orleans/, wedding → ✅ /wedding-welcome-party-cruise-new-orleans/.
- **Season** swaps in Halloween (✅ /halloween-party-boat-cruise-bayou-new-orleans/), NYE (✅), Mardi Gras (✅ /mardi-gras-alternative-party-boat-new-orleans/), winter (✅ /heated-winter-swamp-tours-new-orleans/).
- **No trip date yet:** chapters 1-3 go out weekly, then "Picked your dates yet?" with one-click month buttons that set the date and start the countdown.
- **Trip less than 3 weeks out:** skip ahead, send only the chapters that still fit, 1 per day max.
- **Books a boat:** the drip keeps going (it's still useful!) but the code P.S. drops out and the boat line becomes "see you on the bayou." That's the only drip people will be sad to see end.

**Hard rules:** max 1 email a day, 50 new enrollments a day, stops on unsubscribe, no email reads like "just circling back."

---

## 4a. It changes with when they're coming

The signup form asks **"When are you coming?"** with four options. The drip behaves differently for each one, and each version slowly nudges them one step closer to exact dates.

| They picked | What they get | The quiet ask |
|---|---|---|
| **Exact dates** | Full countdown ("23 days till New Orleans"), chapters timed to the trip | none, they're locked |
| **A month** ("March 2027") | Countdown to the month ("About 5 months out"), chapters about that month: weather, events, what's blooming or parading | "Got exact dates yet?" as tap buttons for each weekend in that month |
| **Just a year** ("Sometime in 2027") | A slower track, about one email every 10 days, leaning on seasons: "New Orleans in spring vs fall" | "Which season's calling you?" Tapping a season → "Which month?" |
| **Just exploring** | Same slow track, more "why New Orleans" and less countdown | "Is this a real trip or a daydream? (Both are fine.)" → Real / Maybe / Daydream |

When they answer, they move up a row, and the next email switches to the new track on its own. The copy shifts from "someday" words to countdown words. Nobody gets told "you've been moved to a new sequence."

---

## 4b. Getting to know the group (every tap updates the CRM)

**Yes, it can.** The engine already signs every unsubscribe link with a secret key, so each person's link only works for them. We use the same trick for two new kinds of links:

1. **Answer links** (`/a`). Each answer button in an email is a link: "Bachelorette", "6-12 people", "March". One tap saves it to their CRM record and opens a small page: "Got it, bachelorette crew 🎉". That page shows **the other unanswered questions as buttons**, so one tap often turns into three answers. Tapping a different answer later overwrites the old one.
2. **Tracked links** (`/c`). Every other link (blog posts, Crew's Picks, the boat) goes through the engine first, which logs it and then sends them on. Clicking the brunch post tags them `foodie`. Clicking the boat pricing twice tags them `hot`.

**What gets saved on each lead:**
| Field | Filled by |
|---|---|
| name, email, phone, sms_consent (+ time, IP, wording) | Signup form |
| trip_when (exact dates / month / year / exploring), trip_date | Form, then taps |
| group_type (bach, bachelor, birthday, girls' trip, guys' trip, couples, family, work, just because) | Welcome email tap |
| group_size (2-5, 6-12, 13-20, 21+) | Welcome email tap |
| first_time_nola (yes / no) | Welcome email tap |
| planner (me / group chat / someone else) | Email 2 P.S. |
| staying_in (Quarter, Marigny, CBD/Warehouse, Garden District, not booked) | Email 3 |
| vibe (full send / chill / little of both) | Email 5 |
| boat_time (morning / afternoon / sunset) | Email 5 |
| excited_for (food / music / the boat / parades / gators) | Email 6 |
| interests (foodie, nightlife, nature, budget...) | Automatic, from which links they click |
| hot flag | 2+ boat clicks. **Pings the manager** so a real human follows up. |

**How the answers change the emails:**
- group_type picks the occasion posts, the Crew's Pick, and the jokes. A bachelorette crew and a family reunion get different emails.
- group_size picks which boat gets the one-line mention (18 → Bayou Boogie, 25 → Party Queen / Tikis) and makes the cost-split math real: "$X each for your 14."
- staying_in makes "Getting Around" about *their* trip: "From the Marigny it's a 15-min Uber to the dock."
- **One question per email, max, and it's always the last line.** Never a survey, always something they'd enjoy answering.

**SMS, done right:**
- The signup form has email (required), phone (optional), and **a separate, unchecked** box: "Text me trip reminders and the forecast before I go. Msg & data rates may apply. Reply STOP to opt out." Consent time, IP, and exact wording get saved.
- If they skip it, email 10 asks once: "Want your forecast by text the morning you land?" That opens a small page with a phone box and the same checkbox. A tap alone doesn't count as SMS consent. They have to enter their number and check the box.
- Nothing texts until the toll-free (888-618-9606) or A2P verification clears.

**Honest gotchas:**
- **Link scanners.** Some work email systems (Outlook, Mimecast) click every link automatically. We ignore clicks in the first 60 seconds after sending and anything from known scanner bots. Answer taps only count from real browsers.
- **Opens are fake now.** Apple Mail pre-loads every email, so we never use opens for anything. Clicks and taps only.
- Add one line to the privacy policy: we remember your answers and which links you click, to make the emails more useful.

### Draft: welcome email (email 1)

> **Subject:** You're going to New Orleans.
> **Preview:** Three quick taps and we'll make these emails actually useful.
>
> Hey {first_name},
>
> You're in. Over the next few weeks we'll send you the stuff locals actually tell their friends: where to eat, where to go out, what to wear, and how not to waste a single hour of your trip.
>
> Help us make it about *your* trip. Three taps, no typing:
>
> **Who's coming?**
> [Bachelorette] [Bachelor] [Birthday] [Girls' trip] [Guys' trip] [Couples] [Family] [Work crew] [Just because]
>
> **How many of you?**
> [2-5] [6-12] [13-20] [21+]
>
> **First time in New Orleans?**
> [First time] [Been before] [I basically live here]
>
> That's it. Tomorrow: a message you can paste straight into the group chat.
>
> {crew_name}
> NOLA Party Barge
>
> P.S. {if code live} Your $50 off any private boat is good through {code_end}. Book any date, ride whenever. Code: {code}

*If they gave a month, year, or "exploring" instead of exact dates, the third question becomes **"When are you thinking?"** [This spring] [This summer] [This fall] [Next year] [No clue yet], and "first time?" moves to email 2.*

---

## 5. The blog plan (the SEO side)

The drip is also an SEO machine. Every chapter sends real readers to a post, and writing the chapters fills the gaps in the blog.

**Why it helps rankings (straight answer):** email clicks alone don't move Google much. What does:
1. **Refreshing old posts that already rank.** The 🔄 posts above have huge impressions and dead click-through. A refresh with a new year, new title, and real content is the fastest SEO win we have.
2. **A hub page** at `/nola-party-planning-guide/` on nolapartybarges.com that links to every chapter. That fixes internal links: 15 posts have zero inbound links and 78 have only 1-2.
3. **Local businesses linking back.** Everyone featured as a Crew's Pick gets a heads-up and a "Featured in the NOLA Party Planning Guide" line to share. Local backlinks and shares are the real prize.

**New posts to write (11), in priority order:**
1. First-Timer's 48 Hours in New Orleans (With a Group)
2. New Orleans Events by Month
3. What to Wear in New Orleans, Month by Month (builds on the 40k-impression December post)
4. Where to Stay in New Orleans With a Group
5. Frenchmen vs Bourbon: A Local's Night Out
6. Brunch Spots in New Orleans That Take Big Groups
7. Getting Around New Orleans With a Group
8. Rainy Day Plan for New Orleans
9. The New Orleans Hangover Recovery Guide
10. New Orleans Daiquiri Shops, Ranked
11. Bachelorette Themes That Aren't Tacky

**Refresh (4):** Best Restaurants 2020 → 2027, Krewe of Endymion 2023 → Mardi Gras 2027 parade guide, 2023 Halloween Things to Do → 2026, Nola Party Planning Tip #1 (2019) → fold into the hub and redirect.

**Refresh calendar (dated posts get rewritten with verified facts, never just a year swap):**

The WordPress REST API works with the admin app password (tested 2026-09-30), so these can ship even while the wp-admin screen is broken. The URL stays the same. Where a slug has a year in it, we create a new clean URL and 301 the old one.

| Post (id) | Now | Refresh to | Publish by | Why then |
|---|---|---|---|---|
| 2023 Halloween Things to Do (1077) | 2023 events, 786 words | **Halloween in New Orleans 2026** (new slug `/halloween-new-orleans/`, 301 old) | **Oct 6, 2026** | Halloween searches peak in October. It's late already. |
| Krewe of Endymion New Parade Route for 2023 (998) | 167 words, 2023 route | **Mardi Gras 2027 Parade Guide for Party Groups** (Endymion + the top krewes, dates, where to watch) | **Dec 1, 2026** | Mardi Gras is Feb 9, 2027, and trip planning starts in December. 14k impressions, 1 click. |
| Best Restaurants in New Orleans for 2022 (392) | 2019 Instagram embeds, some places likely closed | **Best Restaurants in New Orleans for Groups (2027)** with Crew's Picks + researched list | **Nov 1, 2026** | Needs Jeff/JT picks first. |
| How much to budget for New Orleans in 2026 (1230) | 329 words | Same post, 2027 prices, real per-person boat math | **Jan 2, 2027** | Our #1 post (41k impressions). Update it every January. |
| Exploring December Weather (40k impressions) | undated | Add "2026" in the title, a month-by-month link to the new What to Wear post | **Nov 15, 2026** | Before December searches spike |
| NYE / Mardi Gras alternative / Spring Break posts | undated, 2026-07 | Add the 2027 dates and events | NYE: Dec 1 · Mardi Gras: Dec 15 · Spring Break: Feb 1 | Each before its search season |

**Yearly repeat (goes on the NPB calendar):** Halloween → Sept 15 · Mardi Gras → Nov 15 · Budget → Jan 2 · Restaurants → Jan 15 · NYE → Nov 15 · Spring Break → Jan 15. Each refresh: re-verify every business is still open, update dates, bump the title year, and send it through the drip.

**Leave out of the guide:** the ~15 Baton Rouge posts. They're on a New Orleans boat's site and don't fit a New Orleans trip. That's worth a separate look.

**Crew's Picks: David's list needed.** One or two per category, places we genuinely send people: brunch, po'boy, daiquiri, late-night food, live music bar, beignets/coffee, group-friendly hotel, photographer, shirt printer, cake/bakery. Around 12 total, one per email.

---

## 6. Where it shows up

| Spot | Copy |
|---|---|
| Top banner | "Coming to New Orleans? Get the free NOLA Countdown + $50 off a private boat" |
| Popup widget | Same offer, shows once, snoozes |
| Hub page `/nola-party-planning-guide/` | Signup box at the top |
| Top blog posts (budget, December weather, bachelorette itinerary) | Inline signup box. These get the traffic. |
| OpenCX bot | After a price answer: "Want the NOLA Countdown? It's a local's guide to your trip, and there's $50 off a private boat in it." Asks for email. |
| Old giveaway URL | 301 to the hub |

**Form:** first name, email, "When are you coming?" (exact dates / a month / just a year / just exploring), phone (optional) with a separate unchecked SMS consent box. Everything else gets asked later, one tap at a time (4b).

---

## 7. Build order

| # | Task | Owner | By |
|---|---|---|---|
| 1 | Export everything from GHL | David | Oct 3 |
| 2 | FareHarbor Public API key for `neworleanspedalbarge` | David | Oct 3 |
| 3 | **Crew's Picks list** (about 12 local spots) + which crew name signs the emails | David | Oct 7 |
| 4 | FH: create the `CREW50` code, private items only, test with a deposit booking | David / FH | Oct 10 |
| 5 | Get wp-admin back (or have FH swap the banner and add the header script) | David / FH | Oct 10 |
| 6 | MAIL-FROM + DMARC on nolapartybarges.com | Claude | Oct 7 |
| 7 | Booking sync (daily, davids-mbp-2) + shared unsubscribe list across the engine and winback | Claude | Oct 14 |
| 8 | Engine: `trip_when`/`trip_date` + 4 timing tracks, `/a` answer links + `/c` tracked links (signed, scanner-filtered), profile fields, interest tags, hot-lead ping, occasion/size/season swaps, monthly code waves | Claude | Oct 14 |
| 8b | Privacy policy line about remembering answers and clicks | David / wp-admin | Oct 17 |
| 9 | Write emails 1-12 + the group chat paste. Draft → David approves. | Claude | Oct 14 |
| 10 | Refresh the 4 old posts + write the first 4 new posts (the ones chapters 1-7 need) | Claude drafts | Oct 17 |
| 11 | Hub page + 301 the giveaway URL | Claude + wp-admin | Oct 17 |
| 12 | Tests: simulator signup, David test, test booking stops the code P.S. | Claude | Oct 18 |
| 13 | **NPB live: banner + popup + drip** | Claude | **Oct 20** |
| 14 | Remaining 7 new posts, about 2 a week | Claude drafts | Nov 15 |
| 15 | Crew's Picks outreach ("you're in our guide"), from the manager, not David | Draft → approve | Nov 1 |
| 16 | OpenCX email ask + Nudge v2 | David approves | Oct 24 |
| 17 | Old lists → CRM as `lead`, newsletter only, no drip | Claude | Oct 27 |
| 18 | Monthly report | Claude | Nov 1 |

Nothing sends to a real list without David's OK on the copy and a test send.

---

## 8. How we know it's working

| Metric | Now | 60-day target |
|---|---|---|
| Signups per week | ~0 | 40+ |
| Countdown email open rate | - | 50%+ (it's expected mail, it should beat 40%) |
| Clicks to blog chapters per email | - | 8%+ |
| Lead → private charter booking within 90 days | unknown | 5%+ |
| `CREW50` redemptions | - | tracked monthly in FH |
| Clicks on refreshed posts (GSC) | budget 378, Dec weather 154, Endymion 1 | up 2x in 90 days |

---

## 9. Decisions for David

1. **Crew's Picks:** your ~12 local favorites.
2. **Who signs** the emails (a real crew name).
3. **Pontoon in or out** of the $50 code?
4. **Blackout dates** on the code (Mardi Gras weekend, NYE)?
5. **Retire hpb-customer-db** → yes (recommended).
6. **Move the winback** to nolapartybarges.com after Nov 17 → yes (recommended).
