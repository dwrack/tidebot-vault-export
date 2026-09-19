# NOLA Website Outreach — Project Hub

**Date:** September 19, 2026
**Status:** Round 1 built (7). Round 2 built (14), branch `claude/site-generator`, from the recovered audit list. 21 previews total. Outreach not started. Offer and pricing not yet decided.
**Repo:** `dwrack/nola-sites` (GitHub Pages, previews are `noindex` + `robots.txt` Disallow)
**Related:** [[Prospect Cards — Round 1]] · [[Prospect Cards — Round 2]] · [[Round 2 Prospects]] · [[Outreach Scripts]]

---

## What this is

A Google Business Profile audit of New Orleans restaurants and bars turned up well-reviewed places with no website of their own. For seven of them we built a full single-page site from the business's public Google data: story, menu with prices, live open/closed status, popular-times chart, review highlights, photo gallery with lightbox, map and directions, tap-to-call, save-contact vCard, and Restaurant schema.

The pitch is simple: **the site already exists. Walk in, show it on a phone, and ask if they want it.** No mockups, no "imagine if." They see their own place, their own reviews, their own menu, looking better than anything a competitor has.

---

## Round 1 prospects

| # | Business | Area | Type | Rating / reviews | Phone | Preview | Status |
|---|---|---|---|---|---|---|---|
| 1 | Chez Pierre Bakery Lakeview | Lakeview | French bakery + Vietnamese kitchen | 4.3 / 63 | (504) 354-9405 | `/chez-pierre-bakery-lakeview/` | Not contacted |
| 2 | Lucky Jean Seafood | New Orleans East | Seafood takeout counter | 4.2 / 805 | (504) 245-7842 | `/lucky-jean-seafood/` | Not contacted |
| 3 | Banks Meat Market | Mid-City | Corner grocery + po'boy counter | 4.1 / 731 | (504) 301-9171 | `/banks-meat-market/` | Not contacted |
| 4 | Viet Orleans Bistro | CBD | Vietnamese + sushi | 4.3 / 852 | (504) 333-6917 | `/viet-orleans-bistro/` | Not contacted |
| 5 | Cajun Mike's Pub & Grub | CBD | Dive bar + po'boys, est. 2000 | 4.3 / 1,091 | (504) 566-0055 | `/cajun-mikes-pub-grub/` | Not contacted |
| 6 | Ryan's Irish Pub | French Quarter | Irish pub, no kitchen | 4.5 / 875 | (504) 523-3500 | `/ryan-s-irish-pub-inc/` | Not contacted |
| 7 | Mother's Restaurant | CBD / Warehouse | Po'boys + Creole, est. 1938 | 4.2 / 17,396 | (504) 523-9656 | `/mother-s-restaurant/` | **Verify first** (see below) |

Preview base URL: `https://dwrack.github.io/nola-sites/` (confirm Pages is enabled and the URL resolves before the first visit). No email addresses were found for any of the seven. Outreach is walk-in first, phone second.

**Ordering logic:** start with the small independents where the owner is behind the counter and a yes happens on the spot (1–3). Move to the downtown spots that likely have a manager layer (4–6). Mother's is last and conditional.

---

## Offer (proposed, decide before first visit)

Nothing below has been confirmed. Pick one and write it in the scripts before walking in.

**Recommended: one flat monthly, no contract.**
- $99/month. Includes the site, custom domain (we register and hold it, they keep it if they leave), hosting, SSL, and unlimited small edits (hours, menu prices, a new photo, a holiday closure) by text.
- First 30 days free. Site goes live under their own domain the day they say yes.
- Cancel anytime. If they cancel, we hand over the files and the domain.

**Alternative: one-time buyout.**
- $1,200 one-time for the site + domain, then $19/month hosting and edits. Better for owners who hate subscriptions. Worse cash flow for us.

Why the monthly wins: the sites are cheap for us to maintain, most of the value to the owner is "someone will change my hours when I text them," and a $99 line item is under the "I need to think about it" threshold for a place doing $800 to $2,000 a day.

