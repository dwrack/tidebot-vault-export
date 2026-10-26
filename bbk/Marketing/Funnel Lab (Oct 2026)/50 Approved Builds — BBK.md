# Approved builds: BBK (cards c12, c13, c02)

*Drafted 2026-10-15 by the BBK funnel session. DRAFT. Nothing below is live, published, sent or spending. Every number is "verified 2026-10-15" unless marked [VERIFY].*

Board picks this file builds: c12 bat page rebuild vs straight to booking (both), c13 honest water line vs none (both), c02 where cold social lands (waiting on David, drafted both ways anyway so it can start the day he picks).

## What I checked live today (2026-10-15)

| Fact | Live value | Source |
|:-|:-|:-|
| Bat page Book button | FareHarbor item **619305 "Bats & Kayaks Tour"** (calendar, ref=buffalobayoukayak.com) | page HTML + FH public item API |
| Bat page duration | Quick Details says 2 hours, body says "3-hour adventure" | buffalobayoukayak.com/kayak-tours/houston-bat-bridge-kayak-tour |
| Tour name | Site: Houston Bat Bridge Kayak Tour. FareHarbor: Bats & Kayaks Tour. Press release: Sunset Skyline Bat Bridge Tour | three sources, three names |
| Bat bookings last 30 days (to 10/10) | 6 bookings, 12 pax, $768.58 | FareHarbor Reports/2026-10-10 |
| Same-day bookings | 48% of all BBK bookings; Sat median lead time 0 days | same report |
| Meta "Bat Bridge Kayak Tour - Traffic" campaign | **ACTIVE, $20/day**, link-click optimized, 3 video ads, $597 spend last 30d, 5,311 link clicks, 3,385 landing page views, 0 purchases reported | facebook MCP |
| Best bat ad | "The Spectacle (Bats from Kayak)": $523 spend, 5.07% outbound CTR, $0.175 per landing page view, 23,000 video views | facebook MCP |
| Meta pixel on the site | 381452300055179 (33 Purchase events 9/17 to 10/14). Shared pixel 1559188957448084 fires 356 Purchases in the same window but mixes HPB and LSKT | page HTML + pixel stats |
| GTM | GTM-TKMN5XSX loads on every page. No Custom HTML tags (per the 03 infra doc). Publish access still unknown | page HTML |
| GA4 tags on the page | G-2CHJ9R6QSF, G-9J1S6JCPVY, G-CGV97LY2NK (one is property 370861451) [VERIFY which] | page HTML |
| Lead engine for BBK | enabled=false, no /avail or /quiz live, so no live tour times can be pulled onto the page yet | 02 Baseline |

Why this matters for the bat test: the bat tour sells 6 bookings a month while $600 of ads push 3,400 people a month onto its page. Even if every bat booking came from the ads, that is $597 for $769 of revenue. The landing page is not the only problem, but it is the one we can split today.

---

## Card c12: Bat landing page, rebuild (A) vs straight to booking (B)

Both arms run inside GTM. No WordPress edit needed, so the whole test can be unpublished in one click. 50/50 by a 30-day cookie.

### Arm A: the rebuilt first screen (injected above the existing page)

Phone first. This block sits above the current hero. Everything below it is today's page, unchanged.

```
HOUSTON BAT BRIDGE KAYAK TOUR

300,000 bats leave the Waugh Bridge at dusk.
You watch from a kayak, skyline behind them.

$60 a person  |  Ages 7+  |  About 2 to 3 hours [VERIFY: pick 2 or 3]
Leaves from 1019 Commerce St, downtown. No experience needed.

Tours leave about an hour before sunset. Tap for this week's dates.

[ Book the bat tour ]

"Totally different view of the city from the water!"
```

Below the button, three short blocks replace nothing, they just sit between the first screen and the old copy:

```
What happens
Paddle out at golden hour, past the skyline. Hold on the water near the
bridge as it gets dark. The colony comes out over your head.

First time in a kayak?
Most people on this tour are. Life vest, paddle and a quick lesson are
included. "As a first timer, she absolutely eased my anxiety."

The bats are wildlife
They live under the bridge all year. Emergences are common at dusk and
biggest in summer and early fall, thinner in deep winter, never guaranteed.
[VERIFY season wording with David, see open question 1]
```

