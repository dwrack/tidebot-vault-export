# The Crew's Guide to New Orleans: Copy

*Draft 2026-10-13. Internal name: the NOLA Countdown. Spec: [[NPB Lead Capture + Drip Plan (Oct 2026)]] section 4. Status: for David to read and approve. Nothing here is sent, published, or deployed. The machine version of every line lives in `~/Projects/npb-lead-funnels/work/guide/npb_guide.json`, generated from the same source, so edit one and ask for the other to be regenerated.*

## How to read this

1. Emails are in send order: 1, 1b, 2 through 12, then the no-date track, then the crew reward emails.
2. Each email shows subject, preview, and the default body as it renders.
3. Under it, "variants" list only the lines that change for that occasion or month.
4. `{curly}` slots fill at send time. `{per_person}` and `{boat_name}` come from group size (6-18 Bayou Boogie, 19-22 Party Queen, 23-25 a Tiki).
5. `[NEW POST: title]` is a blog post we still have to write. The link goes live when the post does.
6. `[VERIFY]` is a fact the crew has to confirm. A line with [VERIFY] in it should fail the render test, so nothing ships until it's closed.
7. Crew's Pick links go to a Google Maps search for the spot. Swap for the Crew's Map pin once the map exists.
8. P.S. lines show only while a $50 code is live. Early planners (45+ days out) don't see one until 45 days before the trip.
9. If they book, the P.S. drops and the boat line switches to the "booked" version shown under each email.
10. Signer is "the crew at NOLA Party Barge" until a crew member says yes to having their first name on it.

**The one rule every email follows**

| Block | Rule |
|:-|:-|
| Countdown | First line. "{days_to_trip} days till New Orleans." Month track: "{trip_month_name} in New Orleans. Getting closer." |
| Chapter | 3-5 short lines, local and specific, then "read the full chapter" |
| Crew's Pick | One spot and why, in one line |
| The boat | One line, never the main event (email 5 is the one exception, by design) |
| P.S. | The code and its end date, only while it's live |
| Question | One max, always the last thing before the sign-off |

## The 13 emails

### G01. You're going to New Orleans.

**When:** `{"after_hours": 0}`  |  **Subject:** You're going to New Orleans.  
**Preview:** Three quick taps and these emails get a lot more useful.

> *{days_to_trip} days till New Orleans.*
> 
> Hey {first_name},
> 
> You're in. This is The Crew's Guide to New Orleans: short emails timed to your trip, from the people who run boats on the bayou 7 miles from the Quarter.
> 
> Where to eat, where to go out, what to wear, and how not to lose an afternoon in a van. Stuff we'd text a friend.
> 
> Help us make it about your trip. Three taps, no typing.
> 
> **Who's coming?**
> [Bachelorette] [Bachelor] [Birthday] [Girls' trip] [Guys' trip] [Couples] [Family] [Cousins] [Work crew] [Just because]
> 
> **How many of you?**
> [2-5] [6-12] [13-20] [21+]
> 
> **First time in New Orleans?**
> [First time] [Been before] [I basically live here]
> 
> That's it. Tomorrow: a message you can paste straight into the group chat.
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**If trip_when is month, year, or exploring:** the third question becomes **When are you thinking?** [This spring] [This summer] [This fall] [Next year] [No clue yet], and 'First time?' moves to email 2.


### G01B. Paste this in the group chat

**When:** `{"after_days": 1}`  |  **Subject:** Paste this in the group chat  
**Preview:** The per-person number, the boat, and one link. Copy, paste, done.

