# FB Repost Plan, Sep 12 - Dec 11 2026

**What's running:** 2 organic posts a day, 7 days a week, to the NPB Facebook page (89k fans). No ad spend. Every post is a video pulled from the page's own history, re-uploaded fresh with a new caption.

**Where the posts live:** on Meta itself. Each post is uploaded as a scheduled post, so it shows in Meta Business Suite > Planner (and Content > Scheduled) and Meta publishes it, no computer involved. Meta only accepts scheduling ~30 days out, so a small job on the always-on Mac tops the Meta queue up every morning from the CSV, keeping the next 28 days loaded. You can edit or delete any scheduled post right in Business Suite.

| | |
|---|---|
| Slots | 11:00am CT and 4:00pm CT (the 4pm slot is where engagement lives) |
| Days | 91 days, 182 posts, Sep 12 through Dec 11 |
| Top-up job | davids-mbp-2 (always-on), launchd `com.npb.fbposter` at 9:00 + 14:00 Pacific; schedules the next 28 days on Meta, dedups against what Meta already has |
| Queue | `Marketing/FB Daily Queue.csv` (this vault, synced by iCloud) |
| Videos | `Assets/FB Recycle/originals/` (as-is reposts) and `Assets/FB Recycle/edited/` (trimmed + hook overlay) |
| Log | `~/.claude/logs/npb-fb-poster.log` on mbp-2 |

## How the videos were picked

Pulled all 411 videos ever posted to the page with their likes, comments and views. Scored each one (engagement + views/200), dropped anything under 6s or over 90s.

- **Tier A, 119 posts: proven hits, reposted as-is.** Score 60+ (roughly the top 30%). The 26 biggest hits are parked in the Sat/Sun 4pm slots. Same file, new caption.
- **Tier B, 63 posts: mid-performers, lightly edited.** 2022 or newer, score 21-57. Each one trimmed to 22s max, hook text burned in for the first 3.5s (e.g. "COOLER ON THE BAYOU", "MEET THE CREW"), new caption. Different fingerprint, so FB treats it as new content. These take the 11am slot most days.
- Anything posted in the last 60 days is held back until it's been 60 days.
- Cold-weather captions (covered + heated) only start Oct 15. Holiday-party videos only from Nov 1. Thanksgiving / Bayou Classic / Halloween lines are date-fenced.
- No video repeats inside the 3 months. 10 Tier A hits are left in reserve.

## Captions

182 unique captions. One-liner style that wins on this page (real crowd, irreverent, place-based). No "15 minutes from the Quarter, book your boat" brochure lines. About half carry a NolaPartyBarges.com tail, half don't. Nothing mentions pedaling.

## One thing to eyeball

46 of the 182 are 2020-2021 footage (the biggest hits are from that era). Captions never say "pedal," but the footage may show the old pedal setup. If that bugs you, say so and they get swapped for 2022+ videos from the reserve pool.

## Editing the queue

Two places, depending on how far out the post is:

- **Next ~28 days (already on Meta):** edit or delete it in Meta Business Suite > Planner. The CSV row shows `status=scheduled` with the Meta video id in `post_id`.
- **Further out (still `queued` in the CSV):** open `FB Daily Queue.csv` and change `caption` or `asset_path`. Set `status` to `skip` to drop one. To add one, copy a row with a new date + slot and `status=queued`. The top-up job picks it up when it enters the 28-day window.

Watch the `src_eng` / `src_views` columns for what the video did the first time around.

## Pause / resume

To stop future posts from being loaded: on mbp-2, `launchctl unload ~/Library/LaunchAgents/com.npb.fbposter.plist` (`load` to resume). Posts already scheduled on Meta keep publishing unless you delete them in Business Suite. The MacBook copy of the job is disabled.

## Check-in

Around Sep 26 (2 weeks in): pull post engagement from the `post_id` column and compare Tier A vs Tier B, 11am vs 4pm. If the 11am slot is dead, move it to 1pm. If B edits underperform badly, swap the remaining B rows for reserve A hits.
