# 10 Local Family Boat Giveaway: Meta ad + capture funnel (2026-10-16)

> **2026-10-21 decision (David):** draw moved to **Tuesday, Nov 24, 6pm**; close Mon Nov 23; redraw Tue Dec 1.


*Drafted 2026-10-16 by David's Claude from David's ask plus the Hormozi clip (golf-cart store: give the souped-up cart to one family in the hyper-local area, drawing in 30 days, second place gets something material, 72 hours to claim, pile on friction and qualifying questions on the way in, then follow up with the qualified ones). Nothing here is live. Anything marked [VERIFY] is unconfirmed and stays out of public copy until it is.*

**How this fits:** this is NOT a second contest. It replaces the November round of the Survey Contest Funnel (docs 01 to 03 in this folder). Same engine (`fh-lead-engine-capture`, branch `capture-v2`), same rules skeleton (doc 03), same codes. What changes: the audience goes hyper-local, the prize gets a face (one local family), the form gets heavier on purpose, phone + SMS consent gets added, second place is added, and the claim window drops to 72 hours because we'll have a phone number.

---

## 1. The offer in five lines

1. **Grand prize:** one New Orleans-area family gets a private tiki boat for a day. Up to 25 people, about 1 hour 45 minutes on Bayou Bienvenue with captain and deckhand, BYOB, Bluetooth, party lights. Value $1,200. $0 to the winner: no deposit, no booking fee, tip optional.
2. **Second place:** $500 toward any private boat, good 12 months, any date with availability. (David wrote "$500." Credit, not cash: costs us almost nothing, converts to a booking, and the winner brings 20 friends who become leads. If David wants cash, it's legal and allowed, just a 1099 and a dead-end lead. My call: credit.)
3. **Who can enter:** 21+, lives in Orleans, St. Bernard, Jefferson, St. Tammany, or Plaquemines Parish. Louisiana only. That alone kills the New York / Florida bond question from doc 03 for this round.
4. **Window:** entries open Thu Oct 22, drawing live on Facebook from the dock Tue Nov 24, 6:00pm CT (entries close Mon Nov 23, 11:59pm). Winner has **72 hours** to claim by text, email, or phone (we'll have all three). No claim, we redraw on air Tue Dec 1.
5. **Everyone else:** nobody "wins" anything (Louisiana R.S. 51:1723, see doc 03). Non-winners get an **offer** email on Wed Nov 25: $50 off a private boat, through Sun Dec 6, code `LOCAL50-NOV`, plus the per-person math for the group size they told us.

Total prize value $1,700. Under every state's $5,000 line.

---

## 2. Why hyper-local works better for us than for the golf-cart guy

- Our 2-year decline is volume, not price (FH deep dive, Jul 2026). Tikis are 74% of revenue. We sell groups, and locals are the people who have groups here.
- Locals book birthdays, reunions, cousin trips, office parties, Mardi Gras, and they rebook. Tourists book once.
- Private-boat buyers are planners. A giveaway form that asks "who's coming, when, what for" is literally the sales qualification call, filled out voluntarily.
- A 10-mile radius audience on Meta is cheap. Giveaway lead ads to a tight local radius typically run $1 to $4 per lead. $25/day for 30 days = $750 should return 250 to 600 leads with name, email, phone, ZIP, group size, occasion, and date. Compare: the last 30 days of paid + organic social sent 18,147 sessions and captured 0 emails (doc 07 audit, 10/13).

---

## 3. Meta ad: campaign build

**Account:** act_87863118. Pixel 701301873334767. Page 195245397959049. Instagram @nolapartybarge.

**Campaign:** `NPB | Local Family Boat Giveaway | Nov 2026`, objective **Leads**. Budget $25/day campaign-level (Advantage campaign budget), Oct 21 to Nov 23. Cap at $900 total.

**Two ad sets (split test the door, same creatives):**

| Ad set | Door | Why it's in |
|:-|:-|:-|
| A. Landing page | Engine page `nolapartybarges.com/boat/` (iframe to the engine, like `/plan/` in doc 07) | Full control: TCPA-grade SMS consent, our own lead record, pixel `Lead` event, result page with the per-person math. This is the one we want to win. |
| B. Instant Form | Meta Instant Form, **Higher intent** type (adds a review step), same questions as custom questions, leads pulled by the Meta Leads webhook into the engine | Lower friction = cheaper leads, lower quality. Runs to benchmark CPL. If A is within 2x of B's CPL, kill B. |

**Targeting (both):** location = people living in a 10-mile radius pin on the dock [VERIFY dock address for the pin] PLUS the ZIPs below. Age 25 to 64. No interest stacking; let the creative do the filtering. Advantage+ placements. Exclude: nothing. Past guests are great entrants.

ZIP list for the radius and the ad copy: 70117, 70116, 70119, 70122, 70124, 70126, 70127, 70128, 70129, 70043, 70032, 70075, 70085, 70001, 70002, 70005, 70006.

**Custom audience to build on day 1:** all entrants (upload weekly). Day 15: a 1% lookalike of entrants, Louisiana only, for a second ad set if CPL under A is below $3.

**Conversion signal:** pixel `Lead` on the thank-you step (door A), Meta lead event native (door B). Engine fires Meta CAPI Lead too (build item 1 in doc 07) so iOS leads count.

**Compliance in the ad (Meta Pages promotion policy, read 2026-10-03):** no "share to enter," no "tag a friend to enter," no bonus entries for anything social. Every ad carries "No purchase necessary. 21+. LA residents in the 5 parishes. Ends 11/23/26. Official Rules at nolapartybarges.com/boat/rules." Meta release line lives in the rules (doc 03 section 13).

---

## 4. The creatives (3 videos + 2 statics, shoot in one afternoon at the dock)

Shoot on a phone, vertical, real crew, no music bed over the talking. Jeff or JT on camera. Captions burned in. Each under 30 seconds.

**V1. "If you can see this dock from your house."** (primary)
Open on the boat at the dock, crew member walking into frame.
"If you live in Chalmette, Arabi, the Ninth Ward, Gentilly, the East, Metairie, anywhere about ten minutes from this dock, listen up. We're giving this whole boat to one local family. Free. Twenty-five of your people, close to two hours on the bayou, BYOB, your music. No deposit, no catch. We pull the name live right here November twenty-fourth. Takes a minute to enter, link's below."
On-screen text: ONE LOCAL FAMILY WINS THIS BOAT / DRAWING NOV 24 / 70117 70043 70122 70124 70001...

**V2. "Second place."**
Crew member holding up a hand-written sign "$500."
"Everybody asks what second place gets. Five hundred dollars toward your own private boat. Birthday, reunion, the cousins, your office party. Good for a year. First place gets the whole boat free. You in?"

**V3. "We're not shipping it to Ohio."**
"Most giveaways go to somebody three states away. Not this one. You have to live in Orleans, St. Bernard, Jefferson, St. Tammany or Plaquemines. We want a New Orleans family on this boat. That's it. Enter below."

**S1. Static:** wide shot of the tiki boat, big type: "ONE LOCAL FAMILY. ONE FREE BOAT. Drawing Nov 24." Small: "21+, LA residents, 5 parishes. No purchase necessary."

**S2. Static:** phone-screenshot style of the entry form with "Who's coming? [Family and the cousins ✓]" selected. Caption: "The entry form is basically planning the party."

**Primary text (all ads, 125 chars visible):**
"We're giving one New Orleans-area family a private tiki boat for a day. 25 people, about 1 hour 45 on the bayou, free. Drawing Nov 24. Enter in 60 seconds."

**Headline:** "One Local Family Wins the Boat"  |  **Description:** "No purchase necessary. 21+. Ends 11/23."  |  **CTA button:** Sign Up

---

## 5. The entry form (the friction is the point)

One question per screen, big tap buttons, progress bar. Order matters: easy and fun first, contact info in the middle once they're invested, consent last. Nothing is saved until the email screen is submitted. Every answer becomes a tag on the lead record and a swap block in the drip (doc 01 section 3 already defines `like`, `home`, `group_type`, `group_size`, `ride_when`; this adds the rest).

| # | Screen | Options | Field | Why we ask |
|:-|:-|:-|:-|:-|
| 1 | If you win, who's on the boat? | Family and the cousins / My friends / My coworkers / A mix of everybody | `group_type` | Opens the daydream. Office = corporate lead. |
| 2 | How many would you actually bring? | 2 to 6 / 7 to 12 / 13 to 18 / 19 to 25 | `group_size` | Boat fit + per-person math later |
| 3 | What would y'all be celebrating first? | Birthday / Graduation / Anniversary / Family reunion / Holiday party / Mardi Gras / No reason, we just like a boat | `occasion` | Drip branch |
| 4 | When would you take it out? | Before Christmas / Mardi Gras season / Spring 2027 / Summer 2027 | `ride_when` | Urgency score |
| 5 | Whose birthday is next in your crew? (month) | Jan ... Dec / Skip | `next_bday_month` | A dated reason to text them |
| 6 | Does your workplace do a holiday party? | Yes and we still need a spot / Yes, already booked / No / I don't know | `corp_holiday` | Routes to the corporate deck |
| 7 | Ever been on a party boat in New Orleans? | Never / Once / Y'all know me | `prior_boat` | Past guests vs new |
| 8 | First name + last name | text | `first_name`, `last_name` | |
| 9 | Email | text | `email` | Confirm-to-enter (doc 01 decision) |
| 10 | Mobile number | text | `phone` | Needed for the 72-hour claim. Say so on screen: "So we can text you if you win." |
| 11 | ZIP code | text, validated against the 5-parish list | `zip` | Eligibility + lets us check "close enough" |
| 12 | Two boxes, both unchecked | (a) required: "I'm 21+, I live in one of the 5 parishes, and I agree to the Official Rules." (b) optional, TCPA wording from doc 07: "Text me about the drawing and NOLA Party Barge offers (up to 4 msgs/mo, STOP to stop, msg & data rates apply)." | `rules_consent`, `sms_consent` + text, time, IP, source | Rules + separate SMS consent. SMS box is NOT a condition of entry. |

**Thank-you screen:** "You're in once you tap the email we just sent. One more thing while you're here:" then the per-person math for their group size on the boat they'd fit ("13 to 18 people on the Bayou Boogie is about $44 to $62 each") and a "Save this for the group chat" button that reuses the Group Chat Link from doc 07. No share-to-enter button anywhere.

**Instant Form version (door B):** questions 1, 2, 3, 4, 6 as custom multiple-choice, then name/email/phone/ZIP prefilled, rules checkbox as a required custom disclaimer, SMS as an optional custom checkbox. Meta caps the practical count around 8 to 10 before completion collapses, so 5, 7, 8 are dropped there.

---

## 6. Lead scoring and who gets a human

Score at submit, re-score on every tap.

| Points | For |
|:-|:-|
| +3 | ZIP in Orleans or St. Bernard (closest to the dock) |
| +3 | `ride_when` = Before Christmas |
| +2 | `group_size` 13+ |
| +2 | `corp_holiday` = Yes and we still need a spot |
| +2 | `sms_consent` = yes |
| +1 | `prior_boat` = Once or Y'all know me |
| +1 | `occasion` = Birthday with `next_bday_month` inside 60 days |

**8+ = hot.** Jeff gets a Slack line in #helm-npb with the name, group, date, occasion, and a suggested text. He texts from the business line (1056) within one business day: "Hey Marcus, Jeff at NOLA Party Barge. Saw you entered the boat giveaway with 15 for a December birthday. Good luck Tuesday, and if you'd rather not leave it to luck, I've got two Saturday slots left before Christmas. Want me to hold one 24 hours? No deposit till you say so." No guessing at scripts beyond this; David approves the wording first.

**4 to 7 = warm.** Drip only, plus the Nov 25 offer.
**0 to 3 = cold.** Confirm email, drawing reminders, the Nov 25 offer, then the win-back list.

---

## 7. Messages (email now, SMS once the toll-free sender clears)

SMS sending is off until the toll-free refile is verified (doc 07, memory). Consent gets collected now. Winner notice on draw night goes by a human text from 1056, which is 1:1 and fine.

| When | Channel | What | Branches on |
|:-|:-|:-|:-|
| 0 min | email | Confirm your entry (one tap). Subject: "Tap to lock in your boat entry" | none |
| after confirm | email | You're in. Here's the boat you'd fit + per-person math + the Group Chat Link | `group_size` |
| day 3 | email | Meet the boat: 45-second video, the route, the gators, what BYOB means on board | `occasion` echo line |
| day 7 | email | "What 25 of your people looks like on this boat" (photos by group type) | `group_type` |
| day 12 | email | Second place is $500. Here's what $500 covers for a group your size | `group_size` |
| day 18 | email (+SMS if live) | Holiday-party version for `corp_holiday`=need a spot; birthday version for next-60-day birthdays; everyone else gets Mardi Gras season dates | `corp_holiday`, `next_bday_month` |
| day 25 | email + SMS | "Drawing is Tuesday 6pm, watch live on Facebook" with the link | none |
| day 30, 5:45pm | SMS + email | Going live in 15 | none |
| draw night | human text + email + call | Winner: "You're the name we pulled..." 72-hour clock starts. Second place same. | |
| day 31 | email (+SMS) | Non-winners: thank you + the $50 offer + per-person math. Never "congratulations," never "you won." | `group_size` |
| day 45 | email | Offer expires in 48 hours | |
| day 60+ | email | Mardi Gras pre-sale to the whole list; corporate deck to `corp_holiday` yes-need-spot who didn't book | |

Email from `crew@` on the sending domain already set up for the engine. One-click hosted unsubscribe, URL List-Unsubscribe only. Unsubscribing never affects the entry (say so under the email field).

---

## 8. What else to do with it (ranked)

1. **Make the draw an event.** Facebook Live from the dock Tue Nov 24 6pm. Jeff pulls the name from a bucket on camera, calls the winner live on speaker (with their consent in the rules). Post the clip as the next ad. Entrants who tuned in are the warmest list we'll ever have.
2. **Neighborhood groups, organically.** Post the giveaway (no ad spend) in the Chalmette, Arabi, St. Bernard, Gentilly, Lakeview, Mid-City, Bywater/Marigny, Metairie Facebook groups from the business page or a crew member's own account. These groups are exactly the 10-mile radius and they're free. One post each, no reposting.
3. **QR at the dock + on the boats.** Every current guest can enter. A placard at check-in and on each boat's bar: "Locals: win this boat for your family. Scan." Captures the 60% of guests who are visitors too (they just won't be eligible; the form tells them and offers the Crew's Guide instead).
4. **Partner prize add-on, no cost to us.** Ask one local spot (a po-boy shop or daiquiri place from the Sept 30 spots research) to throw in catering for the winning family in exchange for being named in the ad and the Live. Their customers see it; ours see them.
5. **Second-place and the drip sell the boat; the winner sells the brand.** Film the winning family's ride (publicity release in the rules, filmed with their OK). That video is the December and Mardi Gras ad.
6. **Corporate deck handoff.** Every `corp_holiday`=need-a-spot lead gets the Corporate Holiday Deck (Marketing/Corporate Holiday Deck 2026) by email within 24 hours, before the drawing, because holiday dates fill before Nov 24.
7. **Custom audience + lookalike.** 400 locals who raised their hand is a better seed than any interest stack. Build the 1% LA lookalike on day 15 and point the sunset-cruise seat ad at it.
8. **Run it again.** Each month is its own sweepstakes (doc 03). December round: "One local office wins the holiday party boat." February: "One krewe wins the Mardi Gras boat." Same engine, same rules, new face.
9. **Ask the one question the form can't.** Day 7 email reply prompt: "Hit reply and tell me what's stopped you from booking a boat before." Replies route to OpenCX → Jeff. That's the doubt list for the next round's copy.
10. **Don't** pay for entries by shares/tags, don't require a purchase, don't call the $50 a prize, don't text anyone before the toll-free sender clears, and don't use the social-cruise seats ($59, 21+) as the prize image. The prize is a private boat.

---

## 9. Build list

| # | Piece | Where | Owner | Status |
|:-|:-|:-|:-|:-|
| 1 | Add to `capture-v2`: form steps 5, 6, 7, 10, 11 fields; ZIP validator; score; Slack hot-lead ping; second-place draw; 72h claim timer; `LOCAL50-NOV` | `~/Projects/fh-lead-engine-capture` | Claude | not started |
| 2 | `/boat/` and `/boat/rules` pages on WordPress (iframe to engine) | wp-admin | Claude preps, David/Michael paste | pending #1 |
| 3 | Rules: fork doc 03 for this round: 5 parishes, LA only, second prize, 72h claim by text/email/phone, draw date, redraw date | this folder, `11 Local Family Giveaway — Official Rules (Nov 2026).md` | Claude | next |
| 4 | Counsel pass on #3 (doc 03 section 6 questions, now simpler: no NY/FL) | David's attorney | David | blocks launch |
| 5 | Shoot V1 to V3 + S1 at the dock | Jeff/JT, one afternoon | Jeff | needs a date |
| 6 | Meta campaign, 2 ad sets, 5 ads, pixel Lead, Instant Form, leads webhook | Ads Manager (fb MCP can build campaign/adsets/creatives; Instant Form is manual) | Claude builds paused, David flips on | pending #5 |
| 7 | FareHarbor: `LOCAL50-NOV` (exp 12/6, private boats, $50 off total), comp booking type for the prize at $0 [VERIFY FH comp booking charges nothing] | FH dashboard | David | pending |
| 8 | Corporate deck auto-send for `corp_holiday` leads | engine + deck PDF | Claude | pending #1 |
| 9 | Dock QR placard + boat bar cards | print | Jeff | pending #2 |
| 10 | Facebook Live run-of-show for Nov 24 + redraw Dec 1 | this folder | Claude | later |

---

## 10. Decisions for David (5)

1. **Second place: $500 credit (my pick) or $500 cash?**
2. **Prize boat and headcount:** "up to 25 on a tiki" as written, or let the winner pick any boat up to 25? [VERIFY private charters allow under-21 family members on board; if not, "family" copy becomes "your people" and the rules say 21+ riders.]
3. **Eligibility footprint:** the 5 parishes as written, or Orleans + St. Bernard + Jefferson only (tighter, cheaper ads, smaller pool)?
4. **Does this replace the Nov 16 survey-contest draw** (my strong recommendation: yes, one contest, one list) or run alongside it?
5. **Who's on camera and who texts the hot leads:** Jeff for both as written?

Go/no-go stays Mon Oct 19 (same date as the survey contest). Counsel sign-off on the rules is the only true blocker.

---

## 11. Newsletter to post: the parish poll (added 2026-10-16, David's call)

**The split:** entering = answering the survey at `/boat/`. Engagement = a poll that lives in the giveaway post's comments, and the email list is what pushes people to it. Two different actions, two different asks. Nothing on the post earns an entry (Meta's rule), and the newsletter never says it does.

**The post.** The pinned giveaway post on Facebook (and the Instagram mirror) ends with one question: **"Which parish gets the boat? Comment yours."** That's the poll. Crew replies to the first 20 comments the first hour so the thread has a pulse before the email lands. Weekly, Jeff posts the tally as a reply ("Orleans 188, St. Bernard 212, Jefferson 97...") and the newsletter quotes it.

**Sends from the win-back list (SES, mbp-2 runner, 33k):**

| When | Segment | Subject | Ask |
|:-|:-|:-|:-|
| Fri Oct 23 | Local (504/985 area code or LA ZIP) [VERIFY the list carries phone or ZIP; else the whole list gets the non-local version with a "live here?" line] | One New Orleans family gets the boat. Free. | 1. Enter at /boat/ (60 seconds). 2. Then go vote your parish on the post. |
| Fri Oct 23 | Non-local | We're giving a boat to a local family. Pick the parish. | Not eligible, so just the vote. Plus the Crew's Guide link. |
| Fri Oct 30, Nov 6, Nov 13 | Everyone | The parish tally (St. Bernard's up 24) | Leaderboard + post link. Locals also get "not entered yet?" |
| Mon Nov 23 | Everyone | Tomorrow 6pm: we read the tally, then the name | Watch the Live, comment your parish on it. |
| Wed Nov 25 | Local non-winners | A boat for your crew: $50 off through Dec 6 | The offer (not a prize). Per-person math for the boat they'd fit. |
| Wed Nov 25 | Everyone else | The St. Bernard Boat Day (or whichever parish won) | Winner photo, no ask but the Guide. |

**Go-Cup:** giveaway in the sponsor slot both editions for 4 issues; bar-talk section runs the tally.

**Rules for the copy:** "vote" and "comment" never sit next to "enter" in the same sentence. No "share," "tag," "forward to enter." Non-locals never see "you can't win" phrased as winner language. Every link carries UTMs (`utm_source=winback&utm_medium=email&utm_campaign=local-giveaway-nov26&utm_content=<send>`), still missing on the runner per the 10/13 audit, so fix that first. Hosted unsubscribe only. Replies route to OpenCX so parish-pride stories and "my cousin's family" nominations reach Jeff; the best become week 2 and 3 posts, with permission, no entries.

Draft copy: `12 Local Family Giveaway — Newsletter Sends.md`.

---

## 12. The giveaway as the website's lead magnet (added 2026-10-19, David's ask)

**Call:** the site is the giveaway's main front door, not just the Meta ad's landing page. But most site visitors are tourists who can't enter, so every placement has two doors: locals enter the giveaway, visitors get the Crew's Guide. Nobody leaves with nothing, and the entry list stays clean.

**Placements (all point at the same engine form, each tagged with its own `source` so we can see which one fills the list):**

| Placement | Where | `source` | Notes |
|:-|:-|:-|:-|
| Top banner | Every page, replaces the dead GHL "Get early access" form | `site-banner` | Desktop and mobile copy below. Links to /boat/ |
| Popup | Engine `w.js?b=npb`, giveaway door mode | `site-popup` | Second pageview or 30 seconds, once per 7 days per browser, never on /boat/ |
| /boat/ page | WordPress page, engine form in an iframe + rules + parish tally | `boat-page` | Also the Meta ad set A landing page (`meta-a` via UTM) |
| "Or win one" card | Under the private-boat prices on the homepage and boat pages | `site-card` | Small card, one line + button |

**Form change for site traffic:** "Where do you live?" becomes screen 1 (the five parishes as buttons + "Somewhere else"). "Somewhere else" switches to the guide signup, keeps the group / occasion / when answers, and never creates a giveaway entry. The exact ZIP is still asked later and must match a parish from screen 1; a mismatch or an out-of-area ZIP gets the same guide offer instead of an entry.

**Tracking:** GA4 `generate_lead` with `method` = giveaway or guide, Meta CAPI Lead on confirmed entries only, UTMs carried from the landing URL into the lead record.

**After Nov 23 11:59 PM:** the form closes itself (engine refuses entries outside the window). Banner flips to "{winner_parish} won the boat. Here's $50 off yours" through Dec 6 for local leads; popup goes back to guide-only. December round reuses all four placements if David runs it.

**Draft copy (site, needs David's OK):**

- Banner, desktop: "Live around New Orleans? We're giving one local family a private boat. Drawing Nov 24. Enter free"
- Banner, mobile: "Locals: win the boat. Enter free"
- Popup headline: "Free boat for a local family"
- Popup sub: "A private tiki boat for 25 of your people, about 1 hour 45 minutes on the bayou, BYOB. One family from Orleans, Jefferson, St. Bernard, St. Tammany or Plaquemines wins it Nov 24."
- Popup button A: "I live here, enter me"
- Popup button B: "Just visiting? Get the crew's guide"
- Popup small print: "No purchase necessary. 21+. Official Rules."
- Out-of-area screen: "That's outside the five parishes, so this one's locals only. Want the crew's guide to New Orleans instead? Where to eat, where to go out, what to wear, timed to your trip." Button: "Send me the guide"
- Price card: "Or win one. We're giving a private boat to one local family Nov 24." Button: "Enter free"

**Build:** engine `w.js` gets a `giveaway` door mode (config in brands.json, auto-off outside the entry window), the form gets the screen-1 split, WordPress gets the banner swap, /boat/, and the card (David or Michael pastes, same as doc 07 item 4).
