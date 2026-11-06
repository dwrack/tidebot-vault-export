# Community Creator Engine: Plan (Nov 2026)

*Written 2026-10-31 by David's Claude. Offers updated 2026-11-05 (1 seat for a post, 10% commission). Pilot data pulled live 2026-10-31 via Apify (account inspirational_space, about $2.50). Nothing has been sent, posted or scheduled. Tracker: `Creator Tracker.csv` in this folder.*

Builds on two April playbooks that never got run: `Marketing/Creator Outreach Playbook.md` and `Marketing/UGC Outreach & Repost Playbook.md`. Commission rates come from `Marketing/Competitor Sales Channels + Commission Research (Oct 31 2026).md`.

## The short version

1. **Reposting past guests' posts is the best return here, and it's nearly free.** 21 public posts tagged us since March. Several are from real creators (30k, 33k, 11k, 10k, 9.8k followers). None look reposted. Ask permission, repost, re-invite.
2. **Generic hashtags are a weak source of people to invite.** In 45 days, the 8 hashtags returned 149 posts from 77 accounts. About 60% were venues and businesses. Most of the tourists had already gone home, so an invite is too late. Where the hashtags do pay off is finding **local curators and group-trip planners**. Those accounts send us a steady flow of future visitors.
3. **Your history check works.** I pulled the last 40 posts from each of 20 hashtag creators and searched them for us, our boats, tiki, party boat and swamp tour. **None had ever posted about us**, so all 20 count as new. That check runs before anyone gets a message.
4. **Commission goes to planners, not influencers.** Travel advisors and bachelorette planners book groups over and over. Pay them 10% on a FareHarbor affiliate link. Creators get an exchange (1 comp seat) plus their own code, so we can see which of them actually sell.
5. **The bigger problem is that guests barely tag us.** We carry thousands of guests a year and only 21 public tags were visible. A sign on every boat would do more than any scraper.

## Update 2026-10-31 (late): full tagged list + IG DMs

**Tagged tab (read from the logged-in Chrome, nothing clicked):** 264 posts from 183 accounts tag @nolapartybarge, going back to 2023. 41 accounts tagged us 2+ times. The 21 above was only what a logged-out scraper can see.

| Who | Why it matters |
|:-|:-|
| @buoyantbrunchoasis | Jun 2025 reel: **504k plays, 26.5k likes**. Our biggest piece of content and we don't own it. First partnership-ad ask |
| @annayachelcy, 108k | Tagged us twice (Jul 2024) |
| @alexx_robinson, 56k NOLA reel creator | Tagged us **6 times**. Already an ambassador in practice. Make it official (code + comp seat) |
| @bucketlistnola, 17k "best things to do in NOLA" | Tagged us 4 times. Exactly the generic-keyword audience |
| @thecurlycreole | Posts of us with 3.7k and 1.8k likes |
| @boattoursatthewharf (boat tour agency) | Tagged us **10 times**. Looks like a reseller. Find out if they sell our seats and on what terms. This is the commission lane already happening |

**IG DMs (OpenCX, 147 threads since 2026-05-01):** 10 creator/collab requests and 3 planners **came to us first**, among them Tatiana Cardenas (33k, in town Aug 21-23), Tea / Check It Out With Tea, Destiny (NOLA lifestyle), the NOLA Travel page offering a feature, The Travel Esquire (nonprofit group charters), and Special Event Travel Network. Several were handed to a human, and the 2026-10-31 OpenCX study found 0 human replies to handoffs since Aug 28. **The cheapest creator pipeline is the one in our own inbox.** Answer these before sending a single cold DM.

OpenCX doesn't store IG handles (display names only), so DM people are matched by name in the tracker, rows marked `(DM)`.

**Limits hit (history, see CURRENT STATUS below):** the stored Meta Graph token expired 2026-06-29 (blocks API access to tags and DMs; David needs to refresh it). The NPB Apify account hit its monthly hard cap on 2026-10-31, so follower counts are missing for about 160 of the 183 taggers. Re-run when it resets. The monitor needs a higher Apify cap (about $5-10/mo) or the refreshed Meta token, which is free.

## CURRENT STATUS 2026-11-05: names, FareHarbor and full IG inbox checked

**Meta is fine (verified 2026-11-05).** The shared system-user tokens (META_IG_TOKEN, FB_ACCESS_TOKEN) are valid and never expire on both Macs. They reach all 5 IG accounts and include message access. The "expired 6/29" note above was wrong: only the 5 old per-account IG tokens (IG_TOKEN_*) died, and the Instagram tool already falls back to the system token. No action needed.

**Real names:** pulled from Instagram for 195 of 201 handles (column `real_name`).

