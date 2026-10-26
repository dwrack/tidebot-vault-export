# Lead magnet build package: weekly weekday private giveaway (DRAFT for review)

**PRIZE UPDATE (Davey, 2026-10-20): "Win a weekday date night in our new private sauna."** Two people, one weekday evening (Mon, Wed or Thu), in one of the new private saunas. It ties straight into the date-night searches (Google "date ideas portland" 480/mo peaking in January, DataForSEO Oct 20; TikTok "date night spots portland oregon"). The privates are new inventory, so a prize night doesn't displace a paying Social guest. Open check: the privates aren't open yet. Confirm the opening date. Until then, early winners get the first date nights once they open ("be one of the first couples in"). The perk for every signup is still open; early access to book the privates fits this prize.

**DECISIONS (Davey, 2026-10-20):**
1. Offer: weekly draw for a free weekday Private Party PLUS a small perk for every signup (perk TBD by Davey).
2. SMS: collect phone + consent now; emails run now; texts start only after Twilio A2P is refiled and approved (use this form as the opt-in proof).
3. Site: draw popup ships now (Nov 2 target); the Funnel Lab quiz comes later as a second test.
4. Build: Claude builds in test mode (form, emails, draw automation); L and Jess review before anything goes live. Nothing publishes without Davey's OK.
Target launch: week of Nov 2, ahead of the holiday + January search peak.


Status: DRAFT for Davey, Jonah and Kimberlynn, Oct 20 2026. Nothing is built, posted, sent, scheduled or created. No form, popup, code, automation or post exists yet. Every piece below is paste-ready only after the decisions in section 8 are answered.

Built from the concept doc (Marketing, "Lead Magnet, Weekday Private Giveaway", Oct 2026). The five concept decisions stay open. First Plunge (the 3-visit offer) stays dropped; only its build notes are reused here.

How to read the brackets:
- [PLACEHOLDER] = Davey or the team fills it in. Nothing ships with one left in.
- [VERIFY] = a platform capability or fact nobody has confirmed. The owner checks it before building that step.
- [IF x] = copy that only applies to one answer of an open decision.

## 0. The short version

