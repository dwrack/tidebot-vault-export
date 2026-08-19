# Instagram Analytics — @nolapartybarge (Aug 19, 2026)

**Live pull today:** 22,152 followers | 2,015 following | 805 posts (Graph API, profile fields only).

**Data caveat up front:** the `meta-organic` MCP server is not connected to this session, and the shared Facebook app token returns `(#10) Application does not have permission` on every Instagram media and insights endpoint. So there is **no live reach, impressions, saves, shares, profile visits, follower-growth, or audience-demographic data** in this readout. Everything below is built from (a) the live profile counters, (b) the full-history readout pulled 2026-06-20, and (c) 25 daily briefings covering Jun 20 to Aug 19. Post-level like/comment counts are real and observed; reach-based rates are not available. This is the third consecutive day IG has been dark.

---

## 1. The headline problem: 22,152 followers, ~20 likes a post

Median recent post over the last 60 days lands at **16-27 likes**. Against a 22,152 follower base that's roughly **0.09% of followers engaging**. Even accounting for how little of a follower base Instagram actually serves a post to these days, that's a coasting account. The audience was built years ago and the current content isn't reaching it.

For contrast, the account's own 2024 average was 343 engagement per post. 2026 pre-June averaged 160. The last two months are running well under both.

## 2. Three posts carried the whole period

| Date | Post | Likes | Comments | vs. median |
|---|---|---|---|---|
| Aug 5 | "Skeet skeet. Get weird this summer" reel | 197 | 12 | ~10x |
| Jul 3 | Fireworks reel | 101 | 3 | ~5x |
| Jul 16 | Lake Borgne Surge Barrier / "Great Wall of Louisiana" | 78 | 2 | ~4x |
| Jun 8 | Second-line brass band reel | 178 | 2 | ~9x |

Everything else sat between 3 and 27 likes. Aug 13 got 7. Aug 14 got 16. The spread between the best and the most recent post is roughly 40x, which is not a creative-quality problem so much as a *not repeating the thing that worked* problem.

Note the Jul 16 surge-barrier reel kept climbing for a week (44 → 59 → 69 → 73 → 78). Educational/curiosity content has a long tail on Reels. Party footage spikes and dies.

## 3. Cadence is under the stated target, with gaps

- **47 posts in the 60 days since Jun 20** (805 today vs. 758 on Jun 20) = **0.78/day**.
- The strategy doc calls for "1 reel per shift minimum, 1 story per shift minimum." Not being hit.
- Multiple stale windows flagged in the briefs: a 6-day gap Jun 13 → Jun 20 heading into a weekend, and a 5-day gap before that.

## 4. The content signal has been consistent for two months and hasn't been acted on

Every angle that outperforms is the same one the 2019-2026 history readout already identified. From that readout, by median engagement against an IG baseline of 31:

| Angle | IG median | Status |
|---|---|---|
| Giveaway / tag-a-friend | 40 | **Never run in 2026** |
| Ranked / #1 / award social proof | 37 | Underused |
| Humor / personality / POV | 36 | Aug 5 reel proved it again (197 likes) |
| Proximity "15 min from the Quarter" | 36 | In rotation |
| Party / dance energy | 34 | Overused — this is most of the feed |
| Strangers / emotional "moments" | 32, rising to 48 in 2024+ | Barely used |
| Sunset | 28 (below baseline) | **Still listed as a core content theme** |

The all-time IG monster is a 2024 reel with 34,135 likes: "Rules are rules! Don't be late!" Pure personality, zero sell. The pattern holds today: the Aug 5 crass-humor reel beat two months of party footage by 10x.

Meanwhile the strategy doc's content themes still lead with "Sunset Cocktail Cruise vibes," which is the single weakest theme on both Facebook and Instagram.

## 5. Comment replies are being left on the table

The Aug 5 reel's **12 comments have been flagged as unanswered in four consecutive daily briefs (Aug 12, 13, 15, 19)**. Replying to comments in the first hours is one of the cheapest reach levers Instagram has, and it's free. Twelve people raised their hand on the best-performing post of the quarter and nobody answered.

## 6. IG traffic to the site is completely unmeasured

NKST's GA4 shows Instagram as its **largest referral source after direct** (68 sessions Aug 11, 39 sessions Aug 18). NPB has **no GA4 property ID in the business roster at all**, so nolapartybarges.com traffic from Instagram is invisible. Given NPB is the biggest revenue business in the portfolio, that's the most glaring measurement gap here.

---

## What I'd do, in order

1. **Fix the data pipe.** Connect `meta-organic` to the session. Root cause was diagnosed on Aug 16: the node MCP servers are configured to launch from `/Users/wavey/.claude/mcp-servers/...` but this machine's home is `/Users/davidrack`. Until that's fixed, every IG number in every brief is a guess. Also: the shared FB app token has no `instagram_basic` grant, so the per-account direct IG token is the only working path.
2. **Reply to the 12 comments on the Aug 5 reel.** Ten minutes. Overdue by two weeks.
3. **Repeat the Aug 5 format, three times in the next two weeks.** Short, crass, funny, zero sell. It is the only thing in 60 days that broke 100 likes twice over.
4. **Run a tag-a-friend giveaway.** Highest median theme on both platforms, recommended in the June readout, still not done. Once, not weekly — it pulls deal-hunters if overused.
5. **Rebuild the local-landmark curiosity series.** The surge barrier reel beat party footage 3-4x and kept earning for a week. New Orleans has ten more of those.
6. **Drop sunset from the content themes list.** Use it as backdrop, never as the hook.
7. **Stand up a GA4 property for nolapartybarges.com** and add it to the roster so IG→site→booking is at least directionally visible.

---

*Sources: live Graph API profile pull 2026-08-19; `FB Organic Analytics Readout 2018-2026.md` (pulled 2026-06-20, 758 IG posts); TheBrain daily briefings 2026-06-20 through 2026-08-19.*
