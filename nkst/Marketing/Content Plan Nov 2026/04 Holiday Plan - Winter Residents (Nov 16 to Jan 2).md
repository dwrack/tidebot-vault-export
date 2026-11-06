# NKST Instagram: Winter Residents (Nov 16, 2026 to Jan 2, 2027)

CURRENT STATUS (verified 2026-10-31): Week 3 (Nov 16 to 21) is QUEUED in `Review Reels (Oct 2026)/IG Reels Queue.csv`. Nov 23 to Jan 2 is rendered, uploaded and STAGED (status `staged`, the poster skips it) until David OKs the captions; flip to `queued` after that. Renders: `_render/hooks.py holiday | carousels | qc` (outputs in `_render/out/`). S3: `reels/h-*.mp4` and `carousels/h-*/01.jpg...`. The poster now posts carousels (an s3_key ending in `/`); the live container path was tested 2026-10-31 without publishing.

## Name-the-resident rotation (2026-11-02)
David wants the "Now accepting names for our latest swamp resident" format mixed into wildlife posts for variety. Dec 11 cold gator and Dec 18 barred owl captions in the queue CSV now ask for a name (still `staged`; backup `IG Reels Queue.csv.bak-20261102-names`). Nov 20 anhinga, Dec 4 eagle and Jan 1 egret stay as written so it's every other one, not every one. Day-after Story: poll with the top 2 or 3 names. Caption bank and rules: `NKST Social Media Strategy.md`, Lane 2 Wildlife.

## Render changes (2026-10-31, these override the calendar below)
- Nov 16: the GoPro clip's audio is wind only, so the plan's backup hook runs: "airboat people, look away", music bed.
- Nov 21 carousel: DJI_0135, 0125, 0137, 0122, 0143 (all overhead). Dropped 0112/0113 (near twins, same scene as Dec 28), 0119 (mostly black), 0126 (it is the Nov 7 reel), 0133 (Nov 2 reel).
- Nov 25: second card is "he's stealing whichever loses" (one line; two lines touched his ears).
- Nov 27: rendered from DJI_0130 3 to 13s. "Winter kayaking in the swamps.mov" is a titled copy of DJI_0130.
- Nov 28: text moved to y=1420, on the hull.
- Dec 5 carousel: no close-up people (every photo we own shows summer clothes, which contradicted the tips). Gray Honey Island morning cover, kayak-bow and gray-water slides, guests-in-life-jackets last.
- Dec 11: music instead of the clip's sound (a guide is talking on it). Clip starts at 2.5s so the cover shows the gator; "ok, he heard you" lands at 8.3s when he turns off the log.
- Dec 19: DJI_0131 top-down only. P1030011 shows two guests' faces (the catalog said backs), so it waits for permission.
- Dec 28: DJI_0115 golden-hour kayaks (DJI_0130 is already Nov 27). Cut the unverified "most of the people in our kayaks flew here" line.
- Jan 2 carousel: 2026 guide photos only, since the post says 2026. Cover is the green-kayak POV (IMG_2348); no guest faces. Caption ends "See you out there in 2027." (Jan 2 is a Saturday, "back out there Monday" was wrong).
- Every reel was checked at full 9:16 on its first frame, each text switch and its last frame (`out/qc_reels_1..4.jpg`, `out/qc_h-*.jpg`).
Inputs: 03 plan (four lanes), What Works study, Performance.md, the 100-post IG pull (2026-10-31), 00 Asset Inventory, FAQ Complete, 2027 Tour Schedule Proposal, Gift Card Campaigns, UGC playbook.

## What the data says about holidays on this account
- The only holiday promo we ever ran (Dec 1, 2025, "20% off gift cards") reached 155 people, a third of baseline. Pictured Rocks and Zip NOLA holiday promos died the same way. Promos go in stories, never on the feed.
- Nov to Jan has been dead air every year: 0 posts Nov 2025, 1 in Dec, 0 in Jan. The account loses its momentum right when visitors are in town. This plan fixes the cadence first and the holidays second.
- Reels average 949 reach here, carousels 390, single photos 45. Everything below is a reel except one carousel a week on Saturday, which is there for saves.
- Our winners are identity lines and deadpan, not greetings. "Merry Christmas from all of us" is a story frame, not a post.

