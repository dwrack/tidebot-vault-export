# Member Night — Send List (built 2026-07-22)

**38 recipients**: 27 current, 11 past.

## Sources and how they were reconciled

Two sources, cross-checked against each other:

1. **Periode merchant API** — `/products/{id}/subscriptions` across Ember 1-4. 45 rows, 38 unique people.
2. **`betalinger.csv`** — Periode payments export Davey pulled 2026-07-22. 146 rows, 36 unique emails.

33 people appear in both. The differences are explained, not arbitrary:

**In the payments CSV but NOT real members (3).** Each is a single `FAILED` invoice with no active subscription in the API. Payment declined, membership never started. All excluded:

| Email | Name | Product | Note |
|---|---|---|---|
| alfmags@gmail.com | Alf Magnus Stålesen | Ember 3, $299 | Norwegian name on the one product with zero real subscribers. Periode-side test, same bucket as Erik. |
| aubreyhenrichs@gmail.com | Aubrey Henrichs | Ember 2, $139 | Card failed 2026-01-02. Candidate for a separate win-back email, not this one. |
| infoanne@gmail.com | (no name) | Ember 1, $99 | Card failed 2026-04-10. Same. |

**In the API but NOT in the payments CSV (5).** Comped memberships generate no payment rows, so an export of payments can't see them. This is why the API pull is the better source of truth for a member list.
Erik Kvanli's two accounts are Periode vendor tests (excluded). Hannah Bronfman, Mack John, and Jordan Culberson are real comped crew (included).

## Gap this surfaced

The crew gift list ([[reference_crew_gift_membership_list]]) has 6 people on comped Ember 2 through Sept 30, but **only 3 exist in Periode**. Jess Astrella, Grant McElroy, and Kimberlynn Baggs have no Periode record at all, so any member list built from Periode silently drops them. Added manually here per Davey 2026-07-22. **Their memberships should be created properly in Periode so this stops recurring.**

Hannah is in Periode as `hbronfman@gmail.com` but on the crew list as `hannah@ours-here.com`. Sending to the Periode address since that's tied to the actual membership.

## Flag: eabinante+ee@gmail.com

Included, but it looks like a test account. The `+ee` tag, a $1 "Secret Subscription" product, and an Ember 1 subscription that started 2026-07-22 (the same day this list was built, no payment yet) all suggest someone internal testing the signup flow. Included on the logic that wrongly excluding a brand-new member is worse than a teammate getting a party invite. Drop it if you know otherwise.

## Scrub applied

- Gmail-normalized dedup (dots and plus-tags collapsed): 45 rows to 38 people
- SendGrid suppressions checked live: unsubscribes, bounces, blocks, spam reports, invalid emails
- `Marketing/Do Not Contact List.md` checked
- Removed: `erik@periode.no`, `erik+100@periode.no` (Periode vendor tests), `yorefinnej@icloud.com` (Jennifer Wessler, cancelled 2026-06-21 over jet noise, on both the DNC list and SendGrid global suppression)

## Current members
- abundanciacoffee@gmail.com — (no name) — Ember 1
- aestevens617@gmail.com — (no name) — Ember 1
- alishamcb@yahoo.com — Alisha McBride — Ember 2
- amye@msamye.com — (no name) — Ember 1
- areillars@gmail.com — (no name) — Ember 1
- craigvern@gmail.com — (no name) — Ember 1
- danandersonpt@gmail.com — Shirin Zargar — Ember 2
- doleshko@gmail.com — Danesh Oleshko — Ember 2
- eabinante+ee@gmail.com — L Abinante — ?1, Ember 1
- emilygraceanderson12@gmail.com — EMILY GRACE ANDERSON — Ember 2
- erin@wrightmctaggart.com — Erin McTaggart — Ember 2
- eskaar@gmail.com — Eric Z Skaar — Ember 2
- grant@tnbars.com — Grant McElroy — Ember 2 (comped crew)
- hayley.weed@gmail.com — (no name) — Ember 1
- hbronfman@gmail.com — Hannah Bronfman — Ember 2
- jess@ours-here.com — Jess Astrella — Ember 2 (comped crew)
- jordan@hiearlybird.com — Jordan Culberson — Ember 2
- josiahdmarshall@gmail.com — Josiah Marshall — Ember 2
- kennedyhutsell@gmail.com — (no name) — Ember 1
- kimberlynnpdx@gmail.com — Kimberlynn Baggs — Ember 2 (comped crew)
- lauralampton@gmail.com — Laura Scott — Ember 2
- mack@hiearlybird.com — Mack John — Ember 2
- nastiakuznets@gmail.com — (no name) — Ember 1
- nastja.rebrin@gmail.com — (no name) — Ember 1
- peshtainlove@gmail.com — Sergei Kamenskikh — Ember 2
- sjcrouse@gmail.com — (no name) — Ember 1
- zjd5007@gmail.com — Zach Dow — Ember 1, Ember 2

## Past members
- bloodred37@gmail.com — (no name) — Ember 1
- chrisjensen10@yahoo.com — (no name) — Ember 1
- dan_galucki@yahoo.com — (no name) — Ember 1
- devindimeoediger@gmail.com — Devin Dimeo-Ediger — Ember 2
- dnokovic@gmail.com — (no name) — Ember 1
- edelgadore@gmail.com — (no name) — Ember 1
- elizemails@yahoo.com — Elizabeth Kuhn-Wilken — Ember 1, Ember 2
- hightideenergy@gmail.com — Eric grundberg — Ember 2
- jankekolb@gmail.com — (no name) — Ember 1
- jwoodpdx@gmail.com — (no name) — Ember 1
- syoung15301@gmail.com — (no name) — Ember 1
