# Narrated Video Slate — Party & Boat Sayings — Pass 70
*STAGED DRAFT, pending David's approval. Built 2026-08-15. Nothing in this document has been posted, scheduled, recorded, or handed to crew as a shot order.*

---

## Status flags (read first)

- **Nothing here has been recorded, rendered, or posted.** This machine has no ffmpeg and no ElevenLabs API key, so no audio was generated and no video was assembled. Every piece below is a script and shot plan only, ready for whoever runs the actual TTS/render step.
- **This is pass 70.** On disk, this vault held 18 complete prior slate documents going in: an unnumbered base pass, then 14, 15, 16, 17, 22, 23, 24, 25, 26, 27, 29, 36, 37, 40, 59, 60, and 61 (Pass 41's folder exists but is empty, an unresolved gap noted by prior passes and left alone here too). That's 216 prior piece titles across those 18 documents.
- **Dedup process for this pass, and why it does not simply trust the last pass's own bookkeeping:** rather than re-deriving everything from zero, this pass pulled the complete list of prior piece-title slugs directly off disk (every `*-NOTES.txt` filename across all 18 prior folders, 216 unique titles), read Pass 61 in full (the most recent, most heavily self-documented pass), and read the idea bank, Brand Story & Values, and the Crew Roster in full directly. But Pass 61's own "still untapped" list turned out to contain real errors, caught here by grepping the actual NOTES file contents for specific claims instead of trusting the summary:
  - Pass 61 listed idea **#22** (the golden-hour warning) as untapped and cited it for its own Piece 02. It is not untapped — **Pass 59's Piece 02, "This Light's the Best It's Gonna Get,"** already sources idea #22 nearly verbatim ("this right here is the best it's gonna get... the next ten minutes"). This pass does not reuse #22 either, for the same reason, and flags the error for whoever runs Pass 71+.
  - Pass 61 listed the **anhinga** as "only referenced, never centered." It was centered in full in **Pass 26, Piece 12, "The Bird That Can't Waterproof Itself,"** sourced from Script & Caption Bank Lane 9's exact anhinga fact. This pass does not touch the anhinga.
  - Idea **#54** ("Captain for a Minute" photo) and idea **#53** (birthday person hands the aux cord for the first song) both read as untapped from a casual scan but are fully consumed: **Pass 24, Piece 04, "Everybody Wants Five Minutes at the Wheel"** (idea #54, deliberately broadened past birthday-only) and **Pass 59, Piece 03, "It's Your Boat Today"** (idea #53). Idea #55 (surprise call-out via the welcome board) reads as functionally covered too, by Pass 15's "The Welcome Board" and a later pass's "She Didn't Know Until She Saw Her Name," both already on disk under different citations.
  - Net effect: **every idea-bank number cited below (#19, #23, #56, #65) was independently re-verified by grepping the actual text of all 216 prior NOTES files for the specific phrasing that number would produce, not by trusting any prior pass's "still open" list at face value.** Treat this pass's own "still untapped" section the same way going forward: as a starting point to re-verify, not a ledger to trust.
- **What this means for birthday-group and bachelorette content specifically, given the brief asks for both:** the idea bank's dedicated birthday cluster (#51-55) is now confirmed close to exhausted — #52 (age-specific roast, toast-shaped, out on saturation grounds anyway), #53, and #54 are directly confirmed consumed above; #55 reads as functionally covered by two on-disk welcome-board/name-reveal pieces; #51 (bakery dessert delivery) is at minimum adjacent to a beignet detail already used in Pass 61's Piece 05. Rather than force a sixth-plus birthday-flavored piece into crowded ground, this pass holds birthday-specific pieces at zero and says so plainly, the same way Pass 36 through 61 have held toast at zero and Pass 23 through 61 have held bachelorette at zero. The brief's "toasts, captain lines, bachelorette and birthday-group lines, running jokes" cluster is carried in this pass by captain-line, crew-instinct, and running-joke pieces (01, 02, 03, 05, 12) that don't require reskinning saturated occasion territory to deliver "things people say out loud on the water."
- **Toasts stay at zero for a seventh pass in a row** (36, 37, 40, 59, 60, 61, and now 70, all independently reaching the same conclusion: 14+ existing toast-spine pieces, nothing left that isn't a reskin).
- **Bachelorette-specific pieces stay at zero for a sixth pass in a row** (23 through 61, and now 70), for the same saturation reasoning.
- **Every spoken line in every piece was routed through `/copy-mentors` then `/copywriting-2.0`.** Mentor voice and framework applied first, then the 3-test filter (can I visualize it, can I falsify it, can nobody else say it) line by line. Specific catches and rewrites are logged in each piece's Copy Passes note below and in each piece's own NOTES file.
- **Voice rotation:** all 12 available samples used exactly once. This pass's table was solved as a constraint problem against the four most recent tables (Pass 40, 59, 60, 61) so that no position repeats any voice those four tables used at that same position. See Sourcing below for the full comparison.
- **Music bed references:** continuing Pass 59, 60, and 61's mood-only convention. No dedicated Local Sound Bank doc exists in this vault (checked again this pass) and no fresh real-artist research was performed this session. A future pass should either commission genuine research into additional real Louisiana acts or make mood-only the series' permanent convention.
- **Every piece carries a production flag.** Several pieces script something not confirmed as current, standing NPB practice: a proposed captain local-story rotation, a proposed crew read-the-room volume habit, a proposed pre-booking corporate success-call, a proposed quiet loyalty-boat-upgrade, and an alligator-nest sighting/distance protocol that needs confirming with guides before treated as routine. Two eco-tour pieces (07, 08) also flag a fact that should be double-checked against a real source (the film/TV hawk-scream convention) or a real route/season pattern (kite migration window, nest sighting frequency) before publishing. Read every flag before treating any piece as a shot order instead of a concept pitch.
- **Everything below is a draft.** Nothing gets posted, scheduled, or handed to crew as a shot order until David signs off.

## What this is

12 new narrated short-form pieces (16.0-18.0 seconds each) built around party sayings, boat sayings, and the things people actually say (and do) out loud on the water: captain lines, crew instincts, running jokes, and guide FAQ answers, split across NPB's two on-water products, per the brief. Format is modeled exactly on the Admire NOLA narrated series (`Admire NOLA/Content/Narrated/01-poetic-NOTES.txt` and `Admire NOLA/Content/Script & Caption Bank.md`): timestamped VO lines with a bracketed visual on every line, a named voice sample, a music bed, on-screen text treatment, and a shot list.

Split across NPB's two on-water products, consistent with the majority of prior passes' 6/6 framing (the vault's third product, the per-seat social boat, has never been part of this slate series and isn't introduced here either, per `Brand Story & Values.md` Section 1's own instruction not to blur the three products):
- **Private BYOB party fleet** — pieces 01-06
- **Naturalist eco swamp tour** — pieces 07-12

## Sourcing (so nothing here is invented from scratch)

- **Format/structure:** `Admire NOLA/Content/Narrated/01-poetic-NOTES.txt`, `Admire NOLA/Content/Script & Caption Bank.md`, both read in full this pass.
- **Dedup inventory:** all 216 prior piece-title slugs extracted directly from the filenames of every `*-NOTES.txt` file across all 18 prior folders on disk and checked against every title drafted for this pass; zero collisions found in the final 12. Pass 61 read in full. `Ideas/Unreasonable Hospitality — 100 Ideas for NPB.md`, `Brand Story & Values.md`, and `Crew Roster — Captains & Deckhands.md` all read in full directly.
- **Idea-bank sourcing, each individually re-verified against actual prior NOTES file content (not against Pass 61's summary, which contained the three errors logged above):** **#19** ("Neighborhood narration, not a tour script... real stories beat Wikipedia") sources Piece 01; **#23** ("Free second round energy... read the room") sources Piece 02; **#56** ("Pre-event call with the organizer... what does success look like") sources Piece 04; **#65** ("Upgrade without asking... don't announce it as a loyalty perk") sources Piece 06. Piece 03 and Piece 05 are original concepts, checked against the idea bank and found not to match any numbered item. Pieces 07-12 are original eco-tour concepts, individually checked against the facts/devices inventory below.
- **Wildlife/plant topics, verified as untapped by direct grep of all 216 prior titles' file contents, not by title alone:** red-shouldered hawk / film-sound-convention fact (Piece 07, first hawk-species piece in the series; prior raptor pieces cover osprey and bald eagle, both distinct), alligator nest and eggs specifically as opposed to hatchling-carrying behavior, already covered twice from a different angle (Piece 08; Pass 14's "Wait, Gators Can Do That" covers a mother carrying hatchlings in her mouth, Pass 16's "Same Bayou, Never the Same Tour" references a mother gator with babies on her back, neither covers nest-building or eggs, which this piece centers instead), swallow-tailed kite (Piece 09, first kite piece in the series; the vault's owl, warbler, spoonbill, and heron spotlights are all distinct species). Confirmed via direct text search of all 216 prior NOTES files that none of these three topics has been centered before.
- **Voice samples:** `Admire NOLA/Content/Voice Samples/` — all 12 available samples used once each. This machine cannot generate audio from any of them (no ElevenLabs key, no ffmpeg). Names below are casting picks for whoever runs TTS.

| Position | Voice | Position | Voice |
|---|---|---|---|
| 01 | EL-Brian | 07 | voice-en-US-RogerNeural |
| 02 | EL-Jessica | 08 | EL-Sarah |
| 03 | EL-Lily | 09 | EL-Eric |
| 04 | voice-en-GB-RyanNeural | 10 | EL-Daniel |
| 05 | voice-en-US-BrianNeural | 11 | EL-EchoRae |
| 06 | voice-en-US-GuyNeural | 12 | EL-George |

This table was built as a constraint-satisfaction check against the four most recent prior tables, so that no position below repeats any voice those four tables used in that same slot:
- Pass 40: 01 EL-Daniel, 02 EL-Sarah, 03 EL-EchoRae, 04 EL-Eric, 05 GuyNeural, 06 EL-Lily, 07 BrianNeural, 08 EL-Brian, 09 RyanNeural, 10 EL-George, 11 EL-Jessica, 12 RogerNeural
- Pass 59: 01 EL-Sarah, 02 EL-Brian, 03 EL-Jessica, 04 GuyNeural, 05 EL-Daniel, 06 RyanNeural, 07 EL-George, 08 EL-EchoRae, 09 RogerNeural, 10 EL-Lily, 11 BrianNeural, 12 EL-Eric
- Pass 60: 01 EL-Eric, 02 EL-George, 03 EL-Daniel, 04 EL-Lily, 05 EL-Sarah, 06 EL-EchoRae, 07 RyanNeural, 08 EL-Jessica, 09 GuyNeural, 10 BrianNeural, 11 RogerNeural, 12 EL-Brian
- Pass 61: 01 EL-Jessica, 02 EL-Daniel, 03 EL-Brian, 04 EL-Sarah, 05 EL-Eric, 06 EL-George, 07 GuyNeural, 08 EL-Lily, 09 EL-EchoRae, 10 RogerNeural, 11 RyanNeural, 12 BrianNeural
- Pass 70 (this pass), checked position by position against all four above and matching none: table shown above.

- **Music bed options:** no dedicated Local Sound Bank doc exists in this vault (checked again this pass). Continuing Pass 59, 60, and 61's mood-only convention rather than minting unverified real-artist names.
- **Brand voice, product split, confirmed facts:** `Brand Story & Values.md`, read in full this pass. Section 4's voice rules (guests not customers, contractions, no cruise-ship-ad language, "if it reads like a brochure, rewrite it") governed every line. Section 6's "not over-produced, no script, no forced fun" rule directly shaped how Pieces 01, 02, and 06 flag their proposed crew behaviors as illustrative rather than implying staff choreographs guest experience. Section 1's instruction to keep the three products distinct and not blur them is why this pass holds to the private-fleet/eco-tour 6-6 split and leaves the social per-seat boat out.
- **Crew roster (kept unnamed on purpose):** `Crew Roster — Captains & Deckhands.md`. No captain, guide, or deckhand is named on screen in this pass, consistent with Pass 23 onward.
- **Prior slates (title-diffed against all 18 on-disk documents):** the base pass, 14, 15, 16, 17, 22, 23, 24, 25, 26, 27, 29, 36, 37, 40, 59, 60, and 61, plus their `Marketing/Narrated/` folders.
- **Copy process:** every spoken line in all 12 pieces was drafted, then routed through `/copy-mentors` (mentor voice and framework named per piece) and then `/copywriting-2.0` (the 3-test filter, applied line by line). Specific rewrites are logged in every piece's own Copy Passes note below and in each piece's NOTES file.
- **Consent and safety standard applied throughout:** no crew named, no guest identified without a filming ask, no invented ritual presented as fact. No gator, snake, or any wildlife baiting, chasing, or cornering is implied anywhere in this pass; Piece 12 states the opposite of that policy directly. Piece 08 (alligator nest) explicitly keeps kayaks at a stated distance and flags that nest-distance protocol needs confirming with guides before this piece is treated as routine.

## Guardrails honored

- No sibling-brand mentions (NKST, Houston Pedal Barge, etc.) anywhere in this slate.
- No pedaling references (not applicable to this fleet).
- No invented price figures. No claim that any piece is existing, confirmed company tradition unless it already appears in a vault doc or prior pass. Every piece pulling from an idea bank or a new proposal is flagged below.
- No guest named or closely identified on camera without the standard filming ask.
- Brand voice rules followed throughout: guests not customers, contractions, no "curated experience," no cruise-ship-ad language. Humor stays affectionate, never mocking any real guest, crew member, or group type.
- No em dashes in spoken lines or body copy, no "utilize," no "unparalleled," no "book now before it's too late," consistent with brand and global writing style rules.
- No real hotel, concierge desk, rideshare brand, or corporate client named anywhere in this slate. No real movie or actor named in Piece 01.
- No specific merger, company, or real corporate client implied as identifiable in Piece 04.
- David's name does not appear anywhere in this slate or in any on-screen credit.

---

## The slate at a glance

| # | Title | Lane | Product | Voice | Target |
|---|---|---|---|---|---|
| 01 | Half the Boat Googles It by the Dock | Heartfelt / funny, captain line | Party fleet | EL-Brian | 17.0s |
| 02 | Nobody Says Turn It Up | Funny / running-joke, crew instinct | Party fleet | EL-Jessica | 16.5s |
| 03 | Whoever's Phone Is Playing Wins | Funny / running-joke | Party fleet | EL-Lily | 16.0s |
| 04 | Nobody Mentions the Merger | Funny / heartfelt, corporate | Party fleet | voice-en-GB-RyanNeural | 17.0s |
| 05 | Five More Minutes, Captain | Funny / running-joke, captain line | Party fleet | voice-en-US-BrianNeural | 16.0s |
| 06 | The Boat That Showed Up Bigger | Heartfelt / loyalty | Party fleet | voice-en-US-GuyNeural | 17.5s |
| 07 | The Sound Hollywood Uses for Eagle | Did-you-know / wildlife | Eco tour | voice-en-US-RogerNeural | 17.0s |
| 08 | A Few Dozen Eggs, Eighty Million Years of Practice | Heartfelt / wildlife spotlight | Eco tour | EL-Sarah | 18.0s |
| 09 | The Bird Shaped Like Scissors | Did-you-know / wildlife | Eco tour | EL-Eric | 17.0s |
| 10 | If You Can Sit Down, You Can Do This | Myth vs. reality | Eco tour | EL-Daniel | 16.5s |
| 11 | How Deep Do You Think This Is | Funny / running-joke, sensory | Eco tour | EL-EchoRae | 16.0s |
| 12 | As Close As They Let Us | Practical / guide line, FAQ | Eco tour | EL-George | 17.0s |

Total runtime if cut back-to-back: ~3 minutes 26 seconds across 12 standalone pieces (not a single video, each posts separately).

---

## Piece 01 — "Half the Boat Googles It by the Dock"
**Lane:** Heartfelt / funny, captain line · **Product:** Private BYOB party fleet
**Voice:** EL-Brian (ElevenLabs) · **Music:** warm, a little proud, storytelling energy (mood only) · **Target:** 17.0s

```
 0.0s  Every captain points out the same warehouse on the way out. Most just call it "the warehouse."   [wide shot: boat passing a riverside warehouse, captain gesturing]
 3.5s  This one doesn't. "See that? They filmed a chase scene there. My cousin got yelled at by the lead actor for standing in frame."   [close-up: captain mid-story, guests leaning in to listen]
 8.5s  Nobody asked for a movie-trivia lecture. Everybody stops talking anyway.   [medium shot: guests turning toward the captain, drinks paused mid-sip]
12.0s  He's got about five of these lined up for the whole route.   [close-up: captain, easy grin, already scanning ahead for the next landmark]
14.5s  By the time they dock, half the boat's already checking whether the story's true.   [closing wide shot: boat approaching the marina, guests still discussing, phones out]
```

**On-screen text:** none, the story and the reaction carry the beat.
**Shot list:** wide boat passing the warehouse → close-up captain mid-story → medium guests leaning in, drinks paused → close-up captain grinning, scanning ahead → closing wide boat approaching the marina, phones out.
**Copy passes:** channeling Halbert's plain, specific storytelling (a real cousin, a real reaction, no generic "cool local fact"). Copywriting-2.0 caught an early closer, "and it becomes part of the trip," as vague and unfalsifiable, rewrote to the checkable, funnier "half the boat's already checking whether the story's true."
**Production flag:** sourced from idea #19, confirmed untapped by direct grep of all 216 prior titles. No real movie, actor, or filming location named or implied as identifiable. Illustrative captain behavior (a rotation of local stories), not confirmed as current trained practice. No captain identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/01-half-the-boat-googles-it-by-the-dock-NOTES.txt`

---

## Piece 02 — "Nobody Says Turn It Up"
**Lane:** Funny / running-joke, crew instinct · **Product:** Private BYOB party fleet
**Voice:** EL-Jessica (ElevenLabs) · **Music:** building, groove-forward, energy climbing in small steps (mood only) · **Target:** 16.5s

```
 0.0s  Nobody on this boat ever says the word "louder."   [wide shot: boat cruising, group dancing, energy building]
 3.0s  A deckhand just watches feet. When enough of them start moving, the volume goes up one notch.   [close-up: deckhand's hand on the speaker dial, eyes on the dance floor]
 7.0s  No announcement. No "you guys want it louder?" Just more.   [medium shot: bass hits, more guests joining in]
10.5s  If the group wants chill, it stays chill. Nobody's reading a script, just a room.   [close-up: contrast beat, a calmer stretch of guests, deckhand leaving it be]
14.0s  By the third bump, half the boat's convinced the boat somehow knows what they want before they do.   [closing wide shot: full dance energy, group completely locked in]
```

**On-screen text:** none, the piece is built to be told entirely through action, no dialogue to caption.
**Shot list:** wide boat cruising, dancing beginning → close-up deckhand watching, hand on the dial → medium bass hit, more guests joining → close-up calmer contrast beat → closing wide full dance energy.
**Copy passes:** channeling Bencivenga's show-don't-tell patience, no line of dialogue anywhere in the piece. Copywriting-2.0 caught an early closer, "the boat just knows how to read a room," as an overused, unfalsifiable claim, rewrote to the more specific "half the boat's convinced the boat somehow knows what they want before they do."
**Production flag:** sourced from idea #23, confirmed untapped by direct grep. Illustrative crew instinct, not a confirmed trained behavior; wording/timing would vary crew to crew. No crew member identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/02-nobody-says-turn-it-up-NOTES.txt`

---

## Piece 03 — "Whoever's Phone Is Playing Wins"
**Lane:** Funny / running-joke · **Product:** Private BYOB party fleet
**Voice:** EL-Lily (ElevenLabs) · **Music:** playful, quick, comedic timing (mood only) · **Target:** 16.0s

```
 0.0s  The second the boat clears the dock, three phones try to pair to the same speaker at once.   [wide shot: boat pulling away, guests already reaching for phones]
 3.0s  Nobody announced a rule about it. There's just an unspoken one anyway: whoever connects first controls the party.   [close-up: phone screen searching for a connection, guests glancing at each other]
 7.0s  Somebody's song wins by accident. Somebody else pretends they weren't trying.   [close-up: guest reacting, mock-annoyed, laughing]
10.5s  By song three, nobody remembers whose playlist it even was.   [medium shot: whole group dancing, energy building]
13.5s  The DJ booth on this boat is just whoever moved fastest with their thumbs.   [closing wide shot: boat cruising, full party energy]
```

**On-screen text:** none.
**Shot list:** wide boat pulling away, phones out → close-up phone searching for a connection → close-up guest's mock-annoyed reaction → medium full group dancing → closing wide boat cruising, party in full swing.
**Copy passes:** channeling Sugarman's fast comedic rhythm. Copywriting-2.0 caught an early closer, "it's chaos but it works," as vague filler, rewrote to the concrete, ownable "the DJ booth on this boat is just whoever moved fastest with their thumbs."
**Production flag:** original concept, checked against the idea bank (no numbered match) and against all 216 prior titles (no collision on Bluetooth, pairing, or "DJ booth" framing). No guest identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/03-whoevers-phone-is-playing-wins-NOTES.txt`

---

## Piece 04 — "Nobody Mentions the Merger"
**Lane:** Funny / heartfelt, corporate · **Product:** Private BYOB party fleet
**Voice:** voice-en-GB-RyanNeural (free tier) · **Music:** light, dry, a little wry (mood only) · **Target:** 17.0s

```
 0.0s  Three days before a corporate booking, somebody calls the person who planned it.   [wide shot: office setting, generic, phone in hand]
 3.0s  "What's success look like for this one?" Not a script question. An actual one.   [close-up: person on the phone, listening, genuine]
 6.5s  She doesn't say team bonding. She says, "Nobody talks about the merger for two hours. That's it."   [close-up: organizer on the phone, half-laughing, half-serious]
11.0s  That's the whole brief. No icebreakers get planned. No games get forced.   [medium shot: boat later, group just talking, drinks in hand, nobody doing a trust fall]
14.5s  Two hours later, nobody's mentioned the merger once.   [closing wide shot: group laughing together on the boat, completely at ease]
```

**On-screen text:** none.
**Shot list:** wide generic office phone-call setup → close-up caller listening → close-up organizer's honest answer → medium group relaxed on the boat, no forced activities → closing wide group laughing, at ease.
**Copy passes:** channeling Ogilvy's specificity, the merger detail is what makes the ask feel real instead of generic. Copywriting-2.0 caught an early closer, "and everyone had a great time," as vague and unfalsifiable, rewrote to the direct callback "two hours later, nobody's mentioned the merger once."
**Production flag:** sourced from idea #56, confirmed untapped. No real company, merger, or corporate client named or identifiable. Illustrative pre-booking call, not confirmed as a standing practice for every corporate booking. No organizer identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/04-nobody-mentions-the-merger-NOTES.txt`

---

## Piece 05 — "Five More Minutes, Captain"
**Lane:** Funny / running-joke, captain line · **Product:** Private BYOB party fleet
**Voice:** voice-en-US-BrianNeural (free tier) · **Music:** light, warm, a little cheeky (mood only) · **Target:** 16.0s

```
 0.0s  With ten minutes left on every single cruise, somebody asks the same question a different way.   [wide shot: boat nearing the marina, guests glancing at the dock ahead]
 3.5s  "Can we just... not go back yet?"   [close-up: guest, half-joking, half-serious, looking at the captain]
 6.0s  The captain checks his watch. There's another group already waiting at the dock.   [close-up: captain glancing at his watch, then toward the marina]
 9.5s  He never says no outright. He just starts steering slower.   [medium shot: captain easing back on the throttle, boat's wake softening]
13.0s  Four minutes buys the whole boat one more song, and nobody argues with that math.   [closing wide shot: guests still dancing, boat gliding in slow, marina getting closer]
```

**On-screen text:** none.
**Shot list:** wide boat nearing the marina → close-up guest's half-joking ask → close-up captain checking his watch → medium captain easing off the throttle → closing wide guests dancing, boat gliding in slow.
**Copy passes:** channeling Halbert's honesty about real constraints (the schedule is named, not glossed over, per the global writing-style rule about mentioning real limits). Copywriting-2.0 caught an early closer, "and everyone's happy," as vague, rewrote to the concrete, falsifiable "four minutes buys the whole boat one more song."
**Devices check:** the repeated element here is the guest's question, asked a different way every time, not a fixed captain catchphrase; the captain's response is an action (slowing the boat), not a memorized line. Checked against the series' retired fixed-catchphrase-as-comedic-engine device and confirmed structurally distinct, the same distinction Pass 61 documented for its own Piece 03.
**Production flag:** original concept, checked against the idea bank (no numbered match) and all 216 prior titles (no collision). No captain identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/05-five-more-minutes-captain-NOTES.txt`

---

## Piece 06 — "The Boat That Showed Up Bigger"
**Lane:** Heartfelt / loyalty · **Product:** Private BYOB party fleet
**Voice:** voice-en-US-GuyNeural (free tier) · **Music:** warm, understated, a little proud (mood only) · **Target:** 17.5s

```
 0.0s  A guy books his third cruise with us, same as always, nothing special in the request.   [wide shot: marina, guest walking up alone, casual]
 3.5s  The booking goes out for the small boat. What shows up at the dock is the big one.   [close-up: guest looking at a larger boat than expected, slight double-take]
 7.0s  Nobody explains it. Nobody puts "loyalty upgrade" on a form anywhere.   [close-up: deckhand waving him aboard, no announcement, business as usual]
10.5s  He just gets more room, a better sound setup, and a captain who already recognizes him from the dock.   [medium shot: guest settling in on the bigger boat, easy going aboard]
14.5s  He'll mention it to his buddy on the ride out, and neither of them will know why it happened.   [closing wide shot: boat pulling out, guest relaxed, city receding behind him]
```

**On-screen text:** none.
**Shot list:** wide guest walking up alone → close-up guest's double-take at the bigger boat → close-up deckhand waving him aboard, no fuss → medium guest settling in → closing wide boat pulling out.
**Copy passes:** channeling Bencivenga's quiet-reveal patience, no big announcement anywhere in the piece. Copywriting-2.0 caught an early closer, "that's how you build a loyal customer," as telling rather than showing, rewrote to the puzzled-but-happy "neither of them will know why it happened."
**Production flag:** sourced from idea #65, confirmed untapped. Illustrative, not confirmed as a standing scheduling practice; would need real capacity/slow-period rules from ops before treated as routine. No guest or crew identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/06-the-boat-that-showed-up-bigger-NOTES.txt`

---

## Piece 07 — "The Sound Hollywood Uses for Eagle"
**Lane:** Did-you-know / wildlife spotlight · **Product:** Naturalist eco swamp tour
**Voice:** voice-en-US-RogerNeural (free tier) · **Music:** curious, a little wry, quick reveal (mood only) · **Target:** 17.0s

```
 0.0s  A sharp, piercing scream cuts across the water, and every guest looks up expecting a bald eagle.   [wide shot: kayaks pausing, guests scanning the treeline]
 3.5s  It's not an eagle. Real eagles mostly just chirp, kind of a letdown for how big they are.   [close-up: guide gesturing, slight smile]
 7.5s  That scream belongs to a red-shouldered hawk, about a third the size of what everyone pictured.   [close-up: hawk perched, guests spotting it, smaller than expected]
11.5s  It's the sound movies use whenever they want you to feel "eagle." Real eagles just don't deliver.   [medium shot: guide explaining, group amused]
15.0s  Every guest on this tour just got fooled by the same trick Hollywood's been running for decades.   [closing wide shot: hawk taking off, group watching, still processing]
```

**On-screen text:** "RED-SHOULDERED HAWK" small lower-third label at 7.5s, clears fast.
**Shot list:** wide kayaks scanning the treeline → close-up guide's line → close-up hawk perched, smaller than expected → medium guide explaining, group amused → closing wide hawk taking off.
**Copy passes:** channeling Ogilvy's factual reveal, paired with Sugarman's curiosity-gap structure (sound first, reveal second). Copywriting-2.0 caught an early closer, "nature's original sound effect," as a worn phrase, rewrote to the specific "same trick Hollywood's been running for decades."
**Production flag:** the "real eagle calls are weak, a hawk scream gets substituted in film and TV sound design" convention is a widely repeated birding/film-trivia claim, most commonly cited for red-tailed hawks specifically; confirm the exact species convention against a documented source before publishing this as stated fact, and confirm red-shouldered hawks are reliably sighted or heard on NPB's actual eco tour route. First hawk-species piece in the series (distinct from the vault's existing osprey and bald eagle pieces). No guide identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/07-the-sound-hollywood-uses-for-eagle-NOTES.txt`

---

## Piece 08 — "A Few Dozen Eggs, Eighty Million Years of Practice"
**Lane:** Heartfelt / wildlife spotlight · **Product:** Naturalist eco swamp tour
**Voice:** EL-Sarah (ElevenLabs) · **Music:** hushed, tender, a little in-awe (mood only) · **Target:** 18.0s

```
 0.0s  A mound of mud and reeds sits a few feet off the bank, taller than it looks like it should be.   [wide shot: kayaks approaching a mounded nest area from a respectful distance]
 3.5s  A guest asks if it's just a pile of debris. It's a nursery.   [close-up: guest squinting at the mound, curious]
 6.5s  A mother alligator builds it herself, and she doesn't wander far from it all summer.   [close-up: nest mound detail, guide gesturing]
10.5s  The guide keeps the kayaks well clear. This is the one spot on the whole route where distance isn't optional.   [medium shot: guide signaling the group to hold back, calm but clear]
14.5s  Inside, a few dozen eggs are doing something that's been working for eighty million years without any help from us.   [closing wide shot: nest mound from a distance, kayaks holding position, quiet]
```

**On-screen text:** "ALLIGATOR NEST" small lower-third label at 3.5s.
**Shot list:** wide kayaks approaching at a distance → close-up guest questioning the mound → close-up nest detail, guide gesturing → medium guide signaling the group to hold back → closing wide nest from a distance, kayaks holding position.
**Copy passes:** channeling Ogilvy's fact-driven specificity. Copywriting-2.0 caught an early closer, "nature knows what it's doing," as a platitude, rewrote to the concrete, checkable "a few dozen eggs... eighty million years" (crocodilian lineage, a defensible long-timescale claim) paired with the specific egg count.
**Devices check:** distinct from Pass 14's "Wait, Gators Can Do That" (mother carrying hatchlings in her mouth) and Pass 16's "Same Bayou, Never the Same Tour" (mother gator with babies on her back), both of which center post-hatching behavior. This piece centers the nest and eggs specifically, confirmed as the first piece in the series to do so.
**Production flag:** this requires a real, confirmed nest-sighting and safe-distance protocol from guides before treated as a routine tour moment rather than an occasional one; nesting season is roughly early summer, not year-round. No baiting, chasing, or cornering implied or shown. No guide identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/08-a-few-dozen-eggs-eighty-million-years-of-practice-NOTES.txt`

---

## Piece 09 — "The Bird Shaped Like Scissors"
**Lane:** Did-you-know / wildlife spotlight · **Product:** Naturalist eco swamp tour
**Voice:** EL-Eric (ElevenLabs) · **Music:** light, airborne, graceful (mood only) · **Target:** 17.0s

```
 0.0s  Something white and black glides overhead without a single wingbeat, tail split clean in two.   [wide shot: kite soaring high above the treeline, kayaks below]
 3.5s  A guest says it looks like someone cut the bird's tail with scissors. That's basically the whole design.   [close-up: kite's forked tail, twisting mid-flight]
 7.5s  The swallow-tailed kite uses that tail like a rudder, snatching dragonflies out of the air without ever landing.   [close-up: kite banking sharply, mid-air catch]
11.5s  It even drinks on the move, skimming the water's surface at full speed without slowing down.   [medium shot: kite dipping low over the water, brief skim]
15.0s  Most days it never touches a branch, a rail, or the ground at all.   [closing wide shot: kite continuing to soar, kayaks small beneath it]
```

**On-screen text:** "SWALLOW-TAILED KITE" small lower-third label at 7.5s.
**Shot list:** wide kite soaring overhead → close-up forked tail twisting mid-flight → close-up mid-air insect catch → medium kite skimming the water → closing wide kite continuing to soar.
**Copy passes:** channeling Ogilvy's precision, specific behaviors over generic praise. Copywriting-2.0 caught an early closer, "a truly graceful bird to watch," as a dead adjective stack, rewrote to the specific, falsifiable "never touches a branch, a rail, or the ground at all."
**Production flag:** swallow-tailed kites are migratory, present in Louisiana roughly March through August; confirm actual seasonal presence and sighting frequency on NPB's specific route before treating this as a guaranteed, year-round moment. First dedicated kite piece in the series (the vault's existing raptor pieces cover osprey and bald eagle, this pass adds hawk and kite, all four distinct species). No guest identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/09-the-bird-shaped-like-scissors-NOTES.txt`

---

## Piece 10 — "If You Can Sit Down, You Can Do This"
**Lane:** Myth vs. reality · **Product:** Naturalist eco swamp tour
**Voice:** EL-Daniel (ElevenLabs) · **Music:** calm, reassuring, steady confidence (mood only) · **Target:** 16.5s

```
 0.0s  A guest at the dock admits she's never been in a kayak in her life. She looks nervous about it.   [wide shot: guest at the dock, hesitant, eyeing the kayaks]
 3.0s  The guide doesn't downplay it. He just hands her a paddle and says, "If you can sit down, you can do this."   [close-up: guide handing over a paddle, calm and direct]
 7.0s  No rapids. No current fighting back. The whole route is flat, slow water.   [medium shot: kayaks gliding on calm, still water]
10.5s  Forty minutes in, she's steering better than the guy next to her who said he'd done this before.   [close-up: guest paddling confidently, small proud grin]
14.0s  Turns out the only requirement was showing up.   [closing wide shot: full group of kayaks moving easily together through the bayou]
```

**On-screen text:** none, the line and the visible outcome carry the correction without a caption spelling it out.
**Shot list:** wide guest hesitating at the dock → close-up guide handing over the paddle → medium kayaks gliding on calm water → close-up guest paddling confidently → closing wide full group moving easily together.
**Copy passes:** channeling Claude Hopkins and Halbert's direct objection-handling style. Copywriting-2.0 caught an early closer, "anyone can do this tour," as a generic marketing claim, rewrote to the specific, funnier, falsifiable comparison against the guy who claimed prior experience.
**Devices check:** structurally, this is the same guest-question-then-factual-correction shape as Pass 61's Piece 11 ("It's Not Coming for the Boat," the cottonmouth myth-vs-reality piece), which itself was checked against and confirmed distinct from the series' retired guest-expectations-wrong-then-corrected device (that retired device concerns a whole-tour expectation subversion arc, not a single factual objection answered on request). This piece follows the same confirmed-safe Lane 8 shape, second piece in the series to use it. Sourced from Script & Caption Bank Lane 8 directly ("You don't need to be athletic... if you can sit down, you can do this").
**Production flag:** illustrative guide response to a real, common pre-tour objection; not a scripted or trained line. No guest or guide identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/10-if-you-can-sit-down-you-can-do-this-NOTES.txt`

---

## Piece 11 — "How Deep Do You Think This Is"
**Lane:** Funny / running-joke, sensory · **Product:** Naturalist eco swamp tour
**Voice:** EL-EchoRae (ElevenLabs) · **Music:** playful, curious, quick reveal (mood only) · **Target:** 16.0s

```
 0.0s  The guide stops the group and asks everyone to guess the water depth right here.   [wide shot: kayaks paused over black, still water]
 3.0s  Guesses come back fast. Twenty feet. Bottomless. One guy says "the trench."   [close-up: guests calling out guesses, half-joking]
 6.5s  It's about four feet. The black water is doing all the work of looking deep.   [close-up: guide holding a paddle upright, marking the shallow depth]
10.0s  Every single tour, somebody's convinced they could touch bottom, and somebody else is convinced nobody ever will.   [medium shot: guests reacting, surprised, some laughing]
13.0s  Both of them are wrong, and both of them will guess again at the next bend.   [closing wide shot: kayaks moving on, still guessing among themselves]
```

**On-screen text:** none.
**Shot list:** wide kayaks paused over still black water → close-up guests calling out guesses → close-up guide marking the actual depth with a paddle → medium guests reacting, surprised → closing wide kayaks moving on, still guessing.
**Copy passes:** channeling Sugarman's slippery-slide curiosity build, guess-then-reveal structure. Copywriting-2.0 caught an early closer, "it's all part of the mystery," as vague and AI-flavored, rewrote to the concrete, funnier callback about both guessers being wrong and doing it again.
**Devices check:** a numeric depth-guessing game, not an animal-identification guessing game; checked against the series' existing "gator, turtle, or stick" misidentification device and confirmed structurally different (this piece never asks guests to identify a living thing, only to estimate a physical measurement).
**Production flag:** original concept, checked against the idea bank (no numbered match) and all 216 prior titles (no collision on depth-guessing framing). The four-foot figure is illustrative; confirm actual typical depth on NPB's specific route before publishing a number. No guest identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/11-how-deep-do-you-think-this-is-NOTES.txt`

---

## Piece 12 — "As Close As They Let Us"
**Lane:** Practical / guide line, FAQ · **Product:** Naturalist eco swamp tour
**Voice:** EL-George (ElevenLabs) · **Music:** calm, grounded, a little reverent (mood only) · **Target:** 17.0s

```
 0.0s  Somebody always asks, before the kayaks even launch, how close they'll actually get to a gator.   [wide shot: group at the dock, pre-launch, guide addressing them]
 3.5s  Every group asks a version of the same question, and the guide's answer never changes, because the policy doesn't.   [close-up: guide speaking plainly, group listening]
 7.5s  "As close as they let us. We don't chase them, we don't bait them, we don't corner them."   [close-up: guide's line, direct eye contact with the group]
11.5s  Some tours out here feed gators for a better photo. This one doesn't, on purpose.   [medium shot: kayaks paddling at a respectful distance from a sunning gator]
15.0s  Every gator on this route decides how close today gets. Nobody in a kayak does.   [closing wide shot: gator sliding off a bank into the water, unbothered, kayaks holding steady]
```

**On-screen text:** "AS CLOSE AS THEY LET US" pops as a quote card at 7.5s, clears fast.
**Shot list:** wide group at the dock, pre-launch → close-up guide's plain answer → close-up guide's direct line → medium kayaks at a respectful distance from a gator → closing wide gator sliding into the water, kayaks holding steady.
**Copy passes:** channeling Halbert's plain, unembellished honesty about a real policy. Copywriting-2.0 caught an early draft's closer, "and that's what makes this tour different," as vague self-praise, rewrote to the concrete "every gator on this route decides how close today gets. Nobody in a kayak does."
**Devices check:** this is a stated operational policy repeated because it stays factually true, not a guide's personal catchphrase used for comedic branding; reframed the setup line specifically ("the policy doesn't [change]," not "the guide always says this line") to keep the emphasis on the policy rather than a memorized bit, distinguishing it from the series' retired fixed-catchphrase-as-comedic-engine device. Same Lane 11 (practical/FAQ) territory as Script & Caption Bank's own listed FAQ, "How close do you get to gators? As close as they let them. We don't chase, bait, or corner them," sourced directly.
**Production flag:** states a real safety/ethics policy; confirm current wording with ops before using as an on-camera quote. No guide identified.
Full detail: `Narrated/2026-08-15 Party & Boat Sayings — Pass 70/12-as-close-as-they-let-us-NOTES.txt`

---

## What's still untapped for a future pass

- **Idea-bank items confirmed genuinely open after this pass's direct re-verification (not inherited from any prior pass's list):** #1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 20, 21 (toast-shaped, held on saturation grounds, not availability), 24, 25 (adjacent to Piece 02 but not consumed by it), 26, 27, 29, 30, 31, 32, 33, 34, 35 (Pass 61 claimed this for its own Piece 03; unverified this pass, re-check before use), 37, 38, 39, 41, 57, 58, 59, 60, 62, 63, 64, 66, 68, 69 (Pass 61 claimed this for its own Piece 04; unverified this pass, re-check before use), 71 (flagged by Pass 59 and 60 as conflicting with the crew-anonymity rule as written, since it prints a real name on a tag; still unresolved), 72, 74, 75, 76, 77, 79, 80, 82, 83, and the full seasonal/event bank (#84-100, largely untouched by this series). **Do not treat this list as trustworthy without re-grepping** the same way this pass caught Pass 61's three errors; several numbers on prior passes' "open" lists were not actually open.
- **Script & Caption Bank material still open:** Lane 2 (funny/irreverent viral captions) and Lane 13 (sound-on/no-narration) remain flagged as format-incompatible with this series' timed-narration structure by every pass since 27. Lane 8 (myth vs. reality) now has two entries (Pass 61's cottonmouth piece, this pass's fitness/no-experience piece); worth a third in a future pass, e.g. correcting the "airboats are more exciting" myth from a fresh angle, or a first-timer bug-spray/heat objection.
- **This pass's own remaining gaps:** toasts and bachelorette-dedicated pieces held at zero for the seventh and sixth consecutive pass respectively. Birthday-specific pieces held at zero this pass too, a new finding: idea-bank #52-55 are functionally consumed or toast-shaped (documented above), leaving little genuinely fresh ground without reskinning an existing piece; a future pass could still mine an original, non-idea-bank birthday angle if one surfaces. Eco-tour species now covered across the full series: anhinga, prothonotary warbler, roseate spoonbill, green heron, barred owl, osprey, white ibis, wood duck, bald eagle, cottonmouth, red-shouldered hawk, alligator (adult, hatchling-carrying, and now nest/eggs), swallow-tailed kite. Still open: a first-timer's overall physical-comfort myth beyond fitness (heat, bugs, sunscreen already lightly touched elsewhere), a screech or barn owl distinct from the barred owl pieces, nutria beyond the existing misidentification bit, a dedicated turtle-basking spotlight. Corporate content is now two pieces total across the series (Pass 37's "Your Team Showed Up for You" and this pass's Piece 04) and could support a dedicated corporate-focused pass.
- **Music-artist research:** still not re-researched this pass; mood-only direction used throughout, per Pass 59, 60, and 61's precedent.
- **Bookkeeping note for whoever runs Pass 71+:** this pass's dedup found three concrete errors in Pass 61's own "still untapped" section (idea #22, idea #54/#53, and the anhinga claim), all documented above with the specific prior pieces that actually consumed them. This is not a criticism of Pass 61's process, it did real, careful work, it's a reminder that inherited summaries drift and compound across passes. **Re-verify every citation in this pass's own "still untapped" list above by grepping the actual NOTES file contents before trusting it in Pass 71**, the same way this pass caught Pass 61's errors instead of repeating them. The Pass 41 folder on disk remains empty; no content exists there to diff against.

---

## Status

**STAGED DRAFT — pending David's approval.** No audio generated, no video rendered (this machine has no ffmpeg and no ElevenLabs key). Pass 70, built 2026-08-15. All 60 spoken lines routed through `/copy-mentors` then `/copywriting-2.0`; the structural-distinction checks on Piece 05 and Piece 12 (both vs. the retired fixed-catchphrase device) and Piece 10 (vs. the retired guest-expectations-wrong-then-corrected device, following Pass 61's own precedent for the same Lane 8 shape) are logged inline above and in each piece's own NOTES file. Three specific errors in Pass 61's inherited "still untapped" tracking were found and corrected this pass (idea #22, idea #53/#54, and the anhinga claim), documented above with sourcing. Nothing here has been posted, scheduled, or handed to crew as a shot order.
