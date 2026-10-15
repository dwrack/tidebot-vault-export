# Social Analytics + Market Study (Oct 2026)

Pulled 2026-10-14. Our numbers: Instagram Graph API, every post since Jun 1 with reach/saves/shares/views. Market study: Apify scrapes of local competitors and best-in-class similar businesses, one run per market on that brand's own Apify account.

## Bottom line

1. **E&E is the only brand where organic is a real sales channel.** 682 website clicks in 30 days, more than every other brand combined. Two reels did 131k and 51k reach. Both were "do something different with your friends" social framing, not wellness.
2. **The bots are posting our worst format.** DCKT and HPB carousel drips post every day. Carousels get 1/3 the reach of reels on DCKT and 16 to 39 reach on HPB. Meanwhile the NPB and HPB reel queues ran dry in early September and nobody refilled them.
3. **Humor and people beat information, every brand, every time.** DCKT's top 4 posts are all guide jokes. NPB's top post is a "get weird" reel with 249 shares. The bottom of every list is a price, a route, or "book now."
4. **Five accounts are dead or blind.** Austin Kayak (last post Aug 14), BBK (Aug 23), Houston Booze Cruise, Gravity Trails, Cave Point PP (nothing since June). @kayaknola can't be read: the API token lost permission.

## Our numbers by brand (Jun 1 to Oct 14)

| Brand | Followers | Posts | Median reach | Trend | 30d web clicks |
|---|--:|--:|--:|---|--:|
| E&E @ebbandember | 9,293 | 45 | 2,667 (reels) | flat, healthy | 682 |
| NPB @nolapartybarge | 22,558 | 36 | 1,584 | Jul 1.8k, Oct 0.5k | 287 |
| DCKT @doorcountykayaktours | 8,123 | 38 | 993 reels / 378 carousels | down every month | 4 |
| HPB @houstonpedalbarge | 3,905 | 56 | 346 | Jun 495, Oct 146 | 22 |
| BBK @buffalobayoukayak | 1,006 | 78 | 240 | stopped Aug 23 | 24 |
| Admire NOLA | 247 | 42 | 168 | stopped Sep 29 | 1 |
| Austin Kayak | 3,664 | 6 | 177 | stopped Aug 14 | 0 |
| NKST @kayaknola | 5,309 | ? | ? | API blind | ? |
| HBC, Gravity Trails, Cave Point PP | | 0 | | dormant | 0 |

## What works (ours)

- **E&E:** friend-group + floating sauna on the river. "looking for something different to do with friends in Portland?" = 131k reach, 1,827 saves, 3,389 shares. Seasonal event drops (Fall Equinox) = 9k reach, 549 interactions.
- **NPB:** weird/funny ("Skeet skeet. Get weird this summer") 6.5k reach, 249 shares. Second-line brass on the dock 5.2k. Gators + party ("15 minutes from the Quarter") 4k.
- **DCKT:** guide life humor. "human billboard" 4.5k, "Door County Super Bowl" 2.7k, kayak joust 2.7k, Labor Day tourism-worker joke 2.2k. All short, all staff on camera, captions under 15 words.
- **HPB:** one hit in 4 months: "BYOB and come get LIT Houston" (bachelorette tags) 4.3k reach, 143 shares, on Oct 9.
- **BBK:** bats + skyline at night (1.6k). **Admire NOLA:** gator "log had other plans" 9.6k reach, but zero saves or shares, so it reached people and converted nobody.

## What doesn't (ours)

- Info carousels: route/price/duration/"Comment CAVE" posts. DCKT 94 to 378 reach, 0 saves. HPB price carousels 16 and 39 reach.
- Science/education on E&E: "sauna is not a trend" 850, "a lot happens in 20 minutes" 819. Wellness lectures flop; the social angle wins.
- Generic promo reels: NPB "sunset from a boat" 241, "cosmic dance party" 717. HPB "Come join us, BYOB, near Kemah" 107.
- Volume without a hook: BBK posted 78 times in 12 weeks at a 240 median and stopped. HPB posts more every month and reach falls every month.

