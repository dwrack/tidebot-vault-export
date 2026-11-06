# Member booking on our site: Periode JWT plan (2026-11-04)

Status: researched, nothing built, nothing changed in Periode. Needs Davey + Jonah OK before any Periode setting changes.

## The finding
Periode documents "Validating an external membership (JWT)" (periode.no/docs/technical/booking-api). Our site can vouch for a member with a signed token, and Periode then books them without asking them to log in to Periode.

- The token is signed with the merchant shared secret. That is the same key we already keep server-side (~/.config/periode/ebb.env), so no new secret.
- Link: `/booking/<org>/<product>/<date>/<time>?quantities=[...]&autoBook=true&token=<jwt>` goes straight to payment, or to a free confirmation when the price is $0.
- Claims: user_id (required), exp (required), plus name, email and phone, so the member never re-types anything.

## Verified live today
`GET /merchants/:id/allsubscriptions` works with our key. It returned 84 subscriptions: 47 ACTIVE (Ember 1: 24, Ember 2: 23) and 37 STOPPED, every one with a customer email. So our site can check "is this email an active member, which plan".

## Flow
1. The member enters their email on ebbandember.com/members and we email them a 6-digit code.
2. Our server confirms an ACTIVE subscription for that email.
3. The member page, in our design, shows the plan, guest passes, today's times at member price, and Book.
4. Book mints a 15-minute token and opens Periode at payment, or at a free confirmation.

## Periode changes needed (approval required)
1. Set a Webhook url on the products members book. It can point at our site (`/api/periode-webhook`), which also gives us live booking events.
2. Create a members-only child product per session type. Each is linked to the main session so they share capacity, and priced at the member rate (e.g. $0 for included visits, $10/$60 Banya).
3. Waiver: Social has a waiver attached, which blocked autoBook in testing. Decide whether member child products skip it (members signed one at signup) or keep it.

## Our-side setup
- Email for sign-in codes: ebbandember.com is NOT verified in SES us-west-2 (checked 2026-11-04). We need DNS records added there, or another sender.
- A KV store for sessions (the same `ee-signups` ask works, or a second namespace).

## Tradeoffs
- Token bookings are owned by an "external user", not the member's Periode account. They won't show in the member's Periode app history, so our member page becomes their history.
- Plan rules (Daytime vs Anytime hours, guest pass counts) are enforced by our site when it mints the token, not by Periode.

## UPDATE 2026-11-04 (afternoon)
The full plan for L is published at https://claude.ai/artifact/W7iNtQFBEhADzVKjDZdwc3 (local copy in member-booking-plan/). It adds Route A: a member signs in to Periode once per phone, and our links carry the member tier + autoBook. That needs no Periode changes and the bookings stay in their app. Bookings cannot be imported: the API has no create or change-owner route for bookings. Four questions are queued for Erik.
