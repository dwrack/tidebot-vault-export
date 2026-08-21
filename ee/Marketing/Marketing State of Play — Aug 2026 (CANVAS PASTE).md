# Marketing State of Play — Aug 2026

Window: Jul 21 – Aug 19, 2026 vs the 30 days before it. Numbers pulled Aug 20.

## 1. What's actually connected

**Live and reporting**

- **Google Analytics 4** — property 524300531. Purchases and revenue tracking correctly since the Aug 1 attribution fix. This is now our source of truth for revenue by channel.
- **Google Search Console** — sc-domain:ebbandember.com. Only has data back to Jul 2, so no clean year-over-year yet.
- **Google Ads** — account 237-223-4368. Two live campaigns.
- **Google Business Profile** — reviews, replies, posts. 105 reviews at a 4.9 average.
- **Periode** — bookings, subscriptions, sales feed. Server-side purchase events firing into GA4 and Meta.
- **Instagram (@ebbandember)** — organic post and account insights.
- **ActiveCampaign** — imported, synced to Periode, lists segmented. Only lists prefixed "Subscribers" are legally sendable for marketing. Please treat that as a hard rule.
- **Attribution bridge** — the Squarespace footer script forwarding fbclid / gclid / GA client_id into Periode checkout. Before this, 100% of purchases landed as "(not set)."

**Connected but not producing**

- **Meta Ads** — $0 spent in the window. Account access exists (act_1425635901791284 via Elevated Tides) but the @ebbandember Page and IG asset are still not shared to it, which blocks running any ad off an existing IG post. That's a Business Settings share only Davey can do from his own logged-in window.
- **YouTube** — channel exists, MCP connected, but the YouTube Analytics API is disabled on the project so we have zero reporting. Also zero uploads.

**Not connected or gone**

- **SendGrid** — replaced by ActiveCampaign. Open question in #events from Aug 18 about whether the monthly is cancelled. Someone please confirm, it's a live bill.
- **No /thank-you or booking-confirmation page** on Periode. Flagged Aug 2. Without it we can't fire a clean conversion event, which is why Google Ads is optimizing against garbage.
- **No blog.** The content plan assumes /journal plus two pillar pages (/cold-plunge-portland, /private-sauna-rental-portland). None of it exists. The site is still five pages.
- **No SMS marketing.** Twilio brand approved, campaign resubmitted in June, nothing sending.

## 2. The numbers, last 30 days

### Website (GA4)

| Metric | Last 30d | Prior 30d | Change |
|---|---|---|---|
| Revenue | $20,297 | $11,674 | +74% |
| Transactions | 297 | 213 | +39% |
| Sessions | 2,463 | 1,760 | +40% |
| Users | 1,471 | 1,109 | +33% |
| Avg order value | $68 | $55 | +25% |

Revenue grew faster than traffic. People are booking bigger, not just showing up more.

### Where the traffic came from

| Source | Sessions | Share |
|---|---|---|
| Organic search | 953 | 39% |
| Direct | 668 | 27% |
| Instagram | 353 | 14% |
| Google Ads | 246 | 10% |
| Periode referral | 153 | 6% |
| ChatGPT | 5 | — |

ChatGPT is tiny but it's the first month it has shown up at all.

### Search (GSC)

- 1,750 clicks over the window, roughly 60/day.
- The shape matters: 80/day in late July, 44/day by mid-August. We're bleeding search traffic as the viral reel's branded-search halo wears off.
- Terms we genuinely rank for: "floating sauna portland" (68 clicks, pos 2.3), "floating sauna" (24, pos 5.1), "portland floating sauna" (17).
- **Where we're leaving money:** "sauna portland" — 357 impressions, 10 clicks, position 7.4. "portland sauna" — 149 impressions, 9 clicks, position 7.3. "cold plunge portland" — 93 impressions, 4 clicks, position 7.8. We're on page one for the big generic terms and almost nobody clicks. That's a title/meta and landing-page problem, not a ranking problem.
- Homepage does 1,697 of the 1,750 clicks. Everything else is a rounding error. /faq: 2,517 impressions, 47 clicks. /memberships: 2,466 impressions, **9 clicks**.

### Google Ads

| Campaign | Spend | Conversions | Cost/conv | ROAS |
|---|---|---|---|---|
| Core Search ($25/day) | $761 | 8 | $95.16 | **0.83** |
| Tourist Awareness ($1/day) | $31 | 4 | $7.66 | **16.97** |
| Total | $792 | 12 | $65.99 | 1.45 |

- Worst single line item: "sauna near me" — $115 spent, 103 clicks, **zero** conversions. That's 15% of total ad spend on one term that has never converted.
- Caveat worth saying out loud: the "all conversions" column shows 941 conversions on Core Search, which is nonsense. It's counting page views as conversions because we have no real thank-you page. Smart Bidding is optimizing toward the wrong thing, so the 0.83 ROAS is probably understated and the whole account is flying half-blind until that page ships.

### Instagram

