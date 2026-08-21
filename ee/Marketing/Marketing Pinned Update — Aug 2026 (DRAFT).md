# Marketing Pinned Update — Aug 2026 (DRAFT, not posted)

Status: awaiting Davey approval. Target channel: #marketing (C0B1H12MK1S).
Window: Jul 21 - Aug 19, 2026 vs Jun 21 - Jul 20, 2026.

---

:pushpin: *MARKETING STATE OF PLAY — AUG 2026*
_Pinning this so we all work off the same numbers. Window is Jul 21 - Aug 19 vs the 30 days before it._

*1. WHAT'S ACTUALLY CONNECTED*

Live and reporting:
• *Google Analytics 4* — property 524300531. Purchases + revenue tracking correctly since the Aug 1 attribution fix. This is now our source of truth for revenue by channel.
• *Google Search Console* — sc-domain:ebbandember.com. Note it only has data back to Jul 2, so we can't do a clean year-over-year yet.
• *Google Ads* — account 237-223-4368. Two live campaigns.
• *Google Business Profile* — reviews, replies, posts. 105 reviews at a 4.9 average.
• *Periode* — bookings, subscriptions, sales feed. Server-side purchase events firing into GA4 and Meta.
• *Instagram (@ebbandember)* — organic post + account insights.
• *ActiveCampaign* — imported, synced to Periode, lists segmented. L has it wired so "Subscribers" prefixed lists are the only legally sendable marketing lists. Read that again: *only send marketing to lists prefixed "Subscribers."*
• *Attribution bridge* — the Squarespace footer script that forwards fbclid / gclid / GA client_id into Periode checkout. Before this, 100% of purchases landed as "(not set)." It's fixed.

Connected but not producing:
• *Meta Ads* — $0 spent in the window. Account access exists (act_1425635901791284 via Elevated Tides) but the @ebbandember Page and IG asset are still not shared to it, which blocks running any ad off an existing IG post. That's a Business Settings share that only Davey can do in his own logged-in window.
• *YouTube* — channel exists, MCP connected, but the YouTube Analytics API is disabled on the project so we have zero reporting. Also zero uploads.

Not connected / gone:
• *SendGrid* — replaced by ActiveCampaign. Davey asked in #events on Aug 18 whether the monthly is cancelled and nobody answered. Someone please confirm, it's a live bill.
• *No /thank-you or booking-confirmation page* on Periode. Davey flagged this Aug 2. Without it we can't fire a clean conversion event, which is why Google Ads is optimizing against garbage (more on that below).
• *No blog.* The content plan in the vault assumes /journal plus two pillar pages (/cold-plunge-portland, /private-sauna-rental-portland). None of it exists. The site is still five pages.
• *No SMS marketing.* Twilio brand is approved, campaign was resubmitted in June, still nothing sending.

---

*2. THE NUMBERS, LAST 30 DAYS*

*Website (GA4)*
• Sessions 2,463 (up 40% from 1,760)
• Users 1,471 (up 33%)
• Transactions 297 (up 39% from 213)
• *Revenue $20,297 (up 74% from $11,674)*
• Average order value $68 vs $55 last month

That revenue jump is the headline. It's bigger than the traffic jump, meaning people are booking more per booking, not just showing up more.

*Where the traffic came from*
• Organic search — 953 sessions (39%)
• Direct — 668 (27%)
• Instagram — 353 (14%)
• Google Ads — 246 (10%)
• Periode referral — 153 (6%)
• ChatGPT — 5 sessions. Tiny, but it's the first month it's shown up at all.

*Search (GSC)*
• 1,750 clicks over the window, roughly 60/day
• But the shape matters: 80/day in late July, 44/day by mid-August. We're bleeding search traffic as the viral reel's branded-search halo wears off.
• Top non-branded terms we actually rank for: "floating sauna portland" (68 clicks, pos 2.3), "floating sauna" (24, pos 5.1), "portland floating sauna" (17)
• *Where we're leaving money:* "sauna portland" — 357 impressions, 10 clicks, position 7.4. "portland sauna" — 149 impressions, 9 clicks, position 7.3. "cold plunge portland" — 93 impressions, 4 clicks, position 7.8. We show up on page one for the big generic terms and almost nobody clicks. That's a title/meta and page problem, not a ranking problem.
• Homepage does 1,697 of the 1,750 clicks. Everything else is a rounding error. /faq has 2,517 impressions and 47 clicks. /memberships has 2,466 impressions and *9* clicks.

*Google Ads*
• Total spend $792, 872 clicks, 12 conversions, $1,149 in tracked conversion value. Blended ROAS 1.45.
• *Core Search* ($25/day): $761 spent, 8 conversions, $95 per conversion, *ROAS 0.83.* We are losing money on this campaign as measured.
• *Tourist Awareness* ($1/day): $31 spent, 4 conversions, $7.66 per conversion, *ROAS 16.97.*
• Worst single line item: "sauna near me" — $115 spent, 103 clicks, *zero* conversions. That's 15% of total ad spend on one term that has never converted.
• Caveat worth saying out loud: the "all conversions" column shows 941 conversions on Core Search, which is nonsense. It's counting page views as conversions because we have no real thank-you page. So Smart Bidding is optimizing toward the wrong thing. The 0.83 ROAS is probably understated and the whole account is flying half-blind until the thank-you page ships.

