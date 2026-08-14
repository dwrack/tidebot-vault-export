# Fresh Clip Batch — August 2026 (Kemah cut)

**8 clips, recut 2026-08-13. NOT POSTED.**
Location: `Assets/Videos/cut-aug2026/`
Desktop shortcut: `HPB Fresh Clips Aug 2026`

Specs: 1080x1920 vertical, 30fps, H.264 high profile, AAC audio, faststart. 6.4-8.0 seconds each,
5.4-9.5 MB. Ready for FB Reels and IG Reels as-is.

**Angle: Kemah Boardwalk proximity, party framing.** Six of the eight name Kemah directly. No mention
of pedaling, the captain, or how the boat works anywhere in the copy.

## Treatment

Yellow (#FFD400) Impact with a heavy black outline, which is what survives on busy footage. Three beats:
1. **Hook** — first 45%, biggest type, top third
2. **Body** — middle, one supporting line
3. **CTA** — last 2.2s, white, `houstonpedalbarge.com`

Original audio kept on all of them.

## The 8

| File | Hook | Body |
|---|---|---|
| `hpb_01-minutes-from-kemah.mp4` | MINUTES FROM KEMAH. / MILES FROM A REGULAR BAR. | Clear Lake after dark. |
| `hpb_02-ten-minutes-kemah.mp4` | 10 MINUTES FROM / THE KEMAH BOARDWALK | And the whole boat is moving. |
| `hpb_03-boardwalk-then-this.mp4` | DO THE BOARDWALK. / THEN DO THIS. | Kemah is ten minutes away. |
| `hpb_04-byob-26.mp4` | 26 PEOPLE. / BRING YOUR OWN COOLER. | Ten minutes from Kemah Boardwalk. |
| `hpb_05-lights-come-on.mp4` | SUNSET, THEN / THE LIGHTS COME ON | Clear Lake, minutes from Kemah. |
| `hpb_06-two-weekends-left.mp4` | TWO WEEKENDS LEFT / BEFORE SCHOOL STARTS | Kemah day, then the boat. |
| `hpb_07-everybody-does-kemah.mp4` | EVERYBODY DOES / THE KEMAH BOARDWALK | Almost nobody does this. |
| `hpb_08-bachelorette.mp4` | BACHELORETTE PARTIES / BOOK THIS ONE OUT FIRST | Seabrook, ten minutes from Kemah. |

## Why Kemah

The single best-performing organic post of 2026 was the Seabrook/Kemah location line: **270 engagements,
46 shares**, against a page baseline of 1-10. Nothing else in 2026 came close except "by TONIGHT!" (362).
Kemah Boardwalk also has enormous existing search and tourist intent that HPB is sitting ten minutes
from and barely mentioning. Clip 03 and 07 are the two that try to convert that intent directly:
position the boat as the thing you do *in addition to* the boardwalk.

All claims stay on the safe side of what the brand doc supports: "minutes from Kemah Boardwalk and the
Seabrook waterfront." Nothing claims the route goes past the boardwalk.

## PRICE DISCREPANCY — needs David

The Brand Story doc says **public tours run $59-69 per person**. The Aug 10 Facebook post said
**"55 a ticket."** Those don't match.

I pulled the $55 clip from this batch rather than publish a price I can't confirm. If $55 is a live
promo, say so and I'll cut it back in. If $59-69 is current, the Aug 10 post is advertising a price
below rate and should probably come down.

## Also

**Clip 06 expires Aug 24.** "Two weekends left before school starts" is dead after that.

## Source library problem

Of the 34 clips in `organic-library/`, only about 10 are usable:
- **10 have old burned-in giveaway text** with dead dates ("Winner announced 4/29", "Winner decided
  Friday 4/15", "Winner Announced Sun 08/28", "Spooky Singles BOOze Cruise October 24th")
- **3 have a TikTok watermark** plus an old address and phone burned in
- **2 are 360x640**, too low-res for Reels

Worth shooting a few hours of clean, un-captioned party footage. Campaign text was baked into the
masters, which turned reusable assets into one-time-use ones.

## Posting — BLOCKED, not just unapproved

Two mechanical blockers, independent of sign-off:

1. **No Facebook Page video publishing tool exists.** The connected Meta tools cover IG publishing
   (`organic_ig_publish_reel`) and FB *paid ads*, but there is nothing that posts a video to the FB
   Page organically. The FB half of this has to be done by hand or through the existing auto-poster.
2. **IG publishing needs a public HTTPS URL.** `organic_ig_publish_reel` will not take a local file.
   These live in the iCloud vault. They'd need to be uploaded to a public host first (the
   `hpb-email-assets` S3 bucket already used for email images is the obvious candidate) before
   anything can publish.

Suggested order once unblocked, one a day rather than a dump: **02** (the proven line), then **07**,
then **06** while it is still true.


---

# PUBLISH STATE — updated 2026-08-13 17:35

## DONE: all 8 clips are live on public HTTPS

Uploaded to `s3://hpb-email-assets/reels/` (us-west-2). The bucket's existing `PublicRead` policy
covers `hpb-email-assets/*`, so no ACL and no policy change was needed. All 8 verified returning
`200 video/mp4`.

| Clip | URL |
|---|---|
| 01 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_01-minutes-from-kemah.mp4 |
| 02 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_02-ten-minutes-kemah.mp4 |
| 03 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_03-boardwalk-then-this.mp4 |
| 04 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_04-byob-26.mp4 |
| 05 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_05-lights-come-on.mp4 |
| 06 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_06-two-weekends-left.mp4 |
| 07 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_07-everybody-does-kemah.mp4 |
| 08 | https://hpb-email-assets.s3.us-west-2.amazonaws.com/reels/hpb_08-bachelorette.mp4 |

## NOT DONE: nothing is posted to Instagram or Facebook

**Instagram** — target account confirmed: `@houstonpedalbarge`, IG user ID `17841451160734299`,
3,798 followers. Daily publish quota checked: 0 of 100 used. Everything is staged and ready.
The blocker is that the meta-organic connection is currently exposing only its 13 read-only tools.
`organic_ig_publish_reel` is not reachable right now, so no publish call could be made.

**Facebook Page** — there is no organic Page video-publishing tool in the connected set at all,
in any connection state. The FB half has to go through the existing auto-poster or be done by hand.

Also note `organic_ig_list_accounts` returns `(#200) Requires business_management permission`. The
token can read Pages and their linked IG accounts but is missing that scope. Worth fixing.

## Captions, ready to paste

**02 — ten minutes from Kemah** (post this one first)
> Ten minutes from the Kemah Boardwalk and the whole boat is moving. Houston's BYOB party boat on
> Clear Lake out of Seabrook. Bring your cooler and your people, we handle the rest.
> houstonpedalbarge.com
>
> #kemah #kemahboardwalk #houston #htown #houstontx #clearlake #seabrook #partyboat #boozecruise
> #thingstodoinhouston #htownweekend #bacheloretteparty

**07 — everybody does Kemah**
> Everybody does the Kemah Boardwalk. Almost nobody does this. Ten minutes away, 26 seats, BYOB,
> two hours on Clear Lake. houstonpedalbarge.com
>
> #kemah #kemahboardwalk #houston #htown #clearlake #seabrook #partyboat #thingstodoinhouston

**06 — two weekends left** (dead after Aug 24)
> Houston goes back to school the 24th. That is two weekends. Kemah day, then the boat.
> houstonpedalbarge.com
>
> #houston #htown #kemah #clearlake #partyboat #backtoschool #thingstodoinhouston

## Still open

**The price.** Brand Story says $59-69 per person. The Aug 10 FB post said "55 a ticket." No clip in
this batch states a price, so it does not block posting, but the Aug 10 post may be advertising under
rate.
