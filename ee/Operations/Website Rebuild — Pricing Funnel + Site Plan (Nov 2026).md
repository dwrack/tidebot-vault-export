# Website Rebuild: Pricing Funnel + Site Plan (Nov 2, 2026)

TEAM ONLY until launch. Source: Jonah's new pricing post in Slack (launch date TBD). Only the Friday Sunrise Swim is public now.

## The one thing we push
**Get a first visit, turn it into First Plunge, turn that into a membership.** Everything else (privates, credit, specialty nights) is a side door for groups, gifts and events.

## The ladder

| Step | Offer | Price | The nudge that moves them up |
|---|---|---|---|
| 1. First visit | Social Sauna, 1 hr | $35 weekday day / $45 evening + weekend | "Daytime visits from $35" in the hero |
| 1b. Longer visit | 2 hr instead of 1 | +$15 | "2 hours is only $15 more" under the time slots |
| 2. Try it properly | First Plunge, 3 visits in 45 days, any Social Sauna any time (not Banya) | $99 (two people $180) | Hero link, its own band under Find Your Ritual, booking confirmation, post-visit text |
| 3. Make it weekly | Daytime $100 / Anytime $175 a month (3-mo min) | $80 / $150 on 12 months | "the $99 counts toward your membership" + "Daytime pays for itself in 3 visits" |
| 4. Lock it in | 12-month plan | $80 / $150 | 24 guest passes up front, lower monthly |

Checked math (all true at the posted prices):
- Daytime $100 vs 3 weekday 1-hr visits $105. Anytime $175 vs 4 evening 1-hr visits $180.
- First Plunge $99 vs 3 single visits $105 to $135.
- Boat private = exactly 10 seats at every price point ($350/$500/$450/$600). Fits 12. Copy: "It costs the same as 10 seats."
- Small private, 1 hr: $125 vs 4 seats $140 (weekday), $175 vs $180 (evening). Only true for 1 hour; 2 hours is equal or more, so the copy says "a 1-hour private costs less than four seats."

## Side doors

| Who | Offer | Where it shows |
|---|---|---|
| Groups of 4 | Small private, $125 / $200 (weekday), $175 / $250 (evening) | Private Saunas section, "Find your quiet" |
| Groups of 8 to 12 | Boat private, $350 / $500, $450 / $600 | Find Your Ritual card |
| Gift buyers, friend groups | Sauna Credit: $200 gets $240, $400 gets $500 | Own band near the bottom, footer link, gift page. November and December push. |
| Event people | Friday Sunrise Swim $25, Banya Mondays $65 | "On the dock every week" section, events page later |
| Neighbors | 25% floating homes, 10% slips, 10% zips 97217/97211 | NOT on the homepage. A /neighbors page, linked in the footer and handed out on the dock |
| Members' friends | Guest passes (1/mo on 3-mo, 24 up front on 12-mo) | Membership page. This is our referral loop. |

## Homepage order (as built on the dev site, local copy)

> **UPDATED 2026-11-02 (working session):** new agreed order and header/mobile rules are in `Meeting Notes/Website Working Session + Dock Ops (2026-11-02).md`. Short version: Menu, Hero, CTAs (Book a session / Book a private / Take the plunge), Today's sessions + First Plunge side by side, Find your ritual, On the dock every week, New on the dock (privates + email list), How it goes, Know before you go (not collapsed), Reviews, Email signup, Footer. Neighbor discounts proposed to scratch (not decided). List below is the earlier build.

1. Hero: "Daytime visits from $35", Book button + "First Plunge: 3 for $99" second button
2. Today's socials: slots at $35/$50 and $45/$60, "2 hours is only $15 more"
3. First Plunge band ("New here")
4. Find your ritual: Social Sauna, Private Party, Memberships
5. Private Saunas 1 + 2 ("Find your quiet")
6. How it goes
7. Know before you go
8. Reviews
9. On the dock every week: Sunrise Swim, Banya Mondays
10. Sauna Credit
11. Rain alerts
12. Footer (gift link now goes to Sauna Credit)

## Parked
- **Pick Your Sky** (sunset + moon week view, book golden hour or the full moon). Pulled from the homepage 2026-11-02, saved as a future fun page. Code: `~/dev/ee-parked/pick-your-sky.html`.

## Upsells off the website (where the money really moves)

| Moment | Upsell | Channel | Status |
|---|---|---|---|
| Checkout | 1 hr to 2 hr (+$15) | Periode | Ask Periode if checkout can offer an add-on |
| Checkout, 4+ seats | "A private costs less" | Periode or site copy | Site copy done; Periode unknown |
| Booking confirmation | First Plunge (first-timers) + Know before you go | Periode email | Ask Periode for a custom block |
| 2 hrs after first visit | First Plunge, $99 counts toward a membership | Aftercare SMS (com.ebbember.aftercare, dry-run) | Needs Davey OK + A2P verified |
| ~Day 35 of First Plunge | "10 days left for your $99 to count toward a membership" | Email | Not built |
| Member month 2 | 12-month switch (lower rate + 24 passes) | Email | Not built |
| Nov 15 to Dec 24 | Sauna Credit as the gift | Site + email + IG | Wait for launch date |


### Fireside Raclette (added 2026-11-09, idea stage)
- **Site:** raclette date photos from the shoot go on the Private Sauna page and the date night / rain date blog posts, with the cheese partner named and linked. See [[Shoot Brief — Fireside Raclette Date (Nov 2026)]].
- **Upsell to test:** a raclette board add-on at private session checkout, priced with the cheese partner. Not a Periode product until Davey and Jonah OK it.
- **Status:** collab pitch sent to Cow Bell PDX 11/6 (cheeseshop@cowbellpdx.com), no reply yet. Nothing goes on the site until they say yes and the shoot happens.

## Open questions
1. Launch date. Nothing with new prices goes on the public site before it.
2. Lock the dev site (Cloudflare Access, email code for Davey, Jonah, L) before deploying new prices to it?
3. ~~Do First Plunge visits work at any time?~~ ANSWERED 11/2 (Davey): any Social Sauna, any time. Not Banya.
4. Banya Monday times: still pending host confirmation.
5. Banya price: $65 confirmed by Davey 11/3 (Jonah's new pricing). Periode still charges $49 until the 11/23 product switch; site shows $65.
5. Can Periode do checkout add-ons and a custom block in confirmation emails?
6. Private saunas opening date.
7. Does the Friday swim stay at 30 people until the small saunas open (then 40)?
