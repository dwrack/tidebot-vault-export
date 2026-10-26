# OTA + AI Visibility Audit 2026-10-16

Checked live 2026-10-16. Viator: 29 keyword searches (top 24 each) plus 113 supplier lookups, then Viator's bot check blocked further requests. GYG: 13 city/category pages, then rate-limited. ChatGPT: 4 logged-out queries. Claude: not sampled (needs David's login). Gemini: the daily loop has never produced a result (see #1).

## Bottom line
- **Nobody is visibly "buying" the top slots.** Zero "Promoted" or "Sponsored" tags in any Viator search grid or GYG page I checked. The paid lever on both is a commission bump, and it doesn't show a label in search. You can't tell who is paying. You can only spot listings ranking above their review count.
- **GYG says it outright** on every listing page: rank uses "revenue (including supplier commissions)", and "suppliers can increase commissions as part of their marketing investment."
- **ChatGPT already favors us in New Orleans** and links official sites, not OTAs. **Door County is the AI gap.**
- **Most of our brands are missing from the OTA top 10**, and in Houston and Door County the categories are close to empty. Those are cheap wins.

## Per brand

| Brand | Viator (top 24) | GYG (category top 10) | ChatGPT |
|---|---|---|---|
| New Orleans Kayak Swamp Tours | "manchac swamp kayak tour": #2, #3, #4 (4.9, 994 reviews). **Not in the top 10 for "kayak swamp tour new orleans" or "new orleans swamp tour"**, while Zip NOLA's kayak listing (28 reviews) sits at #6 | NOLA kayak: #2, rated 4.2 on only 14 reviews. Wild Louisiana is #1 "Top pick" at 4.8 on 138 | **#1 named** for kayak swamp tour |
| Nola Pedal Barge / Freaky Tiki | "pedal bar new orleans" #1, "bachelorette party boat" #6, "tiki boat" #7, "pedal barge new orleans" #10 (4.8, 116 reviews). Its URL still says Party-Bike-Bar-Booze-Cruise | BYOB Tiki Boat is listed under Gravity Trails LLC; not in the boat/swamp top 10 | **Freaky Tiki #1**, and 4 of the top 5 bachelorette boats look like our fleet (Twerkin' Tiki, Party Queen, Bayou Boogie) |
| NOLA Party Barge, NOLA Bike Bar, Gravity Trails ebike, Crescent City, Hidden Adventure, Honey Island | Not found in the top 24 or by brand-name web search. Brand-name searches got cut off by the block, so these are unverified | Not found | Honey Island Kayak Tours named #3 (confirm it's ours) |
| Lone Star / Austin Kayak Tours | Lone Star supplier ID 46479. Not in the top 10 for any Austin query. Boats and Bats #1, Austin Rowing Club #2 (both running a "Special Offer") | Austin kayak: #5 "Bat Bridge Sunset" (4.6, 6 reviews). Austin Rowing Club #1, "#1 selling", GYG Originals | **Austin Kayak Tours #1**, Lone Star #3 |
| Lone Star in Houston / Buffalo Bayou Kayak | "kayak houston" and "buffalo bayou kayak tour" show no real kayak listing in the top 10 | Houston kayak: #1 rental (4.6, 12 reviews), **#2 Sunset Skyline Kayak Tour at 3.4 stars (5 reviews)** | Not sampled |
| Houston Pedal Barge | "pedal barge houston" top 10 is NASA tickets, CityPASS, and similar. **No pedal barge at all** | Houston boat #1 is a Galveston BYOB cruise (new, 0 reviews). No barge | Not sampled |
| Door County Kayak Tours | Not in the top 10 for "door county kayak tour", "cave point kayak tour" or "shipwreck kayak tour". The Door County results are Segway and boat cruises. A DCKT bluff tour exists on Viator (seen via Groupon) but doesn't rank | Door County kayak category: **1 listing** ("Cave Point Kayak Tour", tagged Chicago, new, 0 reviews, operator unconfirmed). Boat cruises own the page | **DCKT not named.** Lakeshore Adventures #1, Cave Point Paddle & Pedal #2 (ours), "Door County Kayak" Ellison Bay #3 |

## Who is paying
- **Viator Accelerate** (the paid product; there's no CPC "Viator Ads"): you set a higher commission per product. Reported rates run about 28% to the high 40s, and 42 to 51% buys "no competitor ads on my product page". No minimum and no published ROAS. The ads show as "Promoted" shelves on product pages, not in the search grid. Source: Arival trade press and Viator's site-operation page.
- **GYG:** a commission bump feeds the ranking directly, per GYG's own disclosure. Its supplier site mentions "Premium ads" but gives no pricing.
- **Suspected payers (inference, not proof):** Zip NOLA's kayak listing outranks ours on our money keyword with 3% of our review count. Austin Rowing Club holds #1 on both OTAs with "Special Offer" or "#1 selling" tags. Either could also be explained by title match or conversion rate.

## Ranked actions (nothing spends money or touches a listing without your OK)

| # | Action | Est. cost | Why |
|---|---|---|---|
| 1 | Fix the Gemini loop: change one line in `run.py` from `gemini-2.5-flash` to `gemini-3.8-flash`. Every check since launch has failed with a 404, which is why the Scoreboard says "never". I was blocked from editing it; needs your OK. Also set the missing nkst, nola and nolapedalbarge keys | $0 (free tier) | No Gemini or Viator-in-Gemini data until it's fixed |
| 2 | Pause or fix the GYG Houston "Sunset Skyline Kayak Tour" (3.4 stars). Push 5+ fresh reviews or unpublish | $0 | One bad listing drags down GYG's Provider Rating for every Lone Star listing |
| 3 | Retitle the NKST Viator products so they read "New Orleans Kayak Swamp Tour" (they currently lead with "Manchac", which tourists don't search) | $0 | Our 994-review listing misses the top 10 on its own money keyword |
| 4 | List the missing products where categories are near empty: Houston Pedal Barge and BBK on Viator and GYG; DCKT Cave Point and shipwreck on GYG; the NOLA Party Barge fleet on GYG | Viator reportedly $29 per listing (unverified) + 20 to 30% commission per booking | Houston and Door County kayak/barge searches have almost no real competition |
| 5 | NKST GYG review push (post-trip ask to GYG bookers). Optional: GYG Creator Reviews beta | $0 (Creator Reviews cost unknown) | 4.2 on 14 reviews vs Wild Louisiana's 4.8 on 138 |
| 6 | Get DCKT into the sources ChatGPT cites for Door County (Door County Guide, TripAdvisor lists, doorcounty.com) | $0 to low | DCKT isn't named at all; two of the top 3 named are Lakeshore and a possible look-alike |
| 7 | Line up the operator names: the Tiki boat is "Gravity Trails LLC" on GYG and "Nola Pedal Barge" on Viator, and its Viator URL still says Party-Bike-Bar | $0 | Mixed names make it harder for AI assistants to tie listings to one brand |
| 8 | Only after 2 to 5: a 30-day Viator Accelerate test on one proven product (NKST Small-Group Manchac). Raise commission by about 8 points | About $7 extra per booking on a $90 ticket | No published ROAS anywhere, so test it on one product only |
| 9 | Same test on GYG (commission +5 pts on the Austin Bat Bridge tour). Ask the GYG account manager for Premium ads pricing | About $2.50 per booking on $50 | GYG ranks on commission directly |

## Gaps in this audit
- Viator brand-name searches and GYG operator lookups for the Door County listings were blocked mid-run. I didn't try to bypass the bot checks. A re-run tomorrow, or through the mbp-2 Chrome bridge (also blocked for me this session), would fill these in.
- Viator's "Promoted" shelves load client-side on product pages, so I couldn't confirm who is on Accelerate.
- Claude wasn't sampled, and the ChatGPT sample is 4 queries, logged out, one run each.

Sources: [Viator Gemini launch](https://tripadvisor.mediaroom.com/2026-07-30-Viator-Becomes-Googles-First-Connected-App-for-Travel-Experiences), [GYG fall release](https://getyourguide.press/blog/fallrelease2026), [Arival on Viator Accelerate 2.0](https://arival.travel/article/viator-accelerate-2-0-what-it-is-and-why-it-matters/), [GYG ranking help](https://supply.getyourguide.support/hc/en-us/articles/13980972906525-How-ranking-works-on-GetYourGuide), [GYG supplier pricing](https://getyourguide.supply/join/how-much-does-getyourguide-charge), [Viator Badge of Excellence](https://partnerresources.viator.com/?p=725), [GYG NKST listing](https://www.getyourguide.com/new-orleans-l370/new-orleans-manchac-swamp-wildlife-kayaking-tour-t819721/), [Viator Freaky Tiki](https://www.viator.com/tours/New-Orleans/Party-Bike-Bar-Booze-Cruise/d675-218142P1)