The Book button links to `https://fareharbor.com/embeds/book/buffalobayoukayak/items/619305/calendar/?ref=bbk-batA&full-items=yes`. The `ref` lands in the FareHarbor booking's Online Booking Reference, so purchases per arm can be counted in the FH report without GA4.

### Arm B: skip the page

Visitors assigned to B are sent straight to `https://fareharbor.com/embeds/book/buffalobayoukayak/items/619305/calendar/?ref=bbk-batB&full-items=yes` before the page paints. Same ref trick for counting.

### Measure

| Metric | Where it's read |
|:-|:-|
| Book-form views per visitor (primary) | GA4 view_book_form split by the `ab_bat` event the tag pushes, or by FH ref |
| Purchases per arm | FareHarbor Advanced Bookings report, Online Booking Reference contains `bbk-batA` / `bbk-batB` |
| Bounce from the FH calendar (B's risk) | GA4 engagement on fareharbor.com pages for ref=bbk-batB |

At ~4,900 bat-page sessions a month this reads in 2 to 3 weeks. Stop rule: if B's purchases per visitor are below half of A's after 10 days, stop B.

### The GTM build (paste-ready, not published)

**Variable 1.** Type: 1st Party Cookie. Name `ck - bbk_ab_bat`. Cookie name `bbk_ab_bat`.

**Variable 2.** Type: Custom JavaScript. Name `js - bat bucket`.
```js
function() {
  var c = {{ck - bbk_ab_bat}};
  if (c === 'A' || c === 'B') return c;
  var b = Math.random() < 0.5 ? 'A' : 'B';
  var d = new Date(); d.setTime(d.getTime() + 30*24*60*60*1000);
  document.cookie = 'bbk_ab_bat=' + b + '; expires=' + d.toUTCString() + '; path=/; SameSite=Lax';
  return b;
}
```

**Trigger.** Type: Page View, Initialization (fires before the page paints). Name `pv - bat page`. Condition: Page Path contains `/kayak-tours/houston-bat-bridge-kayak-tour`.

**Tag 1: the redirect (arm B).** Type: Custom HTML. Name `AB bat - B redirect`. Trigger `pv - bat page`.
```html
<script>
(function(){
  if ({{js - bat bucket}} !== 'B') return;
  if (/[?&]noab=1/.test(location.search)) return;   // escape hatch for staff
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'ab_bat', ab_variant:'B'});
  location.replace('https://fareharbor.com/embeds/book/buffalobayoukayak/items/619305/calendar/?ref=bbk-batB&full-items=yes');
})();
</script>
```

**Tag 2: the rebuilt first screen (arm A).** Type: Custom HTML. Name `AB bat - A first screen`. Trigger: Page View, DOM Ready, same path condition.
```html
<script>
(function(){
  if ({{js - bat bucket}} !== 'A') return;
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'ab_bat', ab_variant:'A'});
  var book = 'https://fareharbor.com/embeds/book/buffalobayoukayak/items/619305/calendar/?ref=bbk-batA&full-items=yes';
  var html = ''
   + '<section id="bbk-ab-bat" style="padding:20px 16px;background:#fff;font-family:inherit;max-width:720px;margin:0 auto">'
   + '<h1 style="margin:0 0 8px;font-size:28px;line-height:1.15">Houston Bat Bridge Kayak Tour</h1>'
   + '<p style="margin:0 0 12px;font-size:18px">300,000 bats leave the Waugh Bridge at dusk. You watch from a kayak, skyline behind them.</p>'
   + '<p style="margin:0 0 6px;font-weight:600">$60 a person &nbsp;|&nbsp; Ages 7+ &nbsp;|&nbsp; About 2 to 3 hours</p>'
   + '<p style="margin:0 0 12px">Leaves from 1019 Commerce St, downtown. No experience needed.</p>'
   + '<p style="margin:0 0 14px">Tours leave about an hour before sunset. Tap for this week\'s dates.</p>'
   + '<a href="' + book + '" class="a-button" data-ab="bat-A" style="display:block;text-align:center;padding:16px;font-size:18px;font-weight:700;border-radius:8px">Book the bat tour</a>'
   + '<p style="margin:14px 0 0;font-style:italic">&ldquo;Totally different view of the city from the water!&rdquo;</p>'
   + '</section>';
  var main = document.querySelector('main') || document.body;
  main.insertAdjacentHTML('afterbegin', html);
  // hide the old first-row CTA so there is one Book button on the first screen
  var old = document.querySelector('a[data-mixpanel="first-row-cta"]');
  if (old) old.style.display = 'none';
})();
</script>
```
Styling note: the inline styles are a placeholder so the block renders on day one. Match the site's button color once someone with GTM access previews it. The three "below the button" blocks can go in the same tag as a second `insertAdjacentHTML` once the first screen is approved; kept out of v1 so the test changes one thing.

**Tag 3: GA4 event.** Type: GA4 Event. Event name `ab_bat`. Parameter `ab_variant` = `{{dlv - ab_variant}}` (Data Layer Variable). Trigger: Custom Event `ab_bat`. Measurement ID: the one for property 370861451 [VERIFY in GA4 Admin, it is one of G-2CHJ9R6QSF, G-9J1S6JCPVY, G-CGV97LY2NK].

**Publish.** Needs GTM publish access on GTM-TKMN5XSX [VERIFY who]. Preview first with `?noab=1` off and on. Nothing goes live until David says go.

---

## Card c13: Honest water line (A) vs none (B)

Runs on every `/kayak-tours/` page, including the bat page (arm B of the bat test leaves before this matters, so no clash). Separate 30-day cookie `bbk_ab_water`, 50/50.

### The line (arm A)

Placed directly above the first Book button:

> This is a working urban bayou in the middle of Houston. The water's brown, the skyline's huge, and the herons don't mind.

Alternate wording if David wants it shorter:

> Heads up: this is a city bayou. The water is brown, the skyline is huge, the herons don't mind.

### Measure

| Metric | Where |
|:-|:-|
| Book taps per visitor by arm (A may lose a few) | GA4 event `book_tap` with `ab_water`, pushed by a click trigger on `.a-button` |
| 1 to 3 star reviews mentioning water (A should drop) | Monthly review pull. Reviews can't be split by arm directly, so the Book links carry `ref=...wtrA/wtrB` and Connor matches low-star reviewer names to bookings once a month |

Read over a season. Stop rule: if A's Book taps per visitor fall more than 25% behind B after 3 weeks, pause and rethink the wording.

### GTM build (paste-ready, not published)

Variables: `ck - bbk_ab_water` (1st Party Cookie, `bbk_ab_water`) and `js - water bucket` (same Custom JavaScript as the bat bucket with the cookie name swapped).

Trigger `pv - tour pages`: Page View, DOM Ready, Page Path contains `/kayak-tours/`.

Tag `AB water - A line`: Custom HTML.
```html
<script>
(function(){
  var v = {{js - water bucket}};
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({event:'ab_water', ab_variant:v});
  // tag every FareHarbor book link with the arm so purchases carry it
  var links = document.querySelectorAll('a[href*="fareharbor.com/embeds/book/"]');
  for (var i=0;i<links.length;i++){
    var h = links[i].href;
    links[i].href = h + (h.indexOf('ref=')>-1 ? '-wtr'+v : (h.indexOf('?')>-1?'&':'?')+'ref=bbk-wtr'+v);
  }
  if (v !== 'A') return;
  var cta = document.querySelector('#bbk-ab-bat a.a-button') || document.querySelector('a[data-mixpanel="first-row-cta"]');
  if (!cta) return;
  var p = document.createElement('p');
  p.id = 'bbk-ab-water';
  p.style.cssText = 'margin:0 0 12px;font-size:16px;line-height:1.4';
  p.textContent = "This is a working urban bayou in the middle of Houston. The water's brown, the skyline's huge, and the herons don't mind.";
  cta.parentNode.insertBefore(p, cta);
})();
</script>
```
Plus a Click trigger (Just Links, Click URL contains `fareharbor.com/embeds/book`) feeding a GA4 Event `book_tap` with `ab_water` = `{{js - water bucket}}` and `ab_bat` = `{{js - bat bucket}}`.

The same line is already in every BBK quiz result blurb (engine/quiz/bbk.json), so the quiz is arm A of this test by default.

---

## Card c02: Where cold social lands (BBK), both arms as PAUSED drafts

Board: waiting on David. Drafted both ways so either can be built the day he picks. These are specs to build in Ads Manager as PAUSED (the facebook MCP cannot create Instant Forms or native A/B studies, so the forms and the split are UI steps). No campaign exists yet; nothing has been created in the account.

**Budget.** $10/day for 21 days, $210 total, carved out of the current $20/day Traffic campaign (my pick: pause Traffic for the test window so total BBK Meta spend drops, not rises). David confirms before anything is created.

**Audience, both arms.** Houston +20 miles, 21 to 55, home and recent, Facebook and Instagram, Advantage audience off. Same as today's bat ad set so the comparison is clean. Exclude pixel 381452300055179 purchasers 30 days.

**Creative, both arms.** Reuse the "The Spectacle (Bats from Kayak)" video (creative 989774553711284). It is the account's proven asset: 5.07% outbound CTR, 23,000 video views for $523.

### Arm A: cold ads go to a lead step

Campaign `BBK | c02-A | Lead | Who's paddling` (PAUSED). Objective Leads, Instant Form, optimize for Leads. $5/day.

Primary text:
```
300,000 bats leave the Waugh Bridge at dusk. We paddle you under them.

Houston's only bat kayak tour. $60 a person, ages 7+, no experience
needed, leaves from downtown about an hour before sunset.

It's a working city bayou: brown water, huge skyline, herons that don't
mind. Tell us who's paddling and we'll send the right tour, the price and
this week's dates.
```
Headline: `Who's paddling?`  Description: `Bat tour, $60, downtown Houston`  CTA: `Get offer` (or `Learn more`).

Instant Form "Who's paddling? (BBK)":
- Intro: "One tap and we'll send the tour that fits, with price and this week's dates."
- Q1 (multiple choice): Who's paddling? `A date` / `Friends` / `Family with kids` / `Just me`
- Q2 (multiple choice): Ever kayaked? `Never` / `A few times` / `Lots`
- Contact: Email (required), Phone (optional, label "Text me the dates instead")
- Privacy policy link: buffalobayoukayak.com privacy page [VERIFY URL]
- Thank-you screen: "Got it. Check your inbox in a minute. Want to skip ahead? Here's the bat tour calendar." Button → FareHarbor item 619305 with `ref=bbk-c02A`
- Lead delivery: CSV download or the engine's lead endpoint once BBK is enabled [VERIFY]. Until then Connor emails leads the quiz result copy by hand within 24h (batch, not drip).

Retargeting ad set inside the same campaign (PAUSED): Custom Audience "Instant Form opened or submitted, 30d", objective Sales, optimize Purchase on pixel 381452300055179, $1/day, landing on FareHarbor item 619305 `ref=bbk-c02A-rt`. Copy: "Still thinking about the bats? Dates for this week are open." plus the proof line.

### Arm B: cold watches, warm books

Campaign `BBK | c02-B | ThruPlay | Bat reel` (PAUSED). Objective Engagement (video views), optimize ThruPlay. $3/day.

Primary text (short, it's a watch ad):
```
This is 3 miles from downtown Houston. Most people who live here have
never seen it.
```
No link, no CTA button. Same Spectacle video.

Campaign `BBK | c02-B | Sales | Warm viewers` (PAUSED). Objective Sales, optimize Purchase on pixel 381452300055179. Audience: Custom Audience "Watched 50% of Spectacle video, 30d" plus "Watched 95%, 30d". $2/day. Landing: FareHarbor item 619305 `ref=bbk-c02B`.

Primary text:
```
You watched the bats. Here's how to be under them.

$60 a person, ages 7+, downtown launch, about an hour before sunset.
Brown water, huge skyline, no experience needed.

"Totally different view of the city from the water!"
```
Headline: `Book the bat tour`  CTA: `Book now`.

### Measure (both arms, 21 days)

| Metric | A | B |
|:-|:-|:-|
| Cost per lead | Meta | n/a |
| Cost per Book-form view | GA4 view_book_form from ref=bbk-c02A / A-rt | from ref=bbk-c02B |
| Cost per booking | FareHarbor ref report | FareHarbor ref report |
| Sanity | leads emailed within 24h (Connor) | 50% viewer audience size reaches 1,000+ in week 1 |

My pick stands: run both. A tests "no intent", B tests "no trust". Current data can't tell them apart.

---

## Things David decides before any of this goes live

See the numbered list in the chat reply and in 00 Start Here (Status 2026-10-15). The ones this file depends on: tour length (2 or 3 hours), bat season wording, GTM publish access, budget carve-out, and whether to pause the live $20/day Traffic campaign.