Decisions still open:
- [ ] Price and structure (above)
- [ ] Who is the face of this? David personally, or a brand name (a small "sites by ____" footer line)?
- [ ] Payment rail: Square invoice, Stripe link, or GHL?
- [ ] Domain purchasing account (Cloudflare or Namecheap under a dedicated login, not personal)
- [ ] Where hosting moves once a client signs (stays on GitHub Pages under a custom domain, or Cloudflare Pages). GitHub Pages is fine for v1.

---

## Pre-outreach checklist (do these before anyone sees a preview)

- [ ] **Confirm the preview URL loads on a phone** over cellular, not just wifi. The sandbox could not reach github.io, so this is unverified as of today.
- [ ] **Verify each business really has no website.** The audit flagged the Google profile's website field as empty, which is not the same thing. Mother's Restaurant is a nationally known 88-year-old institution and almost certainly has a site; if so, either drop it or reframe the pitch as a redesign. Cajun Mike's is worth a second check too.
- [ ] **Fix the data mismatches** in the preview copy before showing them to an owner who knows their own numbers:
  - Chez Pierre: hero badge said 4.3, stats bar said 4.7. Now 4.3 in both on the generator branch; confirm which is right against the live listing.
  - Viet Orleans: 837 vs 852. Now 852 everywhere on the generator branch.
