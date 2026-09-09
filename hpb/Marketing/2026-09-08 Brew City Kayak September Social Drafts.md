# Brew City Kayak: September Social Drafts
*Drafted 2026-09-08. Six posts, one week. Facebook Page + Instagram (@brewcitykayak).
Photos: `~/Desktop/BCK Photos/`. Voice: terse, matches BCK's own review replies, 1–2 sentences, no flourish.*

---

## The angle

Post-Labor Day is the strongest available story and nobody in the Milwaukee market uses it:
**the tourists are gone, the water is still warm, downtown is quiet.** September is the local's
month. That thread runs through all six.

---

## The posts

### 1 · Tue: the season shift
**Photo:** `IMG_7817.JPG` *(960×960, Hoan Bridge, dramatic sky, already square)*

> Labor Day's over. Water's still warm, the river's quiet, and downtown is basically yours.
>
> September is the local's month.

### 2 · Wed: see it from the water
**Photo:** `BCK7.jpg` *(1080×1080, the Solomon Juneau at water level)*

> The Solomon Juneau, from two feet off the water.
>
> You've walked past her a hundred times. She's a different boat from down here.

### 3 · Thu: the differentiator
**Photo:** `cheesecurdtour1.jpeg` *(1600×1200, curd box + Sprecher root beer, crop to square)*

> Paddle. Then curds. Then a Sprecher.
>
> The Cheese Curd Tour is exactly what it sounds like.

### 4 · Fri: groups
**Photo:** `BCK3.jpg` *(1080×1080, six paddlers, branded hulls, Hoan Bridge behind)*

> Six people. Five boats. One bridge.
>
> Get the group out before the season turns.

### 5 · Sat: golden hour
**Photo:** `Hoansunset.jpg` *(534×712, low res, see note)*

> Sunset comes earlier every week now. Turns out that's a feature.

### 6 · Sun: the monthly hook
**Photo:** `FullMoon.jpg` *(1980×1080 banner, see note)*

> Full Moon Tour. Monthly, and there aren't many left this year.
>
> The city looks completely different at night.

---

## Hashtags (reuse across all six)

`#MilwaukeeKayak #BrewCity #MKE #VisitMilwaukee #KayakMKE #MilwaukeeRiver`

---

## Check before posting

- **`FullMoon.jpg` may not be a Brew City asset.** It is a designed banner, not a photo, and the
  vegetation looks like a southern mangrove river rather than Milwaukee, it reads like it was
  built for another brand in the portfolio. Verify before it goes on the BCK page. Also 16:9, so
  it needs a crop for feed.
- **Post 6 claims "not many left this year."** Confirm against the actual Full Moon schedule.
  The banner says MONTHLY; the remaining-dates claim is unverified.
- **No prices, times, or dates anywhere in these drafts, deliberately.** The only pricing signal
  available was a customer comment on Facebook guessing the Cheese Curd Tour at $145, which is
  not a source worth repeating as fact. GA4 puts *average booking value* at $133.05, which is not
  the same thing as a list price.
- **`Hoansunset.jpg` is only 534×712**: soft on a retina feed. `IMG_7817.JPG` (960×960) is the
  same subject, better. Consider reusing it for post 5 and dropping `Hoansunset.jpg` entirely.

## Strongest two

**Posts 2 and 4.** `BCK7` has an actual point of view, the water-level angle on something locals
only ever see from the sidewalk. `BCK3` carries BREWCITYKAYAK.COM on the hulls, which is free reach.

---

## How to publish

Media cannot be attached by Claude, the Business Suite picker is a native OS dialog. Claude types
the caption; a human drags the photo in. See the `meta-business-suite-media-upload-is-manual` memory.

Fastest path for a batch this size is **Business Suite → Planner**, queueing all six in one sitting
rather than posting daily.

Alternative that removes the drag step entirely: the Graph API `/{page-id}/photos` endpoint accepts
a direct multipart file upload (Facebook only. Instagram still requires a hosted image URL). Needs
a Page access token with `pages_manage_posts` at `~/.config/meta/bck-page-token`.

## Reference

- Page: Brew City Kayak, `business_id=378089712667582`, `asset_id=151955085626575`
- Followers at drafting: 2K Facebook, 1.6K Instagram
- Ads account: CID 158-223-3197, login brewcitykayak@gmail.com, see
  [[2026-08-27 Brew City Kayak Google Ads Audit]]
- Open at drafting: 10+ unread comments, 11 unread messages, including a 3-week-old
  Cheese Curd Tour price question from a warm lead
