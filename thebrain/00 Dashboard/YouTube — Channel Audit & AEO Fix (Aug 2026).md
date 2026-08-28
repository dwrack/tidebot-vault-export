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

## STOP: the automation layer is dead, and that changes the whole fix order

*Added 2026-08-28 after the full title audit. The `(N)` artifacts were a symptom. This is the disease.*

Three YouTube scheduled jobs are loaded, firing on schedule, and failing on every single run. Nobody has seen it because the failures go to log files nobody reads.

### 1. Admire NOLA social mirror: broken since July 28, 25,185 logged failures

`com.admirenola.yt-mirror` runs **every 15 minutes**. It pulls each new Admire NOLA YouTube Short and posts it to Instagram and Facebook. It has failed on every video since **2026-07-28** with `spawnSync yt-dlp ENOENT`.

**`yt-dlp` is not installed on this machine.** Not on PATH, not in either Homebrew directory.

The state file `mirrored.json` still lists the three videos it was seeded with on 2026-06-23. That means **every Admire NOLA Short published in the last month never reached Instagram or Facebook.** Roughly 30 videos, produced and paid for, that went to YouTube only. The log has 25,185 failure lines because it retries the entire backlog four times an hour.

This is the most expensive item in this document. It is also probably a one-line fix: install yt-dlp.

### 2. Buffalo Bayou drip: authenticates, then dies

`com.bbk.youtube-drip` runs daily at 09:00. It successfully authenticates to the right channel (the log's safety check passes and prints `channel OK: Buffalo Bayou Kayak Tours`), then crashes:

```
FileNotFoundError: /Users/davidrack/bbk-yt-migration/upload_queue.json
```

The queue file is gone. The job has been doing this at least since Aug 23. BBK has published nothing since **July 19, 40 days ago.**

### 3. Austin Kayak daily: MODULE_NOT_FOUND every run

`com.akt.youtube.daily` runs daily at 09:15 and dies on a Node `MODULE_NOT_FOUND`. Recent log: 21 runs, 21 errors. AKT has published nothing since **June 21, 68 days ago.**

### What this means

The Shorts machine everyone assumes is running is not running. Three of the businesses in this audit stopped publishing between 40 and 68 days ago and the jobs meant to publish for them have been failing loudly into files with no reader.

**Do not bulk-edit 882 titles while this is true.** Fix the jobs, or the next batch reintroduces every artifact below.

**Not yet checked:** `com.djl.hpb-yt-drip`, `com.djl.npb-yt-drip`, `com.djl.dckt-yt-drip`, `com.ebbember.yt-mirror`, `com.ebbember.yt-scheduler`. Given three for three, assume broken until proven otherwise. HPB last published July 7, which is consistent with a fourth dead job.

**The missing alarm.** Every one of these failures is invisible because nothing watches the logs. Whatever gets fixed, the fix is incomplete without a check in the morning brief: any scheduled job that failed its last N runs gets a line in Coverage Gaps. A job that fails silently for 32 days is worse than no job, because everyone believes it is working.

## Title audit results (all 8 reachable channels, 50 most recent each)

| Channel | Finding | Count |
|---|---|---|
| Buffalo Bayou | Titles ending in a `(N)` variant counter | **27 of 50** |
| Austin Kayak | Exact-duplicate titles across separate videos | **18 videos, 6 titles** |
| Admire NOLA | Duplicate uploads, every duplicate sitting at 0 views | **11 of 37** |
| Ebb & Ember | Duplicate title pairs from a re-upload batch | **~14 pairs** |
| Ebb & Ember | Instagram captions used as titles, truncated mid-sentence with `…` | 6+ |
| Ebb & Ember | Every title carries a `\| Ebb & Ember Portland` suffix | all 50 |
| Door County | Unlisted raw camera filenames (`011f9f2f0ca547fb9e2b2bb5b347c681.MOV`, `take a million.MOV`) | 2 |
| NKST | A Door County zip-line video sitting on the New Orleans channel (`G6TBWhZKTT8`) | 1 |
| NOLA Party Barge | Clean. No artifacts found. | 0 |
| Houston Pedal Barge | Clean. No artifacts found. | 0 |

**Worst offender is Ebb & Ember,** which is the business we just decided to put money behind. Sample of what is public right now:

- `The PNW's most peaceful adventure is waiting — take a peak inside before we | Ebb & Ember Portland`

That title is cut off mid-sentence, and "take a peak" should be "peek." Duplicate titles run through the whole channel: "Meet The Downpour," "Everyone is cool under the downpour," "Four reasons you should probably just book it" each exist twice with different view counts.

**Door County and NKST are the models.** DCKT titles like `Cana Island Lighthouse Half-Day Kayak Tour in Door County` and `Kayaking to Devil's Bathtub at Cave Point County Park` are specific, searchable, and carry a place name. Copy that pattern everywhere.

## The single number that settles the Shorts argument

NKST's most-viewed video:

> **`Manchac Swamp Tour by Kayak: New Orleans' Wild Cypress Bayou`**
> Uploaded **May 2016**. Long-form. Search-written title.
> **467,082 views. 82% of everything that channel has ever earned.**

The 2026 Shorts on that same channel get roughly 1,000 views each. A second 2016 upload, `Honey Island Swamp Tour: Guided Kayak Trip Near New Orleans`, has 22,090. `Manchac Swamp Tour: Guided Kayak Trip Through New Orleans' Cypress Swamp` from 2017 has 39,618.

Three search-titled long-form videos from 2016 and 2017 are still out-earning everything published since, on a channel that has since shipped hundreds of Shorts. That is the argument for search-intent video, made with our own data, on our own channel.

## Fix queue, cheapest first

### 0. Install yt-dlp (one command, unblocks a month of stalled distribution)
`brew install yt-dlp`. This alone restarts the Admire NOLA mirror to Instagram and Facebook. Highest return per keystroke in this document.

### 1. ~~Write the two blank channel descriptions~~ **DONE 2026-08-28**
Buffalo Bayou Kayak and Houston Pedal Barge both now carry a full description and keyword set. Pushed live via `youtube_update_branding`, approved by David.

### 2. Repair the three dead jobs, then add a failure alarm
BBK's missing `upload_queue.json`, AKT's `MODULE_NOT_FOUND`, and the yt-dlp install above. Then check the four unaudited jobs. Then wire a log-failure check into the morning brief so this cannot happen quietly again.

### 2b. Strip the title artifacts (only after the jobs are fixed)
27 `(N)` titles on Buffalo Bayou, 18 duplicate-titled videos on Austin Kayak, the Ebb & Ember truncated captions, and the two DCKT raw filenames. Doing this before the uploaders are fixed just means doing it twice.

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
- **Titles beyond the 50 most recent per channel.** The API caps `list_my_videos` at 50, so this covered roughly 400 of 882 videos. The older tail is unaudited.
- **Four of the seven-plus YouTube scheduled jobs.** `com.djl.hpb-yt-drip`, `com.djl.npb-yt-drip`, `com.djl.dckt-yt-drip`, `com.ebbember.yt-mirror`, `com.ebbember.yt-scheduler` were not opened.
- **What uploads to the Admire NOLA channel.** Found the outbound YouTube-to-social mirror, did not find the job creating the duplicate YouTube uploads.
- **Whether the failed Admire NOLA mirrors were ever posted to IG/FB by hand.** Assumed not, based on `mirrored.json`.
