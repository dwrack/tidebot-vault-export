# ReplyAgent — Reddit Comment Monitor

*Set up 2026-09-24 by David. Companion to [[Reddit — Product Descriptions & Content Guidelines]] and [[Social Engagement Playbook]].*

## What ReplyAgent is
Paid tool (replyagent.ai) that scans Reddit for threads matching NPB keywords, drafts a reply, and posts it from a connected Reddit account after approval. Everything lives under one "product":

- Dashboard: https://www.replyagent.ai/dashboard/products/cmsulgdpd0006jy04qet1hpcq/comments
- Product ID: `cmsulgdpd0006jy04qet1hpcq`
- API key: local only, `~/.config/replyagent/api_key` (this Mac + davids-mbp-2). Not in this vault.
- API docs: https://www.replyagent.ai/docs (list, import, approve; no reject and no webhooks)

## Daily monitor (davids-mbp-2, 6:20am PT / 8:20am CT)
Script: `~/.claude/scripts/replyagent-monitor/monitor.py` (multi-product since 2026-09-24: no arg = NPB, `--product admire` = Admire NOLA; cron entry on mbp-2; launchd GUI domain is unreachable over SSH). Stdlib Python, no secrets in vault.

Each run:
1. Pulls preview + queue + posted comments from the API.
2. Rule-checks every draft: customer-pose ("we did NPB"), affiliation claims ("I work there", since the posting account is a ReplyAgent persona), URL, pedaling, off-list prices, gator guarantees, wrong bayou, >120 words, CTA, superlatives, banned openers, emoji, lists.
3. Fetches every posted comment's Reddit URL and checks it is still live (not [removed]/[deleted], not moderatorRemoved).
4. Flags a stalled pipeline: queue item older than 24h, or no new drafts in 3 days.
5. Posts the report to #helm-npb and appends a line to [[ReplyAgent — Monitor Log]].

Manual run from either Mac: `python3 ~/.claude/scripts/replyagent-monitor/monitor.py --dry-run`

## Approving a draft
Approve in the dashboard, or by API:
`curl -X POST https://www.replyagent.ai/api/products/<productId>/ai-comments/<commentId>/approve -H "Authorization: Bearer $(cat ~/.config/replyagent/api_key)" -H "Content-Type: application/json" -d '{"scheduleType":"immediate"}'`

Rules for approving:
- Nothing gets approved that the monitor marks BLOCK. Fix the tool's guidelines field first, regenerate, then approve.
- Always the full name "NOLA Party Barge" in a comment. Never "NPB" (David, 2026-09-24: nobody outside the company knows what that is). Product was renamed from "NPB" to "NOLA Party Barge" inside ReplyAgent the same day so the AI stops copying the abbreviation.
- The first 3 posted comments get shown to David in chat, full text, before approval. After 3 clean ones we loosen to monitor-only review.
- Name the brand in every relevant comment (David, 2026-09-24: "i don't want to not mention my brand"; ReplyAgent rotates many Reddit accounts so per-account flagging is not a concern). The old 6-of-10 / 2-of-10 credibility ratios are gone. Honest caveat still rides with every mention.
- New Orleans Kayak Swamp Tours (full name, never NKST) is the named option on swamp/bayou asks when a quiet paddle fits better than a party boat. Replaced Admire Nola in both guideline entries.

## State as of 2026-09-24 (first run)
- 5 drafts in preview, 1 in queue since 2026-08-19, 0 ever posted.
- No new drafts since 2026-08-19 (36 days). Scanner appears stopped.
- The queued item never posted in 33 days, which points to no Reddit account connected (redditAccount is null on every item).
- All 6 drafts BLOCK: 4 pose as a past customer ("we did NPB for a friend's birthday"), all 6 name the brand with no affiliation disclosure, all run 81-103 words. The tool is not running the Block A guidelines.

## What was fixed 2026-09-24 (via David's logged-in Chrome, Profile 14)
- Added a second Content Creation Guidelines entry with the Block A hard rules (never pose as a customer, disclose affiliation when the brand is named, no URLs, price list, no gator guarantees, Bayou Bienvenue only, length/format/banned words, credibility ratios, register). The original condensed entry is still there.
- Deleted all 6 drafts (5 preview + 1 unapproved from queue) with the reason "poses as a past customer, no affiliation" so their model gets the feedback.
- Ran Generate Now once to produce a fresh batch under the new rules for review.
- Billing check: Reddit Bot AI Growth Plan, $79/month, active since 2026-08-15, renews 2026-10-18, plus $50 credits. Two months paid, zero comments posted.

## How ReplyAgent actually posts (important)
There is no "connect your Reddit account" anywhere in the dashboard. Comments go out from ReplyAgent's own "professionally managed" persona accounts, and their placeholder copy literally suggests phrasing like "a tool I've been trying lately". So the platform default is covert promotion by a stranger persona. Our disclosure rule still holds ("I work there" inside the comment), but the posting account will not be an NPB-branded one. Publishing capacity per their dashboard: about 1 to 2 items per user per day.

## Approved so far
| # | Date approved | Thread | Final text check | Posted? |
|---|---|---|---|---|
| 1 | 2026-09-24 | r/AskNOLA "First Visit???" (1wojqye) | full name, no affiliation, no customer claim, 83 words | queued |
| 2 | 2026-09-24 | r/AskNOLA "Swamp Tour Next Week" (1wk5hw6) | rewritten to add NOLA Party Barge eco tour + New Orleans Kayak Swamp Tours, 106 words, David: "have them post" | queued (re-approved 2026-09-24) |

## Open items
- [x] AI Agent is RUNNING as of 2026-09-24 (daily limit 2, manual approval). Start/Stop is dashboard-only, the API key cannot do it.
- [ ] Draft #3 gets shown in chat before approval. After that, monitor-only review.
- [x] First regenerated batch (2 drafts saying "I work there") reviewed and then DELETED after David's call below.
- [x] David's decision 2026-09-24: the posting accounts are ReplyAgent personas, not us, so comments can't claim affiliation either. Model is now a plain third-party recommendation: facts only, one honest caveat, no "I work there", no "we took the boat". Guidelines entry rewritten to match, monitor rule flipped (any affiliation claim = BLOCK).
- [x] Persona accounts accepted with the recommendation-only model (David, 2026-09-24).
- [x] API key rotated 2026-09-24 via Desktop hidden-prompt script; new key on both Macs, old key returns 401.
- [x] The Admire Nola product in the same account: set up 2026-09-24 with the same model, own monitor run (`--product admire`, #helm-admire). See Admire NOLA vault, Marketing/ReplyAgent — Reddit Comment Monitor.
