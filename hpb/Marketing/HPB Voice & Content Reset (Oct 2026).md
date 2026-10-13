# HPB Voice & Content Reset (Oct 2026)

Written 2026-10-12 after David asked to rethink HPB's voice and what gets pushed. Inputs: live IG feed (28-day reach 24,799, near-daily posting, 1-7 likes per post), the June 2026 organic readout (full FB + IG history), Brand Story & Values, the 532 grid, Dom Bair's 0-100M playbook (TheBrain 06 Learning), and the 10 staged carousels.

---

## What's wrong, in one paragraph
The cadence is finally right (near-daily since September) and the posts are empty. "Come see us Houston! #houstontx" is a caption with no hook, no person, no question, and no reason to stop scrolling. Our own data from 158 IG posts says exactly what works here and we've been doing the opposite: short captions (median 5.5) instead of long (24), statements instead of questions (question hooks run 2.6x baseline), stills and generic clips instead of carousels (the best format we have, median 56.5, and we've posted two in five years), no emoji (3+ emoji posts run ~3x), and "emotional moments" copy that is the single worst theme on this account. The one post in 60 days with a point of view ("BYOB and come get LIT Houston") got 149 likes. Everything else got single digits. The voice on paper (Stella) is good. It has never made it into the feed.

## The voice, restated for the feed
Stella: a Houstonian who's lived here long enough to be annoyed that people say there's nothing to do. Confident, a little chip-on-the-shoulder, never pushy. Sells the outcome (your crew, your cooler, your playlist, Kemah lights) and never the specs.

Every post passes four checks:
1. **Does it open with a question or a specific?** "Bar crawl or party barge?" "$800 split 20 ways is $40 each." Not "Come see us."
2. **Is the boat the subject, with people on it?** Gorilla rule from Bair: no views from people who will never book. Memes, celebrities, and dance clips are vehicles only if the boat and the group are the point.
3. **Does it name who it's for?** Bachelorette, birthday crew, the team that earned it, family in town. Named groups beat "everyone."
4. **Does it ask for the share or the save?** "Send this to the maid of honor." "Forward this to whoever plans the holiday party." HPB is a group-decision product; shares are the metric, likes are noise.

Never: "luxury," "unique," "don't miss out," "memories," "moments with strangers," award/bragging copy, the word pedal (brand name only), and one-line captions.

## What the data says to post (ranked)
| Lever | Evidence | What it means now |
|---|---|---|
| Question hooks | IG since-2024 median 18.5 vs 7 baseline | Slide 1 or caption line 1 is a question whenever it fits |
| Carousels | n=2, median 56.5, best format on the account | 10 staged, posting daily from Oct 13. This is the test. |
| Long captions + 5-10 hashtags + 3+ emoji | 24 vs 5.5; tags 14 vs 4; emoji 33 vs 12 | Every caption: hook, context, CTA, emoji, 8-10 tags |
| Named groups | bachelorette/group holds above baseline | Rotate bachelorette, birthday, corporate, family |
| Giveaways (tag a friend) | 5 of IG's top 7 all-time, FB's two monsters | One per month, HPB Giveaway v2 doc already drafted |
| Dance trends | 2 of FB's top 6 (Swag Surfin) | Keep one per month on FB, boat in frame |
| 5pm CT weekday, Fri/Wed/Sun best | hour-of-day median 48 at 5pm vs 11am | Carousel queue posts 5pm CT |
| Drop: emotional/moments, bragging, stills, one-liners | worst themes since 2024 | Gone |

## The face question
Bair's phase 1 is founder-led because people follow people. HPB has no face in the feed. Connor is overloaded (3 businesses, absorbs labor) and should NOT be asked to be on camera weekly. Options, in order:
1. A captain or deckhand who likes the camera, paid a small per-clip bonus. Connor names one person; that's the whole ask.
2. Stella stays the written voice (carousels, captions) and the face comes from guests: the UGC repost pipeline, reaction captures by crew (grid rows 5, 17, 30).
3. David as "the guy who built it" for launches only, not weekly.
Decision for David. Default is option 2 now, option 1 when Connor names someone.