## The idea
Winter is the one season where the swamp beats the city. No bugs, no sweat, eagles back, gators slow, hyacinth gone so the channels open up, and 60 degrees while the rest of the country shovels. The holiday angle is "you are in town, or your family is, and you need two hours of quiet." Every post is still one of the four lanes. Holiday is the skin, not the skeleton.

| Lane | Day | Winter skin |
|---|---|---|
| 1. Pick a side | Mon | Same edge as November, lighter in Christmas week (bonfires, resolutions instead of oil) |
| 2. Settle it | Wed | Louisiana holiday arguments: dressing, king cake, bonfires vs Oaks, sweater weather |
| 3. Resident of the week | Fri | The winter cast: anhinga, bald eagle, lazy gator, barred owl, egret |
| 4. Guest and guide | Sat | Carousels for saves (what to wear, from above, year in nine), guide crew, caption this |

No post on Thanksgiving Day or Christmas Day. Stories only. A real account goes quiet on the day and posts the day after.

## Visual system (so the grid reads as one account)
This is the part that makes it look run by a person. Every reel cover and text card uses the same rules from Nov 16 on.
- **Text style (changed 2026-10-31; the poster labels did not land):** one sentence a person would say, sentence case, black Helvetica Neue Medium on a white rounded box per line, the way text looks when it is added in the Instagram app. Renderer: `_render/hooks.py` in this folder. No all caps, no "Resident of the week" eyebrow, no period-ended labels.
- **Every hook earns the stop:** a take, a question, or a joke tied to what is in the photo. Never a label that names what is already on screen ("ANHINGA."). The strongest wildlife shots (the owl, the From above carousel) run with no text at all.
- **Never on the animal or a face:** text goes in the empty part of the frame, the top by default (y 270 to 560), the lower third when the subject fills the top. Checked on the full 9:16 frame for every post. If there is no clean spot, change the crop or the photo; never shrink or cover the animal.
- **Covers:** pick a cover frame for every reel, never let Instagram pick. Cover text sits in the middle so it survives the 3:4 grid crop. If the subject fills the top third (a face, a bird on a branch), the text drops to the lower third (y 1250 to 1450), never over a face.
- **Grid rhythm (3 columns):** never two text-heavy covers side by side, never two aerials side by side, never two gators in a row. Alternate dark water, warm wildlife, people. The grid preview sheet in the scratchpad checks this for the first 12.
- **Captions:** first line is the hook, no emoji as the first character, 3 to 7 hashtags, plain ASCII, business name only, never a guide's name. Wildlife is "common, never guaranteed." We say guests, not customers.
- **Alt text on every post** (one sentence, what is in the frame). **Location tag:** Manchac, Louisiana. **Posting time:** 10:00 CT Mon/Wed/Fri, 6:00pm CT Sat (the What Works test).
- **Reply to every comment inside the hour, pin the best disagreement.** Reply with a question, not "thanks."
- Week 1 (Nov 2 to 7) was re-rendered in the native text style on 2026-10-31 and re-uploaded to the same S3 keys (old versions in `reels/_bak-20261031/`), so the grid starts consistent on Monday.

## Pre-flight (do before Nov 16)
1. Confirm winter start times in FareHarbor. The vault disagrees: 11:30 and 2:00 only (2027 plan) vs 11:30 / 2:00 / 4:30 (Nov outreach). Captions below say "11:30 and 2:00". Fix the captions if 4:30 runs.
2. Confirm 9:00 returns Dec 26 to 31 (2027 plan says yes). The Dec 26 caption depends on it.
3. Open neworleanskayakswamptours.com/gift-certificates/ and confirm it still says no expiry, emailed instantly. That page is the only link in the gift stories.
4. "Same price as July" (Nov 27 post): confirm the $65 flagship price did not change this year.
5. Rights: the 2018 drone set is ours. The Slack photos (96 files, Aug to Oct) need the guide who shot them to say yes before any guest face runs. Carousel on Nov 21 uses only the 2018 drone stills, so it is clean.
6. Frogs at Night.caf: confirm it is our own recording before it goes under the Nov 16 reel. If unsure, use paddle sound only.
7. Verify "most of the people in our kayaks flew here" (Dec 28) against FareHarbor zip codes, or cut the line.

