# Summer 2026 Newsletter Series — Plan & Send Guide

16 emails, 2x per week for 8 weeks, to past customers. Goal: get Cave Point paddlers to come back for Door Bluff, get Door Bluff paddlers back to Cave Point, and get everyone onto an e-bike while they are up here. Poetic, photogenic, short enough to actually read.

Built June 17 2026. Everything lives in `~/Projects/dckt-tools/newsletter-2026/`. The 16 ready-to-send HTML files are in `out/`.

## Status

- 16 emails drafted and rendered (HTML + plain text). DONE.
- Recipient list deduped: **31,751 unique valid emails** (the FareHarbor export had no dupes). DONE.
- SES production path tested: a live test sent from `info@doorcountykayaktours.com` (us-west-2) landed in the business inbox, renders correctly. DONE.
- **Nothing has gone out to customers. Waiting on your go.**

## Two things I need from you before the first send

1. **Hero photos.** Each email has a hero image slot that pulls from `https://www.doorcountykayaktours.com/wp-content/uploads/newsletter/emNN-hero.jpg`. Screenshot the suggested reel frame (listed per email below), name it `em01-hero.jpg` ... `em16-hero.jpg`, and upload them to a `/newsletter/` folder in WP Media. Until then the emails still send fine, they just show the caption text instead of a photo. This is the one manual step. I can also pull frames with ffmpeg if you get me the raw clips.
2. **Approve the cadence.** See the reputation note below. 16 sends to 31.7k in 8 weeks is doable but it is the aggressive end. I recommend it, with the recency caveat handled by SES warmup.

## Suggested schedule (Wed + Sat)

| # | Send | Theme | Subject | Primary CTA |
|---|------|-------|---------|-------------|
| 01 | Wed Jun 24 | Cave Point clarity | The water is so clear it looks fake | Cave Point half-day |
| 02 | Sat Jun 27 | Door Bluff shipwreck | There is a 130 year old shipwreck down there | Door Bluff half-day |
| 03 | Wed Jul 1 | E-bike to the caves | The easiest way to reach Cave Point | E-bike tour / rental |
| 04 | Sat Jul 4 | First-timer reassurance | First time in a kayak? You are exactly who this is for | Cave Point |
| 05 | Wed Jul 8 | Dogs welcome | Yes, the dog can come | Eco Estuary |
| 06 | Sat Jul 11 | Two faces (cross-sell) | There are two Door Counties. Most people only see one. | Both half-days |
| 07 | Wed Jul 15 | Devil's Bathtub | The jump you will be talking about all winter | Cave Point half-day |
| 08 | Sat Jul 18 | Eco Estuary calm | Where the lake goes completely quiet | Eco Estuary |
| 09 | Wed Jul 22 | Weather / free reschedule | Why we watch the wind for you | Cave Point / shipwreck |
| 10 | Sat Jul 25 | Half-day upsell | Why our repeat guests always pick the half-day | Both half-days |
| 11 | Wed Jul 29 | Golden hour | The light up here at the end of the day | Cave Point |
| 12 | Sat Aug 1 | Family / multigen | A day the whole family will actually agree on | Cave Point + Surrey |
| 13 | Wed Aug 5 | Death's Door history | How Death's Door got its name | Door Bluff half-day |
| 14 | Sat Aug 8 | Perfect-day plan | How to spend one perfect day on the water | Kayak + e-bike |
| 15 | Wed Aug 12 | September secret | The locals' favorite month is not the one you think | September Cave Point + fall e-bike |
| 16 | Sat Aug 15 | Full menu | Pick your Door County day | All |

Dates are a clean Wed/Sat run starting Jun 24. Shift the whole thing by editing when you send. The 4th of July email (04) is reassurance, which fits a holiday inbox.

## What else we talk about (your "what else" question)

Beyond the three core goals, the series covers: beginner reassurance (the tipping fear), dogs on board, Devil's Bathtub cliff jumping, the calm Eco Estuary, how we make weather calls and the free reschedule, why the half-day wins, golden-hour light, the whole-family angle, the Death's Door history, a one-perfect-day itinerary, and why September is the secret month. Every one of them ends pointing at a booking.

## How the booking tracking works

Every booking button carries two things:

- **A FareHarbor `ref` tag** like `ref=nl_em02_ship_half`. FareHarbor stamps this onto the actual booking, so in your FareHarbor reports you can see exactly which email drove which purchase. This is the real purchase attribution, and it survives the checkout (unlike GA4, which loses email attribution through the FareHarbor lightframe).
- **UTM params** (`utm_source=newsletter`, `utm_medium=email`, `utm_campaign=cross_sell_summer_2026`, `utm_content=emNN_tour`) for click tracking in GA4.

