# 04 Organic Posts + Survey Page Copy

*Drafted 2026-10-06, fixed 2026-10-08 after the second review pass. Draft only: nothing here is posted, sent, published, or deployed. Dates are round 1, the November 2026 drawing. Everything in `{braces}` is config or an open decision. `{rules_url}` and `{survey_url}` are the rules draft's {RULES_URL} and {SURVEY_URL}. `[VERIFY: ...]` means nobody has confirmed it. Entry rules follow the rules draft: 5 entries max per person, bonus entries only from the follow-up questions, no referral entries, and the entry counts only after the confirm tap in our email. [VERIFY: blueprint sections 3 and 4 still show a personal referral link and a 10-entry cap. This doc follows the rules draft until the two agree.]*

**Lines everyone pastes from:**

| Name | Text |
|:-|:-|
| SCAM GUARD (every contest post and every story frame 3) | We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. |
| ENTRY LINE (Instagram and TikTok) | The quick survey at the link in our bio is the entry. Tap the confirm button in the email we send and you're in. |
| DISCLOSURE, Meta (last line of every Facebook and Instagram caption that mentions the drawing) | No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram. |
| DISCLOSURE, TikTok caption | No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with TikTok. |
| DISCLOSURE, TikTok on-screen (last 2 to 3 seconds, readable) | Free boat ride sweepstakes. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. 1 winner, random draw. Prize value $1,200. Rules at the link in bio. |
| DISCLOSURE, short (story frames) | No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

Every caption below is pasted in full anyway, so nobody has to assemble it.

## 1. Survey page copy

One question per screen, big buttons, tap only. Question 1 is required (rules 4a). Questions 2 to 5 can be skipped. Nothing is saved until the email is submitted.

| Element | Copy |
|:-|:-|
| Headline | What do you love most about New Orleans? |
| Intro line | Five taps and your email gets you a shot at a free private tiki boat ride for you and up to 24 friends. Free to enter. About a minute. |
| Progress label | 1 of 5 (then 2 of 5, and so on) |
| Skip link, questions 2 to 5 | Skip this one |
| Question 1 error | Pick one to keep going. |

| # | Question | Buttons (exact) |
|:-|:-|:-|
| 1 | What do you love most about New Orleans? | The food / The music / Going out / The bayou and the gators / Parades and festivals / The people |
| 2 | Where's home? | New Orleans area / A drive away / I'd fly in |
| 3 | If you win the boat, who's coming? | Bachelorette crew / Bachelor crew / Birthday crew / Friends, no reason needed / Family and the cousins / Work crew / A date or a few of us |
| 4 | How many would you bring? | 2 to 6 / 7 to 12 / 13 to 18 / 19 or more |
| 5 | When could you see yourself out here? | In the next 30 days / The holidays / Mardi Gras season / Spring or summer 2027 / No plans, I'm here for the free boat |

**The form (screen 6), top to bottom:**

| Element | Copy |
|:-|:-|
| Form headline | Last step. Where do we send your result? |
| Field label | First name |
| Field label | Email |
| Line under the email field (exact, from the rules draft) | We'll email you about the drawing, plus New Orleans trip tips and offers from NOLA Party Barge. Unsubscribe with one click anytime. It won't change your entry. |
| Email error | That email doesn't look right. |
| Sweepstakes paragraph | Below. Right above the button, normal text size, not behind a link. |
| Consent checkbox (exact, from the rules draft; unchecked by default, required, "Official Rules" links to {rules_url}) | [ ] I'm 21 or older, I live in the United States, and I agree to the Official Rules. |
| Checkbox error | Check the box to enter. |
| Button | Enter the drawing |
| Under the button, small | We'll email you a confirm button. Your entry counts once you tap it. One entry per person: the same email twice doesn't double anything. |

No phone field. No pre-checked boxes. Save the checkbox state, the exact wording shown, the timestamp, and the IP with the lead.

**Sweepstakes paragraph (exact, from the rules draft, November dates filled in):**