- [x] **Drop "Inc" from Ryan's Irish Pub.** Done on the generator branch (folder slug unchanged).
- [ ] **Merge `claude/site-generator` into `main`** on `nola-sites` once the local session's uncommitted work, if any, is pushed. It touches only three of the seven pages plus new `tools/` and `sites/` folders.
- [ ] **Photo rights.** Every gallery is built from the business's public Google profile photos, some of which are customer uploads. For a preview that is fine. Before a site goes live under the owner's domain, ask them for their own photos or get an okay on the specific images used. Put this in the onboarding step, not the pitch.
- [ ] **Add a "Preview" ribbon or footer line** to each page ("Preview built for [Business] by David Rack. Not yet live.") so anyone who stumbles on it knows what it is, and so the owner sees it was made for them specifically.
- [ ] Print a one-page leave-behind (QR code to the preview, the offer in three lines, David's cell). Owners are rarely in when you walk in; the leave-behind is what the cook hands them.

---

## Pipeline stages

`Not contacted` → `Visited, owner not in` → `Owner saw it` → `Yes` → `Live` / `No` / `Ghosted (3 touches)`

Log every touch in [[Prospect Cards — Round 1]] under the business, with date, who you spoke to, and what they said. Three touches without an answer is a close; move on and revisit in 90 days.

---

## Unit economics (for deciding whether to do Round 2)

At $99/month, ten clients is ~$12k/year of near-zero-maintenance revenue. The build cost per site is already sunk for these seven. The question Round 1 answers is the close rate on a warm walk-in with a finished product. If it is 3 of 7 or better, build Round 2 (next 10 from the audit list) before Round 1 goes live, so the momentum from the first yes carries into the next pitch.

Track: visits made, owners actually reached, yeses, and the objection that killed each no. That is the whole dashboard.

---

## Build pipeline (Round 2 and beyond)

The seven originals were hand-built. They are now data files: `sites/<slug>.json` in `dwrack/nola-sites` (branch `claude/site-generator`), rendered by `tools/build.py`. The round-trip test proves the generator reproduces all seven byte for byte, so any new site is:

1. `tools/fetch.py "Name, New Orleans" --instagram handle` pulls the Google profile (name, address, phone, hours, rating, reviews, CID, up to 12 photos at 1600px) and the top 8 Instagram posts by likes, picks a theme by place type, and writes the JSON with every copy field marked TODO plus a photo contact sheet.
2. Pick photos from the contact sheet, write the copy (headline, story, what to order, menu, tip), run `tools/build.py <slug>`.
3. Places that already have a website are skipped automatically.

Full instructions: `tools/README.md` in that repo.

**What it actually needed, resolved 2026-09-19 on David's Mac:**
- *The audit list.* Found. It was never in the vault export or either repo; it is at `TheBrain/03 Projects/NOLA Web Studio/candidates.csv`, 345 rows, written 2026-09-11. Copied into [[Round 2 Prospects]]. The companion note in that folder is evicted from iCloud and would not re-download, so only the CSV was read.
- *A Places API key.* Still missing, and worked around rather than solved. The only Google key on this machine is `PSI_KEY` in `~/.claude/.env`, a PageSpeed Insights key on project 305859912611. Places API (New) is disabled on that project and it is a billable API, so enabling it is David's call, not an autonomous one. `tools/fetch.py` therefore cannot run at all.
- *The substitute.* `tools/scrape_maps.js` reads the Maps place page with Playwright and `tools/from_scrape.py` feeds the result through fetch.py's own `skeleton()`, so the JSON that comes out is identical in shape to the API path and `test_roundtrip.py` stays green. This also recovers the 5-to-1 star breakdown, which the API never had.
- *Instagram.* Dead end. instaloader 4.13.2 fails on every public profile with a schema error from Instagram's side (`ig_business_category_subvertical has been deleted`). Anonymous access is not possible and logging in as David was not something to do unattended. Every photo on every Round 2 site is from Google.
- *Popular times.* Not obtainable. Google no longer renders the popular-times chart for a signed-out browser. Confirmed by scraping Mother's Restaurant, which Round 1 has real popular-times data for, and getting nothing. Every walk-in window in [[Prospect Cards — Round 2]] is reasoned from posted hours instead, and says so.

Not in the API and left blank for new sites (the page hides the block): popular times, the 5-to-1 star breakdown, the topic cloud. The originals got those from the Maps page itself.

## Round 2 candidates

Pulled and verified. Full table in [[Round 2 Prospects]], one card per business in [[Prospect Cards — Round 2]].

Filter: the sweep's `food_bar_cafe` bucket, site status NONE / NONE (social only) / SQUATTER, 200+ reviews, 4.0+ rating, minus the seven already built. 48 rows cleared that bar.

**Check the domain before building.** Three of the top fifteen turned out to own a live website that simply is not linked on their Google profile, which is what made the sweep read them as having none: Beach On Bourbon (thebeachonbourbon.com), Cafe Porche & Snowbar (cafeporchesnowbar.com), Matassa's Market (matassas.com). Cafe Porche is the instructive one, a JS app with an empty HTML title, so a status-code check alone reads it as parked. They were dropped and three reserves promoted in their place.

---

## Log

- **2026-09-17** — v3 of all seven sites pushed to `dwrack/nola-sites` (menus with prices, live open status, popular-times chart, rating bars, topic cloud, lightbox, deep links, schema). Desktop reveal animation and copy fixes were still being debugged.
- **2026-09-19** — Project hub, prospect cards, and outreach scripts written. No outreach yet.
- **2026-09-19** — Generator pipeline built on `nola-sites` branch `claude/site-generator`: extract, build, fetch, themes, byte-exact round-trip test. Copy fixes applied on that branch (Chez Pierre stat now 4.3 to match the rating, verify against the live listing; Viet Orleans 852 everywhere; "Inc" dropped from Ryan's). Round 2 blocked: no audit list reachable, no Places key, Google and Instagram blocked by the cloud network policy.
- **2026-09-19 (afternoon, David's Mac)** — Round 2 unblocked and building. Ran on the Mac specifically because Google and Instagram are blocked from the cloud environment.
  - **Audit list found.** `TheBrain/03 Projects/NOLA Web Studio/candidates.csv`, 345 rows from the 2026-09-11 sweep. Copied into [[Round 2 Prospects]] with name, category, neighbourhood, rating, reviews, phone, CID and place id. The sibling note in that folder is an iCloud stub that would not download; only the CSV was read.
  - **No Places API key, so the pipeline was rerouted rather than run.** Places API (New) is disabled on the one Google project available here and it is billable, so turning it on is David's decision. `tools/scrape_maps.js` (Playwright against the Maps place page) plus `tools/from_scrape.py` (hands the result to fetch.py's own `skeleton()`) now do the same job. `test_roundtrip.py` stays green on all seven originals throughout.
  - **Three prospects disqualified on inspection**: Beach On Bourbon, Cafe Porche & Snowbar and Matassa's Market all own live websites that are simply not linked on their Google profile. Builds for them were deleted, not shipped. Three reserves promoted.
  - **Could not do:** Instagram photos (instaloader is broken against current Instagram and logging in as David unattended was not appropriate), popular times (Google no longer serves the chart to a signed-out browser, verified against Mother's Restaurant which Round 1 has data for), and menu prices (none of these businesses publish a menu anywhere, so every menu block is a highlights list with a "prices as posted" note rather than invented numbers).

  - **14 sites built and pushed**, one commit each, to `dwrack/nola-sites` branch `claude/site-generator`. `test_roundtrip.py` green on all seven originals throughout. Preview paths, with the photo source for every one being the business's own public Google profile:

| Site | Preview | Google | Photos used |
|---|---|---|---|
| Markey's Bar | `/markey-s-bar/` | 4.5 / 490 | 10 Google profile |
| City Donuts & Café | `/city-donuts-caf/` | 4.0 / 1,034 | 10 Google profile |
| Pal's Lounge | `/pal-s-lounge/` | 4.6 / 709 | 10 Google profile |
| Holy Crepes! | `/holy-crepes/` | 4.7 / 295 | 10 Google profile |
| The Upper Quarter | `/the-upper-quarter/` | 4.7 / 358 | 10 Google profile |
| little bar on gravier | `/little-bar-on-gravier/` | 4.8 / 415 | 10 Google profile |
| Small Mart Cafe | `/small-mart-cafe/` | 4.8 / 293 | 10 Google profile |
| New Orleans Snowball | `/new-orleans-snowball/` | 4.5 / 627 | 10 Google profile |
| Bertha's Place | `/bertha-s-place-bar-restaurant/` | 4.4 / 678 | 10 Google profile |
| Boondock Saint | `/boondock-saint/` | 4.7 / 382 | 10 Google profile |
| Norma's Sweets Bakery | `/norma-s-sweets-bakery/` | 4.3 / 536 | 10 Google profile |
| Don Leoncio | `/don-leoncio-cigars-bar/` | 4.4 / 602 | 14 Google profile |
| The John | `/the-john/` | 4.3 / 571 | 14 Google profile |
| Two Sisters | `/two-sisters-soul-food-in-treme/` | 4.2 / 629 | 14 Google profile |

  - **Menu prices.** Only Two Sisters has real ones, because one of their profile photos is the Sunday menu lying on a table. Every other site's menu block is a highlights list with a note saying prices are as posted. No prices were invented anywhere.
  - **Two sites are thinner than the rest.** Don Leoncio and Two Sisters have no quote band and no star-rating bars, because Google served the review-less page layout for both on every attempt. The template omits those blocks cleanly. Worth one more scraping pass each if either says yes.
  - **Still to verify before anyone walks in:** The Upper Quarter's phone number (not on their Google profile, taken from directories), Don Leoncio's hours and Two Sisters' hours (both third-party), and Two Sisters' name and street number, which differ between their own menu and their Google listing. All flagged on the individual cards.
  - **Seal's Class Act skipped on photo grounds.** Six of its ten profile photos are customers with faces clearly visible, one is a portrait of a single person, and the other four are food shots that contradict a review saying food is not served. Nothing usable for a hero. Details in [[Round 2 Prospects]].
  - **Vault sync did not reach `main`.** `scripts/sync-vault-export.js` exported 2,333 files but the push was rejected. The local export diverged from `origin/main` on 2026-04-20 and is 629 commits ahead / 219 behind; main's last vault-sync commit is from April. Merging risked clobbering the Todo.md edits the cloud side has been making since, so the work was pushed to branch `mac-vault-sync-2026-09-19` instead. **This needs David's call: the Mac's vault export has not reached GitHub main in five months.**
