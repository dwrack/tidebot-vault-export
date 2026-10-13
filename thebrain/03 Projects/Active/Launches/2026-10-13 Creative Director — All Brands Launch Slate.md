# Creative Director: All Brands Launch Slate (2026-10-13)

*Run by /creative-director across every DJL brand on 2026-10-13. One hero idea per brand, the kills shown, the drop plan staged. Nothing here has posted, sent, or spent. David approves per brand.*

## Read this first

- **The week we're launching into.** Hurricane Isaias hit near Destin, FL as a Cat 3 on Oct 9 ([CBS](https://www.cbsnews.com/news/hurricane-isaias-first-storm-2026-atlantic-season-record/)). New Orleans and Houston were spared but the Gulf is still in cleanup. Rule for every NOLA and TX asset this week: no storm, flood, or weather jokes. The TikTok top tag nationally is #hurricaneisaias at 213M views ([Creative Center via Apify, npb key](https://www.tiktok.com/tag/hurricaneisaias)). Don't ride it.
- **The format wave right now is the reveal.** Costume reveal, storytime that ends on a twist, carefree clip under a stressed text overlay ([SocialPilot, Sept 25-Oct 10](https://www.socialpilot.co/blog/tiktok-trends), [Later](https://later.com/blog/tiktok-trends)). #tiktokscaryhorrorcontest is at 45M views / 17.8k posts in 7 days (Apify Creative Center row), Halloween deadline, 60-120s, unverified sponsor. Peaking, usable through Oct 31 only.
- **The brand-response pattern is winning.** Vaseline turned a creator's "Baseline" slip into a stunt within days, no agency ([Marketing Dive H1 roundup](https://www.marketingdive.com/news/best-brand-campaigns-h1-2026-sold-honesty-consumers-buying/819960/)). Every drop plan below has a 48-hour response rule because of it.
- **Apify pulse spend today:** E&E $0.68 (ran earlier today), NPB ~$0.68, CPPP ~$0.68, DCKT $0.12 (reddit only). Estimates from actor list prices; real numbers in console.apify.com. The six brands without their own key (LSKT, HPB, BBK, NKST, NOLA Bike Bar, Admire) were re-pulled on the E&E key after David OK'd it (~$0.61 each, tiktok_trends skipped as duplicate). Their addenda sit at the end of each city section. Reddit returned HTTP 400/502 on every key, so no Reddit rows anywhere today; that is a pulse.py bug to fix.
- **Season reality per brand:** NOLA and TX are in their good-weather window and Halloween is 18 days out. E&E's season starts the first rainy week (this weekend). DCKT is closed, so its launch is a series built for the first freeze. NOLA Bike Bar is revive-or-sell pending: no spend, one cheap option only. Admire NOLA routes, it does not launch.

## Cross-brand verdict (the slate)

| Brand | The one idea | Polarity | Window | Decision David owes |
|---|---|---|---|---|
| NOLA Party Barge | **No Costume, No Boarding.** Deadpan pirate deckhand at the gangway turns away a guy in a polo and a bar-crawl lanyard. Bass Pirates Oct 31, costumes required. | Committed vs uncommitted; Bourbon St. defenders call it elitist | Shoot Tue Oct 20 dusk, drop Wed Oct 21 | Confirm Bass Pirates is live in FH by Oct 20; who plays the polo guy |
| NKST | **The Marshmallow.** One marshmallow on black water, a gator eye surfaces. "That's how some swamp tours guarantee you a gator. We don't. We wait." | Baited wildlife vs waiting; airboat loyalists will say "they all do it" | Shoot Mon Oct 19 dusk (20 min, a $2 bag), drop Thu Oct 22 | Sign off "some tours, historically" wording; batch the shoot ask to Jeffrey with NPB's |
| Ebb & Ember | **Rain Opening Day.** The sauna declares the first rain of the season its opening day. Last frame: a chalkboard on the dock, "OPEN. It's raining." | Pro-rain; the people who complain about Portland weather are the ones we lose | Fires the first morning it pours, target Tue Oct 20 | Confirm the launch bundle (season two + V2 saunas + Banya Mondays); OK a $30 chalkboard; Danesh in for day 5? |
| Austin Kayak (LSKT) | **Reverse Bridge.** 1,000 people on the Congress bridge filmed from one kayak underneath, ends on a cardboard "Nights left: ?" that becomes a nightly countdown until the colony is gone. | Bridge crowd vs the water | Must shoot this week; drop Thu Oct 15 (bats are leaving, Rowing Dock has a bat paddle Oct 30) | Approve the Connor batch message today |
| Buffalo Bayou Kayak | **Drainage Ditch.** Open on a storm grate, match-cut to the bayou 3 miles later: gator, skyline, Waugh bats. | "It's a ditch" vs "it's the destination" | Drop Sat Oct 17 8am, the first cool morning after Friday's front | Same Connor message |
| Houston Pedal Barge | **Conference Room.** Deadpan Q4 team building in windowless Room B, hard cut to the same nine people on the barge. Organic only, ads stay paused. | HR who books the ballroom vs everyone who sat through it | Seed Oct 20, drop Thu Oct 22 | Same Connor message; needs a real corporate booking to shoot on |
| DCKT | **First Ice.** Same rock at Cave Point, filmed the morning the spray freezes, hard-cut to the identical July frame. 2027 opening-weekend pre-sale underneath. | A kayak company posting the day its product is impossible | Pre-built now, fires the first hard-freeze morning (Dec/Jan) | Set the 2027 opening date so FH can list the pre-sale; name Jackson as the backup on the rock |
| NOLA Bike Bar | Zero cost: park the lit bike bar on the Krewe of Boo route Oct 24, film sidewalk reactions. The reaction is the revive-or-sell data point. | n/a | Sat Oct 24 | Is a parking spot on the route even possible, and who holds the keys (Jeffrey or Michael) |
| Admire NOLA / CPPP / Ebike / Airstream | No hero. Admire wraps the NPB hero in the narrated template and hosts the NKST blog. CPPP holds the clear-kayak-photoshoot angle for April. Ebike and Airstream ride the DCKT swarm. | | | None now |

**The one decision that unlocks the most:** approve the Connor batch message (bottom of the Texas section). Austin's window closes with the bats, and it's the cheapest shoot on this list.

## Skill fixes from this run (for Claude, not David)
- `pulse.py` reddit source returned HTTP 400 on BOTH the npb and dckt keys today (0 rows each). The harshmaur actor input or the run-sync call changed; fix before the next pulse. E&E's reddit pull earlier today worked (1 row), so it may be the search-URL form.
- One google_trends term per brand also 400'd ("party boat new orleans"; one of the cppp terms). Same fix.
- No Apify key for `tx` or `la` regions. Six brands are web-only until David runs `~/Desktop/Set Apify Key.command`.

---

## NOLA Party Barge (NPB)

**What's launching (assumption, confirm):** Halloween on the water. The ticketed "Bass Pirates Halloween" boat, Sat Oct 31, 8pm-10pm, 40 seats, $55, BYOB, fire pits after, best costume wins a free charter, plus Oct 30/31 private slots. NYE sits behind it (JT builds those items by Nov 1).
**Audience:** the internet, and bachelorette planners who are mid-search right now.
**Tier:** phone + Jeffrey/JT + one [GEN] shot. No paid; brand Ads are the Oct 14-15 argument with Michael, this stays organic.
**Window:** drop Wed Oct 21. Krewe of Boo is Sat Oct 24, Halloween is a Saturday.

### Pulse (Apify npb key, ~$0.68; reddit and one trends term errored HTTP 400, no rows)
1. "new orleans bachelorette" search is up +1,919% last 14d vs prior 30d (avg 67 vs 3, peak Sep 29). Planners are shopping this week. PEAKING. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=new+orleans+bachelorette&hl=en-US
2. "things to do in new orleans" is down 14% over the same window. Generic listicle demand is soft; the bachelorette niche is where the heat is. TIRED. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=things+to+do+in+new+orleans&hl=en-US
3. #nolathingstodo on TikTok is attraction walkthroughs: JAMNOLA 1.4M, Museum of Illusions 889k, Vue Orleans 729k, all the same "what to expect inside" shape. TIRED, and it's the Astra demo for tourism. https://www.tiktok.com/@alexx_robinson/video/7584490802206854430
4. "if you come to nola, please do an airboat tour!!" 196k plays. Airboats are getting organic love under NOLA tags. (NKST's problem, NPB's reminder that guest-shot beats brand-shot.) PEAKING. https://www.tiktok.com/@hoojagirl/video/7681503332929719566
5. #partyboat globally is Budapest/Marmaris/Split DJ-boat flyers, 150k-500k each, identical. Nobody owns a party-boat voice. EARLY. https://www.tiktok.com/@apolleusdj/video/7668045691658210582
6. IG #nolaparty is bar flyers (The Saint, Beach on Bourbon's "annual pre-Halloween party," 28 likes). The Bourbon Street Halloween is already booked and already boring. TIRED. https://www.instagram.com/p/DeCyu6JOUJt/
7. #tiktokscaryhorrorcontest, #5 US tag, 45M views / 17.8k posts in 7 days; 60-120s, Oct 31 deadline, sponsor unverified. Format is dying on Nov 1. PEAKING. https://www.tiktok.com/discover/tiktok-horror-contest-details
8. Format wave: the costume reveal, and storytime that ends on a twist; sound "Spooky, Scary Skeletons (House VIP Remix)." PEAKING, will be tired by Halloween week. https://www.socialpilot.co/blog/tiktok-trends
9. Krewe of Boo rolls Sat Oct 24, 6:30pm, Marigny through the Quarter to Canal. The city's costume night is a week before ours. TIMING. https://www.kreweofboo.com/
10. Hurricane Isaias, Cat 3 near Destin Oct 9. Nothing about weather, water levels, or "storm" in any NPB asset this month. https://www.cbsnews.com/news/hurricane-isaias-first-storm-2026-atlantic-season-record/

### 12 ideas
1. **No Costume, No Boarding.** A deadpan pirate deckhand at the gangway turns away a guy in a polo and a bar-crawl lanyard. "A boat in New Orleans won't let you on without a costume."
2. **The Pirate Safety Briefing.** Straight-faced Coast Guard briefing that escalates ("in the event of mutiny, the mutineers keep the cooler"). "A party boat posted a safety briefing for pirates."
3. **Lost Bass Pirates.** Found-footage mockumentary: a crew lost on the bayou since 1815 resurfaces Oct 31. "There's a ghost pirate crew on Bayou Bienvenue and you can buy a seat."
4. **The Captain Has Seen Things.** One take, captain to camera, lists Halloween cruise sightings, no smile. "A boat captain listed everything he's seen on Halloween and it's a lot."
5. **Nobody Died.** The review line as the whole ad. "Their best review is two words."
6. **The Bourbon Street Walkout.** A bride in a veil, plastic hurricane, dead eyes, walks off Bourbon mid-crawl, cab, dock, boat pulls away, noise fades to water. "She left Bourbon Street mid-bar-crawl and got on a boat."
7. **Costume Entry #1.** The gator that swims between the barges, judged as the first costume contest entry. "A party boat entered a real alligator in its costume contest."
8. **Flag Raising.** The torn sun-bleached pirate flag goes up the mast at dusk, no words. "Pretty pirate flag."
9. **Backflip Bride, Halloween cut.** The meme clip with a new line. "The bride flipped again."
10. **$55 vs $80.** Side by side: Bourbon hurricane vs a seat on the boat. "They priced a pirate boat against a hurricane."
11. **The Parade Sees Us.** Krewe of Boo spectators spot the pirate boat. "The parade stopped for a boat."
12. **Costume Check on Canal.** The deckhand works the Boo parade route rating costumes "you'd get on / you would not." "A pirate is bouncing Halloween costumes on Canal Street."

| # | Subtract product | Polarity | Text-a-friend | Parody shape | Identity | First 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 No Costume | 8 | 8 | 9 | 9 | 8 | 8 | 50 |
| 2 Safety Briefing | 7 | 5 | 7 | 8 | 6 | 5 | 38 |
| 3 Lost Pirates | 7 | 4 | 8 | 6 | 6 | 7 | 38 |
| 4 Captain Seen Things | 6 | 4 | 7 | 7 | 6 | 4 | 34 |
| 5 Nobody Died | 5 | 3 | 8 | 7 | 5 | 6 | 34 |
| 6 Walkout | 8 | 8 | 8 | 7 | 8 | 9 | 48 |
| 7 Gator Entry | 6 | 3 | 8 | 5 | 6 | 7 | 35 |
| 8 Flag | 2 | 0 | 2 | 1 | 2 | 5 | 12 |
| 9 Backflip cut | 3 | 2 | 5 | 4 | 4 | 7 | 25 |
| 10 $55 vs $80 | 3 | 6 | 5 | 4 | 5 | 2 | 25 |
| 11 Parade Sees Us | 0 | 4 | 7 | 3 | 5 | 6 | 25 |
| 12 Costume Check Canal | 7 | 7 | 8 | 8 | 7 | 7 | 44 |

**Kills.** 2 Safety Briefing: good shape, low stakes, nobody's mad; swarm piece. 3 Lost Pirates: needs a [GEN] budget and 60s, and the polish can't match the premise on a phone. 4 Captain: the inside joke, core only. 5 Nobody Died: the review still hasn't been located (vault search Aug 15), unverified, parked. 7 Gator Entry: safe funny. 8 Flag: the drone reel. 9 Backflip: the meme is an ad asset (167k paid views, 0 likes), not a launch. 10 $55 vs $80: the feature list with a beat. 11 Parade: the boat is on Bayou Bienvenue, not Canal Street; can't be made. 12 Costume Check: strong, but it's the swarm's best day, not the hero; it becomes day 3.

### Top 3 treatments
**1. No Costume, No Boarding.** Logline: a pirate bouncer won't let the uncommitted on the boat. Polarity: people who commit vs people who show up in a polo; Bourbon Street defenders will call it elitist and that's the argument we want. Shape: "the gangway No," a bouncer with one rule, any venue can film its own. First frame: a torn-costume deckhand with a clipboard, dead face, no context. Last frame: the polo guy alone on the dock as the music leaves with the boat.
**6. The Bourbon Street Walkout.** Logline: a bride walks out of her own bar crawl. Polarity: Bourbon Street itself. Shape: the walkout, one continuous move from noise to water. First frame: veil, plastic hurricane, dead eyes in the crowd. Last frame: the boat pulling away, Bourbon inaudible. Risk: a night shoot on Bourbon with a bride and a cab, three locations, needs a real production evening.
**12. Costume Check on Canal.** Logline: the pirate bouncer judges the Krewe of Boo crowd. Polarity: the parade-goers who get a "you would not." Shape: the verdict. First frame: a stranger's costume, then "No." Last frame: "Saturday. 40 seats." Risk: consent on the street, and it's a sequel without a first film.

### The one: No Costume, No Boarding
It works with the boat removed, a bouncer enforcing a dress code is a bit on its own, and it is the one idea that is literally true, costumes are required on the Bass Pirates boat, so the hater reply writes itself. It also gives Jeffrey and JT a character (the deadpan deckhand, the only voice a competitor can't copy, per the meme doc) that carries NYE and every holiday after. Risk: if the 40 seats sell out before Oct 31, keep the private Oct 30/31 slots in the pinned comment so the argument still lands somewhere bookable.

### Hero asset
**Logline:** No costume, no boat.
**Polarity:** the committed vs the uncommitted.
**Format:** 20s vertical, 9:16, one 6s GIF of the "No."
**Lens:** Taika Waititi, Our Flag Means Death register, pirates played completely straight.

| Time | Shot | Source | Sound / text |
|---|---|---|---|
| 0.0-1.5 | Tight: a deckhand in a torn, sun-bleached pirate costume holding a clipboard at the gangway, dead face. No boat visible. | REAL, Jeffrey or JT, dusk Oct 30 at the marina | Dock ambience only. No text. |
| 1.5-5 | Reverse: a guy in a polo, khakis, a bar-crawl lanyard and a plastic hurricane. "We're on the 8 o'clock." Deckhand: "Costume?" Guy: "I'm... a tourist." Deckhand: "No." | REAL, same shoot (a crew friend plays him) | Live audio. The "No." is the sound. |
| 5-9 | Montage, each gets a nod and "go ahead": a bride with a veil over a pirate hat, a guy as a shrimp, two women as one gator. | REAL, Oct 30 private-boat guests with their OK, crew as fallback | Text: "Costumes required. Obviously." |
| 9-13 | The polo guy still on the dock; the thatched barge pulls away behind him, lanterns on, music starting. | REAL, `1-great_2026-08-08_tiki-barge-cruising-past.mov` angle re-shot at dusk Oct 30; fallback the daytime clip graded dark | One bass drop as the boat leaves. |
| 13-17 | [GEN] single cutaway: the thatched barge on black bayou water at night, torn pirate flag, fire-pit glow, cypress silhouettes. Labeled a render in the caption. | [GEN], /seedance-video | Music swells, water. |
| 17-20 | Last frame: the polo guy alone, lanyard, hurricane. Text: "Bass Pirates. Sat Oct 31, 8pm. 40 seats. $55. Costumes required." Logo small. | REAL | Hard cut to silence. |

**Copy-able shape:** the gangway "No." Any bar, boat, or venue can post its bouncer turning away the uncommitted. We want them to.
**Thumbnail:** the deckhand's dead face and clipboard.
**Titles and captions.** IG: "No costume, no boat." Caption: "Bass Pirates. Oct 31, 8pm, 40 seats, $55, fire pits after. Costumes required. Private boats Oct 30 and 31 for crews who want the whole deck. Link in bio." TikTok: on-screen "no costume, no boarding" + caption "we mean it. oct 31. 40 seats. #neworleansbachelorette #nolahalloween #partyboat". X: "No costume, no boarding. New Orleans, Oct 31. Bourbon Street will let anyone in. We won't."

### Drop plan
**T-7 to T-1 (Oct 14-20):** Thu Oct 15 post one still: the clipboard reading "COSTUME CHECK" on the dock, no caption. Jeffrey and JT from their own accounts Fri Oct 16: "something's happening on the bayou the 31st." Mon Oct 19 Instagram Close Friends story to the media list (growth play #10): the deckhand still, "we open the gangway Wednesday." Shoot Oct 30 is too late for the hero, so the hero shoot is Tue Oct 20 at dusk with crew and friends; Oct 30 real-guest costumes feed the swarm.
**T-0 (Wed Oct 21):** IG Reels 12:00 CT, TikTok 12:30, X 1:00 with the polarity line. Jeffrey posts as NOLA Party Barge. Pinned: "Costume or no boat. Too far?" Fan reply: "Correct. Seat 1 of 40 is yours." Hater reply: "You can still come. In a costume. Or rent the whole boat Friday and wear what you want, we won't check." Review-SMS pipe and the h02 Halloween email (Oct 27) carry the deckhand still.
**T+1 to T+7:** Day 2 the 6s "No." GIF and a GBP post. Day 2 the Pirate Safety Briefing (idea 2) as the stitch prompt: "add a rule." Sat Oct 24, Krewe of Boo: the deckhand works the Canal Street route doing costume checks on consenting parade-goers (idea 12), posted Sun Oct 25. Day 5 self-parody: the deckhand turns away the captain. Any venue that posts its own gangway "No" gets a comped seat. Day 7 (Oct 28): Oct 30 costume montage from real guests as the final push.
**48-hour numbers:** views over 10x followers traveled, under 3x didn't. Over 5 comments per 1,000 views means the dress-code argument worked. Report saves and shares. Bass Pirates seats sold out of 40, and Oct 30/31 private slots booked, vs the prior 7 days.
**Kill/boost:** no paid. If it travels, the only amplification is the Oct 27 email and Jeffrey's reply cadence.

### Alternates
**6. The Bourbon Street Walkout.** The purest nemesis film NPB has. Needs one night shoot with a bride, a cab, and Bourbon on a Thursday. Hold for Mardi Gras season when there's a crew and a budget.
**12. Costume Check on Canal.** Becomes day 3 of the swarm; if the hero slips, it can run alone on Oct 25 as a cold open for the week.

### Routing
- /seedance-video: the one [GEN] night-barge shot. One draft, after David approves.
- /ffmpeg-usage: the 20s cut and the 6s "No." GIF; night grade on the cruising-past clip if the dusk re-shoot misses.
- /copywriting-2.0: the pinned comment, the two replies, the X line.
- /social-captions: IG/TikTok/X above plus the SMS line.
- /carousel: Oct 30 costume montage, day 7.
- /growth-plays: log "the deadpan deckhand" as a recurring character play, status Staged; ties to #17 captain POV and #18 anti-marketing stunt.
- /press-release: skip, a ticketed boat is not news. Krewe of Boo weekend tip to one outlet only if the Canal Street costume checks produce a clip worth it.
- Blockers for David: confirm Bass Pirates is built in FH by Oct 20; who plays the polo guy; OK the dusk shoot Oct 20.

## New Orleans Kayak Swamp Tours (NKST)

**What's launching (assumption, confirm):** haunted-swamp season. Manchac at dusk, the Julia Brown legend and the drowned towns, told straight, with the anti-airboat position as the spine. No airboat in frame, ever.
**Audience:** locals and planners, women 25-54.
**Tier:** phone + Jeffrey (interim, one batched ask with NPB) + the vault photo library + one [GEN] shot.
**Window:** drop Thu Oct 22. Hold anything about the 1915 hurricane until the week of Oct 26, two and a half weeks after Isaias, and tell it as history, never as a hook.

### Pulse (web-only; no Apify key for the LA region, run `Set Apify Key.command` for `la`)
1. "if you come to nola, please do an airboat tour!!" 196k plays, guest-shot, "Jacob had us out in that Swamp." The nemesis is winning organically on our own tags. PEAKING. https://www.tiktok.com/@hoojagirl/video/7681503332929719566
2. Manchac folklore is live on TikTok Discover ("cursed bridge spanning an endless swamp," "most haunted swamp in America"), posts about two months old, modest numbers. EARLY, unowned. https://www.tiktok.com/discover/the-manchac-swamp-bridge
3. French Quarter ghost tours (LaLaurie, Lafitte's, lamp-lit walks) dominate "haunted New Orleans" on TikTok. That is the crowded lane; the swamp is the empty one. TIRED. https://www.tiktok.com/discover/ghost-tours-new-orleans-tour-guide
4. The grounded story: Julia Brown was a real herbalist in Frenier; Frenier and Ruddock were wiped out by the 1915 hurricane surge. Sibling site already tells it. https://crescentcitykayak.com/blog/haunted-manchac-swamp/
5. Gator baiting was ordered stopped in Jefferson Parish in 2014 after a viral clip; no statewide law, and a Dec 2025 Yelp review quotes an airboat guide saying it isn't practiced anymore. So: "some tours, historically," never a named operator. https://abc13.com/post/viral-video-leads-to-investigation-of-swamp-tour-guide/110789/
6. #tiktokscaryhorrorcontest, #5 US, 45M views, dies Oct 31, sponsor unverified. Borrowable for a cutdown only. PEAKING. https://www.tiktok.com/discover/tiktok-horror-contest-details
7. Format wave: creepy-fact storytime ending on a twist. PEAKING. https://www.socialpilot.co/blog/tiktok-trends
8. Hurricane Isaias, Oct 9, Cat 3. No storm framing, no "the swamp is rising," nothing. https://www.cbsnews.com/news/hurricane-isaias-first-storm-2026-atlantic-season-record/
9. October heat flirting with records in NOLA this week; dusk paddles are the product, golden hour is late. https://www.fox8live.com/

### 12 ideas
1. **The Marshmallow.** One marshmallow drifting on black swamp water, nothing else, then a gator eye behind it. "A kayak company posted a marshmallow floating in a swamp and it's the creepiest thing I've seen."
2. **The Silent Film.** 20s of swamp silence, one airboat roar offscreen, silence again. "A Halloween ad that's just silence and one engine."
3. **Portrait of an Airboat Captain.** Mockumentary. "They made a fake documentary about an airboat guy."
4. **Julia Brown's Last Song.** Guide tells the legend, twist: she meant it, 1915. "A voodoo priestess said she'd take the town with her and she did."
5. **What the Gators Hear.** Split audio, engine vs paddle drip. "Listen to this with headphones."
6. **Nobody Died.** The review line. "Their best review is two words."
7. **Cancel Your Airboat.** Guide account: show your airboat confirmation, we'll take you instead. "A kayak guide is paying people to cancel airboat tours."
8. **The Owl.** A barred owl stares at you for 10 seconds. "An owl looked at me."
9. **Haunted, No Actors.** A guide promises ghosts, deadpan, delivers a heron, a log, a silence. "A swamp tour is calling French Quarter ghost tours fake."
10. **30 Strangers Screaming.** Audio of an airboat crowd screaming over cypress stills. "That's what the swamp hears every hour."
11. **Golden Hour Cypress.** The reel. "Pretty swamp."
12. **The Contest Entry.** 90s found-footage kayak night paddle for #tiktokscaryhorrorcontest. "A kayak company entered TikTok's horror contest."

| # | Subtract product | Polarity | Text-a-friend | Parody shape | Identity | First 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 Marshmallow | 8 | 9 | 9 | 9 | 8 | 9 | 52 |
| 2 Silent Film | 8 | 7 | 7 | 7 | 7 | 4 | 40 |
| 3 Airboat Captain | 7 | 8 | 8 | 7 | 5 | 6 | 41 |
| 4 Julia Brown | 7 | 3 | 8 | 6 | 7 | 7 | 38 |
| 5 Gators Hear | 5 | 6 | 6 | 6 | 6 | 3 | 32 |
| 6 Nobody Died | 5 | 3 | 8 | 7 | 5 | 6 | 34 |
| 7 Cancel Airboat | 4 | 8 | 8 | 7 | 6 | 3 | 36 |
| 8 Owl | 6 | 1 | 4 | 5 | 5 | 8 | 29 |
| 9 Haunted No Actors | 7 | 7 | 8 | 7 | 7 | 5 | 41 |
| 10 Screaming | 6 | 6 | 6 | 5 | 6 | 3 | 32 |
| 11 Golden Hour | 2 | 0 | 2 | 1 | 2 | 3 | 10 |
| 12 Contest Entry | 5 | 2 | 6 | 3 | 4 | 6 | 26 |

**Kills.** 2 Silent Film: strong, but the first 1.5s is a still swamp and it scrolls; it becomes the swarm's audio piece. 3 Airboat Captain: needs an airboat in frame, forbidden, dead. 4 Julia Brown: real and good, but it's a hurricane story 13 days after Isaias; held to the Oct 26 week as a storytime cutdown. 5 Gators Hear: the feature list with a beat. 6 Nobody Died: review still unlocated, parked. 7 Cancel Airboat: already growth play #12, guide account, not a hero. 8 Owl: no polarity. 10 Screaming: a committee edit of 2 and 5. 11 Golden Hour: the drone reel. 12 Contest: borrowed trend one week before it dies, night-paddle liability, sponsor unverified.

### Top 3 treatments
**1. The Marshmallow.** Logline: this is how some tours guarantee you a gator. Polarity: airboat operators and the 196k people who loved Jacob's airboat; our tribe is anyone who's ever felt weird about a baited animal. Shape: the floating marshmallow, an eerie object anyone can film in any water. First frame: a marshmallow on black water, tight, unexplained. Last frame: cypress mirror, "We don't. We wait."
**9. Haunted, No Actors.** Logline: a ghost tour that refuses to fake it. Polarity: French Quarter ghost tours. Shape: the deadpan promise and the honest payoff. First frame: a guide whispering "listen" at dusk. Last frame: a heron. Risk: safe-adjacent; the Quarter tours won't fight back, they're too big to notice.
**3. Portrait of an Airboat Captain.** Dead on arrival because the brand rule bans the airboat in frame. Listed so David sees the better version of idea 1 is the one that never shows the enemy.

### The one: The Marshmallow
It is one image, it needs no product, no guide, no footage we don't have, and it turns the nemesis into an object instead of a competitor, which keeps the lawyers calm and the comments on fire. It gives NKST a Halloween asset that's actually scary without touching the hurricane. Risk: the comments will name operators; the reply script must never confirm one, and the caption says "some tours, historically" with the 2014 Jefferson Parish link.

### Hero asset
**Logline:** The scariest thing in the swamp is a marshmallow.
**Polarity:** baited wildlife vs. waiting. Airboat loyalists will say "they all do it" or "it's harmless." Good.
**Format:** 18s vertical, 9:16, 6s GIF of the marshmallow and the eye.
**Lens:** Villeneuve. Dread in stillness, one sound.

| Time | Shot | Source | Sound / text |
|---|---|---|---|
| 0.0-1.5 | Tight: one white marshmallow on black water, duckweed at the edge, no horizon. | REAL, Jeffrey's phone at the Manchac launch at dusk, a $2 bag | Water only. No text. |
| 1.5-6 | It drifts. Slow. Nothing happens. | REAL, same | A single low drone note starts. |
| 6-10 | Behind it, a ripple, then a gator eye and brow surface, hold. | [GEN] (the one generated shot) or REAL if the crew gets it; fallback slow push on `manchac-alligator-swimming-duckweed.jpg` | The note holds. Text: "Marshmallows." |
| 10-13 | Cut to black. | n/a | Silence. Text: "That's how some swamp tours guarantee you a gator." |
| 13-17 | Cypress mirror at golden hour, a kayak bow drifting in, no motor. | REAL, `1-great_2026-06-28_cypress-swamp-mirror-reflections.mov`, then `manchac-kayak-bow-calm-river-reflection.jpg` | Paddle drip. Text: "We don't. We wait." |
| 17-18 | Last frame: the still swamp. Text: "See the swamp the right way." Logo small. | REAL | Cut to silence. |

**Copy-able shape:** the floating marshmallow. Any lake, pool, or bathtub, one marshmallow, "this is how X gets you to show up."
**Thumbnail:** the marshmallow, tight.
**Titles and captions.** IG: "The scariest thing in the swamp." Caption: "Some tours, historically, tossed marshmallows to bring gators to the boat (Jefferson Parish ordered it stopped in 2014). We paddle, we wait, we see them anyway. Manchac at dusk, October. Link in bio." TikTok: on-screen "marshmallows" + caption "this is how some swamp tours guarantee a gator. we just wait. #swamptour #louisianaswamp #hauntedneworleans". X: "A marshmallow is the scariest thing in the Louisiana swamp. Ask what your tour feeds the gators."

### Drop plan
**T-7 to T-1 (Oct 15-21):** Thu Oct 15 one still: a bag of marshmallows on the dock, caption "we don't." Nothing else. Jeffrey shoots the marshmallow and the cypress bow Mon Oct 19 at dusk (the hero needs 20 minutes and a bag). Close Friends story to the media list Tue Oct 20: "Thursday, the swamp's Halloween film is one marshmallow."
**T-0 (Thu Oct 22):** IG Reels 12:00 CT, TikTok 12:30, X 1:00. Jeffrey posts as New Orleans Kayak Swamp Tours. Pinned: "Would you still book a tour that feeds the gators to make sure you see one?" Fan reply: "Same. We've never needed to. Dusk this week is the best gator light of the year." Hater reply ("it's harmless / they all do it"): "Not all. Jefferson Parish banned it in 2014 for a reason. We'd rather wait ten minutes than train an animal." Never name an operator in replies. Review-SMS to past guests: the marshmallow still, "you saw yours the slow way."
**T+1 to T+7:** Day 2 GBP post and a /seo-blog-writer post "Why we don't bait gators (and why some tours did)." Day 2 the Silent Film (idea 2) as the audio cutdown, headphones-on prompt. Day 3 stitch: "what did your swamp tour feed the gators?" Mon Oct 26: Julia Brown storytime (idea 4), told straight, 45s, no jokes, no "storm." Day 5 self-parody: a marshmallow in the office coffee. Any creator who posts their own floating-marshmallow gets a seat.
**48-hour numbers:** views over 10x followers traveled; over 5 comments per 1,000 views the baiting argument worked; report saves and shares; dusk bookings vs prior 7 days, and whether any airboat operator responds (publish the response, that's film two).
**Kill/boost:** no paid proposed. If it travels, the Oct 26 storytime rides it.

### Alternates
**9. Haunted, No Actors.** The deadpan ghost tour that delivers a heron. Fires any dusk, no props. Use if David wants to avoid the baiting fight entirely.
**4. Julia Brown's Last Song.** The real story, held to Oct 26. Strong on its own if the week stays quiet.

### Routing
- /seedance-video: the gator eye surfacing behind the marshmallow, black water, duckweed, dusk, photoreal. One draft.
- /ffmpeg-usage: 18s cut from the phone shot, the cypress mirror clip, and the stills; 6s GIF.
- /copywriting-2.0: pinned question and the two replies; the Jefferson Parish line must stay exact.
- /social-captions: IG/TikTok/X plus the SMS.
- /seo-blog-writer: "Why we don't bait," day 2, links the 2014 abc13 story.
- /growth-plays: log "the floating marshmallow" under #12 (cancel-your-competitor) as its public face, status Staged.
- /press-release: skip until an operator responds; then it's a story.
- Blockers for David: confirm Jeffrey can do the 20-minute dusk shoot Oct 19 (batch it with the NPB Oct 20 shoot in one message), and sign off on the "some tours, historically" wording.

### NOLA Bike Bar / Admire NOLA
**NOLA Bike Bar (zero cost, revive-or-sell pending):** park the bike bar, lit, on the Krewe of Boo route Sat Oct 24 as the only float that isn't in the parade, three bikes, crew in costume, phone on a tripod filming sidewalk reactions and strangers climbing on for photos. One post, "Your legs, your playlist, your city," no spend, no pedaling shown as the feature. If the sidewalk doesn't react, that's a data point for the sell side; if it does, it's the revive reel. Needs a parking spot on the route and whoever's holding the keys, Jeffrey or Michael to confirm.
**Admire NOLA:** it routes, it doesn't launch. Wrap the NPB hero in the narrated-video template as "New Orleans Halloween, from the water" on the umbrella channel and point every seat link at Bass Pirates; host the NKST "Why we don't bait" blog on the umbrella site for the SEO side; carry the Bike Bar parade clip if it lands. No asset of its own this month.

### Apify pulse addendum (ran after the sections above, E&E key per David, ~$0.61 per brand, reddit failed on all three)
**NKST.** "swamp tour new orleans" +364% last 14d (48 vs 10) and "airboat tour" +328% (40 vs 9); "kayak swamp tour" fell to zero. People are shopping swamp tours this month and the airboat word is winning the search box. PEAKING. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=swamp+tour+new+orleans&hl=en-US. The swamp clips that travel are mood, not tour: "Louisiana swamps feel like another world" 3.8M, a #swamp moodboard cut to the True Detective theme 988k, a "spooky quiet scary atmosphere piano" boat ride 758k. Dread in stillness is the aesthetic already working. https://www.tiktok.com/@thelifeofjandj/video/763797994726031695, https://www.tiktok.com/@witch33s/video/7636731857098312982. **Verdict: The Marshmallow stands; its Villeneuve lens is what the tag already rewards. Put "swamp tour" (not "kayak swamp tour") in the caption.**

**NOLA Bike Bar.** #neworleansbachelorette is the biggest organic thing in the city: "My girls in nola" 5.0M, "The MOTHER of all bachelorette parties" 2.3M. https://www.tiktok.com/@jinnylee49/video/7622457897624161567. "new orleans bar crawl" search went from 0 to a peak on Oct 10. EARLY. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=new+orleans+bar+crawl&hl=en-US. **Verdict: the Krewe of Boo park-and-film stays as the zero-cost test, but if the sidewalk reacts, the revive case is a bachelorette product, not a party-bus alternative.**

**Admire NOLA.** #neworleansthingstodo is attraction walkthroughs (JAMNOLA 1.4M, Museum of Illusions 889k, Vue Orleans 729k) and "one pass, 25 attractions" posts (369k). "new orleans things to do" flat, "new orleans tours" +10%. TIRED format. **Verdict: no change, Admire routes. The narrated-video wrapper for the NPB hero should borrow the walkthrough cadence those clips use, since that is what the umbrella audience watches.**

---

## Ebb & Ember

**What's launching (assumption, confirm):** winter season two, the two V2 saunas (18'x32' build in progress), and Banya Mondays with Danesh. Treated as one launch: "the rain is back, so are we."
**Audience:** Portland locals. Not tourists, not the wellness-tourism crowd.
**Tier:** phone + Kimberlyn + one [GEN] shot max.
**Window:** first real rain week of the season. Dry and 76F through Fri Oct 16, rain and 59F by Mon Oct 19. Drop Tue Oct 20.

### Pulse
1. "sauna portland" +364% and "floating sauna" +374% last 14d vs prior 30d. Category is warming into winter. EARLY. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=sauna+portland
2. "Americans HAVE NO IDEA HOW TO JUST BE STILL #saunas" 317k plays. Stillness-as-skill is the argument people want to have. PEAKING. https://www.tiktok.com/@miriam_tinny/video/7597931407985478967
3. Visit Finland "survival guide to Finnish sauna culture" 627k. Deadpan rules-of-sauna format works. PEAKING. https://www.tiktok.com/@visitfinland.com/video/7608872792007757078
4. "I thought yall knew how to control those #sauna" 673k. Sauna fail/etiquette humor travels. PEAKING. https://www.tiktok.com/@roux.tv/video/7602360781769837854
5. Wim Hof winter cold plunge 3.6M. Bro-plunge is the dominant frame and it is TIRED (our nemesis). https://www.tiktok.com/@iceman_hof/video/7331877219641429280
6. "first cold plunge ever and it was in fact cold" 651k. The plunge face still lands, unpolished beats polished. PEAKING. https://www.tiktok.com/@pepperonimuffin/video/7540459195653491999
7. Costco cold plunge + chiller setup 225k. Home plunge is commoditizing; river water is the differentiator. EARLY. https://www.tiktok.com/@costco.savvy/video/7645080161259425038
8. Portland rain returns this weekend, Monday high 59 after 76 on Friday. The city's mood flips in 72 hours. TIMING. https://www.kptv.com/2026/10/13/warm-workweek-cooler-weekend-ahead and https://www.koin.com/weather/summer-like-heat-fades-as-rain-fall-temps-arrive-in-portland/
9. Format wave: the "reveal" and the "I just want to be OK" carefree-clip-vs-stressed-overlay. PEAKING, usable for a week more. https://www.socialpilot.co/blog/tiktok-trends and https://later.com/blog/tiktok-trends/
10. IG #pdxwellness is dead weight: IV drips, chiro spotlights, 13-57 likes. Nobody owns Portland sauna on IG yet. EARLY. https://www.instagram.com/p/DeNT468IMgp/

### 12 ideas
1. **Rain Opening Day.** The sauna treats the first rain of the season like a ski resort treats first snow: a ceremonial "we're open" the morning it pours. "A sauna in Portland just declared opening day for rain."
2. **The Portland Sauna Rules.** Deadpan Visit Finland-style etiquette guide, read by a guest in a towel, one rule is "no mantras." "There's a sauna that bans intention-setting."
3. **Plunge Face Hall of Fame.** 30 real post-plunge faces, no music, no words. "Just faces of people who jumped in the Columbia in October."
4. **$200 vs $49.** Split screen: a performative wellness session (crystals, sound bowl) vs. the sauna, same 90 minutes. "They put a sound bath next to a sauna and let you pick."
5. **Nobody's Here.** A lone woman walks the dock in a downpour at night, steps into the lit sauna, the only person for a mile. "Portland's loneliest-looking sauna is the point."
6. **The River Is 48 Degrees.** A thermometer on a string, lowered in once a week all winter, posted every Monday. "A sauna posts the river temp like a weather report."
7. **Banya Monday: the venik.** Danesh beats a guest with birch branches, straight-faced, no explanation. "A guy in Portland will hit you with a tree on Mondays."
8. **Still for 90 seconds.** One unbroken shot of a guest sitting still in the sauna, on-screen counter, most people can't finish. "A video dares you to watch someone do nothing for 90 seconds."
9. **Steam column in the storm.** [GEN] stunt: the sauna lit from inside in a night downpour, steam rising. Beautiful, no argument. "Pretty sauna in rain."
10. **The commute.** Shot from a car on I-5 in rain, cut to the sauna window looking at the same rain. "Same rain, two windows."
11. **Season two trailer.** Montage of the new saunas being built, guests, river. "Our new saunas are done."
12. **Cold plunge vs Costco.** Guest tries the Costco tub, then the Columbia, grades both. "Someone rated Costco's cold plunge against a river."

| # | Subtract product | Polarity | Text-a-friend | Parody shape | Identity | First 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 Rain Opening Day | 8 | 8 | 9 | 9 | 9 | 7 | 50 |
| 2 Sauna Rules | 7 | 8 | 8 | 8 | 7 | 5 | 43 |
| 3 Plunge Faces | 6 | 3 | 7 | 7 | 6 | 8 | 37 |
| 4 $200 vs $49 | 7 | 9 | 7 | 7 | 7 | 4 | 41 |
| 5 Nobody's Here | 8 | 6 | 6 | 5 | 8 | 9 | 42 |
| 6 River Temp | 5 | 2 | 6 | 8 | 7 | 3 | 31 |
| 7 Venik | 7 | 7 | 9 | 6 | 6 | 9 | 44 |
| 8 Still 90s | 9 | 7 | 8 | 9 | 7 | 2 | 42 |
| 9 Steam column | 3 | 0 | 4 | 2 | 3 | 7 | 19 |
| 10 Commute | 5 | 2 | 5 | 6 | 6 | 4 | 28 |
| 11 Trailer | 1 | 0 | 2 | 1 | 2 | 1 | 7 |
| 12 vs Costco | 6 | 5 | 7 | 6 | 4 | 5 | 33 |

Kills: 3 plunge faces, no one to lose, it's a swarm piece not a hero. 4 split screen, strong polarity but the first frame is a sound bowl, and it punches a real local business. 5 nobody's here, gorgeous, but it's the drone reel with a person in it. 6 river temp, a series slot, not a launch. 8 still 90s, great shape, dead first frame, keep for the swarm. 9 steam column, zero polarity, pretty sauna in rain, the drone reel. 10 commute, safe, nobody texts it. 11 trailer, the Astra demo. 12 Costco, review-content, borrowed format a week late.

### Top 3 treatments
**A. Rain Opening Day.** Logline: Portland's floating sauna declares the first rain of the season its opening day. Polarity: Portlanders who hate the rain vs. the ones who secretly live for it; the hate-rain crowd will call it smug. Shape: "Opening Day" for weather, a ski-resort ritual stolen by a sauna. First frame: a woman in a towel on the dock, face up, rain hitting her, eyes closed, no context. Last frame: a chalk sign on the dock, "OPEN. It's raining." Cheap, two-person shoot, Kimberlyn's phone, ships the day the rain starts.

**B. The Portland Sauna Rules.** Logline: a deadpan etiquette guide for the sauna where rule four is "no intention-setting." Polarity: wellness-ritual people vs. heat-and-water people. Shape: numbered rules read flat, Visit Finland style, remixable by any sauna. First frame: "RULE 1" over a guest mid-plunge. Last frame: "RULE 7: leave feeling different, or don't. Both fine." Risk: the 673k and 627k sauna videos prove the format, which also means it's crowded.

**C. Banya Monday: the venik.** Logline: on Mondays, a Ukrainian ceremonialist hits Portlanders with birch branches and nobody explains why. Polarity: "that's assault" vs. "that's the oldest sauna tradition on earth." Shape: the whack, no explanation, caption only. First frame: branches mid-swing. Last frame: the guest grinning, red, "see you Monday." Risk: Danesh is a partner, not staff, needs his OK, and it's one weekday product, not the season.

### The one: Rain Opening Day
It's the only idea where the product is optional: a city arguing about whether rain is good is a video with or without a sauna in it, and it drops the exact day the whole city's mood flips. It also sets a yearly slot E&E owns forever, like First Ice for Door County. Risk: it rains Saturday instead of Monday and we ship late; the shoot has to be ready Friday and fire the morning it pours.

### Hero asset
**Logline:** Portland's floating sauna declares the first rain of the season opening day.
**Polarity:** pro-rain. The people who complain about Portland weather for six months are the ones we lose, on purpose.
**Format:** 22s vertical, 9:16, one 6s GIF cut of the chalk sign. No 60s version.
**Director's lens:** Aki Kaurismäki. Flat faces, no smiles until the last frame, rain as the main character.

| Time | Shot | Source | Sound / text |
|---|---|---|---|
| 0.0-1.5 | Tight: a woman in a towel on the dock, face tilted up, rain on her face, eyes shut. No logo, no sauna visible. | REAL, Kimberlyn phone, Mon/Tue morning shoot | Only rain on wood. Text: none. |
| 1.5-5 | Pull wide: she's alone on the dock, gray river, the lit sauna behind her. She does not go in. | REAL, same shoot; fallback still `rainy-dock-floating-sauna-gray-sky-portland.jpg` | Rain. Text fades in: "Portland, October 19." |
| 5-9 | Cut: second guest walks down the gangway in a raincoat, drops it, towel underneath, same face-up pose. Then a third. | REAL, same shoot (3 members or friends) | Rain only. Text: "Day one." |
| 9-13 | The turn: inside, steam, the window streaming with rain, guests sitting still, nobody talking. Hold 4s. | REAL, `sauna-window-boat-on-river.jpg` angle, shoot it as video | First sound of the stove: one ladle of water, hiss. |
| 13-17 | Payoff: one guest walks out, drops into the Columbia, the plunge face, a laugh. | REAL, `floating-sauna-roof-jump-gray-day-portland.jpg` angle | Splash, the laugh, then back to rain. |
| 17-20 | [GEN] single shot: the sauna from the water at night in a downpour, steam column lit from inside, Marine Drive lights behind. Mark it as a cutaway, never as documentary. | [GEN], /seedance-video prompt | Rain swells. |
| 20-22 | Last frame: chalk sandwich board on the dock in the rain: "OPEN. It's raining." Small logo under it. | REAL, buy a $30 chalkboard | Hard cut to silence. |

**Copy-able shape:** "Opening Day" for weather. Any Portland business can post its own "OPEN. It's raining." board, and we want them to.
**Thumbnail / first frame:** the face-up-in-rain woman, cropped tight.
**Titles and captions.** IG: "Opening day." Caption: "It's raining. We're open. That's the whole post." TikTok: on-screen "the first rain is our opening day" + caption "Portland's floating sauna. Rain is the season." Portland Reddit (r/Portland, posted by a member, not the brand): "The floating sauna on the Columbia apparently treats the first rain like opening day. Went this morning."

### Drop plan
**T-7 to T-1 (Oct 13-19):** Tue Oct 13 post the chalkboard blank with "soon" and nothing else. Thu Oct 15 Kimberlyn shoots the dry-day b-roll and recruits 3 members for the rain shoot. Fri Oct 16 Instagram Close Friends story to the media list (growth play #10): "we open for rain Monday, come stand on the dock." Sat/Sun: nothing. Weather call Sunday night.
**T-0 (Tue Oct 20, or the first morning it actually rains):** shoot 7-8am, cut by 11am, post IG Reels 12:00 PT, TikTok 12:30, a member posts the Reddit thread 4pm. Kimberlyn posts, signs as Ebb & Ember. Pinned comment: "Is the rain the best part of living here or the worst? Be honest." Fan reply: "Opening day's every rainy day from here. See you on the dock." Hater reply: "Fair. We'll be out here anyway, 180 degrees inside, 50 in the river. Come argue in person." Email/SMS to the Période list within the hour: the chalkboard still, "It's raining. We're open."
**T+1 to T+7:** Day 2 the 6s chalkboard GIF and a GBP post. Day 2 blog: "Why rain is sauna season in Portland" via /seo-blog-writer. Day 3 the Still-for-90-seconds cut (idea 8) as the stitch prompt: "can you sit this long." Day 4 Plunge Faces from the shoot as a carousel (/carousel). Day 5 Banya Monday teaser with Danesh (idea 7) if he's in. Day 5 parody ourselves: the chalkboard says "OPEN. It stopped raining. Still open." Any Portland business that posts its own board gets a comped social session.
**48-hour numbers:** views over 10x followers means it traveled, under 3x it didn't. Comments per 1,000 views over 5 means the rain argument worked. Report saves and shares, not likes. Périod bookings vs the prior 7 days.
**Kill/boost:** over 10x, boost the hero only, on Meta, Portland metro, 25-54, only if David approves spend (/meta-ads-insider). Under 3x, no boost, run the Sauna Rules alternate the following Tuesday.

### Alternates
**B. The Portland Sauna Rules.** Fires any day, no weather dependency, rule four ("no intention-setting") carries the polarity. Use if the rain slips past Oct 23.
**C. Banya Monday venik.** Needs Danesh's yes. Strongest single image of the three. Use as the Nov follow-up so Mondays get their own launch.

### Routing
- /seedance-video: the one [GEN] shot (night, downpour, steam column, Marine Drive lights). One draft only.
- /ffmpeg-usage: the 22s cut and the 6s chalkboard GIF from Kimberlyn's clips.
- /carousel: Plunge Faces, day 4.
- /social-captions: the IG/TikTok/Reddit lines above, per platform.
- /copywriting-2.0: the pinned comment and the two replies.
- /seo-blog-writer: "Why rain is sauna season in Portland," day 2.
- /growth-plays: log "Rain Opening Day" as a yearly slot, status Staged, and tie it to play #10 (Close Friends list).
- /press-release: skip. Rain is not news. Pitch the Portland Monthly editor the "opening day for rain" line instead, inside the thread already open.
- Blockers for David: confirm the launch bundle (season two + V2 saunas + Banya Mondays), OK the $30 chalkboard, and whether Danesh is in for the day-5 piece.

---

Pulse for all three is WEB-ONLY. No Apify key exists for the tx region (resolve.py stops). Have David double-click `~/Desktop/Set Apify Key.command` and pick a Texas vault so the next run gets TikTok sounds and Google Trends momentum. Nothing below was spent.

## Austin Kayak Tours (LSKT)

**What's launching (assumption):** "Last Bats." The final two weeks of the Congress bridge emergence seen from the water, then the season closes. The launch is a countdown, not a product.
**Audience:** Austin locals who have stood on the bridge and never once been under it. **Tier:** phone + crew clips, one [GEN] shot max. **Window:** drop Thu Oct 15, countdown runs to the first night the refuge logs no flight.

**Pulse (web-only, verified Oct 13):**
- Partial migration started Oct 7, ~501,000 bats left for Bracken; bats still flying nightly as of Oct 12, flight window 7:25-7:55pm, sunset 7:04. Peaking, then gone. https://austinbatrefuge.org/congress-avenue-bridge/
- No source gives a last-flight date; the refuge log is the only live gauge. Early (a countdown nobody is running). Same URL.
- Statesman says best viewing windows end mid-September; October is the tail. Tired as a "go see the bats" post, early as a "they're leaving" post. https://www.statesman.com/entertainment/article/austin-bats-time-congress-bridge-bracken-22094780.php
- ACL weekend two ended Oct 11; Zilker lawn is torn up and partly closed, Great Lawn reopening date unannounced. The city's attention is on the park, not the lake. Tired. https://www.austintexas.gov/parks/news/austin-parks-and-recreation-prepares-zilker-park-acl-fest-weekend-two
- Rowing Dock already lists a one-night Halloween Bat Paddle Oct 30. Competitor is on the bat angle; we have to be earlier and stranger. https://www.rowingdock.com/happenings/
- Lady Bird Lake blue-green algae warning still on the Rowing Dock page. Don't show dogs in the water. Same URL.
- TikTok format wave: storytime-with-a-twist and the reveal. Peaking through Halloween. https://www.socialpilot.co/blog/tiktok-trends
- "I just want to be OK" carefree-clip-vs-stressed-overlay format. Peaking. https://later.com/blog/tiktok-trends
- Vaseline "Baseline" proved the win is responding in days with no agency. https://www.marketingdive.com/news/best-brand-campaigns-h1-2026-sold-honesty-consumers-buying/819960/

**12 ideas:**
1. Bat Clock: a public countdown to the last flight, posted nightly from the water. "A kayak company is running a doomsday clock for the bats."
2. Reverse bridge: 1,000 people on the bridge filmed from one kayak underneath. "They're all looking up. We're the only ones looking at them."
3. Bat obituary: deadpan eulogy for the colony, read on the water. "Someone did a funeral for 1.5 million bats."
4. Last Flight Lottery: free seat for whoever guesses the final emergence date. "Guess when the bats leave, win a kayak."
5. Silent film: 30s of the column, no music, no words. "No sound. Just bats."
6. Tuesday 5:30pm: a guide leaves a desk job mid-call and is on the water in 12 minutes. "15 minutes from 6th Street."
7. Bat migration as a breakup text. "The bats are ghosting Austin."
8. Bat census: guide counts out loud until the number is absurd. "He got to 40,000 and gave up."
9. Guide to camera: "Why I quit standing on the bridge." One take.
10. ACL hangover paddle: Zilker mud vs flat water the morning after. "The lawn is closed. The lake isn't."
11. Bracken Cave FaceTime: call the bats at their destination. "We called Bracken to see if they got there."
12. Drone reel of the column at sunset with piano. "Pretty."

| # | Subtract | Polarity | Text | Shape | Identity | 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 | 8 | 7 | 9 | 9 | 8 | 7 | 48 |
| 2 | 7 | 8 | 8 | 7 | 9 | 9 | 48 |
| 3 | 7 | 6 | 8 | 8 | 6 | 7 | 42 |
| 4 | 3 | 2 | 6 | 5 | 4 | 3 | 23 |
| 5 | 6 | 3 | 5 | 4 | 5 | 6 | 29 |
| 6 | 4 | 5 | 6 | 6 | 7 | 4 | 32 |
| 7 | 5 | 4 | 7 | 7 | 4 | 4 | 31 |
| 8 | 6 | 2 | 7 | 7 | 5 | 5 | 32 |
| 9 | 4 | 6 | 5 | 3 | 5 | 2 | 25 |
| 10 | 3 | 5 | 6 | 4 | 6 | 4 | 28 |
| 11 | 6 | 3 | 7 | 6 | 4 | 6 | 32 |
| 12 | 1 | 0 | 2 | 1 | 2 | 0 | 6 |

Kills: 4 a contest nobody argues about, safe funny. 5 a mood piece, no side. 6 the Astra demo of a Tuesday paddle. 7 a caption, not a film. 8 inside joke, dies after the first count. 9 founder-to-camera with nothing at stake. 10 borrowed trend one week late, ACL is over. 11 a bit that needs a paragraph. 12 the drone reel, zero on polarity and first frame.

**Top 3:** (1) Bat Clock. Logline: a kayak outfit runs a doomsday clock for Austin's bats. Polarity: tourists who think the bats are permanent vs locals who know the season. Shape: the nightly number card. First frame: a hand-painted number on cardboard held up from a kayak at dusk. Last frame: the number hits 0 over an empty bridge underside. (2) Reverse Bridge. Logline: everyone looks up, one boat looks at them. Polarity: bridge crowd vs the water. Shape: the flipped POV. First frame: 1,000 faces lit by phones, shot from below. Last frame: the column pours over them. (3) Bat Obituary. Logline: a eulogy for 1.5 million temporary residents. Polarity: sentimental vs "they're bats." Shape: the deadpan reading. First frame: black suit in a kayak. Last frame: "Survived by Austin."

**The one: Reverse Bridge, with the Bat Clock number card as its last frame.** It only works from the water, which is the whole brand argument, and the first frame (a crowd lit by phones, seen from underneath) is the strangest image anyone will see that night. Risk: a dim dusk clip reads muddy on phones; the 1-great clips in the index prove the light is there, but the under-bridge crowd shot is new and has to be filmed this week.

**Hero asset.** Format: stunt / one impossible image, 22s vertical. Lens: Villeneuve (scale from below, silence first).
- 0.0-1.5s: Hard cut in on the under-bridge crowd, hundreds of faces and phone screens, shot straight up from a kayak. No music. Water slap on the hull. On-screen: nothing.
- 1.5-5s: Slow pull back revealing the kayak bow and the railing line above. Text: "They've been looking up for 40 years."
- 5-11s: `1-great_2026-08-21_bat-column-sunset-sky.mov` then `1-great_2026-08-23_congress-bridge-bat-sunset.mov`, the column pours over the crowd. First sound: wingbeats, raised to a roar.
- 11-16s: `1-great_2026-08-13_austin-skyline-bat-paddle.mp4`, kayaker looks up. Text: "Nobody told them you can watch from the water."
- 16-20s: [GEN] one shot, the same bridge underside at the same hour, empty, no bats, a single kayak. Text: "Oct 7: 501,000 left for Bracken."
- 20-22s: Cardboard number held up from the kayak: "Nights left: ?" Last frame holds on the question mark. Logo only here.
- Copy-able shape: **the Number Card.** Any business can hold up a countdown from an odd vantage.
- TikTok title: "austin has been watching the bats from the wrong side for 40 years." Caption: "They leave soon. Nobody knows the night. We'll post the number every evening from under the bridge until it's 0. #austin #congressbridge #batsofaustin"
- IG: same video. Caption: "Last Bats. Nightly number from the water until the colony is gone. Which night do you think is the last one?"

**Drop plan.** Seed Oct 13-14: one still, the cardboard "?" from the water, no caption. Guide (Tristan or Peter, through Connor) posts "something's happening from the water Thursday." T-0 Thu Oct 15, TikTok 11:30am CT then IG 1pm. Posted by Connor's lane. Pinned: "Be honest, have you ever seen the bats from the water?" Fan reply: "The water side is the quiet side. Seats are up for the last nights." Hater reply ("it's just bats"): "1.5 million just bats. Stand under them, then tell us." Swarm T+1-7: nightly Number Card post at 7:15pm from the dock (15s, same frame), day 2 duet prompt "show us your bridge-side video, we'll show the water side," day 3 guide reaction, day 5 self-parody (number card for the Rowing Dock crowd), GBP post day 2, SMS to past guests within the hour of T-0. 48h: views over 10x followers boost the hero only with David's spend call; comments per 1,000 views over 5 means the polarity worked. Kill: no seed by Oct 14, push a week (the bats may be gone, so the fallback is the Obituary).

**Alternates.** Bat Clock standalone: the nightly card without the hero, cheaper, runs itself. Bat Obituary: shoot in one take the night the refuge logs zero, 90s, the response video when the countdown ends.

**Routing:** /seedance-video for the single [GEN] empty-bridge shot; /ffmpeg-usage for the cut from the five index clips; /social-captions for the nightly cards; log as a growth play under #14 (shareable proof) with a status line. No paid.

## Buffalo Bayou Kayak (BBK)

**What's launching (assumption):** Fall season opens the moment the Friday front breaks the heat, with Waugh bridge bats from the water as the opening-week product.
**Audience:** Houstonians who drive over the bayou daily. **Tier:** phone + crew clips, one [GEN]. **Window:** seed Oct 14-15, drop Sat Oct 17 morning, the first cool day.

**Pulse (web-only, verified Oct 13):**
- Feels-like 100s Tuesday; strong front reaches Houston Friday Oct 16, Saturday the coldest night with lows in the 50s, highs upper 70s, sharp humidity drop. Peaking: the whole city will post about it. https://fox26houston.com/weather/houston-weather-tuesday-october-13-2026 and https://spacecityweather.com/
- Usual first true fall front is Oct 22, so this one is early and will feel like an event. https://www.houstonchronicle.com/news/houston-weather/forecast/article/houston-weekend-rain-cooler-days-gulf-development-22458707.php
- Waugh bridge colony ~250-300k, bat chats run through October, then thin out. Peaking, two weeks left. https://www.houstonchronicle.com/news/houston-texas/trending/article/houston-bat-bridges-20266537.php
- Radar-captured emergence clips have gone viral before (KHOU, Chron). Tired as a format, usable as a reference. https://www.khou.com/article/news/local/radar-bat-colonies-houston/285-bd3d9c58-434c-4ae0-87eb-81a8dcd0ac6e
- Isaias hit Destin Oct 9 as a Cat 3; Houston spared. No flood or storm humor this week. https://www.cbsnews.com/news/hurricane-isaias-first-storm-2026-atlantic-season-record/
- Astros finished 81-81, manager interviewing elsewhere; the city is in a self-pity mood. Early for a "Houston has one thing left" angle. https://www.foxsports.com/mlb/houston-astros-team
- No Reddit or TikTok thread on "nothing to do in Houston" surfaced in web search; the discourse is real but unverified this week. Don't build on it as a trend. https://www.yahoo.com/lifestyle/articles/world-cup-2026-houston-guide-202702632.html
- Reveal / twist storytime format peaking through Halloween. https://www.socialpilot.co/blog/tiktok-trends

**12 ideas:**
1. First Cool Morning: one continuous shot from the water at 7am Saturday, skyline over the trees, breath visible. "Houston at 58 degrees from the bayou."
2. Drainage Ditch: open on a storm-drain grate, cut to the same water 3 miles later with a heron. "The ditch has a gator."
3. Kayak commute: paddle from Montrose to downtown in a suit, timed against I-10. "He beat traffic in a kayak."
4. Bayou cleanup stunt (growth play #18): "we spent the ad budget on trash bags." "They filmed themselves hauling 400 lbs out of the bayou."
5. The Gator Nobody Believes: `gator-cruising-green-bayou` clip with a city bus in frame. "There's a gator downtown and nobody cares."
6. Bat chat from the water: Waugh emergence with the deck crowd above. "Everyone's on the bridge. We're under it."
7. Reverse Hill Country: couple packs the car for Hill Country, drives 3 miles, unloads at the bayou. "They drove to the Hill Country and ended up downtown."
8. Heron counting: guide tallies birds by name like a roll call. "She knows the herons by name."
9. Astros consolation: "Houston lost 81. The bayou is undefeated." Deadpan.
10. Flood line: paddle past the 2017 Harvey high-water mark. "Serious."
11. Skyline POV with piano. "Pretty."
12. Guide to camera: "I moved here and nobody told me about this." One take.

| # | Subtract | Polarity | Text | Shape | Identity | 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 5 | 7 | 6 | 8 | 6 | 38 |
| 2 | 8 | 8 | 9 | 9 | 8 | 9 | 51 |
| 3 | 7 | 6 | 8 | 8 | 7 | 7 | 43 |
| 4 | 7 | 7 | 8 | 7 | 8 | 6 | 43 |
| 5 | 6 | 5 | 8 | 5 | 7 | 7 | 38 |
| 6 | 5 | 4 | 6 | 5 | 6 | 6 | 32 |
| 7 | 5 | 6 | 7 | 6 | 6 | 3 | 33 |
| 8 | 4 | 2 | 5 | 4 | 5 | 3 | 23 |
| 9 | 5 | 6 | 7 | 5 | 6 | 4 | 33 |
| 10 | 3 | 3 | 4 | 2 | 3 | 5 | 20 |
| 11 | 1 | 0 | 2 | 1 | 2 | 0 | 6 |
| 12 | 3 | 4 | 4 | 2 | 4 | 2 | 19 |

Kills: 1 beautiful, only works because the product is nice (the Astra demo, cold edition); keep the shot for the hero. 5 a one-off, no mechanic. 6 same idea as Austin, weaker colony. 7 committee edit, two jokes stapled. 8 inside joke. 9 safe funny, and the city doesn't want to laugh yet. 10 wrong week, grief is not a hook. 11 drone reel. 12 nothing at stake.

**Top 3:** (2) Drainage Ditch. Logline: the thing you call a ditch has a gator and a skyline. Polarity: Houstonians who say it's a ditch vs the ones who've been on it. Shape: the grate-to-water match cut. First frame: a storm grate, rain running in. Last frame: heron takes off in front of the skyline. (3) Kayak Commute. Logline: a man in a suit beats I-10 by water. Polarity: drivers vs paddlers. Shape: the split-screen race. First frame: a tie in a kayak. Last frame: he walks into a downtown lobby, dripping. (4) Trash Bags. Logline: we spent the ad budget on trash bags. Polarity: "clean it or shut up about nature." Shape: the receipt. First frame: a Home Depot receipt for 400 bags. Last frame: the pile on the dock.

**The one: Drainage Ditch.** It is the nemesis sentence said out loud and then disproved in nine seconds, and the match cut is a shape every city with an ugly river can steal. Risk: the water is brown in half the index clips; the cut has to land on the green-water gator and golden-hour shots only, or the film agrees with the insult.

**Hero asset.** Format: short film, 24s vertical. Lens: Bourdain (ugly place, honest eye).
- 0.0-1.5s: Macro of a street storm grate, water pouring in, traffic noise. Text: "Houston calls this a ditch."
- 1.5-4s: Match cut on the water line to `3-usable_2026-07-18_kayak-launch-pov-bayou.mp4` (the slide-in only, 2s), same brown water, same sound.
- 4-9s: `2-good_2026-08-08_gator-cruising-green-bayou.mp4`, hold, no text. Traffic fades, bayou ambience up.
- 9-14s: `1-great_2026-06-27_kayak-pov-houston-skyline.mov` then `2-good_2026-06-12_bayou-bridge-golden-paddle.mp4`. Text: "3 miles from the grate."
- 14-19s: `1-great_2026-08-08_kayakers-watch-bat-emergence.mp4`, the Waugh column. Text: "300,000 bats. Downtown."
- 19-22s: [GEN] one shot, the same storm grate at dawn with a heron standing on it, skyline reflected in the puddle. Text: "The ditch is the destination."
- 22-24s: `1-great_2026-08-07_kayakers-cheering-victory-arms.mp4`, logo, "Saturday's the first cool one."
- Copy-able shape: **the Grate Cut.** Any ugly-river city can do grate-to-water.
- TikTok title: "houston calls this a ditch." Caption: "3 miles from the grate there's a gator, a heron, and 300,000 bats. Front hits Friday. First cool paddle Saturday. #houston #buffalobayou #htx"
- IG: same. Caption: "Your backyard bayou. Say ditch again."

**Drop plan.** Seed Oct 14: the storm-grate macro as a 3s clip, no caption. Oct 15: a guide (Axel or Dillon through Connor) posts "front hits Friday, I know where I'll be Saturday." T-0 Sat Oct 17, TikTok 8am CT (the first cool morning, people are outside and posting), IG 11am. Pinned: "Ditch or destination? Be honest." Fan reply: "The front did the hard part. Saturday slots are open." Hater reply ("that water is disgusting"): "It's brown after rain and green after a week. Come on the green week." Swarm: 6s GIF of the Grate Cut on X, day 2 duet prompt "film your nearest grate, we'll find the water," day 3 trash-bag cleanup clip (play #18) as the second film, day 5 self-parody (grate-to-parking-lot), GBP post day 2, SMS to past guests Saturday 9am. 48h: 10x followers boosts hero only on David's call; comments per 1,000 over 5. Kill: front stalls past Saturday, hold the drop to the first morning under 65.

**Alternates.** Kayak Commute: needs a weekday morning shoot and a suit, ship it week 2 as the second film. Trash Bags (#18): already ranked, make it the day-3 swarm piece, not the hero.

**Routing:** /seedance-video for the heron-on-grate [GEN]; /ffmpeg-usage for the seven index clips; /carousel from the Grate Cut stills after the hero; log under growth play #18 with status "hero shipped, cleanup as swarm."

## Houston Pedal Barge (HPB)

**What's launching (assumption):** Fall and holiday party season: Halloween weekend, Friendsgiving, corporate. Ads paused on purpose by David and Michael, so this is organic only, zero spend.
**Audience:** Houston locals planning a group night. **Tier:** phone by Connor or Isabella Walker, plus the existing YouTube "Birthday Cruise On Clear Lake" footage; one [GEN]. **Window:** seed Oct 20-21, drop Thu Oct 22, two weekends before Halloween.

**Pulse (web-only, verified Oct 13):**
- Same front: Friday Oct 16 cools Houston, weekend highs upper 70s, lows 50s. The first outdoor-party weather of the year. Peaking. https://spacecityweather.com/
- Astros 81-81, Espada interviewing in Seattle, season called an embarrassment. The city wants somewhere to put its pride. Early. https://www.foxsports.com/mlb/houston-astros-team
- Isaias missed Houston; no storm jokes. https://www.cbsnews.com/news/hurricane-isaias-first-storm-2026-atlantic-season-record/
- TikTok Halloween reveal format (costume reveal, home tours, twist storytimes), Spooky Scary Skeletons house remix. Peaking, tired by Oct 25. https://www.socialpilot.co/blog/tiktok-trends
- "I just want to be OK" overlay format (carefree clip, stressed text). Peaking. https://later.com/blog/tiktok-trends
- Vaseline "Baseline": respond in days, no agency. https://www.marketingdive.com/news/best-brand-campaigns-h1-2026-sold-honesty-consumers-buying/819960/
- NPB's own YouTube data: HPB's best organic video is 7.5k views vs NPB's 167k paid; the party-boat meme engine lives in NOLA, not Houston (vault doc, Party Boat Meme Engine, Sept 2026). HPB needs its own shape, not a NOLA hand-me-down.
- "Nothing to do in Houston" discourse not verifiable in web search this week; treat as a standing nemesis, not a trend.

**12 ideas:**
1. Conference Room: a deadpan corporate team-building session filmed in a windowless room, cut to the same team on the barge. "The HR lady is on a boat now."
2. Safety Briefing: a straight-faced Coast Guard-style briefing that escalates ("in the event of a bad playlist"). "The safety video is the ad."
3. Tell Me Houston Is Boring: a full barge, skyline lit, no words, one caption. "Say it again."
4. Astros Group Therapy: a support group for fans, held on the water. "81 and 81. Now get on the boat."
5. The View Nobody's Seen: a lifelong Houstonian sees the skyline from the water, reaction only. "She's lived here 40 years."
6. Worst Team Outing Confessions: strangers read their worst corporate outing stories on deck. "Someone did a trust fall at a Chili's."
7. Halloween costume reveal on the gangway, group by group. "40 skeletons boarded a barge."
8. Friendsgiving on the water: a full table set on deck. "They did Thanksgiving on a boat."
9. Bachelorette vs corporate split screen, same boat. "Same boat, different Tuesday."
10. Drone reel with the skyline and piano. "Pretty."
11. Captain Isabella to camera: "What people say when they see the skyline." One take.
12. Date-night upgrade: dinner-and-a-movie vs the barge. "Tired."

| # | Subtract | Polarity | Text | Shape | Identity | 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 | 8 | 8 | 9 | 9 | 7 | 8 | 49 |
| 2 | 8 | 6 | 8 | 9 | 6 | 8 | 45 |
| 3 | 4 | 7 | 7 | 5 | 8 | 5 | 36 |
| 4 | 6 | 7 | 8 | 6 | 7 | 6 | 40 |
| 5 | 5 | 4 | 6 | 5 | 7 | 5 | 32 |
| 6 | 7 | 5 | 8 | 7 | 6 | 6 | 39 |
| 7 | 3 | 2 | 5 | 4 | 5 | 4 | 23 |
| 8 | 4 | 3 | 6 | 5 | 5 | 4 | 27 |
| 9 | 4 | 4 | 5 | 5 | 4 | 3 | 25 |
| 10 | 1 | 0 | 2 | 1 | 2 | 0 | 6 |
| 11 | 3 | 4 | 4 | 2 | 4 | 2 | 19 |
| 12 | 2 | 3 | 4 | 3 | 3 | 2 | 17 |

Kills: 3 the brand overview with a caption, passes on polarity only. 5 the Astra demo (showing it working). 7 borrowed trend, one week late by drop day. 8 feature with a beat. 9 committee edit. 10 drone reel. 11 nothing at stake. 12 the brand slogan as a video. 6 survives to alternate, 4 survives as a response video if the Astros news breaks again.

**Top 3:** (1) Conference Room. Logline: the team-building day, filmed exactly as sad as it is, then the boat. Polarity: HR and office managers who book the ballroom every quarter vs everyone who has sat through it. Shape: the two-room cut. First frame: a tray of stale donuts under fluorescent light. Last frame: the same tray on the deck rail, skyline behind, someone finally eats one. (2) Safety Briefing. Logline: a deadpan maritime safety video that slowly admits it's a party. Polarity: people who hate "fun" corporate content vs people who'll quote it. Shape: the numbered-rule escalation. First frame: a captain's hat and a laminated card. Last frame: "Rule 11: the skyline is mandatory." (3) Astros Group Therapy. Logline: a support group for 81-81. Polarity: fans who want to laugh vs fans still mad. Shape: the circle of chairs on a boat. First frame: a man in an Altuve jersey introducing himself. Last frame: the circle, skyline, "we'll get 'em next year."

**The one: Conference Room.** It names HPB's actual buyer (the person who books the team outing) and the nemesis (the ballroom) in one cut, and it costs a borrowed meeting room and a phone. Risk: the barge half has to look like a real company outing, not a bachelorette; shoot it on an actual corporate booking or it reads as a bit.

**Hero asset.** Format: deadpan corporate, 28s vertical. Lens: Wes Anderson for the room (centered, symmetric, dead), handheld for the boat.
- 0.0-1.5s: Centered tray of donuts under fluorescent light, a hum. Text: "Team Building Day. Q4."
- 1.5-7s: Static wide of nine employees in a windowless room, a facilitator holds a ball of yarn. Nobody moves. A clock ticks. Text: "Conference Room B. 2:14pm."
- 7-10s: Close on one employee's face. She blinks. The yarn lands in her lap.
- 10-12s: Hard cut, handheld, wind, music hits: the same nine people on the barge, Isabella at the helm, Clear Lake or the bayou behind (phone footage from a real corporate booking, Connor or Isabella shoots; fallback is the existing "Birthday Cruise On Clear Lake" YouTube footage).
- 12-20s: The yarn ball thrown across the deck, caught, people shouting. Skyline or open water. Text: "Same team. Same afternoon. Same budget."
- 20-24s: [GEN] one shot, the empty conference room, chairs pushed back, the donut tray, the clock still at 2:14. Text: "Conference Room B is available."
- 24-28s: The tray on the deck rail, someone eats a donut, laughs. Logo. "Houston has a waterfront. Get on it."
- Copy-able shape: **the Room B cut.** Any venue can film the sad default then the hard cut to theirs.
- TikTok title: "your Q4 team building, before and after." Caption: "Conference Room B is still available if you want it. #houston #teambuilding #htx #corporateevents"
- IG: same. Caption: "Tell your office manager it's the same budget. Houston has a waterfront."

**Drop plan.** Seed Oct 20: the donut tray still, "2:14pm," no caption. Oct 21: Isabella posts "filmed something in a conference room today, don't ask." T-0 Thu Oct 22, TikTok 11:30am CT, IG 1pm, posted by Connor's lane. Pinned: "What's the worst team outing you've been forced to attend?" Fan reply: "Send this to whoever books yours. Halloween weekend and Friendsgiving dates are open." Hater reply ("our team building is fine"): "Then you've never been handed a ball of yarn. Lucky." Swarm: day 2 the confession prompt (idea 6) as a duet video, day 3 Isabella reaction, day 4 corporate proof post (play #21, "booked every year since"), day 5 self-parody (Room B on the boat, yarn included), GBP post day 2, email to past corporate bookers within the hour of T-0. 48h: comments per 1,000 over 5, saves and shares reported. No boost: ads are paused on purpose, so the kill/boost rule is skip boost entirely unless David and Michael reverse the pause.

**Alternates.** Safety Briefing: 20s, shoot on any booking with Isabella reading a laminated card, ship week 2. Astros Group Therapy: hold as the response video if the Espada story breaks; 24-hour turnaround, Vaseline rule.

**Routing:** /seedance-video for the empty Room B [GEN]; /ffmpeg-usage to cut phone footage; /copy-mentors for the 11 safety rules if the alternate ships; log under growth play #21 (corporate social proof) with status. Zero paid.

### Apify pulse addendum (ran after the section above, E&E key per David, ~$0.61 per brand, reddit failed on all three)
**Austin (LSKT).** "congress bridge bats" search +2,842% last 14d vs prior 30d (avg 11 vs 0), "austin kayak" +493% (22 vs 4). People are searching the bats right now, the countdown is landing into live demand. PEAKING. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=congress+bridge+bats&hl=en-US and https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=austin+kayak&hl=en-US. On TikTok the lake is owned by Retro Boat Rentals (1.6M, 172k) and "book a water activity in Austin" listicles (636k); nobody is posting from under the bridge. TIRED format, EMPTY slot. https://www.tiktok.com/@rachellately/video/7348084 and https://www.tiktok.com/@dailyxsarahtonin/video/7671008860546551054. **Verdict: Reverse Bridge stands, and ship it this week.**

**Buffalo Bayou (BBK).** "kayak houston" +321% (16 vs 4), "buffalo bayou" +76% (59 vs 33). EARLY, warming. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=kayak+houston&hl=en-US. The polarity is already on TikTok: a greenscreen "kayaking in the buffalo bayou?" set to Mozart's Lacrimosa, 756k plays, i.e. the city mocking the idea. That clip is the hater we're answering, quote it in the day-2 stitch. https://www.tiktok.com/@talkswithreggie/video/7667781914010422559. Downtown water is being sold by Discovery Green bumper boats and clear kayaks (4.2M, 462k, 442k), 30-minute rentals, no nature in frame. https://www.tiktok.com/@prettygirleatshouston/video/7509551934165126446. Expect "the Buffalo Bayou serial killer" (604k) in the comments; the hater reply should not engage it. https://www.tiktok.com/@10wayz._/video/7572300425546812702. **Verdict: Drainage Ditch stands, stronger than before.**

**Houston Pedal Barge (HPB).** "houston bachelorette" +2,035% (38 vs 2, peak Oct 2). That is the single biggest demand spike in the whole portfolio pulse and the Conference Room hero does not speak to it. https://trends.google.com/trends/explore?date=today+3-m&geo=US&q=houston+bachelorette&hl=en-US. Houston TikTok this fortnight is downtown fall date nights and pumpkin patches (569k, 517k, 444k). PEAKING. https://www.tiktok.com/@after9houston/video/7687267031619521823. No Houston party-boat voice exists on the tag; the boat clips are DMV and Caribbean (440k, 374k). EMPTY slot. **Verdict: keep Conference Room as the hero (it's the only one with a nemesis), but the day-2 swarm piece becomes a bachelorette cut, the same nine-people format with a bride: "Bachelorette, before and after" (hotel-room pregame under fluorescent light, hard cut to the deck). Add #houstonbachelorette to every caption. If David would rather chase the spike directly, swap the hero for the bachelorette cut and run Conference Room in November for corporate holiday parties. His call.**

## Connor batch message

Staged for David, not sent. One Slack message to Connor:

"Hey Connor, three small asks, all this week, all phone-only. (1) Austin: Thursday evening, get one clip from a kayak straight up at the bridge crowd before the bats come out, and hold up a cardboard '?' for a still. That's the whole shoot. (2) BBK: Saturday is the first cool morning. One guide posts Thursday that the front's coming. We cut the hero from the clips library, nothing new needed. (3) HPB: next corporate booking, have Isabella film 20s of the group on deck, plus 10s of any conference room before they leave the office. I'll send exact shot cards for each. Reply with which days work and I'll stop bugging you."
---

## Door County Kayak Tours (DCKT)

**What's launching (assumption, David to confirm):** "First Ice," a recurring calendar-slot series: the morning Cave Point's spray starts freezing to the cliffs, filmed from the same rock every year. Built now, dropped the first freeze morning (Dec or Jan), with the 2027 opening-weekend pre-sale as the booking hook under it.
**Audience:** the internet at large, plus Milwaukee and Chicago planners (older, FB and IG first).
**Tier:** David's phone on the rock, drone library, Crew Clips (102 DCKT clips), one [GEN] shot max.
**Window:** first hard-freeze morning after a northeast blow. No date. Everything is pre-built and waits.

### Pulse (DCKT Apify pull was reddit-only today, ~$0.12 on the dckt key; CPPP pull was still running at write time)
1. r/wisconsin upvotes Sturgeon Bay landmark photography hard: the Canal North Pierhead Light (+115) and the Bayview Bridge (+48), both by Aaron Johnson. Single still, named photographer, no caption. **Peaking.** https://reddit.com/r/wisconsin/comments/1wlg4d1/the_sturgeon_bay_canal_north_pierhead_light_aaron/
2. La Sirena (Door County) made the NYT 50 Best Restaurants; r/DoorCounty +68, 14 comments. Door County is in a "national list" mood this month. **Early.** https://reddit.com/r/DoorCounty/comments/1wjd5rv/la_sirena_named_one_of_new_york_times_50_best/
3. "New favorite Wisconsin beach" (+56, 15 comments): locals argue about which shoreline is best. Argument format works here. **Peaking.** https://reddit.com/r/wisconsin/comments/1wvd443/new_favorite_wisconsin_beach/
4. Fall color peaks the third week of October, northern tip first. No 2026 report found. Leaf content is the saturated channel right now. **Tired.** https://www.doorcounty.com/newsletter/find-fall-colors-in-door-county/
5. Cave Point does not freeze over; wave spray "can shoot 20 to 30 feet" and freezes in layers on the cliffs, "constantly forming and reforming." The ice is built by storms, not cold. **Early (season hasn't started).** https://www.travelwisconsin.com/article/natural-attractions-and-parks/find-winter-adventure-at-cave-points-ice-formations
6. The sea caves are "visible only from a kayak or when scuba diving." From December to April nobody can reach them. That's the sentence. https://doorcountystay.com/cave-point-park-a-natural-treasure-of-door-county/
7. Fox 11 runs a "Cave Point icy wonders draw visitors" story most winters; local TV will cover the ice without being asked. **Recurring.** https://fox11online.com/news/local/door-countys-icy-wonders-draw-visitors-to-cave-point-county-park
8. Green Bay freezes "eight to 12 weeks or more" most winters; Coast Guard icebreaking near Sturgeon Bay ran late January 2026. Bay ice is February; cliff ice is December. Film the cliffs. https://www.glc.org/dailynews/20260128-coast-guard-advises-icebreaking-greenbay/
9. TikTok format wave this fortnight: the reveal, and storytime that ends on a twist. **Peaking.** https://www.socialpilot.co/blog/tiktok-trends
10. Nothing viral found for Door County ice in 2026 yet. The slot is open.

### 12 ideas
1. **First Ice.** Same rock, same frame, the morning the spray sticks. "This kayak company films the exact same rock every year the day it freezes."
2. **Locked Out.** The caves you can't reach for 140 days, filmed from the one place you can't be. "The sea caves close for winter and nobody has a key."
3. **The Drone Reel.** Golden-hour cliffs, piano. "Pretty Door County video."
4. **The Quiet Cave.** A tandem kayak enters a cave, everyone goes silent, 20 seconds of nothing. "A tour where the whole group shut up."
5. **The Guide Who Noticed.** A guest letter read over footage: mother-in-law, 15 years off the water, cried in the cave. "A kayak guide made a 70-year-old cry (good)."
6. **Conveyor Belt.** Deadpan mockumentary of an assembly-line outfitter: numbered guests, laminated card, 90-second cave. "A kayak company roasted their competitors with a fake tour."
7. **Ice Shove.** The bay pushing ice onto shore, time-lapse. "Lake Michigan is eating the beach."
8. **Spray Count.** A guide stands on the rock while waves throw spray 30 feet over them, counting winters. "A guy stood under a 30-foot wave for a sauna ad."
9. **The 2027 Ballot.** Locals vote on which cave gets a name. "Door County is naming a cave by Facebook poll."
10. **Last Paddle.** The final kayak of the season being hung in the rack, one take. "The saddest 15 seconds in Wisconsin."
11. **Cherry vs. Cave.** A split screen arguing which is the real Door County. "A kayak company picked a fight with cherry pie."
12. **Ice Cold Open.** A reveal: 1.5s of a frozen cliff, then the same frame in July. "Same rock, 6 months apart."

| # | Subtract product | Polarity | Text-a-friend | Parody shape | Identity | First 1.5s | Total |
|---|---|---|---|---|---|---|---|
| 1 First Ice | 8 | 5 | 8 | 9 | 8 | 8 | 46 |
| 2 Locked Out | 7 | 6 | 8 | 7 | 7 | 7 | 42 |
| 3 Drone Reel | 2 | 0 | 2 | 1 | 2 | 1 | 8 |
| 4 Quiet Cave | 6 | 3 | 6 | 7 | 6 | 5 | 33 |
| 5 Guide Who Noticed | 4 | 2 | 7 | 4 | 5 | 4 | 26 |
| 6 Conveyor Belt | 7 | 7 | 7 | 8 | 5 | 6 | 40 |
| 7 Ice Shove | 7 | 2 | 6 | 3 | 6 | 7 | 31 |
| 8 Spray Count | 6 | 4 | 7 | 6 | 5 | 8 | 36 |
| 9 Ballot | 5 | 6 | 6 | 5 | 7 | 2 | 31 |
| 10 Last Paddle | 5 | 1 | 5 | 6 | 4 | 3 | 24 |
| 11 Cherry vs Cave | 5 | 6 | 7 | 6 | 5 | 4 | 33 |
| 12 Ice Cold Open | 7 | 3 | 8 | 8 | 6 | 7 | 39 |

**Kills.** 3 Drone Reel: the named failure mode, every outfitter has one, zero polarity. 4 Quiet Cave: the brand overview with the sound off, and we have no winter cave footage. 5 Guide Who Noticed: beautiful, but only works because the product is kind; Astra demo in a cardigan. 7 Ice Shove: the bay is February, the footage belongs to the weather channel, nothing to copy. 8 Spray Count: safe funny with a real safety liability on the ledge. 9 Ballot: participation without an image; the first frame is a poll. 10 Last Paddle: the inside joke, core only. 11 Cherry vs Cave: a committee edit of two brands' content pillars. 12 Ice Cold Open: absorbed into #1 as the copy-able shape, not its own film.

### Top 3 treatments
**1. First Ice.** Logline: every winter, the day Cave Point freezes, one person films one rock, forever. Polarity: a kayak company posting on the day it is most impossible to kayak; summer-only operators will call it pointless, the Door County faithful will defend it as the truest thing posted all year. Shape: the fixed-frame anniversary shot (the "same rock" cut, July to ice in one hard cut). First frame: a sheet of white ice with cedar branches, no horizon, unreadable. Last frame: the July frame, same cedars, emerald water, text "Opens May 2027 (date unconfirmed, David sets it)."
**2. Locked Out.** Logline: the caves nobody can reach for 140 days. Polarity: a brand telling you that you cannot have the thing. Shape: the countdown stamp ("Day 1 of 140"). First frame: the mouth of the sea cave from the water, July, zoom to black. Last frame: the same cave mouth sealed with ice, from the cliff.
**6. Conveyor Belt.** Logline: a mockumentary of the outfitter that runs you through in 90 seconds. Polarity: names the nemesis in a county where everyone knows which operator it is. Shape: the ticket-number guest. Risk: DCKT's tone is warm, not snark; Door County is small; the target will know.

### The one
**First Ice.** It needs no product, no guests, no season, no staff in an empty-chair winter, and it builds a slot DCKT can own for ten years at the cost of one morning on a rock. The single risk: the freeze arrives on a morning David isn't in Door County, so the shot has to be reachable by a named local backup (Jackson) with the frame marked on the rock.

### Hero asset
**Logline:** Same rock. Every year. The morning it freezes.
**Polarity:** we post the exact moment our product becomes impossible.
**Format and length:** series slot, 18 seconds, 9:16, with a 6-second GIF of the hard cut. No long cut.
**Script:**
- 0.0-1.5s: REAL (phone, Dec). Tight on layered white ice over limestone, cedar twigs locked inside it, wind audible, nothing explains the frame. On-screen: nothing.
- 1.5-5s: REAL (phone). Pull back on the same tripod mark: the full Cave Point ledge glazed, a wave hits and the spray hangs, freezes mid-air feel. Natural sound only, wind and the concussion of the wave. Text: "Cave Point. December 14." (whatever the date is).
- 5-9s: REAL (Crew Clips `1-great_2026-07-20_waves-crashing-cliff-ledge.mp4`). Hard cut, no transition, to the identical framing in July: turquoise water, same ledge, same cedars. The cut is the whole film. Text: "Same rock. July."
- 9-13s: REAL (`1-great_2026-07-06_sea-cave-tandem-kayak.mov`). Two guests paddle into the cave mouth over green water. Text: "The caves are closed for 140 days."
- 13-16.5s: [GEN] one shot: the same cave mouth sealed by a curtain of ice, seen from the water, nobody in frame. Labeled in caption as a render, never passed as a photo.
- 16.5-18s: REAL. Back to the ice frame from 0.0. Text: "First Ice, year one. Opens May 2027." Logo small, last half second.
**Sound:** no music. Wind, water, one wave. If a platform needs a sound, use the ambient track as an original sound so others can reuse it.
**Copy-able shape:** "the same-rock cut." Any brand with a fixed landmark can post July-to-ice in one hard cut; that's the parody and the point.
**Thumbnail / first frame:** the unreadable white ice with cedar twigs.
**Titles and captions.**
- FB: "Same rock. Every year. The morning it freezes. First Ice, year one. The caves are closed until May. Opening weekend 2027 goes on sale today."
- IG: "First Ice. Same rock, every year. Day 1 of 140 without the caves. Opening weekend 2027 is live at the link."
- TikTok: "we film the same rock the day it freezes. every year. this is year one #doorcounty #cavepoint #lakemichigan"
**Lens:** Malick for the ice, Anderson for the fixed frame. No Bourdain narration; nobody talks.

### Drop plan
- **T-7 to T-1 (seed):** the day the forecast shows a northeast blow with lows in the teens, post one still: the July rock with a marker X and the caption "we'll be here." No explanation. Jackson's own account: "something's happening at Cave Point this week, bring spikes." Plant nothing on Reddit; r/wisconsin posts photographers' stills on their own, so the seed there is the still itself, credited to whoever shot it, no brand in the title.
- **T-0:** FB first at 11am CT the morning after the freeze (older audience, shares to family), IG at noon, TikTok at 1pm. Who posts: David, or the scheduler if he's not in Door County (Jackson shoots, David posts). Pinned comment: "Is this the best day of the year at Cave Point or the worst?" Fan reply: "Both. That's why we film it." Hater reply ("who cares, you can't even kayak"): "Correct. 140 days. We'll be here May 16." Email and SMS to every 2026 guest within the hour: the ice still, the line, "you were on this rock in July," pre-sale link.
- **T+1 to T+7:** day 1 the 6s same-rock GIF; day 2 a /carousel of 8 frames from the clip library titled "What the ice is hiding"; day 2 GBP post and a /seo-blog-writer post "Cave Point in winter: what you're looking at"; day 3 stitch prompt "show us your same-rock cut"; day 4 Fox 11 tip (the newsworthiness gate passes: first ice is a date, not an update) through /press-release signed as the business; day 5 self-parody, the same cut on the shop's mailbox.
- **48 hours:** views divided by followers over 10x on FB or TikTok means it traveled; argument ratio over 5 comments per 1,000 views means the polarity worked; the number that pays is 2027 pre-sale bookings in 48 hours vs. zero baseline. Under 3x on all platforms: don't boost, keep the slot anyway, year two is the asset. Over 10x: boost the hero only to Milwaukee and Chicago 50+ via /meta-ads-insider with David's spend.

### Alternates
- **Locked Out:** the 140-day countdown stamp on one still a week, same cave mouth, ending on opening weekend. Fallback if the freeze comes late or David can't be on the rock.
- **Conveyor Belt:** the mockumentary, held for spring hiring season when guides are back and the tone can be played warm, not mean.

### Routing
- /seedance-video: the one [GEN] shot, "sea cave mouth sealed by a curtain of ice, from water level, Lake Michigan, overcast, no people, photoreal." One draft only, after David approves.
- /ffmpeg-usage: the same-rock cut from `1-great_2026-07-20_waves-crashing-cliff-ledge.mp4` and `1-great_2026-07-06_sea-cave-tandem-kayak.mov` with December phone footage; 9:16 and a 6s GIF.
- /carousel: "What the ice is hiding," eight clip-library frames.
- /social-captions: three platform captions above, plus the guest SMS.
- /press-release: one-line tip to Fox 11 and the Door County Pulse the morning of.
- /growth-plays: log "First Ice" as a new series play, status "built, waiting on freeze."
- Pre-sale: David confirms the 2027 opening date and that FareHarbor can list it now.

### Ebike / Airstream Sauna / CPPP
**Door County Ebike Tours:** rides the hero as the day-2 carousel's last frame ("the roads thaw before the caves do") and as the second product in the pre-sale. No separate asset; "Slow down. See more." is the winter caption, the ebike is how you reach the ice overlook in April without a car.
**Airstream Sauna:** it is the only DCKT product that works on First Ice morning. If it runs in winter, the swarm's day-3 still is the Airstream's window with the frozen lake behind it, "Wood fire. Cold air. Nothing else." If it's paused (David's call per the roster), it stays out of frame.
**Cave Point Paddle & Pedal:** operationally separate from DCKT for SEO and outreach, so it does NOT share the hero or the press tip. Its version is the heritage cut: the same rock, but the caption is "23 winters from this shop." Different sender, different week, never the same editor. CPPP pulse (dckt-region key) was still running when this section was written; check `~/Projects/creative-director/cache/cppp/2026-10-13/pulse.md` before building its cut.

**CPPP pulse (landed after the section above was written, dckt-region key, est $0.68, reddit errored 400):** "clear kayak" on TikTok is a photoshoot product, not a tour: Barbados 538k, Jamaica 443k, Zanzibar 703k, all "book your clear kayak photoshoot" (https://www.tiktok.com/@clearoceanbarbados/video/7563080175743798, https://www.tiktok.com/@coollocs97/video/7610549505867451661). Peaking. The 2.5M clip is a transparent kayak used to hunt sea creatures, catch-and-cook (https://www.tiktok.com/@ybsyounggbloods/video/75726799534147371). Cave Point itself: 387k on "one of my favorite places in Wisconsin" (https://www.tiktok.com/@justhereexploring/video/76436426985906537), and a guest tagged DCKT at 247k (https://www.tiktok.com/@misskurana/video/7401541289642134826). Google Trends: "clear kayak" +41% last 14d, "door county" flat, "cave point kayak" near zero off-season. What to do with it: CPPP's 2027 spring asset is the clear-kayak-as-photoshoot angle over the emerald water, which nobody in the Midwest is selling; hold it for the April pre-season, not now.
