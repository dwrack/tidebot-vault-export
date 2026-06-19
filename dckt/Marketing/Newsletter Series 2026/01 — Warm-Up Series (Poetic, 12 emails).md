# Summer 2026 Warm-Up Series — Poetic Re-Engagement (12 emails)

*Built 2026-06-18. Purpose: wake up the cold 31.7k past-customer list with poetic, sensory,
genuinely-enjoyable-to-read summer conversation before the booking-heavy 16-email cross-sell
series runs. Booking nudges are a whisper (soft inline link), not a pitch. Secondary goal:
drive Instagram scrolling. Voice = the "Scout" (warm, real, short sentences, concrete images,
no gush) written to the customer avatar (35-55 WI/Chicago mom, first-timer, reading on her phone).*

## Where it lives
- **Content (source of truth):** `~/Projects/dckt-tools/newsletter-2026/engage-emails.mjs`
- **Renderer:** `~/Projects/dckt-tools/newsletter-2026/engage-build.mjs` → `engage-out/wuNN-slug.html` + `.txt`
- Build: `cd ~/Projects/dckt-tools/newsletter-2026 && node engage-build.mjs`
- **Sending:** reuse the existing `send-ses.mjs` pipeline (Amazon SES **us-west-2 production**,
  from + reply-to `info@doorcountykayaktours.com`). Same recipients/suppression as the cross-sell
  series. Send in waves (--limit 500 / 3000 / all) to warm the list.

## Why this series first
The list is cold (nothing sent to the 31.7k yet as of build date). Hitting a cold list with
"book now" risks spam folders and burns sender reputation. This soft series gets them opening
and clicking, then the [[16-email cross-sell series]] (`emails.mjs`) lands on a warm list and
actually converts. One series at a time, ~2x/week.

## Cadence — 2 emails/week × 6 weeks
| # | Send | Subject | Theme | IG block |
|---|------|---------|-------|----------|
| 1 | Wk1 Tue | The lake's been quiet without you | Re-open / the water's back | single |
| 2 | Wk1 Fri | How to do nothing in Door County | Stillness / slow down | strip |
| 3 | Wk2 Tue | You can see your own shadow on the lakebed | Water clarity (educational) | follow |
| 4 | Wk2 Fri | The dinner that ends in a fireball | Fish boil (food) | single |
| 5 | Wk3 Tue | The cherries are coming | Cherry season (food) | strip |
| 6 | Wk3 Fri | Book the late one. Thank us later. | Golden hour | single |
| 7 | Wk4 Tue | The afternoon nobody argues about | Family / connection | follow |
| 8 | Wk4 Fri | What the lake gives back | Driftwood + shipwreck | strip |
| 9 | Wk5 Tue | The prettiest way to the water has no engine | E-bike | single |
| 10 | Wk5 Fri | Set an alarm on vacation. Trust us. | Early morning calm | follow |
| 11 | Wk6 Tue | The locals' favorite month isn't the one you'd guess | September shoulder | strip |
| 12 | Wk6 Fri | Whenever you're ready, the water's right here | Capstone invitation | single + follow |

IG treatment is **mixed on purpose** (single featured / 3-up tappable strip / follow-only band)
so the format stays fresh across 12 sends. Every IG image is tappable and opens the real post.
**Each email gets its own distinct posts** (no recycling the same frames across emails).

**Layout (David's calls, 2026-06-18):**
- **Headline leads, photo farther down.** Order = logo → gold rule → kicker + serif headline →
  opening line → hero photo → rest of body → IG block → footer. The text is what's above the
  fold, not a big image.
- **No cold-weather photos.** Never use shots with people in coats / snow / ice in a summer
  series (it reads off-season). Verified-out: the icy e-bike shot `DUWaZ6TkuBY` and the winter
  ice-shard `DYSWcBriASD`. Prefer people-free summer shoreline/water shots when unsure.

## Instagram covers — DONE
Pulled the real post covers off the live @doorcountykayaktours feed (via og:image), optimized,
and uploaded to S3 `dckt-email-assets/email/ig-<shortcode>.jpg` (verified public). 6 clean
summer/water frames in rotation:
- `ig-DZbkiSQge0N` wide turquoise · `ig-DZSrLduxIVV` kayakers on open water ·
  `ig-DZBB3NcJfoB` clear water over rock · `ig-DZIs3-yJJfc` e-bikes ·
  `ig-DMyouEcJzKB` sunset collage · `ig-DZWA1qEJO9o` kayaks in evening light.
- Skipped duds: winter ice shot, a near-blank fog frame, and a text-graphic with a cut-off eagle.

## Heroes — DONE (unique per email)
Each email has its OWN landscape hero (real DCKT photos pulled from the website media library
via WP REST, optimized, uploaded to S3 `dckt-email-assets/email/hero-*.jpg`):
01 Cave Point aerial · 02 foggy still Cave Point · 03 clear water over rock · 04 paddlers coming
off the water · 05 ripe cherries on the branch · 06 kayakers in a pink sunset · 07 group of boats
+ guide · 08 kayak-POV bluff shoreline · 09 fat-tire e-bikes · 10 misty dawn at Cana · 11 the
winding fall-color road · 12 silhouette under a sea cave (capstone). To swap any later: replace
the source, re-upload same filename, bump `ASSET_V` in `engage-build.mjs`.

## What's left before send
1. **Approve copy + cadence.**
2. **Warm the list in waves** (`send-ses.mjs` style --limit 500 / 3000 / all).

## Verified food facts used (do not drift from these)
- **Fish boil (E04):** whitefish + red potatoes + onions over open wood fire; boilmaster throws
  kerosene ~9-10 min in for the boil-over; Scandinavian roots, late 1800s; cherry pie included.
  Named real Fish Creek venues: **Pelletier's** (nightly, mid-May–mid-Oct) and **White Gull Inn**
  (dining since 1896). [VERIFIED]
- **Cherries (E05):** tart **Montmorency** is the Door County cherry; u-pick ~mid-July into August
  (weather-dependent, "call ahead"); **Lautenbach's Orchard Country** (Fish Creek, DCKT partner) +
  **Seaquist** (Sister Bay); **Jacksonport Cherry Fest = Aug 1, 2026** (NOT July 4). [VERIFIED]
- Do NOT use: Viking Grill (closed 2022), "National Cherry Festival" (that's Michigan).

## Tracking
Every booking link carries a FareHarbor `?ref=nl_wuNN_<tour>` tag (real purchase attribution that
survives checkout, unlike GA4) + UTM params. Campaign = `warmup_summer_2026`. IG/profile links
are UTM-tagged too. See [[reference_deposit_model_ads_value]], [[feedback_ga4_fareharbor_attribution]].

Signed "The crew at Door County Kayak Tours" (never David's name, per outbound rule).
