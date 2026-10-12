# NPB Email Engagement Research (2026-10-12)

## Bottom line

1. Stop the weekly whole-list blast now. 4 bookings and $1,140 from 388,537 sends, with rebooking identical to 2025 (0.17%), means the newsletter is not moving bookings. A once-a-year occasion buyer does not need 52 emails a year.
2. The Promotions tab is not your problem and fighting it is a waste. A plain SES test also landed there, so it is sender-level, not design. Your real problem is click collapse (0.83% to ~0.2%) and 2.1% bounces, which hurt reputation.
3. Build the program on timing and relevance: anniversary email in each repeat guest's usual month (with their own review), a 3-email win-back for one-timers, and a small seasonal send (Halloween, Mardi Gras, Jazz Fest) only to people who clicked in the last 6-9 months.
4. Reel-driving emails are fine as a secondary element, but the booking link must be the primary click. Measure by FareHarbor ref tag per email and per link, not by opens (Apple MPP makes opens meaningless).
5. Judge it by 3 numbers: tagged bookings per 1,000 delivered, 90-day-engaged list size (clickers), and complaint+bounce rate. Run a holdout (10%) so you can finally prove lift versus the 0.17% baseline.

---

## 1. Gmail Promotions vs Primary

Google publishes no tab formula. What follows is vendor consensus (Suped, Close, PowerDMARC, Customer.io), flagged as not primary-sourced.

| Factor | Effect on tab | NPB takeaway |
|---|---|---|
| Recipient engagement history (opens, replies, archive/delete, moving you to Primary) | Heaviest factor per vendors | Ignored mail trains Gmail to file you in Promotions. 33-46k mostly-dormant guests is the drag. |
| Per-user training (drag to Primary) | Works per user, unreliable at scale | Only helps for warm repeat guests. |
| Sender reputation, complaints, volume spikes | Affects inbox vs spam more than tab | Your 0.016% complaints is excellent. 2.1% bounces (8,213 of 388,537) is not. Clean the list. |
| Content: images, many links, promo words, buttons | Pushes to Promotions | Your plain SES test also landed there, so content is not the only cause. |
| Auth (SPF, DKIM, DMARC) | Foundation, required for bulk (>5,000/day to Gmail) | Confirm all three pass plus one-click List-Unsubscribe (URL form). Google reportedly enforcing since Nov 2025. |
| ESP shared IPs | Shared IP reputation can bleed in | Check whether SendGrid IP is shared or dedicated. At 40k/week you could justify dedicated. |