## YouTube (28 days to Oct 14)

| Channel | 28d views | Last upload | Note |
|---|--:|---|---|
| Admire NOLA | 54,204 | active | one clip ("She Brought Her Own Concert") = 36.9k |
| E&E | 11,681 | active | every post uploaded twice; copies split views (3,194 vs 217) |
| NPB | 1,309 | Jul (1 unlisted since) | gator + bachelorette titles win |
| HPB | 801 | Jul | "Bachelorette Weekend in Houston" 1.5k; BYOB one-liners 2 to 4 views |
| DCKT | 360 | Jul 23 | Cave Point waves 1.8k, wipeouts 1.2k; rental/"book now" single digits |
| BBK | 212 | Jul 19 | duplicate "(2)" uploads split views |
| AKT | 126 | Jun 21 | same bat-bridge title reposted 5+ times; rope swing won |
| NKST, HAT | n/a | NKST Jun 30 | Analytics API not enabled on the GCP project |
| DC Detours | n/a | | token dead (invalid_grant) |

**YouTube lesson:** the drips died in July and the ones still running post duplicates. Duplicates don't double reach, they halve it. One upload per video, people-on-camera titles, never the same title twice.

## Market study (Apify, Oct 14)

Small samples (about 25 posts per account), handles found by search, so treat it as directional. Raw JSON stayed in the session scratchpad. Total Apify spend about $5.90 across 4 brand accounts.

### NOLA party (NPB, Admire). Benchmarks: Nashville Pedal Tavern, Scottsdale Bachelorette, Savannah Party Cat, Big Tex
- **Named crew as characters wins the segment.** Nashville Pedal Tavern's "Erik makes every ride the BEST ride" did 481k views, and "Dan's already on it" did 80k. Its trash PSA joke hit 7M.
- **Bride-request payoffs:** Scottsdale's bride only asked for Drake, so the whole weekend went Drake. 206k views, likes at 103% of followers.
- **Costume and holiday nights** ("Costumes? Coming out. Drinks? Pouring.") did 599k.
- **Flat:** fleet tours with no people, planner carousels, #nolabachelorette (salons and planners, under 80 likes).
- **TikTok:** @nolapedalbarge's "no more gator hole" rebrand post did 2.5M plays. It's almost certainly our old pre-rename account, so check who has the login. Customer vlogs that mention NPB get 10 to 30k plays.
- **Local field is empty.** Most NOLA party competitors on IG are dead or tiny.

### NOLA swamp (NKST). Benchmarks: Cajun Encounters, Moondance Kayak (WA)
- **Guide deadpan wins.** Moondance's top 5 are all dry guide humor or guide life, at 14 to 100%+ ER ("Don't ask us about Chuckanut sandstone" 39k views on 2.8k followers).
- **The category is abandoned on IG.** Cajun Encounters is the only active competitor (1.5 posts a week). @kayaknola last posted Jul 14.
- **TikTok's viral swamp clips are tourist POVs** (904k, 521k plays), and tourists tag Cajun Encounters, not us.
- Our two best: "We need our time in nature..." (11.4% ER) and "Some girls want yachts... we want murky water and at least one suspiciously large gator" (5%). Identity line first, no CTA.
- **Flat:** gift cards (7 likes), educational nature carousels, scenery-only photos, and the haunted angle by itself (the one ghost-tour account is dying).

### Door County (DCKT, CPPP). Benchmarks: Clearly Tahoe, Door County Trolley, White Gull Inn, Pictured Rocks Kayaking
- **Novelty water visuals:** a glowing clear kayak on Tahoe did 58.6k views on 23k followers.
- **Named guides:** the Trolley's "5 Star Ronnie" and its ghost tour reel got views at 211% of followers.
- **Scarcity in a human voice:** White Gull's "limiting to-go scones to 6" got 10.9% ER.
- **Off-season holds up** for kayak accounts that keep posting: Tahoe Paddle's winter ER is 5.3% vs 2.3% in summer. What works: opening countdowns, snow humor, fall color, team stories.
- **Flat:** weather notices, merch, holiday greetings, "summer please stay."
- @cavepointpp's old reels (5k views on 1.4k followers) beat the main account per follower. It's been dormant since Jun 2025.