## Rebuilt content mix (per week, 7 posts)
- 3 carousels (question hook, long caption, share CTA)
- 2 reels from the 532 grid, layout B text-over-b-roll first since it needs no one on camera (rows 2, 4, 8, 14, 16, 20, 26, 28)
- 1 guest-reaction or UGC repost
- 1 practical/offer post for FB cross-post (booking link helps on this page; weekends filling up, giveaway month)
Holiday-party angle (team outing, family in town) owns November. Bachelorette owns spring. "Nothing to do in Houston" is evergreen.

## The carousel test (started 2026-10-12)
10 carousels, one per day at 5pm CT, Oct 13 through Oct 22, in this order:
1. Houston has a waterfront (Q hook, the thesis)
2. Public cruise vs private charter (Q, pricing)
3. Bar crawl vs party barge (Q, bachelorette)
4. Four things Houston gets wrong (myth-bust)
5. Your team outing doesn't have to suck (holiday party)
6. First cruise? Three things to know (Q, practical)
7. What our crew wishes every group knew (practical)
8. Family in town, Thanksgiving on Clear Lake (Q, seasonal)
9. Meet the boat (specs, lowest expectation, control post)
10. What Houston groups say (reviews; count verified before posting)

Hook split: 4 question openers, 6 statements. That split is deliberate so the readout can confirm or kill the question-hook rule on carousels.

What we measure (per carousel, 72h after post and again at 7d): reach, saves, shares, profile visits, follows, comments. Compare to the account's 2026 median (6 likes, ~? reach). Winner = top 3 by shares+saves. Loser = below the account median on reach.

What we do with it (Oct 23): re-run the top 3 formats with new topics, cut the bottom 3 formats, rebuild week 3 of the grid from the winners, and decide whether question hooks earned their slot.

Queue + log: `Marketing/Carousels - Staged/queue.json` (mirror of the poster queue on davids-mbp-2 `~/hpb-carousels/`). Readout: `python3 ~/.claude/scripts/hpb_carousel_readout.py` writes `Marketing/Carousels - Staged/RESULTS.md`.

## What 981 Google reviews say (added 2026-10-12, full read: `Marketing/Customer Voice — 981 Google Reviews (Oct 2026).md`)
- **The face question is answered.** Captain or crew are named in 38% of text reviews (295 of 782). By name: Bella 78, Tom 71, Abby 66, Zach 64, Don 44, Jade 30, Ahmad 30, Shay 27, Jeff 26. Customers already made the crew the brand. Whoever of those is still on staff is the on-camera face; Connor only has to say which one.
- **Their words, not ours.** Customers say "vibe" (45), "boat ride" (40), "cruise" (20). They almost never say "party barge" (2), "charter" (4), or the boat names Delta Dream / Mama Tried (0). Captions and slide copy should say "boat ride," "the whole boat," "vibe." The 10 staged carousels were rewritten 2026-10-13 before the first post: 'private charter' became 'the whole boat', 'party barge' in copy became 'boat ride' (brand name and handle unchanged). David's call.
- **What they actually describe:** fun/blast (38%), crew (38%), friends/group/girls (19%), BYOB/cooler/ice (14%), relaxing/vibes (9%), birthday (8%), family/kids (6%). Music/playlist 5%, Kemah/view 5%, sunset 1.4%, dolphins once. The playlist is a bigger deal in our copy than in their reviews; the crew is a far bigger deal in their reviews than in our copy.
- **Pedaling is a non-issue in reviews.** About 6 mentions as an activity, zero complaints. The brand story's worry that it "costs bookings" is a pre-purchase objection, not a post-trip one. Keep de-escalating it on the site and in DMs, stop spending feed posts on it.
- **Complaints (18 one-stars, all about what happens around boarding, none about the ride):** cancellations / no captain / boat down (8, often after a 45-60 min drive); the June 6, 2026 storm day (8: leaking roof, soaked seats, felt pushed out in lightning; 6 say they got a gift card instead of the promised refund, useless out of state); manager conduct (5, named; rude, blocked numbers, stopped answering); and 3 say "seats 26" but about 12 real seats. Four-star hedges: vulgar playlist, weak speakers, heat, a late guest holding the boat.
- **Marketing implications of the complaints:** the carousel line "26 means 26" and "up to 26 guests" is true for capacity and contested for seating; David should decide whether copy says "room for 26" instead. The refund-vs-gift-card pattern is growth play #1 (credit over refund) done wrong: credit works when it is offered as a choice, not substituted for a promised refund.
