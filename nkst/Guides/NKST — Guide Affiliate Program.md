# NKST — Guide Affiliate Program

*Created: July 18, 2026*

---

## What this is

Every active NKST guide is now a formal affiliate in the Affiliate Master Doc (Google Sheet, tab "NOLA"), same system already used for ~65 outside partners (ghost tour guides, hotel staff, Uber drivers, etc.) since 2023. This is distinct from [[NKST — Affiliate & Partner Program]], which covers those external partners — this doc is guide-specific.

Guides get their own tracked FareHarbor booking link, a 10% commission on anything that books through it, and (once bios/photos are in) their own landing page on the main site to point people to.

---

## Commission & payout

- **10%** of the booking total, matching the standard already used for every other affiliate on the sheet — no guide gets a different rate.
- Tracked automatically through FareHarbor via the `ref`/`asn` URL parameters on each guide's unique link — no manual promo code needed, no dashboard login required for the guide.
- Paid the same way existing affiliates are paid: through FareHarbor, per the sheet's standing note ("paid through fareharbor"). Confirm payout cadence with David before guides start actively pushing this — the sheet doesn't specify a schedule.

---

## Active guide roster & link status

| Guide | Status | Affiliate Code | Booking Link |
|---|---|---|---|
| Nick Napoda | **Already active** (since 2023) | `nicknapoda` | Working |
| Alex Wallace | **Already active** (since 2023) | `alexwallace` | Working |
| MJ Hicks (Madeline Joan Hicks) | **Already active** (since 2023) | `madelinejoanhicks` | Working |
| Ryan Carr (Ryan David Carr) | **Already active** (since 2023) | `ryandavidcarr` | Working |
| Michelle Healey | **Already active, but under an old code** | `ramparttreehouse` (her old pizza-bar business, not her guide identity) | Working, but flagged below |
| Stephanie Lazensky | **Added 2026-07-18** | `stephanielazensky` | Working, link generated |
| Josh Smith | **Added 2026-07-18** | `joshsmith` | Working, link generated |
| River Bourne | **Added 2026-07-18** | `riverbourne` | Working, link generated |
| River Umberger | **Added 2026-07-18** | `riverumberger` | Working, link generated |

**Flag on Michelle:** her existing affiliate row is tagged to "Rampart Treehouse" (a pizza bar), not her as an NKST guide. Didn't touch her existing row or generate a second one — changing/duplicating a live affiliate entry without checking first risks breaking whatever tracking history is already tied to that code. Decide with David whether to rename it, add a second guide-specific row for her, or just leave it as-is since it still works.

All four new rows are marked `Connection Complete = FALSE` and `Dashboard Access = FALSE` in the sheet — the booking link itself works right now, but nobody's set up a FareHarbor partner dashboard login or generated a QR code for these four yet. That's a manual FareHarbor-side step, not something doable via API (NKST has no FareHarbor API access — see [[reference_fareharbor_no_api]]).

---

## Landing pages — ON HOLD

Individual guide bio pages (built on the main WordPress site via the existing Playwright publish workflow — see [[reference_nkst_wp_publish_workflow]]) are **paused until David has the Zoom call recording** to pull real bio content and video from. Building placeholder pages now would mean rewriting them once real content lands — better to wait and build all 9 in one pass with real material.

Once that recording's in hand: pull each guide's story/photo, build the page (H1 = guide name, bio, favorite swamp story, their tracked booking link as the CTA), publish under something like `/guides/nick-napoda`.

---

## What's next

- [ ] David: confirm payout cadence/process for the 4 newly-added guides (Stephanie, Josh, River B, River U)
- [ ] David/Dylan: decide what to do about Michelle's old Rampart Treehouse code
- [ ] David: get the Zoom recording over so bios/landing pages can get built
- [ ] Send each guide their link + the social selling playbook (see [[NKST — Guide Affiliate Social Selling Playbook]]) once ready to activate
- [ ] Set up FareHarbor QR codes/dashboard access for the 4 new guides (manual, FareHarbor side)

---

*Related: [[NKST — Affiliate & Partner Program]] · [[NKST — Guide Affiliate Social Selling Playbook]] · [[Guides/Guide Roster 2026 — Active]] · [[reference_fareharbor_no_api]]*
