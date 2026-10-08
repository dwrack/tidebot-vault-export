# Lead Magnet Plan: NOLA Party Barge (Oct 2026)

*Drafted 2026-10-03. Draft only. Nothing here is live, sent, or posted. It fits inside the Sept 30 lead plan (the Lead Capture + Drip Plan, Oct 2026, in the vault's Marketing folder) and uses the same engine, the same $50 code, and the same field names. Every stat carries its date. Anything marked [VERIFY] is not confirmed and can't go in copy until it is.*

## The short version

1. **The NOLA Countdown stays the flagship.** Every other magnet is a side door into it, or a small drip that hands off to it. Nobody builds a second guide.
2. **Build three next:** the survey contest, the cost splitter, and the crew photo. One fills the top, one catches the planner at the price question, one catches the riders we already had on the boat and never got an email from.
3. **No PDFs**, with one exception (the office party one-pager, because planners forward it to a boss). Everything else is a page or an email.
4. **Judge each door on bookings, not list size.** The contest will bring the most emails and the weakest ones. That's fine as long as we can see it.
5. Two ideas from the brief got merged, not built: the which-boat quiz and the cost splitter are one tool, and the group chat paste is what that tool hands back, not its own signup.

## 1. The magnets

Effort: S = under a day. M = 2 to 5 days, or it needs a crew habit. L = more than a week or new engine features. Priority 0 is already in build.

| # | Magnet | Who it's for | Format | Hook line | Where it lives | Captures, and tags it sets | Feeds | Effort | Built from | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **The NOLA Countdown** (flagship) | Visitors planning a group trip, any occasion | Email drip timed to their trip date, 12 chapters, each one a blog post | "Coming to New Orleans? Get the free NOLA Countdown + $50 off a private boat." | Top banner, popup, hub page, inline box on the big blog posts, Nolan | First name, email, trip_when. Taps add group_type, group_size, first_time_nola. `source=countdown` | Countdown (it is the drip) | L | The Sept 30 plan, welcome email draft, about 10 live posts to link, capture API and popup | 0, in build for Oct 20 |
| 2 | **Win a Boat Day** (survey contest) | Social followers, locals and visitors, people not shopping yet | Tap survey on a page, monthly draw [default, not confirmed] | "What do you love most about New Orleans? Tell us and you're in the draw for a private boat day." (prize is the default, not confirmed) | Organic Facebook and Instagram post, the "Win a Trip!" nav item, the old giveaway URL, Instagram bio link | Email, 21+ check, survey answers as interest tags, trip_when, is_local. `source=contest` | Contest warm-up, then Countdown (visitors) or Open Boat List (locals) | M to L | Nav and banner slot already on the site, giveaway URL sitting at position 6 with 8,023 impressions and 1 click (90 days to Aug 2026), a drafted title and meta, 2021 giveaway history on Facebook | 1 |
| 3 | **What It Costs Each of You** (boat matcher + cost splitter) | The planner with a headcount and a price question | 3-tap tool. Shows the boat and the per-person price. An email unlocks the group chat message and the code | "Which boat fits your crew, and what it costs each of you. Takes 20 seconds." | /boat-rental/, /our-boats/, each boat page, the budget post, /contact-us/, Nolan's answer to "how much" | Email, group_size, group_type, under-21 yes or no, trip_date. `source=split`. Hot if 13+ guests and a date inside 30 days | Countdown, starting at email 1b (the paste) | M | Price table matched to FareHarbor on 2026-09-30, the email 1b idea in the Sept 30 plan, `/lead` already saves `source` | 2 |
| 4 | **The Crew Photo** | Riders who didn't book. Each booking gives us 1 email for 12 to 25 riders | QR on the boat. Crew takes one group shot, we email it | "Want today's crew photo? Scan this and we'll email it to you." | Sign at the boat bar, dock check-in, the captain's send-off | First name, email, boat and ride date (from the QR), is_local, group_type. `source=crewphoto`, tag `rider` | Rider drip (3 emails), then the reel newsletter | M, mostly a crew habit | Group photo step in the captain agreement draft [VERIFY: in force?], Photography Upsell Pilot notes (QR and gallery idea, not built), the tracked redirect pattern the review texts use | 3 |
| 5 | **Holiday party one-pager + headcount quote** | Office managers, assistants, HR at New Orleans companies, event planners | One-page PDF plus a 5-field quote form | "The only holiday party in New Orleans that leaves the dock." | 1:1 emails from info@, a /holiday-parties page, Nolan | Name, work email, company, headcount, date. `source=corp`, group_type=work, hot | No drip. A human gets pinged the same day | S | Flyer file, past-guest company list, 13 email drafts staged 2026-09-10 [VERIFY: sent?], positioning David picked 2026-09-10 | 4, time-boxed. Out by Oct 17 or park it for 2027 |
| 6 | **The Open Boat List** | Locals: birthday organizers and friend groups who live here | Short email, once a week at most, only when boats or seats are open | "Live here? Get the Open Boat List. When a boat's open this week, you hear first." | Facebook page posts, Google Business post, the crew photo page, the contest thank-you page | Email, is_local=yes, best_days. `source=locals` | Locals drip (welcome, then a broadcast). Never the Countdown | S to capture, M to run | FareHarbor availability is readable by API (reference note), Friendsgiving copy in the fall holiday plan, bookings now land in-week and weekdays are starting to earn (Jul 2026) | 5 |
| 7 | **Mardi Gras 2027 for Party Crews** | Groups coming for parade season. Mardi Gras Day is Tue Feb 9, 2027 | Refreshed blog post plus an emailed day-by-day parade week plan | "Mardi Gras 2027 with a crew: which parades, which days, and where a boat day fits." | /krewe-of-endymion/ (refresh), the Mardi Gras alternative post, Countdown chapter 4, a December social post | Email, arrival date, group_size. `source=mardigras27`, trip_when=Feb 2027, season=mardi_gras | Countdown with the Mardi Gras swap | M | Krewe research from 2026-09-30 (dates set, times and routes still TBC), Endymion page with 14,440 impressions and 1 click (90 days to Aug 2026), a refresh already due Dec 1 | 6, ships Dec 1 |
| 8 | **Steal Our Bachelorette Plan** | Maids of honor and brides planning a New Orleans weekend | The itinerary as a group chat message plus the pack list, by email | "Steal a local's New Orleans bachelorette plan. Paste it straight into the group chat." | The bachelorette itinerary post, the bachelorette boat page, bachelorette reels | Email, trip_date, group_size. `source=bach`, group_type=bach | Countdown, bachelorette branch | S | Live itinerary post (position 21 as of Aug 2026), boat page (position 29) with a rewrite staged 2026-08-15, the BYOB pack list post | 7 |
| 9 | **The Cousin Trip Vote Kit** | The planner cousin. Groups of 6 to 15, planning 6 to 12 months out | Three ready-to-post options the family can vote on, by email | "Planning the cousin trip? Here's a New Orleans plan your family can vote on." | A /cousin-trips page (not built), cousin reels | Email, trip month, group_size. `source=cousin`, group_type=cousin (new value) | Countdown, month or year track | M | Cousin trips research from 2026-08-27, 10 video hooks, 5 ad angles, a landing page outline | 8 |
| 10 | **Bayou Spotter Card** | Swamp tour shoppers and families | One-screen spotter card by email: gators, herons, cypress, the surge barrier | "What you'll actually see on Bayou Bienvenue, including the Great Wall of Louisiana." | /swamp-tour-questions/, the closest swamp tour post, the surge barrier reel when it runs | Email, trip_when, kids yes or no. `source=spotter`, interests=nature, group_type=family if kids | Countdown, with the swamp tour as the boat line | S | Surge barrier reel (cheapest clicks of the year at $0.022, Jul 2026), swamp pages that already rank | 9 |
| 11 | **Concierge Card** | Hotel guests already in town | QR card at the front desk, to a hotel-tagged page | "15 minutes from the French Quarter: gators, a tiki boat, and a bathroom on board." | Front desks of partner hotels | Mostly a booking, not an email. `source=hotel-<name>`. Email is optional | None. They book this week or they don't | S per hotel | 11 hotel intro emails sent 2026-06-17 [VERIFY: who replied], the tracker sheet, the tracked redirect pattern | 10, only when a hotel says yes |

**Merged, dropped, or parked**

| Idea | Call | Why |
|---|---|---|
| Group chat paste as its own signup | Merged | It's the share format for #3 and for Countdown email 1b. A second signup for the same thing splits the traffic. |
| Which-boat quiz | Merged into #3 | Same three questions as the splitter. One tool, one page. |
| PDF city guide | Dropped | The Countdown is the guide, and it knows their dates. A PDF gets saved and never opened. |
| Tag-a-friend giveaway | Dropped | Meta's promotion rules don't allow tagging or sharing as a way to enter (per the contest assumptions). Extra entries come only from answering the follow-up questions. Referral entries were cut too: Meta's rules ban rewarding people for publicizing a promotion (rules draft, section 0). |
| Text club | Parked | Texting is off until the toll-free or A2P verification clears. |
| Gift card offer | Parked | Not in this version of the Sept 30 plan. |
| Popup on the sister sites | Parked | They sent the best-converting traffic we have, 7% and 11% as of May 2026. Don't put a form in front of that. |

## 2. The three to build first

The Countdown is build zero and it's already on the calendar for Oct 20. These three come next, in this order.

**1. Win a Boat Day (the survey contest).** This is the door David asked for, and it replaces something that's broken today: the "Win a Trip!" nav item and the banner point at a giveaway page with no prize and no follow-up, which got 8,023 impressions and 1 click. Giveaways are also the biggest reach lever this page has ever had. The 2021 giveaway post is the all-time Facebook record at 107,524 engagements, giveaways have the highest median engagement of any theme on Instagram (40 against a baseline of 31), and none ran in 2026 as of the Aug 19 readout. The spec lives in the contest files in this folder, so here is only how it fits: the survey answers become tags, everyone who doesn't win gets the $50 private boat code after the draw (the default, not confirmed), visitors with a trip get handed to the Countdown, and locals get handed to the Open Boat List. The risk is deal hunters. The fix is the survey itself, since "when are you coming" and "who's coming" sort the real planners from the people who just want free stuff.

**2. What It Costs Each of You.** Price is the question people actually ask. In the chat data (986 sessions, 90 days to 2026-08-28), a third of the guests who sent one message and vanished had asked about price, and what they got back was a rate card. $1,200 with no story is just a big number. $48 each is a yes. The tool asks three things: how many of you, anyone under 21, what's the occasion (plus an optional date). It shows the boat and the per-person number right away, no email needed, because holding the price hostage is the rate card problem all over again. The email unlocks two things: the message to paste in the group chat, and the $50 code. The math comes straight from the verified price table:

| Group size | The tool shows | Total | Each | Against $59 seats |
|---|---|---|---|---|
| 1 to 6 | Luxury Pontoon (says plainly: no bathroom on board), or seats | $350 | $58 at 6 | About even at 6. Fewer than 6, seats win |
| 7 to 13 | Seats on a social cruise (21+) | $59 each | $59 | A private boat costs more per head here. If anyone is under 21, it's private only, so show the Bayou Boogie |
| 14 to 18 | The Bayou Boogie | $800 | $57 at 14, $44 at 18 | Private wins from 14 up |
| 19 to 25 | A tiki boat first, The Party Queen as the lower price pick | $1,200 or $900 | Tiki: $63 at 19, $48 at 25. Party Queen: $47 at 19, $36 at 25 | Tiki wins from 21 up, Party Queen from 16 up |
| 26 | The Party Queen | $900 | $35 | |
| 27 or more | Two boats. A person follows up | | | Hot ping |

All numbers are before the $50 code and before taxes and fees [VERIFY: what FareHarbor adds at checkout, so the split matches the total they'll see]. The paste it hands back reads like this (draft):

> Found our boat day. Private tiki boat on the bayou with NOLA Party Barge, 15 minutes from the French Quarter. BYOB, bathroom on board, captain and crew, 1 hr 45 min. It's $1,200 for the whole boat, so about $57 each if all 21 of us go. $350 holds the date. Who's in? {personal_link}

It works on day one with the engine as it is (the capture API already saves `source`), and it also gives Nolan a better answer to "how much" than five prices in a row: one line and a link.

**3. The Crew Photo.** This is the only magnet that needs zero new traffic. A private boat leaves the dock with 12 to 25 people on it and we get one email. The riders are the warmest leads we will ever have, since they just did the thing. Each boat gets a small sign at the bar with a QR code. The page asks for a first name, an email, and two taps (live here or visiting, what are you celebrating). The crew takes one group shot at the best spot and drops it in that boat's album for the day before the shift ends [VERIFY: captain or deckhand owns this]. Then three emails: the photo link the next morning and nothing else, "your turn to plan one" two days later with the $50 code and the per-person math, and one question a week after (visitors: when's your next trip, locals: want the Open Boat List). The free part is one group photo. A full photo set stays a paid add-on if that pilot goes ahead (it's on the Add-On Menu at $15 a person, idea stage). Two checks before it runs: the photo release wording in the waiver, and that only adults can sign up, since private charters allow ages 6 and up [VERIFY both].

**Not a build, just an approval:** the holiday party one-pager (#5). The flyer and the 13 drafts were staged on 2026-09-10 and the plan said offices book December in September and October. It's waiting on David confirming what's true on the ground in December. The homepage says the boats are covered and heated in winter. The indoor room, its capacity, and the fire pits are not confirmed [VERIFY]. If that doesn't happen by Oct 17, park it and aim the same kit at 2027.

## 3. Which magnet goes where

One magnet per spot. Two offers on one page means neither gets picked.

| Spot | Magnet | Note |
|---|---|---|
| Top banner | Countdown | Line from the Sept 30 plan |
| "Win a Trip!" nav item | Contest | It already says what it is |
| Old giveaway URL (8,023 impressions) | Contest page | The Sept 30 plan said 301 it to the hub. I'd host the contest there so those searches land on a live prize. Decision below |
| Popup | Countdown | Shows once, then snoozes |
| Homepage | Popup only | The booking calendar is on this page. Nothing goes above it |
| /boat-rental/ (about 13,500 impressions), /our-boats/ (about 9,000), each boat page | Splitter | These are price shoppers |
| /contact-us/ (about 8,500 impressions) | Splitter link | "Which boat fits your party?" |
| Budget post (about 41,000 impressions, our #1 post) | Splitter, then Countdown box at the end | It's a cost article. Lead with the per-person math |
| December weather post (about 40,000 impressions) | Countdown, month preset to December | Same magnet, already knows when they're coming |
| How many days, dress code, neighborhoods, walking tour posts | Countdown inline box | Trip planners, no price intent yet |
| /krewe-of-endymion/ (14,440 impressions, 1 click) | Mardi Gras 2027 plan | After the Dec 1 refresh |
| Bachelorette itinerary post and bachelorette boat page | Bachelorette plan | Low traffic today, so low priority |
| Swamp tour pages | Spotter card | |
| Hub page /nola-party-planning-guide/ | Countdown at the top | Links out to every other magnet |
| Facebook page (about 85K fans) | Contest post, 1 or 2 a month at most. Open Boat List the other weeks | The Facebook readout says 1 or 2 a month, because giveaways pull deal hunters |
| Instagram bio link (22,152 followers as of 2026-08-19) | Contest while a draw is open, Countdown otherwise | |
| Nolan (site chat, Instagram and Facebook DMs) | After a price question: the splitter link. Otherwise: the Countdown | The bot asked for an email in 2% of chats, and about 6% of non-email chats left any contact info (90 days to 2026-08-28) |
| On the boat and at the dock | Crew Photo | Locals who scan get offered the Open Boat List on the thank-you page |
| Weekly past-guest email (about 46,190 people) | One P.S. line for the contest, inside a send that's already scheduled | Needs David's OK. No extra sends. Scheduled dates: Oct 6, 13, 20, 27, Nov 17 |
| 1:1 emails to companies and planners | Holiday one-pager | Signed by the manager or the business, never the owner |
| Hotel front desks | Concierge card | One tracked link per hotel |
| Sister sites | Nothing at launch | See parked list |

All stats in this table are 90 days to Aug 2026 unless a date is shown. Re-pull them before quoting.

Tracked short links can be added the same way /boost and /boost-ig were, one per magnet and channel. The board shows a new site in design as of 2026-10-03, so each magnet page should be a small standalone page that moves with it [VERIFY: where those pages get hosted in the meantime].

## 4. How a signup gets tagged so the right drip starts

**What works today, no build:** every form posts to the engine's `/lead` with its own `source` value (40 characters max) plus the `utm_` fields. That alone gives signups by magnet from day one.

**What needs build** (all inside task 8 of the Sept 30 plan unless marked new):

| Piece | Status |
|---|---|
| Profile fields on the lead (group_type, group_size, trip_when, trip_date and the rest) | Needs build, planned |
| Schedule picked by `source` and tags (branch-aware schedules) | Needs build, planned |
| Answer links and tracked links | Needs build, planned |
| Hot-lead ping to a person | Needs build, planned |
| Second signup merges into the same lead: add to a `magnets` list, keep the drip position, never restart | Needs build, new |
| New fields: is_local, rode_on, boat, ref, company, headcount | Needs build, new |
| Broadcast to one tag (the Open Boat List) | Needs build, new |
| Personal link (`ref`) | Parked. No contest entries for referrals under Meta's rules. Whether any referral reward survives is counsel question 2 in the rules draft |

**The routing table**

| `source` | Form sends | Tags set at signup | Drip that starts | Then |
|---|---|---|---|---|
| `countdown` | first name, email, trip_when, trip_date | none yet, taps fill the rest | Countdown, track picked by trip_when | Reel newsletter |
| `contest` | email, 21+ yes, survey answers, trip_when, is_local, ref | interests from answers, contest month | Contest warm-up | After the draw: $50 code. Visitors with a trip go to the Countdown, locals to the Open Boat List |
| `split` | email, group_size, group_type, under-21, trip_date | hot if 13+ guests and a date inside 30 days | Countdown from email 1b, skipping questions already answered | Same as Countdown |
| `crewphoto` | first name, email, boat, ride date, is_local, group_type | rider, rode_on, boat | Rider (3 emails) | Locals to the Open Boat List, visitors to the reel newsletter |
| `corp` | name, work email, company, headcount, date | group_type=work, hot | None. Person pinged same day, one follow-up on day 3 | Nothing automatic |
| `locals` | email, is_local=yes, best_days | local | Locals welcome, then the broadcast | Stays there |
| `mardigras27` | email, arrival date, group_size | season=mardi_gras, trip_when=Feb 2027 | Countdown with the Mardi Gras swap | Same as Countdown |
| `bach` | email, trip_date, group_size | group_type=bach | Countdown, bachelorette branch | Same as Countdown |
| `cousin` | email, trip month, group_size | group_type=cousin | Countdown, month or year track | Same as Countdown |
| `spotter` | email, trip_when, kids | interests=nature, group_type=family if kids | Countdown, swamp tour as the boat line | Same as Countdown |
| `hotel-<name>` | the click, email optional | in_town | None | Nothing |

**Rules that keep it sane**

- One selling drip per lead at a time. If someone fits two, the order is: booked, rider, corporate, Countdown, contest, locals.
- Max 1 email a day per lead, across every drip. That's the Sept 30 rule and it doesn't bend.
- When `/booked` gets called, the code P.S. drops out everywhere.
- The 50 new enrollments a day cap will get beaten by a good contest post. Entry confirmations should go right away. Drip starts should queue in signup order. Flagged for the engine spec.
- Until the past-guest list and the engine share one unsubscribe list, keep engine broadcasts off the past-guest send dates (Oct 6, 13, 20, 27, Nov 17) so nobody gets two emails from us in a day.
- Clicks and taps only. Never opens.

**Cheap attribution before booking sync exists (optional):** FareHarbor codes are shared, so a code can't tell us who booked. A code name per door can. `CREW50-NOV` for the Countdown and the small doors, `BAYOU50-NOV` for the contest, `RIDE50-NOV` for riders. Same $50, same expiry, and the FareHarbor promo report then shows bookings by door. Cost: three codes a month to create, and a small engine change to pick the code by `source`.

## 5. What to measure

The one number: **bookings within 90 days, by `source`.** A door that brings 500 emails and 2 bookings loses to a door that brings 40 emails and 6.

| Metric | How it's counted | Starting target (a target, not a forecast) |
|---|---|---|
| Signups by source, weekly | `source` on the lead | 40+ a week across all doors (the Sept 30 target). Today it's about 0 |
| Capture rate per magnet | Signups divided by page views or scans | Splitter: 25% of people who finish it. Others: track for 30 days, then set one |
| First question answered | Answer link taps | Half of new leads answer at least one |
| Handoffs | Contest and photo leads who reach the Countdown or the Open Boat List | Track |
| Booked within 90 days, by source | `/booked` once booking sync exists. Until then, code redemptions in FareHarbor | 5%+ on Countdown and splitter leads (the Sept 30 target). The contest will run lower |
| New emails per private boat | Crew Photo signups divided by private trips run | 4 per boat |
| Unsubscribes by source | Engine | Any door at twice the average gets its first email rewritten |
| Hot pings answered | Time from ping to a person replying | Same day |
| Corporate quotes | Quote forms, and how many booked | Count them. Small numbers, big tickets |

**Kill rule:** a magnet that's been live 30 days in front of real traffic with under 10 signups gets moved to a better spot once, then pulled.

All of this goes in the monthly report that's already planned for Nov 1.

## 6. Decisions for David

| # | Decision | My call |
|---|---|---|
| 1 | Does the contest live at the old giveaway URL, or does that URL 301 to the hub like the Sept 30 plan said? | Contest lives there. It already ranks |
| 2 | Free crew photo next to a paid photo package? | Yes. A $10 group photo add-on can't beat a handful of new emails per boat |
| 3 | When a group of 19 to 25 fits both a tiki ($1,200) and The Party Queen ($900), which does the tool show first? | Tiki first, Party Queen right under it as the lower price pick. Never hide it |
| 4 | Does the Open Boat List get a locals or weekday price, or just first dibs? | First dibs only to start. No new discount until we see it fill boats |
| 5 | Is the pontoon in the splitter's $50 math? | Follows the open pontoon decision in the Sept 30 plan |
| 6 | One $50 code for all doors, or a code name per door? | Per door, until booking sync exists |
| 7 | Holiday one-pager: confirm the December facts by Oct 17, or park it? | Confirm and send. The kit is already built |
| 8 | Who takes and uploads the crew photo? | Captain takes it, deckhand uploads it before the shift ends |

## Sources

All in the vault unless noted: the Sept 30 lead plan, SEO Audit 2026-08-15, Title + Meta Rewrites (Aug 2026), SEO Action Plan May 2026, Why Leads Ghost (OpenCX data, 2026-08-28), Cousin Trips research (2026-08-27), 2027 Sponsorship + Events Plan (2026-09-10), Holiday Pushes Fall 2026, the Add-On Menu (2026-09-10), NOLA Spots + Mardi Gras 2027 research (2026-09-30), the Facebook and Instagram readouts (2026-06-20 and 2026-08-19), Boosted Posts best performers (2026-10-02), the shared board (2026-10-03), and the engine code at `~/Projects/fh-lead-engine` (read 2026-10-03). Prices and boat facts come from this job's facts file, matched to FareHarbor on 2026-09-30.
