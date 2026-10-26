# Sauna Content Research: What's Working (Oct 2026)

Pulled 2026-10-20 via apify-ee. Raw rows: `Sauna Content Research — What's Working (Oct 2026) raw.csv` (232 rows: 172 TikTok, 44 IG hashtag reels, 16 IG brand reels).

## Read this first (limits of the data)

- Hashtag pulls return a popularity-weighted mix, not a clean last-90-days slice. TikTok rows span 2022 to Oct 2026 (69 of 172 are from the last 90 days). IG hashtag pulls were capped at about 11 reels per tag (free tier returns the first page only).
- On-screen text and shot-level hooks were NOT pulled (that needs the paid AI description add-on). Hook analysis below comes from captions, durations, and the clips' titles. Treat the "on-screen text" patterns as inferred from captions plus your own 22.7K spike.
- Views relative to followers is only reliable on TikTok (follower counts came back). IG hashtag rows have no follower count.
- Brand pulls: Löyly, Othership, Community Sauna Baths worked. Koti, Arc, Guss Mobile Sauna returned nothing (private, wrong handle, or not found). Sauna Social Club handle returned only 2022 junk posts.
- Our own TikTok shows up in the data: @ebbandember floating sauna posts sit at 232 to 3,860 views, member night at 2,712. Our typical range matches the 1-3K you mentioned.

## Top 15 example posts

Ranked by views, but filtered to be relevant to a social sauna / bathhouse / floating sauna brand (news gossip clip at 10.4M and pure supplement ads left out).

| # | Views | Account (followers) | Posted | Len | Likes / Shares | Link | Why it worked |
|---|---|---|---|---|---|---|---|
| 1 | 2.9M | @builtwithtools (small) | 2026-02-25 | 104s | 34.8K / 5.9K | https://www.tiktok.com/@builtwithtools/video/7610592135980535070 | Personal story hook ("I started plunging for the energy boost to be honest"), blue-collar everyman, long watch time |
| 2 | 2.3M | @miaboutiquestays (18K) | 2026-03-25 | 15s | 140.4K / 10K | https://www.tiktok.com/@miaboutiquestays/video/7621289768185285901 | "I almost didn't want to share this": secret-spot hook, outdoor baths in redwoods, 128x its follower count |
| 3 | 1.2M | @prisrecs (16K) | 2025-09-19 | 29s | 55.3K / 30.7K | https://www.tiktok.com/@prisrecs/video/7551852949941603639 | "Save this for your next spa day": explicit save/send CTA, 1.8% share rate, bathhouse in Flatiron |
| 4 | 1.1M | @_bryan_johnson_ (910K) | 2026-10-07 | 81s | 79.4K / 10.3K | https://www.tiktok.com/@_bryan_johnson_/video/7694004397604424990 | "The 3 tiers of sauna and their benefits": listicle/education from a big name |
| 5 | 900K | @ninainsauna (255K) | 2025-06-27 | 23s | 37K / 1.4K | https://www.tiktok.com/@ninainsauna/video/7520668839315541270 | "Sauna rules in Finland": cultural rules/etiquette format |
| 6 | 651K | @pepperonimuffin | 2025-08-20 | 103s | 125.8K / 534 | https://www.tiktok.com/@pepperonimuffin/video/7540459195653491999 | "This was actually my first cold plunge ever": first-time reaction, no polish |
| 7 | 579K | @mainelycass (8.8K) | 2026-05-16 | 45s | 21.2K / 4.5K | https://www.tiktok.com/@mainelycass/video/7640476592866692365 | Floating sauna tour ("Tour the floating sauna ... with me"), 66x follower count. Closest comp to us |
| 8 | 523K | @meme.hopecore_ (44K) | 2026-08-18 | 19s | 32K / 5.9K | https://www.tiktok.com/@meme.hopecore_/video/7675511029563919649 | Friend-group humor ("we only ever go together"), shareable relationship/friends angle |
| 9 | 396K | @fortmillmama (3.4K) | 2025-11-03 | 32s | 30.8K / 13.4K | https://www.tiktok.com/@fortmillmama/video/7568606949290396958 | New-facility reveal with price ("$60 for 2 hours"), 3.4% share rate |
| 10 | 366K | @_kierra.monique_ (1.8K) | 2026-06-04 | 15s | 27.9K / 1.2K | https://www.tiktok.com/@_kierra.monique_/video/7647689549786778911 | "Perfect way to unwind", PNW weekend-getaway tags, 15s mood clip, Oregon |
| 11 | 305K | @jimmysundays | 2026-10-16 | 29s | 22.5K / 775 | https://www.tiktok.com/@jimmysundays/video/7697340841622392094 | "Natural cold plunge" + sunrise/dawn visual, caption two words |
| 12 | 243K | @alittlerainey (22.7K) | 2026-03-19 | 18s | 5.2K / 1.6K | https://www.tiktok.com/@alittlerainey/video/7619012482866122014 | "Floating sauna on Lake Union ... most unique ways to unwind in Seattle", PNW floating comp |
| 13 | 241K | @fittwotravel | 2026-02-23 | 48s | n/a | https://www.tiktok.com/@fittwotravel/video/7609881721202380062 | "If you're near Portland and needing some self-care", local-intent hook (Cascada) |
| 14 | 177K | @isabellatorner (IG) | 2026-07-31 | 30s | 4.3K / 1.2K | https://www.instagram.com/p/DbdeNbaIbT8/ | "Sweden, America, WORLD, we need to talk": opinion-bait, 3-word caption |
| 15 | 95K | @biigwaterguy | 2026-05-18 | n/a | n/a | https://www.tiktok.com/@biigwaterguy/video/7641278821022371085 | "Portland's first and only floating sauna" tagging Ebb & Ember. Proof local creators already drive our biggest reach |