## Post calendar
Format: reel unless marked. On-screen = cover text. Each caption is complete and ready to paste. Hashtags: `#neworleans #nola #swamptour #kayaking #louisiana #manchac` plus one topical tag where noted. Sources for Lane 1 numbers are in `01 Hot Topics Research`; the cited line goes in the caption because the poster cannot leave a first comment.

### Week 3: Nov 16 to 21. "The swamp in a fleece"

**Mon Nov 16, L1 airboats.** Asset: `Raw Footage/winter swamp kayaking/C0015.mp4` (8s GoPro paddle, silent), paddle drips only for 5s, then frog audio if cleared (pre-flight 6). On-screen (top): "what a swamp sounds like / without an airboat". Needs real sound under it (paddle drips, then frog audio once cleared). If the audio comes out thin, use "airboat people, look away" instead.
Caption: You cannot hear a swamp from an airboat. You can only hear the airboat. Airboats are faster, they reach the flats, and they are the right call for people who cannot paddle. We run silent kayaks, which is why the heron does not leave when we show up. Airboat people, make your case. #neworleans #nola #swamptour #kayaking #louisiana #manchac #airboat
Alt: A kayak bow moving through still black water under cypress, text about airboat noise.

**Wed Nov 18, L2 Tangipahoa.** Asset: `Carousel Picks/manchac-swamp-aerial-kayaks-canopy.jpg`, 5s slow zoom. On-screen (top): "tell me you're from / Tangipahoa without telling me"
Caption: Tell me you are from Tangipahoa without telling me you are from Tangipahoa. St. John and St. Charles, you can play too. Go. #neworleans #nola #swamptour #louisiana #manchac #tangipahoa
Alt: Aerial of kayaks under the cypress canopy, Manchac swamp.

**Fri Nov 20, L3 anhinga.** Asset: `Slack Pull Oct 2026/originals/2026-10-19-anhinga-drying-wings-cypress-P1030370.jpg` (guide Lumix shot, wings spread on a branch, the only real anhinga in the library), 6s slow push. On-screen (top, above the bird): "this bird has to air dry / after every single swim"
Caption: Anhinga. Its feathers soak through on purpose so it can swim underwater, which means after every dive it has to stand like this until it dries out. Same energy as getting out of the shower in a cold house. Common, never guaranteed. #neworleans #nola #swamptour #kayaking #louisiana #manchac #birding
Alt: An anhinga perched on a branch with its wings spread wide to dry, moss-covered trees behind.
(Bench: green heron `Slack Pull June 2026/originals/P1020216.jpg` and two sharper green herons in `Slack Pull Oct 2026/originals/` if this slot needs a swap.)

**Sat Nov 21, L4 carousel "From above."** Assets (5 slides, 4:5): DJI_0112, DJI_0113, DJI_0119, DJI_0126, and a frame grab from DJI_0133 at 12s. No cover text. The photo carries it.
Caption: Late fall from 300 feet. These are from a November drone shoot a few years back, same channel we paddle this week. Save this for the next person who says there is nothing to do outside the Quarter. Which one goes on the wall? #neworleans #nola #swamptour #kayaking #louisiana #manchac #drone
Alt: Five aerial photos of red kayaks in a cypress swamp at golden hour.

### Week 4: Nov 23 to 28. Thanksgiving

**Mon Nov 23, L1 second-growth trees.** Asset: `Carousel Picks/manchac-sun-rays-through-cypress.jpg`, 8s slow push (the bare cypress belongs to Dec 23; using it twice would repeat a photo). On-screen (top): "almost every tree out here / is a replacement", then at 4s "the last original was cut in 1957"
Caption: Nearly every tree you paddle past is a replacement. The originals were cut for lumber starting in the 1830s and the last virgin cypress came out of the Manchac in 1957. What grew back is what we have, and it is still the best thing within an hour of the city. Thankful for second chances, trees included. Does your family have a cypress story, a camp, a pirogue, a swing? Source: Fox 8, Turtle Cove research station. #neworleans #nola #swamptour #louisiana #manchac #cypress
Alt: Sun rays through moss-draped cypress.

