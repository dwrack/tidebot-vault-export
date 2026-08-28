---
type: audit
created: 2026-08-28
scope: all connected YouTube channels
source: live MCP pull 2026-08-28
status: findings + fix queue, nothing pushed live yet
---

# YouTube — Channel Audit & AEO Fix

*Pulled live 2026-08-28. Supersedes the assumption that these channels are idle. They are not idle, they are unmaintained, which is a different problem with a different fix.*

---

## What is actually there

| Channel | Videos | Views | Subs | Views/sub | Last public upload | Channel description |
|---|---|---|---|---|---|---|
| NOLA Party Barge | 169 | 888,205 | 289 | 3,073 | — | Good |
| NKST | 45 | 572,071 | 182 | 3,143 | — | Good |
| Door County Kayak Tours | 203 | 528,511 | 102 | 5,181 | — | Good |
| Houston Pedal Barge | 131 | 98,970 | 82 | 1,207 | Jul 7 (52 days) | **EMPTY** |
| Ebb & Ember | 90 | 31,283 | 7 | 4,469 | — | Good |
| Admire NOLA | 27 | 22,968 | 15 | 1,531 | — | Good |
| Buffalo Bayou Kayak | 101 | 22,538 | 9 | 2,504 | Jul 19 (40 days) | **EMPTY** |
| Austin Kayak Tours | 116 | 11,767 | 3 | 3,922 | Jun 21 (68 days) | Good |
| **Total** | **882** | **2,176,313** | **689** | | | |
| Door County Detours | — | — | — | | | **Auth dead (`invalid_grant`)** |

882 videos and 2.18 million views is a real asset. It is also 689 subscribers, which is the tell.

## The diagnosis

**These are Shorts, and Shorts views are not audience.** Door County Kayak Tours over the last 90 days:

| Video | Views | Avg view duration | Subs gained |
|---|---|---|---|
| nIEIujugx5U | 104,827 | 27 sec | **0** |
| UlE5F4HNnJ0 | 52,739 | 20 sec | **0** |
| next 8 combined | 13,006 | 8-12 sec | 4 |

Two videos carry 92% of the channel's 90-day views. 157,566 views produced zero subscribers. Average view durations of 8 to 27 seconds mean nobody is watching, they are scrolling past. The Shorts feed served us to 157,000 people who had no interest in a kayak tour in Wisconsin.

**The content was batch-dumped, not published.** Buffalo Bayou uploaded six videos within roughly thirty seconds of each other on July 18. Austin uploaded eight within two minutes on June 21. Houston uploaded seven inside half an hour on July 7. Views inside a single batch: 2,490, 115, 29, 23, 10, 8, 6, 5, 2. That spread is the Shorts lottery, not a content strategy.

**Batch-generator artifacts shipped to public.** Live public titles right now on Buffalo Bayou:

- `This Is Why People Are Kayaking Buffalo Bayou 🛶 (4)`
- `This Belongs On Your Houston Bucket List 🛶✅ (3)`
- `Trade Screen Time For Paddle Time In Houston 🛶 (3)`
- `Spend A Morning Kayaking Buffalo Bayou 🛶☀️ (3)`

Those trailing numbers are variant counters from whatever generated the batch. They are public, on a channel with 22,538 views, under a brand name.

**Two channels have no description at all.** Buffalo Bayou Kayak and Houston Pedal Barge both return an empty channel description and no keywords. Every sibling brand has both.

## Why this breaks the AEO plan specifically

[[AEO Action Plan - All Sites]] line 486 says: *"YouTube: the 30-sec guide videos become YouTube Shorts (AI Overviews pull from YouTube heavily)."*

That is true and it is also not enough. An answer engine cites a YouTube video by reading its **title, description, and transcript**. Consider what ours offer:

- Title: `Spend A Morning Kayaking Buffalo Bayou 🛶☀️ (3)`
- Channel description: *(blank)*
- Length: a few seconds, so effectively no transcript
- Description: generic or absent

There is nothing there to cite. We have 2.18 million views proving we can get distribution, and almost none of the metadata that converts distribution into a citation, a subscriber, or a booking.

**The correction to the plan is one word: order.** The plan treats YouTube as a redistribution endpoint for social clips. For AEO it has to be the origin, where the title and description are written for search before the asset ever gets cut down for Reels. Same asset, opposite direction of travel.

## Fix queue, cheapest first

### 1. Write the two blank channel descriptions (free, ~20 min, needs approval)
Buffalo Bayou Kayak and Houston Pedal Barge. Every sibling channel has a keyword-carrying description and these two have nothing. Drafts prepared, awaiting David's approval before any live write.

### 2. Strip the `(2)` `(3)` `(4)` artifacts from public titles (free, ~30 min)
Buffalo Bayou confirmed. Audit all 882 titles across all channels for the same pattern before fixing, since whatever generated them likely ran everywhere.

### 3. Turn on the YouTube Analytics API (free, 5 min, blocking everything else)
GCP project `250476721704` has the YouTube Analytics API disabled. Only the Door County project has it on, which is why DCKT is the only channel in this document with real numbers. Seven of eight channels are currently unmeasurable. Enable at:
`https://console.developers.google.com/apis/api/youtubeanalytics.googleapis.com/overview?project=250476721704`

Do this first. Every recommendation below is a guess until it is on.

### 4. Re-authorize Door County Detours (5 min)
Returns `invalid_grant`. Token is dead, needs a fresh OAuth run.

### 5. Rewrite the descriptions on the two DCKT videos carrying 157,566 views (~20 min)
`nIEIujugx5U` and `UlE5F4HNnJ0`. These are the single highest-leverage twenty minutes available on YouTube right now. They already have the distribution. Give them a real description with the tour name, the location, what the viewer is looking at, and a booking link. Even a 0.1% conversion off 157,000 views beats anything a new upload will do this quarter.

### 6. Flip the order in the AEO plan (~10 min doc edit)
Line 390's content table lists the 30-second guide intro as *"Instagram Reels, TikTok, YouTube Shorts."* Reorder to YouTube first, and add the requirement that YouTube gets a search-written title and a real description before the asset is cut for the other two.

## The bigger question this raises, which is David's call

Everything above is maintenance and it is all worth doing. But it does not answer the strategic question the data actually poses:

**Shorts are giving us views and nothing else.** 157,566 views, 0 subscribers, 20-27 second average duration. We cannot currently see whether any of it produces a booking, because the analytics API is off on seven channels and most of these businesses have no GA4.

The thing that gets cited by answer engines and found by people actually planning a trip is not a seven-second Short. It is a searchable video that answers a question: "Cave Point sea caves kayak tour, what it's actually like," "Manchac vs Honey Island swamp tour," "is the Austin bat bridge worth it from the water." Longer, titled for search, with a transcript worth reading. Ten of those are probably worth more than the next four hundred Shorts.

That is a real change in how the content gets made, not a metadata fix, so it is not in the queue above. Flagging it as the actual question.

## What I could not check

- **Traffic sources and booking attribution for 7 of 8 channels.** Analytics API disabled on project `250476721704`.
- **Whether YouTube drives any bookings at all, anywhere.** No GA4 property on most of these businesses, and NKST's GA4 does not capture FareHarbor bookings.
- **Door County Detours entirely.** Dead auth.
- **Whether the `(N)` title artifact extends beyond Buffalo Bayou.** Only sampled 8 titles per channel.