> NOLA Party Barge November 2026 Free Boat Ride Sweepstakes. NO PURCHASE NECESSARY. A purchase won't improve your chances. Open to legal residents of the 50 United States and D.C. who are 21 or older. Starts Thursday, October 22, 2026 and ends Sunday, November 15, 2026 at 11:59 PM Central. One winner will be picked in a random drawing on or about Monday, November 16, 2026. Prize: one private tiki boat ride of about 1 hour 45 minutes on Bayou Bienvenue for the winner and up to 24 guests. Approximate retail value $1,200. BYOB: no alcohol is included. Eligible days and blackout dates apply, and the ride must be taken by Sunday, May 16, 2027. Odds depend on how many eligible entries we get. Limit 5 entries per person. Your entry counts once you tap the confirm button in our email. You can also enter by mail without the survey. See the Official Rules: {rules_url}. Void where prohibited. Sponsor: {SPONSOR_LEGAL_NAME}, doing business as NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. This sweepstakes is not sponsored, endorsed, administered by, or associated with Meta, Facebook, Instagram, or TikTok, and by entering you release them from any liability. Your answers and email go to NOLA Party Barge, not to those platforms.

Rules 4a and this paragraph both count the entry at the confirm tap. [VERIFY: counsel, question 6b.]

**Config, not copy.** `MONTH_YEAR`, `START_DATE`, `END_DATE`, `DRAW_DATE`, `RIDE_BY_DATE`, `rules_url`, `survey_url`, `SPONSOR_LEGAL_NAME`, and the question 5 buttons live in config and change each round. The page reads them at render time. Nothing hardcodes the open date: if Oct 19 is a no-go, the open moves to Thu Oct 29 or Thu Nov 5 and the close stays Sun Nov 15. December's values: open Mon Nov 16 12:00pm, close Sun Dec 13 11:59pm, draw Mon Dec 14, ride by Mon Jun 14, 2027, and its own rules page. Between a close and the next open (Sun 11:59pm to Mon noon), the page hides the form and shows: "Entries for the November drawing closed Sunday at 11:59pm. We draw today at noon. The December drawing opens at noon." Needs build. (The alternative is opening December at 12:00 AM Mon Nov 16; the rules draft's placeholder table flags the choice.)

**Result page ("Your New Orleans type").** The copy lives in `copy/asks.md`, PAGE RESULT, which is the master for the six types. Under the type, in this order:

1. Tap the email we just sent to lock in your entry. It's from info@nolapartybarges.com. Not there in 10 minutes? Check spam.
2. The first two follow-up questions as buttons: "Who plans things in your group?" (I do / The group chat does / Somebody else) and "Full send or chill?" (Full send / Chill / A little of both). Tap feedback: "Saved. Tap the email to make it count." No entry count shows before the confirm tap.
3. No share button, no referral link, no "tag a friend". "Family and the cousins" never sees the $59 seats line (seats are 21+).
4. Footer links: Official Rules and Privacy, same as the survey page.

## 2. Launch post set

Five concepts from the organic brief, adjusted: six options, close Sun Nov 15, story ladder from Thu Oct 22, the survey plus the confirm tap is the only entry. Instagram gets the joke, Facebook gets the details, never the same caption. Footage from 2022 or later only. Option order never changes.

**Pinned first comment on every feed post:** "Comments are for arguing. The quick survey is the entry, then one tap on the confirm button in our email. Link in bio." On Facebook, swap "Link in bio" for nolapartybarges.com/win.

### Concept 1: The crew can't agree (launch hero, Sat Oct 24)

**Shoot:** 20 to 25 seconds, handheld at the dock, by Sat Oct 17. Six answers, one person each, fast cuts, their own words. The last one is deadpan: "The gators. Obviously." Captain closes: "Settle it. Your answer on the survey gets you in the drawing for this boat." End card, 3 seconds: the six options stacked like buttons, "Pick one." `[VERIFY: who shoots it and which crew are on camera]`

**Instagram caption (4:00pm CT):**

> We asked the crew the best thing about New Orleans. It got heated. 🔥
> Six crew, six wrong answers. What do YOU love most about New Orleans? Comment your pick.
> The quick survey at the link in our bio is the entry. Tap the confirm button in the email we send and you're in the drawing for a free private tiki boat ride for you and up to 24 friends.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**Facebook caption (5:30pm CT, the cut with the end card):**

> We asked our crew the best thing about New Orleans and it got heated. Six crew members, six different answers, zero agreement. Settle it for us.
>
> What do you love most about New Orleans?
> 1. The food
> 2. The music
> 3. Going out
> 4. The bayou and the gators
> 5. Parades and festivals
> 6. The people
>
> Comment your number. Then take the quick survey, that's the actual entry, and tap the confirm button in the email we send: nolapartybarges.com/win
>
> One winner gets a private tiki boat ride for you and up to 24 friends. 1 hr 45 min on Bayou Bienvenue, about 15 minutes from the French Quarter. Captain and crew, Bluetooth sound system, party lights, bathroom on board, BYOB. Covered and heated once it gets cold. 4.9 stars, 3,800+ reviews.
>
> Free to enter. Drawing is Monday, Nov 16. Comments are for arguing, the survey is the entry.
>
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**TikTok (6:00pm CT).** `[VERIFY: which TikTok account posts this. The existing handle carries the old brand name. If none is clean, skip TikTok for round 1.]` Content disclosure setting "Your brand" on. Commercial Music Library audio only. No drinks in frame.

