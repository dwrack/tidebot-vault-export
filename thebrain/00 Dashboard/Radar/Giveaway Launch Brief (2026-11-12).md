# Cross-Brand Giveaway: Handoff Brief (written 2026-11-13)

Status verified 2026-11-12. Nothing public has posted. No customer has been messaged.

## Approved by David (2026-11-12)
- Brands (8): NPB, Houston Pedal Barge, NOLA Bike Bar, NKST, DCKT, Buffalo Bayou Kayak, Austin Kayak, Lone Star Kayak. Ebb and Ember excluded. Cave Point, Detours, Tiki Boats left out (assumed, not confirmed).
- Platforms: Facebook, Instagram, TikTok.
- Prize: 6 tickets (NOT a private barge). Kayak brands: tour for 4 (proposed, not confirmed).
- Dates: launch Tue Nov 17, close Sun Nov 29, draw Mon Nov 30.
- Ad: boost each post for engagement, $10/day per brand (assumed from "approve"), two hooks for 48h then cut the loser.
- Facebook entry = comment "who are you bringing" (Facebook bans share/tag to enter). Instagram and TikTok = follow + tag friends.
- Auto-message versions to split-test:
  - A: You're entered to win 6 tickets on the tiki barge. Winner gets drawn Monday, Nov 30 and we'll message you right here. Celebrating anything soon?
  - B: same, ending "What are you drinking if you win?"
  - Kayak brands B: "What are you hoping to see out there?"
- Rejected: "What are you wearing?" and "Have you been out with us before?"

## Built
- Auto-message script: `~/Projects/giveaway-autodm/reply.py <page_id> <post_id> [--send]` (dry run by default, Meta official private reply, one per comment, state file prevents repeats). Messages in `messages.json`.
- Hidden NPB test post (unpublished): https://www.facebook.com/1593787309417704/posts/1741439517985815 , post id `195245397959049_1741439517985815`, NPB page id `195245397959049`.
- Meta AI research harness: `~/Projects/meta-ai-harness/`. Findings: `Meta AI Competitor Scan 2026-11-12.md` in this folder.

## Known facts
- OpenCX (NPB) handles Messenger and Instagram DM sessions, but has no comment trigger and no private-reply action. Route: Meta sends the first message, the person's reply lands in OpenCX. Only NPB's OpenCX was checked.
- The Meta token in `~/.claude/settings.json` env has pages_messaging and comment permissions for NPB.

## Next steps, in order
1. BLOCKED ON DAVID: he comments on the hidden test post from his personal Facebook (on his dashboard).
2. Run `reply.py 195245397959049 195245397959049_1741439517985815 --send`, confirm the message arrives.
3. David replies in Messenger; confirm the session opens in OpenCX and the AI answers correctly.
4. Load giveaway facts (prize, dates, rules) into each brand's OpenCX so the AI does not invent details.
5. Check OpenCX Messenger/Instagram connection for the other 7 brands.
6. Build creative for 8 brands (Text-Overlay TikTok style + Giveaway Carousel for rules). Show David every final post before anything goes live.
7. Run /design-review before scheduling reply.py on davids-mbp-2.
8. Delete the hidden test post after the test passes.
