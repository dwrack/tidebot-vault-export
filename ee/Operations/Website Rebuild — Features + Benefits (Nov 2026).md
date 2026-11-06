# Website Rebuild: Features + Benefits (Nov 2026)

Status 2026-11-03: preview at ebb-and-ember-site.pages.dev (password), noindex until launch. New prices go live Mon 11/23, announce 11/15. Shared doc for Jonah + L: https://claude.ai/artifact/QiBVT1yFMHm4KzEWYtXbZN

## Shared table (what is on the doc)

### Booking
| Feature | What it does | Why it matters |
|---|---|---|
| Book without leaving the site | Every Book button opens Periode checkout in a panel on ebbandember.com, full screen on phones | No hand-off to a different-looking site, fewer people lost at the jump |
| Live open seats | Homepage shows the next 3 days of socials with real seats left, refreshed about every minute from Periode | Guests see what is actually open; "2 seats left" is true, not a gimmick |
| Seat picker before checkout | Seats, 1 hr vs 2 hr, promo or gift code field, all on our page | Fewer clicks inside Periode |
| Periode warms up in the background | Loads quietly after the page finishes, or on first hover | Checkout opens in a second or two instead of 8 to 10 |
| One button per product | Social, Banya Monday, Friday, Private, each straight to the right Periode product | No hunting through a list |
| All-in prices on the page | $35/$50 weekday, $45/$60 evenings and weekends, 2 hr for $15 more, no last-step fees | Site standard: price never gated, never a surprise |
| Gift cards | Social $49 to $295 and weekday Private $449, bought through Periode | Shop works without a cart system |
| Member note | "Sign in on the next screen for your member price" | Members are not confused by guest prices |

### Pages
| Page | What is on it |
|---|---|
| Home | Hero, Today's socials, First Plunge, find your ritual, Private Saunas preview, how it goes (short loops), know before you go, reviews, weekly events, FAQ, email signup |
| /memberships | Daytime and Anytime plans, 3 and 12 month, "does it pay for itself" math, First Plunge as the on-ramp |
| /private-saunas | Private Saunas 1 and 2, pricing, whole-boat party, waitlist form, concept renders labeled as such |
| /events | Banya Mondays, Industry Happy Hour, Women + Femme Night, Silent Night, Sunrise Swim, host your own |
| /faq | Five groups, FAQ schema |
| /columbia-river | Live river temp (USGS gauge) and PDX air temp, month by month temps, ladder of cold, how to plunge |
| /shop | Gift cards |
| /best-saunas-portland | Local's honest guide, comparison page for search |
| Privacy, terms, 404 | Done |
| Old links | Squarespace URLs redirect (/home, /fitness, /wellness, /joinus, /cart) |

### Capture
| Feature | What it does | Why it matters |
|---|---|---|
| Email signup | Rain days, open seats, occasional update; one click unsubscribe | List grows from the site, not just IG |
| Waitlists | Private sauna waitlist and membership waitlist forms | Demand on record before the new saunas open |
| First Plunge band | $99, 3 visits in 45 days, counts toward a membership | Clear first step for a new guest |
| Spam guard | Honeypot, dedup, text-us fallback if the form fails | Clean list, no lost signups |

### Speed + search
| Measure | Old Squarespace site | New site |
|---|---|---|
| Lighthouse mobile performance | 73 | 99 |
| Accessibility | | 100 |
| Best practices | | 100 |
| SEO | | 100 once indexing is on (69 now, only because of the launch hold) |
| Desktop performance | | 97, hero paints in about 1.1 s |

| Feature | Why it matters |
|---|---|
| Static pages on Cloudflare's edge | No Squarespace renderer or plugins; pages load from the nearest server |
| WebP images at 3 sizes, lazy loaded | Phones download small files; desktop still gets the 2400 px version |
| Fonts no longer block | Text shows at once, Basal swaps in |
| Videos load only when played | Loops do not slow the first paint |
| FAQ and LocalBusiness schema | Google gets hours, location, FAQ answers in structured form |
| Search-aimed titles | "Portland floating sauna", "Columbia River temperature today", "sauna gift cards Portland" |
| Sitemap + robots | Ready for launch |

### Tracking
| Feature | Why it matters |
|---|---|
| GA4, Google Ads, Meta pixel on every page | One file, only fires on ebbandember.com |
| Ad click carried into Periode | fbclid, gclid, utm and GA4 session ride along, so a purchase credits the ad that caused it |
| Periode purchase events on all 4 products | Social, Private, Banya, Friday all report to GA4 and Meta server side |
| GA4 fixed | Periode no longer counts as a referral; session timeout 4 h so a slow checkout stays one visit |
| On-page events | Book clicks, checkout opened, booking complete, email lead, phone/email taps, which FAQ questions get opened |

### Brand
| Feature | Why it matters |
|---|---|
| Charcoal, sand, copper palette; Basal headings, Inter body | Matches the dock and the socials |
| Hero: friends in the cedar sauna, "Take the ladder" | One photo, one line |
| "Hot. Cold. Repeat." band with 4.9 Google rating and two reviews | Proof up high |
| Know before you go stays visible | No lifeguard, buddy, ladder, no alcohol, waiver |
| Copy rules | No "come", not wood-fired, Portland and Columbia River wording, "docked" |
| Phone-first layout | Menu hides on scroll, flame-only logo on small phones, checkout full screen |

## Davey only: what we could and probably should do later

Flagged as important before launch:
1. Sitemap is missing /best-saunas-portland, /privacy, /terms. Two-minute fix, do it at launch.
2. Launch steps still on hold by your call: Periode key as a Cloudflare secret, drop the noindex meta and header.
3. Hero photo: river-side wide shot with the sauna in focus still owed (Jonah's camera). Paddleboard shot is the stopgap.
4. Homepage order to the 11/2 agreed layout, and "New on the dock" as its own band.
5. Banya product in Periode to $65 on 11/23 with the rest of the switch.

Later, roughly in the order I would do them:
6. Sauna Credit band (spend $200 get $240, $400 get $500) on /shop and the homepage. In the plan, not built.
7. First Plunge lifecycle: post-visit text (needs A2P + your OK), "10 days left" email around day 35, month-2 member nudge to the 12-month plan.
8. Periode checkout add-ons: 1 hr to 2 hr upsell, "a private costs less" at 4+ seats, First Plunge block in confirmation emails. Need to ask Erik whether Periode supports any of it.
9. A matching review on each booking page (group review on Private, solo review on Memberships).
10. Rain-day homepage banner: when PDX forecast is rain, swap the hero line and push Downpour. The weather feed is already on the page.
11. "Seats left today" surfaced outside the site: IG bio link page, Google Business post, Slack alert to the team at 45% and 70% fill (ad pacer already does the math).
12. Abandoned checkout follow-up if Periode exposes it; otherwise a GA4 audience for Meta retargeting of checkout_open without booking_complete.
13. Event pages as their own URLs with Event schema (Banya Mondays, Sunrise Swim) so they show as events in Google.
14. Pick Your Sky (sunset and moon week view), parked in ~/dev/ee-parked.
15. /neighbors page (floating homes, slips, zips). Undecided, leaning scratch.
16. AI search prep: llms.txt and short answer blocks at the top of FAQ and river pages.
17. Photo library AI tagging (sunrise, sunset, people, no people) to feed the site and socials.
18. A/B tests from Funnel Lab once there is traffic (hero line, First Plunge price framing, 1 hr vs 2 hr default).
19. Cloudflare Access instead of basic auth on the preview, Cloudflare login for Jonah under sauna@, GitHub repo for Jonah's Claude.