To read results: in FareHarbor, filter bookings by the `nl_` referrer tags. Each email and each tour has its own tag, so you can tell that email 02's shipwreck button outperformed its 2-hour button, etc. Judge on bookings driven, not GA4 revenue (deposits make GA4 look low, that is normal).

## How to send

From `~/Projects/dckt-tools/newsletter-2026/`:

```
node build.mjs                                  # rebuild HTML after any copy edit
node recipients.mjs                             # rebuild the list (run after editing unsubscribes.json)

node send-ses.mjs --email em01-clear-water                      # DRY RUN, sends nothing
node send-ses.mjs --email em01-clear-water --test you@you.com --go   # one real test to yourself
node send-ses.mjs --email em01-clear-water --go --limit 500     # send to first 500 (warmup)
node send-ses.mjs --email em01-clear-water --go                 # full send (it makes you type the count to confirm)
```

Sender details, all wired in: From and Reply-To are `info@doorcountykayaktours.com`, region us-west-2 (production), concurrency 12 (well under the 31/sec quota), List-Unsubscribe header on every message, CAN-SPAM physical address in the footer. Every send writes a `sent-emNN-DATE.json` log with ok/fail counts.

## Sender reputation, read this once

You are sending to a 31.7k list that has not been emailed much. Do this and you stay out of spam folders:

- **Warm up.** For email 01, send in waves: `--limit 500`, wait a few hours, `--limit 3000`, then the rest the next day. After the list proves clean, later emails can go in one shot.
- **Process bounces.** After each send, pull SES bounce/complaint notifications, add those addresses to `bounces.json` (array of `{"email": "..."}`), and re-run `recipients.mjs`. Repeatedly mailing dead addresses is what actually tanks a domain. The smart long-term move is an SES configuration set with an SNS topic that auto-collects bounces. I can set that up.
- **Honor unsubscribes fast.** Right now unsubscribe is a mailto that hits `info@`. Watch for those replies, drop them into `unsubscribes.json`, rerun `recipients.mjs`. A real one-click unsubscribe page on the WP site would be better and I can build it.
- **Cadence.** 2x/week is fine for engaged people but will fatigue a cold list. If opens drop or complaints rise after a few sends, I would thin the cadence to 1x/week for the back half. Your call, I will watch the logs.

## A couple of notes

- The emails are signed "The crew at Door County Kayak Tours," not your name, per the standing rule about your name on outbound business mail. If you would rather a named human (Bella, a guide), tell me and I will swap the signature.
- No sunset kayak tour is sold, so email 11 sells the late-afternoon light on a regular tour, not a "sunset tour" SKU. Same for Peninsula e-bike and Cana Island, I kept the CTAs on things that are actually bookable.
- Pricing used: Cave Point 2hr $69 + $4 park fee, half-day $145, Door Bluff $69 / $145, Eco Estuary $65, e-bike tour $99, e-bike rental $30/hr. If anything changed, tell me and I rebuild.

## Per-email hero screenshots to grab

| File | Screenshot from | Note |
|------|-----------------|------|
| em01-hero.jpg | reel #43 | clearest turquoise water over rock |
| em02-hero.jpg | reel #98 | underwater Fleetwing timbers |
| em03-hero.jpg | reel #81 | aerial trail curving to the shore |
| em04-hero.jpg | reel #147 | calm glassy launch / still water |
| em05-hero.jpg | reel #57 | dog in a life vest on a kayak |
| em06-hero.jpg | reel #4 | paddling into the sea cave |
| em07-hero.jpg | reel #8 | cliff jumper mid-air over clear water |
| em08-hero.jpg | reel #107 | pelican flock over the glassy estuary |
| em09-hero.jpg | reel #166 | glassy mirror-still shoreline |
| em10-hero.jpg | reel #12 | full group raising paddles |
| em11-hero.jpg | reel #145 | golden-hour shoreline glow |
| em12-hero.jpg | reel #37 | rafted-tandem family group |
| em13-hero.jpg | reel #126 | towering layered cliff strata |
| em14-hero.jpg | reel #67 | "POV: you booked with us" frame |
| em15-hero.jpg | reel #142 | fall-foliage canopy |
| em16-hero.jpg | reel #2 | postcard Door County establishing shot |

Reel URLs for every email (3 each) are in the footer of each email and in `out/manifest.json`.
