# Survey Contest Funnel: Emails

What this is: every email in the NOLA Party Barge survey contest funnel, assembled from the reviewed copy files (contest, warmup, blocks, asks), plus the block library, the tap questions with their answer pages, the small pages, and the open facts.
Date: 2026-10-06. Facts are as of the facts file (2026-10-03) and the Blueprint (doc 01).
Status: draft, nothing sent. Nothing here is posted, published, committed, or deployed.
How to read it: Part 1 lists the emails in send order. A slot in double braces, like {{MATH-SIZE}}, pulls a version from the block library in Part 3 at send time. A placeholder in single braces, like {first_name} or {code_end}, fills at send time. Part 2 shows three finished emails with everything filled in.

Conventions the renderer follows (so Part 1 doesn't repeat them 23 times):
- Every email ends the same way: the tap question is the last line of the body, then {signer} (default: The crew at NOLA Party Barge; who signs is decision 9), then the P.S. if there is one, then the FOOTER block from Part 3.
- The P.S. of most emails is {{CODE-PS}}. It renders only when the $50 code is live, in its last days, or after a booking. Locked means no P.S. at all.
- Tap buttons come from the ask bank in Part 4. If the named question is already answered, the engine asks the first unanswered bonus question instead (planner, vibe, buy_mode, intent, blocker, trip_month). Nothing renders at 5 of 5 entries or once the round is closed. Routing taps (reentry, stay, holdup, locals_topic) always render.
- Entries: 1 for the confirm tap, +1 for each of the first 4 bonus questions answered, 5 max. No referral entries (the rules draft cut them under Meta's promotion rules), so the Blueprint's friend-link lines are gone.
- The $50 code is an offer, not a prize. Non-winner copy never calls it a win or a runner-up anything.
- Dates, {days_left}, prices with the code, and {per_person} are computed at send time. {days_left} counts today, so the last day shows 1.
- Reply-To on every send is info@nolapartybarges.com.
- SC-10c is not in the Blueprint's list of 18. The review added it so crews of 2 to 6 get a result email with seat and pontoon math and no code (decision 7).

## Contents

- [[#Part 1. The emails, in send order]]
  - [[#SC-01 Confirm your entry]]
  - [[#SC-01b Confirm your entry (24 hour nudge)]]
  - [[#SC-02 Bonus entries]]
  - [[#SC-03 Your pick, like a local]]
  - [[#SC-04 The boat day, your version]]
  - [[#SC-05 The math for your crew]]
  - [[#SC-06 What your group chat will ask]]
  - [[#SC-07 The answer to your one doubt]]
  - [[#SC-08a Draw countdown]]
  - [[#SC-08b Last call]]
  - [[#SC-09 Winner notice]]
  - [[#SC-10 Result and your $50]]
  - [[#SC-10b Result (booked guest)]]
  - [[#SC-10c Result (crew of 2 to 6)]]
  - [[#SC-11 One week left on the code]]
  - [[#SC-12a Code countdown (day before)]]
  - [[#SC-12b Code countdown (last day)]]
  - [[#SC-13 Hot unlock]]
  - [[#SC-14 What's the hold-up?]]
  - [[#SC-15 Still want these?]]
  - [[#SC-16 See you on the bayou]]
  - [[#SC-17 Bridge to the NOLA Countdown]]
  - [[#SC-18 Locals list welcome]]
- [[#Part 2. Three finished samples]]
  - [[#Kayla's SC-05]]
  - [[#Marcus's SC-13]]
  - [[#Dee's SC-10]]
- [[#Part 3. Block library]]
- [[#Part 4. Ask bank, answer pages, and small pages]]
- [[#Part 5. VERIFY list]]

Round 1 values used in this doc: {round} = November, {next_round} = December, {draw_date} = Mon Nov 16, {close_date} = Sun Nov 15, {code} = BAYOU50-NOV, {code_end} = Mon Nov 30. Round 2: December, January, Mon Dec 14, Sun Dec 13, BAYOU50-DEC, Thu Dec 31.

## Part 1. The emails, in send order

| ID | Name | Sends | Button | Tap question |
|:-|:-|:-|:-|:-|
| SC-01 | Confirm your entry | Instant on submit | Confirm my entry | none |
| SC-01b | Confirm your entry (24 hour nudge) | +24h, unconfirmed only | Confirm my entry | none |
| SC-02 | Bonus entries | Day 1 | none | planner |
| SC-03 | Your pick, like a local | Day 3 | none | vibe |
| SC-04 | The boat day, your version | Day 6 | See the boats | buy_mode |
| SC-05 | The math for your crew | Day 9 | Check open dates | intent |
| SC-06 | What your group chat will ask | Day 12 | What to expect | blocker |
| SC-07 | The answer to your one doubt | Day 15 | Check your date | first_unanswered |
| SC-08a | Draw countdown | Thu before the draw | none | first_unanswered |
| SC-08b | Last call | Close day | none | first_unanswered |
| SC-09 | Winner notice | Draw day, winner only | none | none |
| SC-10 | Result and your $50 | Draw day 2pm | Use my $50 | reentry |
| SC-10b | Result (booked guest) | Draw day 2pm, booked | What to expect | reentry |
| SC-10c | Result (crew of 2 to 6) | Draw day 2pm, crews of 2 to 6 | See the boats | reentry |
| SC-11 | One week left on the code | Monday after the draw | Check open dates | none |
| SC-12a | Code countdown (day before) | Day before the code dies | Use my $50 | none |
| SC-12b | Code countdown (last day) | Last day of the code | Book today | none |
| SC-13 | Hot unlock | Morning after 2nd boat click | See open dates | first_unanswered |
| SC-14 | What's the hold-up? | 5 days after SC-13 | none | holdup |
| SC-15 | Still want these? | Day 9 slot, zero taps | none | stay |
| SC-16 | See you on the bayou | Morning after /booked | What to pack | first_unanswered |
| SC-17 | Bridge to the NOLA Countdown | Day after SC-07, visitors | Start my Countdown | trip_month |
| SC-18 | Locals list welcome | Day after SC-07, locals | none | locals_topic |

### SC-01 Confirm your entry

**When and who:** The second they submit the survey, any day of the week, to everyone who submits (up to 500 a day in week 1; past that the page says the email comes at 9am tomorrow).

**Subject:** One tap locks in your entry for a free private tiki boat

Subject variants:
- like=food: You said the food. One tap locks in your entry
- like=music: You said the music. One tap locks in your entry
- like=night: You said going out. One tap locks in your entry
- like=wild: You said the gators. One tap locks in your entry
- like=parade: You said parades. One tap locks in your entry
- like=people: You said the people. One tap locks in your entry

**Preview:** No tap, no entry. We draw {draw_date} at noon. The ride costs the winner nothing.

**Body:**

{{LIKE-ECHO}}
Your New Orleans type: {type}. Now the part that counts.
One tap on the button puts you in the {round} drawing. No tap, no entry. That rule keeps the bots out, and it means a real person has to want this.
The prize: a private tiki boat for you and up to 24 guests. 1 hour 45 minutes on Bayou Bienvenue with captain and crew, sound system, party lights, and a bathroom on board. BYOB, so no drinks are included. About $1,200 if you paid for it. The winner pays nothing.
Tap before {close_date} at 11:59pm Central and your entry counts. We draw {draw_date} at noon. Every bonus question after that is one tap and one more entry, up to 5, the most anyone gets.
One more thing. We only contact the winner by email from info@nolapartybarges.com, and we'll never ask for a card number.

**Button:** Confirm my entry (link: confirm)

**Tap question:** none (the confirm button is the tap)

**P.S.:** Didn't take our survey? Somebody typed your email by mistake. Don't tap the button. One reminder comes, then nothing.


### SC-01b Confirm your entry (24 hour nudge)

**When and who:** 24 hours after SC-01, once, to anyone who submitted and hasn't tapped confirm. Never after the round closes (Sun Nov 15, 11:59pm Central for round 1).

**Subject:** Your entry isn't locked in yet. One tap fixes it

Subject variants:
- like=food: You said the food, but your entry isn't locked in yet
- like=music: You said the music, but your entry isn't locked in yet
- like=night: You said going out, but your entry isn't locked in yet
- like=wild: You said the gators, but your entry isn't locked in yet
- like=parade: You said parades, but your entry isn't locked in yet
- like=people: You said the people, but your entry isn't locked in yet

**Preview:** We draw {draw_date}. Nothing counts until you tap. This is the only reminder.

**Body:**

{{LIKE-ECHO}}
You took the survey for the {round} drawing, a free private tiki boat for you and up to 24 guests, but the entry isn't locked in yet. One tap does it.
No tap, no entry. Tap before {close_date} at 11:59pm Central. We draw {draw_date} at noon. For anyone who isn't the winner, that boat costs about $1,200.
This is the only reminder. After this we leave you alone.

**Button:** Confirm my entry (link: confirm)

**Tap question:** none (the confirm button is the tap)

**P.S.:** Wrong person? Ignore this and nothing else comes.


### SC-02 Bonus entries

**When and who:** Day 1 after the confirm tap, on every pacing, to every confirmed entrant.

**Subject:** You're in: {entries} of 5 entries for the {round} boat drawing

Subject variants:
- entries=5: You're in: 5 of 5 entries for the {round} boat drawing

**Preview:** Each question we ask is one tap and one entry, up to 5. We draw {draw_date} at noon.
- Preview when entries=5: Nothing left to tap. We draw {draw_date} at noon.

**Body:**

{{STATS-LINE}}
Here's how the rest work, {first_name}. Each bonus question we ask from here is one tap. Answer it and that's one more entry, until you hit 5. Nothing to buy, nobody to tag. Just taps.
Do them all today or one at a time. Entries close {close_date} at 11:59pm Central, and we draw {draw_date} at noon.
First one's easy.

**Button:** none. The tap buttons are the action.

**Tap question:** Who plans things in your group?

Buttons (planner): I do / The group chat does / Somebody else
- Tap when entries=5: none

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)

**Whole-body variant when entries=5:**

{{STATS-LINE}}
You did the questions already, {first_name}. Entries close {close_date} at 11:59pm Central, and we draw {draw_date} at noon.
Next email is the fun one: three spots for what you said you love about New Orleans.


### SC-03 Your pick, like a local

**When and who:** Day 3 after the confirm tap (day 2 on the fast pacing for people riding in the next 30 days), to confirmed entrants who aren't quiet. Prize-only entrants get it too.

**Subject:** Where we'd send a friend who said {like_label}

**Preview:** No boat talk today. Just the places locals argue about.

**Body:**

{{ECHO-LINE}}
Quick one, {first_name}. No boat talk today.
You told us what you love about New Orleans. Here's where we'd send a friend for exactly that.
{{LIKE-PICKS}}
{{HOME-LINE}}
Go to one. Then one tap, so the next email fits your crew:

**Button:** none. The tap buttons are the action.

**Tap question:** Full send or chill?

Buttons (vibe): Full send / Chill / A little of both

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-04 The boat day, your version

**When and who:** Day 6 (day 4 on the fast pacing), to confirmed entrants who aren't quiet. Prize-only entrants get it too.

**Subject:** What 1 hour 45 minutes on the bayou looks like for your crew

**Preview:** Start to finish, your version. Bathroom on board, BYOB, your playlist.

**Body:**

{{ECHO-LINE}}
Here's the boat day, {first_name}, start to finish. The prize should be a real thing in your head, not a line on a rules page.
{{CREW-SCENE}}
{{LIKE-BOAT}}
{{HOME-LINE}}
{{WHEN-PS}}

**Button:** See the boats (link: boats)

**Tap question:** Seats or the whole boat?

Buttons (buy_mode): A few seats / The whole boat / Not sure yet

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-05 The math for your crew

**When and who:** Day 9 (day 6 on the fast pacing), to confirmed entrants who are selling OK and not booked.

**Subject:** What a boat day costs each person in your crew

**Preview:** Flat boat prices split by heads, and what it takes to hold a date.

**Body:**

{{ECHO-LINE}}
Before anyone in the group chat says yes, they ask the same thing: what's this going to cost me? So here's the math, {first_name}.
{{MATH-SIZE}}
A private boat is one flat price, so every person you add brings the per-head number down. Use that on the holdouts.
{{WHEN-PS}}
Open dates are behind the button. Looking isn't booking.

**Button:** Check open dates (link: dates)

**Tap question:** If you don't win, would you still do this?

Buttons (intent): Planning one / Maybe / Only if it's free

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-06 What your group chat will ask

**When and who:** Day 12 (day 8 on the fast pacing), same audience as SC-05.

**Subject:** The 5 questions your group chat will ask, answered

**Preview:** How far, ages, bathroom, drinks, weather. Paste, don't type.

**Body:**

{{ECHO-LINE}}
The second you float a boat day, {first_name}, the group chat turns into a Q and A. Same five questions every time. Here they are, answered, so you can paste instead of type.
{{CREW-FAQ}}
{{HOME-LINE}}
And the pitch itself, written the way you'd write it. Copy it, drop it in, and let them fight about the date.
{{CREW-SHARE}}

**Button:** What to expect (link: expect)

**Tap question:** What would stop your crew?

Buttons (blocker): Price / Weather / Getting everyone to commit / Don't know that part of town / Nothing, we're in

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-07 The answer to your one doubt

**When and who:** Day 15 (day 10 on the fast pacing), same audience as SC-05.

**Subject:** The one thing that might stop your crew, answered

Subject variants:
- blocker unanswered: What guests say after the ride: 4.9 stars across 3,800+ reviews

**Preview:** Plus 4.9 stars across 3,800+ reviews, if you'd rather hear it from guests.

**Body:**

{{ECHO-LINE}}
Short one, {first_name}. You've got the picks, the boat day, the math, and the group chat answers. One thing left, and it's usually the thing that decides it.
{{DOUBT-ANSWER}}
{{PROOF}}

**Button:** Check your date (link: dates)

**Tap question:** {{ASK-BANK}}

The first unanswered bonus question, in this order: planner, vibe, buy_mode, intent, blocker, trip_month (buttons in Part 4). Renders nothing at 5 of 5 entries or once the round is closed.

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-08a Draw countdown

**When and who:** The Thursday before the draw at 10am (Thu Nov 12, then Thu Dec 10), to every confirmed entrant who entered 3 or more days ago, quiet and booked included.

**Subject:** We draw {draw_date}. You have {entries} of 5 entries

**Preview:** Entries close {close_date} at 11:59pm Central. One tap adds one if you're under 5.

**Body:**

{{STATS-LINE}}
Entries close {close_date} at 11:59pm Central. We draw {draw_date} at noon, with two people in the room and a public random number, so anyone can check the math.
A question waiting at the end of this? One tap, one more entry. Takes less time than reading this.
No question waiting? You're done. Go about your week.
The prize is one private tiki boat for you and up to 24 guests, about $1,200 worth, BYOB, at no cost to the winner.

**Button:** none. The tap buttons are the action.

**Tap question:** {{ASK-BANK}}

The first unanswered bonus question, in this order: planner, vibe, buy_mode, intent, blocker, trip_month (buttons in Part 4). Renders nothing at 5 of 5 entries or once the round is closed.

**P.S.:** Win or not, you'll hear from us after the draw.


### SC-08b Last call

**When and who:** Close day at 10am (Sun Nov 15, then Sun Dec 13), to entrants who tapped in the last 14 days, are under 5 entries, still have a bonus question open, and aren't quiet.

**Subject:** Last call: entries close {close_date} at 11:59pm Central

**Preview:** You have {entries} of 5 entries. The list freezes at midnight. We draw {draw_date}.

**Body:**

{{STATS-LINE}}
Entries close at 11:59pm Central tonight. We draw {draw_date} at noon.
You're under 5, and the question at the end of this email is one tap, one entry, and the last one this round.
After tonight the list freezes and nothing changes it. Not even us.

**Button:** none. The tap buttons are the action.

**Tap question:** {{ASK-BANK}}

The first unanswered bonus question, in this order: planner, vibe, buy_mode, intent, blocker, trip_month (buttons in Part 4). Renders nothing at 5 of 5 entries or once the round is closed.

**P.S.:** No purchase, no sharing, no tagging. Answering questions is the only way to add entries.


### SC-09 Winner notice

**When and who:** Draw day (Mon Nov 16, then Mon Dec 14) by 1pm after the manager check, to the potential winner only. A reminder at 48 hours if no reply, then the next name once {reply_deadline} passes. Nobody else ever gets it.

**Subject:** You were drawn: NOLA Party Barge free boat ride ({round} drawing)

**Preview:** Reply by {reply_deadline}. It costs you nothing. No deposit, no fees.

**Body:**

{{WIN-OPEN}}
The boat: about 1 hour 45 minutes on Bayou Bienvenue with captain and crew. About $1,200 value. BYOB, so no drinks are included.
It costs you nothing. No deposit, no fees.
Three steps:
1. Reply to this email by {reply_deadline}. A one-word yes works.
2. We check your ID (21 or older, US address) by video call or at the dock. We don't keep a copy. Then a short form to e-sign through DocuSeal, within 7 days.
3. A written prize confirmation within 10 days: open days, blackout dates, ride-by date, how to book. [VERIFY: counsel question 3]
Rides run Sunday through Thursday [VERIFY: decision 2]. Ask 14 days ahead, ride within 6 months of the drawing. Nothing's final until we confirm it in writing.
No reply by {reply_deadline}, and the Official Rules have us draw the next name. We'd rather it be you.
Official Rules: {rules_url}

**Button:** none. The reply is the action.

**Tap question:** none (the reply is the action)

**P.S.:** This went only to you. Nothing gets posted until your form is signed, and the announcement is just your first name, last initial, city, and state. [VERIFY: decision 10 and counsel question 3: whether the name post is part of the signed release or needs a separate yes]


### SC-10 Result and your $50

**When and who:** Draw day at 2pm in batches, most recent tappers first (leftovers the Wednesday after, 10am), to every confirmed non-winner who hasn't booked and isn't a crew of 2 to 6. Quiet and prize-only included.

**Subject:** Not this time. But $50 off a private boat, good until {code_end}

**Preview:** One name got drawn. The {round} result, your crew's math, and one tap for {next_round}.

**Body:**

{{LIKE-ECHO}}
The {round} drawing ran {draw_date} at noon. One name came up, and it wasn't yours. Not this time.
Here's the part that doesn't depend on luck:
{{CODE-PS}}
{{MATH-SIZE}}
{{HOME-DEAL}}
To be clear, that's a discount, not a prize. After {code_end} it's gone.
Want another shot at the free one? {next_round} is its own drawing with its own tiki boat. One tap below puts you in at 1 entry. No tap, and the drawing emails stop.

**Button:** Use my $50 (link: book)

**Tap question:** Put me in the {next_round} drawing

Buttons (reentry): Put me in the {next_round} drawing

**P.S.:** Once the form is signed and the winner says yes, we'll share who's taking the boat out: first name, last initial, city, and state.


### SC-10b Result (booked guest)

**When and who:** Same send as SC-10, to confirmed non-winners who have already booked. No code, no math.

**Subject:** Not your name this time. Your boat day stands, and {next_round} is one tap away

**Preview:** One name got drawn. Your booking is already on the calendar.

**Body:**

{{LIKE-ECHO}}
The {round} drawing ran {draw_date} at noon. One name came up, and it wasn't yours. Not this time.
The good news: you didn't need luck. Your boat day is already on the calendar.
Want in on {next_round}? Fresh drawing, its own tiki boat, and a booked guest whose name comes up rides twice. One tap puts you in at 1 entry.

**Button:** What to expect (link: expect)

**Tap question:** Put me in the {next_round} drawing

Buttons (reentry): Put me in the {next_round} drawing

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-10c Result (crew of 2 to 6)

**When and who:** Same send as SC-10, to confirmed non-winners with a crew of 2 to 6 who haven't booked. Seats and pontoon math, no code (decision 7).

**Subject:** Not this time. Here's what a boat day costs for a crew your size

**Preview:** One name got drawn. The {round} result, the price for a crew your size, and one tap for {next_round}.

**Body:**

{{LIKE-ECHO}}
The {round} drawing ran {draw_date} at noon. One name came up, and it wasn't yours. Not this time.
Here's the part that doesn't depend on luck, the price for a crew your size:
{{MATH-SIZE}}
Want another shot at the free one? {next_round} is its own drawing with its own tiki boat. One tap below puts you in at 1 entry. No tap, and the drawing emails stop.

**Button:** See the boats (link: boats)

**Tap question:** Put me in the {next_round} drawing

Buttons (reentry): Put me in the {next_round} drawing

**P.S.:** Once the form is signed and the winner says yes, we'll share who's taking the boat out: first name, last initial, city, and state.


### SC-11 One week left on the code

**When and who:** The Monday after the draw at 10am (Mon Nov 23, then Mon Dec 21), to non-winners who aren't booked, aren't quiet, are selling OK, and aren't a crew of 2 to 6.

**Subject:** {days_left} days left on {code}: $50 off a private boat until {code_end}

**Preview:** Book by {code_end}, ride any open date. $350 holds the boat.

**Body:**

It's been a week since the {round} drawing, {first_name}.
{{PROOF}}
Meanwhile, the clock: {days_left} days left on {code}.
{{MATH-SIZE}}
{{HOME-DEAL}}
You don't need the whole crew to commit this week. Pick a date, put down the deposit, and let the group chat catch up.

**Button:** Check open dates (link: dates)

**Tap question:** none (the button is the action)

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-12a Code countdown (day before)

**When and who:** The day before the code dies at 10am (Sun Nov 29, then Wed Dec 30), to the same group as SC-11 who are also hot, or tapped Planning one, or clicked a boat link since the draw.

**Subject:** {code} ends {code_end} at 11:59pm. $50 off a private boat goes with it

**Preview:** Only the booking has to happen by {code_end}. The ride can be any open date.

**Body:**

One heads-up before it goes, {first_name}. {code} ends {code_end} at 11:59pm Central. After that a private boat is back to full price.
{{MATH-SIZE}}
Only the booking has to land by then. The ride can be any open date after, even months out.
Booked already? Then ignore this. The code emails stop as soon as your booking posts.

**Button:** Use my $50 (link: book)

**Tap question:** none (entries are closed; the button is the action)

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-12b Code countdown (last day)

**When and who:** The last day of the code at 9am (Mon Nov 30, then Thu Dec 31), to non-winners who aren't booked, aren't a crew of 2 to 6, and clicked a boat link since the draw.

**Subject:** Last day for {code}: $50 off a private boat ends {code_end} at 11:59pm

**Preview:** After tonight {code} is gone. Pick a date, put down the deposit, done.

**Body:**

You've been looking at dates since the drawing, {first_name}. Today's the day. {code} ends at 11:59pm Central tonight, and tomorrow a private boat is full price again.
{{MATH-SIZE}}
If the group chat is still deciding, you don't need them to. The booking has to happen today. The ride doesn't.
Stuck between two dates? Reply with both and a person on the crew will tell you which one's open.

**Button:** Book today (link: book)

**Tap question:** none (entries are closed; the button is the action)

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-13 Hot unlock

**When and who:** 9am the next open morning after a second boat or pricing click (10 or more minutes apart, inside 7 days), to hot leads who aren't booked, aren't a crew of 2 to 6, and whose code is still locked. A manager gets an alert the same day.

**Subject:** You don't have to wait for the drawing

**Preview:** $50 off a private boat is live for you now. Your entry stays in.

**Body:**

You've been looking at the boats, {first_name}. So let's skip the wait.
Your $50 off a private boat is live. The code is in the math below, and its end date is at the bottom. Your entry in the {round} drawing stays in. Booking doesn't change that, and if your name comes up after you book, you ride twice.
{{MATH-SIZE}}
{{HOME-DEAL}}
Need the group chat version? Paste this:
{{CREW-SHARE}}
Reply to this email with a date and a real person on the crew will check it for you.

**Button:** See open dates (link: dates)

**Tap question:** {{ASK-BANK}}

The first unanswered bonus question, in this order: planner, vibe, buy_mode, intent, blocker, trip_month (buttons in Part 4). Renders nothing at 5 of 5 entries or once the round is closed.

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-14 What's the hold-up?

**When and who:** 5 days after SC-13 on the next open day, once, to hot leads who got SC-13 and still haven't booked (not quiet, not a crew of 2 to 6). Needs build.

**Subject:** Price, the date, or the group? One tap tells us

**Preview:** Price, the date, the group, or just looking. Tap one and the answer page has the fix.

**Body:**

Still thinking it over, {first_name}? Fair. A boat for your whole crew isn't an impulse buy, no matter what the group chat says at midnight.
This isn't a nudge. We want to know what's actually in the way, so the next thing we send is useful instead of loud. Tap one below. Two seconds, and the answer page says what we can do about it.
Your $50 off a private boat is still live. The code and its end date are at the bottom.

**Button:** none. The tap buttons are the action.

**Tap question:** What's the hold-up?

Buttons (holdup): Price / The date / Getting the group to commit / Just looking

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-15 Still want these?

**When and who:** Takes the day 9 slot (day 8 on the fast pacing), to confirmed entrants with zero taps and zero clicks since confirming. No tap in 7 days sets quiet.

**Subject:** Keep the New Orleans tips coming, or just the drawing?

**Preview:** One tap. Your entry stays in either way.

**Body:**

{{LIKE-ECHO}}
Since you entered we've sent a few emails and you haven't tapped a thing. That's fine. Maybe they're landing in spam, maybe you're just here for the free boat.
One tap tells us which: keep them coming, just the drawing, or take me off.
Your entry stays in no matter what you pick. Even "take me off" keeps you in the {round} drawing. We'd just stop writing.

**Button:** none. The tap buttons are the action.

**Tap question:** Still want these?

Buttons (stay): Keep them coming / Just the drawing / Take me off

**P.S.:** No tap in a week and we take the hint: drawing emails only.


### SC-16 See you on the bayou

**When and who:** The next open morning after a booking is posted to /booked, to the booked guest. Selling stops after this; the entry stays in.

**Subject:** You're booked. What to bring on your NOLA Party Barge day

**Preview:** Your boat is on the calendar. Here's what to pack and where the dock is.

**Body:**

You booked, {first_name}. Thank you. The crew will have the lights on and the bar set up for whatever you bring.
{{HOME-LINE}}
Pack your drinks (BYOB, with a bar on board to set them up), a playlist for the Bluetooth sound system, and a layer if it's cold. The boat is covered and heated in winter, but the bayou breeze is real.
Captain and crew are included. Every boat but the Luxury Pontoon has a bathroom on board.
Booking doesn't change your drawing entry. If your name ever comes up, that's a second boat day at no cost.

**Button:** What to pack (link: pack)

**Tap question:** {{ASK-BANK}}

The first unanswered bonus question, in this order: planner, vibe, buy_mode, intent, blocker, trip_month (buttons in Part 4). Renders nothing at 5 of 5 entries or once the round is closed.

**P.S.:** {{CODE-PS}} (only when the code is live, in its last days, or after a booking; otherwise there is no P.S.)


### SC-17 Bridge to the NOLA Countdown

**When and who:** The day after SC-07 (or the day it would have sent), or the day they tap a month, whichever is first, to visitors (home = drive, fly, or unanswered) with some timing and at least one tap or boat click. Late bloomers get it the day after the code dies.

**Subject:** Your New Orleans trip, one chapter at a time

**Preview:** Tell us the month. We send the good stuff when it's actually useful.

**Body:**

{{LIKE-ECHO}}
This one's about your trip, not the boat, {first_name}.
We write a thing called The NOLA Countdown. Twelve short chapters timed to your dates: where to eat, how to get around, what to wear, and a Crew's Pick local spot in every one. Each chapter lands when it's useful, not six weeks early.
The only thing it needs is your month. Already told us? Chapter one is next. Not yet? One tap below does it, or hit the button if you've got exact dates.
{{WHEN-PS}}

**Button:** Start my Countdown (link: countdown)

**Tap question:** Got dates yet?

Buttons (trip_month): November / December / January / February / March / April / Not yet

**P.S.:** This is the trip side. The drawing runs on its own, by email, and nothing here changes your entry.


### SC-18 Locals list welcome

**When and who:** The day after SC-07 (or the day it would have sent), or 3 days after booking, to locals with at least one tap or boat click.

**Subject:** Locals get first dibs on open boats

**Preview:** Two emails a month, tops. No coupon, no fluff.

**Body:**

{{LIKE-ECHO}}
No trip guide for you, {first_name}. You live here. What you need is to know when there's a boat open on a Thursday.
That's what this list is. When a boat has open seats or an open private date, you hear first. Two emails a month at most, and one of those is just the drawing.
No coupon, no fluff. First dibs is the perk.
{{HOME-LINE}}

**Button:** none. The tap buttons are the action.

**Tap question:** What do you want to hear about?

Buttons (locals_topic): Weeknight openings / Holiday boats / Just the drawing

**P.S.:** Nothing here changes your entry in the drawing. Locals can win it too.

**Whole-body variant when group_type=family:**

{{LIKE-ECHO}}
No trip guide for you, {first_name}. You live here. What you need is to know when there's a boat open on a Thursday.
That's what this list is. When a private boat has an open date, you hear first. Two emails a month at most, and one of those is just the drawing.
No coupon, no fluff. First dibs is the perk.
{{HOME-LINE}}
What do you want to hear about?


## Part 2. Three finished samples

Made-up people from Blueprint section 9, same launch weekend. Every slot and placeholder is filled. Signed links ({rules_url}, {unsub_url}, the button) are generated per person at send, so they appear here as (link). {signer} renders its default until decision 9 lands.

| | Kayla | Marcus | Dee |
|:-|:-|:-|:-|
| Survey answers | The food, I'd fly in, bachelorette crew, 13 to 18, spring or summer 2027 | The music, New Orleans area, friends (no reason needed), 7 to 12, the next 30 days | The bayou and the gators, a drive away, family and the cousins, 19 or more, no plans (here for the free boat) |
| Confirmed | Sat Oct 24 | Sat Oct 24 | Sun Oct 25 |
| Taps before this email | planner = I do (SC-02), buy_mode = The whole boat (SC-04) | None. Clicked See the boats twice on Wed Oct 28 | None. Tapped Just the drawing on SC-15 (Wed Nov 4), so quiet |
| State at send | Standard pacing, code locked, 3 of 5 entries | Fast pacing, hot, code live from the confirm tap, 1 of 5 | Prize only, quiet, family guard, 1 of 5. Not the winner |
| Sample | SC-05, Mon Nov 2 | SC-13, Thu Oct 29, 9am | SC-10, Mon Nov 16, 2pm |

### Kayla's SC-05

Blocks picked: ECHO-LINE buy_mode boat, MATH-SIZE 13-18 locked (no `13-18 boat` version exists, so the plain key renders), WHEN-PS later, ask intent, CODE-PS locked (no P.S.), FOOTER default.

```
From: NOLA Party Barge <info@nolapartybarges.com>
To: Kayla
Subject: What a boat day costs each person in your crew
Preview: Flat boat prices split by heads, and what it takes to hold a date.

You said the whole boat.

Before anyone in the group chat says yes, they ask the same thing: what's this going to cost me? So here's the math, Kayla.

The Bayou Boogie is $800 flat for up to 18, about $44 each if all 18 come. From 14 people up, a private boat beats $59 seats, and you get it to yourselves.
$350 holds the boat. The rest is due the day you ride.

A private boat is one flat price, so every person you add brings the per-head number down. Use that on the holdouts.

Spring or summer 2027 is a ways out. The booking doesn't have to be: pick a date now, ride when it's warm.

Open dates are behind the button. Looking isn't booking.

        [ Check open dates ]  (link)

If you don't win, would you still do this?

        [ Planning one ]   [ Maybe ]   [ Only if it's free ]

The crew at NOLA Party Barge

You took the NOLA Party Barge survey for the free boat drawing on Sat Oct 24, 2026. Official Rules: (link)
Unsubscribe with one click: (link)
Unsubscribing doesn't remove your entry.
We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. 1 (504) 264-1056
```

No P.S.: Kayla's code is locked until the draw, so CODE-PS renders nothing.

### Marcus's SC-13

Blocks picked: MATH-SIZE 7-12 live (no buy_mode tap, not family), HOME-DEAL local, CREW-SHARE friends with {boat_price} = $750 and {per_person} = $63 (code live), ask bank first unanswered = planner, CODE-PS live, FOOTER default. {round} = November.

One catch, flagged in Part 5: Blueprint section 9 sends Marcus SC-13 on Thu Oct 29, but the reviewed SC-13 audience rule skips anyone whose code is already live (Marcus picked the next 30 days, so his went live at the confirm tap). Under the reviewed rule he'd get the manager's personal reply and no SC-13. This sample shows the email as written for a 7 to 12 friends crew who lives here.

```
From: NOLA Party Barge <info@nolapartybarges.com>
To: Marcus
Subject: You don't have to wait for the drawing
Preview: $50 off a private boat is live for you now. Your entry stays in.

You've been looking at the boats, Marcus. So let's skip the wait.

Your $50 off a private boat is live. The code is in the math below, and its end date is at the bottom. Your entry in the November drawing stays in. Booking doesn't change that, and if your name comes up after you book, you ride twice.

Seats are $59 each on a social cruise (21+). Want it to yourselves? With BAYOU50-NOV, a private Bayou Boogie is $750 flat for up to 18, about $63 each if 12 of you come.
$350 holds the boat. The rest is due the day you ride.

A weeknight, this weekend, or something months out. Only the booking has to land by Mon Nov 30.

Need the group chat version? Paste this:

No reason, we just should. Boat day in New Orleans with NOLA Party Barge: private boat, just us, on the bayou 15 min from the Quarter. BYOB with a bar on board, our playlist, a bathroom, captain drives. 1 hr 45 min. $750 for the boat, about $63 each. $350 holds it and the rest is due the day we ride. Yes or no, I'm booking this week.

Reply to this email with a date and a real person on the crew will check it for you.

        [ See open dates ]  (link)

Who plans things in your group?

        [ I do ]   [ The group chat does ]   [ Somebody else ]

The crew at NOLA Party Barge

P.S. BAYOU50-NOV takes $50 off a private boat (the Bayou Boogie, the Party Queen, or a tiki). Book by Mon Nov 30 at 11:59pm Central, ride any open date.

You took the NOLA Party Barge survey for the free boat drawing on Sat Oct 24, 2026. Official Rules: (link)
Unsubscribe with one click: (link)
Unsubscribing doesn't remove your entry.
We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. 1 (504) 264-1056
```

### Dee's SC-10

Blocks picked: LIKE-ECHO wild, CODE-PS live as a box (every non-winner's code goes live at SC-10), MATH-SIZE `19+ family` live, HOME-DEAL visitor (home = drive), ask reentry. Quiet entrants still get SC-10 (suppression rule 5). {round} = November, {next_round} = December.

```
From: NOLA Party Barge <info@nolapartybarges.com>
To: Dee
Subject: Not this time. But $50 off a private boat, good until Mon Nov 30
Preview: One name got drawn. The November result, your crew's math, and one tap for December.

You said the bayou and the gators. Our kind of people.

The November drawing ran Mon Nov 16 at noon. One name came up, and it wasn't yours. Not this time.

Here's the part that doesn't depend on luck:

  ==================================================================
  | BAYOU50-NOV takes $50 off a private boat (the Bayou Boogie, the  |
  | Party Queen, or a tiki). Book by Mon Nov 30 at 11:59pm Central, |
  | ride any open date.                                             |
  ==================================================================

With BAYOU50-NOV, a tiki is $1,150 flat for up to 25: $46 each if you fill it. The Party Queen is $850 private for up to 26: about $33 each at 26. Ages 6 and up on a private boat. More than 26 is two boats, and a person from the crew helps you sort it.
$350 holds the boat. The rest is due the day you ride.

Your trip doesn't have to happen before Mon Nov 30. The booking does.

To be clear, that's a discount, not a prize. After Mon Nov 30 it's gone.

Want another shot at the free one? December is its own drawing with its own tiki boat. One tap below puts you in at 1 entry. No tap, and the drawing emails stop.

        [ Use my $50 ]  (link)

        [ Put me in the December drawing ]

The crew at NOLA Party Barge

P.S. Once the form is signed and the winner says yes, we'll share who's taking the boat out: first name, last initial, city, and state.

You took the NOLA Party Barge survey for the free boat drawing on Sun Oct 25, 2026. Official Rules: (link)
Unsubscribe with one click: (link)
Unsubscribing doesn't remove your entry.
We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.
NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. 1 (504) 264-1056
```

Dee taps Put me in the December drawing. Her answer page: You're in the December drawing with 1 entry. Nothing else to do. One email before the draw, one on draw day. Official Rules: (link)

## Part 3. Block library

17 families. Every family has a default, so a missing answer never breaks an email. Lookup order: guarded key (for example `19+ family`), then the plain key, then `default` with the guard, then `default`. Where a version has more than one line, the lines are shown one after another in the cell.

| Family | Versions | Used in |
|:-|:-|:-|
| LIKE-ECHO | 7 | Line one of SC-01, SC-01b, SC-10, SC-10b, SC-10c, SC-15, SC-17, SC-18 |
| ECHO-LINE | 57 | Line one of SC-03 to SC-07 |
| STATS-LINE | 3 | SC-02, SC-08a, SC-08b |
| LIKE-PICKS | 7 | SC-03 |
| LIKE-BOAT | 10 | SC-04 |
| CREW-SCENE | 10 | SC-04 |
| CREW-SHARE | 9 | SC-06, SC-07 (commit), SC-13 |
| CREW-FAQ | 5 | SC-06 |
| HOME-LINE | 4 | SC-03, SC-04, SC-06, SC-16, SC-18 |
| HOME-DEAL | 3 | SC-10, SC-11, SC-13 |
| MATH-SIZE | 14 | SC-05, SC-07 (price), SC-10, SC-10c, SC-11, SC-12a, SC-12b, SC-13 |
| WHEN-PS | 9 | SC-04 and SC-05 (plain keys), SC-17 (`trip` keys) |
| DOUBT-ANSWER | 6 | SC-07 |
| PROOF | 3 | SC-07 (when blocker is unanswered) and SC-11 |
| CODE-PS | 5 | The P.S. of SC-02 to SC-07, SC-10b, SC-11 to SC-14, SC-16 |
| WIN-OPEN | 4 | SC-09 only |
| FOOTER | 2 | Every email |
| **Total** | **158** | |

MATH-SIZE arithmetic (rounded half up): Bayou Boogie $800 at 12 = about $67, at 18 = about $44; with the code $750 at 12 = about $63, at 18 = about $42. Tiki $1,200 at 25 = $48; $1,150 at 25 = $46. Party Queen $900 at 26 = about $35; $850 at 26 = about $33. Luxury Pontoon $350 at 6 = about $58, out of the code. Seats: 13 x $59 = $767 (seats win), 14 x $59 = $826 (the $800 Bayou Boogie wins), so the 14-and-up line holds.

### LIKE-ECHO

Line one of SC-01, SC-01b, SC-10, SC-10b, SC-10c, SC-15, SC-17, SC-18. By `like`.

| Version | Text |
|:-|:-|
| food | You said the food. Correct answer. |
| music | You said the music. Same. |
| night | You said going out. No judgment here. |
| wild | You said the bayou and the gators. Our kind of people. |
| parade | You said parades and festivals. A person of taste. |
| people | You said the people. Yeah. It's the people. |
| default | You told us what you love about New Orleans. |

### ECHO-LINE

Line one of SC-03 to SC-07. Names the newest thing they told us. The `like` lines are the same words as LIKE-ECHO.

| Field | Value | Line |
|:-|:-|:-|
| like | food | You said the food. Correct answer. |
| like | music | You said the music. Same. |
| like | night | You said going out. No judgment here. |
| like | wild | You said the bayou and the gators. Our kind of people. |
| like | parade | You said parades and festivals. A person of taste. |
| like | people | You said the people. Yeah. It's the people. |
| home | local | You said you live here. |
| home | drive | You said you're a drive away. |
| home | fly | You said you'd fly in. |
| group_type | bach | You said bachelorette crew. |
| group_type | bachelor | You said bachelor crew. |
| group_type | birthday | You said birthday crew. |
| group_type | just_because | You said friends, no reason needed. Best reason there is. |
| group_type | family | You said family and the cousins. |
| group_type | work | You said work crew. |
| group_type | couples | You said a date, or a few of you. |
| group_size | 2-6 | You said 2 to 6 people. |
| group_size | 7-12 | You said 7 to 12 people. |
| group_size | 13-18 | You said 13 to 18 people. |
| group_size | 19+ | You said 19 or more. Big crew. |
| ride_when | soon | You said the next 30 days. |
| ride_when | holiday | You said the holidays. |
| ride_when | mardigras | You said Mardi Gras season. |
| ride_when | later | You said spring or summer 2027. |
| ride_when | none | You said no plans, you're here for the free boat. Fair. |
| planner | me | You said you're the planner. |
| planner | chat | You said the group chat plans it. So nobody does. |
| planner | other | You said somebody else does the planning. |
| vibe | full | You said full send. |
| vibe | chill | You said chill. |
| vibe | both | You said a little of both. Same. |
| buy_mode | seats | You said a few seats. |
| buy_mode | boat | You said the whole boat. |
| buy_mode | unsure | You said you're not sure yet. That's what this one's for. |
| intent | plan | You said you're planning one. |
| intent | maybe | You said maybe. |
| intent | free | You said only if it's free. Honest. |
| blocker | price | You said price. |
| blocker | weather | You said weather. |
| blocker | commit | You said getting everyone to commit. |
| blocker | far | You said you don't know that part of town. |
| blocker | none | You said nothing's stopping you. |
| trip_month | 2026-11 | You said November. |
| trip_month | 2026-12 | You said December. |
| trip_month | 2027-01 | You said January. |
| trip_month | 2027-02 | You said February. Mardi Gras month. |
| trip_month | 2027-03 | You said March. |
| trip_month | 2027-04 | You said April. |
| trip_month | 2027-05 | You said May. |
| trip_month | 2027-06 | You said June. |
| trip_month | none | You said no dates yet. Fair. |
| holdup | price | You said price. |
| holdup | date | You said the date. |
| holdup | commit | You said getting the group to commit. |
| holdup | looking | You said just looking. |
| stay | keep | You said keep them coming. Good. |
| default | | (renders nothing) |

### STATS-LINE

SC-02, SC-08a, SC-08b. By entry count.

| Version | Text |
|:-|:-|
| count | You have {entries} of 5 entries. Five is the most anyone gets. |
| maxed | You have 5 of 5 entries, the most anyone gets. Nothing left to tap this round. |
| default | Your entry is in. Five entries is the most anyone gets. |

### LIKE-PICKS

SC-03. Three local spots for what they love, from the NOLA Spots research file.

| Version | Text |
|:-|:-|
| food | Parkway, Mid-City. The po'boy locals argue about. Closed Monday and Tuesday, so plan around it.<br>Killer Poboys, in the Quarter, inside Erin Rose. Different po'boy, same argument.<br>Clesi's, Mid-City. Crawfish when they're running, seafood the rest of the year. |
| music | The Spotted Cat, Frenchmen Street. Walk in, stay for the next set.<br>Blue Nile, same street. Do both in one night.<br>Maple Leaf, Tuesday nights. Rebirth Brass Band. That's the one you text people about afterward. |
| night | Melba's, Elysian Fields. Daiquiris, 24/7.<br>Lafitte's Blacksmith Shop, on Bourbon. The daiquiri stop when you're already in the Quarter.<br>Clover Grill, 24/7. It's cashless, so bring a card. |
| wild | Bayou Bienvenue. It's the water we run on: gators, herons, cypress, and the storm surge barrier, about 7 miles from the Quarter.<br>Two more from the crew once we've argued about them. |
| parade | Krewe du Vieux, Sat Jan 23, 2027. Marigny into the Quarter. Adult satire, and the only krewe that rolls through the Quarter. The early-season pick.<br>Muses, Thu Feb 4, Uptown. All-women krewe. The shoe is the throw everybody wants.<br>Endymion, Sat Feb 6, Mid-City. The biggest one. The neutral ground is an all-day tailgate.<br>Times and routes aren't posted yet, so check before you plan around them. |
| people | Bacchanal, Bywater. Live music, and everybody ends up talking to everybody.<br>Cafe Beignet. Shorter lines than the famous one, plus beer and wine.<br>Loretta's Authentic Pralines. Local, Black-owned. Buy more pralines than you think you need. |
| default | Parkway, Mid-City. The po'boy locals argue about. Closed Monday and Tuesday, so plan around it.<br>Killer Poboys, in the Quarter, inside Erin Rose. Different po'boy, same argument.<br>Clesi's, Mid-City. Crawfish when they're running, seafood the rest of the year. |

### LIKE-BOAT

SC-04. One line tying their pick to the boat. `family` guards where the plain line names a 21+ seat.

| Version | Text |
|:-|:-|
| food | If the food is the point, there's a boat for that: the Sunset Cocktail Cruise and Seafood Boil. About 2.5 hours, a seafood boil on the water, first drink included, from $165. |
| food family | Your own boat, ages 6 and up, 1 hr 45 min on the water. Do the po'boys before, the bayou after. |
| music | Bluetooth sound system and party lights on every boat. Your playlist runs the whole 1 hr 45 min. |
| night | BYOB, with a bar on board to set up your drinks. You pick the bottle, you pick the price. |
| wild | Bayou Bienvenue out both sides of the boat: gators, herons, cypress, the storm surge barrier. If you'd rather look than party, the Swamp Eco Tour is 2 hours, from $50. |
| wild family | Bayou Bienvenue out both sides of the boat: gators, herons, cypress, the storm surge barrier. |
| parade | A boat day fits between parades. The boats are covered and heated in winter, so a cold February afternoon on the water still works. |
| people | No crew yet? $59 gets you a seat on a social cruise (21+) with people who came to have a good time. Got a crew? Take a whole boat. |
| people family | Bring the whole family on your own boat, ages 6 and up. Nobody on it but you. |
| default | BYOB, with a bar on board to set up your drinks. You pick the bottle, you pick the price. |

### CREW-SCENE

SC-04. What 1 hr 45 min looks like for that crew. just_because renders `friends`, couples renders `couple`, crews of 2 to 6 render `2-6` (or `2-6 family`).

| Version | Text |
|:-|:-|
| bach | Here's your 1 hr 45 min. The bride and up to 24 of her people on a tiki, nobody else on it. Your playlist on the Bluetooth, party lights on, the bar set up with whatever you carried on. The captain drives, the crew handles the rest. Bathroom on board, so nobody's holding it. Gators, herons, and cypress out both sides, 15 minutes from the Quarter. |
| bachelor | Here's your 1 hr 45 min. The groom and up to 24 of his people on a tiki, nobody else on it. Your playlist on the Bluetooth, party lights on, the bar set up with whatever you carried on. The captain drives, the crew handles the rest. Bathroom on board, so nobody's holding it. Gators, herons, and cypress out both sides, 15 minutes from the Quarter. |
| birthday | Your boat, your people, your playlist on the Bluetooth, party lights on. Bring the cake and the cooler: there's a bar on board to set it all up and a bathroom so nobody has to plan around one. The captain drives, the crew handles the rest. Gators, herons, and cypress out both sides for 1 hr 45 min, 15 minutes from the Quarter. |
| friends | No occasion needed. 1 hr 45 min on the water with the people you'd actually want on a boat. Your playlist, your drinks on the bar, bathroom on board. The captain drives, the crew handles the rest. Not enough people for a whole boat? $59 gets you a seat on a social cruise (21+), and you meet the rest of the boat out there. |
| family | The whole family on your own boat, ages 6 and up. Covered, so the sun's not a problem, and heated when it's cold. Bathroom on board. The captain drives, the crew handles the rest, and the bayou does the show: gators, herons, cypress. BYOB is for the grown-ups; the bar on board holds the juice boxes too. If the kids would rather look than party, the Swamp Eco Tour is 2 hours, family friendly, from $50. |
| work | 1 hr 45 min, 15 minutes from the Quarter, so it fits between the last session and dinner. Your own boat, so you set the guest list. Playlist on the Bluetooth, or no playlist, your call. BYOB with a bar on board to set it up, bathroom on board, covered and heated in winter. The captain drives, the crew handles the rest, and a person from the crew follows up to help you plan it. |
| couple | A date, or a few of you: $59 a seat on a social cruise (21+). Bring your own drinks, there's a bar on board to set them up, and you meet the rest of the boat out there. Want it to yourselves? The Luxury Pontoon is $350 private for up to 6. No bathroom on that one, so plan accordingly. 1 hr 45 min on a social cruise, captain and crew included. |
| 2-6 | Your crew of 2 to 6: $59 a seat on a social cruise (21+). Bring your own drinks, there's a bar on board to set them up, and you meet the rest of the boat out there. Want it to yourselves? The Luxury Pontoon is $350 private for up to 6. No bathroom on that one, so plan accordingly. 1 hr 45 min on a social cruise, captain and crew included. |
| 2-6 family | The whole family on the Luxury Pontoon, private for up to 6, $350 flat. No bathroom on that one, so plan accordingly. Ages 6 and up on a private boat. The captain drives, and the bayou does the show for 1 hr 45 min: gators, herons, cypress. BYOB is for the grown-ups. If the kids would rather look than party, the Swamp Eco Tour is 2 hours, family friendly, from $50. |
| default | No occasion needed. 1 hr 45 min on the water with the people you'd actually want on a boat. Your playlist, your drinks on the bar, bathroom on board. The captain drives, the crew handles the rest. Not enough people for a whole boat? $59 gets you a seat on a social cruise (21+), and you meet the rest of the boat out there. |

### CREW-SHARE

SC-06, SC-07 (commit), SC-13. A message to paste in the group chat. {boat_price} and {per_person} come from group_size and code state (7-12: $800 and $67, or $750 and $63 with the code; 13-18: $800 and $44, or $750 and $42; 19+ and unanswered: $1,200 and $48, or $1,150 and $46).

| Version | Text |
|:-|:-|
| bach | Ok hear me out. Bachelorette boat day in New Orleans. NOLA Party Barge: a private boat, just us, on the bayou 15 min from the Quarter. Captain drives, we bring our own drinks, there's a bar on board, a bathroom, lights, our playlist. Real gators. 1 hr 45 min. It's {boat_price} for the whole boat, about {per_person} each. I'm putting $350 down to hold it and the rest is due the day we ride, so I need a yes or no from everybody this week. |
| bachelor | Ok hear me out. Bachelor boat day in New Orleans. NOLA Party Barge: a private boat, just us, on the bayou 15 min from the Quarter. Captain drives, we bring our own drinks, there's a bar on board, a bathroom, lights, our playlist. Real gators. 1 hr 45 min. It's {boat_price} for the whole boat, about {per_person} each. I'm putting $350 down to hold it and the rest is due the day we ride, so I need a yes or no from everybody this week. |
| birthday | Birthday plan, hear me out. Boat day in New Orleans with NOLA Party Barge. Private boat, just us, on the bayou 15 min from the Quarter. We bring our own drinks (there's a bar on board), our own playlist, there's a bathroom, and the captain does the driving. 1 hr 45 min, real gators. {boat_price} for the boat, about {per_person} each. $350 holds it, the rest is due the day we ride. Who's in? |
| friends | No reason, we just should. Boat day in New Orleans with NOLA Party Barge: private boat, just us, on the bayou 15 min from the Quarter. BYOB with a bar on board, our playlist, a bathroom, captain drives. 1 hr 45 min. {boat_price} for the boat, about {per_person} each. $350 holds it and the rest is due the day we ride. Yes or no, I'm booking this week. |
| family | Family boat day idea. NOLA Party Barge, a private boat for just our family (kids 6 and up are fine), on the bayou 15 min from the Quarter. Covered, heated if it's cold, bathroom on board. Captain drives, we bring the cooler. Gators, herons, cypress. 1 hr 45 min. {boat_price} for the boat, about {per_person} each. $350 holds it, the rest is due the day we ride. Who can make it? |
| work | Team outing idea: a private boat on the bayou with NOLA Party Barge, 15 min from the Quarter, 1 hr 45 min. Captain and crew included, BYOB with a bar on board, bathroom, covered and heated in winter, our own playlist. {boat_price} for the boat, about {per_person} a head. $350 holds it, the rest is due the day we ride. Reply with a date that works for you. |
| couple | Boat idea for New Orleans: NOLA Party Barge, on the bayou 15 min from the Quarter. We bring our own drinks, there's a bar on board, the captain drives, real gators, 1 hr 45 min. Seats are $59 each on a social cruise (21+), or if we want it to ourselves the Luxury Pontoon is $350 flat for up to 6 (no bathroom on that one). Which way? |
| 2-6 family | Family boat day idea. NOLA Party Barge, the Luxury Pontoon, private for up to 6 of us (kids 6 and up are fine), on the bayou 15 min from the Quarter. Captain drives, we bring the cooler. Gators, herons, cypress. 1 hr 45 min, $350 flat. No bathroom on that one, so plan accordingly. Who can make it? |
| default | No reason, we just should. Boat day in New Orleans with NOLA Party Barge: private boat, just us, on the bayou 15 min from the Quarter. BYOB with a bar on board, our playlist, a bathroom, captain drives. 1 hr 45 min. {boat_price} for the boat, about {per_person} each. $350 holds it and the rest is due the day we ride. Yes or no, I'm booking this week. |

### CREW-FAQ

SC-06. bach, bachelor, birthday and just_because render `party`.

| Version | Text |
|:-|:-|
| party | How far is it? About 7 miles from the French Quarter, a 15 minute ride. The dock is at 2101 Paris Road.<br>Do we all have to be 21? For seats on a social cruise, yes. On a private boat it's ages 6 and up, so the cousin who's 19 can come on that one.<br>Is there a bathroom? Yes, on every boat except the Luxury Pontoon.<br>What about drinks? BYOB. There's a bar on board to set them up. Bring the cooler.<br>What if it's cold or gray? The boats are covered and heated in winter. |
| family | How far is it? About 7 miles from the French Quarter, a 15 minute ride. The dock is at 2101 Paris Road.<br>Can the kids come? On a private boat, yes, ages 6 and up. The Swamp Eco Tour is family friendly too: 2 hours, from $50.<br>Is there a bathroom? Yes, on every boat except the Luxury Pontoon.<br>What about drinks? BYOB for the grown-ups, with a bar on board. Bring the juice boxes too.<br>What if it's cold or gray? The boats are covered and heated in winter. |
| work | How far from the hotel? About 7 miles from the French Quarter, a 15 minute ride. The dock is at 2101 Paris Road.<br>Does everyone need to be 21? It's your private boat, so you set the guest list. Ages 6 and up.<br>Is there a bathroom? Yes, on every boat except the Luxury Pontoon.<br>What about drinks? BYOB, with a bar on board to set them up. Expense the cooler.<br>What if it's cold or gray? The boats are covered and heated in winter. |
| couple | How far is it? About 7 miles from the French Quarter, a 15 minute ride. The dock is at 2101 Paris Road.<br>Do we have to be 21? For seats on a social cruise, yes. A private boat is ages 6 and up.<br>Is there a bathroom? Yes, on every boat except the Luxury Pontoon, which is the small private one for up to 6.<br>What about drinks? BYOB. There's a bar on board to set them up.<br>What if it's cold or gray? The boats are covered and heated in winter. |
| default | How far is it? About 7 miles from the French Quarter, a 15 minute ride. The dock is at 2101 Paris Road.<br>Do we all have to be 21? For seats on a social cruise, yes. On a private boat it's ages 6 and up, so the cousin who's 19 can come on that one.<br>Is there a bathroom? Yes, on every boat except the Luxury Pontoon.<br>What about drinks? BYOB. There's a bar on board to set them up. Bring the cooler.<br>What if it's cold or gray? The boats are covered and heated in winter. |

### HOME-LINE

SC-03, SC-04, SC-06, SC-16, SC-18. By `home`.

| Version | Text |
|:-|:-|
| local | The dock, if anyone asks: 2101 Paris Road, on Bayou Bienvenue. |
| drive | You're driving in. From a hotel near the French Quarter, the dock is about a 15 minute ride. |
| fly | You're flying in. Drop the bags near the French Quarter and the dock is about a 15 minute ride from there. |
| default | The dock is about a 15 minute ride from the French Quarter, at 2101 Paris Road. |

### HOME-DEAL

SC-10, SC-11, SC-13. The deadline line under the code. drive, fly and unanswered render `visitor`.

| Version | Text |
|:-|:-|
| local | A weeknight, this weekend, or something months out. Only the booking has to land by {code_end}. |
| visitor | Your trip doesn't have to happen before {code_end}. The booking does. |
| default | Your trip doesn't have to happen before {code_end}. The booking does. |

### MATH-SIZE

SC-05, SC-07 (price), SC-10, SC-10c, SC-11, SC-12a, SC-12b, SC-13. One of `locked` or `live` renders, then the closing line (2-6 has none). Lookup: guarded key, then plain key, then default with the guard, then default. Guards: family, seats, boat. All prices before whatever FareHarbor adds at checkout [VERIFY].

| Version | Text |
|:-|:-|
| 2-6 | locked: $59 a seat on a social cruise (21+). Want it to yourselves? The Luxury Pontoon is $350 private for up to 6, about $58 each if 6 of you come. No bathroom on that one, so plan accordingly.<br>live: $59 a seat on a social cruise (21+). Want it to yourselves? The Luxury Pontoon is $350 private for up to 6, about $58 each if 6 of you come. No bathroom on that one, so plan accordingly. |
| 2-6 family | locked: The Luxury Pontoon is $350 private for up to 6, about $58 each if 6 of you come. Ages 6 and up on a private boat. No bathroom on that one, so plan accordingly. If the kids would rather look than party, the Swamp Eco Tour is 2 hours, family friendly, from $50.<br>live: The Luxury Pontoon is $350 private for up to 6, about $58 each if 6 of you come. Ages 6 and up on a private boat. No bathroom on that one, so plan accordingly. If the kids would rather look than party, the Swamp Eco Tour is 2 hours, family friendly, from $50. |
| 7-12 | locked: Seats are $59 each on a social cruise (21+). Want it to yourselves? A private Bayou Boogie is $800 flat for up to 18, about $67 each if 12 of you come.<br>live: Seats are $59 each on a social cruise (21+). Want it to yourselves? With {code}, a private Bayou Boogie is $750 flat for up to 18, about $63 each if 12 of you come.<br>$350 holds the boat. The rest is due the day you ride. |
| 7-12 boat | locked: A private Bayou Boogie is $800 flat for up to 18, about $67 each if 12 of you come. If the group shrinks, seats are $59 each on a social cruise (21+).<br>live: With {code}, a private Bayou Boogie is $750 flat for up to 18, about $63 each if 12 of you come. If the group shrinks, seats are $59 each on a social cruise (21+).<br>$350 holds the boat. The rest is due the day you ride. |
| 7-12 family | locked: A private Bayou Boogie is $800 flat for up to 18, about $67 each if 12 of you come. Ages 6 and up on a private boat.<br>live: With {code}, a private Bayou Boogie is $750 flat for up to 18, about $63 each if 12 of you come. Ages 6 and up on a private boat.<br>$350 holds the boat. The rest is due the day you ride. |
| 13-18 | locked: The Bayou Boogie is $800 flat for up to 18, about $44 each if all 18 come. From 14 people up, a private boat beats $59 seats, and you get it to yourselves.<br>live: With {code}, the Bayou Boogie is $750 flat for up to 18, about $42 each if all 18 come. From 14 people up, a private boat beats $59 seats, and you get it to yourselves.<br>$350 holds the boat. The rest is due the day you ride. |
| 13-18 seats | locked: Seats are $59 each on a social cruise (21+). At your size, though, run the numbers: the Bayou Boogie is $800 flat for up to 18, about $44 each at 18. From 14 people up it beats seats, and you'd have the boat to yourselves.<br>live: Seats are $59 each on a social cruise (21+). At your size, though, run the numbers: with {code}, the Bayou Boogie is $750 flat for up to 18, about $42 each at 18. From 14 people up it beats seats, and you'd have the boat to yourselves.<br>$350 holds the boat. The rest is due the day you ride. |
| 13-18 family | locked: The Bayou Boogie is $800 flat for up to 18, about $44 each if all 18 come. Ages 6 and up on a private boat.<br>live: With {code}, the Bayou Boogie is $750 flat for up to 18, about $42 each if all 18 come. Ages 6 and up on a private boat.<br>$350 holds the boat. The rest is due the day you ride. |
| 19+ | locked: A tiki is $1,200 flat for up to 25: $48 each if you fill it. The Party Queen is $900 private for up to 26: about $35 each at 26. More than 26 is two boats, and a person from the crew helps you sort it.<br>live: With {code}, a tiki is $1,150 flat for up to 25: $46 each if you fill it. The Party Queen is $850 private for up to 26: about $33 each at 26. More than 26 is two boats, and a person from the crew helps you sort it.<br>$350 holds the boat. The rest is due the day you ride. |
| 19+ seats | locked: Seats are $59 each on a social cruise (21+). At 19 or more, though, a private boat costs about the same or less, and it's all yours: a tiki is $1,200 flat for up to 25 ($48 each if you fill it), the Party Queen is $900 private for up to 26 (about $35 each at 26). More than 26 is two boats, and a person from the crew helps you sort it.<br>live: Seats are $59 each on a social cruise (21+). At 19 or more, though, a private boat costs about the same or less, and it's all yours: with {code}, a tiki is $1,150 flat for up to 25 ($46 each if you fill it), the Party Queen is $850 private for up to 26 (about $33 each at 26). More than 26 is two boats, and a person from the crew helps you sort it.<br>$350 holds the boat. The rest is due the day you ride. |
| 19+ family | locked: A tiki is $1,200 flat for up to 25: $48 each if you fill it. The Party Queen is $900 private for up to 26: about $35 each at 26. Ages 6 and up on a private boat. More than 26 is two boats, and a person from the crew helps you sort it.<br>live: With {code}, a tiki is $1,150 flat for up to 25: $46 each if you fill it. The Party Queen is $850 private for up to 26: about $33 each at 26. Ages 6 and up on a private boat. More than 26 is two boats, and a person from the crew helps you sort it.<br>$350 holds the boat. The rest is due the day you ride. |
| default | locked: A tiki is $1,200 flat for up to 25. Fill it and it's $48 each.<br>live: With {code}, a tiki is $1,150 flat for up to 25. Fill it and it's $46 each.<br>$350 holds the boat. The rest is due the day you ride. |
| default seats | locked: $59 a seat on a social cruise (21+). Or a tiki at $1,200 flat for up to 25: fill it and it's $48 each.<br>live: $59 a seat on a social cruise (21+). Or, with {code}, a tiki at $1,150 flat for up to 25: fill it and it's $46 each.<br>$350 holds the boat. The rest is due the day you ride. |
| default family | locked: A tiki is $1,200 flat for up to 25. Fill it and it's $48 each. Ages 6 and up on a private boat.<br>live: With {code}, a tiki is $1,150 flat for up to 25. Fill it and it's $46 each. Ages 6 and up on a private boat.<br>$350 holds the boat. The rest is due the day you ride. |

### WHEN-PS

SC-04 and SC-05 (plain keys), SC-17 (`trip` keys). By `ride_when`. none and unanswered render the default, which is blank.

| Version | Text |
|:-|:-|
| soon | Riding in the next 30 days? A lot of our bookings come in the same week people ride, so if you've got a day in mind, check it early. The group chat will take a week to vote anyway. |
| holiday | Holiday trip? The boats are covered and heated in winter. A December boat day is a plan, not a dare. |
| mardigras | Mardi Gras Day is Tue Feb 9, 2027. A boat day between parades gets your crew off the route and onto the water for an afternoon. |
| later | Spring or summer 2027 is a ways out. The booking doesn't have to be: pick a date now, ride when it's warm. |
| soon trip | Next 30 days means the Countdown runs fast: only the chapters that still fit, one a day at most. |
| holiday trip | Holiday trip: the eating chapter and the what-to-wear chapter move to the front. |
| mardigras trip | Mardi Gras season: the parade chapter goes to the front of the line. Mardi Gras Day is Tue Feb 9, 2027. |
| later trip | Spring or summer: you get the slow version, about one chapter a week, until the countdown kicks in closer to your dates. |
| default | (renders nothing) |

### DOUBT-ANSWER

SC-07. By `blocker`. price embeds MATH-SIZE, commit embeds CREW-SHARE, default ends in PROOF; the email drops its own copy of that slot when the matching version fires.

| Version | Text |
|:-|:-|
| price | Price is a fair one, so here's the math. A private boat is one flat price, split as many ways as you bring. BYOB, so the bar bill is whatever you carry on.<br>{{MATH-SIZE}} |
| weather | Fair. The boats are covered, and heated in winter, so a gray day is still a boat day. |
| commit | Getting everyone to commit is the real one for most crews. The fix is a date and a number, so nobody's sending money to a group pot months early. Paste this in the chat (same one as last time, it still works) and let it do the work:<br>{{CREW-SHARE}} |
| far | Not far. The dock is at 2101 Paris Road, on Bayou Bienvenue, about 7 miles from the French Quarter. That's a 15 minute ride. Out there it looks like you drove an hour: gators, herons, cypress, the storm surge barrier. You didn't. |
| none | Nothing stopping you? Then the only thing left is a date. Pick one, check it's open, and the rest sorts itself out. |
| default | You never told us what might stop your crew, so here's what guests say after the ride:<br>{{PROOF}} |

### PROOF

SC-07 (when blocker is unanswered) and SC-11. `winner` only once the signed form is in.

| Version | Text |
|:-|:-|
| reviews | What usually decides it is what other guests say after the ride: 4.9 stars across 3,800+ reviews. |
| winner | The last drawing has a winner. [VERIFY: winner first name, last initial, city, and state, only after the signed form] is taking a private tiki boat out with up to 24 guests and paying nothing for it. That's the drawing you're in. |
| default | What usually decides it is what other guests say after the ride: 4.9 stars across 3,800+ reviews. |

### CODE-PS

The P.S. of SC-02 to SC-07, SC-10b, SC-11 to SC-14, SC-16. A box in the body of SC-10. By `code_state`.

| Version | Text |
|:-|:-|
| locked | (renders nothing) |
| live | {code} takes $50 off a private boat (the Bayou Boogie, the Party Queen, or a tiki). Book by {code_end} at 11:59pm Central, ride any open date. |
| last_days | Days left on {code}: {days_left}. It ends {code_end} at 11:59pm Central. $50 off a private boat, book by then and ride any open date. |
| booked | See you on the bayou. |
| default | (renders nothing) |

### WIN-OPEN

SC-09 only. The opener; the claim steps never change.

| Version | Text |
|:-|:-|
| first | {first_name}, your name came up. You're the potential winner of the {round} drawing: a free private tiki boat ride for you and up to 24 guests. Potential, because the Official Rules have us check two things first. Both are quick. |
| reminder | {first_name}, second notice. Your name came up in the {round} drawing two days ago and we haven't heard back. You're the potential winner of a free private tiki boat ride for you and up to 24 guests until {reply_deadline}. After that the Official Rules move the prize to the next name. |
| alternate | {first_name}, the first name we drew in the {round} drawing didn't claim the prize under the Official Rules, so it moves to the next name drawn. That's you. You're now the potential winner of a free private tiki boat ride for you and up to 24 guests. |
| default | {first_name}, your name came up. You're the potential winner of the {round} drawing: a free private tiki boat ride for you and up to 24 guests. Potential, because the Official Rules have us check two things first. Both are quick. |

### FOOTER

Every email. `unconfirmed` on SC-01 and SC-01b, `default` everywhere else.

| Version | Text |
|:-|:-|
| unconfirmed | You took the NOLA Party Barge survey for the free boat drawing on {entry_date}. Official Rules: {rules_url}<br>Unsubscribe with one click: {unsub_url}<br>We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.<br>NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. 1 (504) 264-1056 |
| default | You took the NOLA Party Barge survey for the free boat drawing on {entry_date}. Official Rules: {rules_url}<br>Unsubscribe with one click: {unsub_url}<br>Unsubscribing doesn't remove your entry.<br>We only contact the winner by email from info@nolapartybarges.com. We'll never ask for a card number.<br>NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129. 1 (504) 264-1056 |

## Part 4. Ask bank, answer pages, and small pages

How a tap works: every tap opens a small page headed Got it, then one count line, then the text for the value they tapped, then the next unanswered bonus question as buttons. The count line reads That's {entries} of 5. when the tap earned an entry; at the cap it reads That's 5 of 5, the most anyone gets. We draw {draw_date}. and no further question shows. Routing taps (reentry, stay, holdup, locals_topic, crew_going) earn nothing and show no count line. Taps on the result page before the confirm tap show Saved. Tap the email to make it count. Bonus order: planner, vibe, buy_mode, intent, blocker, trip_month. Family crews skip buy_mode everywhere.

Guards on an answer page line (for example `price[group_type=family]`) are tried in the order written, first match wins, then the plain line. A line that still carries [VERIFY] fails the render test; until the fact lands it renders up to the bracket.

| Ask | Question | Asked in | Earns an entry |
|:-|:-|:-|:-|
| planner | Who plans things in your group? | SC-02, result page | Yes, one of the first 4 |
| vibe | Full send or chill? | SC-03, result page | Yes, one of the first 4 |
| buy_mode | Seats or the whole boat? | SC-04 (never for family crews) | Yes, one of the first 4 |
| intent | If you don't win, would you still do this? | SC-05 | Yes, one of the first 4 |
| blocker | What would stop your crew? | SC-06 | Yes, one of the first 4 |
| trip_month | Got dates yet? | SC-17, and any open slot | Yes, one of the first 4 |
| reentry | Put me in the {next_round} drawing | SC-10, SC-10b, SC-10c | No, routing |
| stay | Still want these? | SC-15 | No, routing |
| holdup | What's the hold-up? | SC-14 | No, routing |
| locals_topic | What do you want to hear about? | SC-18 | No, routing |
| crew_going | Is this crew actually going? | Dormant in round 1 (was the connector question for the cut friend-link email) | No, routing |

### Ask: planner

**Question:** Who plans things in your group?

**Buttons:** I do / The group chat does / Somebody else

Values: me, chat, other

| Tapped | Answer page says |
|:-|:-|
| me | You're the planner. $350 holds a private boat, so nobody has to front the whole thing. |
| chat | The group chat decides. So give it numbers: a private boat is one flat price for everybody, and $350 holds the date. |
| other | Somebody else plans it. Send them a date. $350 holds a private boat. |

### Ask: vibe

**Question:** Full send or chill?

**Buttons:** Full send / Chill / A little of both

Values: full, chill, both

| Tapped | Answer page says |
|:-|:-|
| full | Full send. Every boat has a Bluetooth sound system and party lights. Bring the playlist and the cooler. It's BYOB, with a bar on board to set your drinks up. |
| chill | Chill. 1 hr 45 min on Bayou Bienvenue with gators, herons, and cypress. Covered, and heated in winter. |
| both | A little of both. Gators on the way out, playlist on the way back. Same boat, same 1 hr 45 min. |

### Ask: buy_mode

**Question:** Seats or the whole boat?

**Buttons:** A few seats / The whole boat / Not sure yet

Values: seats, boat, unsure

| Tapped | Answer page says |
|:-|:-|
| seats | A few seats. $59 a seat on a social cruise, 21 and up. Bathroom on board, BYOB, and you meet the rest of the boat out there. |
| boat[group_size=2-6] | The whole boat. For a crew your size that's the Luxury Pontoon: $350 private for up to 6, no bathroom on that one. $350 is the whole price, so nothing's due on the day. |
| boat | The whole boat. Private boats run from $350 for up to 6 on the Luxury Pontoon (no bathroom on that one) to $1,200 for up to 25 on a tiki. $350 holds the date, the rest is due the day you ride. |
| unsure | Not sure yet. Rough rule: under 14 people, seats at $59 each. From 14 up, a private boat costs less per person. |

### Ask: intent

**Question:** If you don't win, would you still do this?

**Buttons:** Planning one / Maybe / Only if it's free

Values: plan, maybe, free

| Tapped | Answer page says |
|:-|:-|
| plan | Planning one. Then the drawing is just a bonus. Open dates are on nolapartybarges.com. |
| maybe | Maybe. No rush. The boats run all year, covered and heated in winter. The drawing closes {close_date}. |
| free | Only if it's free. Fair enough. You're in the drawing. The sales emails stay out of your inbox until the draw. The countdown and the result still come. |

### Ask: blocker

**Question:** What would stop your crew?

**Buttons:** Price / Weather / Getting everyone to commit / Don't know that part of town / Nothing, we're in

Values: price, weather, commit, far, none

| Tapped | Answer page says |
|:-|:-|
| price[group_type=family] | Price. A private boat is one flat price for everybody, ages 6 and up: $800 for up to 18 on the Bayou Boogie, $1,200 for up to 25 on a tiki. $350 holds the date, the rest is due the day you ride. |
| price[group_size=2-6] | Price. Seats are $59 each on a social cruise (21+). Want it to yourselves? The Luxury Pontoon is $350 private for up to 6. No bathroom on that one. |
| price | Price. Private boats are one flat price for everybody: the Bayou Boogie is $800 for up to 18, a tiki is $1,200 for up to 25, which is $48 each when it's full. $350 holds the date, the rest is due the day you ride. |
| weather | Weather. Every boat is covered, and heated in winter. [VERIFY: rain and cancellation policy from the manager. Until it lands, this page ends at the first sentence.] |
| commit | Getting everyone to commit. $350 holds the date. Nobody else pays a thing until the day you ride. Paste that in the chat. |
| far | Don't know that part of town. The dock is 2101 Paris Road, about 7 miles and a 15 minute ride from the French Quarter. |
| none | Nothing's stopping you. Then pick a date. Open dates are on nolapartybarges.com. |

### Ask: trip_month

**Question:** Got dates yet?
- When home=local: What's next on your calendar?

**Buttons:** November / December / January / February / March / April / Not yet

Values: 2026-11, 2026-12, 2027-01, 2027-02, 2027-03, 2027-04, none

| Tapped | Answer page says |
|:-|:-|
| 2026-11 | November. Thanksgiving is Thu Nov 26. The boats are covered and heated, so a cold front doesn't change the plan. |
| 2026-12 | December. A private boat holds a holiday party of up to 26. Covered, heated, BYOB. |
| 2027-01 | January. Krewe du Vieux rolls Sat Jan 23, the early-season pick and the only krewe that goes through the Quarter. A boat day fits between parades. |
| 2027-02 | February. Mardi Gras Day is Tue Feb 9, 2027. A boat day between parades gets the crew off the route for an afternoon. |
| 2027-03 | March. Spring on the bayou. Open dates are on nolapartybarges.com, and $350 holds a private boat. |
| 2027-04 | April. Plenty of time to get the crew to commit. $350 holds the date. |
| 2027-05 | May. Long evenings on the water. $350 holds a private boat. |
| 2027-06 | June. Summer on the bayou. Every boat is covered, so the shade comes with it. |
| none | Nothing yet. No problem. We'll ask again later. |

### Ask: reentry

**Question:** Put me in the {next_round} drawing

**Buttons:** Put me in the {next_round} drawing

Values: yes

| Tapped | Answer page says |
|:-|:-|
| yes | You're in the {next_round} drawing with 1 entry. Nothing else to do. One email before the draw, one on draw day. Official Rules: {rules_url} |

### Ask: stay

**Question:** Still want these?

**Buttons:** Keep them coming / Just the drawing / Take me off

Values: keep, drawing, off

| Tapped | Answer page says |
|:-|:-|
| keep | Keep them coming. The tips keep coming, and you're still in the drawing. |
| drawing | Just the drawing. One email before the draw and one on draw day. Nothing else. |
| off | You're off the list. Your entry stays in the drawing. If you win, the only email comes from info@nolapartybarges.com. |

### Ask: holdup

**Question:** What's the hold-up?

**Buttons:** Price / The date / Getting the group to commit / Just looking

Values: price, date, commit, looking

| Tapped | Answer page says |
|:-|:-|
| price | Price. {code} takes $50 off a private boat through {code_end}. $350 holds it, the rest is due the day you ride. |
| date | The date. Open dates are on nolapartybarges.com. Book by {code_end}, ride any open date. |
| commit | Getting the group to commit. $350 holds the date and nobody else pays until the day you ride. Paste that in the chat. |
| looking | Just looking. All good. {code} is good through {code_end} if that changes. |

### Ask: locals_topic

**Question:** What do you want to hear about?

**Buttons:** Weeknight openings / Holiday boats / Just the drawing

Values: weeknight, holiday, drawing

| Tapped | Answer page says |
|:-|:-|
| weeknight[group_type=family] | Weeknight openings. When a private boat has an open weeknight, you hear first. Two emails a month at most. |
| weeknight | Weeknight openings. When a boat has open seats or a private slot on a weeknight, you hear first. Two emails a month at most. |
| holiday | Holiday boats. You hear first when holiday dates open. Two emails a month at most. Covered, heated, BYOB. |
| drawing | Just the drawing. One email before each draw, one on draw day. That's it. |

### Ask: crew_going

**Question:** Is this crew actually going?

**Buttons:** Yes, help me pick a date / Not yet

Values: yes, notyet

| Tapped | Answer page says |
|:-|:-|
| yes | Yes. Open dates are on nolapartybarges.com. Pick two or three that work, and $350 holds the one the chat agrees on. |
| notyet | Not yet. No rush. The drawing doesn't care either way. |

### Page: Confirm

The page behind the Confirm my entry button in SC-01 and SC-01b. One rendered view is the headline, the line, the button, one of the four state lines, then the footer. The state lines never show together. Under the after line, the next unanswered bonus question shows as buttons (nothing at 5 of 5, nothing on the closed state).

| Element | Text |
|:-|:-|
| Headline | One tap and you're in. |
| Line | This locks in your entry in the NOLA Party Barge {round} drawing: a free private tiki boat for you and up to 24 guests. We draw {draw_date}. |
| Button | Confirm my entry |
| After the tap | You're in with {entries} of 5 entries. Every bonus question from here is one tap and one entry, until you hit 5. |
| After the tap, at 5 of 5 | You're in with 5 of 5 entries, the most anyone gets. We draw {draw_date}. |
| Already confirmed | You're already in with {entries} of 5 entries. Nothing else to do. We draw {draw_date}. |
| Round closed | Entries for the {round} drawing closed {close_date} at 11:59pm Central, so this tap came too late to count for it. The next drawing is its own round, and the survey page has it when it opens. |
| Footer | Official Rules: {rules_url} |

### Page: Result (your New Orleans type)

Shown right after the survey form. Headline on every version: Your New Orleans type: {type}. Then the two type lines, the boat line (family guard where the plain line names a 21+ seat), then the shared tail. This page is the master copy; doc 04 points here.

| like | Type | Type lines | Boat line | Boat line for family crews |
|:-|:-|:-|:-|:-|
| food | The Po'boy Scholar | You order it dressed, no questions. Friends ask you before picking a restaurant. | Your boat: the Sunset Cocktail Cruise and Seafood Boil. From $165, first drink included. | Your own boat, ages 6 and up. Po'boys before, bayou after. |
| music | The Frenchmen Regular | You've stood outside a packed club because the horns carried. Second set's your set. | Bluetooth sound system and party lights on every boat. Bring the playlist. | same |
| night | The Go-Cup Champion | The night doesn't end when the bar does. You rate the walk between bars. | BYOB, with a bar on board for your drinks. The captain drives. | same |
| wild | The Gator Spotter | You pull over for herons. You show gator photos to people who didn't ask. | Gators, herons, cypress, storm surge barrier. Swamp Eco Tour from $50, family friendly. | same |
| parade | The Parade Chaser | You know the corner, the route, and which float throws the good stuff. Feb 9, 2027 is circled. | A boat day between parades. Covered, heated in winter. | same |
| people | The Porch Sitter | Never met a stranger, just people you haven't talked to yet. Last one off the porch, every time. | $59 a seat on a social cruise (21+). Or your own boat. | Your own boat, ages 6 and up. Just your family aboard. |

Shared tail, all six types:

| Element | Text |
|:-|:-|
| Lock line | Tap the email from info@nolapartybarges.com to lock in your entry. Nothing in 10 minutes? Check spam. |
| Lock line, over the daily cap | Your confirm email comes tomorrow at 9am. Tap it to lock in your entry. (never shown on the last 2 days of a round; the cap is lifted then) |
| Bonus line | Two taps now, two more entries after you confirm. |
| Question 1 | Who plans things in your group? (planner buttons) |
| Question 2 | Full send or chill? (vibe buttons) |
| Tap feedback | Saved. Tap the email to make it count. |
| Footer | Official Rules: {rules_url}. Privacy: the privacy page, same link as the survey page footer. No UTMs on either. |

No share button, no referral link, no tag-a-friend anywhere on the page.

### Page: Survey thanks

| Element | Text |
|:-|:-|
| Headline | Thanks, {first_name}. Check your email. |
| Body | It's from info@nolapartybarges.com. One tap in it locks in your entry. Not there in 10 minutes? Check spam. |
| Button | See my New Orleans type |
| Over the daily cap | Your confirm email comes tomorrow at 9am. One tap in it locks in your entry. (never shown on the last 2 days of a round) |

### Page: Got it (the tap interstitial)

Every tap button in an email lands here. Headline Got it, then the count line (rules at the top of Part 4), then the answer text from the ask tables above, then the next unanswered bonus question as buttons. A month tap from SC-17 gets its answer page with no count line; for visitors, once the Countdown is live, the month page ends with Your NOLA Countdown starts from here.

### Page: Bad link

| Element | Text |
|:-|:-|
| Headline | That link didn't work. |
| Body | It may have expired or got cut off in a forward. Open the newest email from info@nolapartybarges.com and tap again. Your entry isn't affected. |
| Unsubscribe box | Trying to unsubscribe? Type your email and we'll take you off. Your entry stays in. |
| Button | Unsubscribe me |

### Page: Unsubscribe confirm

| Element | Text |
|:-|:-|
| Headline | Take you off the list? |
| Body | One tap stops every email from NOLA Party Barge. Your drawing entry stays in. If you win, you'll get one email from info@nolapartybarges.com and nothing else. |
| Button | Unsubscribe me |
| Secondary | Keep me on |

### Page: Unsubscribed

| Element | Text |
|:-|:-|
| Headline | You're off the list. |
| Body | No more emails from NOLA Party Barge. Your entry stays in the drawing. We only contact the winner by email from info@nolapartybarges.com, and we never ask for a card number. |
| Button | Back to nolapartybarges.com |

### Manager alerts (internal, to info@nolapartybarges.com)

A guest never sees these. Angle-bracket fields are engine fields. The manager replies as a person from info@nolapartybarges.com.

| Alert | Fires | Subject | Body |
|:-|:-|:-|:-|
| Hot lead | At the second boat or pricing click | Hot lead: {first_name}, <group_type> crew of {group_size}, riding <ride_when> | {first_name} <email> clicked a boat link twice (<click_1>, <click_2>). Loves {like_label}. Home: <home>. Seats or boat: <buy_mode>. Doubt: <blocker>. {code} goes out at 9am tomorrow in the hot unlock email. Reply from info@ as a person today. |
| Work crew | At the confirm tap | Work crew entered: {first_name}, {group_size} people, riding <ride_when> | {first_name} <email> confirmed as a work crew, {group_size} people, home <home>, riding <ride_when>. Send the holiday party one-pager from info@ and offer two open dates. |
| Whole-boat lead | At the first boat click when planner = me, group_size 13-18 or 19+, intent = plan | Whole-boat lead: {first_name}, <group_type>, {group_size}, planning one | {first_name} <email> is the planner, {group_size} people, said Planning one, and just clicked a boat link. Home <home>, riding <ride_when>. Reply from info@ with two open dates and the deposit line. |

## Part 5. VERIFY list

Every open fact in the copy, the pages, and the Blueprint, in one table. A [VERIFY] inside a rendered line fails the render test, so nothing ships until its row is closed. Who can close it is the person, not a doc.

| # | Open fact | Where it bites | Who can close it |
|:-|:-|:-|:-|
| V1 | Rain and cancellation policy: what happens if the captain calls off a trip, and whether guests can move the date or get a refund | DOUBT-ANSWER weather (SC-07), ASK blocker weather answer page | The manager (JT) |
| V2 | Two outdoor picks from the crew, with a few words on each, for the gator version of the local picks | LIKE-PICKS wild (SC-03) ends on a placeholder line until they land | The crew |
| V3 | One real guest review, one or two lines, first name and where it was posted | PROOF reviews and default (SC-07, SC-11) | The crew, from TripAdvisor, Yelp, or Batch |
| V4 | Winner first name, last initial, city, and state, only after the signed form | PROOF winner (SC-11 the Monday after each draw, SC-07 from round 2) | The manager, after each draw |
| V5 | What FareHarbor adds at checkout (tax, fees). If anything, every MATH-SIZE line needs plus tax and fees | MATH-SIZE, CREW-SHARE, the price answer pages | David, in FareHarbor |
| V6 | Prize days: which days are off-peak in FareHarbor. SC-09 says rides run Sunday through Thursday | SC-09, Official Rules (decision 2) | David |
| V7 | Whether the written prize confirmation within 10 days (open days, blackout dates, ride-by date, how to book) is the right claim shape | SC-09 step 3 (counsel question 3) | Lawyer |
| V8 | Whether posting the winner's first name, last initial, city, and state is part of the signed release or needs a separate yes | SC-09 P.S. (decision 10, counsel question 3) | Lawyer, then David |
| V9 | An unsubscribed entrant whose name comes up: can they get SC-09 once and nothing else | SC-09 audience, suppression rule 1, FOOTER (Unsubscribing doesn't remove your entry) | Lawyer |
| V10 | Official Rules: state registration at a $1,200 prize, the Meta release wording, the age and residency checks | Every FOOTER ({rules_url}), SC-01, SC-09 | Lawyer, before Mon Oct 19 (the go or no-go item) |
| V11 | Prize tax paperwork for a $1,200 prize | SC-09 claim steps | CPA |
| V12 | What the locals list sends: first dibs on open boats, 2 emails a month at most, no new discount | SC-18, ASK locals_topic (decision 12) | David |
| V13 | Who signs as {signer}: a real crew member's first name with their OK, or the default | Every email (decision 9) | David |
| V14 | The exact survey option label strings, lowercase, for {like_label} (the food, the music, going out, the bayou and the gators, parades and festivals, the people) | SC-03 subject, manager hot lead alert | The builder, against doc 04 |
| V15 | Ages on the Luxury Pontoon and the Swamp Eco Tour. Copy uses the facts file rule (private boats 6 and up, Eco Tour family friendly) and never states a pontoon-specific age | CREW-SCENE 2-6 family, MATH-SIZE 2-6 family, LIKE-BOAT wild, CREW-FAQ family | The manager |
| V16 | BAYOU50-NOV in FareHarbor: private boats only, pontoon excluded, $50 off the total and not the deposit, tested with a deposit booking | CODE-PS, MATH-SIZE live lines, SC-10 to SC-13 | David, in FareHarbor |
| V17 | Every local spot re-checked as open the week before each send | LIKE-PICKS (SC-03), trip_month answer pages | Whoever ships the copy |
| V18 | DNS for go.nolapartybarges.com, which sets {rules_url}, the confirm page, and the result page addresses | Every FOOTER, SC-01, SC-01b | David, or FareHarbor if the zone is in their Cloudflare |
| V19 | The public random seed: NIST Randomness Beacon still publishes, else drand | SC-08a line about a public random number | The builder |
| V20 | Whether the FareHarbor webhook that already feeds the review texts on mbp-2 can post to /booked, so SC-16 and the booked SC-10b fire without a manual post | SC-16, SC-10b, selling stop | The builder |
| V21 | Whether Nolan (OpenCX) can send the survey link on a DM keyword | Survey entry, no email copy | The builder, in OpenCX |
| V22 | How the winner's free boat gets booked in FareHarbor | SC-09 step 3 | The manager |
| V23 | Which sender and domain the weekly reel uses after Nov 17, and one shared unsubscribe list before any survey lead is added to it | Hand-off after SC-10 | Engine build |
| V24 | The Countdown's live date. If it slips, visitors wait as countdown_pending after SC-17 | SC-17, trip_month answer pages | Engine build |

Doc conflicts to settle (not facts, but the copy and the Blueprint disagree):

| # | Conflict | Where | Call needed from |
|:-|:-|:-|:-|
| C1 | Entry cap and referrals. Blueprint sections 4, 7 and 8 say 10 entries with +2 per friend link. The rules draft and all four copy files say 5 entries, no referral entries, and STATS-LINE, CREW-SHARE and SC-02 were rewritten to match. Blueprint needs the update, not the copy | Blueprint vs rules draft | David |
| C2 | Claim window. Blueprint says 72 hours with a reminder at 48 (Thu Nov 19, 1pm). SC-09 uses {reply_deadline} and says each alternate gets their own 5 days, with 7 days for the e-sign form and 10 for the written confirmation. The calendar row for Meet the winner (Mon Nov 23) only works on the 72 hour clock | SC-09, Blueprint section 4 calendar, Official Rules | David with the lawyer |
| C3 | SC-13 for people riding in the next 30 days. Blueprint section 9 sends Marcus SC-13 on Oct 29. The reviewed SC-13 audience skips anyone whose code is already live (ride_when = soon goes live at confirm) and fires the manager alert only. Either the rule or the worked example changes | SC-13 audience, Blueprint section 9 | David |
| C4 | SC-14. Blueprint calls it A friend got in. With referral entries cut, the copy made SC-14 the hold-up email for hot leads 5 days after SC-13 (the Blueprint had it under Later). Needs build either way | SC-14, Blueprint sections 7 and 11 | David |
| C5 | SC-11 name. Blueprint calls it Meet the winner. The copy renamed it One week left on the code because PROOF can only show the winner once the signed form is in, so the fixed text never promises a name | SC-11 | None, just so you know |

Needs build before any of this sends (copy depends on it): whole-field variants by guard (subject[like=food], body[entries=5]), suppress SC-01b after the close, SC-01 for the next round when a submit lands between rounds, hold code_state at locked for crews of 2 to 6, the forfeited-winner version of SC-10, SC-14 and SC-17 as steps, locals_topic = drawing sets quiet, the hot flag and manager alerts, the draw script, the claim reply handling with Reply-To on info@nolapartybarges.com.

