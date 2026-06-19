# Ebb & Ember YouTube assets

Channel: https://www.youtube.com/@ebbandember (ID UCbzG-G9b9s9Uz49QZuGqOeQ)

## Done (live now)
- Channel title, description, keywords (pushed via API)
- Banner (`banner.jpg`) live on the channel
- 6 reels uploaded as public Shorts (see mapping below)

## Needs David, one-time: verify the channel to unlock custom thumbnails + avatar
Custom thumbnails are blocked until the channel is phone-verified. The API returned:
"The authenticated user doesn't have permissions to upload and set custom video thumbnails."

1. Go to https://www.youtube.com/verify (signed in as sauna@ebbandember.com), verify by phone.
2. Once verified, I can push all 6 thumbnails below automatically. Or apply them manually in
   YouTube Studio > Content > each video > Thumbnail > Upload.
3. Avatar (profile picture) can never be set by API. Upload `avatar.png` manually:
   YouTube Studio > Customization > Branding > Picture.

## Thumbnail mapping (file name starts with the video ID)
| Video | Title | Thumbnail file |
|---|---|---|
| Q4RW4j_fBDg | No Plans Tonight? | thumbnails/Q4RW4j_fBDg_no-plans-tonight.jpg |
| wOrwtCi8cMk | Banya Mondays / Steam Ritual | thumbnails/wOrwtCi8cMk_banya-steam-ritual.jpg |
| pH4j6lYgY0U | Make the Sauna Your Weekly Reset | thumbnails/pH4j6lYgY0U_weekly-reset-memberships.jpg |
| _RUn6rnv2RA | Rainy Portland Day | thumbnails/_RUn6rnv2RA_rainy-day-reset.jpg |
| hhd48I6wBOc | Sauna, River Plunge, Repeat | thumbnails/hhd48I6wBOc_sauna-plunge-repeat.jpg |
| Hh-ojWzBhM0 | Inside Portland's First Floating Sauna | thumbnails/Hh-ojWzBhM0_step-inside.jpg |

## Thumbnail recipe (for the rest of the reels)
- 1080x1920, source = a strong frame from the reel
- Brand font TAYBasal (`TAYBasal.otf`, also in Drive > Typography), all-caps
- Cream hook (245,240,230), sage rule + CTA (121,141,127), dark bottom + top scrim
- Generator script: /tmp/ebb_reels/make_thumb.py (rebuild locally as needed)

## Remaining reels to migrate (~20, by IG engagement) — quota is ~6 uploads/day
DXxSFy3y8mT, DV9WJGJkmoY, DU9TyG8EtTl, DYkgHsAxTjK, DXc5ZXQjy-K, DWw_Snmkst8,
DW9RYF5ke8o, DYP6wLNBB42, DXiF6fuD76z, DXLI5p7EboE, DWU31WDD2s4, DZnWHoERUJP,
DZtWmB3x0BG, DUv6MsHkgFe, DYGfbgvROKh, DX8Dw0cxFwU, DUgYxnlkatY, DTdvaOPEwRp,
DTD5DSkEktb, DSHC... (full list from IG)
Skip DW9fD9YCflb (duplicate of DYGfbgvROKh, only 4 likes).
