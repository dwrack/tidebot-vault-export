# Website Comb-Through (2026-11-21)

Full-site review of the new static site (repo `~/dev/ee-site-preview`, GitHub `dwrack/ebb-and-ember-site`, live at https://ebb-and-ember-site.pages.dev), captured at commit 3370451 on 2026-11-21 at 390px, 960px (Davey's Chrome zoom) and 1440px.

- Review page with before/after pictures and Approve / Deny / note per item: https://claude.ai/artifact/1xfCVFXzRkdaoAsZXBKgEE
- Davey's marks live in that artifact's database, collection `decisions`, doc `f01`..`f34` (`status` approve/deny/empty, `note`). Read them with ArtifactData before applying anything.
- STATUS 2026-11-21: nothing applied. Each fix waits on his Approve. Save path tested 11/21 (mark + note round-tripped to the db and back after reload; test mark cleared, so doc f01 may exist with empty status).
- Items 30 to 34 have no patch: they need his wording, photo picks or a redraw first.
- How to apply: `git pull --rebase origin main`, add the CSS below to the pages listed (site-wide ones via a checked scripted replace like `tools/apply_nav.py`), commit, push to main (auto-deploys), check live, log the decision row.
- Dropped after mock-up: sticky first column on the best-saunas comparison table (no visible gain).

## Fix before launch

### 1. Footer is crushed on desktop

- Pages: Every page, 900px and wider. Phones are fine.
- Problem: The address, phone and blurb are squeezed into a column about 75px wide, so they wrap one or two words per line and the footer runs about 650px tall. The links sit at the bottom right with empty space above them.
- Fix: Give the address block a real column (up to 340px) and set the links in three tidy columns beside it, both aligned to the top.
- Patch (mock 01, shown on `/sessions/`):

```css
@media (min-width:900px){.foot{grid-template-columns:minmax(0,340px) minmax(0,1fr);align-items:start;column-gap:72px}.foot nav{display:grid;grid-template-columns:repeat(3,max-content);gap:14px 48px;justify-content:end}}
```
- SCOPE: site-wide footer CSS, all 37 pages with the shared header/footer (index-v2.html and photos.html are old internal pages, skip).
- Decision: open

### 2. Book button lands with the heading hidden

- Pages: Home (Book, Find Your Ritual and other jump links), Memberships (plans link). All widths.
- Problem: Tapping Book in the header jumps to Today On The River, but the heading ends up underneath the fixed header. You land mid-card and can't see where you are.
- Fix: Add a scroll offset to every jump target so it stops 20px below the header.
- Patch (mock 02, shown on `/`):

```css
[id]{scroll-margin-top:calc(var(--hdr,64px) + 20px)}
```
- SCOPE: safe site-wide; needed on home and memberships.
- Decision: open

### 3. Journal buttons: unreadable text

- Pages: 21 journal pages: every article and month guide, plus the date buttons in the guides.
- Problem: Copper buttons in the journal have cream text instead of the dark text used everywhere else. Contrast is 2.3 to 1, well under the 4.5 minimum. Button labels on the journal index and the guide date buttons are also underlined like links.
- Fix: Use the same dark button text as the rest of the site and remove the underline.
- Patch (mock 03, shown on `/blog/portland-in-december/`):

```css
.art a.btn,.art a.btn:hover{text-decoration:none}.art a.btn:not(.ghost){color:var(--bg)}
```
- SCOPE: journal pages only (the 21 pages under /blog/ that use `.art`).
- Decision: open

### 4. Month guide weather tiles are cut off

- Pages: All 12 month guides.
- Problem: The first number (46.9°/36.2°) runs past its tile and loses its last digit. The daylight tile wraps to three lines and drops to a row by itself.
- Fix: Two wide tiles on top, three below, numbers at one size that always fit on one line.
- Patch (mock 04, shown on `/blog/portland-in-december/`):

```css
.post .facts{grid-template-columns:repeat(6,minmax(0,1fr))}.post .facts div,.facts div:first-child{grid-column:span 2}.post .facts div:nth-child(-n+2){grid-column:span 3}.post .facts b,.facts div:not(:first-child) b{font-size:20px!important;line-height:1.15;white-space:nowrap}.post .facts div{display:grid;align-content:space-between;gap:12px;min-height:88px}@media (max-width:599px){.post .facts{grid-template-columns:repeat(2,minmax(0,1fr))}.post .facts div,.post .facts div:nth-child(-n+2){grid-column:auto}.post .facts div:first-child{grid-column:1/-1}.post .facts b,.facts div:not(:first-child) b{font-size:19px!important}}
```
- Decision: open

### 5. Articles have no space between paragraphs

- Pages: All 21 journal posts.
- Problem: Paragraphs run together with no gap, the byline sits on top of the intro, and the intro sits on the note below it. Long posts read as one block.
- Fix: 16px between paragraphs, 20px under the byline and intro, more room above each heading, and a thin rule above the Sources line.
- Patch (mock 05, shown on `/blog/best-saunas-portland/`):

```css
.art p{margin:0 0 16px}.post .meta{margin:0 0 20px}.post .lede{margin:0 0 22px}.art h2{margin:48px 0 14px}.art h3{margin:32px 0 10px}.art ul{margin:0 0 16px}.post .src{margin-top:32px;padding-top:16px;border-top:1px solid var(--line)}.art-fig{margin:28px 0}.post .cta p{margin:0 0 16px}
```
- Decision: open

### 6. Privacy and Terms are a wall of text

- Pages: Privacy, Terms of Service.
- Problem: Every section runs straight into the next with no spacing, so about 800px of policy is one block.
- Fix: Space between paragraphs and extra room before each bold section lead-in.
- Patch (mock 06, shown on `/privacy/`):

```css
main p{margin:0 0 16px}main p:has(>b:first-child),main p:has(>strong:first-child){margin-top:28px}
```
- SCOPE: Privacy and Terms pages ONLY. `main p{...}` applied anywhere else would re-space every page.
- Decision: open

### 7. Seat widget footnote is squeezed

- Pages: Home, desktop widths.
- Problem: "Live seat counts from our booking system. Every open time:" is crushed into a narrow three-line column beside the Social, Private and Banya links.
- Fix: Let the sentence run full width with the links following it on the same lines.
- Patch (mock 08, shown on `/`):

```css
.live-src{display:block;line-height:1.7}.live-src .live-dot{display:inline-block;margin-right:8px;vertical-align:middle}.live-src a{margin-left:10px;white-space:nowrap}
```
- Decision: open

### 8. Prices break in the middle

- Pages: Sessions, Private Saunas and Know Before You Go fact lists, at your zoom and on phones.
- Problem: The evening price breaks as "$45 for 1 hr · $60" then "for 2 hr", and on phones the weekday price leaves "hr" alone on a line. The label takes the room the price needs.
- Fix: The price always stays on one line; the label wraps instead.
- Patch (mock 09, shown on `/sessions/`):

```css
.x-facts dt{flex:1 1 0;min-width:0}.x-facts dd{flex:0 1 auto;max-width:64%;text-align:right}
```
- Decision: open

### 9. River page: temperature labels crushed on phones

- Pages: Columbia River page, phones.
- Problem: Labels like "Warmest river day, Aug 26, 2025" are squeezed into a 60px column and wrap to four lines beside each big number.
- Fix: On phones, put each label under its number.
- Patch (mock 28, shown on `/columbia-river/`):

```css
@media (max-width:599px){.rung{grid-template-columns:1fr;gap:4px}}
```
- Decision: open

### 10. Empty space beside the seat widget

- Pages: Home, desktop widths.
- Problem: The left column ends about 500px before the seat widget does, leaving a blank charcoal block. First Plunge only starts below. Your Nov 2 section order has today's sessions beside First Plunge.
- Fix: Move the First Plunge card up into the left column so the two columns end together.
- Mock script (mock 17, shown on `/`), describes the markup change:

```js
(()=>{const f=document.getElementById('first'),i=document.querySelector('.top-grid .intro');if(f&&i){i.appendChild(f);f.classList.remove('wrap','gut');f.style.cssText='padding:0;margin:12px 0 0'}})()
```
- SCOPE: NOT a CSS patch. Markup move in index.html: move the `#first` First Plunge section into `.top-grid .intro`, drop its `wrap gut` classes, set padding 0 and margin 12px 0 0. Check phone order after the move.
- Decision: open

### 11. Instagram block looks unfinished

- Pages: Journal index.
- Problem: Until our own Instagram tiles are switched on, the three embeds show as Instagram's white cards (or as bare text links while they load) on a dark page. It is the loudest thing on the page.
- Fix: Hide the three embeds until our own tiles are live, and keep the heading and the Follow button.
- Patch (mock 07, shown on `/blog/`):

```css
.ig-grid:not(.ig-live){display:none}.ig-follow{margin:16px 0 28px}
```
- SCOPE: journal index only; remove the hide rule once IG_TOKEN is set and `.ig-live` tiles render.
- Decision: open

## Alignment and layout

### 12. "From the journal" line is off the grid

- Pages: Sessions, Events, Private Saunas, Columbia River and others with that closing line.
- Problem: The line is indented about 100px from everything else and sits right on the footer rule with no space under it.
- Fix: Align it with the page edge and give it room above the footer.
- Patch (mock 11, shown on `/sessions/`):

```css
.blog-xl{max-width:1120px;margin:0 auto;padding:28px 20px 48px}
```
- Decision: open

### 13. Price cards stop short of the page edge

- Pages: Private Saunas (Pick Your Sauna). Same pattern on the Prices plan cards.
- Problem: The two cards end 180px before the right edge that every other block on the page uses, so it looks like a third card is missing.
- Fix: Let the two cards share the full width.
- Patch (mock 10, shown on `/private-saunas/`):

```css
.x-picks.two{max-width:none;grid-template-columns:1fr 1fr;gap:24px}
```
- Decision: open

### 14. Join buttons don't line up

- Pages: Memberships, desktop widths.
- Problem: The two plan lists are different lengths, so Join Anytime sits a few pixels higher than Join Daytime.
- Fix: Pin both buttons to the bottom of their column.
- Patch (mock 13, shown on `/memberships/`):

```css
.plans{align-items:stretch}.plan{grid-template-rows:auto auto auto auto 1fr auto}.plan .btn{align-self:end}
```
- Decision: open

### 15. Starting Soon cards: forms at different heights

- Pages: Events.
- Problem: Card text lengths differ, so the email boxes and Tell Me buttons sit at different heights across each row.
- Fix: Pin the email form to the bottom of each card.
- Patch (mock 14, shown on `/events/`):

```css
.x-card{display:flex;flex-direction:column}.x-card .in{flex:1 1 auto;display:flex;flex-direction:column;gap:10px}.x-card .in form.notify{margin-top:auto;padding-top:6px}
```
- Decision: open

### 16. Keep Reading leaves one lonely card

- Pages: All journal articles. The journal index sections end the same way.
- Problem: Four related posts in a three-column grid leaves the fourth alone on a second row with empty space beside it.
- Fix: Two by two, so every row is full.
- Patch (mock 15, shown on `/blog/best-saunas-portland/`):

```css
@media (min-width:600px){.rel-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
```
- Decision: open

### 17. Review quote stranded on the left

- Pages: Memberships, First Plunge, Private Events, Gift Cards, Events, Know Before You Go.
- Problem: The Google review sits in a half-width box against the left edge with nothing beside it.
- Fix: Center it at reading width.
- Patch (mock 12, shown on `/memberships/`):

```css
figure.g-review{max-width:760px;margin-inline:auto!important}
```
- Decision: open

### 18. Home reviews block is cramped

- Pages: Home.
- Problem: The 4.9 sits tight under the headline and reads like part of it. The one-line quote is stretched to match its neighbor, and the buttons are glued to the cards.
- Fix: Space under the headline, quotes sized to their text, room above the buttons. The headline also comes down from about 125px to 96px at this width.
- Patch (mock 16, shown on `/`):

```css
.statement h2{font-size:clamp(44px,9vw,96px)}.statement .stars{margin-top:20px}.statement .quotes{row-gap:32px;align-items:start}.statement .cta-row{margin-top:28px}
```
- Decision: open

### 19. "What you get" headings wrap raggedly

- Pages: Private Events.
- Problem: The four copper headings break onto two or three lines each, so the paragraphs under them start at different heights. "The lounge +" leaves a plus sign hanging.
- Fix: Smaller headings that fit in two lines, so all four paragraphs start level.
- Patch (mock 19, shown on `/private-events/`):

```css
.math.ev4 b{font-size:21px;line-height:1.2;min-height:2.4em;text-wrap:balance}
```
- Decision: open

### 20. Poem lines break mid-phrase

- Pages: First Plunge.
- Problem: The rain poem is held to a narrow column, so lines split as "steam lifting off your / shoulders." and "By the third visit, it's / yours."
- Fix: One line per beat, as written. Phones keep natural wrapping.
- Patch (mock 20, shown on `/first-plunge/`):

```css
.poem{max-width:none}.poem p{white-space:nowrap}@media (max-width:599px){.poem p{white-space:normal}}
```
- Decision: open

### 21. Photo rows: tall photos, floating text

- Pages: Memberships (What Members Get). Same rows on Sessions, Gift Cards and Know Before You Go.
- Problem: Three lines of text sit beside a 500px tall photo, so the section runs about 2,200px with big empty zones.
- Fix: Crop the photos to 4:3, center the text against them and tighten the gap. About 40% shorter.
- Patch (mock 21, shown on `/memberships/`):

```css
.x-rows{gap:48px}.x-row{align-items:center}.x-row:not(.wide) .ph{aspect-ratio:4/3;height:auto}.x-row:not(.wide) .ph img,.x-row:not(.wide) .ph video{width:100%;height:100%;object-fit:cover}
```
- Decision: open

### 22. Photo strip has no left margin on phones

- Pages: Sessions, Gift Cards. Phones.
- Problem: The swipeable photo strip starts hard against the screen edge while everything else is inset 20px.
- Fix: Start the first photo at the page margin and keep the next one peeking in on the right.
- Patch (mock 18, shown on `/sessions/`):

```css
.x-gal{padding-inline:20px;scroll-padding-inline:20px}
```
- Decision: open

## Polish

### 23. Pull quotes shout in all caps

- Pages: All journal articles and month guides.
- Problem: Full sentences are set in the all-caps display face, which your brand rules keep for short display lines.
- Fix: Set pull quotes in Inter, sentence case.
- Patch (mock 22, shown on `/blog/date-ideas-portland/`):

```css
.post blockquote{font:500 22px/1.45 var(--body);padding:4px 0 4px 24px;margin:40px 0;text-transform:none;letter-spacing:0}
```
- Decision: open

### 24. Prices page reviews have a doubled rule

- Pages: Prices (four reviews).
- Problem: Each review has an outer copper line and a second line on the inner box, so it reads as two nested blocks.
- Fix: Keep one.
- Patch (mock 26, shown on `/prices/`):

```css
figure.rv{border-left:0!important;padding-left:0!important;max-width:640px}
```
- Decision: open

### 25. River safety list is one long column

- Pages: Know Before You Go, desktop widths.
- Problem: Eleven bullets of equal weight in one wide box.
- Fix: Two columns on desktop. Same words, half the height.
- Patch (mock 27, shown on `/know-before-you-go/`):

```css
@media (min-width:768px){.safety ul{display:block;columns:2;column-gap:44px}.safety li{break-inside:avoid;margin:0 0 8px}}
```
- Decision: open

### 26. Closing headline leaves one word alone

- Pages: Columbia River. Same rule helps the other closing headlines.
- Problem: "SEE IT FROM THE" then "LADDER" on a line by itself.
- Fix: Balance the two lines.
- Patch (mock 29, shown on `/columbia-river/`):

```css
.rv-cta h2,.x-end h2{text-wrap:balance}
```
- Decision: open

### 27. Footer links are hard to tap on phones

- Pages: Every page, phones.
- Problem: The 13 footer links are 22px tall with 8px between them. Your build brief asks for 44px tap targets.
- Fix: Two columns with full-height rows.
- Patch (mock 23, shown on `/sessions/`):

```css
@media (max-width:899px){.foot nav{display:grid;grid-template-columns:1fr 1fr;gap:0 20px}.foot nav a{padding:11px 0}}
```
- Decision: open

### 28. 404 page buttons wrap unevenly

- Pages: 404 page, phones.
- Problem: Two buttons share a line and the third drops alone to a second row.
- Fix: Stack them full width, Book on top.
- Patch (mock 24, shown on `/this-page-does-not-exist`):

```css
@media (max-width:599px){.cta-row .btn{flex:1 1 100%}}
```
- SCOPE: 404.html ONLY (`.cta-row .btn` exists on other pages).
- Decision: open

### 29. Soft night photo, used in four places

- Pages: Home (full-width band), 404, Events hero, December guide.
- Problem: The night shot of the sauna is soft and noisy at full width and half of it is nearly black. It is the weakest image on each page it appears on.
- Fix: Swap it for a sharper one. Shown here on the home band with the pink sunset from the deck, which is already in the site library. Tell me if you'd rather pick a different photo for any of the four spots.
- Mock script (mock 25, shown on `/`), describes the markup change:

```js
(()=>{const i=document.querySelector('.bleed img');i.removeAttribute('srcset');i.src='/a/floating-sauna-pink-sunset-columbia-river-portland.webp'})()
```
- SCOPE: NOT a CSS patch. Photo swap; needs Davey's photo pick per spot (home band, 404, Events hero, December guide). Mock used /a/floating-sauna-pink-sunset-columbia-river-portland.webp on the home band only.
- Decision: open

## Needs your call, no picture

### 30. Sessions closing line reads like a leftover

- Pages: Sessions.
- Problem: Under the big HOT. COLD. REPEAT. at the bottom, the line says "Live seat counts from our booking system, right on the homepage." There is no seat widget on that page, so it reads as a stray note.
- Fix: Give me a replacement line, or say remove and I'll leave just the headline and the Book button.
- Decision: open

### 31. Three tiny text fixes

- Pages: Memberships, Privacy, Home.
- Problem: Memberships has a dangling dot after the "Private saunas" link with nothing after it. Privacy says "Phone:(503)" with no space. "Secure checkout by Periode" on the home widget is 11px, under your 12px minimum.
- Fix: Remove the dot, add the space, raise the line to 12px. Approve and I'll do all three.
- Decision: open

### 32. Home repeats the same photos

- Pages: Home.
- Problem: The deck photo is in both How It Goes and the Private Event Space card. The sauna sketch appears in Find Your Ritual and again full size in East and West Saunas. The couple on the roof deck is in the hero rotation and the Group Session card.
- Fix: Approve and I'll put replacement options from the ranked photo library in front of you to pick from.
- Decision: open

### 33. River temperature showed "n/a" once on a phone

- Pages: Home, top weather card. Seen in one of three captures.
- Problem: When the river reading doesn't load, the card shows "n/a" next to a real air temperature in the first screen.
- Fix: Hide the River Now cell when there's no reading, or show the last known value with its time.
- Decision: open

### 34. River map labels clipped on phones

- Pages: Columbia River page, phones.
- Problem: On the "Where the river starts" map, the Ebb & Ember label overlaps PACIFIC OCEAN and the Snake River label is cut off at the right edge.
- Fix: Needs the labels repositioned in the drawing for phone width. Approve and I'll redo them and show you.
- Decision: open
