# NKST Summer 2026 Newsletter — Campaign Plan & Send Guide

Built 2026-06-17. Code lives at `~/Projects/nkst-tools/newsletter-2026/`. Cloned from the DCKT system; it is an independent copy.

## What this is
16 emails, 2x/week for 8 weeks, to ~31,600 past customers. Goal: get repeat bookings and gift-card sales through the slow summer/fall, cross-sell Manchac <-> Honey Island, and upsell the longer trips and the plantation combo. Sent through Amazon SES (us-west-2 production) from info@neworleanskayakswamptours.com.

## The list
31,599 deduped, valid recipients from the FareHarbor export. This list has barely been mailed, so warmup discipline matters. All of David's businesses share ONE SES sending reputation (account 193742567930), so a sloppy blast here can hurt DCKT and the others. Take email 01 slow.

## Warmup plan for email 01 (do NOT one-shot 31k)
1. Wave 1: `--go --limit 500`. Wait a few hours. Pull SES bounces/complaints.
2. Wave 2: `--go --limit 3000`. Wait. Add any bounced addresses to `bounces.json`, rerun `node recipients.mjs`.
3. Wave 3: the rest (`--go`, confirm the count when prompted).
After email 01 is warmed in, emails 02-16 can go to the full list on their schedule (still watch bounces).

`--limit N` always sends to the FIRST N of recipients.json, so waves overlap. That is fine for a first send to a cold list (everyone hears from us once, earliest names twice) but if you want clean non-overlapping waves, slice recipients.json by hand. For a warmup, overlap is acceptable.

## Suppression / unsubscribes
- Unsubscribes: footer mailto + List-Unsubscribe header both point to info@neworleanskayakswamptours.com with subject "Unsubscribe." Watch that inbox. Add anyone who asks to `unsubscribes.json` as `[{"email":"x@y.com"}]`, then `node recipients.mjs`.
- Bounces: after each wave, check the SES console (us-west-2) or the inbox for bounce notifications, add hard bounces to `bounces.json`, rerun recipients.

## The 16 emails (2x/week — Wed + Sat)
| # | slug | angle |
|---|------|-------|
| 01 | beat-the-heat | FEATURE layout. Beat-the-heat hero. Feature block LEADS with the NEW Bayou Bienvenue self-guided rental (15 min from the French Quarter). Four cards: Bayou Bienvenue (NEW) / Manchac / Honey Island / Shell Bank. Cross-promo to DCKT + Austin. |
| 02 | alligators | Wildlife / gators up close from a kayak (Honey Island) |
| 03 | first-timer | Never kayaked? Flat calm water, you won't tip |
| 04 | two-swamps | Manchac vs Honey Island, do both |
| 05 | cypress-cathedral | The scenery, ancient cypress, mirror water |
| 06 | go-longer | Upsell the Shell Bank half-day / Honey Island Extended |
| 07 | best-time | Go early or late, skip midday heat |
| 08 | honey-island | Honey Island deep dive (Pearl River) |
| 09 | family | A day the whole family agrees on |
| 10 | plantation-combo | Swamp + Whitney Plantation, the premium day |
| 11 | fishing | Kayak fishing/crabbing/shrimping charter |
| 12 | what-to-expect | Heat, bugs, weather, how we handle it |
| 13 | groups | Bachelorettes, birthdays, private trips |
| 14 | rental | Self-guided rental for independent paddlers |
| 15 | fall-season | Fall is the locals' secret + gift cards |
| 16 | pick-your-day | Full menu recap, one link each |

## Tracking & how to judge it
Every booking button carries a FareHarbor `ref=nl_emNN_<tour>` tag plus UTM params (campaign `summer_2026`). FareHarbor stamps the ref onto the booking, so **real sales show up in FareHarbor reports — filter bookings by `nl_`.** That is the number that matters. GA4 purchase attribution through FareHarbor is unreliable; judge on FareHarbor ref + cost-per-booking, not GA4 revenue. The cross-promo band uses `ref=nkst_nl_emNN` so the sister businesses can see traffic we send them.

## Before every send (mandatory)
1. `node build.mjs`
2. Serve `out/` and look at the email at phone + desktop width. Confirm every photo shows the full subject, nothing cropped weird, no broken images.
3. Send yourself a live test: `--test you@gmail.com --go`.
4. Only then send to the list (warmup waves for 01).

## Commands
```
cd ~/Projects/nkst-tools/newsletter-2026
node build.mjs
node recipients.mjs
node send-ses.mjs --email em01-beat-the-heat                       # dry run (default)
node send-ses.mjs --email em01-beat-the-heat --test you@x.com --go # one real test
node send-ses.mjs --email em01-beat-the-heat --go --limit 500      # warmup wave
node send-ses.mjs --email em01-beat-the-heat --go                  # full send (confirms count)
```

## Status
- 2026-06-17: System built, all 16 emails rendered, images on S3, email 01 reviewed at phone width, live test sent to dwrack81@gmail.com. **Holding — not sent to the list. Awaiting David's go.**