**FareHarbor (38,850 bookings, 2018 to now):** 20 creators have booked with us (column `fh_history`). 7 were already comped, so they're past collabs, not new invites:
- Alex Robinson (@alexx_robinson): comped 3x (2022, 2022, 2024)
- Tasha Buras (@thecurlycreole): comped 3x (2024-25)
- @nightsonbourbon: comped 2x (Apr 2025)
- The Nola Collective (Bianca Cook): comped May 2025. Earlier I listed them as never posting us. Wrong
- TTD NOLA / @thingstodonola (Natasha Coleman): comped Aug 2025
- Krystal Jade (@jaderbomb), David Punch (@dpunchphoto): comped 2025
- Paid: Annaya Chelcy (Jul 2024), Kayla Weiss (12 guests, Oct 2025), Vass Kazee ($1,250 private, Jun 2025), Niya Frazier, Athena Blackwood, DJ Lickerish, Shazia Carithers, Nyree Gaines. A few common-name matches are marked "maybe".

**Full IG inbox via Graph (1,710 threads since 2019):** 77 of the 201 handles have DM'd us (column `ig_dm_last`). The pattern: when a creator tags us in a story, the bot answers with a sales pitch ("$63/person...") and no person follows up. Open threads to answer first:
- @bucketlistnola, Feb 10 2026: agreed to collab ("still happy to collab, will be in touch"). Never followed up
- @pennyonthelane: tagged us again Oct 21 2026, no reply
- @girlabouttown.nola, Jun 23 2026: asked for a referral discount for her bach clients, gave her email. Bot said a tour expert would reach out. Nobody did
- @thetravelesquire_, May 10 2026: 22-person charter for Jul 18, left a phone number. No human follow-up found
- @kayla.denise.rn, Jan 2026: "I was the one who took that picture." Got the sales pitch back
- @theswampleprechaun, @alexthatmediagurl, @dovetailnola (asked for a LIVE AGENT Sep 13), @uneaktershai: recent story tags or asks

**Offers (David, 2026-11-05):** 1 free seat for a post. 10% commission for planners.

## What the pilot found (2026-10-31)

| Bucket | Count | Best ones |
|:-|:-|:-|
| Past guests who tagged us (Mar to Oct 2026) | 21 posts, 18 accounts | @pennyonthelane 33.7k (ran a Latinas meetup on our boat), @blacktravelexperience 30.5k, @queentyler 11.5k, @bosslady_misa 10.2k, @jillianlovesfilm 9.8k (filmmaker, Oct 25 bach reel), @rustylazer 9k local (314 likes, our best post) |
| Group-trip planners | 4 | @thetravelesquire_ (already brought 30 ladies in July, Freaky Tiki), @bachtobasic 66.9k bach planner |
| Local curators / creators, never posted us | 8 worth inviting | @thenolacollective 66.6k, @eatingthrunola 10.2k, @allinthenola 5.3k, @locallynola, @onehungryrugger, @newfavspot |
| Bach vendor (referral partner, not a creator) | 1 | @girlabouttown.nola (bach decor/setup) |
| Tourists who already left | 5 | Skip. Too late to invite |

Small fix: @lex_da_flex tagged **@nolapartybarges** (wrong handle). Ask them to fix it when we reach out.

## Is reposting old posts worth it? Yes, with three rules

- **Ask first, every time.** A DM asking permission is also the re-invite. If they say yes, use an IG Collab post or a Story share with a tag. Never download and repost without asking.
- **Ask for ad rights in the same message.** If they say yes, run the post as a Meta **partnership ad** from their handle. Partnership ads usually beat brand-handle ads. This is where the money is.
- **Repost to Stories first, feed second.** Stories cost us nothing in grid quality. Only the best 1 or 2 a month go to the feed. Old posts still get a bump when we comment and share them.

## The system: four lanes

### Lane 1: Past guests (repost + re-invite)
- Source: weekly pull of posts that tag or mention @nolapartybarge (Apify `mentions`).
- Action: a comment on their post the same day, then a DM asking to repost (and for ad rights), plus a "come back" offer.
- Offer for a return trip: **bring 2 new friends and your own seat is free** on a public cruise. A return guest who brings 2 paying friends costs us nothing.

### Lane 2: Local creators (exchange)
- Source: weekly pull of generic NOLA hashtags. Keep only people/creators based in New Orleans with 2k-100k followers and real comments. Run the history check against the tracker and their last 40 posts.
- Offer: **1 comp seat on a public cruise** (an empty seat costs us about $0). In return we ask for one Reel or 3 Stories with a Collab tag, and rights to reuse their clips in ads. Nothing scripted.
- Cap: **2 creators per weekend, 8 a month.** That keeps one creator on a boat almost every weekend without swamping paying guests.
- Each creator gets a personal FareHarbor code (e.g. RUSTY10, 10% off for their followers). That tells us who sells and who only posts.

### Lane 3: Planners and advisors (commission)
- Who: bachelorette planners, group-trip planners, travel advisors (Fora, luxury travel), and local hotel concierges later.
- Offer: **10% commission** on every booking through their FareHarbor affiliate link, plus one comp seat so they've seen the product. FareHarbor already has a "Payable to Affiliate" column in our booking export, so the plumbing exists.
- This is the lane that answers your question about the commission opportunity. Planners book again every season. Influencers mostly don't.