Also worth a look (not in the 15): Othership "Episode 4: The Group Chat" scripted skit, 652K IG plays, 45.8K likes, https://www.instagram.com/p/DcCMtJWJ9S7/ . Our travelportland feature (31K): https://www.tiktok.com/@travelportland/video/7685910231003434271 .

## Patterns, ranked by evidence

1. **Short, mood-only clips beat long ones inside travel/venue content, but a long personal story beats everything on the education side.** Median TikTok plays by length: 11-20s = 42.9K, 41-90s = 21K, 21-40s = 12.6K, 0-10s = 3.3K, over 90s = 234K (small sample of 18, mostly story and education). Your 9s spike worked because of the audio and caption pairing, not the length alone: pure 0-10s clips in this set mostly flopped (3.3K median). Sweet spot for venue/vibe content is 12-20s.
2. **Place-reveal framing with a secret/first-time hook.** "I almost didn't want to share this", "Portland's first and only floating sauna", "Tour the floating sauna ... with me", "New sauna facility in South End". The discoverable-new-place angle is the single most repeated winner for venue accounts (ranks 2, 3, 7, 9, 10, 12, 13, 15). Small accounts (under 20K followers) repeatedly hit 60x to 130x their follower count with it.
3. **Save/send CTAs on reveal posts drive shares.** The highest share rates in the set (1.5% to 3.8%) are bathhouse reveals with "Save this for your next spa day" or a price plus "2 hours" line. Rows: meggyeatz (3.8%), fortmillmama (3.4%), prisrecs (2.6%). Price in the caption helps (they all state $50 to $65).
4. **Friends/group framing.** "Girl time in the sauna", "with your girlfriend", "the person you want to experience this with" (Alberta floating sauna, 63.7K IG plays, 1,013 shares at 9s), "Wir gehen nur zusammen hin" (friends-only humor, 523K). "Send this to ..." phrasing generates shares. This matches your "+ your besties >>>" win.
5. **Floating sauna is an underserved, high-ceiling niche, but most posts are small.** #floatingsauna median is only 1.9K plays vs 98K for #coldplunge, but the top outliers hit 579K and 243K (Maine, Seattle). So the tag is thin and a good post can stand out. #portlandsauna median 9.4K, with Cascada, Ebb & Ember, and Löyly Portland already in it. Local and travel intent works ("If you're near Portland ...").
6. **Cold plunge is raw and reaction-driven.** Winners: first-time plunge, natural cold plunge at sunrise (no caption beyond two words), frozen lake, head-under thrills. Authentic, unproduced, often one-take. Science "norepinephrine +300%" posts also do 350K+ but belong to the biohacker lane, off-brand for us.
7. **Culture/etiquette explainers travel far (Finland, Germany, naked-sauna rules).** 1.4M, 900K, 756K, 622K, 304K plays across Finnish and German sauna-culture posts. Format: "Sauna rules in X", "things I learned". Works for a social sauna brand as "Sauna rules at Ebb & Ember" / "first-timer guide".
8. **Time of day and light.** Winners cluster around dawn and dusk, mist, steam, water-level shots (sunrise cold plunge, redwood outdoor baths, Seattle Lake Union). Night glow and blue hour appear in the venue reels in the set (Löyly, TEMZ launch, Tuli Lodge waterfront) but I could not verify lighting from metadata alone. Your blue-hour 9s montage fits the pattern, treat it as strongly consistent but not proven by this dataset.
9. **Original audio vs licensed.** Overall median plays: original sound 25K vs licensed 12.6K, but the original-sound set includes the biggest personality/story accounts. Don't read this as "avoid music". Dreamy trending audio on mood b-roll still matches your result. Test one more mood clip with a different trending dreamy track to isolate audio vs caption.
10. **Brand accounts underperform creator accounts.** Löyly: 8.9K to 31.6K plays on 50.7K followers, mostly brunch and menu posts, tiny engagement. Community Sauna Baths: 3K to 20K plays on 47.9K followers, mostly event calendars and carousels. Othership is the exception, and only when it produces entertainment (scripted "Group Chat" skit: 652K plays, 45.8K likes, 4.5x its own best normal post). Calendar posts and menus do not travel. Skits and first-timer POVs do.

