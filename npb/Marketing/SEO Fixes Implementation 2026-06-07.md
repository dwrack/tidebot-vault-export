# NOLA Party Barges - SEO Fixes (paste-ready)

**Date:** 2026-06-07
**Source:** Follow-up to `SEO Action Plan May 2026.md`. These are the five items confirmed still broken in the June GSC/GA4 review.
**How to use:** Items are ordered by leverage. Item 1 is a single global setting that fixes the "Pedal Barge" suffix on most pages at once. Do it first, then the per-page edits.

Verified live state on 2026-06-07 by fetching each page's HTML.

---

## 1. Kill "Pedal Barge" sitewide (ONE global setting, do first)

The " | New Orleans Pedal Barge" suffix and `og:site_name: New Orleans Pedal Barge` are coming from the global site title, not from each page. Fix the source and most pages correct themselves.

- WordPress Admin -> Settings -> General -> **Site Title**: change `New Orleans Pedal Barge` to `New Orleans Party Barge`. Save.
- Then in the SEO plugin (RankMath or Yoast) -> Titles & Meta / Title Settings: confirm the global title template ends in `%sitename%` (or the separator + site name), not a hardcoded "Pedal Barge" string. If it's hardcoded, change it there too.
- After saving, re-fetch 3 pages and confirm the suffix reads "New Orleans Party Barge" and `og:site_name` matches.

Pages with a hardcoded per-page SEO title (Cajun Queen, see item 5) will NOT be fixed by this and need their own edit.

---

## 2. Budget article refresh (highest-traffic page, the one declining)

Page: `/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/`

**Do NOT change the URL slug.** It ranks at position ~4 with ~17k impressions/month. Changing the slug forces a 301 and risks the ranking. Leave the URL as-is (the "2024" in the URL is fine), and update everything on-page to 2026.

Current title: `How Much Do You Need To Budget For A New Orleans Vacation In 2024? | New Orleans Pedal Barge`
Current meta: auto-snippet starting with `&nbsp;` (mangled)
Current H1: `How much do you need to budget for a New Orleans Vacation in 2024?`

Fix:
- **SEO title:** `How Much to Budget for a New Orleans Vacation (2026)`
- **Meta description:** `Planning a New Orleans trip in 2026? Here is what to budget for food, hotels, tours and nightlife, plus one BYOB bayou cruise that does not blow the budget.`
- **H1:** `How Much Do You Need to Budget for a New Orleans Vacation in 2026?`
- **Body:** find/replace every `2024` -> `2026`. Refresh any dollar figures that are clearly stale (hotel/food estimates). Confirm no "pedal" references remain in body copy.
- **Add a mid-article CTA module** (drop it after the section on activities/entertainment costs):

> ### One New Orleans experience that fits the budget
> If you want something that feels uniquely New Orleans without wrecking your trip budget, a BYOB party boat cruise runs about $63 per person. You get the boat, a captain, and a 2-hour run through the bayou 7 miles from the French Quarter. Bring your own drinks, split it across the group, and it lands cheaper per head than most French Quarter bar nights.
> [See the Freaky Tiki cruise ->](/the-freaky-tiki/)

---

## 3. Twerkin Tiki meta description (currently cut off to "The Twerkin")

Page: `/the-twerkin-tiki/`

- **SEO title:** `Twerkin Tiki: BYOB Party Boat in New Orleans (Holds 30)`
- **Meta description:** `The Twerkin Tiki is a BYOB party boat in New Orleans for up to 30 guests. A 2-hour bayou cruise built for bachelorettes and birthdays, from $63 per person.`
- H1 is fine ("The Twerkin' Tiki").

---

## 4. Our Boats meta description (currently "New Orleans Pedal Party Boat Booze Cruise")

Page: `/our-boats/`

- **SEO title:** `Our Boats: 5 BYOB Party Boats in New Orleans`
- **Meta description:** `Compare our New Orleans party boats: Freaky Tiki, Twerkin Tiki, Cajun Queen, Bayou Boogie and Bentley. BYOB cruises for groups of 6 to 32, from $63 per person.`
- H1 is fine ("Our Boats").

---

## 5. Cajun Queen / Party Queen identity (most broken page)

Page: `/the-cajun-queen/`

Current title: `The Party Queen | Pedal Bike Party Booze Cruise`
Current H1: `The Party Queen`
Current meta: `Introducing the newest New Orleans swamp tour party, the city's first-ever pedal party boat tour perfect for a booze cruise. BYOB or Bottle service.`

**Decision: canonicalize to "Cajun Queen"** (matches the URL). The "the party queen" search query is negligible (9 impressions). Make everything say Cajun Queen and strip all pedal references.

- **H1:** change `The Party Queen` to `The Cajun Queen`
- **SEO title:** `The Cajun Queen: BYOB Party Boat for Groups in New Orleans`
- **Meta description:** `The Cajun Queen is a BYOB party boat in New Orleans for larger groups. Captain included, 2-hour bayou cruise, perfect for birthdays, bachelorettes and corporate events.`
- **Body:** rewrite the intro line. Remove "first-ever pedal party boat tour" entirely. This page also needs the deeper rewrite from the action plan (800-1,200 words, structured H2s) to climb off position 21, but the de-pedal + title + H1 + meta is the urgent part.

---

## 6. GA4 self-referral leak (forward-only fix)

The booking widget bounces sessions through the same domain, so GA4 logs `nolapartybarges.com` as a referral source (4,831 sessions last period, up from 2,192). This pollutes channel reporting and hides true organic/paid attribution.

- GA4 -> Admin -> **Data streams** -> select the web stream -> **Configure tag settings** (Google tag) -> Show all -> **List unwanted referrals**.
- Add (match type "Referral domains that contain"):
  - `nolapartybarges.com`
  - `fareharbor.com`
- Save.

Note: this only cleans data going forward. Historical reports stay polluted. Don't expect the self-referral line to vanish from old date ranges.

---

## Verification (after changes)

Re-fetch each page and confirm title/meta/H1. For GA4, check the Traffic Acquisition report in ~3-7 days and confirm the `nolapartybarges.com` referral line stops growing.
