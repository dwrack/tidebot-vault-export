# NOLA Website Outreach — Project Hub

**Date:** September 19, 2026
**Status:** Sites built (7). Generator pipeline ready on branch `claude/site-generator`. Round 2 blocked on the audit list and a Places API key. Outreach not started. Offer and pricing not yet decided.
**Repo:** `dwrack/nola-sites` (GitHub Pages, previews are `noindex` + `robots.txt` Disallow)
**Related:** [[Prospect Cards — Round 1]] · [[Outreach Scripts]]

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

**What it needs to run, and why it did not run on 2026-09-19:**
- A Google Maps Platform key with Places API (New) enabled, in `GOOGLE_MAPS_API_KEY`. None exists in any repo or environment.
- Network access to Google and Instagram. The cloud session's network policy blocks google.com, maps.googleapis.com photo media, googleusercontent, instagram.com, and cdninstagram. Run it on David's machine, or open those hosts in the environment settings.
- The audit list. It is not in the vault export, `nola-sites`, or `tidebot`. It lives in the local "GMB audit New Orleans" session. Export it as one line per business (`Name, New Orleans` or the ChIJ place id) into `prospects.txt` and run `tools/fetch.py --list prospects.txt`.

Not in the API and left blank for new sites (the page hides the block): popular times, the 5-to-1 star breakdown, the topic cloud. The originals got those from the Maps page itself.

## Round 2 candidates

Not yet pulled. See the pipeline section above for what unblocks this. Target: no-website listings with 200+ reviews and 4.0+ rating.

---

## Log

- **2026-09-17** — v3 of all seven sites pushed to `dwrack/nola-sites` (menus with prices, live open status, popular-times chart, rating bars, topic cloud, lightbox, deep links, schema). Desktop reveal animation and copy fixes were still being debugged.
- **2026-09-19** — Project hub, prospect cards, and outreach scripts written. No outreach yet.
- **2026-09-19** — Generator pipeline built on `nola-sites` branch `claude/site-generator`: extract, build, fetch, themes, byte-exact round-trip test. Copy fixes applied on that branch (Chez Pierre stat now 4.3 to match the rating, verify against the live listing; Viet Orleans 852 everywhere; "Inc" dropped from Ryan's). Round 2 blocked: no audit list reachable, no Places key, Google and Instagram blocked by the cloud network policy.
