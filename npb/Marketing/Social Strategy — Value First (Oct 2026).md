---
type: strategy
business: NOLA Party Barge
date: 2026-10-15
owners: David (approve), Jeff (crew + captures), JT (on-the-ground)
supersedes: NOLA Party Barge Social Media Strategy.md (2025), the sales-CTA caption formula in Freaky Tiki TikTok Launch Plan
related: "[[Social Analytics + Market Study (Oct 2026)]]", "[[30-Day Slate — Oct 17 to Nov 15 2026]]", "[[Holiday Pushes Fall 2026 — Halloween to NYE]]"
---

# NPB Social: Value First

## The one idea

**Be the most interesting account about the bayou, not the loudest ad for a boat.** Every post gives the viewer something: a laugh, a fact they'll repeat, a crew member they feel like they know, a moment they want to send to their group chat. The booking is the side effect. Nothing in the caption asks for it.

## What the numbers say

| Proof | Number | Lesson |
|---|---|---|
| "Rules are rules" mustache skit (May 2024) | 33,907 likes, our all-time best by 3x | A bit with a punchline beats any promo |
| Lake Borgne Surge Barrier explainer, boosted 3x (Jul to Aug 2026) | $0.022 per click, best in the account all year, every run | A real fact about the bayou converts cheaper than party footage |
| "Skeet skeet, get weird" (Aug 2026) | 249 shares, our best share count since June | Weird and funny gets sent to friends |
| Second-line brass at the dock (Jun 2026) | 5.2k reach, 2nd best of summer | Culture, not product |
| "Sunset from a boat, private and public trips available" (Oct 13) | 241 reach | A promo caption on a pretty shot is our floor |
| Nashville Pedal Tavern "Erik makes every ride the best ride" | 481k views | A named crew member as a character is the top format in our segment |
| Scottsdale Bachelorette "the bride only asked for Drake" | 206k views | The bride's one wild request, on camera, is the bachelorette format |

Full data: [[Social Analytics + Market Study (Oct 2026)]].

## Five pillars (every post belongs to one)

1. **Bayou Files.** Facts and stories people will repeat. The Great Wall of Louisiana. Why gators are out in October. Jean Lafitte. What Bayou Bienvenue was before it was a bayou. The surge barrier post is the template: one fact, a why, a real view of it from the boat. Send-bait: "send this to someone who thinks New Orleans is just Bourbon Street."
2. **The Crew.** Recurring named characters. Captains Ben, Eddie and Poppa Charles; deckhands Shannon, Darius, Calvin; the deadpan captain in the TACOCAT shirt (name him); Captain Save-a-Hoe skits for the bit lane. Format: "[Name] runs this boat," a weekly weather report, a word of the day, a boat-name roast. Nashville's Erik/Dan format, in our accent.
3. **Moments.** Real guests doing real things: the bride's aisle rehearsal, 25-years-married champagne guns, the worm on the bar table, a football game on the boat, strangers forming a choir. Tag-bait: "tag the friend who'd do this."
4. **Weird Louisiana.** The marina zoo and the stuff that only happens here. The horse in the shallows, the goose who runs security, the skink, the shark costume, the dog running check-in, fog that doesn't cancel. Share-bait, and it's the lane nobody else in NOLA is in.
5. **What's Coming.** Seasonal intrigue, not offers. Halloween pirate weekend (Oct 30 and 31), the costume trunks, Friendsgiving on the water, Bayou Classic, heated boats in winter. Say the date and ask a question. Never a price, never "spots are filling."

Rough mix per week: 2 Moments, 1 Crew, 1 Bayou Files, 1 Weird Louisiana, 1 What's Coming, and Stories every day a boat goes out.

## Caption rules

- **No URL, no phone number, no "book now," no "link in bio," no price** on the main feed. The bio link does that job. (David's share-first rule, Sep 2026. Now it's the whole feed, not just Batch 4.)
- One job per caption: tag, send, or save. Pick one.
- 3 to 15 words for Moments and Crew. Up to 2 sentences for Bayou Files.
- 3 to 5 hashtags, local and niche: #neworleans #nola #bayou #bayoubienvenue plus one topical. No #fyp.
- Nolan's voice (Brand Story section 4): contractions, short sentences, a little swagger, would you say it at a bar.
- Never pedals, never "world's best," never "memories that last a lifetime."
- Gator feeding or touching clips stay on NPB accounts only, never @admirenola.

