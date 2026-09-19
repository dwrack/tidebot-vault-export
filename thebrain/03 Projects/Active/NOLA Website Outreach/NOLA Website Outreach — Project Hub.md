# NOLA Website Outreach — Project Hub

**Date:** September 19, 2026
**Status:** Sites built (7). Outreach not started. Offer and pricing not yet decided.
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
  - Chez Pierre: hero badge says 4.3 stars, stats bar says "4.7 stars on Google." One is wrong.
  - Viet Orleans: header says 852 reviews, stats bar says 837.
- [ ] **Drop "Inc" from Ryan's Irish Pub** everywhere in the page. That is the legal name from the Google listing, not what anyone calls it.
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

## Round 2 candidates

Not yet pulled. The audit list lives in the local session that built Round 1 (the "GMB audit New Orleans" session on David's machine). Export the remaining no-website listings with 200+ reviews and 4.0+ rating to this note when Round 1 has two yeses.

---

## Log

- **2026-09-17** — v3 of all seven sites pushed to `dwrack/nola-sites` (menus with prices, live open status, popular-times chart, rating bars, topic cloud, lightbox, deep links, schema). Desktop reveal animation and copy fixes were still being debugged.
- **2026-09-19** — Project hub, prospect cards, and outreach scripts written. No outreach yet.
