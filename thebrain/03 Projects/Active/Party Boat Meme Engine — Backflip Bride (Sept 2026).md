# Party Boat Meme Engine — Backflip Bride

*Started 2026-09-10. Source of truth for which party-boat video won and the meme lines we're running over it.*

## The winner

**"Bachelorette Bride Backflips on a New Orleans Party Boat"** — NOLA Party Barge
https://www.youtube.com/watch?v=zoUYega3hcI · 16.7s · 1920x1080 landscape

Last 12 months (2025-09-10 → 2026-09-10), YouTube Analytics:

| Video | Views | Avg view % | Likes | Shares |
|---|---|---|---|---|
| Backflip bride (NPB) | 166,986 | 103% | 0 | 1 |
| BYOB Tiki Booze Cruise (NPB) | 106,992 | 93% | 86 | 19 |
| Party Boat Goes OFF (NPB) | 104,338 | 78% | 237 | 36 |
| Birthday Cruise On Clear Lake (HPB) | 7,554 | 124% | 8 | 1 |

NPB beats Houston Pedal Barge by roughly 22x. Not close. The party-boat meme engine lives on NPB.

## The caveat that matters

Channel traffic sources for the same window: **ADVERTISING 391,178 views** vs SHORTS 43,943 and YT_SEARCH 4,277. The top three videos add up to 378k, so those view counts are almost entirely paid. The backflip clip is our best *ad asset*, not proof of organic virality (0 likes on 167k views gives it away).

Organic-side leaders, for comparison:
- "Freaky Tiki Party Boat" — 3,136 views, 42 shares
- "Private BYOB Party Boat" — 2,985 views, **65 shares** (2.2% share rate, best on the channel)

Backflip bride is still the right meme base: full watch-through at 103%, and a bride in a veil flipping off a boat is self-explanatory in one frame. But track the memes' organic numbers separately from the ad numbers or we'll fool ourselves.

## Meme kit

Working folder: `~/Movies/NPB Meme Kit/`
- `backflip-bride-source.webm` — the pulled source
- `meme-lines.txt` — one line per meme, `slug|text`
- `make-memes.sh` — burns text over the clip, outputs 1080x1920 to `out/`
- `out/*.mp4` — ready to post

Add a line to `meme-lines.txt` and re-run, or one-off it:
```
~/Movies/NPB\ Meme\ Kit/make-memes.sh "Her mom is watching this right now"
```

Style: Impact, white, heavy black stroke, top third. Blurred fill behind so the landscape clip works vertically.

## Round 1 lines (24)

**Bride / bachelorette**
1. Nobody died. (Actual review.) ← ties to [[Nobody Died — Review Hook for Party Boat & Kayak Videos]]
2. Her mom is watching this right now
3. Last flip as a single woman
4. The groom is on a golf course right now
5. The maid of honor said don't do anything crazy

**Gators / bayou**
6. Somewhere under her, a gator is filing a complaint
7. New Orleans does not have a shallow end

**Crew deadpan** (this is the vein worth mining, it's the only voice a competitor can't copy)
8. This is what BYOB does to a person
9. The captain has seen things
10. That's the third one today
11. We do not train them. They arrive like this.
12. Our insurance guy just called
13. The safety briefing was 90 seconds long
14. The cooler was full when we left the dock
15. No refunds for this level of commitment
16. Employee of the month
17. Form check: 10 out of 10

**Comparison / FOMO**
18. Bachelorette parties in Nashville could never
19. Your bachelorette: a brunch. Hers:
20. Meanwhile your group chat is still looking into options
21. This is 15 minutes from the French Quarter
22. You could be doing this instead of another rooftop bar
23. Bourbon Street wishes
24. POV: your friend picked the itinerary

## Open items

- [ ] Release check. The bride is identifiable and this is a real guest. It's already public on the channel, but memeing her repeatedly is a different use than a highlight reel. Same blocker as [[boatcam]] — confirm we have a photo/video release covering it before this scales.
- [ ] Post the first 5-6 organically on NPB IG/TikTok, no spend, and log views + shares here after 7 days.
- [ ] Winners get promoted to Meta ad creative via /ad-scripter. Losers get deleted, not fixed.
- [ ] Find the actual "nobody died" review (GBP/TripAdvisor/Airbnb, NPB + NKST) so line 1 can be attributed on screen.