- 7,046 accounts engaged over the month.
- Reach fell from ~11,000/day in late July to ~2,200/day by Aug 18. An 80% drop.
- New followers fell from 293/day to 11/day over the same stretch.
- This is a decay curve, not a failure. The Jul 17 reel ("looking for something different to do with friends in Portland?") did 2,157 likes, 28 comments and **3,378 shares**. Everything since has coasted on it. The Jun 1 reel ("No plans tonight? Might I suggest a floating sauna on the Columbia River?") did 2,014 likes and 1,796 shares. Those two posts are carrying the account.
- For contrast: Aug 18 sunrise carousel, 22 likes. Aug 5 sauna-science carousel, 17 likes. The Aug 11 "are you getting in the river this summer" reel shows 0 likes and 0 comments, which almost certainly means something broke on publish. Worth someone checking.

### Email

- Last real send was the Jul 28 member-night invite: 2,128 delivered, 43.7% open, 2.4% click, 0.80% unsubscribe, 0 spam complaints.
- 43.7% open on a 2,100-person list is genuinely good. 2.4% click is not. The offer and the CTA are the weak link, not deliverability.
- The Sept 15 member party email is built in ActiveCampaign and waiting on approval to send.

### Reviews

- 4.9 stars, 105 total. Our best owned asset.
- Three recent five-star reviews are sitting without a reply (Aug 17, 19, 20).
- One 3-star from Aug 12: a guest booked a banya session and nobody showed. Already replied to and being made right, but flagging it because it's the second operational miss that became a public review.

## 3. What we could be working on

Ranked by what actually moves revenue.

1. **Ship a /thank-you page on Periode.** Everything downstream of ad performance is guesswork until this exists. Highest leverage item here and it's a small build.
2. **Move Google Ads budget.** Tourist Awareness is doing 17x on a dollar a day. Core Search is doing 0.83x on twenty-five. At minimum, negative-keyword "sauna near me" and shift $10/day to Tourist. Five-minute change, pays for itself in a week.
3. **Fix the generic-term CTR problem.** We rank page one for "sauna portland," "portland sauna," "cold plunge portland" and get almost no clicks. That's titles, meta descriptions, and the fact that we send everything to the homepage. Building /cold-plunge-portland alone would capture a term where we currently get 4 clicks off 93 impressions.
4. **Fix /memberships.** 2,466 impressions, 9 clicks. When people do land it converts fine (15% bounce, 2:25 average time on page). The page is good. Nobody's getting to it.
5. **Get the Page and IG shared to the ad account.** We have two organic reels that did 3,378 and 1,796 shares. Proven creative sitting unused. Putting even $300 behind the Jul 17 reel is the cheapest test we'll run all year.
6. **Reply to the three open reviews** and set a standing cadence.
7. **Confirm SendGrid is cancelled.**

## 4. What we should be posting about

The data is unusually clear. Both 2,000-like reels share the same DNA: a direct, second-person invitation to do a specific thing tonight, framed as "something different to do in Portland." Not wellness education. Not benefit lists. An invitation.

What flops: educational carousels (sauna science, heat benefits) and anything leading with a feature instead of a plan.

**More of:**

- **"Something different to do in Portland" framing.** Our proven hook. Run it back with new footage, new seasons, new group types. Date night, birthday, out-of-town guests, post-run recovery.
- **The seasonal flip, starting now.** Summer ends in about four weeks and the whole feed still reads like July. Strongest winter angle we have is reframing Portland rain as something you book on purpose. Seed it in early September, don't wait for the first grey week.
- **The Downpour, and the next build.** The reveal reel did 154 likes and 67 shares; the Jul 22 "things are evolving" reel did 158 likes and 93 shares. People respond to a new physical thing they can see. The two new private saunas and the enclosed cold plunge are coming. Document that build now, post it as it happens.
- **Reviews as content.** 105 reviews at 4.9. "ooh heaven is a place on earth" is a better caption than anything we'd write. Overlay them on b-roll.
- **Memberships, properly.** 9 clicks from search in a month. Members are 58% repeat and drive 67% of revenue. We barely talk about it.
- **The Sept 15 member party** and the community-partner story around it: Human Access Project, plus the local F&B brands Lauren curated (Stray Cider, Hetty Alice, Landmass, Hama Hama, Cowbell, Little T). Cross-tagging six local brands is free reach.
- **Off-peak and Tuesday service industry.** Tuesday is our worst day at 13% full. That's what paid social and email should be pointed at.

**Less of:** standalone wellness-benefit carousels. They consistently underperform and they're what we default to when we don't have footage.

## 5. Open loops

- Member party email is built and waiting on one approval. RSVP deadline is a week before, so it needs to go out by roughly Sept 8.
- @lifted_pdx filmed the Travel Portland collab on Aug 13. Nobody has reported whether it's live or what it did.
- Star News story in progress with Maggie Grainger, quotes attributed to Jonah.
- 1859 Magazine mentioned us and pitched a Sept/Oct ad. Their deadline was Aug 14 and we said we were "evaluating." That window has closed.
- Portland Rose Festival auction invite (Oct 8) is unanswered in the inbox.
- Sharon Doka (run-club creator) collab — we replied, no call booked.
- Lodging partnerships with Innventures / South Waterfront and Brandstand are warm and moving. Ties into the lodging-referral campaign staged in the vault since June and never sent.
- Print advertising: Portland Mercury pitched. Consensus was print is dying and hard to track. Calling that a no unless someone objects.

---

Anything here is queryable. Ask and I'll re-run it.