- **What it is:** sign up (name, email, optional phone) and you're in a weekly draw for a private weekday session. Everyone who signs up joins the email list.
- **Who it's for:** cold and undecided traffic. Locals first: reviews talk like a Portland product (Portland mentioned in 21% of reviews, visitors 3.5%). Friend groups and couples are the two biggest named segments.
- **Who should NOT see it:** people already on a booking page, people arriving from a Google Ads click, and current members. They're ready to book; a giveaway popup only slows them down. Suppress the popup there [VERIFY Jess can scope the popup by page and by UTM].
- **What it costs us:** one weekday afternoon slot a week. Weekday 1 PM and 3 PM Social sessions averaged 0.9 to 3.2 of 8 seats (Periode, Aug 15 to Oct 12). The real cost is whatever Social seats that slot would have sold, so the prize should land on a slot with zero Social bookings (see section 7, L's step 6).
- **Economics line:** max cost per lead and per booked guest can't be set until the Nov 1 pricing is final. Formula once it is: max CAC = (average first-visit spend + expected repeat spend) x gross margin / 3. [PLACEHOLDER: fill after Nov 1 pricing.] Until then, judge it on cost per weekly slot given away vs bookings by entrants within 30 days.

## 1. Funnel map

```
ENTRY POINTS                                  CAPTURE              NURTURE                         CONVERT
Site popup (once per visitor)    -+
Site banner (every page)         -+
IG: comment PRIVATE -> DM link   -+-> /draw page (AC form) -> tag weekday-draw -> Email 1 (instant)  -> Book a session (Periode)
IG / TikTok link in bio          -+        + source tag          + src-<source>   Email 2 (day 3)
On-site QR (deck + lounge)       -+                                               Wednesday draw -> Winner notice + code -> Prize booked
                                                                                  Email 3 (Wed, all entrants)
                                                                                  Email 4 (still want to come?)
                                                                                  Email 5 -> newsletter list
                                                                                  Winner post (IG/TikTok) -> shares -> back to /draw
```

One form, one entry path. Every entry point sends people to the same `/draw` page [PLACEHOLDER: final URL] so the rules, consent and data are identical everywhere. Comments are NOT entries; a comment only gets you the link.

| Step | What happens | Measure | Target (guess, check after 4 weeks) | Where the number lives |
|:-|:-|:-|:-|:-|
| 1. Popup shown | Once per visitor, 20 sec on mobile or exit intent on desktop | Impressions | n/a | Squarespace / popup tool [VERIFY it reports views] |
| 2. Popup or banner click | Tap to the form | Click rate per variant (A/B) | Popup 3 to 6%, banner 0.5 to 1% | GA4 event `draw_popup_click`, `draw_banner_click` [VERIFY Jess can fire events] |
| 3. IG comment PRIVATE | Link sent by DM | Comments, DMs sent, link taps | 1 in 3 commenters taps | IG insights + `?src=ig` |
| 4. Bio link / QR scan | Lands on /draw | Visits by `src` | n/a | GA4 property 524300531, UTM + `src` |
| 5. Form submit | Entry created | Submit rate per source (visits to entries) | 25%+ from social, 10%+ from popup clicks | ActiveCampaign tag counts by `src-*` |
| 6. Phone + SMS box ticked | SMS consent | % of entries with consent | 30 to 50% | AC field `sms_consent` |
| 7. Email 1 to 5 | Nurture | Open, click, reply, unsubscribe per email and per subject | Open 45%+, click 5%+, unsub under 1% | AC reports |
| 8. Weekly draw | One winner | Entries in the draw, winner response time | Claim within 48 hrs | Claude's draw log |
| 9. Prize redeemed | Winner books with the code | Code used within 30 days | 80%+ | Periode code report |
| 10. Booking by an entrant | Paid booking, not the prize | Entrants who book within 30 days, by source | 3 to 5% of entrants | Claude's weekly match of entrant emails vs Periode export [VERIFY export has email] |
| 11. Winner post | Shares | Shares, saves, profile visits, entries in the 48 hrs after | Entries up the day after the post | IG insights + AC tag dates |

The one number that matters: **paid bookings by entrants within 30 days, per weekly slot given away.** Everything else is diagnosis.

## 2. Popup, banner, form, consent, thank-you

House rules for all on-site copy: "Ebb & Ember", no prices, never wood-fired, never "a float", no promised feelings, cold plunge always optional.

### Popup (once per visitor; 20 sec on mobile, exit intent on desktop; not on booking pages or for members)

**Variant A (lead with the river)**
- Headline: Win a private weekday session on the Columbia.
- Body: We draw one name every Wednesday. Heat, the river, the deck, and nobody else there but your people.
- Button: Enter the draw
- Under the button: No purchase necessary. 21+. [Rules link]

**Variant B (lead with who you'd bring)**
- Headline: Who would you bring?
- Body: One winner a week gets a private weekday session at Ebb & Ember, Portland's floating sauna on the Columbia River. Entering takes 20 seconds.
- Button: Put my name in
- Under the button: No purchase necessary. 21+. [Rules link]

### Banner (Squarespace announcement bar, every page except booking pages)

- **A:** Win a private weekday session on the river. We draw every Wednesday. Enter ->
- **B:** This week's private session is still up for grabs. Enter the draw ->

### The /draw page (where IG, TikTok, QR and both site units all land)

- H1: Win a private weekday session at Ebb & Ember
- Line: One winner every Wednesday. Bring [IF prize A: your crew, up to [10 or 12, VERIFY]] [IF prize B: up to 3 friends].
- Form (below)
- Three short lines under the form: What you'd win. How the draw works. Already want to come? [Book a session link]
- Footer: No purchase necessary. Must be 21+. [IF residency limited: Open to Oregon and Washington residents.] Not sponsored by or affiliated with Instagram, Meta or TikTok. [Official rules link]

### Form fields (ActiveCampaign form, embedded on /draw and in the popup)

| Field | Required | Notes |
|:-|:-|:-|
| First name | Yes | |
| Email | Yes | |
| Phone | No | Label: "Phone (optional, only if you want a text when you win)" |
| SMS consent checkbox | No, unchecked by default | Only shows or only counts if phone is filled [VERIFY AC conditional logic] |
| 21+ confirmation checkbox | Yes | "I'm 21 or older." |
| [IF residency limited] State | Yes | Oregon / Washington / Other. "Other" shows "Sorry, this one's for Oregon and Washington residents." |
| `src` hidden field | Auto | Filled from the URL `?src=popup`, `banner`, `ig`, `tiktok`, `qr` [VERIFY AC hidden field reads URL params; fallback is one AC form per source] |

Email consent line under the button (required, not a checkbox): "You'll get our emails, including the weekly draw. Unsubscribe anytime with one click."

### SMS consent text (DRAFT, tighter than the concept doc; decision 10)

> Text me from Ebb & Ember if I win, plus a reminder the day before each draw (up to [4] msgs/month). Consent isn't a condition of entry. Msg & data rates may apply. Reply STOP to opt out, HELP for help. [Privacy link] [Terms link]

Why it changed from the concept text ("Text me if I win and the occasional offer"): carriers rejected our A2P campaign in June because the opt-in wasn't verifiable. A specific line that names the brand, the message types, the frequency, and links ebbandember.com/privacy and ebbandember.com/terms-of-service is the version most likely to pass. "Occasional offer" adds promotional texts we haven't written and makes the campaign harder to approve.

### Thank-you state (replaces the form after submit)

- Headline: You're in.
- Body: We draw this week's winner Wednesday morning and email them that day. Check your inbox for a quick guide to your first session.
- Button: Don't want to wait? Book a session
- Small link: Share the draw with a friend [copies /draw?src=share]

## 3. Official rules (DRAFT for Jess to build as one page; attorney review is decision 8)

**Ebb & Ember Weekday Private Session Giveaway: Official Rules**

NO PURCHASE OR PAYMENT OF ANY KIND IS NECESSARY TO ENTER OR WIN. A PURCHASE DOES NOT IMPROVE YOUR CHANCES OF WINNING. VOID WHERE PROHIBITED.

1. **Sponsor.** [LEGAL ENTITY NAME that operates Ebb & Ember], 173 NE Bridgeton Rd, Portland, OR 97211 ("Sponsor").
2. **Eligibility.** Open to legal residents of [the United States / Oregon and Washington, decision 7] who are 21 or older at the time of entry. Employees, contractors and owners of Sponsor and their immediate families and household members are not eligible. [IF excluded: Current Ebb & Ember members are not eligible.] [IF excluded: Prior winners are not eligible for [6] months after their win.]
3. **Promotion period.** The giveaway starts [START DATE] at 12:00 AM Pacific Time and ends [END DATE or "when Sponsor posts notice of its end on this page"]. It runs in weekly draw periods. Each draw period runs Wednesday 12:00 AM PT through Tuesday 11:59 PM PT.
4. **How to enter.** Complete the entry form at [/draw URL] with your first name, a valid email address and confirmation that you're 21 or older. Phone number and text consent are optional and do not affect your chances. Comments, likes, follows and shares on social media are not entries.
5. **Entry limits.** One entry per person per draw period. Multiple entries with the same email, multiple emails by one person, or automated entries will be disqualified. [IF carry-over: An entry stays in the draw for [4] consecutive draw periods, then expires. You may enter again after it expires.] [IF single draw: Each entry is good for the draw period in which it was received.]
6. **Drawing.** One winner is selected at random from all eligible entries received in the draw period, by computer-generated random selection, on the Wednesday after the period closes, at about [10:00 AM] PT. Odds depend on the number of eligible entries received.
7. **Notification.** The winner is notified by email (and by text, only if they opted in). The winner must reply within [48] hours to claim. If they don't, or are found ineligible, Sponsor may select an alternate from the same period's entries.
8. **Prize.** One (1) prize per draw period: [IF prize A: a private weekday session in the Ebb & Ember main sauna (a "Private Party") for the winner and up to [9 or 11, VERIFY capacity] guests, Monday to Thursday at 1 PM or 3 PM, excluding [Tuesday, if decision 9 says so] and holidays] [IF prize B: a private sauna session for 2 to 4 people, weekday afternoons only]. Approximate retail value (ARV): [ARV, set after the Nov 1 pricing is final]. The prize is delivered as a single-use code that must be redeemed for a session within 30 days of notification, subject to availability. No cash value, not transferable, no substitution except by Sponsor if the prize becomes unavailable, in which case a prize of equal or greater value is awarded. Unused prizes are forfeited.
9. **Session conditions.** All guests must sign Sponsor's waiver and follow posted safety rules. Sessions are self-guided; no staff are on site. The cold plunge in the river is always optional. Guests must be [21+ / 18+ / minors with a guardian, VERIFY current guest age policy]. Sponsor may reschedule for weather, river conditions or safety.
10. **Taxes.** The winner is responsible for any taxes on the prize.
11. **Publicity.** Sponsor will announce each winner by first name and last initial only. Any photo, video or quote from the winner is used only with their separate written OK.
12. **Privacy.** Entry information is used to run the giveaway and to send Ebb & Ember emails (and texts, if you opted in), under our privacy policy at ebbandember.com/privacy. Unsubscribe from email anytime with the one-click link in every email. Reply STOP to any text to stop texts.
13. **Platform release.** This giveaway is in no way sponsored, endorsed, administered by or associated with Instagram, Meta or TikTok. Entrants release those platforms from any liability.
14. **General.** Sponsor may cancel, suspend or modify the giveaway if fraud, technical failure or anything else impairs its fairness, with notice posted on this page. Sponsor's decisions are final. To the extent the law allows, Sponsor isn't responsible for lost, late, incomplete or misdirected entries. These rules are governed by Oregon law.
15. **Winner list.** For the name of a draw period's winner, email [PUBLIC EMAIL, e.g. sauna@ or hello@, VERIFY which inbox] within 30 days of that draw.

## 4. Email sequence (ActiveCampaign)

**Every email:**
- From name: Ebb & Ember. From address: whatever the newsletter uses now [VERIFY in AC]. Reply-to: davey@ebbandember.com.
- Signed "Ebb & Ember". Never a personal name.
- Button above the fold on an iPhone, then the photo, then the details. Open with 2 or 3 short concrete lines.
- A/B the subject on every send (AC split, 50/50) [VERIFY AC plan tier allows split testing inside an automation; if not, alternate weekly by cohort].
- Plain ASCII punctuation only: straight quotes, no dashes as punctuation, no ellipses.
- Ends with a real question and an ask to hit reply.
- Footer: Official rules [link] / No purchase necessary / 173 NE Bridgeton Rd, Portland, OR 97211 / Unsubscribe [hosted one-click link].
- **Unsubscribe:** hosted link that processes the opt-out itself, plus headers `List-Unsubscribe: <https://[hosted unsubscribe URL]>` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. Never a mailto, never "reply to unsubscribe." [VERIFY AC sends the URL-form one-click header by default and no mailto header; if it includes a mailto, L checks whether it can be turned off.]
- Suppression: the SendGrid-era unsubscribes (119 + 21 bounces as of Jul 28) and the Do Not Contact list must be in AC's suppression before the first send [VERIFY they were imported].

### Email 1: Welcome (instant, on tag `weekday-draw`)

- **Subject A:** you're in this week's draw
- **Subject B:** your name's in the hat
- **Preview:** We pick a winner Wednesday. Here's how a session works in the meantime.

> You're in.
>
> One name a week. A private weekday session on the Columbia. We draw Wednesday morning.
>
> Don't feel like waiting?
>
> [Button: Pick a time]
>
> [Photo: steam off the deck, river behind]
>
> If it's your first time, here's the short version:
>
> Bring a swimsuit, [two towels, VERIFY whether towels are provided], water and sandals.
> It's self-guided. You'll get door and check-in details when you book.
> Getting here: 173 NE Bridgeton Rd. [Parking line, VERIFY current parking and signage.]
> The river plunge is optional. Plenty of people just sit on the ladder, or skip it.
>
> Who would you bring if your name comes up? Hit reply and tell us. A real person reads every one.
>
> Ebb & Ember

### Email 2: Day 3 (what a session looks like)

- **Subject A:** what actually happens out there
- **Subject B:** heat, river, deck, repeat
- **Preview:** Your first session, start to finish, in about a minute.

> Hot cedar. Cascade snowmelt. A deck in the open air.
>
> That's the whole thing, done a few times.
>
> [Button: Pick a time]
>
> [Photo: someone on the ladder, river below]
>
> How it goes:
>
> 1. Check in and change.
> 2. Heat. Sit as long as feels right.
> 3. Cold. Off the ladder into the river, a cold rinse, or nothing. Your call.
> 4. Deck. Sit outside and breathe. Rain counts.
> 5. Repeat until you're done.
>
> The river is real. It's 40-plus feet deep with current. Life jackets and throw rings are on deck, use the buddy system, and when in doubt, don't go out.
>
> "Such a perfect way to end a river day." [Real Google review, already in Customer Truth. Swap for another real one any week; never write one.]
>
> Done a sauna before, or would this be your first? Reply and let us know.
>
> Ebb & Ember

### Email 3: Wednesday draw email (to everyone still in the draw, excluding the winner)

- **Subject A:** this week's winner is [First name L.]
- **Subject B:** we drew a name this morning
- **Preview:** [IF carry-over: Not you this time. You're still in next week's draw.] [IF single draw: Not you this time. Next week's draw is open.]

> We drew this week's name.
>
> The private session goes to [First name L.]. [Optional, only with their OK: "Bringing her climbing crew."]
>
> [IF carry-over: You're still in. Next draw is [DATE].] [IF single draw: Next week's draw is open. Enter again here: [link to /draw?src=email].]
>
> Weekday afternoons are the quiet ones on the river. If you'd rather not wait on luck:
>
> [Button: Book a weekday session]
>
> [Photo: empty deck, afternoon light or rain on the river]
>
> What day of the week would you actually come out? Reply with one word. It helps us plan.
>
> Ebb & Ember

### Email 3W: Winner notice (sent by a person after Davey OKs the pick; not automated)

- **Subject A:** you won this week's private session
- **Subject B:** your name came up
- **Preview:** Reply within 48 hours to claim it.

> [First name], your name came up.
>
> You won this week's private weekday session at Ebb & Ember.
>
> Reply to this email within 48 hours to claim it. Once you do, we'll send your code.
>
> [After claim, send: Your code: [CODE]. Good for one [Private Party / private sauna session], Monday to Thursday, 1 PM or 3 PM [minus Tuesday, decision 9], within 30 days. [Button: Book with my code]]
>
> Everyone in your group signs the waiver when you book. The river plunge is optional for all of them.
>
> One small ask: can we share your first name and last initial in our winner post? A photo only if you want to send one.
>
> Ebb & Ember

### Email 4: Non-winner "still want to come?" ([Friday] after their first draw; once per person; skip anyone who has booked since signing up)

- **Subject A:** still want to come out?
- **Subject B:** no luck this week, here's the easy way in
- **Preview:** Weekday afternoons are quiet on the river. Pick one.

> No luck this week.
>
> The river's still there, and weekday afternoons are the quietest time to try it.
>
> [Button: Find a weekday time]
>
> [Photo: two people on the deck, steam, river]
>
> [IF LIVE BY LAUNCH, VERIFY: This week on the river: Tuesday is industry happy hour, 1 to 7 PM. Wednesday is Women + Femme Night. Thursday is Silent Night: no phones, no talking.]
>
> Bring one person. That's the best way to do it the first time.
>
> What's kept you from coming out so far? Reply and tell us, even if it's one word.
>
> Ebb & Ember

### Email 5: Handoff to the newsletter (after their last draw: [IF carry-over: after draw [4]] [IF single draw: 7 days after Email 4])

- **Subject A:** what you'll hear from us now
- **Subject B:** one email a week, from the river
- **Preview:** The draw's done for you. Here's what comes next.

> Your entry's run its course.
>
> From here you'll get our regular email: what the river's doing, new sessions, and the odd event on the deck. About once a week.
>
> [Button: Book a session]
>
> [IF re-entry allowed: Want back in the draw? You can enter again anytime: [link to /draw?src=email].]
>
> Not for you? The unsubscribe link at the bottom works in one click.
>
> What should we write about? Reply with anything you're curious about.
>
> Ebb & Ember

Automation after Email 5: remove tag `weekday-draw`, add the contact to the newsletter list, end. Any contact who unsubscribes at any point exits everything.

### Exit rules

| Trigger | Action | Status |
|:-|:-|:-|
| Unsubscribes | Exit all, suppressed everywhere, also removed from SMS | AC native |
| Books a paid session after signup | Skip Email 4 | [VERIFY how Periode bookings reach AC. L said in July that punch-pass purchases don't sync. Fallback: Claude's weekly match removes bookers by email before Friday.] |
| Wins | Out of future draws for [6] months (decision 13); still gets Emails 2, 5 | Claude's draw script |

## 5. Two optional texts (consent only, and only after A2P is VERIFIED)

**A2P status:** the concept doc and the brief say "last known IN_PROGRESS Jun 3." A newer memory note says Davey's team checked the API on **Oct 19 and the campaign is FAILED** (rejected Jun 3, error 30908: opt-in not verifiable). I did not re-check it live today (files only). If that note is right, these texts can't go out until a new campaign is filed and verified, and the /draw consent checkbox could be the live opt-in evidence that the new campaign needs. Sender would be the Twilio number, which is never listed as a public contact.

Quiet hours: send only 9 AM to 8 PM Pacific. Scrub against the Do Not Contact list (email and SMS are one opt-out). Validate phone format before any send.

- **Winner notice (Wednesday, right after the winner email):**
  `Ebb & Ember: your name came up in this week's draw. Check your email and reply within 48 hrs to claim your private session. Reply STOP to opt out.`
- **Draw reminder (Tuesday, about 5 PM, to consented entrants still in the draw):**
  `Ebb & Ember: we draw this week's private session tomorrow morning. You're in. Want to come sooner? [short link] Reply STOP to opt out.`

## 6. Social (Kimberlynn)

Every giveaway post and its caption carries: "No purchase necessary. 21+. [IF limited: OR and WA residents.] Not sponsored by or affiliated with Instagram/TikTok. Rules: link in bio." Never "wood-fired", never "a float", no health claims, cold plunge shown as optional at least once per piece. Real footage only. Check the photo library for PRIVACY-HOLD before using any guest face.

### Launch Reel (IG, 15 to 20 sec; opens on the jump per card c09)

| Time | Shot | On-screen text (Inter) |
|:-|:-|:-|
| 0 to 2s | Someone steps off the deck into the river, splash | we're giving this away every week |
| 2 to 5s | Steam rolling out of the door, river through the glass | a private session on the Columbia |
| 5 to 9s | Group on the deck, wrapped in towels, rain or late light | you + your people. nobody else. |
| 9 to 13s | Someone sitting on the ladder, not going in | plunge optional. always. |
| 13 to 17s | Phone screen filling the form, or a hand dropping a slip in a jar | comment PRIVATE for the link |
| 17 to 20s | BASAL end card | winner drawn every Wednesday |

Caption:
> Every Wednesday we draw one name for a private weekday session at Ebb & Ember. Comment PRIVATE and we'll send you the link, or tap the link in bio. Who are you bringing?
>
> No purchase necessary. 21+. Not sponsored by or affiliated with Instagram. Rules: link in bio.

Audio: river and steam sound under a quiet track. No voiceover needed.

### Carousel (IG, 6 slides)

1. **Cover:** Win a private weekday session on the Columbia. (Photo: deck, river, steam)
2. **What you'd win:** [IF A: The whole big sauna for you and your crew, a weekday afternoon.] [IF B: A private sauna for 2 to 4, a weekday afternoon.]
3. **How to enter:** Link in bio, or comment PRIVATE. 20 seconds. Name and email.
4. **When:** We draw every Wednesday morning. Winner hears from us that day.
5. **What a session is:** Heat. River (optional). Deck. Repeat.
6. **The small print:** No purchase necessary. 21+. Full rules at the link in bio. Not affiliated with Instagram.

Caption: "One name every Wednesday. Tag the person you'd bring in the comments (tagging isn't an entry, the link is). Comment PRIVATE for the link."

### TikTok (20 to 30 sec, built on our two search phrases)

Search phrases to hit in on-screen text, voiceover and caption: **"date night spots portland oregon"** and **"girls activity for a rainy day in portland"**. Say each one out loud once; TikTok indexes speech.

| Time | Shot | Voiceover | On-screen text |
|:-|:-|:-|:-|
| 0 to 3s | Rain hitting the river, shot from inside the sauna | "If you're looking for date night spots in Portland, Oregon," | date night spots portland oregon |
| 3 to 8s | Couple stepping out into the rain, steam off their shoulders | "this is a sauna floating on the Columbia River." | floating sauna. columbia river. |
| 8 to 13s | Friends laughing on the deck in the rain | "And if you need a girls activity for a rainy day in Portland, the rain is kind of the point." | girls activity for a rainy day in portland |
| 13 to 18s | Ladder, someone deciding, then going in (or not) | "Heat, river, deck. The plunge is optional." | plunge optional |
| 18 to 25s | Text over the river | "Every Wednesday we give away a private weekday session. Link in bio." | win a private session. link in bio. |

Caption:
> Date night spots in Portland, Oregon, or a girls activity for a rainy day in Portland: a floating sauna on the Columbia River. We draw a private weekday session every Wednesday. Link in bio. No purchase necessary. 21+. Not sponsored by or affiliated with TikTok.
>
> #portlandoregon #pdx #datenightportland #rainydayportland #floatingsauna #coldplunge

Note: rain is the feature here, per the brand doc. Never "don't let the rain stop you."

### Weekly winner post template (IG post + story; TikTok optional)

Only after the winner OKs first name and last initial. Photo only if they send one or say yes.

- **Image:** a real deck or river shot from that week (or the winner's own photo with OK), text overlay: "This week's winner: [First name L.]"
- **Caption:**
  > This week's private session goes to [First name L.]. [Optional, with OK: one line they gave us.]
  >
  > Next draw is Wednesday [DATE]. Link in bio to enter. Who would you bring?
  >
  > No purchase necessary. 21+. Not sponsored by or affiliated with Instagram. Rules: link in bio.
- **Story:** same image, link sticker to /draw?src=ig, poll sticker "Would you plunge? yes / ladder / no way".

## 7. Build checklist by owner

Nothing goes live from this list without Davey's explicit go right before it happens. Build everything as inactive or hidden first.

### L: ActiveCampaign + Periode codes

| # | Step | [VERIFY] |
|:-|:-|:-|
| 1 | Create tags `weekday-draw`, `src-popup`, `src-banner`, `src-ig`, `src-tiktok`, `src-qr`, `src-share`, `src-email`, `draw-winner`; fields `sms_consent`, `age_21_confirmed`, `draw_entry_date`, [IF residency] `state` | |
| 2 | Build the form (section 2) with the hidden `src` field | AC hidden field fills from URL param; if not, one form per source |
| 3 | Confirm the unsubscribe link is hosted one-click and the `List-Unsubscribe` header is URL form with `List-Unsubscribe-Post`, no mailto | AC header behavior |
| 4 | Import SendGrid unsubscribes/bounces and the Do Not Contact list into AC suppression | Whether this was done when AC took over |
| 5 | Build the automation: Email 1 instant, Email 2 day 3, Email 3 weekly Wednesday, Email 4 [Friday], Email 5 handoff, exits per section 4. Leave INACTIVE | AC plan supports split subjects inside automations |
| 6 | Periode prize code: 100% off, 1 use, valid 30 days, limited to the prize product | Whether Periode codes can restrict day of week and start times (L confirmed date, product, uses, seats in Oct). If not: a weekday-only prize product, or the winner books by reply and L books it by hand into a slot with zero Social bookings |
| 7 | Use the Discount Template + internal note on each code so it shows in discount tracking | |
| 8 | Decide how Periode bookings reach AC for the Email 4 skip | Periode to AC sync for single bookings |
| 9 | Send test entries from all 5 sources; confirm tags, emails, headers in Gmail and Apple Mail | |

### Jess: Squarespace + rules page

| # | Step | [VERIFY] |
|:-|:-|:-|
| 1 | Build the /draw page with the AC form embed, unlisted until launch | Final URL |
| 2 | Build the rules page from section 3, unlisted, linked from /draw, popup, banner and every email | |
| 3 | Popup: once per visitor, 20 sec mobile / exit intent desktop, A/B 50/50, hidden on booking pages, for members and for `utm_source=google` | Whether Squarespace's popup can A/B and scope by page and UTM, or this needs Footer Code Injection |
| 4 | Banner: A/B, every page except booking pages | Whether the announcement bar can A/B; fallback is alternate weeks |
| 5 | Fire GA4 events `draw_popup_view`, `draw_popup_click`, `draw_banner_click`, `draw_form_submit` | Footer injection can send GA4 events |
| 6 | QR codes for deck and lounge pointing to /draw?src=qr, plus a small sign | Sign placement OK with marina neighbors |
| 7 | Check /draw and the popup on a phone, one-handed, on weak signal | |

### Kimberlynn: social

| # | Step | [VERIFY] |
|:-|:-|:-|
| 1 | Cut the launch Reel and the TikTok from existing footage; build the carousel | Footage without PRIVACY-HOLD faces |
| 2 | Set bio links to /draw?src=ig and /draw?src=tiktok | TikTok account can show a bio link |
| 3 | Comment PRIVATE: decide manual DM replies vs a tool | IG comment-to-DM needs a tool like ManyChat; nothing set up today (decision 16) |
| 4 | Pin the rules line as a comment on every giveaway post | |
| 5 | Weekly winner post every Wednesday after the winner OKs their name | |
| 6 | Draft everything in Asana for Davey's OK before posting | |

### Claude: weekly draw automation + reporting

Run `/design-review` before building this; it's a scheduled job.

| # | Step | [VERIFY] |
|:-|:-|:-|
| 1 | Weekly job on the always-on Mac (davids-mbp-2), Wednesday about 9 AM PT. Read-only pull of contacts tagged `weekday-draw` with entry dates in the period from the AC API | AC API key location and read-only scope |
| 2 | Filter: 21+ confirmed, [residency], not staff, not a winner in the last [6] months, not unsubscribed, deduped by Gmail-normalized email | |
| 3 | Pick one at random with a logged seed; write the entry count, seed and pick to a vault draw log | |
| 4 | DM Davey in Slack with the pick and one alternate. Davey (or L) approves and sends the winner notice. Nothing goes to the winner automatically | |
| 5 | Every Monday: report to the vault and Slack with entries by source, popup/banner A/B, email opens/clicks/unsubs per subject, codes redeemed, and entrants who booked within 30 days (match vs Periode export) | Periode export includes guest email |
| 6 | Alert if weekly entries drop under [PLACEHOLDER] or unsubscribes go over 1% | |

### Davey

- Answer section 8.
- Approve every first send, post and code, and each weekly winner.
- Twilio: confirm the A2P status and refile the campaign with the /draw opt-in before any text.

## 8. Decisions (answer by number)

From the concept doc, unchanged:
1. Draw (recommended in the concept) or a private session for every signup?
2. Prize: the Private Party now (A), or wait for the private saunas (B)? Private saunas aren't open yet, so B can't be promised until there's an opening date.
3. Weekly or every two weeks? (Copy says "every Wednesday"; switch to "every other Wednesday" if biweekly.)
4. Include the SMS opt-in now, or email only until A2P is verified?
5. Launch date. The week of Nov 2 avoids the Nov 1 pricing change.

New from this build:
6. **Popup conflict with Funnel Lab c21.** The concept doc calls this the "offer" popup Davey approved in c21, but the board shows c21 picked A, the **quiz** popup. Which runs: giveaway popup instead of the quiz, A/B against it, or giveaway now and quiz later?
7. **Entries: one draw or carry over?** Does a signup count for one week, or stay in for [4] weeks? Carry-over grows the pool and gives a reason to open the Wednesday email.
8. **Residency and legal review.** Open to anyone 21+ in the US, or Oregon and Washington residents only? And does Todd Key (or another attorney) read the rules before launch?
9. **Tuesday conflict.** The prize is Mon to Thu at 1 or 3 PM, but Tuesday 1 to 7 PM is now the industry happy hour in the big sauna (Oct 19 update). Drop Tuesday from the prize? Also check whether Monday Banya blocks Monday afternoons.
10. **SMS consent wording.** Use the tighter version in section 2 (names the two texts, frequency, not a condition of entry) instead of "the occasional offer"?
11. **Who sends the winner notice and issues the code each week:** L or Davey? (Claude picks and drafts; a person sends.)
12. **Winner publicity:** first name + last initial only, photo only with OK. Agree?
13. **Who's excluded:** current members? Past winners for how long ([6] months suggested)? Staff and families (yes, in the draft rules).
14. **Prize value for the rules.** Rules need an ARV. Set it after the Nov 1 pricing is final; it stays off every other piece of copy.
15. **Guest age for the winner's group.** Entrants are 21+. What's the minimum for the guests they bring?
16. **Comment PRIVATE:** manual DM replies by Kimberlynn, or set up a tool (ManyChat or similar)? Or skip comments and use the bio link only.
17. **Sponsor name on the rules:** which LLC is the legal sponsor for Ebb & Ember?
18. **Private Party capacity:** live FAQ says up to 10, the website rebuild draft says up to 12. Which is right?

## 9. Self-check (run Oct 20 2026)

| Rule | Result |
|:-|:-|
| "Ebb & Ember" with ampersand everywhere | Pass |
| Never wood-fired; never "a float" | Pass |
| No prices or dollar figures anywhere | Pass (ARV and economics are placeholders) |
| Private saunas: 2 to 4 people, not promised as open; Private Party = big sauna | Pass |
| Emails signed "Ebb & Ember", reply-to davey@, no personal name | Pass |
| Unsubscribe = hosted one-click URL + List-Unsubscribe-Post, no mailto | Pass (AC behavior is [VERIFY]) |
| SMS consent-only, gated on A2P verified, STOP language, quiet hours | Pass |
| Sweepstakes: no purchase necessary, 21+, residency flagged, platform disclaimer | Pass |
| No em dashes or double dashes in this file's text | Pass (checked by search; the filename's dash is the given path) |
| Plain ASCII punctuation in email copy, sentence-case subjects, A/B subject + preview on every email, CTA above the fold | Pass |
| No health or feeling promises; plunge always optional | Pass |
| Concept decisions left open | Pass (1 to 5 unchanged) |