BIMI: gives a logo next to your name in supported inboxes. It needs DMARC at enforcement and (for Gmail's checkmark) a VMC or CMC certificate. It builds recognition but I found no solid evidence it moves tab placement. Low priority. Unverified.

**Is Promotions bad for NPB? No, not for this business.** Evidence is thin (vendor opinion: people check Promotions when hunting offers). For a party-boat buyer planning a trip, Promotions is where travel deals are read. Primary placement matters for the anniversary email only because it is personal, and a one-to-one tone plus a reply invitation is the realistic route. Do not contort design to escape Promotions.

**Promotions annotations / deal cards:** Gmail can show image, logo, promo code and expiry on the Promotions tab preview. Constraints per third-party docs: mobile app only, sending domain must be approved by Google, Gmail decides when to show, no tracking of effectiveness. Verdict: skip. NPB runs no discounts, so there is no deal to annotate, and you cannot measure it. Revisit only if you run a dated offer (for example a Jazz Fest weekend rate). Syntax is inconsistent across sources (JSON-LD vs microdata), so verify against Google's docs before any build.

## 2. Benchmarks and why weekly whole-list sends decay

Benchmarks conflict, so treat them as ranges. Unverified at Mailchimp/Klaviyo travel-specific level.

| Metric | Reported range | Source quality |
|---|---|---|
| Travel/hospitality click rate | 0.77% to 2.43% | Two secondary roundups disagree 3x |
| Global avg click rate | 1.4% to 2.0% | MailerLite / martech.zone |
| Travel open rate | ~22.6% (inflated by MPP across the board) | Secondary |
| Klaviyo flows vs campaigns (click) | 5.58% vs 1.69% | Klaviyo benchmark page |
| Flow vs campaign revenue per recipient | ~18x higher for flows | Klaviyo |
| Automated vs scheduled campaign revenue per email (2025) | $3.41 vs $0.155 | Omnisend, via Hello Retail (secondary) |
| Triggered vs batch conversion | 3.41% vs 0.55% (older) | Blueshift |

Where NPB sits: 0.37% click is well under even the low travel figure, and the audience is stale, one-time buyers. Your own data is the best benchmark: week 1 0.83%, then 0.2-0.3%.

I found no travel-specific "click to booking" benchmark. Your own number is the one to use: 4 bookings from 1,424 clicks is 0.28% click-to-booking, about $0.003 per delivered email.

**Why weekly whole-list sends decay (inference from the sources plus your data):**
- Week 1 pulled the curious and recently-engaged; the remainder do not plan a trip this month. Most guests booked once for an occasion, so there is no "next trip" to trigger.
- Mailbox providers watch engagement; sending constantly to non-engagers lowers future placement (vendor consensus). Opens are unusable since Apple MPP, so engagement must be defined by clicks plus first-party data (booking, site visit).
- Over-mailing causes quiet tune-out well before unsubscribes (Mailpro). Your 94 unsubscribes and 0.016% complaints show people are not angry, they are just ignoring you. That is worse for tab placement than angry.
- Sunset caveat: long purchase cycles justify keeping some inactive buyers. NPB's repeat guests return about every 12 months, so use a 12-18 month window for them, not 90 days.

**Recommended sunset rule for NPB:** no click and no booking in 9 months, AND not in an anniversary window in the next 60 days = move to quarterly only. No click in 18 months = stop mailing. Hard-bounced and role/old addresses off immediately.

## 3. What makes people look forward to emails

Honest limitation: my searches returned solid detail on Morning Brew, Help Scout, CB Insights, and almost nothing on Chubbies, Skift or Death Wish Coffee emails. I did not verify examples from tour operators. Do not treat the list below as researched travel-brand case studies.

| Example | What worked (per sources) | NPB translation |
|---|---|---|
| Morning Brew | One imagined reader, signed by named editors, humor as a "sprinkle", riddles, consistent format | Write to one persona (the bachelorette planner). Same recurring bit each send. |
| Help Scout | Issues signed by a real team member | Sign as the captain or crew, not "NOLA Party Barge". Respect the rule on not using David's name; use captain or manager. |
| CB Insights | Irreverent, signature sign-off, strong voice | A repeatable sign-off line. |

Ideas that fit NPB (my judgment, not benchmarked):
- **Crew and captain stories:** a captain's one-paragraph "worst gator sighting" with their first name.
- **Guest photo of the month:** feature a real group, with permission, tagged to the month they rode. Drives forwarding (they send it to their group chat).
- **Local-insider content:** "what to do the day after your boat ride," bayou wildlife calendar. Useful content earns reading.
- **A playful recurring series** (for example "Bayou Report": one wildlife sighting, one local tip). Sending less often with a recognizable format beats weekly variety.
- Reply-friendly closers ("what was the best part of your trip?") help engagement signals and Primary placement.

## 4. Email to Instagram reels

- **Does it convert?** I found no data on email-to-Instagram-reel clicks. Unverified. A reel link opens the Instagram app, sends the guest into the feed and away from booking. Treat reels as brand warmth, not conversion. Your own data will answer this: compare reel-link clicks to Book Now clicks per send.
- **Presentation:** real video does not play in email (CanIEmail: most clients unsupported). Standard pattern is a linked image. Vendor claims say animated GIF thumbnails beat static play-button images (6-10% vs 2-4% CTR, unnamed dataset), but one A/B (Wave.video) showed the GIF edge was not significant. Directional only. If you try a GIF, keep it under 1 MB, first frame must read as a good static (Outlook shows frame 1), and test it against your current thumbnail.
- **Recommendation:** make the thumbnail click go to a booking-adjacent page (a landing page on nolapartybarges.com embedding the reel) rather than Instagram. Then the guest is on your site with Book Now one scroll away.

**Link-level measurement (SendGrid):**
- Enable click tracking and the Event Webhook; click events carry the clicked `url` (so UTMs come back in it) plus any custom args you attach to the message. Ref: SendGrid Event Webhook reference.
- Give each link its own UTM: `utm_source=email&utm_medium=newsletter&utm_campaign=<send-id>&utm_content=reel|book|review`.
- Booking attribution: append your FareHarbor ref/tracking tag per campaign (and per link where FareHarbor allows) so FareHarbor bookings tie back to a specific email. Check exact FareHarbor param naming in your account, unverified here.
- Bots and security scanners click links too; count a click as real only if the Book Now page has a session (GA4) or the click is not within a second or two of delivery.

## 5. Segments and triggers that beat blasts

Klaviyo's published data: flows get ~3x the click rate and ~18x revenue per recipient versus campaigns. Anniversary-specific benchmarks do not exist in what I found (only a dated 2010 deck). Directionally, though, triggered beats batch, and NPB's data (repeat guests return annually, same month, book 9 days ahead) says timing is the whole game.

| Trigger | Who | Timing | Notes |
|---|---|---|---|
| Anniversary | Repeat guests (about 2%) and any guest with a matched review | 5-6 weeks before usual trip month, reminder at 2 weeks | Highest-value program. Small list, so reply-like personal tone. |
| 3-email win-back | One-time guests with consent, 9-24 months since ride | Day 0, day 10, day 25, then stop | Different angle each: memory, what is new, ask a question. No discount. |
| Seasonal event | Clickers in last 9 months | 3-4 weeks ahead of Mardi Gras, Jazz Fest, Halloween weekend, Saints/LSU weekends | Visiting-group demand. Tie to date: "Halloween's on a Saturday" already works as a hook. |
| Group-chat forward | Everyone in the sequences | One line: "Planning for a group? Forward this to whoever is organizing" | Bachelorette organizers are the decision-maker. Add a unique forward-to-friend link tagged ref=forward. |
| Upcoming-NOLA signals | Opted-in guests only | If they reply or click about a trip | I found no reliable data source for "visiting NOLA soon" without ad or location data. Do not scrape. Use clicks on seasonal content as the proxy. |

**Quoting a guest's own review back to them:**
- Reviews are public on Google, so quoting is legally low risk, but the creepy line is the recipient not expecting you to have connected their name to their review. Mitigations: use only first name plus a short snippet, show it as "You said this after your ride in March 2024" with a link to the review so they own it, never quote anything private (survey, DM, booking notes), skip if the review was negative or mentions people other than the guest, and provide an easy way to say don't use this.
- The match (Google display name to FareHarbor guest) is inherently fuzzy. Require high-confidence matches only (same email or exact full-name plus ride date) and otherwise use a generic aggregate: "3,642 reviews, 4.9 average."
- Privacy/legal check on that is unresolved here; get a quick read before launch. Unverified.

## 6. Recommended NPB program

### Stop
- Weekly whole-list send to all 33-46k.
- Counting opens (MPP) as a success metric.
- Mailing hard bounces and chronically unengaged addresses (clean the 2.1% bounce pool first).
- Treating Promotions placement as a problem to fix.

### Keep
- Experience-led, no-discount voice. Subjects like "Still the only party boat with alligators" are fine; the issue is the audience and frequency, not the writing.
- One short story and a Book Now button. Reels as a secondary element on your own landing page.
- One-click URL unsubscribe (no mailto), already required.

### Start

| Program | Segment | Cadence | Goal |
|---|---|---|---|
| Anniversary | Repeat guests, usual month | 1 email 5-6 weeks before, 1 nudge at 2 weeks | Rebook (they book ~9 days out, so a 2-week nudge matters) |
| Win-back (3 emails) | One-time guests 9-24 months out, opted in | Days 0, 10, 25, then stop | Re-engage or retire |
| Seasonal drop | 9-month clickers only | 3-5 per year, tied to events | Group demand spikes |
| Monthly "Bayou Report" | Clickers + repeat guests (target 5-10k) | Once a month, crew-signed | Keeps engagement signal alive |
| Everyone else (non-clickers) | Dormant | Quarterly at most, then sunset | Protect reputation |

Start with a 10% holdout of the dormant list that receives nothing, to prove incremental bookings versus the 0.17% baseline.

### Example subject lines (NPB voice)
- "Your barge crew remembers you" (anniversary)
- "It's almost October again" (anniversary, month-specific)
- "Quick question about your last trip" (win-back 1, reply invite)
- "Jazz Fest weekend: boat's open" (seasonal)
- "Forward this to whoever's planning the group" (group-chat)

### The 3 metrics
1. **Tagged bookings per 1,000 delivered** (FareHarbor ref tag, plus holdout lift). Current: 4 bookings / 388.5k = about 0.01 per 1,000. Aim for anniversary flow well above that.
2. **Engaged list size:** unique clickers (not openers) in the last 90 days, and share of sends going to them.
3. **List health:** bounce under 1%, complaints under 0.1% (Google's published bar is under 0.3%, healthy under 0.1%), and Postmaster Tools domain reputation.

## Caveats and things I could not verify
- Gmail tab logic: vendor opinion only, no Google source.
- Travel email benchmarks: conflicting secondary sources; no Mailchimp or Klaviyo travel breakdown.
- GIF vs static CTR: vendor numbers, one non-significant A/B.
- Instagram-reel-in-email conversion: no data found.
- Anniversary email benchmarks: none found newer than 2010.
- Brand examples: Chubbies, Skift, Death Wish Coffee emails not found.
- Review-quoting privacy: reasoned, not legally checked.
- FareHarbor ref-tag syntax and BIMI effect on placement: not verified.

## Sources
- Gmail tab factors (vendor): https://www.suped.com/email-deliverability/answers/how-does-gmail-decide-which-emails-go-to-the-promotions-tab
- Gmail tab factors (vendor): https://emaillistvalidation.com/blog/how-gmail-decides-which-emails-go-to-promotions-tab/
- Gmail tab influence: https://www.suped.com/email-deliverability/answers/how-do-i-influence-which-tab-my-email-goes-to-in-gmail
- Bulk sender rules: https://www.searchenginejournal.com/google-sets-new-rules-for-bulk-email-senders/497697/
- Bulk sender rules (2026 summary): https://powerdmarc.com/google-and-yahoo-updated-email-authentication-requirements-for-2024/
- Gmail schema.org markup (Google): https://developers.google.com/gmail/markup/
- Promotions annotations (Customer.io): https://docs.customer.io/messaging/channels/email/recipes/gmail-promotions/
- Promotions annotations (Suped): https://www.suped.com/email-deliverability/answers/how-do-i-implement-gmail-annotations-and-troubleshoot-common-issues
- Promotions annotations (Dotdigital): https://marketing.help.dotdigital.com/en/articles/12781598-add-gmail-annotations-to-your-email-campaigns
- Travel benchmarks (Acoustic): https://www.acoustic.com/resources/one-pagers/travel-and-hospitality-2025-benchmark-snapshot
- Benchmarks (martech.zone): https://martech.zone/email-roi/
- Benchmarks (MailerLite): https://www.mailerlite.com/blog/20-incredible-facts-about-email-marketing
- Sunset policies (Braze): https://www.braze.com/docs/user_guide/message_building_by_channel/email/best_practices/sunset_policies
- Sunset policies (Mailpro): https://www.mailpro.com/blog/email-sunset-policy
- Sunset and deliverability (Simon Data): https://www.simondata.com/blog-posts/email-deliverability-best-practices
- Morning Brew voice: https://marketingagainstthegrain.com/articles/morning-brew-on-channels-and-voice
- Brand newsletter personality (beehiiv): https://www.beehiiv.com/blog/injecting-personality-into-your-corporate-emails
- Newsletter examples: https://www.engagebay.com/blog/best-newsletter-examples/
- Video in email (Klaviyo): https://www.klaviyo.com/blog/how-to-embed-videos-in-email
- Video in email (Wave.video test): https://wave.video/blog/images-or-videos-in-email-marketing
- GIF vs static (vendor): https://marketbetter.ai/blog/gif-thumbnails-sales-emails-outperform-static-images/
- SendGrid Event Webhook: https://docs.sendgrid.com/for-developers/tracking-events/event
- Triggered vs batch (Hello Retail, cites Omnisend): https://helloretail.com/en/blog/2026-06-09-ecommerce-email-statistics/
- Klaviyo benchmarks: https://klaviyo.com/au/products/email-marketing/benchmarks
- Bluecore triggered benchmarks: https://www.bluecore.com/blog/triggered-email-benchmarks/
