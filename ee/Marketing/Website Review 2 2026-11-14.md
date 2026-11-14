# Website review 2, 2026-11-14

Site: https://ebb-and-ember-site.pages.dev (repo dwrack/ebb-and-ember-site). Four lenses: script sweep + image check, conversion (page-cro), design (frontend-design), SEO audit. Previous sweep: [[Website Sweep 2026-11-14]].

## Fixed and live (commits 35724ba, ff0a293, f9f8b01)

**Images**
- Every image already had an SEO filename (no IMG_1234 style names) and a descriptive alt on its main page.
- 102 card thumbnails on the blog had empty alt text. They now reuse each photo's alt from its main page.

**SEO**
- 25 meta descriptions rewritten to 120 to 155 characters (Google cuts off longer ones). og and twitter descriptions match.
- Banya Mondays and the Friday Sunrise Swim now carry a weekly schedule in the event schema, so they don't "expire" in Google after one date.
- Footer on every page now links Private saunas, Private events and River temperature. Private events had only 5 internal links before.
- River page: the yearly temperatures are now plain text under the live reading (crawlers and AI search saw only "--" before). The live line now credits the nearest USGS gauge instead of "our ladder".
- Sitemap dates refreshed.
- All JSON-LD validates. No broken internal links. Every page has one H1 and a correct canonical.

**Conversion and design**
- Phone bug: 8 pages had a final section with no side margin (text touching the screen edge). Fixed.
- Memberships: the "MEMBERSHIPS" heading ran off the right edge on phones. Fixed.
- Shop: "Buy" buttons now say "Buy a sauna gift card" / "Buy a private sauna gift card".
- Sessions: "Plans change? Move or cancel up to 1 hour before and get a gift card for the full amount." sits under the prices.
- Private events: "Or text (503) 308-1293 with your date, headcount and start time." under both Plan Your Event buttons.
- Book buttons added on the blog index and near the top of the river page.
- 29 booking links were missing a checkout title. All have one now.

**Cleanup**
- 9 stray page copies (events_index.html and similar) that were committed by accident are deleted.
- Review quotes: Rebecca's quote dropped "I will be coming back" (the "come" rule). The Banya quote is now Anjuli's, because Heather's said "healing".

## Needs Davey (decisions)
1. **Home hero buttons.** Three equal buttons, and "Book a private" wraps onto its own line. Recommendation: keep "Book a session" plus "First Plunge: 3 for $99", and drop "Book a private" (Find Your Ritual already covers it).
2. **Home order.** The phone page is about 10,000px tall. Recommendation: collapse the 9 safety bullets to one line plus the video, and move the reviews block up right after Find Your Ritual, with a Book button after it.
3. **$59 in "Today on the river".** The live seats show $59 while the hero says from $35. Most likely Periode is still on the old prices until the 11/23 switch (unverified). Check it on launch day.
4. **Private saunas page on phones.** East + West (not bookable until December) shows before the bookable Group Session. Recommendation: show Group Session first.
5. **Events.** The three "Starting soon" cards have no action. Recommendation: one "Tell me when these open" email signup. Optionally swap the dark night hero for a photo with people in it.
6. **First Plunge.** The rain stats (150 days, 9 hours, 1 in 2) push the Take the Plunge button down. Recommendation: move them below the button.
7. **Blog titles on phones** wrap to as many as 7 lines. Recommendation: a smaller heading size for blog posts.
8. **AI search leads.** Home, prices, sessions, memberships and First Plunge open with short lines. A 40 to 60 word opening paragraph (what, where, price, hours) is what ChatGPT and Google AI Overviews quote. I can draft these for approval.
9. **"Cold plunge portland."** No page targets it. Options: retitle the river page, or add a short /cold-plunge-portland/ page.

## Checked and not changed
- Rating schema (aggregateRating): Google ignores star ratings a business puts on its own site about itself. Not added.
- "Black image boxes" reported on fast scroll: these were lazy images that hadn't loaded during an automated screenshot. Not a real bug.
- Blog dates are correct (published 11/3 and 11/14).
- Heading jumps (H1 straight to H3) on the bachelorette, birthday and terms pages: minor, left as is.

## Shipped 11/14 (Davey's picks)
- Home: reviews moved up under Find Your Ritual with Book + "Read all 139 reviews"; safety box is one line plus the video.
- Private saunas: Group Session shows first on phones.
- Events: "Get an email when this opens" on each Starting Soon card, saved to its own list: event_industry_happy_hour, event_women_femme_night, event_silent_night, event_sauna_hat_workshop. L to make matching tags in the email tool.
- First Plunge: rain stats moved below Take the Plunge.
- Blog post titles smaller on phones.
- Poetic 40 to 60 word openers on home, prices, sessions, memberships, First Plunge.
- /columbia-river/ now targets "cold plunge Portland": title, H1, description, VideoObject schema, footer link "Cold plunge + river temp", /cold-plunge-portland redirects to it. Safety video v8.3 inline with 8 chapter buttons.
- Site video is now v8.3 everywhere (home too). Videos are served with byte ranges by functions/a/[[path]].js so chapters and scrubbing jump instantly.
- Not done (not picked): home hero buttons. $59 seat price: check on launch day.