### Lane 4: Pre-trip intercept (later, after lanes 1-3 work)
- Watch for "NOLA next week", "bach in New Orleans in March" and "girls trip NOLA" posts from people who haven't arrived yet. They're the one tourist group we can still convert.
- Reply with a public comment ("if you want a swamp party boat on the trip, we've got you"), then a DM only if they engage. No cold DMs to strangers in bulk.

## The monitor

**Recommended:** one weekly job on davids-mbp-2, Monday 7am CT, about $1-2/week on the NPB Apify account. **Not built yet.** Run `/design-review` before building it.

What it does each Monday:
1. Pulls new mentions of @nolapartybarge, adds them to the tracker as `past_guest` and marks them for repost.
2. Pulls the 8 generic hashtags plus TikTok search ("things to do in new orleans", "nola bachelorette"). Keeps only real people based in New Orleans, scores them (followers, engagement rate, how well they fit) and runs the history check.
3. Removes anyone already in the tracker so nobody gets a second message.
4. Writes `Creator Weekly — <date>.md` here with the top 5 new invites, the repost queue, and who's on a boat this week.
5. Posts one line to #helm-npb ("5 new creators, 3 reposts ready, link"). No Slack thread spam, given the Oct 13 Slack fatigue pause.

**What it never does:** send DMs. Instagram doesn't allow automated DMs to people who haven't messaged us first, and the account risk isn't worth it. Jeff sends by hand from the @nolapartybarge app, about 15 minutes a day.

## Two things to fix before the first DM goes out

1. **OpenCX will answer creator replies.** Nolan handles inbound IG DMs, so a creator who replies "yes I'd love to come out!" would get a sales pitch. Fix: add an OpenCX instruction that hands off any IG thread that starts with our outreach, or tag those threads `creator` and route them to Jeff. Without this, the outreach looks like a bot.
2. **The seat price changes Nov 2** ($59 to $65). Comp seats are worth $65 each. Book creators on cruises that are under 60% full so they never take a seat someone would pay for.

## On-boat tagging (the biggest lever)

- A small sign at each boat's bar/cooler area: "Tag @nolapartybarge in your post. We repost our favorites and pick one group a month for a free cruise."
- Captains say it once at the end of the ride: "If you post today, tag us, we share the best ones."
- Goal: 21 tags in 8 months becomes 20+ a month. Every one of those feeds Lane 1.

## Weekly rhythm (Jeff, about 90 minutes a week)

| Day | Task | Time |
|:-|:-|:-|
| Mon | Read the weekly file. Comment on new tags. Send 5 repost/re-invite DMs | 30 min |
| Tue-Thu | Send 3 creator invites + 1 planner pitch a day, update tracker | 15 min/day |
| Fri | Confirm the weekend's creators, tell the captain who's coming | 10 min |
| Sun | Collect the creator posts, share to Stories, log views in tracker | 15 min |

## How we know it's working (check monthly)

- Reposts approved per month (target 10+)
- Creators on boats per month (target 6-8), and how many delivered a post (target 80%+)
- Bookings on creator codes and planner affiliate links (the number that matters)
- Partnership ads running and their cost per purchase vs our brand ads ($50.22 avg, Oct 12-25)
- Public tags per month (baseline: about 2-3/month, Mar to Oct 2026)

## Next steps

- [x] David: offers set 2026-11-05: 1 free seat for a post (creators), 10% commission (planners). Past-guest bring-2-ride-free still stands
- [ ] David: confirm Jeff owns sending, or name someone else
- [ ] Claude: OpenCX creator-handoff rule (needs David's OK, touches the live bot)
- [ ] Claude: FareHarbor affiliate setup for planners + creator codes (Settings > Affiliates / Campaigns)
- [ ] Claude: `/design-review`, then build the Monday monitor on mbp-2
- [ ] Jeff: on-boat tag sign, print and post on all boats
- [ ] Jeff: send the first 10 DMs from the tracker (drafts below)

## DM drafts (for Jeff, from @nolapartybarge)

**A. Past guest, repost + re-invite**
> Hey! We just found your post from the boat and it made our week. Mind if we share it on our page? We'd tag you of course. And if you're cool with us using it in an ad too, even better. Also, if you're ever back in town, come out again on us: bring 2 friends and your seat is free.

**B. Local creator, exchange**
> Hey [name], love what you're doing with [specific post]. We run the swamp party boats out in the bayou (live gators, music, BYOB, way off the Bourbon St path). Want a free seat on us one weekend this month? All we ask is one post (a Reel or a few Stories) tagging us. No script. We'll share it and set you up with a code for your followers.

**C. Planner / travel advisor, commission**
> Hi [name], saw the NOLA trip you put together, looked like a blast. We run party boats on the bayou that groups love for bachelorettes and birthdays. We pay planners 10% on every group they send through their own booking link, and we'd love to have you out first so you know what you're selling. Want me to set that up?
