# Gator Collision: what is built and what you need to finish

Built 2026-09-22 in Ads Manager, account `act_87863118`. Everything below is **unpublished
draft**. Nothing is spending.

- Campaign: **NPB | Purchase | Gator Collision | Sept 2026** (`52578687844700`)
- Ad set: **Nightlife & Bars | 24-45 | NOLA 50mi** (`52578687844500`)
- Ad: **NPB | Gator Collision v1 | 9x16 video** (`52578687844300`)

Video master: `Assets/Ad Creative/npb-gator-collision-v1-1080x1920.mp4` (42MB)
Upload copy:  `Assets/Ad Creative/npb-gator-collision-v1-upload.mp4` (8MB, use this one)

---

## Already configured

| Setting | Value | Why |
|---|---|---|
| Objective | Sales | Traffic ran 0.18x on this account |
| Performance goal | Maximize number of conversions | Defaulted to *link clicks*, which is the losing setting |
| Conversion event | Purchase | |
| Dataset | GT Pixel- NPB, Kayak (`701301873334767`) | matches the vault |
| Budget | $40/day campaign budget | matches what your other Sales campaigns spend. **Change if you want** |
| Location | New Orleans +50mi | |
| Minimum age | 24 | product is 21+, brief targets 24-45 |
| Interest | Nightlife (bars, clubs & nightlife) | this is the 5.74x Party Bike Bar winner |
| Format | Single video | carousel ran 2.4x vs video's 4.5%+ CTR |
| Facebook Page | New Orleans Party Barge | |
| Instagram | nolapartybarge | |
| Landing page | nolapartybarges.com/the-freaky-tiki/ | |

## Three things Meta defaulted wrong that I changed

1. **Advantage+ catalog was ON** and auto-attached a catalog named **"Products for Door
   County Kayak Tours"**, a different business entirely. Turned off.
2. **Performance goal defaulted to "Maximize number of link clicks."** That is the
   optimization your own data says returns 0.18x. Changed to conversions.
3. **The ad was set to post as "New Orleans Kayak Swamp Tours" / @kayaknola.** Changed to
   New Orleans Party Barge / @nolapartybarge.

---

## What you need to do

### 1. Upload the video (I cannot do this one)

Meta's uploader opens a native macOS file picker with no DOM element behind it, so browser
automation cannot reach it. Same limitation as Business Suite media.

- Open the ad, **Ad creative → Set up creative → Video ad → Upload**
- Drag in `Assets/Ad Creative/npb-gator-collision-v1-upload.mp4`

### 2. Paste the text

**Primary text**

```
There's an alligator about twenty feet from the dance floor right now.

That's the ad. That's the whole thing.

Most swamp tours out here are a two hour round trip and you need a rental car to get there. We're seven miles from the French Quarter, off Paris Road. Fifteen minute Uber, and you're back before dinner.

Bring whatever you're drinking. Plug in your own playlist. The captain finds the gators, you handle everything else.

An hour and forty five minutes on the bayou. Covered, so a rainy forecast doesn't cancel your afternoon. Bathroom on board, which no other party boat in New Orleans can say.

4.9 stars, 3,800+ reviews, and the line that keeps showing up is "best part of our trip."

$63 a seat, or take the whole boat for your group at $1,250. Pick a date and we'll see you at the dock.
```

**Headline**

```
Gators. Your playlist. 15 minutes.
```

**Description**

```
$63 a seat. BYOB on the bayou. 4.9 stars, 3,800+ reviews.
```

**Call to action:** Book Now

### 3. Get yourself Advertiser role on the ad account (this blocks everything)

**Correction to what I first told you.** I originally guessed the `#1487194` permission
error came from cancelling the creative wizard. That was wrong. Trying to duplicate the ad
on 2026-09-22 returned the real cause:

> To create or edit ads for ad account 87863118, contact an admin to get permission with
> **Advertiser role or higher**. (#200.2490585)

You are logged in as Michael Fischer (`100002046915131`), and that user's role on
`act_87863118` is below Advertiser. Reading the account works, and the draft edits appear
to save because Ads Manager holds them in a local draft layer, but anything that actually
writes through the ads API is refused. That includes duplicating an ad, and very likely
publishing this campaign.

**Good news: you can fix this yourself, no one else needed.** Checked 2026-09-22.

The owning Business Manager is **Daves Businesses**, portfolio ID `10153674406626399`, and
you are a **full admin** of it. Meta states plainly that you "can manage everything,
including settings, people, tools and business assets" and "can delete the business
portfolio at any time."

The catch is that portfolio admin does not grant asset access in Meta's model. Each ad
account needs its own assignment, and you do not have one on `87863118`. Only three people
are assigned to it, all Full access: **Claude2**, **David Rack**, **Jeffrey Chitek**.

To fix, 20 seconds:

> business.facebook.com → Settings → Accounts → **Ad accounts** → **Gravity Trails /
> Admire NOLA** → **Assign people** → yourself → **Full access** → Save.

Two notes while you are in there. **Claude2 looks like an automation identity**, the same
pattern as the claude-gmail API user on the Google Ads side, so leave it alone. And Door
County Kayak Tours sits in this same portfolio, which is exactly why Ads Manager kept
auto-attaching its product catalog to your campaign.

Until that is done, do not bother with the steps below. They will not stick.

### 4. Two optional cleanups

- **Uncheck "Multi-advertiser ads"** on the ad. It lets Meta resize and crop your creative,
  and this video has burned-in text at specific positions.
- There is a **separate stuck draft** in the account, unrelated to this campaign: one ad
  with change "Updated: Ad status" that has its own error and cannot publish. It sits in
  the "Review and publish" queue and is selected by default. Uncheck it or fix it before
  you publish, or it rides along.

### 5. Publish paused

Publish creates the campaign. Leave the campaign toggle **off** until you have eyes on the
preview, then flip it on.

---

## About the video

23.4 seconds, 1080x1920, 30fps. Cut from `NPB video dump/` plus the gator and drone footage
in `Assets/Videos/`. Arc: gator hook → party → 7 miles → your drinks → your playlist →
captain finds the gators → 1hr45 rain or shine → 4.9 stars → logo card.

**It is silent on purpose.** Every usable party clip has copyrighted music playing on the
boat, which risks a music-rights flag. Add a track from Meta's own cleared sound library in
Ads Manager if you want audio. The burned-in text carries the ad sound-off either way.

Two clips were deliberately left out as too suggestive for paid: the twerking sequences in
`225613746708835408.mp4` and `682554809377183693.mp4`.

Text is set in Arial Black, not Alegreya Sans SC. The brand font is not installed on this
Mac. If you want it exact, install Alegreya Sans SC and I will re-render.