| On-screen text | When |
|:-|:-|
| We asked the crew the best thing about New Orleans 👀 | 0 to 2 sec |
| Each answer as a caption, one at a time | the cuts |
| Pick one. (six options stacked) | end card, 3 sec |
| The survey at the link in bio is the entry. Then tap the confirm button in our email. | end card |
| Free boat ride sweepstakes. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. 1 winner, random draw. Prize value $1,200. Rules at the link in bio. | last 2 to 3 sec |

> We asked the crew the best thing about New Orleans. It got heated. 🔥 What do you love most about New Orleans? The quick survey at the link in bio is the entry for a free private tiki boat ride for you and up to 24 friends. Tap the confirm button in our email and you're in.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with TikTok.

**3 story frames (Sun Oct 25 reshare, and any reshare after):**

| Frame | What's on it |
|:-|:-|
| 1 | 5-second clip, the gator line. Text: "The crew can't agree. Can you?" |
| 2 | Poll sticker: "What do you love most about New Orleans?" The food / The music / Going out / The bayou and the gators. Small text: "Parades and the people are on the survey too. Next frame." |
| 3 | Link sticker to /win-story, label "Take the survey". Text: "Your pick is worth a shot at a free private tiki boat ride for you and up to 24 friends. The quick survey is the entry, then one tap in our email." Small text: We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

### Concept 2: The part of New Orleans most visitors never see (Facebook hero, Sun Oct 25, the one to put $15 a day behind)

**Edit:** 20 to 30 seconds from footage we have: the surge barrier reel, the drone gator shot, the bayou. On-screen in order: "Most people fly home from New Orleans without ever seeing this." / "15 minutes from the French Quarter." / "This is our favorite part of the city. What's yours?" / the six options. `[VERIFY: nothing on screen beyond gators, herons, cypress, and the storm surge barrier. No wall or wildlife stats.]`

**Facebook caption (5:30pm CT, first):**

> Most people fly home from New Orleans without ever seeing this.
>
> Bayou Bienvenue. Gators, herons, cypress, and the storm surge barrier, about 15 minutes from the French Quarter. It's our favorite part of the city. What's yours?
>
> 1. The food
> 2. The music
> 3. Going out
> 4. The bayou and the gators
> 5. Parades and festivals
> 6. The people
>
> Comment your number, then take the quick survey to get in the drawing and tap the confirm button in the email we send: nolapartybarges.com/win
>
> One winner gets a private tiki boat ride out here for you and up to 24 friends. 1 hr 45 min, captain and crew, Bluetooth sound system, bathroom on board, BYOB. Covered and heated in winter. Free to enter. Drawing is Monday, Nov 16.
>
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**Instagram caption (4:00pm CT):**

> Most people fly home without ever seeing this. 🐊
> It's 15 minutes from the French Quarter and it's our favorite part of the city. What's yours? Comment it.
> The quick survey at the link in our bio is the entry. Tap the confirm button in the email we send and you're in the drawing for a free private tiki boat ride for you and up to 24 friends.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**TikTok (6:00pm CT).** Same settings as Concept 1. On-screen: the four lines from the edit note, then "Link in bio = the entry. Then tap the confirm button in our email.", then the on-screen disclosure for the last 2 to 3 seconds.

> Most people fly home from New Orleans without ever seeing this. 🐊 15 minutes from the French Quarter. What's your favorite part of the city? The quick survey at the link in bio is the entry for a free private tiki boat ride for you and up to 24 friends. Tap the confirm button in our email and you're in.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with TikTok.

**3 story frames:**

| Frame | What's on it |
|:-|:-|
| 1 | Surge barrier clip. Text: "Most visitors never see this. 15 minutes from the Quarter." |
| 2 | Poll sticker: "Ever been out on Bayou Bienvenue?" Yes 🐊 / Didn't know it existed |
| 3 | Link sticker to /win-story, label "Take the survey". Text: "The quick survey is the entry for a free private tiki boat ride out here for you and up to 24 friends. Then one tap in our email." Small text: We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

