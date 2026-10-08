# YouTube Round 2 Plan: Slack Clips + Quote Voiceovers (Oct 2026)

Status as of 2026-10-07: planned, nothing uploaded yet.

## Where the channel stands
- IG backlog drip finished Jul 23. 161 live, 24 skipped on purpose (off-brand hobby/travel), 3 failed (retryable, files are on the laptop at `~/dckt-yt-migration/videos/`).
- Drip job on davids-mbp-2 still runs daily at 10:45 and logs "nothing left."

## Source pool
| Source | Count | Notes |
|---|---|---|
| Failed old IG uploads | 3 | Cave Point sea caves, sunset sailboats, Jimbo's July 4th forecast |
| New IG reels since Jun 25 | 20 | Never queued. Includes rough-water cancels (Jun 25, Jul 18, Sep 18) and e-bike reels (Jun 29, Jul 22) |
| Slack #doorcountykayaktours | 30 | Jul 12 to Oct 3, ~0.1 GB total (short phone clips). Unreviewed |

Priority themes: e-bikes, rough water at Cave Point.

## Phase 1: Slack clip review
1. Download the 30 clips (DJL Slack user token, read-only) to `~/dckt-yt-migration/slack/raw/`.
2. Frame contact sheet per clip, watch every one.
3. Sort: keep / keep-with-caution (guest faces, kids) / toss (shaky, under 5s, dupes).
4. Tag by theme: e-bike, rough water, glassy water, caves, guide life.
5. David approves the keeper list before anything goes public.

### Slack review results (2026-10-08)
Clips at `~/dckt-yt-migration/slack/raw/s01-s30.mp4` (laptop). Download note: the Slack user token lacks `files:read`; downloaded via the Profile 14 debug Chrome session.

No e-bike footage in Slack at all. Rough water is the strongest pool.

| Bucket | Clips |
|---|---|
| Rough water (keep) | s07 waves exploding off the Cave Point cliff (best clip), s18 green surf into the caves, s14 golden-hour waves along the caves, s16 + s30 stormy shore/dock, s17 choppy launch, s28 kayak bow in chop, s29 whitecaps, s05 hazy chop |
| Glassy/clear (keep) | s09 + s03 emerald water at Cave Point, s27 cliffs + green water, s01 fleet staged on clear rock-bottom water, s26 glassy dusk, s25 overlook with kayakers below |
| Sunsets (keep) | s21 (27s, best), s12, s13, s22, s23 |
| Caution: guests on camera | s11 guests in kayaks (faces), s15 dock with guests small in frame |
| Toss | s02 (minors, trail), s06, s08 (feet), s10, s19, s20 (shadow), s24 |

Pilots built from s07/s18/s14, s09/s03/s27, s01/s25/s26 at `~/dckt-yt-migration/slack/pilots/` (text-only, VO pending key).

## Phase 2: Quote voiceover pilots (3 videos)
- **Quotes:** public domain only. Thoreau, Muir, Emerson, Whitman, Melville, Twain. Decided 2026-10-07.
- **Matching:** rough water gets Melville/Muir on storms and sea; glassy mornings get Thoreau on stillness; e-bikes get Twain/Whitman on the open road.
- **Format:** 15-30s Shorts. Quote on screen + ElevenLabs VO, natural water sound or soft bed, close on logo + book link. Credit the author on screen.
- **Voice:** ElevenLabs (David has an account, used for Admire NOLA). Samples at `Admire NOLA/Content/Voice Samples/` (EL-Brian, EL-Daniel, EL-George, EL-Eric etc.). Commercial use needs at least the $5/mo plan.
- **Blocker:** no ElevenLabs API key found on this MacBook. Needs to be set up locally via a hidden-prompt `.command` script, stored at `~/.config/elevenlabs/api_key` (never in a vault).
- Run each quote line through `/copy-mentors` only for the on-screen framing/title, never to alter the quote.
- David picks a voice and style from the 3 pilots before scaling.

## Phase 3: Scale
- Same treatment for approved Slack keepers + 20 new IG reels. Retry the 3 failed uploads as-is.
- Drip about 1/day, e-bike and rough water first, through the existing `com.djl.dckt-yt-drip` job on mbp-2 (titles from actual content, never positional).
- Then: make the job auto-pull new IG reels going forward.