**Wed Nov 25, L2 dressing.** Asset: `Slack Pull Oct 2026/originals/2026-10-07-raccoon-in-tree-P1030135.jpg` (raccoon peering through branches), 6s slow push. On-screen (top, one line above his ears): "oyster or cornbread dressing?", then at 3s same spot "he's stealing whichever one loses"
Caption: Oyster dressing or cornbread dressing. Settle it before Thursday. Whichever one loses, he is taking it off the counter. #neworleans #nola #swamptour #louisiana #manchac #thanksgiving
Alt: A raccoon peering out from tree branches.

**Thu Nov 26.** No post. Story only (see Stories).

**Fri Nov 27, no Black Friday sale.** Asset: `Assets/Videos/Winter kayaking in the swamps.mov`, best 10s, 9:16 crop. On-screen (top): "we're not having a / Black Friday sale", then at 4s "same price as July. / way fewer mosquitoes."
Caption: We are not having a Black Friday sale. The swamp costs the same as it did in July. It is a lot cooler, the mosquitoes left, and the eagles are back. If you want the gift version, it is in our story today. #neworleans #nola #swamptour #kayaking #louisiana #manchac
Alt: Kayakers paddling a winter cypress swamp, gray light, text about no sale.

**Sat Nov 28, Small Business Saturday, the crew.** Asset: `Carousel Picks/manchac-guide-in-kayak-cypress.jpg` (guide in purple shirt, viewed; the "guides selfie" files are one guide with his face half out of frame), 6s, framed so his face is in the top third and the text sits in the lower third. On-screen (lower third, on the kayak, clear of his face and hands): "this is our entire office"
Caption: Small Business Saturday. This is our entire office: a kayak, a paddle and two hours of swamp. No building, no bus, no gift shop. Thanks for keeping it that way. #neworleans #nola #swamptour #kayaking #louisiana #manchac #smallbusinesssaturday
Alt: A guide in a sun hat sitting in an orange kayak, talking, cypress and marsh grass behind.

### Week 5: Nov 30 to Dec 5. Winter residents move in

**Mon Nov 30, L1 marshmallows.** Asset: `Slack Pull Oct 2026/originals/2026-09-06-alligator-eyes-in-hyacinth-P1020845.jpg` (wild gator, eyes and snout above the water in hyacinth, keeping its distance), 7s slow push. On-screen (top; the gator sits low in frame): "if a gator swims up to you, / somebody's been feeding it"
Caption: If a gator swims up to your boat looking for a marshmallow, a tour taught it to do that. We do not feed them, which is why ours keep their distance and their manners. Wild, never baited. Would you rather see a gator at 3 feet that was trained, or a wild one at 40? Source: LDWF warning, July 2019. #neworleans #nola #swamptour #kayaking #louisiana #manchac #alligator
Alt: An alligator's eyes and snout just above dark water among hyacinth leaves.

**Wed Dec 2, L2 sweater weather.** Asset: `Carousel Picks/manchac-gray-sky-moody-reflection.jpg`, 5s. On-screen (top): "Louisiana sweater weather / starts at what temp?"
Caption: Sweater weather starts at what temperature? Louisiana edition. Wrong answers accepted, 68 is not wrong. #neworleans #nola #swamptour #louisiana #manchac
Alt: Gray winter sky over cypress reflected in still water.

**Fri Dec 4, L3 bald eagle.** Asset: `2025 Wildlife & Guests/1000019017.jpg` (eagle lifting off with a fish, VIEWED) 4s, cut to `1000019019.jpg` 4s. The 20s "Bald eagle" drone video is a find-the-dot clip with no visible bird; do not use it. On-screen (top, above the eagle): "the eagles are back"
Caption: Bald eagle. They move into the Manchac for the winter and December through February is when we see them most. Not every tour, never guaranteed, but the guides know which trees to check. Bring a long lens if you own one. #neworleans #nola #swamptour #kayaking #louisiana #manchac #baldeagle
Alt: A bald eagle lifting off the hyacinth bank with a fish in its talons.