**If it runs as an ad** (act_87863118, not the Boost button): skip the short link, use the Facebook caption above, and paste `utm_source=fb&utm_medium=paid&utm_campaign=survey_contest&utm_content={{ad.name}}` in the URL parameters field. Ad set age targeting 21+ (the caption says BYOB). For the organic run, set the Page's audience age restriction to 21+ in Page settings until Nov 16.

### Concept 3: New Orleans, pick a side (story ladder, 9:30am CT)

Instagram stories, cross-posted to Facebook stories. No feed caption, no TikTok. Three frames a day on the ladder days in section 4. Instagram polls hold 4 options, so frame 1 shows four and the survey page carries all six.

| Frame | What's on it |
|:-|:-|
| 1 | Text: "New Orleans, pick a side." Poll sticker: "What do you love most about New Orleans?" The food / The music / Going out / The bayou and the gators. Small text: "Parades and the people are on the survey too. Last frame." Day 2 on: open with yesterday's real number first (lines below). |
| 2 | Text: "Pick a side." Two-option poll with the day's matchup: po'boy or beignet / Frenchmen or Bourbon / second line or parade / daiquiri or hurricane / crawfish or oysters / gators or ghosts (Halloween week) / streetcar or walk it / Uptown or Bywater / jazz brunch or the late set |
| 3 | Link sticker to /win-story, label "Take the survey". Text: "Your picks are worth a shot at a free private tiki boat ride for you and up to 24 friends. The quick survey is the entry, then one tap in our email." Small text: We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

**Next-morning openers (real numbers only, change the wording daily):**

- {pct}% of you said Frenchmen. The rest of you, we need to talk.
- Po'boy took it, {pct}%. Beignet people, you had your chance.
- {pct}% picked gators over ghosts. Bold, for Halloween week.
- Food is winning the big one so far, {pct}%. Music, you're not far behind.

### Concept 4: Pick a number (the Facebook giveaway post, Sat Oct 24, pinned)

**Video:** a proven crowd clip (2022 or later) with "WIN THIS BOAT" on screen, then "A free private tiki boat ride for you and up to 24 friends." Pin the post to the top of the page until Nov 16.

**Facebook caption (5:30pm CT):**

> We're giving away a free private tiki boat ride for you and up to 24 friends. You just have to tell us one thing.
>
> What do you love most about New Orleans?
> 1. The food
> 2. The music
> 3. Going out
> 4. The bayou and the gators
> 5. Parades and festivals
> 6. The people
>
> Comment your number. Then take the quick survey to get in the drawing: nolapartybarges.com/win
>
> The prize: a private tiki boat ride, 1 hr 45 min on Bayou Bienvenue, 15 minutes from the French Quarter. Captain and crew, Bluetooth sound system and party lights, bathroom on board, BYOB with a bar to set up your drinks. Covered and heated once it's cold. Retail value $1,200, and the winner pays nothing. 4.9 stars, 3,800+ reviews.
>
> How it works: free to enter, 21+, US only. Entries close Sunday, Nov 15 at 11:59pm CT. One winner, random drawing Monday, Nov 16. Comments, likes, and shares don't count as entries. The survey does. Then tap the confirm button in the email we send. That locks it in. Answer the quick follow-up questions after you enter and you can get up to 5 entries.
>
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**Instagram caption (spare, not on the calendar; Concept 1 is the Instagram launch post):**

> Free private tiki boat ride for you and up to 24 friends. 🚤 You just have to tell us one thing: what do you love most about New Orleans? Comment it.
> The quick survey at the link in our bio is the entry. Tap the confirm button in the email we send and you're in.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**TikTok:** none. This one is Facebook only.

**3 story frames:**

| Frame | What's on it |
|:-|:-|
| 1 | The crowd clip. Text: "WIN THIS BOAT" then "A free private tiki boat ride for you and up to 24 friends." Small text: No purchase necessary. US, 21+. Rules on the last frame. |
| 2 | Text: "You just have to tell us one thing." Poll sticker: "What do you love most about New Orleans?" The food / The music / Going out / The bayou and the gators. Small text: "Parades and the people are on the survey too." |
| 3 | Link sticker to /win-story, label "Take the survey". Text: "Free to enter. 21+, US only. Drawing Monday, Nov 16. The survey is the entry, then one tap in our email." Small text: We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

### Concept 5: Nobody stays a stranger (mid-run, Sun Nov 1; last-day cut Sun Nov 15)