> *{days_to_trip} days till New Orleans.*
> 
> Every trip has one person doing the real work. If that's you, here's the message we'd send. We did the math for {n} of you.
> 
> Copy from here:
> 
> New Orleans, {trip_month_name}. I found a private boat on the bayou 7 miles from the Quarter. Just us, our music, our own drinks, real gators. The {boat_name} for {n} of us is {per_person} each. Tap in if you're in: {share_url}
> 
> Every friend who taps in counts toward stuff for the crew, and the first unlock is at 6.
> 
> Read the full chapter: [NEW POST: First-Timer's 48 Hours in New Orleans]
> 
> **Crew's Pick:** Cafe Beignet in the Quarter. Shorter line than the famous one, and they pour beer and wine with the beignets.
> 
> The boat in that message is real: {boat_name}, private, BYOB, bathroom on board.
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**If they booked, the boat line becomes:** You already booked, so paste it anyway. It's the easiest way to get everyone's share back.

**Occasion variants (only the lines that change):**

- **bachelorette:** Copy from here: /  / Bride squad: New Orleans, {trip_month_name}. I found our boat. Private, on the bayou 15 min from the Quarter, our playlist, bring our own drinks, gators for the photos. The {boat_name} for {n} of us is {per_person} each. Tap if you're in: {share_url} /  / Every friend who taps in counts toward perks for the bride's crew. First one unlocks at 6. | Link: A local's itinerary for a New Orleans bachelorette (https://nolapartybarges.com/a-locals-itinerary-for-a-new-orleans-bachelorette-party/)
- **bachelor:** Copy from here: /  / Boys. New Orleans, {trip_month_name}. Private boat on the bayou, 15 min from the Quarter, our music, our own cooler, actual alligators. {boat_name} for {n} of us comes to {per_person} each. Tap in so I can lock it: {share_url} /  / Every guy who taps in counts toward perks for the crew. First one unlocks at 6. | Link: The bachelor party boat, on the bayou (https://nolapartybarges.com/bachelor-party-booze-cruise-new-orleans-bayou/)
- **birthday:** Copy from here: /  / Birthday plan for {trip_month_name}: a private boat on the bayou in New Orleans, 15 min from the Quarter. Our music, our own drinks, gators as guests. The {boat_name} for {n} of us is {per_person} each. Tap if you're coming: {share_url} /  / Every friend who taps in counts toward perks for the birthday crew, starting at 6. | Link: Milestone birthdays on a private boat (https://nolapartybarges.com/milestone-birthday-private-party-boat-new-orleans/)
- **girls_trip:** Copy from here: /  / Girls' trip, New Orleans, {trip_month_name}. I found a private boat on the bayou, 15 min from the Quarter. Our playlist, our drinks, sunset photos. The {boat_name} for {n} of us is {per_person} each. Tap in: {share_url} /  / Every friend who taps in counts toward perks for the group. First unlock is at 6. | Link: The girls' weekend, done right (https://nolapartybarges.com/girls-weekend-party-boat-new-orleans/)
- **guys_trip:** Copy from here: /  / New Orleans, {trip_month_name}. Private boat on the bayou, 15 min from the Quarter, bring our own cooler, see some gators. The {boat_name} for {n} of us is {per_person} each. Tap in if you're in: {share_url} /  / Every friend who taps in counts toward perks for the group. First unlock is at 6.
- **couples:** Copy from here: /  / Couples trip, New Orleans, {trip_month_name}. A private boat on the bayou just for us, 15 min from the Quarter, our own drinks, sunset if we want it. {boat_name} for {n} of us is {per_person} each. Tap in: {share_url} /  / Every couple that taps in counts toward perks for the whole group, starting at 6.
- **family:** Copy from here: /  / Family trip idea for {trip_month_name}: a private boat on the bayou in New Orleans, 15 min from the Quarter. Gators, egrets, a bathroom on board, ages 6 and up. The {boat_name} for {n} of us is {per_person} each. Tap if you're in: {share_url} /  / Every relative who taps in counts toward perks for the family, starting at 6.
- **cousins:** Copy from here: /  / Cousin trip, New Orleans, {trip_month_name}! I found our boat: private, on the bayou 15 min from the Quarter, our music, our cooler, gators for the shirt photo. {boat_name} for {n} of us is {per_person} each. Tap in: {share_url} /  / Every cousin who taps in counts toward perks for the crew. First unlock is at 6. | Link: [NEW POST: Cousin Trips in New Orleans (the /cousin-trips page)]
- **work:** Copy from here: /  / Team outing, New Orleans, {trip_month_name}: a private boat on the bayou, 15 min from downtown. Our own music and drinks, bathroom on board, back for dinner. The {boat_name} for {n} of us is {per_person} each. Tap in: {share_url} /  / Every coworker who taps in counts toward perks for the team, starting at 6.
- **just_because:** Copy from here: /  / No occasion needed. New Orleans, {trip_month_name}, a private boat on the bayou 15 min from the Quarter, our music, our own drinks, real gators. The {boat_name} for {n} of us is {per_person} each. Tap in: {share_url} /  / Every friend who taps in counts toward perks for the crew. First unlock is at 6.


### G02. How many days is enough? (and what it costs)

**When:** `{"after_days": 2}`  |  **Subject:** How many days is enough? (and what it costs)  
**Preview:** Three nights is the sweet spot. Here's why, and where the money goes.

> *{days_to_trip} days till New Orleans.*
> 
> {first_name}, the two questions every group chat asks first.
> 
> Two nights feels like a highlight reel. Four and your feet file a complaint.
> Three nights is the sweet spot for most crews: one big night, one long brunch, one day you'd actually tell your mom about.
> The money goes to rooms and dinners. Po'boys for lunch and the streetcar where it works save more than any coupon.
> The sneaky cost is time. Anything an hour outside the city eats half a day, both ways.
> 
> Read the full chapter: What it really costs to do New Orleans (https://nolapartybarges.com/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/)
> 
> Also: How many days do you need in New Orleans? (https://nolapartybarges.com/1253-2/)
> 
> **Crew's Pick:** Parkway in Mid-City. The po'boy people fly in for. Closed Monday and Tuesday, so Wednesday is po'boy day.
> 
> Split {n} ways, the {boat_name} comes to {per_person} each. That's the whole boat, not a seat on someone else's.
> 
> **Who's actually planning this?**
> [I am] [The group chat] [Someone else]
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**If they booked, the boat line becomes:** Your boat's already in the budget. See you on the bayou.


### G03. Where to crash with a crew

**When:** `{"after_days": 5}`  |  **Subject:** Where to crash with a crew  
**Preview:** The neighborhoods that work for 8 people and a 2am ride home.

> *{days_to_trip} days till New Orleans.*
> 
> Big groups need two things from a place to stay: room for everyone, and a short ride home at 2am.
> 
> Marigny: walk to Frenchmen for music, quieter streets, real houses that sleep a crew.
> Lower Garden District: calmer nights, close to Magazine Street, easy streetcar access.
> CBD and Warehouse District: hotels with room blocks, everything walkable, the most noise.
> Sleeping right on Bourbon sounds fun until it's 4am and somebody's still singing under your window.
> 
> Read the full chapter: [NEW POST: Where to Stay in New Orleans With a Group]
> 
> **Crew's Pick:** Verti Marte on Royal. Open 24/7, and that deli counter has rescued more 1am crews than any hotel kitchen.
> 
> Wherever you land, the dock is about a 15-minute ride: 2101 Paris Road, on Bayou Bienvenue.
> 
> **Where are you staying?**
> [French Quarter] [Marigny] [CBD / Warehouse] [Garden District] [Not booked yet]
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*


### G04. What's happening the weekend you're here

**When:** `{"before_trip_days": 42}`  |  **Subject:** What's happening the weekend you're here  
**Preview:** The stuff locals plan around in {trip_month_name}, before you book dinner.

> *{days_to_trip} days till New Orleans.*
> 
> New Orleans throws a party most weekends and only tells the locals. Here's what to check for {trip_month_name}.
> 
> Second lines: neighborhood brass-band parades roll on Sundays for much of the year. Follow one for a few blocks. [VERIFY: second line season months]
> Game days: if the Saints are home that weekend, hotels fill up and prices climb. Check before you book a room.
> Festivals: the full chapter lists what's on in {trip_month_name}, and we keep it updated.
> Build one free afternoon into the plan. Something always turns up.
> 
> Read the full chapter: [NEW POST: New Orleans Events by Month]
> 
> **Crew's Pick:** Maple Leaf Bar. Rebirth Brass Band plays every Tuesday. If your trip touches a Tuesday, that's your night.
> 
> The bayou is the quiet side of a loud weekend. A boat afternoon between plans works like a reset button.
> 
> **Full send or chill?**
> [Full send] [Chill] [A little of both]
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**Month variants (only the lines that change):**

- **jan:** Carnival starts before most people show up. / Krewe Boheme rolls Fri Jan 22. Krewe du Vieux rolls Sat Jan 23 from the Marigny into the Quarter, the only krewe that goes through the Quarter. It's bawdy adult satire, so leave the kids at the hotel. / Freret rolls Sat Jan 30. / Times and routes are TBC until the krewes post them. We'll update the chapter when they do. | Link: [NEW POST: Mardi Gras 2027 Parade Guide (refresh of the Krewe of Endymion 2023 post)]
- **feb:** Mardi Gras Day is Tue Feb 9, 2027. The weekend before is the big one. / Muses, Thu Feb 4, Uptown. All-women krewe, and the hand-decorated shoe is the throw everyone wants. / Sat Feb 6 is a double: Tucks at noon Uptown, then Endymion around 4pm in Mid-City, where the neutral ground is an all-day tailgate. / Bacchus Sun Feb 7, Orpheus Mon Feb 8. Times and routes are TBC until the krewes post them. | Link: [NEW POST: Mardi Gras 2027 Parade Guide (refresh of the Krewe of Endymion 2023 post)] | Also: Need a break from the parade route? (https://nolapartybarges.com/mardi-gras-alternative-party-boat-new-orleans/)
- **oct:** Halloween weekend, the Quarter and Frenchmen turn into one long costume party. / Pack a costume even if you swear you won't wear it. You'll be the only one without one by 9pm. / Group costumes win. Matching is easier than it sounds. / Book dinner early. Everyone had the same idea. | Link: Halloween on the bayou (https://nolapartybarges.com/halloween-party-boat-cruise-bayou-new-orleans/)
- **dec:** December is the quiet month, which is the secret. / Shorter lines, cheaper rooms, and the city lit up for the holidays. / New Year's Eve is the exception. Book everything early for that one. / Bring a real jacket. Bayou evenings get cold. | Link: New Year's Eve on the bayou (https://nolapartybarges.com/new-years-eve-holiday-party-boat-booze-cruise-new-orleans/) | Also: Heated winter trips on the bayou (https://nolapartybarges.com/heated-winter-swamp-tours-new-orleans/)


### G05. The boat day, hour by hour

**When:** `{"before_trip_days": 28}`  |  **Subject:** The boat day, hour by hour  
**Preview:** 15 minutes from the Quarter, then cypress, egrets, and gators. Here's the whole afternoon.

> *{days_to_trip} days till New Orleans.*
> 
> Today's chapter is the one thing in this guide we run ourselves. Here's the afternoon, start to finish.
> 
> Leave the Quarter and about 15 minutes later you're at the dock on Bayou Bienvenue, 7 miles out. Check-in is inside, with air conditioning and a real restroom. [VERIFY]
> You bring the drinks, the snacks, and the playlist. The boat brings a captain who knows the water and a bathroom on board.
> Then it's cypress trees, egrets, turtles, and gators sliding past while somebody's toasting the occasion.
> Afternoon or sunset? Sunset wins the photos. The full chapter has the rest. You're back in the Quarter for dinner.
> 
> Read the full chapter: Bayou party cruise: what to expect (https://nolapartybarges.com/bayou-party-cruise-new-orleans-what-to-expect/)
> 
> Also: What time of day is best? (https://nolapartybarges.com/what-time-of-day-is-best-for-a-swamp-tour-in-new-orleans/)
> 
> Also: The closest swamp tour to the French Quarter (https://nolapartybarges.com/closest-alligator-swamp-tour-french-quarter-new-orleans/)
> 
> **Crew's Pick:** Clesi's in Mid-City. Boiled seafood the way locals eat it, crawfish when it's in season. Good fuel before a boat day.
> 
> The {boat_name} is private for your {n}. A $350 deposit holds the date.
> 
> **Which time sounds like your crew?**
> [Morning] [Afternoon] [Sunset]
> 
> The crew at NOLA Party Barge
> 
> P.S. Reminder: {code} takes $50 off any private boat, and it's good through {code_expires}. It ends that day. Ride any date.  *(only while a code is live; dropped once they book)*

**If they booked, the boat line becomes:** You're booked. Bring the cooler, we'll bring the bayou.


### G06. Eat like you live here

**When:** `{"before_trip_days": 21}`  |  **Subject:** Eat like you live here  
**Preview:** Brunch for 12, po'boy day, and the 24/7 grill. Three rules from people who eat here.

> *{days_to_trip} days till New Orleans.*
> 
> Three food rules from people who eat here every day.
> 
> Brunch for 8 or more needs a reservation. Atchafalaya in the Irish Channel has a room for 8+ they call the Poker Room.
> Po'boys are lunch. Parkway is closed Monday and Tuesday and Domilise's is closed Sunday, so plan po'boy day around them.
> Late night, Clover Grill is open 24/7 and cashless. Bring a card.
> The full chapter has the rest, all re-checked for 2027.
> 
> Read the full chapter: [NEW POST: Best Restaurants in New Orleans for 2027 (refresh of post 392)]
> 
> Also: [NEW POST: Brunch Spots That Take Big Groups]
> 
> **Crew's Pick:** Galatoire's on a Friday. Lunch rolls into the afternoon and nobody in the room is in a hurry.
> 
> Brunch, boat, nap, dinner. A lot of crews swear by that Saturday.
> 
> **What are you most excited for?**
> [The food] [The music] [The boat] [Parades] [Gators]
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**Occasion variants (only the lines that change):**

- **bachelorette:** Brunch is the main event, so book it first. / The Country Club in the Bywater does a drag brunch, 21 and up. Call ahead with your headcount, they don't publish a group cap. / Atchafalaya in the Irish Channel has a room for 8+ called the Poker Room. / Late night it's Melba's on Elysian Fields, open 24/7. | Link: A local's itinerary for a New Orleans bachelorette (https://nolapartybarges.com/a-locals-itinerary-for-a-new-orleans-bachelorette-party/)
- **birthday:** Book the birthday dinner first. Everything else fits around it. / Arnaud's takes groups up to 220 and Antoine's has 14 private rooms, so 'can they fit us' isn't the question. / Brunch the next morning: Court of Two Sisters, jazz buffet in the Quarter. / Late night, Clover Grill is 24/7. Bring a card, it's cashless. | Link: Milestone birthdays on a private boat (https://nolapartybarges.com/milestone-birthday-private-party-boat-new-orleans/)
- **cousins:** Feeding 12 people from 25 to 65 without a vote. / Court of Two Sisters jazz brunch buffet: everybody picks their own plate, nobody fights the menu. / Clesi's in Mid-City for boiled seafood at one long, loud table. / Parkway for po'boys any day but Monday and Tuesday. Grandma gets the first one. | Link: [NEW POST: Cousin Trips in New Orleans (the /cousin-trips page)]
- **family:** Kids, grandparents, and one picky uncle. / Court of Two Sisters jazz buffet works for every age. / Cafe Beignet for beignets with a shorter line than the famous one. / Superior Seafood Uptown has an oyster happy hour for the grownups. | Link: [NEW POST: Brunch Spots That Take Big Groups]
- **work:** Private rooms do the hosting for you. / Antoine's has 14 of them. Arnaud's takes groups up to 220. / Peche in the Warehouse District for the smaller team dinner. Call about group size first. / Galatoire's Friday lunch if you're closing a deal, or just pretending to. | Link: [NEW POST: Best Restaurants in New Orleans for 2027 (refresh of post 392)]


### G07. What to wear (it's not what you think)

**When:** `{"before_trip_days": 14}`  |  **Subject:** What to wear (it's not what you think)  
**Preview:** Shoes first. The sidewalks here have opinions.

> *{days_to_trip} days till New Orleans.*
> 
> {first_name}, two weeks out. Time to talk shoes.
> 
> Sidewalks here are cracked, tilted, and sometimes just missing. Sneakers you can dance in beat heels you can't walk in.
> The full chapter has {trip_month_name} weather. Short version: summer means a fresh shirt by afternoon, and fall nights run cooler than people pack for.
> Dress codes are real at the old-line restaurants. Check before you book dinner, not at the door.
> For the boat: flat shoes, sunglasses, and a layer for sunset.
> 
> Read the full chapter: Do New Orleans bars have a dress code? (https://nolapartybarges.com/unveiling-the-charm-do-new-orleans-bars-have-a-dress-code/)
> 
> Also: [NEW POST: What to Wear in New Orleans, Month by Month]
> 
> **Crew's Pick:** Loretta's Authentic Pralines. Local, Black-owned, and the praline you bring home for whoever didn't come.
> 
> The bayou doesn't do dress codes. Matching shirts are welcome.
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**Month variants (only the lines that change):**

- **dec:** Also: New Orleans in December: the weather (https://nolapartybarges.com/exploring-december-weather-in-new-orleans-what-to-wear/)
- **jan:** Also: New Orleans winter weather (https://nolapartybarges.com/exploring-december-weather-in-new-orleans-what-to-wear/)


### G08. Bourbon is the appetizer

**When:** `{"before_trip_days": 10}`  |  **Subject:** Bourbon is the appetizer  
**Preview:** Do it once, get the photo, then go where locals actually go out.

> *{days_to_trip} days till New Orleans.*
> 
> Do Bourbon once. Walk it, get the photo. Then go where the locals go.
> 
> Frenchmen Street is a few blocks of live music: Spotted Cat, Blue Nile, d.b.a. Walk in and there's a band.
> Daiquiris, by when you need them: Melba's on Elysian Fields is 24/7, Bourree in Carrollton runs Thursday to Sunday, and Lafitte's Blacksmith Shop pours yours in a candlelit bar from the 1700s. [VERIFY]
> Water between stops. Day two is the good day, don't miss it.
> 
> Read the full chapter: [NEW POST: Frenchmen vs Bourbon: A Local's Night Out]
> 
> Also: Beyond Bourbon Street (https://nolapartybarges.com/beyond-bourbon-street-things-to-do-new-orleans-water/)
> 
> Also: [NEW POST: Daiquiri Shops Ranked]
> 
> **Crew's Pick:** Bacchanal in the Bywater. Wine shop up front, a band in the backyard, and it feels like someone's party.
> 
> Want a night out with nobody else's crowd in it? The boat's private: your playlist, your people.
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**Occasion variants (only the lines that change):**

- **bachelorette:** Start on Frenchmen, not Bourbon. Spotted Cat for the band, Blue Nile for dancing. / Bride in front for every photo. Everyone else, take turns being the one who knows where the group is. / End at Melba's on Elysian Fields, open 24/7, for the daiquiri and the late food. / Water between stops. Brunch is tomorrow and it's the main event. | Link: [NEW POST: Frenchmen vs Bourbon: A Local's Night Out]
- **birthday:** Pick one home-base bar so the birthday person isn't herding all night. d.b.a. on Frenchmen works. / If it's a Tuesday, it's Maple Leaf. Rebirth Brass Band plays every week. / Late food: Clover Grill, 24/7, cashless. / Somebody gets the birthday person home. Decide who before you leave. | Link: [NEW POST: Frenchmen vs Bourbon: A Local's Night Out]
- **cousins:** Mixed ages need a place where the 25-year-olds and the 60-year-olds both have a good night. / Bacchanal in the Bywater: chairs, a backyard band, food, no shouting. / After that the young ones take Frenchmen, the rest take a ride home. Nobody's stuck. / Regroup at brunch for the stories. | Link: [NEW POST: Cousin Trips in New Orleans (the /cousin-trips page)]
- **family:** A night out with kids looks different, and it's still good. / Early dinner, then a walk down Frenchmen while the first bands play through open doors. / Beignets at Cafe du Monde before bed. / The grownups can go back out after lights out. That's what the second key is for. | Link: [NEW POST: First-Timer's 48 Hours in New Orleans]
- **work:** One dinner together, then let people split. / Music people go to Frenchmen: Spotted Cat, d.b.a. / Everyone else is a 10-minute ride from bed. / Nobody has to be the last one out to prove anything. Breakfast still happens. | Link: [NEW POST: Frenchmen vs Bourbon: A Local's Night Out]


### G09. The pack list

**When:** `{"before_trip_days": 7}`  |  **Subject:** The pack list  
**Preview:** Shoes, a battery pack, and the BYOB boat list. Plus what to leave home.

> *{days_to_trip} days till New Orleans.*
> 
> One week. Here's the list we'd hand a friend.
> 
> For the city: shoes you can walk 15,000 steps in, a phone battery pack, a light layer.
> For the boat, it's BYOB: drinks in cans or plastic, a cooler with ice, snacks, sunscreen, and a playlist downloaded ahead of time. [VERIFY: glass and cooler rules]
> Leave home: heels and the plan to go to bed early.
> Matching shirts? Do it. If they're not ordered yet, today's the day.
> 
> Read the full chapter: The BYOB boat pack list (https://nolapartybarges.com/byob-what-to-pack-new-orleans-booze-cruise/)
> 
> **Crew's Pick:** Killer Poboys, in the back of Erin Rose in the Quarter. Grab lunch on the way out of town.
> 
> You bring the cooler. We bring the boat, the captain, and the bathroom.
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*

**Occasion variants (only the lines that change):**

- **bachelorette:** Sash, veil, matching shirts. Pick a theme, just not the one six other crews picked. / For the boat: drinks in cans, a cooler, snacks, sunscreen, the bride's playlist. [VERIFY: glass rule] / Pack a portable fan if it's summer. You'll thank us. / Leave home: the heels. Cobblestones win. | Link: [NEW POST: Bachelorette Themes That Aren't Tacky (+ local shirt printers)]
- **birthday:** Crown or sash for the birthday person. A cake that travels in a box. / For the boat: drinks in cans, a cooler, snacks, sunscreen, and their favorite songs queued up. / A card for everyone to sign. It'll get read on the bayou. / Leave home: heels and any plan that starts before 10am. | Link: The BYOB boat pack list (https://nolapartybarges.com/byob-what-to-pack-new-orleans-booze-cruise/)
- **cousins:** The shirts are non-negotiable. Order now if you haven't. / Bring a printed photo of grandma for the group shot. Somebody will cry, it's fine. / For the boat: drinks in cans, a cooler, snacks, sunscreen, one good speaker playlist everybody can agree on. Good luck. / Leave home: the family group chat drama. | Link: [NEW POST: Cousin Trips in New Orleans (the /cousin-trips page)]
- **family:** Kids' sunscreen, hats, snacks they'll actually eat, a spare shirt. / Private boats are ages 6 and up, so check the youngest before you book. / For the boat: a cooler with drinks for every age. / Leave home: anything you'd cry about losing to the bayou. | Link: The BYOB boat pack list (https://nolapartybarges.com/byob-what-to-pack-new-orleans-booze-cruise/)
- **work:** Name tags if half the team just met. Seriously, it helps. / One person owns the playlist. Decide who now. / For the boat: a cooler with drinks for everyone, including the non-drinkers. / Leave home: the laptop. It'll be fine. | Link: The BYOB boat pack list (https://nolapartybarges.com/byob-what-to-pack-new-orleans-booze-cruise/)


### G10. Your New Orleans forecast

**When:** `{"before_trip_days": 3}`  |  **Subject:** Your New Orleans forecast  
**Preview:** The weather for your weekend, the rain plan, and how to get around with a crew.

> *{days_to_trip} days till New Orleans.*
> 
> Three days. Here's your weekend.
> 
> {forecast}
> If it rains: storms here usually blow through. Give it an hour before you cancel anything.
> Getting around: the streetcar is cheap and slow, rides are fast and pricey after parades. Order one car per 4 or 5 people before you're all standing on the curb.
> From the Quarter, the dock is about a 15-minute ride. Driving? Free parking at the marina. [VERIFY]
> 
> Read the full chapter: [NEW POST: Getting Around New Orleans With a Group]
> 
> Also: [NEW POST: Rainy Day Plan for New Orleans]
> 
> **Crew's Pick:** Morning Call, now at 5101 Canal Blvd by City Park. The rainy-morning beignet, away from the Quarter crowd.
> 
> Weather calls for the boat come from the captain, and the organizer hears first. [VERIFY: rain policy]
> 
> **Want your forecast by text the morning you land?**
> [Yes, text me]
> 
> The crew at NOLA Party Barge
> 
> P.S. Your $50 off any private boat is good through {code_expires}. Book by then, ride any date. Code: {code}  *(only while a code is live; dropped once they book)*


### G11. Welcome home, sort of

**When:** `{"before_trip_days": 0}`  |  **Subject:** Welcome home, sort of  
**Preview:** Day one plan, and the emergency beignet protocol.

> *{days_to_trip} days till New Orleans.*
> 
> You made it, {first_name}.
> 
> Drop the bags and eat something real first. A po'boy counts.
> Walk the Quarter in the afternoon, while the streets are still clean-ish.
> Go out tonight, just not all the way. Tomorrow's the good day.
> If tomorrow starts rough: water, something salty, then beignets. In that order.
> 
> Read the full chapter: [NEW POST: The New Orleans Hangover Recovery Guide]
> 
> **Crew's Pick:** Cafe du Monde. Yes, the famous one. Go once, get powdered sugar on everything, don't wear black.
> 
> If your crew wants a slow afternoon, the bayou is 15 minutes away.
> 
> The crew at NOLA Party Barge

**If they booked, the boat line becomes:** Boat day: 2101 Paris Road, on Bayou Bienvenue. Get there 15 minutes early. [VERIFY: arrival time]


### G12. How'd we do?

**When:** `{"after_trip": true, "before_trip_days": -2}`  |  **Subject:** How'd we do?  
**Preview:** Send us your best photo. And tell whoever's planning next.

> Hope New Orleans was good to you, {first_name}.
> 
> Two quick asks.
> Send us your best photo, or tag @nolapartybarge. We repost the good ones. [VERIFY: handle per platform]
> Know someone planning a trip? Forward this guide. It's free, and it's what we'd tell them anyway.
> 
> **Crew's Pick:** For next time: Domilise's Uptown. Closed Sunday, worth the trip every other day.
> 
> **Coming back?**
> [Already planning it] [Someday] [Once was plenty]
> 
> The crew at NOLA Party Barge

**If they booked, the boat line becomes:** Thanks for riding with us. If the crew earned it, a review helps more than you'd think: [VERIFY: review link]


## The no-trip-date track

For anyone who picked a year or 'just exploring', or never tapped a month. They still get 1, 1b, 2, and 3 on the normal day-based timing, then these four go out weekly (the year track can stretch to every 10 days). Any tap that sets a month or exact date moves them onto the countdown at the right chapter; nobody gets told they switched tracks. If nd04 gets no tap, they roll into the monthly reel newsletter and get asked again in 6 weeks.

### ND01. Spring, fall, or the weird months?

**When:** weekly #1  |  **Preview:** No dates yet is fine. Here's how each season actually feels.

> {first_name}, no dates yet is fine. Here's how the year actually feels.
> 
> Spring: festival season and the city's favorite weather. [VERIFY: spring festival names]
> Summer: hot, cheaper rooms, afternoon storms, long gold evenings.
> Fall: cooler nights, football weekends, Halloween done properly.
> Winter: the quiet stretch, until Carnival takes over in January and February.
> 
> Read the full chapter: [NEW POST: New Orleans Events by Month]
> 
> **Crew's Pick:** Superior Seafood Uptown. Oyster happy hour, any season.
> 
> The bayou runs year-round. The gators just keep their own schedule.
> 
> **Which season's calling you?**
> [Spring] [Summer] [Fall] [Winter] [Mardi Gras]
> 
> The crew at NOLA Party Barge

### ND02. The first-timer's mistake

**When:** weekly #2  |  **Preview:** Bourbon, a far-off swamp tour, a ghost tour, home. There's a better version.

> Most first trips go the same way.
> 
> Bourbon Street, a swamp tour an hour away in a van, a ghost tour, home. Fine. Forgettable.
> The better version: one neighborhood you didn't plan on, like the Bywater or Mid-City.
> One meal locals argue about.
> One afternoon on the water close to town. You don't need dates to start that list.
> 
> Read the full chapter: [NEW POST: First-Timer's 48 Hours in New Orleans]
> 
> **Crew's Pick:** Johnny's Po-Boys in the Quarter. An argument-starter for the best po'boy near your hotel.
> 
> Our bayou is 7 miles from the Quarter. That's the whole pitch.
> 
> **Is this a real trip or a daydream? (Both are fine.)**
> [Real] [Maybe] [Daydream]
> 
> The crew at NOLA Party Barge

### ND03. Mardi Gras or not Mardi Gras?

**When:** weekly #3  |  **Preview:** Mardi Gras 2027 is Tue Feb 9. Here's the honest case for and against.

> The big question for a lot of crews.
> 
> Mardi Gras Day 2027 is Tue Feb 9. The weekend before it is the most fun the city has all year, and the hardest weekend to find a room.
> For an early-season trip, Krewe du Vieux rolls Sat Jan 23 through the Marigny and the Quarter. Adults only, in spirit.
> Any other month you get the same food and music without the crowd.
> No wrong answer. Just book early if it's February.
> 
> Read the full chapter: Mardi Gras, minus the crowd (https://nolapartybarges.com/mardi-gras-alternative-party-boat-new-orleans/)
> 
> **Crew's Pick:** Lafitte's Blacksmith Shop, at the quiet end of Bourbon. Candlelit, old, and the best case for that street.
> 
> Parade weekend or not, the bayou is the calm 15 minutes from the chaos.
> 
> The crew at NOLA Party Barge

### ND04. Picked your dates yet?

**When:** weekly #4  |  **Preview:** Tap your month and the countdown starts.

> {first_name}, one tap.
> 
> Pick your month and every email after this gets timed to your trip: what's on that weekend, what to wear, what to book first.
> No month yet? Tap 'Still no clue' and we'll check back in a few weeks. No pressure.
> 
> **When are you coming?**
> [Nov] [Dec] [Jan] [Feb] [Mar] [Apr] [May] [Jun] [Jul] [Aug] [Sep] [Oct] [Still no clue]
> 
> The crew at NOLA Party Barge

Month buttons are generated at send time: the next 12 months from the send date, plus [Still no clue]. Tapping a month opens the answer page with that month's weekends as buttons ('Got exact dates?').

## Trip under 3 weeks away: the compression rule

Max 1 email a day. Always 1, then 1b the next day. After that, send what still fits, in this order. If a chapter's slot passes while an earlier one is still queued, the earlier one is dropped, not stacked.

| Days out at signup | Send (1 a day, in order) | Dropped |
|:-|:-|:-|
| 15-20 | 1, 1b, 5, 6, then 7, 8, 9, 10, 11, 12 on their normal days | 2, 3, 4 |
| 8-14 | 1, 1b, 5, 6, 8, then 9, 10, 11, 12 on their normal days | 2, 3, 4, 7 (the shoe line folds into 9) |
| 4-7 | 1, 1b, 6 or 8 (occasion picks: bachelorette, birthday, guys' trip get 8; the rest get 6), 9, then 10, 11, 12 | 2, 3, 4, 5, 7 |
| 1-3 | 1, then 10 the next morning, 11, 12 | everything else, 1b included unless they haven't booked (then 1b replaces 10) |
| Arrival day or later | 11 if it's still arrival day, then 12 | everything else |

Booked guests in compression skip 5 entirely. The P.S. never shows for anyone under 3 weeks who's already booked.

## Crew milestone rewards (share page)

Sent to the organizer when their crew's tap-ins on the "I'm in" page cross a milestone. Each email fires once. Their personal referral link counts too.

### 6 tapped in: `map`

**Subject:** Six of your people said yes  
**Preview:** That unlocks the Crew's Map. It's below.

> {first_name}, six people tapped in. Your people showed up, and you're the reason.
> 
> Unlocked: the Crew's Map. Every spot we'd send a friend to, pinned in one place: brunch that takes 8+, po'boys, the 24/7 deli on Royal, where the bands are. Share it with the group so nobody asks 'where should we eat' at 9pm.
> 
> Next one's at 10: your crew gets featured on our pages.
>
> [Open the Crew's Map]
>
> The crew at NOLA Party Barge

### 10 tapped in: `feature`

**Subject:** Ten in. Your crew's about to be famous-ish  
**Preview:** We'll feature your crew to our 80k followers. Send us your handle.

> Ten people said yes, {first_name}. You built a real crew.
> 
> Unlocked: after your ride, we feature your crew on NOLA Party Barge's Facebook, Instagram, and TikTok, about 80k followers, and tag you. [VERIFY: follower count]
> 
> Reply with your Instagram or TikTok handle. A real person on our crew posts it after the ride, nothing goes up automatically, and you can say no anytime.
> 
> Next unlock is at 14.
>
> The crew at NOLA Party Barge

### 14 tapped in: `photo`

**Subject:** Fourteen in. The captain wants your name  
**Preview:** A free crew photo on the boat, plus a shoutout for the person who pulled this off.

> Fourteen people tapped in, {first_name}. Most group chats can't agree on lunch.
> 
> Unlocked: when you ride, our crew takes your group photo on the boat, free, and the captain gives the organizer a shoutout by name. That's you. [VERIFY]
> 
> Reply with how you want the name said. Nicknames encouraged.
> 
> One more milestone: at 18, your $50 off becomes $100 off.
>
> The crew at NOLA Party Barge

### 18 tapped in: `hundred`

**Subject:** 18 in. Your boat just got $100 cheaper  
**Preview:** Code {code}, good on any private boat booked by {code_expires}.

> Eighteen people said yes, {first_name}. You did that.
> 
> Your code: {code}. It's $100 off any private boat, instead of $50. Book by {code_expires}, ride any date you want. [VERIFY]
> 
> At 18, the Bayou Boogie fits you exactly. The Party Queen takes 22 and the Tikis take 25 if more people show up.
> 
> A $350 deposit holds the date.
>
> [Pick your boat]
>
> The crew at NOLA Party Barge

## The Crew's Map

34 rows (33 spots plus one open slot) from the research file, grouped for the Google My Maps list. This is also the Crew's Pick pool. Neighborhoods marked * aren't in the research file; they come from crew knowledge, so confirm them (V7). Re-check every spot is open the week before it's featured (V6).

| Group | Spot | Neighborhood | Crew line | Note |
|:-|:-|:-|:-|:-|
| brunch for 8+ | Atchafalaya | Irish Channel | Ask for the Poker Room. It's the 8+ room, and brunch there runs long on purpose. | 8+ room |
| brunch for 8+ | The Country Club | Bywater | Drag brunch, 21 and up. The bachelorette brunch we'd book first. | 21+; group cap not published, call first |
| brunch for 8+ | Court of Two Sisters | French Quarter | Jazz buffet in a courtyard. Works for every age and every picky eater. |  |
| brunch for 8+ | Commander's Palace | Garden District | The grown-up brunch. Private rooms if you call ahead. | group cap not published, call first |
| po'boys | Parkway | Mid-City | The po'boy people fly in for. Wednesday is po'boy day. | closed Mon/Tue |
| po'boys | Domilise's | Uptown | Old-school corner shop. Worth the streetcar ride. | closed Sun |
| po'boys | Killer Poboys | French Quarter | Tucked in the back of Erin Rose. Lunch on the way out of town. | inside Erin Rose |
| po'boys | Johnny's Po-Boys | French Quarter | The closest good po'boy to most Quarter hotels. |  |
| daiquiris | Melba's | Elysian Fields | Open 24/7. Daiquiri and late food in one stop. | 24/7 |
| daiquiris | Bourree | Carrollton | The daiquiri locals drive for. Plan a Thursday to Sunday. | Thu-Sun |
| daiquiris | Lafitte's Blacksmith Shop | French Quarter | Candlelit, old, at the quiet end of Bourbon. |  |
| daiquiris | New Orleans Original Daiquiris | Several locations | The local chain. Easy when the group can't agree. |  |
| late night | Clover Grill | French Quarter * | Open 24/7 on Bourbon. Burgers at 3am. Bring a card, it's cashless. | 24/7, cashless |
| late night | Verti Marte | French Quarter | 24/7 deli on Royal. Has saved more 1am crews than any hotel kitchen. | 24/7 |
| late night | Buffa's | Esplanade Ave | Bar and kitchen on Esplanade, between the Quarter and Frenchmen. | kitchen hours conflict between sources, confirm |
| live music | The Spotted Cat | Frenchmen St (Marigny) | Small room, big band. Walk in and dance. |  |
| live music | Blue Nile | Frenchmen St (Marigny) | The dancing stop on Frenchmen. |  |
| live music | d.b.a. | Frenchmen St (Marigny) | Good home base for a birthday night out. |  |
| live music | Maple Leaf Bar | Carrollton * | Rebirth Brass Band every Tuesday. If your trip has a Tuesday, it's this. | Rebirth on Tue |
| live music | Bacchanal | Bywater | Wine shop up front, a band in the backyard. Works for mixed-age crews. |  |
| beignets/coffee | Cafe du Monde | French Quarter * | The famous one. Go once, don't wear black. |  |
| beignets/coffee | Cafe Beignet | French Quarter * | Shorter lines, and they pour beer and wine. |  |
| beignets/coffee | Loretta's Authentic Pralines | [VERIFY: neighborhood] * | Local, Black-owned. The praline you bring home. |  |
| beignets/coffee | Morning Call | City Park area (5101 Canal Blvd) | Moved from the French Market. The rainy-morning beignet. | new address |
| group dinners | Arnaud's | French Quarter * | Takes groups up to 220. The size question goes away. | up to 220 |
| group dinners | Antoine's | French Quarter * | 14 private rooms. The birthday dinner, handled. | 14 rooms |
| group dinners | Galatoire's | French Quarter * | Friday lunch that turns into the afternoon. | Friday lunch |
| group dinners | Peche | Warehouse District | Wood-fired seafood for the smaller team dinner. | group cap not published, call first |
| seafood | Clesi's | Mid-City | Boiled seafood, crawfish in season, one long loud table. |  |
| seafood | Superior Seafood | Uptown | Oyster happy hour. The grown-ups' reward. | oyster happy hour |
| seafood | Seither's | Harahan | Worth the drive for a crew that takes boiled seafood seriously. | outside the city |
| seafood | Casamento's | Uptown * | Tiny oyster house, reopened Oct 1 and likely in its final season. Go while you can. | small room; final season per its site |
| the bayou side | NOLA Party Barge dock | Bayou Bienvenue (2101 Paris Road) | 7 miles from the Quarter, about a 15-minute ride. Gators, egrets, cypress. | free parking at the marina [VERIFY] |
| the bayou side | [VERIFY: crew pick for food near the dock] | [VERIFY] | [VERIFY: one line from JT or Jeff] |  |
## Share page microcopy (Group Chat Link, "I'm in" page)

| Slot | Copy |
|:-|:-|
| Headline | New Orleans, {month}. Who's in? |
| Per-person line | {per_person} each for {n} of you |
| Tap-in button | I'm in |
| Empty state | Nobody's tapped in yet. Go first, it makes everyone else braver. |
| Organizer's "Book it" | Your people showed up. Lock the {boat} with a $350 deposit and the date is yours. |
| Progress | {tapped} of {needed} in for {reward} |
| Unlocked | Unlocked: {reward} |
| Next reward | {needed} more tap-ins and the crew gets {reward}. |
| Referral (organizer's personal link) | Know another crew planning a trip? Send them this; their tap-ins count for you too. |

`{reward}` names: the Crew's Map / a feature on our pages / a free crew photo on the boat / $100 off the boat.

**Paste templates** (placeholders {n}, {per_person}, {boat}, {month}, {share_url}; all under 320 characters before fill, and under 260 so a long share URL still fits):

- **default** (212 chars): New Orleans, {month}. I found a private boat on the bayou 7 miles from the Quarter. Just us, our music, our own drinks, real gators. The {boat} for {n} of us is {per_person} each. Tap in if you're in: {share_url}
- **bachelorette** (235 chars): Bride squad: New Orleans, {month}. I found our boat. Private, on the bayou 15 min from the Quarter, our playlist, bring our own drinks, gators for the photos. The {boat} for {n} of us is {per_person} each. Tap if you're in: {share_url}
- **birthday** (221 chars): Birthday plan for {month}: a private boat on the bayou in New Orleans, 15 min from the Quarter. Our music, our own drinks, gators as guests. The {boat} for {n} of us is {per_person} each. Tap if you're coming: {share_url}
- **cousins** (213 chars): Cousin trip, New Orleans, {month}! I found our boat: private, on the bayou 15 min from the Quarter, our music, our cooler, gators for the shirt photo. {boat} for {n} of us is {per_person} each. Tap in: {share_url}
- **family** (227 chars): Family trip idea for {month}: a private boat on the bayou in New Orleans, 15 min from the Quarter. Gators, egrets, a bathroom on board, ages 6 and up. The {boat} for {n} of us is {per_person} each. Tap if you're in: {share_url}
The other five occasions (bachelor, girls_trip, guys_trip, couples, work, just_because) also have paste text: see the 1b variants above, and `paste_templates_extra` in the JSON.

## [VERIFY] list

Everything the crew must confirm before any of this sends.

| # | Fact | Where it shows | Who closes it |
|:-|:-|:-|:-|
| V1 | **Price conflict.** The brief says $63/seat and $1,250 Tikis. The vault says site and FareHarbor were corrected to **$59 / $1,200** on 2026-09-30 (Meta Ads Price Fix Sheet). Copy never prints a seat price; {per_person} must use whatever FareHarbor says today | 1b, 2, share page, paste templates | David |
| V2 | **Trip length conflict.** Brief says 3 hours; Brand Story, the bach page, and the contest emails say 1 hour 45 minutes. Copy avoids stating a length until this is settled | 5 | JT |
| V3 | Rain and cancellation policy, and who gets told when the captain calls weather | 10 | JT |
| V4 | Check-in inside with AC and a restroom, and free parking at the marina (both from the Closest Swamp Tour page draft, Aug 2026) | 5, 10, Crew's Map | JT |
| V5 | What to arrive with: glass allowed or not, cooler size, ice, and how early to arrive (copy says 15 minutes) | 9 and its variants, 11 | JT |
| V6 | Every spot re-checked as open the week it's featured | Every Crew's Pick, the map | Whoever ships |
| V7 | Neighborhoods marked * in the map (Clover Grill, Maple Leaf, Cafe du Monde, Cafe Beignet, Loretta's, Arnaud's, Antoine's, Galatoire's, Casamento's) | Crew's Map | Crew |
| V8 | Group caps at The Country Club, Commander's Palace, and Peche (not published, call first) | 6 variants, map | Crew |
| V9 | Buffa's kitchen hours (sources conflict) | Map | Crew |
| V10 | One bayou-side food pick near the dock, with a line from JT or Jeff | Map | JT / Jeff |
| V11 | Second line season months | 4 | Crew |
| V12 | Spring festival names for the no-date track | nd01 | Crew |
| V13 | Mardi Gras 2027 parade times and routes (all TBC until krewes publish) | 4 (jan, feb), nd03 | Re-check in Dec |
| V14 | CLOSED 2026-10-13: all post slugs filled from the live sitemap list (site-urls.txt). Only open bit: the budget post slug ends in 2024, so the post itself may want a 2027 refresh | 2 | Content |
| V15 | CLOSED 2026-10-13: NYE slug is /new-years-eve-holiday-party-boat-booze-cruise-new-orleans/ | 4 (dec) | none |
| V16 | Do NOT link post 392 (Best Restaurants) until the 2027 refresh is live. It still names Hot Stuff and other closed spots | 6 | Whoever ships |
| V17 | Lafitte's Blacksmith Shop "from the 1700s" line | 8 | Crew |
| V18 | Social handles per platform (copy uses @nolapartybarge) and the review link for booked guests | 12 | David |
| V19 | **Rewards: follower count.** "About 80k followers" across Facebook, Instagram, TikTok | feature email | David |
| V20 | **Rewards: $100 code.** Needs its own FareHarbor code (private boats only, pontoon out, tested against the $350 deposit), separate from the $50 rolling codes, plus its own end date. The spec only built for $50 | hundred email | David, in FareHarbor |
| V21 | **Rewards: free crew photo + captain shoutout.** Who takes it, how it's delivered, and how the captain gets the organizer's name on the manifest. Ties to the photography upsell pilot, so giving it free needs an ops yes | photo email | JT |
| V22 | **Rewards: referral tap-ins counting.** The contest rules cut referral entries under Meta's promotion rules. This isn't a contest, so it should be fine, but confirm the share page isn't reused for the survey contest | share page referral line | David |
| V23 | Featuring a guest crew publicly: the reply with a handle is the yes, but get a photo release line from the crew at the dock | feature email | David |
| V24 | Ages 6 and up on private boats (from the contest copy facts) | 9 family variant, paste family | JT |
| V25 | Who signs: a crew first name with their OK, or the default | Every email | David |
| V26 | Guest review quotes: the brief pointed at the ads data pack, but it has none. No review lines are used. If you want one, pull it from TripAdvisor/Yelp/Batch | none yet | Crew |
