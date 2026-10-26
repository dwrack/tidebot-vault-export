# Tag-to-Story Reshare Engine (Oct 2026)

Status: idea being developed 2026-10-16. Nothing built. Revives the paused May 2026 "Story Reshare" plan, minus the Cloudflare dependency that stalled it.

## What it does
Someone tags or mentions a brand account in an IG post or reel. Within ~15 min the system pulls it, grades it, and (after Slack approval, or automatically once calibrated) reshares it to that brand's Story with a credit to the creator, then thanks them in a comment. Every brand, same engine, per-brand settings.

## Why
- "Tag us and we'll share you" is the cheapest UGC engine there is, and it only works if the share actually happens, fast, every time. Managers miss tags inside the 24h story window.
- Feeds the share-to-unlock idea: the thank-you comment can carry the discount code.
- Keeps the brand stories alive on days nobody posts.

## Flow
1. Detect: poll Graph API `/{ig-user-id}/tags` every 15 min per account (tagged posts and reels). Caption @mentions come via the mentions webhook; story mentions arrive as `story_mention` DMs (OpenCX lane, phase 2). Polling, not webhooks, for v1: no public endpoint, runs as a launchd loop on davids-mbp-2.
2. Grade (Claude vision, one call per item): on-brand yes/no, sentiment, visual quality 1-10, people/kids visible, competitor logos, text/overlay junk, is the account a real customer vs spam/bot. Output a 1-10 score + one-line reason.
3. Route (decided 2026-10-16, David wants minimal babysitting):
   - score >= 8: AUTO. Posts to the brand Slack channel, waits 2 hours for a ❌ veto, then publishes on its own. David does not need to look.
   - 5-7: queued for a twice-weekly batch (Tue + Fri). TideBot posts one bulleted list per brand, ✅ on the message publishes the lot, ✅ on an item publishes just that one. Feed/reel tags never expire, so the wait costs nothing.
   - <5 or spam: log only.
   - Story mentions (24h window, phase 2): auto at >= 7, no veto delay.
   - Feed repost (score 9+ reels only): queued for the Tue/Fri batch, always needs ✅. Decided: yes, do feed reposts for the best ones.
4. Publish (two paths):
   - A. Graph API Story (v1): build a 1080x1920 story frame (media + "@creator" credit + brand mark), publish with `media_type=STORIES`. Reliable, works for all 11 linked accounts, no phone. Limits: no native tap-through to the original, no mention sticker, so the creator is NOT notified by the story itself.
   - B. Native reshare via phone-harness (v2): tap "Add post to your story" on the posting phone. Real reshare, mention sticker, creator notified. Costs a phone per few accounts + ban-safety rules. Do this after A proves volume is worth it.
5. Thank the creator (notifies them even on path A): reply on their post from the brand account, 3-4 rotating warm variants, NO discount code (decided 2026-10-16). One per creator per 30 days.
6. Creator ledger (decided 2026-10-16): `_Ops/UGC Reshares/<brand>-creators.csv`: handle, follower count, # tags, avg score, best permalink, last tagged, engagement on their post. Monthly roll-up ranks creators; David decides who gets a discount, free trip, or ambassador offer. Outreach is manual and approved, never automatic.
7. Log: `_Ops/UGC Reshares/<brand>.csv` (date, creator, permalink, score, decision, story id). Weekly line in the Monday helm post, change-gated.

## Per-brand settings (one yaml)
account id, slack channel, min score, auto-publish on/off, thank-you variants, discount code or none, blocked handles.

## Guardrails
- Never reshare kids' faces without a manual ✅ (score forces manual when minors detected).
- Never reshare posts that also tag a competitor.
- One story reshare per creator per 7 days, max 4 reshares per brand per day.
- Auto-publish is live from day one for score >= 8 with a 2h veto window (David's call 2026-10-16). First 2 weeks: Claude reviews the grader's calls weekly and tightens the prompt.
- Instagram pacing rule applies: Graph API only, one call at a time, stop on 429.

## Where it runs
davids-mbp-2, launchd loop every 15 min, Python, META_IG_TOKEN (system user, never expires). Slack via TideBot (reaction handler already exists for approvals). No Cloudflare, no R2: media_url from the API is good for the story build, nothing is archived except the CSV + a copy of approved media in the brand vault Assets/UGC/.

## Timeline
- Week 1: build, dry run on NPB and NKST against the last 30 days of tags (grade only, nothing publishes), David skims one scored list.
- Week 2: live on NPB + NKST with auto 8+ / Tue-Fri batch.
- Week 3-4: add HPB, Austin, E&E; DCKT and Cave Point when spring starts.
- Later: path B native reshare on the phone fleet; story-mention DMs via OpenCX; share-to-unlock code in the thank-you comment.

## Decisions (David, 2026-10-16)
1. Auto-publish 8+ with a 2h veto; 5-7 batched Tue/Fri; he does not want to babysit daily.
2. Story + feed repost for 9+ reels (feed always ✅).
3. No discount in the thank-you. Log creator quality, decide outreach monthly.
4. Pilot: NPB + NKST.

## Known gaps
- 12 FB pages have no linked IG (NOLA Bike Bar, LSKT, Crescent City, Hidden Adventure, DC Detours, DC Ebike, and others): nothing to poll until linked.
- @kayaknola token gap (see IG Graph setup reference): fix the System User asset assignment before NKST pilot.