**Sat Dec 5, L4 carousel "What to wear in December."** 6 slides, 4:5, text top (same native style, never over a person): 1 `Carousel Picks/manchac-kayaks-staged-at-launch.jpg` "what to actually wear / on a December paddle" (the gear-up photo shows a guest in shorts, wrong for December) / 2 `Slack Pull Oct 2026/originals/2026-09-06-guests-cypress-channel-01-P1020849.jpg` (backs only) "wool or fleece. no cotton, no jeans." / 3 `Carousel Picks/manchac-guide-paddling-cypress-grass.jpg` "a shell that stops the wind" / 4 `2018 Fall Drone Shoot/aerial-photos/DJI_0119.JPG` "closed-toe shoes that can get wet" / 5 `Slack Pull Oct 2026/originals/2026-09-06-guests-cypress-channel-02-P1020857.jpg` (backs only) "gloves. the paddle gets cold first." / 6 `Honey Island Swamp Kayak Tour/Assets/Carousel Picks/honey-island-gray-morning-kayakers-river.jpg` "life jacket's on us. the water runs 40s to 60s."
Caption: What to wear on a December paddle, from the guides. Wool or fleece, no cotton and no jeans. A shell that stops wind. Closed-toe shoes that can get wet. Gloves, because the paddle gets cold before you do. Water runs 40s to 60s this time of year and you will not be in it, but the air off it is real. Save this for the morning of. #neworleans #nola #swamptour #kayaking #louisiana #manchac #whattowear
Alt: Six slides of winter swamp photos with clothing tips.

### Week 6: Dec 7 to 12. Storm memory and visitors

**Mon Dec 7, L1 storm clock.** Asset: `Honey Island Swamp Kayak Tour/Assets/Carousel Picks/honey-island-aerial-flooded-cypress-kayaks.jpg` (water-level aerial), 6s. On-screen (top): "which storm does your family / measure time by?"
Caption: Every family out here measures time by a storm. Before Katrina. After Ike. That one in 2021. Ike pushed about ten feet of surge through Pass Manchac and you can still read the line on some of the trees. Which storm is your family's clock? Source: local reporting on the Pass Manchac rebuild. #neworleans #nola #swamptour #louisiana #manchac #hurricane
Alt: Aerial of kayaks over flooded cypress.

**Wed Dec 9, L2 bonfires or Oaks.** Asset: `Carousel Picks/manchac-sunset-golden-hour-open-water.jpg`, 5s. On-screen (top): "levee bonfires or Celebration / in the Oaks? you only get one"
Caption: Christmas Eve bonfires on the River Road levee, or Celebration in the Oaks. You can only keep one. The bonfires are about 25 minutes from our launch, for what it is worth. #neworleans #nola #swamptour #louisiana #manchac #christmasinneworleans
Alt: Golden-hour sunset over open swamp water.

**Fri Dec 11, L3 lazy gator.** Asset: `Slack Pull Oct 2026/videos/2026-10-16-cypress-channel-vertical-02-IMG_8825.mov` (guide phone video, 13s vertical 720p: gator basking on a log under moss, then slides in), use 0 to 11s with its own sound. On-screen (top, gator mid-frame): "he's not dead, / he's just cold", then when he slides in "ok, he heard you"
Caption: He is not dead. Below about 65 degrees a gator slows down, stops eating, and spends the afternoon on a log like this one, until somebody paddles too close. In December you see them on sunny afternoons and almost never on gray ones. Common, never guaranteed. The 2:00 tour is the gator tour this month. #neworleans #nola #swamptour #kayaking #louisiana #manchac #alligator
Alt: An alligator basking on a log under Spanish moss, then sliding into the water.

