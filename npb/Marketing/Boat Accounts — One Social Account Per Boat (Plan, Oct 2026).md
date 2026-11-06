# Boat Accounts: One Social Account Per Boat

Plan written 2026-10-31. Owner: David. Nothing created yet.

## The call

Give each boat its own **Instagram + TikTok** account, run as a character under the NOLA Party Barge brand. Threads comes free with each IG. Keep **YouTube, Pinterest, Facebook and X at the brand level**, with one playlist / board / album per boat instead of a separate account per boat.

Why not every platform per boat: 5 boats x 7 platforms is 35 accounts. Nobody on the team can feed that, and split YouTube channels or Pinterest accounts each start at zero and never get out. IG and TikTok are where a "character" account actually works (the For You feed doesn't care how many followers you have). The others reward one big account.

Start with the two tikis. They're about 74% of revenue (Jul 2026 FareHarbor deep dive) and Freaky Tiki already has 48 cut-and-hooked clips sitting in `Marketing/Freaky Tiki TikTok/Ready to Post/`.

## The fleet and who each account is

| Boat | Handle (check availability) | Character | Who it sells to |
|---|---|---|---|
| Freaky Tiki | @nolafreakytiki | The wild one. Gators and champagne in the same frame | Bachelorettes, birthday girls trips |
| Twerkin' Tiki | @nolatwerkintiki | The boat named for exactly what happens on it | Bach parties, younger groups |
| Party Queen | @nolapartyqueen | The big room. 22 shared / 26 private | Birthdays, reunions, office groups, holiday parties |
| Bayou Boogie | @nolabayouboogie | The smaller, chill boat (18). Sunset, swamp, music | Couples, families, locals, smaller birthdays |
| Bentley pontoon | skip for now | Private luxury pontoon | Revisit once it's running again (needed a lower unit in Jul 2026) |

Each bio links to that boat's own FareHarbor item with a `ref=` tag (Website Standards rule), never the homepage. Each bio names the brand: "A NOLA Party Barge boat."

**Name check needed:** the registration says "Cheeky Tiki" but the site, signage and Google Ads say "Twerkin' Tiki." Use whatever's painted on the boat.

## Phases

| Phase | When | What | Gate to move on |
|---|---|---|---|
| 1 | Nov 2026 | Freaky Tiki + Twerkin' Tiki on IG, TikTok, Threads | 3 posts/week each for 6 weeks |
| 2 | Jan 2027 (bach planning season, searches double) | Party Queen + Bayou Boogie | Phase 1 shows profile visits and at least a few `ref=`-tracked bookings |
| 3 | Spring 2027 | Brand-level Pinterest, Snapchat Spotlight, Lemon8 | Clip library big enough to feed them without new shooting |

Kill rule: any boat account under ~500 followers and zero tracked bookings after 90 days folds back into the brand account. No zombie accounts.

## Platform by platform

| Platform | Per boat or brand | How |
|---|---|---|
| Instagram | Per boat | Post every reel as a **Collab** between the boat and @nolapartybarge, so it lands on both grids and pools the views |
| TikTok | Per boat | Business account, Commercial Music Library sounds only |
| Threads | Per boat (free) | Auto-share from each IG. Text posts are optional, don't staff it |
| YouTube | Brand | Shorts on the NPB channel, one playlist per boat. The IG to YouTube drip already runs |
| Facebook | Brand | Reels cross-post from the brand IG. One Facebook page can only link one IG, so no boat pages |
| Pinterest | Brand | One board per boat plus "NOLA Bachelorette Ideas." People plan bachelorettes here months ahead. Phase 3 |
| X | Brand, low effort | Auto-post only. Almost no bookings come from it. Grab the boat handles so nobody squats them |
| Snapchat Spotlight | Brand | Repost the best vertical cuts. Big 18 to 24 audience. Phase 3 |
| Lemon8 | Brand | Bach itinerary carousels. Phase 3, only if it's still around |
| Google Business Profile | Brand | Photo per boat, tagged by name. Not a new account |

**What else:** grab the handles everywhere now, even on platforms we won't use yet. It's free and stops a copycat.

## The rule that keeps the accounts from getting buried

Instagram and TikTok both push down accounts that post the same file another account already posted (Meta calls it "unoriginal content"). So:

- **IG:** don't post the same reel on two accounts. Use Collab. One upload, two grids.
- **TikTok:** no Collab, so each boat posts its own cuts. Same footage is fine with a different hook, crop and length. The hook-variant system (v1/v2/v3) already does this.
- Never post a Freaky Tiki clip on the Twerkin' Tiki account. Each account only shows its own boat. That's the whole point.

## Content supply

Each boat needs about 3 to 5 clips a week. Where they come from:

1. **Backlog first.** 48 Freaky Tiki cuts are done. Do the same frame-scan for Twerkin' Tiki, Party Queen and Bayou Boogie clips in `Assets/Videos` and `NPB video dump`, and tag every clip by boat.
2. **Crew capture.** The social-capture SOP already exists. Add one line: "Say the boat name in the file name or the first 2 seconds." Clips without a boat are useless for this.
3. **Boat-specific series** so each account has a repeat format:
   - Freaky Tiki: "Gator or no gator" (weekly gator count)
   - Twerkin' Tiki: "Read the sign" (reaction shots of the TWERKIN TIKI sign)
   - Party Queen: "How many fit" (crowd boarding timelapse)
   - Bayou Boogie: "Golden hour on the bayou" (sunset, 10 seconds, music)

## Accounts setup (per boat)

- Email: an alias on the business domain, like `freakytiki@` (or `info+freakytiki@` if aliases aren't available). Never a personal email.
- Phone for 2FA: the business line, not anyone's personal cell.
- All IG accounts under the NPB Meta Business portfolio so they show in Business Suite and can run ads.
- Passwords in the shared password manager, not a vault note.
- Bio link: boat's FareHarbor item with `ref=ig-<boat>` / `ref=tt-<boat>` so bookings show up per account.
- Bio words: no "booze" (Google Ads flag, Oct 9 rule), no pedaling, full business name.

## Posting

- One scheduler that handles IG, TikTok, Threads, YouTube, Pinterest and X (Metricool or Buffer, roughly $20 to $60/month at this account count). TikTok has no posting route we already own, so this is the cheapest way to avoid hand-posting.
- Claude builds the weekly queue per boat (clip, hook, caption, tags) into one CSV like `IG Reels Queue.csv`, with a `boat` column. Jeff approves and loads it.
- Read the numbers every Monday in the existing tracker format: views 48h, completion, shares, saves, profile visits, tracked bookings.

## What's already true (checked 2026-10-31)

- Freaky Tiki TikTok plan, keyword research, and 48 hook variants exist in `Marketing/Freaky Tiki TikTok/`.
- The TikTok Posting Tracker has 10 rows marked "queued" from Aug 27 to Sep 8 with no numbers filled in. Unverified whether @nolafreakytiki was ever created on TikTok.
- The Freaky Tiki Instagram Queue shows day 1 posted 2026-08-31. Which account it went to isn't clear from the file.

## Decisions for David

1. Go on phase 1 (two tikis, IG + TikTok + Threads)?
2. Who posts: Jeff, or a part-time creator paid per clip?
3. Scheduler: Metricool or Buffer?
4. Twerkin' Tiki or Cheeky Tiki as the public name?
