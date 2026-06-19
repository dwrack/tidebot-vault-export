# Repeat-Business Win-Back Survey

*Created 2026-06-19. David's question: why don't past guests rebook? Find out, then fix it. Start with a survey email to past customers on ONE business as a pilot.*

## The real question
Across the portfolio we get a lot of first-time bookings and not much repeat. Is that because the experience is one-and-done by nature (destination tourists who won't be back in Door County for years), or because we never gave them a reason/path to return (no follow-up, no locals offer, no "bring your crew next time")? A short survey to past guests tells us which.

## Mechanics
1. **Pull the past-customer list** from FareHarbor for the pilot business (export bookings → emails, with first name + tour + date). FareHarbor is the source of truth for who actually came.
2. **Draft one short survey email** — 3-4 questions max, mobile-friendly, plain ASCII subject. Ask the things that actually move rebooking:
   - How was it? (1-click rating)
   - What would make you come back / book again?
   - Would you do a different tour with us, or refer a group? (surfaces cross-sell + referral)
   - One open box: what stopped you from booking again?
   Offer a small incentive for a repeat/referral booking (a returning-guest code) — gives them a reason and a path back.
3. **Send** via Amazon SES **us-west-2** (production region) for a real list, or the business Gmail for a smaller batch / more personal feel. Past guests are a warm list, so a personable Gmail send is fine for the pilot.
4. **Read the answers**, then turn the top reason into a fix (a returning-guest offer, a post-tour "what's next" email, a locals season pass, etc.). This feeds the email-funnel framework.

## Pilot business — NEEDS DAVID'S PICK
Recommendation: pick a business with a big enough past-customer list AND realistic repeat potential.
- **Buffalo Bayou Kayak** or a **Houston barge (HPB/NPB)** — local/Houston + group-driven, highest realistic repeat + referral rate. Best signal.
- **DCKT / NKST** — biggest lists, but destination-tourist heavy, so "why don't they come back" may just be "they live 1,000 miles away." Still useful for cross-sell/referral.

Once David picks, build the list + draft the email for that one, send, measure, then roll the winning version to the others.

## Outbound rules
- Plain ASCII subject, specific to the content. Short. Clear ask.
- Never sign David's real name — send as the business / manager persona.
