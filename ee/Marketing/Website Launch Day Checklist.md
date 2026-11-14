# Website launch day checklist

Per Davey (2026-11-14): Periode setup waits until the day the new site goes live on ebbandember.com. Do these on that day, in this order.

## Periode (match it to the site)
- [ ] **Private sauna gift card:** the site's shop page and the experience gifts post still sell "One weekday private, up to 10 guests, $449". Replace it with the any-amount gift card (per Jonah's launch email) or a Group Session card at the new prices ($350 / $500 weekdays, up to 12), then update both pages to match.
- [ ] **Membership join link:** ship the Daytime and Anytime signup links and point every "Join" button at them. Today the buttons go to the "joining opens soon" email box.
- [ ] **First Plunge:** allow it on 1 and 2 hour Social, Ember 1 and Ember 2 times, and the Friday Sunrise Swim. The site says the Friday swim is included. Periode still excludes it. Also confirm how the $99 membership credit gets applied (asked Jonah and L in #dev).
- [ ] **Booking windows:** members book privates 90 days ahead, everyone else 60. Social is 21 days on the site but 45 in Periode today.
- [ ] **New prices live in Periode:** Social $35/$50 and $45/$60, Group Session $350/$500 and $450/$600, Banya $65 guided and $60 self-guided, Friday swim $25.

## Site cutover
- [ ] Remove `<meta name="robots" content="noindex,nofollow">` from every page.
- [ ] Remove `X-Robots-Tag: noindex, nofollow` from `_headers`.
- [ ] Point ebbandember.com at the Cloudflare Pages project. Check that robots.txt and sitemap.xml load from the live domain, then submit the sitemap in Search Console.
- [ ] Spot-check one booking from each product, plus the gift card checkout, on a phone.

## Related
- Open site work: Marketing/Website Sweep 2026-11-14.md
- Keyword plan: Marketing/SEO Month Guides Keyword Research 2026-11-14.md
