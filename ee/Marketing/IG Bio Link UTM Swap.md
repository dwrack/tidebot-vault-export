# IG bio link UTM swap

Why: Oct 17 report showed 512 IG link taps but 0 GA4 bookings credited to Instagram (last 28 days). Bookings DO carry through when the visitor lands on ebbandember.com first (Google organic: 73 credited, verified 2026-10-19), so the fix is routing + tagging.

Tag convention (same as the Aug 2026 Hannah handoff, don't change it): `utm_source=instagram` (never `ig`), `utm_medium=bio` / `story` / `reel`.

## The bio is a link stack, not one link

As of Oct 13 it held several direct Periode links (Autumn Equinox, Sunset Session, Summer Punch Pass, Banya Mondays), most stale. Direct Periode links can never be credited to Instagram. Rebuild the stack so every link lands on ebbandember.com:

**Winter stack (drafted 2026-10-19, matches Jonah's Oct 17 ask in #marketing):**

| # | Bio link title | URL |
|---|---|---|
| 1 | Book a session | `https://www.ebbandember.com/?utm_source=instagram&utm_medium=bio&utm_content=book` |
| 2 | Banya Mondays | `https://www.ebbandember.com/wellness?utm_source=instagram&utm_medium=bio&utm_content=banya` |
| 3 | Private party | `https://www.ebbandember.com/?utm_source=instagram&utm_medium=bio&utm_content=private` |
| 4 | Memberships | `https://www.ebbandember.com/memberships?utm_source=instagram&utm_medium=bio&utm_content=memberships` |
| 5 | Gift cards (from Nov 1) | `https://www.ebbandember.com/shop?utm_source=instagram&utm_medium=bio&utm_content=giftcards` |

Social, Sunrise and Moonlight are all buttons on the homepage (checked 2026-10-19), so link 1 covers them. Banya only lives on /wellness. The site has no per-session pages, so separate Sunrise/Moonlight bio links would just be duplicate homepage links.

**Site issues spotted (for Jess):** homepage Periode buttons carry stale dates in the URL: Sunrise + Moonlight `2026-10-01`, Private party `2025-12-05`, the generic Book Now buttons `2025-11-09`. Check they still open on today's availability.

## Swap it in (phone, 2 min)

1. Instagram app, @ebbandember profile, **Edit profile** > **Links**.
2. Remove stale links (Equinox, Sunset, Summer Punch Pass).
3. Edit or add each link with the URLs above, **Done**.
4. Tap each link from the profile once to confirm it loads.

## Story link stickers

`<site page>?utm_source=instagram&utm_medium=story&utm_content=<what-the-story-was>`

## Two GA4 settings that decide whether IG gets credit (recommended Aug, not done yet)

GA4 Admin > Data Streams > web stream > Configure tag settings:
1. **List unwanted referrals:** add `periode.no`, `minside.periode.no`, `merchant.periode.no`. Periode is still crediting itself with 31 bookings / 28 days.
2. **Adjust session timeout:** 30 min to 4 hours, so someone who taps tonight and books after dinner still counts as Instagram.

## Check it worked

GA4 (property 524300531) > Traffic acquisition, session source = instagram: visits within 24h. Re-check bookings credited to instagram / bio around Nov 2.