**Edit:** 15 to 20 seconds of existing per-seat cruise footage where strangers end up dancing together. Guests in frame must look 21+. Text over it: "The best thing about New Orleans isn't on any list." / "It's that nobody stays a stranger here." / "What's your favorite thing about this city?" / the six options. End card, two versions. Nov 1: "Two weeks left to get in the drawing." Nov 15: "Last day to get in the drawing." `{date_line}` in the captions swaps the same way. Nov 1 = "Two weeks left. Entries close Sunday, Nov 15." Nov 15 = "Last day. Entries close tonight at 11:59pm CT."

**Instagram caption (4:00pm CT):**

> The best thing about New Orleans isn't on any list. It's that nobody stays a stranger here. 🎺
> What's the most New Orleans thing a stranger ever did for you? Tell us below.
> Then the quick survey at the link in our bio is the entry for a free private tiki boat ride for you and up to 24 friends. Tap the confirm button in our email and you're in. {date_line}
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**Facebook caption (5:30pm CT):**

> The best thing about New Orleans isn't on any list. It's that nobody stays a stranger here.
>
> That clip is one of our per-seat social cruises: $59 a seat, 21+, you show up solo or as a pair and leave with a group chat. The private boats are the other way to do it, and one of those is the prize.
>
> What's the most New Orleans thing a stranger ever did for you? Tell us in the comments.
>
> Then take the quick survey, that's the entry, and tap the confirm button in the email we send: nolapartybarges.com/win
> One winner gets a private tiki boat ride for you and up to 24 friends. 1 hr 45 min on Bayou Bienvenue, 15 minutes from the French Quarter. BYOB, bathroom on board, covered and heated in winter. {date_line}
>
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

**TikTok:** not in the brief's plan. Only cut it if a clip with no drinks in frame exists (that rules out most party footage). Then use Concept 1's settings, the same on-screen lines plus "Link in bio = the entry. Then tap the confirm button in our email.", the on-screen disclosure, and the TikTok caption line from the table at the top.

**3 story frames:**

| Frame | What's on it |
|:-|:-|
| 1 | The clip. Text: "Nobody stays a stranger here." |
| 2 | Question sticker: "The most New Orleans thing a stranger ever did for you?" (answers land in DMs; Nolan replies with the /win-dm script in section 3) |
| 3 | Link sticker to /win-story, label "Take the survey". Text: "{date_line} The quick survey is the entry for a free private tiki boat ride for you and up to 24 friends. Then one tap in our email." Small text: We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number. No purchase necessary. US, 21+. Ends Sunday, November 15, 2026. Rules: {rules_url}. Not affiliated with Meta. |

### Mid-run and close posts (on the calendar, short)

**Results reel, Thu Oct 29 (Instagram 4pm, Facebook 5:30pm). Real numbers only.** On-screen: "{n} of you answered." / "{pct_top}% said {top}." / "The gators want a recount."

> Instagram: {n} of you answered. {pct_top}% said {top}. The gators want a recount. 🐊 Still time: the quick survey at the link in our bio is the entry for a free private tiki boat ride for you and up to 24 friends. Tap the confirm button in our email and you're in. Entries close Sunday, Nov 15.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

Facebook: the same, with the numbered list of six and "take the quick survey to get in the drawing, then tap the confirm button in our email: nolapartybarges.com/win" in place of "link in our bio", then the scam guard and the Meta disclosure line.

**Last call, Sun Nov 15 (Instagram 4pm, Facebook 5:30pm).** The Concept 5 last-day cut, or a results update if Concept 5 already ran Nov 1:

> Instagram: Last day. {n} of you are in and {pct_top}% said {top}. Entries close tonight at 11:59pm CT and we draw tomorrow at noon. The quick survey at the link in our bio is the entry for a free private tiki boat ride for you and up to 24 friends. Tap the confirm button in our email tonight and you're in.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, November 15, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

Facebook: the same, with nolapartybarges.com/win, the scam guard, and the Meta disclosure line.

**Round closed, Mon Nov 16, story only (9:30am):** "Round 1 is closed. {n} entries. Drawing today at noon. Round 2 opens at noon, next drawing Mon Dec 14." Link sticker labeled "Rules" pointing at {rules_url} until noon, then "Take the survey" to /win-story after noon, once the December round is open. Small text: the scam guard, then the short disclosure with Sunday, December 13, 2026 as the end date and December's {rules_url}.

**Winner post (only after the winner has replied by email, passed the ID check, and signed the release). First name, last initial, city, state. Never a requirement to post or tag.**

