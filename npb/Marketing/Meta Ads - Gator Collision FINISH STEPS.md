# Gator Collision: LIVE

Turned on 2026-09-22. All four ad sets show green **Learning**. Spending **$160/day**.

| Ad set | Ad | Headline |
|---|---|---|
| Nightlife & Bars \| Gator Collision | NPB \| Gator Collision v1 | Gators. Your playlist. 15 minutes. |
| Nightlife & Bars \| Planner's Win | NPB \| Planner's Win | You'll look like a genius for this |
| Nightlife & Bars \| Weather Kill | NPB \| Weather Kill | Rain doesn't cancel this |
| Nightlife & Bars \| Anti-Bourbon | NPB \| Anti-Bourbon | The NOLA that isn't Bourbon St |

Campaign `52578687844700`. Same 23 second video on all four, so the only variable is copy.

**To stop it:** Campaigns > NPB | Purchase | Gator Collision | Sept 2026 > toggle off.
Note that in the campaign edit panel the toggle is only a draft edit, you have to click
**Publish** after flipping it. From the campaigns list the toggle applies immediately.

**Pre-launch audit** lives in `Meta Ads - Gator Collision PRE-LAUNCH AUDIT.md`. Nothing
blocking was found; the Purchase pixel event was confirmed Active before launch.

## Why it is structured this way

Splitting into ad sets alone would not have produced a clean read. The campaign was using
**campaign budget optimization**, one $40/day pot that Meta reallocates toward whichever ad
set wins early. That is the same concentration problem one level up.

So: campaign budget is now **off**, each ad set carries its own $40/day, and **"share some
of your budget with other ad sets" is unchecked**. Without that last one Meta would still
shuffle up to 20% between them.

## Settings, identical across all four

| Setting | Value |
|---|---|
| Objective | Sales |
| Performance goal | Maximize number of conversions |
| Conversion event | Purchase |
| Dataset | GT Pixel- NPB, Kayak (`701301873334767`) |
| Budget | $40/day per ad set |
| Location | New Orleans +50mi |
| Minimum age | 24 |
| Interest | Nightlife (bars, clubs & nightlife) |
| Format | Single video |
| Page / IG | New Orleans Party Barge / nolapartybarge |
| Landing page | nolapartybarges.com/the-freaky-tiki/ |
| CTA | Book now |
| Multi-advertiser ads | Off |

## AI settings turned off

Meta had these on by default and each one would have altered the work:

- **Text improvements** was rewriting the copy. The preview had already swapped the hero
  headline for "Bathroom on board."
- **Video touch-ups** applies AI adjustments to the footage.
- **Creative translation** had Spanish plus **17 other languages silently selected**.
- **Creative generation** offered AI images branded **NOLAPEDALBARGE.COM**, which breaks
  the no-pedal rule. None selected.

## What was handled at publish

- The campaign toggle was set **off before** publishing, so it went live paused rather
  than going live and then being stopped.
- The unrelated stuck draft was **unchecked** so it did not ride along. It turned out to be
  **"New Orleans Kayak Swamp - Video views"** with change "Updated: Ad status", nothing to
  do with this campaign. It is still sitting in the queue as the one remaining draft item,
  still erroring. Deal with it separately or leave it.
- The three other live campaigns (New Sales Campaign, NPB | Messenger | TOF,
  NPB | Purchase | Retargeting) were not touched and are still Active.

Each ad still shows "Your ad won't deliver to 1 placement." Expected for a 9:16 video that
does not fit one squarer placement. It does not block the rest.

## Reading the test

$160/day, seven days, about $1,120. At a ~$150 average booking value that needs roughly 8
bookings to wash its face.

Give it the full seven days. Each ad set needs volume to leave the learning phase, and
judging on day two will just be reading noise. The thing you are looking for is which
angle produces the lowest cost per purchase, not which gets the most clicks.
