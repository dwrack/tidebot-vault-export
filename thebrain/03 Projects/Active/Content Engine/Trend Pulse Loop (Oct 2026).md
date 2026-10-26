# Trend Pulse Loop (Oct 2026)

Started 2026-10-16 from an @reeltrendsapp post (Oct 12 list). Goal: catch trending sounds, formats, and hashtags every week, put the ones that fit into our posts, then grade them against our own numbers so the picks get better each week.

## What the post actually said (Oct 12)

| Sound | Artist | Reels using it | Our fit |
|---|---|--:|---|
| My October | The Folks | 284K | E&E fall sauna, DCKT "season's over" fall-color montage |
| Cinnamon & Coffee | Vintage Relaxation | 60K | E&E cozy morning steam + cold plunge. Smallest count, so earliest. Best one to ride |
| Saxophones Getting Louder | AXRYN | 214K | NPB build-up edit: the sax gets louder as the party gets wilder. Our brass-on-the-dock reel did 5.2k |

Hashtags were national and broad (#nyc, #taylorswift, #momlife). Mostly useless for local tours. The usable ones: #halloween, #october, #fallvibes, #travel, #smallbusiness, as a garnish next to the local tags in `night-shift/apify_config.json`.

**Business-account catch:** brand accounts only get Meta's commercial music library. Search each sound in the IG app before shooting. If it's grayed out for that account, use the format (the build-up, the cozy montage) with a library track or a voiceover instead. The Graph API can't attach library music, so trending audio gets added in-app (by a manager, or later by the phone rig).

## Do now (this week)

1. **Halloween is Oct 31.** #halloween is the top tag nationally. NKST haunted swamp reel, NPB Halloween barge reel, E&E "spooky sauna night" reel. Shoot by Oct 24 so they get a week to run.
2. **Swap the carousel drips for reels.** Oct 14 study: carousels get about 1/3 the reach of reels on DCKT, and HPB price carousels did 16 to 39 reach. Pull the rest of the HPB queue (runs through Oct 22) and give 2 or 3 slots to reels with a trending sound.
3. **Three trend reels from the list above:** E&E on Cinnamon & Coffee, NPB on Saxophones Getting Louder, DCKT season-wrap on My October.
4. **Comment-reply reels.** Answer a real comment with a video (IG "reply with reel"). People and humor beat info on every brand, and this format is both.

## Sources to follow

| What | Source | How we pull it |
|---|---|---|
| Trending sounds (TikTok, leads IG by 1-2 weeks) | TikTok Creative Center, US, commercial-use filter | Apify `s_actors/tiktok-trending-sounds-scraper` with `commercialOnly: true`, about $0.10/run |
| Sounds gaining fastest | TikTok chart history | Apify `trendingtiktoksongs/tiktok-trending-sounds-history`, growth mode |
| IG Reels trending audio | IG app: Reels audio picker, the arrow next to a song | manual, 2 min a week, or phone rig |
| Weekly IG lists | @reeltrendsapp, Later's weekly Instagram trends post | read weekly, gently (no rapid IG fetches) |
| Local music taste | Shazam city charts (New Orleans, Houston, Austin, Portland), Spotify Viral 50 USA | web fetch |
| Local hashtags + location UGC | Our 17 tags + location IDs | already running, `night-shift/apify_config.json` |
| Meme formats | Know Your Meme, TikTok Creative Center "trending videos" | weekly scan. Formats go stale in about 2 weeks |
| What our crowd says | Our IG/FB comments, GBP reviews, competitor top comments | social-listening harvest (already built) + Apify comments |
| Local calendar | event radar / chief-of-staff | already running |

## The learning loop

1. **Monday pull (mbp-2, launchd):** sounds (commercial-only), sound growth, local hashtags, our last 7 days of post insights.
2. **Score each trend per brand:** fit with brand voice, how early it is (fewer uses = earlier), is it in the business music library, does it match a format that already won for that brand.
3. **Write `Trend Pulse <date>.md`:** top 3 sounds + top 2 formats per active brand, each with a one-line shot idea. Post the short version to the brand's Slack lane.
4. **Tag every post that uses a trend** in a ledger (`trend-ledger.csv`: post id, brand, sound, format, hook, date).
5. **7 days later, grade it:** reach, saves, shares, profile/web clicks vs. that brand's median. Shares count double for NPB and HPB (group-decision brands).
6. **Update `What Works` per brand:** which sound types and formats beat median. Next Monday's scoring reads this table first, so picks drift toward what our audiences actually reward instead of what's trending nationally.
7. **Winners feed paid:** anything over 2x median goes on the boost list (paid + organic single loop).

**Blocker to check first:** the IG Graph API returned a permission error on media reads in October, and @kayaknola is unreadable. Step 5 needs insights working on every brand account.