Not supported by the data (do not over-claim): exact on-screen-text formulas, shot counts, POV vs wide split, and sound ids. Next pull should enable the AI video description add-on on the top 20 URLs only (about $0.03 per ten seconds of video, a few dollars total).

## What this means for Ebb & Ember (quick)

- Make more 12-20s dawn/dusk mood clips with the "place + place + your besties >>>" text and no CTA, and run one variant with a "Send this to ..." caption to test shares.
- Repost or stitch creator content. @biigwaterguy (95K), @travelportland (31K), @pnwplatesandplaces and @delaneyxclara already feature us. Ask them for raw clips.
- Add a "First time at a floating sauna? Here's what to know" explainer and a "Sauna rules" etiquette post.
- Floating sauna content should keep the "first and only on the Columbia" claim. Never mention wood-fired.

## Actors and inputs used, approximate cost (apify-ee account)

| Actor | Input | Rows | Approx cost |
|---|---|---|---|
| clockworks/tiktok-scraper | hashtags: sauna, floatingsauna, coldplunge, saunaculture, contrasttherapy, bathhouse, portlandsauna; resultsPerPage 25; no downloads, no date filter (date filter only applies to profiles) | 175 (172 unique) | about $0.65 ($0.0037 per result + $0.001 start) |
| apify/instagram-hashtag-scraper | hashtags: sauna, coldplunge, saunaculture, floatingsauna; resultsType reels; resultsLimit 20 (free tier capped to first page, about 11 per tag) | 44 | about $0.11 |
| apify/instagram-scraper | directUrls for loylyhelsinki, othership, communitysaunabaths, saunasocialclub, kotisauna, gussmobilesauna, arc.sauna; resultsType posts; resultsLimit 12 | 43 (3 profiles errored) | about $0.10 to $0.20 |

Total roughly $0.9 to $1.0. Datasets: TikTok T2wxdme9OKhsd0uqr, IG hashtag Q4b2AyEX6w6QvLeHm, IG brands a4gQFhlXqi85cyOQn.
