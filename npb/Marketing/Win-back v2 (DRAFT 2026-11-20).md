# NPB Win-back v2 (DRAFT 2026-11-20, not approved, nothing scheduled)

Replaces the h01-h03 / w-series style. Old series: 136k emails Oct 6-Nov 17, 0 ref-tagged bookings, two complaint auto-kills (h02 0.69%, h03 1.06%).

## Why the old one missed (from FareHarbor 2026 data, pulled 2026-11-20)
- **Wrong product.** 95% of tiki boat bookings were 1-9 guests, median 2 guests, about $60/head: people bought seats. The copy kept pitching "private boat, your crew, nobody you didn't invite."
- **Wrong ask.** 90% of riders have out-of-town phone numbers (3,527 of 3,913). "Come back this Saturday" doesn't land for someone who visited NOLA once.
- **Wrong audience.** Sent to 46k incl. people who never opted in. Complaints come from "who is this?" Only ~7% of 2026 bookers opted in.
- **Two CTAs.** The Instagram reel card competed with the booking button and made it look like a promo blast.
- **Too often.** 3-5 emails in 6 weeks to the same people.

## Send rules for v2
- Opted-in only, booked in the last 24 months, never got h02/h03. Most recent riders first, 2,000/day max.
- One email per person, not a series. Max 1 NPB marketing email per person per 90 days.
- Split by phone area code: 504/985/225 = local version, everything else = visitor version.
- First line says who we are and why they're getting this. One button. No reel card, no header banner.
- Hosted one-click unsubscribe (existing). Ref tags: `npb-winback-v2-visitor` / `npb-winback-v2-local`.
- Verify before send: seat price (median $60/head in 2026 data, confirm on FareHarbor).

## Version A: visitors (~90%)

Subject: Know anyone heading to New Orleans?
Preview: You rode with us on the bayou. Here's the short version to pass along.

Hey {first_name},

This is NOLA Party Barge. You rode one of our tiki boats on Bayou Bienvenue, so we figure you're the person friends ask "what should we do in New Orleans?"

If someone you know has a trip coming up, here's the short version to pass along:

- A 2-hour BYOB tiki boat on the bayou, 15 minutes from the French Quarter
- Grab a couple of seats (around $60 each), or take the whole boat for a bachelorette or birthday
- Bring your own drinks and your own playlist

Just forward this email. The booking link is right below.

And if you're the one coming back, we'd love to have you out again.

[Button: See boats and times]

NOLA Party Barge

## Version B: locals (~10%)

Subject: You're 15 minutes from the bayou
Preview: Late fall is the best weather we get all year.

Hey {first_name},

This is NOLA Party Barge. You rode with us on Bayou Bienvenue, and you live close enough to do it again any weekend you want.

Late fall is our favorite stretch: cool air on the water and sunset around 5. Grab a couple of seats for a Saturday, or take the whole boat for a birthday or a holiday get-together.

[Button: See this weekend's boats]

NOLA Party Barge