> Instagram: Our November winner: {first_name} {last_initial}. from {city}, {state}. See you on the bayou. 🚤 For the record, {pct_top}% of you said {top}. December's drawing is Mon Dec 14. The quick survey at the link in our bio is the entry, then one tap on the confirm button in our email.
> We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
> No purchase necessary. US residents 21+ only. Ends Sunday, December 13, 2026 at 11:59 PM CT. One winner, random drawing. Prize: a private tiki boat ride for you and up to 24 guests, value $1,200. BYOB, no alcohol included. Rules and free mail-in entry: {rules_url}. Not sponsored, endorsed, administered by, or associated with Meta, Facebook, or Instagram.

Facebook: the same, with "take the quick survey, then tap the confirm button in our email: nolapartybarges.com/win" in place of "link in our bio", the scam guard, and the December Meta disclosure line. Pin it where Concept 4 was.

## 3. Comment and DM replies

**Rules:** public reply inside 60 minutes, 9am to 9pm CT. Change the wording every time (copy-paste replies read as spam). One private reply per commenter, inside 7 days, link included, and no second message unless they write back. Never argue. Hide spam, slurs, and anyone who posts their email or phone (then send them the link privately). If a post passes about 50 comments in a day, switch the public reply to "DM us BOAT for the link." On Facebook, add nolapartybarges.com/win to every public reply.