### Portland sauna (E&E). Benchmarks: Koti Sauna PDX, Othership, Village Sauna, Sauna Festivaali
- **Small, owner-voiced accounts get 3 to 5% ER; big brands get 0.2%.** E&E sits at 0.73%.
- **Entertainment beats wellness:** Othership's scripted comedy "Episode 4: The Group Chat" did 394k views.
- **Save-the-date + ticket-drop posts** (Festivaali 19% ER), **partner pop-ups** (Village Sauna x local inn, 10.7%), and **giveaways** (the only thing that moves comments at scale).
- **Founder voice:** Koti's owner-intro and personal-story posts get 12 to 15%.
- **Flat:** promo codes, class schedules, "open daily, link in bio."

## The rules (all brands, effective now)

1. **People, not product.** Every feed post has a person in frame in the first 2 seconds. Best of all is a named crew member who recurs (Erik/Dan/Ronnie format).
2. **One joke or one tension per post.** Guide deadpan, local in-joke, gator-or-log, bride's wild request. No feature lists.
3. **Captions 3 to 15 words** for party brands, up to 200 characters for nature brands. 3 to 5 hashtags. No "book now, link in bio" in the first line.
4. **Info content goes to Stories, highlights and the website, not the feed.** Price, route, duration and "what to know" carousels are capped at 1 per week per brand.
5. **Reels over carousels.** Carousels only for save-the-date, social proof (real reviews with faces) or a seasonal mood set.
6. **One upload per video, per platform.** Never the same title twice on YouTube.
7. **Steal formats, not footage.** Series to start: E&E "plans with friends" (proven twice) + save-the-date drops. NPB "Captain [Name]" + bride-request payoffs. DCKT/NKST weekly guide-deadpan reel. HPB bachelorette "BYOB and come get LIT" variants (its only hit).
8. **Boost what earns shares.** Shares per reach is the signal: NPB "Skeet skeet" (249 shares), E&E friends reel (3,389), HPB LIT reel (143). Those three go to Meta as social-proof ads first.

## What changed today (2026-10-14)

- **DCKT carousel drip** (mbp-2 `~/Projects/dckt-carousel-drip`): 7 info carousels moved to `held.json`. The rest is 1 carousel a week, with all 7 reels and all stories kept. Backup: `queue.json.bak-20261014-*`.
- **HPB carousel drip** (mbp-2 `~/hpb-carousels`): 5 of 8 pending carousels set to `held`. The 3 left (team outing, things nobody tells you, Thanksgiving) post weekly on Oct 20, Oct 27 and Nov 5. Backup alongside.
- **E&E YouTube mirror** (mbp-2 `~/.config/ebb-youtube/mirror.py`, synced to vault master, md5 verified): now checks the channel before uploading and skips a reel that's already there. A second, unidentified uploader posts every reel about 45 seconds earlier. That copy usually wins on views, so the mirror backs off. Backup: `mirror.py.bak-predupe-20261014`.

## Still open (needs a person or its own session)

- **Reel queues are empty** for NPB and HPB (bots idle since early Sept), and NKST, BBK and AKT haven't posted since summer. This is the biggest gap. The fix is cutting crew-character reels from Crew Clips footage, which is real editing work.
- **@kayaknola API permission is gone** (#10 error). It needs the System User + App asset assignment in Business Manager (steps in the IG Graph setup memory).
- **Texas has no Apify key**, so there's no Houston/Austin market study yet.
- **DCKT Apify account is at $5.25 of its $5 monthly cap.** NKST is at $3.15.
- **YouTube:** DC Detours token dead (invalid_grant), NKST/HAT Analytics API not enabled on GCP project 250476721704. BBK and AKT have duplicate-title uploads splitting views.
- **The other E&E YouTube uploader** is unidentified (not on mbp-2 launchd, not on the laptop). It could be Kimberlyn's scheduler or the DCKT Mac (unreachable today).
