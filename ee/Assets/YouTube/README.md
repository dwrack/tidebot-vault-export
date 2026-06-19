# Ebb & Ember YouTube assets

Channel: https://www.youtube.com/@ebbandember (ID UCbzG-G9b9s9Uz49QZuGqOeQ)

## Done (live now)
- Channel title, description, keywords (pushed via API)
- Banner (`banner.jpg`) live on the channel
- 6 reels uploaded as public Shorts (see mapping below)

## STATUS: migration complete — all 26 reels uploaded as public Shorts (2026-06-19)
The ~6/day quota cap turned out not to bind, so all batches went up the same day via the
local script `~/.claude/scripts/ebb_youtube_batch.py` (idempotent, reads `migration_manifest.json`).
All 26 branded thumbnails are stashed in `thumbnails/` (named by YouTube video id) but are
NOT applied yet — blocked on channel verification (below). No launchd job was installed
because there's nothing left to pace; re-run the script manually if new reels are added.

## Needs David, one-time: verify the channel to unlock custom thumbnails + avatar
Custom thumbnails are blocked until the channel is phone-verified. The API returned:
"The authenticated user doesn't have permissions to upload and set custom video thumbnails."

1. Go to https://www.youtube.com/verify (signed in as sauna@ebbandember.com), verify by phone.
2. Once verified, I can push all 6 thumbnails below automatically. Or apply them manually in
   YouTube Studio > Content > each video > Thumbnail > Upload.
3. Avatar (profile picture) can never be set by API. Upload `avatar.png` manually:
   YouTube Studio > Customization > Branding > Picture.

## Thumbnail mapping (file name starts with the video ID)
Batch 1:
| Video | Title | Thumbnail file |
|---|---|---|
| Q4RW4j_fBDg | No Plans Tonight? | thumbnails/Q4RW4j_fBDg_no-plans-tonight.jpg |
| wOrwtCi8cMk | Banya Mondays / Steam Ritual | thumbnails/wOrwtCi8cMk_banya-steam-ritual.jpg |
| pH4j6lYgY0U | Make the Sauna Your Weekly Reset | thumbnails/pH4j6lYgY0U_weekly-reset-memberships.jpg |
| _RUn6rnv2RA | Rainy Portland Day | thumbnails/_RUn6rnv2RA_rainy-day-reset.jpg |
| hhd48I6wBOc | Sauna, River Plunge, Repeat | thumbnails/hhd48I6wBOc_sauna-plunge-repeat.jpg |
| Hh-ojWzBhM0 | Inside Portland's First Floating Sauna | thumbnails/Hh-ojWzBhM0_step-inside.jpg |

Batch 2:
| Video | Title | Thumbnail file |
|---|---|---|
| MCwI45b9TdY | The Most PNW Way to Relax | thumbnails/MCwI45b9TdY_most-pnw-way.jpg |
| qhEewCFwxts | Some Views Just Hit Different | thumbnails/qhEewCFwxts_some-views-hit-different.jpg |
| aCp67yuevWw | Floating Sauna Nights | thumbnails/aCp67yuevWw_floating-sauna-nights.jpg |
| 5gL3j2niMMo | No Notifications, No Rushing | thumbnails/5gL3j2niMMo_no-notifications.jpg |
| 9__8Yk77PGI | Rainy Days Hit Different | thumbnails/9__8Yk77PGI_rainy-days-hit-different.jpg |
| 5iNq65PX2hs | Sunrise or Sunset | thumbnails/5iNq65PX2hs_sunrise-or-sunset.jpg |

## Thumbnail recipe (for the rest of the reels)
- 1080x1920, source = a strong frame from the reel
- Brand font TAYBasal (`TAYBasal.otf`, also in Drive > Typography), all-caps
- Cream hook (245,240,230), sage rule + CTA (121,141,127), dark bottom + top scrim
- Generator script: /tmp/ebb_reels/make_thumb.py (rebuild locally as needed)

## Progress
- Batch 1 (2026-06-18): 6 up. Batch 2 (2026-06-19): 6 up. **12 of 27 done.**

## Remaining reels to migrate (14, by IG engagement) — quota is ~6 uploads/day
Next batch first. Each: yt-dlp download, branded thumbnail (TAYBasal), public Short, stash thumb in vault.
1. DW9RYF5ke8o (Saturday plans)
2. DXLI5p7EboE (Ebb and flow)
3. DWU31WDD2s4 (8pm weekday sunset)
4. DYP6wLNBB42 (sometimes you just need heat + cold)
5. DXiF6fuD76z (views like this)
6. DZnWHoERUJP (summer invite)
7. DZtWmB3x0BG (Summer Punch Pass)
8. DYGfbgvROKh (sauna really does help)
9. DX8Dw0cxFwU (sauna but intentional)
10. DUv6MsHkgFe (Valentine's — evergreen the copy)
11. DUgYxnlkatY (National Sauna Week ritual — drop expired code)
12. DW-mM6xkdtZ (25% off private — drop expired code)
13. DTdvaOPEwRp (get the most out of your session)
14. DTD5DSkEktb (Mind-Body Wellness Day)

SKIP DW9fD9YCflb (duplicate of DYGfbgvROKh, only 4 likes).