## Format rules

- Reels first. Carousels only for a save-the-date or a mood set.
- A person or an animal in frame in the first 2 seconds.
- Cover line in 3 to 6 words. It's the hook, not a label.
- 6 to 15 seconds for Moments and Weird. 20 to 45 seconds for Bayou Files, where the fact needs room.
- Stories carry the info the feed no longer does: prices, which boat, how to get there, tonight's weather. Pin them in highlights: "Which boat," "Getting here," "What to bring."

## The look (one system, every reel)

Set 2026-10-15 after the first cut looked haphazard: four text styles, three resolutions, old logo cards. Same fonts and palette as the NPB carousels (`~/.claude/skills/carousel/brands/npb.json`), so the grid reads as one account.

| Element | Rule |
|---|---|
| Canvas | 1080x1920, 30 fps. Sources at 720x1280 or better only. Landscape masters crop to 9:16 on the action, never letterbox. |
| Hook panel | Anton, all caps, 100px, ink `#fbf6ee` on bayou teal `#1f4e5a`, 10px coral `#fea087` left edge. Upper left, 72px margin, 2 lines max. On for the first 3.2 seconds, then gone. Text never sits directly on the footage. |
| Brand tag | Small chip, lower left at y=1436 (clear of the IG caption zone): NOLA PARTY BARGE in Anton, BAYOU BIENVENUE in Inter 700 letter-spaced. Same teal. On for the whole clip. |
| Grade | One mild pass on everything: contrast 1.05, saturation 1.10. No LUT, no vignette. |
| Audio | Loudness-normalized to -16 LUFS so the feed doesn't jump in volume. |
| Archive bits | A clip whose burned-in text is the joke (Capt. Save-a-Hoe skits) keeps its own text and gets the tag only. Rare, labeled in the slate. |
| Never | Old "Pedal Barge" logo cards, "book the boats" end cards, emoji, drop shadows, more than one accent color, text over faces. |

Build: `Marketing/Slates/<slate>/build.py` reads `slate.json`, renders the overlays with headless Chrome (real Google fonts), cuts and grades with ffmpeg, writes the review board. Re-run after editing the slate; it only rebuilds what changed.

## The two series to start now

**"Captain's Report."** One captain, one minute, once a week, at the dock. Weather, water, what the gators are doing, one thing that happened on the last trip. Same framing every time, so it becomes a thing. Starts with whichever captain Jeff says is most comfortable on camera.

**"Bayou Files."** One fact a week, told from the boat, filmed on a phone. The surge barrier post is episode zero. Next: why the bayou is so close to the Quarter (the MRGO story), the October gator question, Jean Lafitte, the 1915 hurricane, the Isleño fishing villages.

## What this replaces

- The 2025 strategy's "street team posts with promo codes and CTAs" and "upsell visuals: champagne guns, salt gun shots" as feed content. Upsells live in Stories and the post-booking sequence.
- The Freaky Tiki caption formula ("hook + CTA line with the number"). The cuts are still good. The captions get rewritten under the rules above before any go to @nolapartybarge.
- The daily "book this weekend" reel. Replace with one What's Coming post a week that names a date and asks a question.

## How we'll know in 30 days

- Shares per reach is the number. Baseline since June: 13 shares on a 1,584-reach median post. Target: 30+ shares on a median post.
- Reach median back above 2,000 (July was 1,832, October so far 542).
- Website clicks from IG hold or grow with zero links in captions. If they drop more than 30%, the bio link needs a better landing page, not a caption fix.
- One crew member people start naming in comments.

## Who does what

- David: approves each weekly batch on the review board, signs off on the crew named on camera.
- Jeff: picks the Captain's Report captain, films it Friday at the dock, sends Crew Clips through the TideBot channel as usual.
- JT: Stories on days boats go out (weather, which boat, the marina), one a day minimum.
- Claude: cuts and stages the weekly batch from the footage library, writes captions, runs the review board, reports shares per reach every Monday.
