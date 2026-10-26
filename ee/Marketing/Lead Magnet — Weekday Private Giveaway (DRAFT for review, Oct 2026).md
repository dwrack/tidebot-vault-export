# Lead magnet: weekly weekday private giveaway (DRAFT for review)

**PRIZE UPDATE (Davey, 2026-10-20): "Win a weekday date night in our new private sauna."** Two people, one weekday evening (Mon, Wed or Thu), in one of the new private saunas. It ties straight into the date-night searches (Google "date ideas portland" 480/mo peaking in January, DataForSEO Oct 20; TikTok "date night spots portland oregon"). The privates are new inventory, so a prize night doesn't displace a paying Social guest. Open check: the privates aren't open yet. Confirm the opening date. Until then, early winners get the first date nights once they open ("be one of the first couples in"). The perk for every signup is still open; early access to book the privates fits this prize.


Full build package: `Lead Magnet — Build Package (DRAFT for review, Oct 2026)`.

Status: CONCEPT for Davey, Jonah and Kimberlynn to review, Oct 20 2026. Nothing is built, posted or scheduled. This replaces nothing: "First Plunge" ($99 for 3 visits) was dropped by Davey on Oct 16 and stays dropped.

## The idea in one line
Sign up with your name, email and (optionally) phone, and you're entered to win a free weekday private session. We draw one winner every week. Everyone who signs up joins the list.

**Why a draw, not a free private for everyone:** a free private for every signup gives away our product to people who might have paid. A weekly draw costs us one empty weekday slot a week, which we're not filling anyway (weekday afternoons average under 2 of 8 Social seats, Periode Aug 15 to Oct 12). It also gives Kimberlynn a weekly "this week's winner" post that drives shares.

## The prize
- **Option A, available now:** a weekday Private Party (the big sauna) for the winner and friends, Mon, Wed or Thu, 1 PM or 3 PM. Tuesday 1 to 7 PM is now the sliding-scale happy hour, and Monday Banya may block Monday.
- **Option B, when they open:** a private sauna session for 2 to 4 people, weekday afternoon. Confirm the opening date before promising it.
- The prize is booked with a 100%-off Periode code limited to one use, weekday slots only, and valid 30 days.

## How people enter
1. **Website popup and banner** (Squarespace). Note: in Funnel Lab card c21, Davey picked the quiz popup (A), not an offer popup. Decide whether the draw replaces it or rides inside the quiz.
2. **Instagram and TikTok:** "comment PRIVATE" or a link in bio to the same form.
3. **On-site QR** on the deck and lounge, for guests to share with a friend.

**Form fields:** first name, email, phone (optional), plus a text-consent checkbox.

**Consent text:** "Text me if I win and the occasional offer. Msg & data rates may apply. Reply STOP to opt out."

**Small print:** No purchase necessary. One entry per person per week. Must be 21+. The winner is drawn every Wednesday and notified by email (and text if they opted in). Not sponsored by or affiliated with Instagram or TikTok. Full rules are linked.

## What happens after signup (email)
- **Right away:** "You're in this week's draw." Includes a first-timer guide (what to bring, how a session works) and a Book button for anyone who doesn't want to wait.
- **Day 3:** a short walkthrough of a session, with photos.
- **Wednesday:** winner announcement to the whole list, plus "next week's draw is open."
- **After that:** they move to the regular newsletter, with unsubscribe as a hosted link.
- **Texts** only go to people who checked the box, and only once Twilio's business texting registration (A2P) is approved. Per the Oct 19 memory note it FAILED (opt-in not verifiable) and needs refiling. The new form's consent box could be the opt-in proof.

## What it takes to build
| Piece | Who | Notes |
|---|---|---|
| ActiveCampaign form + tag `weekday-draw` + 3 emails | L | Same AC account as the newsletter |
| Squarespace popup + banner | Jess | Footer code injection, popup once per visitor |
| Weekly draw + winner code | Claude can automate the draw; L or Davey issues the code | One Periode code per winner |
| Official rules page | Jess | One page, linked from the form |
| Weekly "winner" post + entry reminders | Kimberlynn | Doubles as the shares driver |
| Measure | Claude | Weekly signups, entries by source (popup, IG, TikTok, QR), and bookings by entrants within 30 days |

## Decisions (answer by number)
1. Draw (recommended) or a free private for every signup?
2. Prize: the Private Party now (A), or wait for the private saunas (B)?
3. Weekly or every two weeks?
4. Include the SMS opt-in now, or email only until A2P is verified?
5. Launch date. The week of Nov 2 avoids the Nov 1 pricing change.
