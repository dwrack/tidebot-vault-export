# Website review 3, 2026-11-14

Site: https://ebb-and-ember-site.pages.dev (repo dwrack/ebb-and-ember-site). Commits 95035f5, 94633e8 and two follow-ups. Checks covered speed on a slow phone, layout shift, links, accessibility, copy rules, Search Console queries, and a fresh-eyes conversion and design pass at phone and desktop. Earlier passes: [[Website Sweep 2026-11-14]], [[Website Review 2 2026-11-14]].

## Fixed and live

**Speed**
- On a slow phone, the home page's first photo took 6.6 s to show. The page was loading all six slideshow photos at once, plus a leftover preload of a photo the hero no longer uses.
- Now it loads the first photo first and the rest once the page is up. Three cold loads on throttled 4G measured 2.9 s each.
- Layout shift is 0 to 0.03 on every page. Only one image is over 300 KB.

**Home booking widget**
- It now opens on the first day that has open seats. On a sold-out evening it used to show only "Full" rows.
- The heading follows the tab: TODAY, TOMORROW or SATURDAY ON THE RIVER.
- A fully booked day says "Every seat is taken. Try another day."
- A new "See every open time" link opens the full Social Sauna calendar. The widget itself shows only 3 days.

**Phone menu (all 37 pages)**
- Book a session is first.
- Private events and Know before you go are added.
- The phone number is tap-to-call and stays on one line.

**Accuracy and copy rules**
- Memberships guest-pass answer: "comes with" is now "includes" (from today's membership update).
- First Plunge search description: "the $99 comes off" is now "counts toward your membership".
- Prices "Do the math": the comparison used the 12-month price without saying so. The rows now read "Daytime, 12-month plan" and "Anytime, 12-month plan", and the FAQ answer names the plan.
- New Prices FAQ, also in the schema: "Which days count as holidays?" The answer lists New Year's Day, MLK Day, Memorial Day, July 4, Labor Day, Thanksgiving and the day after, Christmas Eve, Christmas and New Year's Eve, priced like evenings and weekends. The list comes from Jonah's pricing.
- East and West Saunas now say "Opening in December" on the home card and in the private events intro.
- Shop: "$35 covers a weekday hour; $60 covers two hours on an evening or weekend."
- Christmas Ships, checked against the official 2026 schedule on christmasships.org:
  - On Dec 4, 9 and 15, 7 to 9 PM, the fleet runs to North Portland Harbor, which is our water.
  - The Nov 27 tree lighting is both fleets. The November guide wording is fixed.
  - The November and December guides did not actually contradict each other.
- August guide: the meteor calendar link was a 404. It now points to the IMO's current calendar.
- Chat helper answers are rebuilt from the updated pages (102 questions). The test set still passes 50 of 50.

**Layout**
- Events "Starting soon" is a 2x2 grid on desktop. It was 3 cards plus 1 alone on the second row.
- Month guides on phones: the high/low tile spans the row and no numbers clip. All 12 guides checked.

**Launch safety**
- index-v2.html, photos.html (old 11/12 drafts) and the river poster template now have their own noindex rule in `_headers`. They stay out of Google when the sitewide noindex comes off.

## Search Console (current Squarespace site, Aug 14 to Nov 13, brand searches excluded)

| Search | Impressions | Position | Click rate |
|---|---|---|---|
| sauna portland | 1,271 | 6.8 | 3.9% |
| portland sauna | 543 | 7.7 | 3.9% |
| floating sauna portland | 377 | 2.6 | 59% |
| sauna portland oregon | 337 | 7.0 | 3.9% |
| saunas portland | 287 | 10.3 | 2.1% |
| cold plunge portland | 253 | 9.6 | 2.0% |
| sauna near me | 207 | 8.0 | 7.7% |
| sauna cold plunge portland | 196 | 3.2 | 9.2% |
| private sauna portland | 98 | 8.9 | 3.1% |

"Floating sauna" searches are already won. The volume is in "sauna portland" searches, where we sit at positions 7 to 10. Three things on the new site target them:
- The new home title, "Portland Floating Sauna + River Cold Plunge".
- The best saunas guide.
- The river page, which now targets cold plunge.

Recheck these numbers 4 weeks after launch.

## Needs Davey
1. **Christmas Ships nights.** The fleet passes our dock Dec 4, 9 and 15, 7 to 9 PM. Add one line on home and events: "Christmas Ships pass our dock Dec 4, 9 and 15. Watch from the heat." Add a Book button for those evenings. Recommend yes, up before Dec 1.
2. **Holiday hours.** Are we open Thanksgiving (11/26), Dec 24, Dec 25, Dec 31 and Jan 1, and what hours? Then one line on the FAQ and sessions pages. Needed before 11/26.
3. **Holiday parties.** Add a "Holiday parties" tile on private events and a December note on Group Session: "Holiday party for up to 12, the whole sauna, from $350 weekdays or $450 evenings." Needed first: any December blackout dates.
4. **Gift card delivery.** How does the card arrive: by email right away, as a printable, with a gift message? Then add one line on the shop page for last-minute buyers.
5. **First-timer questions with no answer on the site.** Each one needs facts from the team:
   - Lockers, or where phones and keys go.
   - Is the dock step-free, and what is boarding like for limited mobility?
   - Is there a hot shower after?
   - Lighting for 10 PM sessions.
6. **Dec 21 solstice or New Year's Eve session.** Run one? Copy is ready if yes.
7. **Delete index-v2.html and photos.html** (old drafts, now noindexed)? Recommend delete.
8. **Bus line.** The FAQ lists bus 11 and bus 6. Know Before You Go lists only bus 11. Which is right for 173 NE Bridgeton Rd?

Still open from earlier passes:
- Home hero buttons.
- The $59 seat price, to check on launch day.
- The $449 private gift card.

## Checked and left alone
- **Google Fonts loads twice on every page** (a preload plus a blocking copy). Removing the blocking copy made no difference in tests (under 0.1 s), so it stays.
- **153 images have no width or height set.** Measured layout shift is 0 anyway, so no change.
- **travelportland.com and powells.com links** return "blocked" to automated checks. They are most likely fine in a browser.
- **Cosmetic:** some photos repeat on private events, and the last home review card is short. Skipped.