**Public reply to someone who answered in the comments** (thanks them, points them to the survey page, says comments aren't entries):

| They said | Instagram reply (Facebook: add nolapartybarges.com/win) |
|:-|:-|
| The food | Correct answer. The food is undefeated. Make it official though: the quick survey at the link in our bio is what gets you in the drawing, then one tap on the confirm button in our email. Comments don't count, they're just for arguing. |
| The music | Frenchmen on a random Tuesday will change a person. Agreed. The survey in our bio is the entry, the comment isn't, so go tap it and then tap the confirm email. |
| Going out | Respect. Pace yourself. The quick survey at the link in our bio is the actual entry (plus one tap in our email). This comment is just you being right in public. |
| The gators | A person of taste. The gators say hi. Link in bio, the survey there is what gets you in the drawing. Tap the confirm button in our email after. |
| Parades and festivals | Throw me something. Love it. Comments aren't entries though. The quick survey at the link in our bio is, then the confirm button in our email. |
| The people | Softest answer in the thread and also the right one. Now go make it count: survey at the link in our bio, then tap the confirm email. That's the entry. |
| All of it | Fair. Narrow it down for us on the survey (link in bio) and tap the confirm button in our email, and you're in. |
| How do I enter? | Free to enter, 21+, US only. Take the quick survey at the link in our bio, then tap the confirm button in the email. Full rules are on that page. Comments don't count as entries. |
| A number with no words (Facebook) | A {number} person, noted. Thanks for playing. The survey is the entry, not the comment, then one tap in our email: nolapartybarges.com/win |
| A troll or a complaint | One friendly line or nothing. |

**Nolan DM script (OpenCX, one message, link in it).** Triggers: BOAT, win, giveaway, contest, drawing, sweepstakes, free boat, survey, and any story reply or question-sticker answer during the round. `[VERIFY: OpenCX can send a private reply off a post comment. If not, a person sends these by hand from the Business Suite inbox.]`

| Where | Message |
|:-|:-|
| Instagram DM | Hey {first_name}! Saw your answer. It's worth a shot at a free private tiki boat ride for you and up to 24 friends. The quick survey is what enters you: nolapartybarges.com/win-dm Free to enter, 21+, US only. Rules are on that page. Tap the confirm button in the email to lock it in. |
| Facebook Messenger | Hey {first_name}! Saw your answer. It's worth a shot at a free private tiki boat ride for you and up to 24 friends. The quick survey is what enters you: nolapartybarges.com/win-fbdm Free to enter, 21+, US only. Rules are on that page. Tap the confirm button in the email to lock it in. |

| If they write back with | Nolan says |
|:-|:-|
| Did it work? / No email | If you got the email from info@nolapartybarges.com, tap the button in it. That's what locks in the entry. Nothing in 10 minutes? Check spam. Still nothing, tell me the email you used and a person will look. |
| Can I enter twice? | One entry per person, same email every time. Answer the follow-up questions on the result page and in our emails and you can get up to 5. |
| Did I win? / When's the drawing? | The drawing is Monday, Nov 16 at noon. We only email the winner, from info@nolapartybarges.com. Nobody hears "you won" from a DM. |
| Someone DM'd me that I won | That's not us. We never DM a winner and we never ask for a card number. Report and block that account. The real notice only ever comes by email from info@nolapartybarges.com. |
| Anything about booking or prices | Hand off to Nolan's normal booking flow. The contest and the boats are separate conversations. |

**"Is this real?" (comment or DM, same answer):**

> Real. One winner, random draw Monday, Nov 16 at noon, picked from the confirmed survey entries. The ride is worth about $1,200 and the winner pays nothing: no deposit, no fees. Free to enter, 21+, US only. We only contact the winner by email from info@nolapartybarges.com, never by DM, and we'll never ask for a card number. Rules are here: {rules_url}

## 4. Link plan and calendar

**Links.** Same build as /boost and /boost-ig: a 302 from the slug to `{survey_url}` with UTMs, built through the Redirection plugin REST API by Sat Oct 17, tested with curl and on a phone on cellular (the edge cache served a stale target for minutes on Sep 23). Every link carries `utm_campaign=survey_contest`. All seven slugs were free on 2026-10-03.

| Short link | Used for | utm_source | utm_medium | utm_content | Goes to |
|:-|:-|:-|:-|:-|:-|
| nolapartybarges.com/win | Facebook feed captions, pinned first comments, public replies on Facebook | fb | social | feed | {survey_url} |
| /win-ig | Instagram bio link, first of the 5 bio links. Every reel says "link in bio" | ig | social | bio | {survey_url} |
| /win-story | Story link stickers | ig | social | story | {survey_url} |
| /win-dm | Instagram DMs and private replies, Nolan or a person | ig | social | dm | {survey_url} |
| /win-fbdm | Messenger and Facebook private replies | fb | social | dm | {survey_url} |
| /win-tt | TikTok bio link | tiktok | social | bio | {survey_url} |
| /win-yt | YouTube Shorts description, only if the hero reel is cross-posted | youtube | social | shorts | {survey_url} |
| "Win a Boat Ride" nav item (label pending sign-off, section 5), footer item, old giveaway URL, site chat | On-site, so no UTMs (a UTM on an internal link overwrites the real source in GA4) | none | none | none | {survey_url} plain |
| An ad in act_87863118 | No short link. URL parameters field: `utm_source=fb&utm_medium=paid&utm_campaign=survey_contest&utm_content={{ad.name}}` | fb | paid | ad name | {survey_url} |

Bio links: Instagram holds 5. Order: /win-ig, the booking link, then the rules page labeled "Sweepstakes rules" (plain {rules_url}, no UTMs), because Instagram captions aren't clickable and the disclosure line names the rules. TikTok holds one: /win-tt, and the survey page carries the rules link one tap in. The survey page reads `utm_*` off the URL and passes it to `POST /lead` with `source=survey`. Read results in GA4 property 322288940, Traffic acquisition, Session campaign = survey_contest, plus Session manual ad content. A "survey finished" key event needs build.

**Two-week calendar, Thu Oct 22 to Wed Nov 4 (all times CT, nothing after 9pm).** The Facebook queue keeps posting at 11am and 4pm; contest posts go at 5:30pm so they stay the newest thing on the page overnight. Instagram feed at 4:00pm. Stories at 9:30am. Past-guest emails go out Tue Oct 27 and Tue Nov 17 from a separate system: no change.

| Date | 9:30am stories | 4:00pm Instagram | 5:30pm Facebook | Notes |
|:-|:-|:-|:-|:-|
| Thu Oct 22 | Ladder: question 1 poll, "po'boy or beignet", link | none | none | Entries open, quiet. Bio links switch (/win-ig first, rules third). "Win a Trip!" and the old giveaway URL switch to the survey. Small traffic on purpose |
| Fri Oct 23 | Yesterday's number, "Frenchmen or Bourbon", "Something drops tomorrow at 4", link | none | none | Final check of all 7 links on a phone |
| **Sat Oct 24** | Question 1 poll, link | **Concept 1 hero reel.** Pin it | **Concept 4 giveaway post.** Pin it | LAUNCH. TikTok cut of Concept 1 at 6pm. Pinned first comment on both. Someone on comment duty 4 to 7pm |
| **Sun Oct 25** | Concept 1 frames 1 to 3 (reshare the reel) | **Concept 2** | **Concept 2**, long caption, /win | Best Instagram day. TikTok cut of Concept 2 at 6pm |
| Mon Oct 26 | "Food is winning so far" with real numbers, "second line or parade", link | none | none | Comment sweep from the weekend, private replies |
| Tue Oct 27 | Yesterday's number, "daiquiri or hurricane", link | none | none | Checkpoint: if Concept 2 is pulling comments, start the $15 a day ad in act_87863118 |
| Wed Oct 28 | Yesterday's number, "crawfish or oysters", link | none | none | Quiet |
| Thu Oct 29 | Link sticker only | **Results reel**, real numbers | Same, long caption, /win | |
| Fri Oct 30 | "gators or ghosts", link | none | none | Halloween weekend owns the feed |
| Sat Oct 31 | Yesterday's number, link | none | none | Halloween. No contest feed posts |
| **Sun Nov 1** | "Two weeks left", link. Second story at 6:30pm: Concept 5 clip, link | **Concept 5**, two-weeks-left end card | **Concept 5** cut, long caption, /win | Clocks fall back this morning. Mid-run reminder, not last call |
| Mon Nov 2 | "{n} entries so far. Closes Sun Nov 15", "streetcar or walk it", link | none | none | Comment sweep |
| Tue Nov 3 | none | none | none | Ladder drops to two a week from here |
| Wed Nov 4 | none | none | none | Usual non-contest reels keep going so the feed isn't all contest |

**Through the close (two ladders a week, then the last call):**

| Date | 9:30am stories | Feed | Notes |
|:-|:-|:-|:-|
| Thu Nov 5 | Ladder: question 1 poll, "Uptown or Bywater", link | none | |
| Sun Nov 8 | Yesterday's number, "jazz brunch or the late set", link | none | |
| Thu Nov 12 | "We draw Monday." Question 1 poll, link | none | The draw countdown email goes out the same morning |
| Sat Nov 14 | "Closes tomorrow night at 11:59pm CT", link | none | |
| **Sun Nov 15** | "Last day", link. Second story at 6:30pm: "Closes tonight at 11:59pm CT", link | Instagram 4pm: last-call reel. Facebook 5:30pm: last-call post, /win | The only day "last day" is allowed |
| Mon Nov 16 | "Round 1 is closed. {n} entries. Drawing today at noon. Round 2 opens at noon, next drawing Mon Dec 14." | none | Winner post only after the winner replies, passes the ID check, and signs |

After that: one contest post a month per platform, two story ladders a week, and the normal reels in between.

## 5. Nav item, top banner, Nolan

| Spot | What it says | Where it goes |
|:-|:-|:-|
| Main nav and footer item | Win a Boat Ride. Blueprint decision 11 kept the old "Win a Trip!" label, but rules section 8 excludes travel, lodging, food, and drinks, so "trip" overstates the prize. Needs sign-off before Oct 22 (blueprint decision 11). | {survey_url}, plain, no UTMs |
| Old giveaway URL /new-orleans-booze-cruise-giveaway/ | Nothing. 301 it to the survey and retire the GoHighLevel form, so the old 18+ terms and the old brand name stop coexisting with the new rules | {survey_url}, plain |
| Top banner | Stays with the Countdown, not the contest (decision 11, one offer per spot). Line from the lead magnet plan: "Coming to New Orleans? Get the free NOLA Countdown + $50 off a private boat." | The Countdown hub page (doc 05 owns it) |
| Survey page, bottom | A one-line footer link, no UTMs: "Official Rules" and "Privacy" | {rules_url}, {PRIVACY_URL} |

**Nolan on site chat** (plain link, no UTMs; the page records `source=survey` anyway):

| They say | Nolan says |
|:-|:-|
| win, giveaway, contest, drawing, sweepstakes, free boat, survey, "Win a Trip" | Yep, the drawing's on. Five quick taps and your email, then one tap in the email we send, and you're in the drawing for a free private tiki boat ride for you and up to 24 guests: {survey_url} Free to enter, 21+, US only. Rules are on that page. |
| Did it work? / No email | Tap the button in the email from info@nolapartybarges.com. That's what locks in the entry. Nothing in 10 minutes? Check spam. Still nothing, tell me the email you used and a person will look. |
| Is this real? | The "Is this real?" answer in section 3, with {rules_url}. |
| Booking, prices, dates | Normal booking flow. Don't mix the contest into a booking conversation. |

## 6. What to avoid

1. Tag-a-friend, share-to-enter, comment-to-enter, follow-to-enter: Meta bans it, and a comment gives us no email. The survey plus the confirm tap is the only entry.
2. "Book your boat" tails, sunset as the hook, party footage as the whole idea, the same caption on both platforms, and any 2020 or 2021 footage.
3. Calling the $50 code a prize, "you won" to anyone but the verified winner, drinks in the TikTok cut, "booze cruise giveaway".
4. Posting after 9pm CT, Monday for anything that matters, the Boost button (build the ad in act_87863118), and "last day" on any day but Sun Nov 15.
5. A contest comment sitting unanswered past 60 minutes, a local spot that isn't in the Sept 30 spots file, and any promise of texts.