*Instagram*
• 7,046 accounts engaged over the month
• Reach fell from ~11,000/day in late July to ~2,200/day by Aug 18. That's an 80% drop.
• New followers fell from 293/day to 11/day over the same stretch.
• This is not a failure, it's a decay curve. The Jul 17 reel ("looking for something different to do with friends in Portland?") did 2,157 likes, 28 comments and *3,378 shares.* Everything since has been coasting on it. The Jun 1 reel ("No plans tonight? Might I suggest a floating sauna on the Columbia River?") did 2,014 likes and 1,796 shares. Those two posts are carrying the account.
• Recent posts for contrast: Aug 18 sunrise carousel 22 likes. Aug 5 sauna-science carousel 17 likes. Aug 11 "are you getting in the river this summer" reel posted with 0 likes and 0 comments, which almost certainly means something broke on publish — worth someone checking.

*Email*
• Last real send was the Jul 28 member-night invite: 2,128 delivered, 43.7% open, 2.4% click, 0.80% unsubscribe, 0 spam complaints.
• 43.7% open on a 2,100-person list is genuinely good. 2.4% click is not. The offer and the CTA are the weak link, not deliverability.
• The Sept 15 member party email is built in ActiveCampaign and *sitting waiting on approval.* Nameserver propagation was the last blocker.

*Reviews*
• 4.9 stars, 105 total reviews. Best owned asset we have.
• Three recent five-star reviews are sitting without a reply (Aug 17, 19, 20).
• One 3-star from Aug 12: a guest booked a banya session and nobody showed. Already replied to and being made right, but flagging it because it's the second operational miss that turned into a public review.

---

*3. WHAT WE COULD BE WORKING ON*

Ranked by what I think actually moves revenue:

1. *Ship a /thank-you page on Periode.* Everything downstream of ad performance is guesswork until this exists. Highest-leverage item on this list and it's a small build.
2. *Move Google Ads budget.* Tourist Awareness is doing 17x on a dollar a day. Core Search is doing 0.83x on twenty-five. At minimum, negative-keyword "sauna near me" and shift $10/day to Tourist. This is a five-minute change that pays for itself in a week.
3. *Fix the generic-term CTR problem.* We rank page one for "sauna portland," "portland sauna," "cold plunge portland" and get almost no clicks. That's titles, meta descriptions, and the fact that we send everything to the homepage. Building /cold-plunge-portland alone would capture a term where we currently get 4 clicks off 93 impressions.
4. *Fix /memberships.* 2,466 impressions, 9 clicks, and when people do land it converts fine (15% bounce, 2:25 average time on page). The page is good. Nobody's getting to it.
5. *Get the Page + IG shared to the ad account.* We have two organic reels that did 3,378 and 1,796 shares. Those are proven creatives sitting unused. Putting even $300 behind the Jul 17 reel is the cheapest test we'll run all year. Blocked on Davey doing the Business Settings share.
6. *Reply to the three open reviews* and set a standing cadence. Reviews are our strongest channel and we're letting them sit.
7. *Confirm SendGrid is cancelled.*

---

*4. WHAT WE SHOULD BE POSTING ABOUT*

The data is unusually clear about what works for us. Both 2,000-like reels have the same DNA: a *direct, second-person invitation to do a specific thing tonight,* framed as "something different to do in Portland." Not wellness education. Not benefit lists. An invitation.

What flops: educational carousels (sauna science, heat benefits), anything that leads with a feature instead of a plan.

Post more of:
• *"Something different to do in Portland" framing.* This is our proven hook. Run it back with new footage, new seasons, new group types. Date night, birthday, out-of-town guests, post-run recovery.
• *The seasonal flip, starting now.* Summer is over in about four weeks and our whole feed reads like July. The strongest winter angle we have is reframing Portland rain as something you book on purpose. Start seeding it in early September, don't wait for the first grey week.
• *The Downpour.* The reveal reel did 154 likes and 67 shares, and the Jul 22 "things are evolving" reel did 158 likes and 93 shares. People respond to a new physical thing they can see. We have another one coming: the two new private saunas and the enclosed cold plunge. Document that build now, post it as it happens.
• *Reviews as content.* 105 reviews at 4.9. "ooh heaven is a place on earth" is a better caption than anything we'd write. Overlay them on b-roll.
• *Memberships, properly.* 9 clicks from search in a month. Members are 58% repeat and drive 67% of revenue. We're barely talking about it.
• *The Sept 15 member party,* and the community-partner story around it. Human Access Project, the local F&B brands Lauren curated (Stray Cider, Hetty Alice, Landmass, Hama Hama, Cowbell, Little T). Cross-tagging six local brands is free reach.
• *Off-peak and Tuesday service-industry.* Tuesday is our worst day at 13% full. That's the one thing paid social and email should be pointed at.

Post less of: standalone wellness-benefit carousels. They consistently underperform and they're the thing we default to when we don't have footage.

---

*5. THINGS SITTING WITHOUT AN OWNER OR A DECISION*

• Member party email — built, waiting on one approval to send. RSVP deadline was set at a week before, so this needs to go out by roughly Sept 8.
• *Kimberlynn's last day is Sept 15 — the same day as the member party.* No successor named. Content calendar, posting, and the Travel Portland collab all live with her right now.
• @lifted_pdx filmed the Travel Portland collab post on Aug 13. Nobody has said whether it's live or what it did.
• Star News story is in progress with Maggie Grainger, quotes attributed to Jonah.
• 1859 Magazine mentioned us and pitched a Sept/Oct ad. Their deadline was Aug 14 and we said we were "evaluating." That window has closed.
• Portland Rose Festival auction invite (Oct 8) is *unanswered* in the inbox.
• Sharon Doka (run-club creator) collab — we replied, no call booked.
• Lodging partnerships with Innventures / South Waterfront and Brandstand are warm and moving. This ties into the lodging-referral campaign that's been staged in the vault since June and never sent.
• Print advertising: Portland Mercury pitched, and consensus in this channel was "print is dying and hard to track." Calling that a no unless someone objects.

_Numbers pulled Aug 20. Anything here is queryable, ask and I'll re-run it._
