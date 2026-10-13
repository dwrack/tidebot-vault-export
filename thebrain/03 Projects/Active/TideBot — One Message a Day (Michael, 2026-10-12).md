# TideBot: one message a day

Requested by Michael in #the-helm, 2026-10-12. Reason: crew and managers have communication fatigue from TideBot comments. Target: TideBot sends at most ONE scheduled message per channel per day. It still answers when someone @mentions it.

## What posts today (verified 2026-10-12 on the always-on Mac)

| Poster | Where | Cadence now |
|---|---|---|
| TideBot (Railway) per-log coaching and content asks | brand crew channels, as thread replies on guide trip logs | one reply per log. Could not read its reply log from this session, so the daily count is unverified. This is the likely fatigue source. |
| nkst-log-watch | #new-orleans-kayak-swamp-tours | runs every 30 min, actually posted 1 to 3 reminders a day over the last 4 weeks |
| helm-monday goals | private #helm-npb, #helm-nkst, #helm-hpb, #helm-bbk, #helm-lskt | once a week, Monday 6am |
| helm-weekend pacing | same #helm-* channels | once a week, Wednesday 7am |
| review-watch | weekly | Monday 5:33am |
| @Claude bridge, tidebot-do | #the-helm and tagged threads | reply only when tagged or asked |

The Reddit lead posts, EOD posts, and capture-challenge posts were already paused in September.

## Proposed change

1. **TideBot (Railway):** stop replying to individual trip logs and audio logs. Collect everything it would have said (coaching notes, clip asks, missing-log reminders) into one digest per crew channel, posted once a day at 7:00am local for that business. Skip the post entirely on a quiet day. @mention replies stay on.
2. **nkst-log-watch:** stop posting reminders directly. Hand its missing-log list to the same daily digest. Keep the 30-min check running so the data is current.
3. **helm-monday, helm-weekend, review-watch:** already one message or fewer per day. No change unless Michael wants them folded into the digest too.
4. **Digest format:** phone-sized, under 10 lines, business name in the first line, nothing cross-brand.

## What has to happen to ship it

- Code change in the tidebot repo plus a Railway redeploy. David approves.
- Edit nkst-log-watch to write to the digest instead of posting. Reload the launchd job on the always-on Mac.
- Nothing above has been applied. Waiting on David's go.

## Addendum: Michael wants off TideBot's Slack until this ships (2026-10-12)

Checked the always-on Mac: none of the scheduled loops tag or DM Michael (Slack ID U0ATYT71R25). He only sees the posts because he is a member of the channels. The one place his ID appears is the @Claude bridge allow-list, which only answers when he tags it, so that stays.

So "take me off" has to be a Slack-side change, and only David can approve it:
- Remove Michael from the crew channels and #helm-* channels that TideBot posts into, and re-add him when the digest version is live. The bot can't be muted for one person.
- Also add his ID to a no-tag list in the Railway TideBot during the digest change so he never gets @'d by it.

Nothing applied. Waiting on David.

## Open question for Michael

Does "one message a day" mean one per channel, or one across the whole workspace? Plan above assumes one per channel. If he means one total, the digests should merge into a single #the-helm post for David and Michael and the crew channels go silent except for @mentions.