**Sat Dec 12, L4 caption this.** Asset: `Slack Pull Oct 2026/originals/2026-10-07-red-shouldered-hawk-perched-P1030103.jpg` (red-shouldered hawk on a branch, side-eye), 6s. The egret was too tall: any text at the top crossed its neck. On-screen (top, above the hawk's head): "what's he thinking?"
Caption: Caption this. Best one gets pinned. #neworleans #nola #swamptour #louisiana #manchac #hawk
Alt: A red-shouldered hawk perched on a lichen-covered branch, looking sideways.

### Week 7: Dec 14 to 19. In town for the holidays

**Mon Dec 14, L1 ghost forest.** Asset: `Crescent City Kayak/Assets/Carousel Picks/manchac-dead-cypress-snag-moody.jpg` (same swamp, sister folder), 7s. On-screen (top): "our best tour stop / is a dead tree"
Caption: Our best tour stop is a dead tree. Salt water got into this part of the Maurepas, the cypress died standing, and the ghost forest is the most photographed stretch of the route. Ugly truth sells. The river reintroduction project upstream is the first real shot at fresh water coming back. Would you rather we paddled around it? #neworleans #nola #swamptour #louisiana #manchac #ghostforest
Alt: A dead cypress snag standing in dark water under a gray sky.

**Wed Dec 16, L2 locals vs tourists.** Asset: `Carousel Picks/manchac-guided-group-cypress-swamp.jpg`, 5s. On-screen (top): "locals, when's the last time / you came out here?"
Caption: Is a swamp tour a tourist thing or a local thing? Locals, be honest about the last time you came out here. Visitors, say where you flew in from. #neworleans #nola #swamptour #louisiana #manchac
Alt: A guided group of kayakers paddling through cypress.

**Fri Dec 18, L3 barred owl.** Asset: `Slack Pull Oct 2026/originals/2026-09-30-barred-owl-close-01-P1030040.jpg` (face-on, sharp, best owl in the library), 6s. No text. The owl staring at you is the hook.
Caption: Barred owl. The call sounds like "who cooks for you," and you hear them on the late tour far more than you see them. This one sat still long enough for a photo, which almost never happens. #neworleans #nola #swamptour #louisiana #manchac #owl
Alt: A barred owl looking straight at the camera through branches.

**Sat Dec 19, L4 two hours away from your family.** Asset: `Slack Pull Oct 2026/originals/2026-09-30-red-kayaks-sun-rays-cypress-P1030011.jpg` 3s, cut to DJI_0131 top-down follow 6s. On-screen (top): "two hours where nobody / asks when you're moving home"
Caption: In town for the holidays and need two hours where nobody asks about your job, your plans, or when you are moving back? We run 11:30 and 2:00 through the holidays, 35 minutes from the Quarter. The swamp does not ask questions. Link in bio. #neworleans #nola #swamptour #kayaking #louisiana #manchac #holidaysinneworleans
Alt: Two guests in a red kayak among cypress, then a single red kayak seen from above.

### Week 8: Dec 21 to 26. Christmas

**Mon Dec 21, L1 bonfires (light).** Asset: `Carousel Picks/manchac-sunset-cypress-silhouette.jpg`, 7s. On-screen (top): "in 3 days the levee will be / on fire. on purpose."
Caption: Christmas Eve at 7, the levee from Gramercy to Lutcher lights up. The story is the fires guide Papa Noel down the river. It is about 25 minutes from our launch, so a 2:00 paddle and a 7:00 bonfire is a real plan. Which parish's fires are the best, and do not say yours just because it is yours. #neworleans #nola #swamptour #louisiana #manchac #bonfires
Alt: Cypress silhouettes against a pink and orange sunset, reflected in the water.

**Wed Dec 23, L2 real tree.** Asset: `Carousel Picks/manchac-winter-bare-cypress-still-water.jpg`, 5s. On-screen (top; the turtle sits low): "real tree or fake tree?", then at 3s "this one's real. it drops / its needles every winter."
Caption: Real tree or fake tree. Ours is a bald cypress, a conifer that drops its needles every winter, which is how it got the name. Bare, gray, and still the best tree in the state. #neworleans #nola #swamptour #louisiana #manchac #cypress
Alt: Bare winter cypress standing in still water, turtle on a log.

**Fri Dec 25.** No post. Story only.

**Sat Dec 26, the day after.** Asset: `Great new orleans kayak swamp tour photos/IMG_0444.jpg` (green bow, overcast), 6s. On-screen (top): "day after Christmas. / nobody talks for ten minutes."
Caption: The day after. Cold air, quiet water, nobody talking for the first ten minutes. Morning tours are back this week through New Year's Eve. #neworleans #nola #swamptour #kayaking #louisiana #manchac
Alt: The green bow of a kayak on still water in an overcast cypress swamp.

### Week 9: Dec 28 to Jan 2. New Year

**Mon Dec 28, L1 resolution.** Asset: DJI_0130 golden-hour aerial rise, 8s. On-screen (top): "locals, this is 35 minutes / from your couch"
Caption: A resolution for locals: paddle the swamp 35 minutes from your house before somebody from Ohio does. Most of the people in our kayaks flew here. That is backwards. #neworleans #nola #swamptour #kayaking #louisiana #manchac
Alt: Aerial rising over cypress at golden hour with kayaks below.
(Pre-flight 7: confirm the "flew here" line or cut it.)

**Wed Dec 30, L2 king cake.** Asset: `2025 Wildlife & Guests/1000017218.jpg` (gator head), 5s. On-screen (top, one notch higher so it clears the snout): "king cake before Jan 6: / crime or fine?"
Caption: King cake before Twelfth Night. Crime, or fine? January 6 is a week out. The gator has opinions but he is asleep. #neworleans #nola #swamptour #louisiana #manchac #kingcake
Alt: An alligator's head at the surface of dark water.

**Fri Jan 1, L3 egret.** Asset: `2025 Wildlife & Guests/1000017830.jpg` (great egret wading, framed so the whole bird is in shot), 6s. On-screen (lower third, on the water below the bird): "2027 goal: stand still more"
Caption: Great egret. Standing in cold water on purpose. New year, same bird, same swamp, first tour at 11:30. #neworleans #nola #swamptour #louisiana #manchac #egret
Alt: A great egret wading in still green water, its reflection below.

**Sat Jan 2, L4 carousel "2026 in nine."** Nine best stills of the year in 4:5 (the eagle with the fish, the owl, the cabin gator, red kayaks in the mossy channel, the five from above, sun rays, golden-hour group, guides selfie, sunset silhouette). Slide 1 cover (DJI_0113, golden red kayaks): "2026, out here"
Caption: 2026 in nine frames. Thanks for every paddle, every wrong gator guess, and every dressing argument. Back out there Monday. #neworleans #nola #swamptour #kayaking #louisiana #manchac
Alt: Nine photos from a year of swamp tours: eagle, owl, alligators, kayaks, sunsets.

## Stories (3 to 5 frames, posted by hand from the account; the poster cannot do these)
Rule from the stories skill: a face or a hand in frame 1, one idea per frame, the ask at frame 4, nothing above y=250 or below y=1600. Sell gift cards here, never on the feed. Each sequence needs one guide clip from that day's tour (10 seconds, phone, vertical) dropped in #new-orleans-kayak-swamp-tours. That is the only new footage these need.

**Every tour day (default, 3 frames):** 1 guide hand on the paddle at the launch, "Water is 61 today." 2 one clip from the tour, no text. 3 poll: "Would you paddle in a fleece?" Yes / Talk me into it. Reply to every "talk me into it."

**Mon Nov 30, Cyber Monday, gift (5 frames):** 1 guide at the launch holding a paddle, "The one gift that is not a thing." 2 the eagle clip, 3s. 3 text on the bare-cypress still: "Gift certificate. Emailed in a minute. Never expires." 4 link sticker to the gift page, "Tap to send one." 5 quiz: "Gators in December are: asleep / dead / at 58 degrees and thinking about it." Answer frame tomorrow.
Repeat the gift sequence Mon Dec 7, Mon Dec 14, Mon Dec 21 (frame 1 changes: "Ten days left to ship a box. This takes a minute."), and Wed Dec 23 ("Last-minute. Emailed instantly."). Five gift stories, zero gift posts.

**Thu Nov 26, Thanksgiving (3 frames):** 1 guide hand holding a cup at the launch, "Thankful mosquito season ended on Halloween." 2 the 2018 golden-hour drone still, no text. 3 question box: "What do you tell visiting family to do in New Orleans besides eat?" Answers feed the Dec 16 post replies.

**Fri Dec 4, eagle day (4 frames):** 1 guide face, "Eagle week. Here is where we look." 2 eagle clip. 3 quiz: "Bald eagles in the Manchac are here: all year / Dec to Feb / never." 4 "Answer: December to February. Friday's post has the rest."

**Fri Dec 25, Christmas (2 frames):** 1 the sunset silhouette still, "Merry Christmas from the swamp. Back tomorrow at 9." 2 nothing else. One frame is enough.

**Thu Dec 31, New Year's Eve (4 frames):** 1 guide at the launch, "Last paddle of 2026 goes out at 2:00." 2 clip from the morning tour. 3 question box: "One thing you want to see out here in 2027." 4 countdown sticker to the first 2027 tour (Jan 1, 11:30).

**After every question box:** reply to each answer by hand. Good answers become captions in January.

## QC checklist (run on every post before it is queued)
- Date and weekday match (python calendar check, not memory).
- Every number traces to a line in `01 Hot Topics Research` or the FAQ; UNVERIFIED items never go in a caption.
- No em dash, no curly quotes, no emoji first character, no "customers," no guide named, no competitor named.
- Spell-check the caption. Read it aloud once. If it sounds like a brand, cut a sentence.
- Hashtags 3 to 7, topical tag last.
- Text never touches an animal or a face. Check the full 9:16 frame (`python3 _render/hooks.py check1` and `check2`), not just the grid crop. Nothing above y=250 or below y=1600.
- Faces: 2018 drone set and guide selfies are ours; anything from Slack needs the shooter's yes; guest faces need the permission rule.
- Music: from `Review Reels (Oct 2026)/music/` with LICENSES.md, or original sound. No trending audio from the library on a Lane 1 post (it dates the post).
- Grid check: open the last 9 covers side by side before queueing. No two text-heavy, no two aerials, no two gators adjacent.
- Alt text and location tag filled in the queue row.
- Lane tag in the theme column so Performance.md grades it.

## What this needs from people
- One guide 10-second phone clip per tour day for stories (the shoot list already asks for seven clips; these are in addition and lower effort: water temp at the launch, paddles in the rack, a wake).
- Someone to post stories from the account on the phone (the poster script cannot). David or the guide on shift, 2 minutes a day.
- Comment replies inside the hour on Lane 1 days (Mon). This is the one thing an SMM does that a script cannot.

## New guide footage on the bench (Slack pull 2026-10-31)
39 files in `Assets/Slack Pull Oct 2026/` (catalog inside). Not yet placed: two water snake close-ups (Sep 14 and Oct 21; say "water snake" only, no species), red-shouldered hawk, raccoon in a tree, juvenile night heron (Week 2 name-this-bird), great blue heron wading, three caterpillar macros, red kayaks in sun rays, and guest groups that need permission. The snake reel is our biggest proven subject (10,027 plays), so the first snake goes in January when the plan extends; snakes are not out much in December and the caption would mislead. `videos/2026-08-28-cypress-channel-pov-IMG_4107.mov` shows an orange object hanging on a cypress: possibly trash or flagging tape, ask the guide before using it for the trash take.

## Open items
- Gift card denominations are not built in FareHarbor; stories link to the dollar-value page as is.
- Mascots (Beaux Bleu, Grandpa Earl, Cookie) are still DRAFT and unnamed by David. This plan does not use them. If the cast is approved, Cookie takes the Dec 18 owl slot and Earl takes Dec 11.
- Week 2 (Nov 9 to 14) still needs its four reels rendered: beads, Pontchartrain estuary, name-this-bird eagle, comment-reply.
