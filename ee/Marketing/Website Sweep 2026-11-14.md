# Website sweep, 2026-11-14

Site: https://ebb-and-ember-site.pages.dev (repo dwrack/ebb-and-ember-site). This covered 39 pages: an automated sweep of links, images, schema, SEO tags and brand rules, plus a page-by-page review of conversion and consistency.

## Fixed and live (commit e6cdede and the commit before it)
- First Plunge: the Friday Sunrise Swim is now shown as included everywhere. The home page and First Plunge page used to say it was excluded. Periode still excludes it until Jonah and L update the product (already on the dashboard).
- Memberships hero: checked against Jonah's "E&E Pricing Launch Drafts" doc, which says members "book privates 30 days before everyone else". That matches the site's 90-day member / 60-day public window. The hero now uses Jonah's wording: "book 30 days before everyone else".
- "No staff" answers on the FAQ and sessions pages now say Monday Banya and the Friday Sunrise Swim are hosted by partners, not E&E staff (Davey 11/14). "Our steam master" on the prices and events pages is now "a partner steam master".
- Private events said the Social Sauna holds 12. It now says 8 shared, or 12 as a Group Session.
- The private saunas hero no longer promises three saunas today. It now says to book the whole sauna for up to 12, and that the East and West Saunas open in December.
- Events FAQ: the missing "Group Session" link is fixed.
- The algae answer on the FAQ and Know Before You Go now says "as of November 2026".
- "Come" wording removed on the FAQ, private events and events pages ("COMING SOON" became "STARTING SOON"). Em dash removed on the privacy page.

## Needs Davey
1. **Private sauna gift card** (shop page and the prices page link): it says "One weekday private, up to 10 guests, $449". That's the old private price and the old 10-guest cap. The new Group Session is $350 for 1 hr or $500 for 2 hr, up to 12. Decide what the Periode gift card should sell after the 11/23 switch, then update both the card and the page.
2. **Memberships has no way to join.** Every "Join" button goes to a "joining opens soon" email box. Either ship the Periode member link or relabel the buttons "Join the waitlist" on the home, prices and memberships pages.
3. **Launch blocker:** every page carries noindex, via a meta tag in each page plus `X-Robots-Tag` in `_headers`. That's right for pages.dev, but both must come off at the ebbandember.com cutover or Google lists nothing.

## Should do
- Put "4.9 on Google, 139 reviews" right under the home page hero buttons.
- First Plunge: link "Take the plunge" straight to the First Plunge product in Periode instead of /#today. Make "Two people $180" say "3 visits each". Mention the 18+ rule near "bring a friend".
- Private events: add a "from $X" price anchor, a CTA after the add-ons list, and "we reply within 1 business day". Check that sauna@ is watched, since the mailto goes there.
- Door code: add "Code not working? Text (503) 308-1293" to Know Before You Go and the booking-day copy.
- Cancellation: the sessions page and home page show only the 1-hour rule. Add one line for Group Sessions (cancel 48 hours before, move up to 3 hours before).
- Memberships hero says "As low as $80/mo", but the plan card leads with $100. Pick one framing.
- Shorten 20 page titles over 65 characters, home, prices and private saunas first. Trim 15 meta descriptions that are slightly long.

## Could do
- Events: add "Tell me when it starts" email capture on the starting-soon cards.
- Shop: say how the gift card arrives (email, minutes) and add a "send as a gift" note.
- Use one phrase for where guests rest: "covered deck or roof", not "rooftop or the landing".
- Make the transit info match: the FAQ lists bus 11 and bus 6, Know Before You Go lists bus 11 only.
- Home page: put the Group Session card ahead of the East/West "opening in December" card.
- Prices comparison table: label which plan each billing row belongs to.
- Add a "Book" bar that stays on screen on phones (sessions, home).
