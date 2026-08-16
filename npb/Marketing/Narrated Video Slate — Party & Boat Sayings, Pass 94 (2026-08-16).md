# Narrated Video Slate — Party & Boat Sayings — Pass 94
*STAGED DRAFT, pending David's approval. Built 2026-08-16. Nothing in this document has been posted, scheduled, recorded, or handed to crew as a shot order.*

---

## Status flags (read first)

- **Nothing here has been recorded, rendered, or posted.** This machine has no ffmpeg and no ElevenLabs API key, so no audio was generated and no video was assembled. Every piece below is a script and shot plan only, ready for whoever runs the actual TTS/render step.
- **On disk going into this pass:** 25 prior slate documents in `Marketing/` (the base pass plus Pass 14 through Pass 93), and 300 prior `NOTES.txt` files under `Marketing/Narrated/`, one per piece, across those same 25 passes. Two folders exist with no content and were not treated as real prior passes: `Marketing/Narrated/2026-08-15 Party & Boat Sayings — Pass 41` (empty, 0 files) and `Marketing/Narrated/2026-08-16 Party & Boat Sayings — Pass 77` (empty, 0 files, previously flagged the same way by Pass 93).
- **Dedup method this pass:** a full-corpus read, not a sample. Six parallel research agents were run in the background, each assigned a slice of the 25 prior passes, and each read every slate `.md` and every one of its `NOTES.txt` files in full, cross-checking the two against each other for discrepancies (none found — every pass's `NOTES.txt` files matched its summary document word for word). Combined with a direct full read of Pass 92 and Pass 93 (the two most recent prior passes) and a complete filename audit of all 300 `NOTES.txt` files, this pass has verified exact spoken hook/closer text for every one of the 300 prior pieces, not just titles. That is a deeper dedup pass than several prior passes could do (some relied on filename audits alone). The full compiled catalog is preserved in this session's background-agent transcripts.
- **Toast, bachelorette, and birthday content — corrected count:** Pass 93 estimated toast at "roughly 18 structural angles" and birthday at "exactly two pieces in 264 prior pieces." This pass's full-text audit found both estimates were undercounts: toast-spine pieces actually number in the low twenties across the series (anaphora toast lists, captain toasts, quiet toasts, absent-friends toasts, corporate toasts, bottle-cheers, divorce-party toasts, milestone toasts, bachelorette-redirect toasts, and more), and birthday-flavored pieces number at least seven, not two (including "It's Your Boat Today," Pass 59, and "She Didn't Know Until She Saw Her Name," Pass 60, both missed by Pass 93's own count). This pass does not attempt a fourth toast device or a new plain birthday-toast device given that saturation. Instead: birthday content in this pass is delivered through a genuinely different mechanic (a private, non-toast, non-song wish-making moment, Piece 11), and bachelorette content is delivered through a mechanic no prior piece has used (a co-maid-of-honor headcount mixup, Piece 06, distinct from all seven prior bachelorette angles: bell curve, poker-chip bet, MOH phone call, bride-goes-last, survival kit, last-sail-before-the-veil, and the toast-redirect device).
- **A real duplicate was found already living in the existing corpus, not created by this pass:** Pass 60 Piece 07 ("The Pink Bird Nobody Believes Is Real") and Pass 93 Piece 08 ("Roseate Spoonbill") are the same species with different framing devices. This pass does not add a third spoonbill piece, and flags this for whoever next builds the "still open wildlife" tracking list, since Pass 93's own list didn't catch the Pass 60 overlap.
- **Idiom bank used this pass, each confirmed unused by full-text audit against all 300 prior pieces:** "take the helm" (Piece 01), "clear the decks" (Piece 02), "shipshape" (Piece 03), "landlubber" (Piece 04). All four were named as still-open in Pass 75's own tracking list and confirmed independently unused by this pass's audit. Remaining confirmed-open idioms for a future pass: above board, flotsam and jetsam, cut and run, hold fast, at loose ends, shot across the bow, pipe down, keel over, swab the deck, jump ship, close quarters (shiver me timbers and walk the plank remain deliberately set aside as too costume-pirate for the brand, per Pass 92's original note).
- **Eco-tour wildlife subjects, each confirmed unused across all 300 prior pieces:** yellow-crowned night-heron (Piece 07) and king rail (Piece 08). Both were named as open in Pass 75's tracking. This pass does not add a fifth heron-family piece beyond what already exists (wood stork, snowy egret, great blue heron, tricolored heron are already on file) without a clearly distinct mechanic — Piece 07 uses a "night shift" framing (the only nocturnal-specialist bird piece in the series) rather than another visual-ID or guide-correction structure, and Piece 08 is the first piece in the series built entirely around a bird that is heard, never seen.
- **Non-species, non-idiom devices confirmed unused by full-text audit:** the multilingual toast round (Piece 05), the co-maid-of-honor mixup (Piece 06), the guide's stock deflection on "have you ever fallen in" (Piece 09), the guest-reaction-variance montage at the first gator sighting (Piece 10), the private wish-before-the-sighting birthday device (Piece 11), and the guide's private dockside logbook ritual (Piece 12).
- **Every spoken line in every piece was routed through `/copy-mentors` then `/copywriting-2.0`, both invoked directly this pass, not simulated.** `/copy-mentors` was invoked first and loaded with this pass's specific context (12 short-form scripts, party/boat sayings, toasts, captain lines, bachelorette/birthday-group lines, running jokes, split across the two on-water products) and returned the full five-master framework and routing table used to draft every line below. `/copywriting-2.0` was invoked second and returned the 3-test filter (visualize / falsify / nobody-else-could-say-it), the kill list, and Blair Warren's 27 words, all applied to every line. Specific catches and rewrites are logged in each piece's own Copy Passes note below and in each piece's `NOTES.txt` file. The most consequential catch: Piece 09's original closer stated an invented, oddly precise operational figure ("fourteen tours a week for six years") as if it were a real confirmed schedule; `/copywriting-2.0` flagged this as a falsify-test failure (an invented specific stated as fact reads worse than an honest round number) and it was rewritten to "Hundreds of tours. Still one story he's keeping," which keeps the scale claim without asserting fabricated operational data. Piece 12's original closer used the word "souvenir," which echoes Pass 15 Piece 10 ("The Only Souvenir That Fits in a Pocket") closely enough in theme that `/copy-mentors` flagged it during drafting and it was rewritten to avoid the word and the echo entirely, even though the two pieces' mechanics are otherwise distinct (a guest takeaway vs. a guide's private ritual).
- **Voice rotation:** all 12 available samples used exactly once, solved as a constraint-satisfaction problem against the four most recent passes with a full 12-slot voice table on file (Pass 73, 75, 92, 93), so that no position below repeats any voice those four tables used in the same position. Worked solution in Sourcing below.
- **Music bed references:** continuing the mood-only convention every pass since Pass 59 has used. Pass 40 already flagged the real-artist music-bed reserve as exhausted; no fresh real-artist research was performed this session, consistent with that finding.
- **Production flags carried on several pieces** (claims that need verification before this is treated as a shot order rather than a concept pitch): Piece 07's yellow-crowned night-heron and Piece 08's king rail are real, documented Louisiana wetland species, but neither is confirmed by this pass as a regular sighting on NPB's specific eco-tour route — confirm with a guide before treating either as anything more than occasional. Piece 01's supervised wheel-touch moment, Piece 09's guide backstory, Piece 11's wish-timing device, and Piece 12's logbook ritual are all illustrative bits a captain or guide could plausibly do, not confirmed existing company traditions.
- **Everything below is a draft.** Nothing gets posted, scheduled, or handed to crew as a shot order until David signs off.

## What this is

12 new narrated short-form pieces (15.5–17.5 seconds each) built around party sayings, boat sayings, toasts, captain lines, bachelorette and birthday-group lines, and the things people actually say out loud on the water, split across NPB's two on-water products, per the brief. Format is modeled exactly on the Admire NOLA narrated series (`Admire NOLA/Content/Narrated/01-poetic-NOTES.txt` and `Admire NOLA/Content/Script & Caption Bank.md`): timestamped VO lines with a bracketed visual on every line, a named voice sample, a music bed, on-screen text treatment, and a shot list.

Split across NPB's two on-water products, consistent with the series' established 6/6 convention (the vault's third product, the social per-seat boat, has never been part of this slate series and isn't introduced here either, per `Brand Story & Values.md` Section 1's instruction not to blur the three products):
- **Private BYOB party fleet** — pieces 01-06: four new idiom-driven captain/deckhand lines, one new toast device, one new bachelorette device
- **Naturalist eco swamp tour** — pieces 07-12: two new wildlife subjects, one new FAQ-style running joke, one new guest-reaction device, one new birthday-group device, one new closing ritual

## Sourcing (so nothing here is invented from scratch)

- **Format/structure:** `Admire NOLA/Content/Narrated/01-poetic-NOTES.txt`, `Admire NOLA/Content/Script & Caption Bank.md`, both read in full this pass.
- **Dedup verification:** six parallel background research agents, each reading a slice of the 25 prior passes' slate documents and `NOTES.txt` files in full, plus a direct full read of Pass 92 and Pass 93, plus a complete filename audit of all 300 prior `NOTES.txt` files. See Status flags above for what this method caught that prior passes' methods missed (the Pass 60/Pass 93 spoonbill overlap, the undercounted toast/birthday totals).
- **Idiom bank:** see status flag above. Four idioms used this pass, all confirmed unused: take the helm, clear the decks, shipshape, landlubber.
- **Wildlife/nature topics, verified as open ground by the full-text audit:** yellow-crowned night-heron (Piece 07), king rail (Piece 08).
- **Brand voice, product split, confirmed facts:** `Brand Story & Values.md`, re-read in full this pass. Section 4's voice rules (guests not customers, contractions, no cruise-ship-ad language, sell the outcome not the specs) governed every line. Section 1's instruction to keep the three products distinct is why this pass holds to the private-fleet/eco-tour 6-6 split and does not introduce the social per-seat boat.
- **Crew roster (kept unnamed on purpose, consistent with Pass 23 onward):** `Crew Roster — Captains & Deckhands.md` was checked; no captain, guide, or deckhand is named on screen anywhere in this pass. All crew are referred to generically (captain, deckhand, guide), consistent with Pass 92 and Pass 93's convention.
- **Prior slates (diffed against all 25 on-disk documents and all 300 `NOTES.txt` files via the methods described above):** the base pass, 14 through 93.
- **Copy process:** every spoken line in all 12 pieces was drafted, then actually routed through the `/copy-mentors` skill and then the `/copywriting-2.0` skill this session. Specific rewrites are logged in every piece's own Copy Passes note below and in each piece's `NOTES.txt` file.
- **Consent and safety standard applied throughout:** no crew named, no guest identified without a filming ask. No wildlife baited, chased, cornered, or handled anywhere in this pass. Piece 08's king rail is deliberately never shown on camera (the whole device is that it's heard, not seen), which sidesteps any staging risk entirely.

**Voice samples:** `Admire NOLA/Content/Voice Samples/` — all 12 available samples used once each. This machine cannot generate audio from any of them (no ElevenLabs key, no ffmpeg). Names below are casting picks for whoever runs TTS.

| Position | Voice | Position | Voice |
|---|---|---|---|
| 01 | EL-George | 07 | EL-Brian |
| 02 | EL-EchoRae | 08 | voice-en-US-GuyNeural |
| 03 | EL-Lily | 09 | voice-en-US-RogerNeural |
| 04 | EL-Jessica | 10 | voice-en-GB-RyanNeural |
| 05 | EL-Sarah | 11 | EL-Eric |
| 06 | EL-Daniel | 12 | voice-en-US-BrianNeural |

This table was solved as a constraint-satisfaction problem against the four most recent prior tables with a full 12-slot table on file — Pass 73, 75, 92, and 93 — so that no position below repeats any voice those four tables used in that same position:
- Pass 73: 01 EL-Daniel, 02 EL-George, 03 EL-Jessica, 04 EL-Eric, 05 EL-Brian, 06 EL-EchoRae, 07 EL-Lily, 08 BrianNeural, 09 RyanNeural, 10 GuyNeural, 11 RogerNeural, 12 EL-Sarah
- Pass 75: 01 EL-EchoRae, 02 EL-Daniel, 03 EL-Brian, 04 EL-Lily, 05 EL-Eric, 06 EL-Jessica, 07 EL-George, 08 RogerNeural, 09 EL-Sarah, 10 BrianNeural, 11 RyanNeural, 12 GuyNeural
- Pass 92: 01 EL-Lily, 02 EL-Sarah, 03 EL-Daniel, 04 EL-George, 05 EL-EchoRae, 06 EL-Brian, 07 EL-Eric, 08 EL-Jessica, 09 GuyNeural, 10 RogerNeural, 11 BrianNeural, 12 RyanNeural
- Pass 93: 01 EL-Jessica, 02 EL-Lily, 03 EL-George, 04 EL-Brian, 05 EL-Daniel, 06 EL-Eric, 07 EL-Sarah, 08 RyanNeural, 09 BrianNeural, 10 EL-EchoRae, 11 GuyNeural, 12 RogerNeural
- Pass 94 (this pass), solved position-by-position against all four above and matching none: table shown above. (Positions 8, 9, 10, and 12 each had exactly one Neural voice not used in that position by any of the four prior tables — GuyNeural, RogerNeural, RyanNeural, and BrianNeural respectively — which forced all four Neural voices into those slots and, as a consequence, forced position 11 to take the one remaining EL voice, EL-Eric.)

- **Music bed options:** no dedicated Local Sound Bank doc exists in this vault (checked again this pass). Continuing the mood-only convention rather than minting unverified real-artist names.

## Guardrails honored

- No sibling-brand mentions (NKST, Houston Pedal Barge, etc.) anywhere in this slate.
- No pedaling references (not applicable to this fleet).
- No invented price figures. No claim presented as existing, confirmed company tradition unless it already appears in a vault doc or prior pass. Every piece is flagged below and in its `NOTES.txt` file where it proposes something not yet confirmed.
- No guest named or closely identified on camera without the standard filming ask.
- Brand voice rules followed throughout: guests not customers, contractions, no "curated experience," no cruise-ship-ad language. Humor stays affectionate, never mocking any real guest, crew member, or group type.
- No em dashes in spoken lines or body copy, no "utilize," no "unparalleled," no "book now before it's too late," consistent with brand and global writing style rules.
- No real hotel, concierge desk, rideshare brand, or corporate client named anywhere in this slate. No real competitor named or identifiable anywhere. No real public figure named.
- David's name does not appear anywhere in this slate or in any on-screen credit.

---

## The slate at a glance

| # | Title | Lane | Product | Voice | Target |
|---|---|---|---|---|---|
| 01 | Take the Helm | Idiom, birthday-group captain line | Party fleet | EL-George | 16.0s |
| 02 | Clear the Decks | Idiom, running joke | Party fleet | EL-EchoRae | 16.5s |
| 03 | Shipshape | Idiom, before/after joke | Party fleet | EL-Lily | 16.0s |
| 04 | Landlubber | Idiom, affectionate running joke | Party fleet | EL-Jessica | 17.5s |
| 05 | Twelve Ways to Say Cheers | Toast, multilingual device | Party fleet | EL-Sarah | 17.0s |
| 06 | Every Boat's Got Two Maids of Honor | Bachelorette, running joke | Party fleet | EL-Daniel | 15.5s |
| 07 | Yellow-Crowned Night-Heron | Wildlife spotlight, nocturnal framing | Eco tour | EL-Brian | 17.5s |
| 08 | King Rail | Wildlife spotlight, heard-not-seen | Eco tour | voice-en-US-GuyNeural | 16.0s |
| 09 | Have You Ever Fallen In? | FAQ, running joke | Eco tour | voice-en-US-RogerNeural | 15.5s |
| 10 | Everybody's First Word | Guest-reaction montage | Eco tour | voice-en-GB-RyanNeural | 15.5s |
| 11 | Make a Wish Before the First Gator | Birthday-group line, eco tour | Eco tour | EL-Eric | 17.0s |
| 12 | The Logbook Nobody Reads But Him | Closing ritual, poetic | Eco tour | voice-en-US-BrianNeural | 17.5s |

Total runtime if cut back-to-back: ~3 minutes 42 seconds across 12 standalone pieces (not a single video, each posts separately).

---

## Piece 01 — "Take the Helm"
**Lane:** Idiom, birthday-group captain line · **Product:** Private BYOB party fleet
**Voice:** EL-George (ElevenLabs) · **Music:** warm, a little ceremonial, mood only · **Target:** 16.0s

```
 0.0s  "Helm" used to mean the actual wheel. The thing that turns the whole boat.   [close-up: captain's hand resting on the wheel]
 3.0s  Nobody just walks up and takes it.   [medium shot: guest reaching toward the wheel, captain shifting slightly]
 5.5s  Except today. Birthday girl gets thirty seconds, captain's hand still on it the whole time.   [medium shot: captain guiding guest's hand onto the wheel, both hands visible]
10.0s  She's not steering. She's just finally allowed to hold it.   [close-up: guest's face, delighted, hand on the wheel]
13.0s  Thirty seconds. Then the captain takes his boat back.   [wide shot: captain retaking the wheel, guest laughing, stepping back]
```

**ON-SCREEN TEXT TREATMENT:** Quote card, "TAKE THE HELM," pops in at 13.0s under the closing line, clears with the shot.

**SHOT LIST:**
- Close-up: captain's hand on the wheel (opener)
- Medium shot: guest reaching toward the wheel
- Medium shot: captain guiding the guest's hand onto the wheel
- Close-up: guest's delighted expression
- Closing wide shot: captain retaking the wheel, guest stepping back laughing

**SOURCE GROUNDING:** Built around the idiom "take the helm," confirmed unused across all 300 prior pieces by this pass's full-text audit. Distinct from Pass 24 Piece 04 ("Everybody Wants Five Minutes at the Wheel"), which is a running joke about guests asking for a photo op at the wheel with no captain involvement described; this piece is framed as an idiom explainer with a supervised, captain-guided birthday moment, not a photo request.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Bencivenga for the etymology claim (a checkable, specific fact rather than a vague nautical vibe) and Sugarman for the short opening sentence. `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "She's not steering. She's just finally allowed to hold it," which is concrete, visualizable, and doesn't overclaim that a guest is actually piloting the boat.

**DEVICES CHECK:** First "take the helm" piece in the series. See Source Grounding for the explicit distinction from the existing wheel-photo piece.

**PRODUCTION FLAG:** Illustrative captain bit, not a confirmed existing company tradition or safety-approved practice. Any real guest hand-on-wheel moment would need captain judgment and control retained at all times, exactly as scripted here. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered (this machine has no ffmpeg and no ElevenLabs key). Pass 94, 2026-08-16.

---

## Piece 02 — "Clear the Decks"
**Lane:** Idiom, running joke · **Product:** Private BYOB party fleet
**Voice:** EL-EchoRae (ElevenLabs) · **Music:** upbeat build, mood only · **Target:** 16.5s

```
 0.0s  Old navy term: "clear the decks" meant get ready, something's about to happen.   [close-up: cooler being slid to the side]
 3.5s  On this boat, it means the exact same thing.   [medium shot: deckhand moving a cooler and folding a chair out of the way]
 7.0s  Chairs stacked, cooler pushed back, three feet of open deck.   [wide shot: cleared space in the middle of the boat]
10.5s  That's not cleanup. That's the dance floor getting built.   [medium shot: first guest stepping into the cleared space]
13.5s  Clear the decks. Something's about to happen.   [wide shot: whole group moving into the cleared space, energy shifting]
```

**ON-SCREEN TEXT TREATMENT:** No text until 13.5s, small lower-third: "CLEAR THE DECKS." Clears with the shot.

**SHOT LIST:**
- Close-up: cooler being moved aside (opener)
- Medium shot: deckhand clearing a chair
- Wide shot: cleared deck space
- Medium shot: first guest stepping in
- Closing wide shot: whole group moving into the space

**SOURCE GROUNDING:** Built around the idiom "clear the decks," confirmed unused across all 300 prior pieces. Distinct from Pass 40 Piece 05 ("The Moment the Boat Remembers It's a Party"), which is about an energy shift with no idiom framing and no physical clearing action described; this piece is specifically an idiom-explainer built around the literal act of moving the cooler and chairs.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Sugarman for the slippery-slide build (short lines escalating to the payoff). `/copywriting-2.0` confirmed all five lines pass the 3-test filter with no further changes. The line to keep is "That's not cleanup. That's the dance floor getting built," the sharpest reframe in the piece.

**DEVICES CHECK:** First "clear the decks" piece in the series. See Source Grounding for the explicit distinction from the existing energy-shift piece.

**PRODUCTION FLAG:** Illustrative crew action, not a scripted or company-mandated ritual. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 03 — "Shipshape"
**Lane:** Idiom, before/after joke · **Product:** Private BYOB party fleet
**Voice:** EL-Lily (ElevenLabs) · **Music:** quick, tidy, a little comedic, mood only · **Target:** 16.0s

```
 0.0s  "Shipshape" meant every rope coiled, every line stowed, nothing loose on deck.   [close-up: rope being coiled neatly on a cleat]
 3.5s  This boat gets ninety seconds of that. Right before the next group walks up.   [wide shot: deckhand quickly wiping down seats, straightening cushions]
 7.0s  Empty cans gone. Cushions squared. Somebody's forgotten flip-flop, gone too.   [close-up: deckhand tossing a stray flip-flop into a bin]
11.0s  Ninety seconds, and it looks like nobody was ever here.   [wide shot: boat looking clean and ready, empty]
13.5s  Shipshape. Then the next twelve people show up and start over.   [wide shot: new group walking down the dock toward the boat]
```

**ON-SCREEN TEXT TREATMENT:** Quote card, "SHIPSHAPE," at 13.5s under the closing line, clears with the shot.

**SHOT LIST:**
- Close-up: rope being coiled (opener)
- Wide shot: deckhand wiping down seats
- Close-up: stray flip-flop tossed into a bin
- Wide shot: boat clean and ready
- Closing wide shot: next group approaching the dock

**SOURCE GROUNDING:** Built around the idiom "shipshape," confirmed unused across all 300 prior pieces. Distinct from Pass 24 Piece 03 ("The Cooler Audit"), which is about checking cooler stock levels specifically, not general deck turnaround.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Ogilvy for the specific, checkable detail (ninety seconds, not "quickly"). `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "Ninety seconds, and it looks like nobody was ever here," concrete and falsifiable in spirit even though the exact figure is illustrative.

**DEVICES CHECK:** First "shipshape" piece in the series. See Source Grounding for the distinction from the cooler-audit piece.

**PRODUCTION FLAG:** The ninety-second turnaround figure is illustrative, not a confirmed timed operational standard. Confirm actual turnaround time with ops before treating it as a stated fact rather than a rounded description. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 04 — "Landlubber"
**Lane:** Idiom, affectionate running joke · **Product:** Private BYOB party fleet
**Voice:** EL-Jessica (ElevenLabs) · **Music:** warm, a little playful, mood only · **Target:** 17.5s

```
 0.0s  "Landlubber" used to be an insult. Somebody clumsy on a boat, better off on land.   [medium shot: guest wobbling slightly stepping aboard, deckhand steadying them]
 4.0s  One guest grabs the rail with both hands before the boat's even moved.   [close-up: guest's white-knuckle grip on the rail]
 7.5s  "You're fine. You're a landlubber. Everybody starts there."   [medium shot: deckhand, warm, reassuring, guiding the guest to a seat]
11.5s  An hour later, same guest is standing up, drink in hand, not holding onto anything.   [wide shot: same guest now relaxed, dancing, hands free]
15.0s  Landlubber's a starting point. Not a life sentence.   [wide shot: whole group, that guest now fully part of the fun]
```

**ON-SCREEN TEXT TREATMENT:** No text until 15.0s, small lower-third: "LANDLUBBER'S A STARTING POINT." Clears with the shot.

**SHOT LIST:**
- Medium shot: guest wobbling while boarding (opener)
- Close-up: white-knuckle grip on the rail
- Medium shot: deckhand's reassurance
- Wide shot: guest relaxed and dancing an hour later
- Closing wide shot: whole group, guest fully at ease

**SOURCE GROUNDING:** Built around the idiom "landlubber," confirmed unused across all 300 prior pieces. Distinct from Pass 16 Piece 11 ("The Guest Who Almost Didn't Come," eco tour) and Pass 15 Piece 05 ("Wait, It's Just Us?," party fleet), neither of which is about physical nervousness on the boat itself or built around this idiom.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Halbert for the reassuring, conversational deckhand line (this hits the "allay their fears" lever from Blair Warren's 27 words: a nervous first-time guest gets told, plainly, that everyone starts there). `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "Landlubber's a starting point. Not a life sentence," the strongest, most ownable closer in the piece.

**DEVICES CHECK:** First "landlubber" piece in the series.

**PRODUCTION FLAG:** Illustrative guest behavior, not a specific real guest. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 05 — "Twelve Ways to Say Cheers"
**Lane:** Toast, multilingual device · **Product:** Private BYOB party fleet
**Voice:** EL-Sarah (ElevenLabs) · **Music:** warm strings building into a full group cheer, mood only · **Target:** 17.0s

```
 0.0s  One toast, going around the boat, and nobody says "cheers" the same way twice.   [wide shot: group forming a loose circle, drinks raised]
 3.5s  "Salud." "Prost." "Kanpai." Whatever your family says, that's the one you use.   [medium shot: three different guests each saying their own word, cups touching]
 8.0s  Nobody planned this. It just happens when there's more than one hometown on the boat.   [medium shot: guests laughing at the mix of languages]
12.0s  Twelve people, one drink, six different words for the exact same thing.   [wide shot: whole group finishing the toast together]
15.0s  Same toast. Everybody just says it like home.   [close-up: two guests clinking cups, smiling]
```

**ON-SCREEN TEXT TREATMENT:** As each toast word is spoken (3.5s), it pops on screen in a different simple font weight per word, "SALUD," "PROST," "KANPAI," clearing quickly in sequence so it doesn't clutter the frame.

**SHOT LIST:**
- Wide shot: group forming a toast circle (opener)
- Medium shot: three guests, three different words, cups touching
- Medium shot: group laughing at the mix
- Wide shot: whole group finishing the toast
- Closing close-up: two guests clinking cups

**SOURCE GROUNDING:** New toast device, confirmed unused across all 300 prior pieces by this pass's full-text audit. Every prior toast piece on file (roughly two dozen, see Status flags above) is built around a single spoken English toast line, whether from a captain, deckhand, or guest. This is the first multilingual toast-round device in the series. Deliberately avoids "laissez les bons temps rouler," which is already its own dedicated piece (Pass 17, Piece 01), and avoids "who dat," already its own dedicated piece (Pass 26, Piece 07).

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Ogilvy for the factual specificity (real, checkable words in real languages, not invented ones) and Sugarman for the short opening sentence. Original opening draft read "Toasts go all the way around this boat, and it's never the same word twice," which `/copywriting-2.0` flagged as a longer, less concrete first sentence than Sugarman's rule calls for; rewritten to "One toast, going around the boat, and nobody says 'cheers' the same way twice," which slides into the second line faster. The line to keep is "Twelve people, one drink, six different words for the exact same thing," the most ownable line in the piece because it's the one no single-language toast piece elsewhere in the series could say.

**DEVICES CHECK:** First multilingual toast piece in the series, structurally distinct from all prior toast-spine pieces (see Source Grounding). Given how saturated the toast lane already is (see Status flags), this pass adds exactly one new toast piece, not more.

**PRODUCTION FLAG:** Illustrative toast scenario dependent on an actual mixed-hometown group; not every group will produce this naturally. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 06 — "Every Boat's Got Two Maids of Honor"
**Lane:** Bachelorette, running joke · **Product:** Private BYOB party fleet
**Voice:** EL-Daniel (ElevenLabs) · **Music:** light comedic bounce, mood only · **Target:** 15.5s

```
 0.0s  "Who's the maid of honor?" the deckhand asks, mic in hand.   [medium shot: deckhand holding a small speaker, scanning the group]
 3.0s  Three hands go up.   [wide shot: three different guests raising their hands, looking at each other, confused]
 5.5s  Nobody warned him there'd be two co-maids of honor and one very confident cousin.   [medium shot: deckhand, amused, lowering the mic slightly]
 9.5s  "Alright. All three of you. Up here."   [medium shot: all three guests stepping forward together, laughing]
12.5s  Every boat's got a maid of honor. This one's got three.   [wide shot: all three giving the toast together, whole group cheering]
```

**ON-SCREEN TEXT TREATMENT:** Quote card, "THREE MAIDS OF HONOR," pops in at 12.5s under the closing line, clears with the shot.

**SHOT LIST:**
- Medium shot: deckhand asking the question (opener)
- Wide shot: three hands going up
- Medium shot: deckhand's amused reaction
- Medium shot: all three guests stepping forward
- Closing wide shot: all three giving the toast, group cheering

**SOURCE GROUNDING:** New bachelorette device, confirmed unused across all 300 prior pieces by this pass's full-text audit. Every existing bachelorette piece on file (the bell curve, the poker-chip bet, the maid-of-honor phone call, bride-goes-last, the survival kit, the walk-on song, the toast-redirect device) is built around a single, clearly designated maid of honor or the bride herself. This is the first built around a headcount mixup over who actually holds that role.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Sugarman for the narrative setup-twist-payoff structure. `/copywriting-2.0` confirmed all five lines pass the 3-test filter with one adjustment: the original closer, "Every boat's got two maids of honor. This one's got three," repeated the piece's title verbatim as a flat restatement, which failed the burrito test (it added nothing pulling forward); tightened to "Every boat's got a maid of honor. This one's got three," a smaller change that keeps the punchline's math instead of just repeating the headline. The line to keep is "Nobody warned him there'd be two co-maids of honor and one very confident cousin," the most specific and visualizable line in the piece.

**DEVICES CHECK:** First "co-maid-of-honor mixup" device in the series. See Source Grounding for the explicit distinction from all seven prior bachelorette angles.

**PRODUCTION FLAG:** Illustrative moment, not a confirmed real event. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 07 — "Yellow-Crowned Night-Heron"
**Lane:** Wildlife spotlight, nocturnal framing · **Product:** Naturalist eco swamp tour
**Voice:** EL-Brian (ElevenLabs) · **Music:** low, quiet, a little mysterious, mood only · **Target:** 17.5s

```
 0.0s  Most of the birds on this tour work the day shift. This one doesn't.   [medium shot: heron perched still, camouflaged against branches]
 3.5s  Yellow-crowned night-heron. Red eyes, pale crown, hunts mostly after dark.   [close-up: heron's distinctive head markings, red eye visible]
 8.0s  Crawfish and crabs, mostly. It's doing our job, on a different shift.   [close-up: heron poised, still, watching the water]
12.0s  Catch it at sunrise and it looks half asleep. It's not. It's clocking out.   [wide shot: heron taking off low over the water at dawn light]
15.5s  Night shift, same bayou.   [wide shot: boat gliding past as the heron disappears into the tree line]
```

**ON-SCREEN TEXT TREATMENT:** Small lower-third at 3.5s: "YELLOW-CROWNED NIGHT-HERON." Clears after 2 seconds.

**SHOT LIST:**
- Medium shot: heron perched, still (opener)
- Close-up: head markings, red eye
- Close-up: heron poised over water
- Wide shot: heron taking off at dawn
- Closing wide shot: boat gliding past, heron gone

**SOURCE GROUNDING:** Confirmed unused across all 300 prior pieces. Every prior heron-family piece on file (wood stork, snowy egret, the great blue heron's "eats like a local" piece, the tricolored heron) uses a visual-ID, guide-correction, or ID-difficulty structure. This piece is the first built around a nocturnal-specialist framing, distinct in mechanic from all of them.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Ogilvy for factual specificity (a real diet-based and behavior-based claim, not a vague "cool bird" line). `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "It's doing our job, on a different shift," the most ownable line in the piece since it directly parallels the guide's own working hours.

**DEVICES CHECK:** First yellow-crowned night-heron piece in the series, and the first piece in the series built around a nocturnal-specialist "shift work" framing for any species.

**PRODUCTION FLAG:** Yellow-crowned night-herons are a real, documented Louisiana wetland species, but this pass does not confirm them as a regular sighting on NPB's specific eco-tour route. Confirm with a guide before treating this as anything more than an occasional sighting. No wildlife baited, chased, or handled.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 08 — "King Rail"
**Lane:** Wildlife spotlight, heard-not-seen · **Product:** Naturalist eco swamp tour
**Voice:** voice-en-US-GuyNeural · **Music:** quiet, a little suspenseful, mood only · **Target:** 16.0s

```
 0.0s  Some birds you spot. This one, you just hear.   [wide shot: dense marsh grass, no bird visible]
 3.0s  A clattering, rattling call, coming from somewhere in the reeds nobody can pinpoint.   [close-up: marsh grass swaying gently]
 7.0s  King rail. Guides go years between actual sightings.   [medium shot: guide scanning the reeds, listening]
10.5s  You're not failing to spot it. Almost nobody does.   [medium shot: guests scanning too, straining to see]
13.5s  Some of the best wildlife on this tour, you just have to take on faith.   [wide shot: boat drifting past the reeds, call fading behind]
```

**ON-SCREEN TEXT TREATMENT:** No text overlay. The device is entirely about sound and absence; a text card would undercut the point by naming the bird visually before the VO does.

**SHOT LIST:**
- Wide shot: dense marsh reeds, empty frame (opener)
- Close-up: reeds swaying, implying the call
- Medium shot: guide scanning and listening
- Medium shot: guests scanning too
- Closing wide shot: boat drifting past, sound fading

**SOURCE GROUNDING:** Confirmed unused across all 300 prior pieces. Every prior wildlife piece on file involves a visual sighting, sometimes with a delayed reveal, but always eventually shown on camera. This is the first piece in the series where the subject is never shown at all.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Bencivenga for honesty about scarcity (years between sightings, stated plainly rather than oversold) and Halbert for the reassuring, conversational tone ("you're not failing," directly answering an unspoken guest worry, hitting the "allay their fears" lever from Blair Warren's 27 words). `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "You're not failing to spot it. Almost nobody does," the most reassuring and ownable line in the piece.

**DEVICES CHECK:** First king rail piece in the series, and the first "heard, never seen" wildlife device in the series.

**PRODUCTION FLAG:** King rails are a real, documented and genuinely secretive Louisiana marsh species. This pass does not confirm king rail calls as a regular or reliable occurrence on NPB's specific eco-tour route. Confirm with a guide before treating this as anything more than an occasional, unpredictable occurrence. No wildlife baited, chased, or handled, and none is shown on camera by design.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 09 — "Have You Ever Fallen In?"
**Lane:** FAQ, running joke · **Product:** Naturalist eco swamp tour
**Voice:** voice-en-US-RogerNeural · **Music:** light, deadpan comedic, mood only · **Target:** 15.5s

```
 0.0s  Every single tour, somebody asks it.   [medium shot: guest, half-joking, half-curious, looking at the guide]
 2.5s  "Have you ever fallen in?"   [close-up: guest waiting for the answer]
 4.5s  The guide doesn't even pause. "Once. I don't tell that story anymore."   [close-up: guide, completely deadpan, still paddling]
 8.5s  Nobody's ever gotten more than that out of him.   [medium shot: guests exchanging looks, laughing, waiting for more]
11.5s  Hundreds of tours. Still one story he's keeping.   [wide shot: guide paddling on, unfazed, boat gliding forward]
```

**ON-SCREEN TEXT TREATMENT:** No text until 4.5s, small lower-third under the guide's line: "'ONCE. I DON'T TELL THAT STORY ANYMORE.'" Clears after 2 seconds.

**SHOT LIST:**
- Medium shot: guest about to ask (opener)
- Close-up: guest waiting
- Close-up: guide's deadpan answer
- Medium shot: guests' reaction
- Closing wide shot: guide paddling on

**SOURCE GROUNDING:** Confirmed unused across all 300 prior pieces. Distinct from every prior guide-line piece on file (the deadpan cottonmouth delivery, the weather-excuse running joke, the fake-out point) in that this is the first built around a question the guide deflects rather than answers.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Halbert for the conversational deadpan delivery. `/copywriting-2.0` caught the original closer, "Fourteen tours a week for six years. One story he's keeping," as a fabricated, oddly precise operational figure stated as fact, a falsify-test failure since it invents specific scheduling data with no basis. Rewritten to "Hundreds of tours. Still one story he's keeping," which keeps the scale of the claim without asserting invented specifics. The line to keep is "The guide doesn't even pause. 'Once. I don't tell that story anymore,'" the strongest and funniest line in the piece precisely because it withholds instead of explaining.

**DEVICES CHECK:** First "have you ever fallen in" piece in the series, and the first FAQ-style piece built around a guide deflecting rather than answering.

**PRODUCTION FLAG:** Illustrative bit and guide backstory, not describing any real guide or real incident. No guide identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 10 — "Everybody's First Word"
**Lane:** Guest-reaction montage · **Product:** Naturalist eco swamp tour
**Voice:** voice-en-GB-RyanNeural · **Music:** playful, quick cuts, mood only · **Target:** 15.5s

```
 0.0s  First gator of the tour. Everybody reacts differently.   [wide shot: gator surfacing near the boat]
 2.5s  One guy just says a curse word, quietly, like it slipped out.   [medium shot: guest's face, mouthing a word, embarrassed]
 5.5s  A kid just yells "GATOR" loud enough to startle the actual gator.   [medium shot: kid pointing and yelling, gator submerging slightly]
 9.5s  One guy goes completely silent and just points.   [medium shot: guest, wide-eyed, silent, finger extended]
12.5s  Different words, same sentence underneath: I did not expect that to be real.   [wide shot: whole boat, mixed reactions, gator gliding past]
```

**ON-SCREEN TEXT TREATMENT:** Quote card, "EVERYBODY'S FIRST WORD," pops in at 12.5s under the closing line, clears with the shot.

**SHOT LIST:**
- Wide shot: gator surfacing (opener)
- Medium shot: guest's quiet curse
- Medium shot: kid yelling, gator reacting
- Medium shot: silent guest pointing
- Closing wide shot: whole boat's mixed reactions

**SOURCE GROUNDING:** Confirmed unused across all 300 prior pieces. Distinct from Pass 14 Piece 11 ("There, Right There"), which is about the whole boat leaning and whispering in sync; this piece is built around variance between guests, not synchrony.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Sugarman for the quick comedic escalation across three distinct reaction beats. `/copywriting-2.0` confirmed all five lines pass the 3-test filter. The line to keep is "Different words, same sentence underneath: I did not expect that to be real," the strongest closer in the piece because it names the shared feeling without flattening the individual reactions into one joke.

**DEVICES CHECK:** First "reaction variance" piece in the series, distinct from the existing "whole boat reacts together" device (see Source Grounding).

**PRODUCTION FLAG:** Illustrative composite of guest reactions, not describing specific real guests. No guest identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 11 — "Make a Wish Before the First Gator"
**Lane:** Birthday-group line, eco tour · **Product:** Naturalist eco swamp tour
**Voice:** EL-Eric (ElevenLabs) · **Music:** warm, quiet build, mood only · **Target:** 17.0s

```
 0.0s  The guide already knows whose birthday it is. Doesn't say anything yet.   [medium shot: guide glancing back with a small knowing look]
 3.5s  Right before the first likely spot, he leans back. "Make a wish. Gator's about to earn it."   [medium shot: guide, warm smile, addressing the birthday guest]
 8.5s  She closes her eyes for two full seconds on a moving kayak.   [close-up: guest, eyes closed, small smile]
11.5s  Gator surfaces twenty feet out, right on schedule. Or close enough.   [wide shot: gator surfacing near the boat]
14.5s  Nobody checks if wishes on gators actually work. Nobody wants to know.   [wide shot: whole group smiling, birthday guest looking thrilled]
```

**ON-SCREEN TEXT TREATMENT:** No text until 14.5s, small lower-third: "NOBODY WANTS TO KNOW." Clears with the shot.

**SHOT LIST:**
- Medium shot: guide's knowing glance (opener)
- Medium shot: guide addressing the birthday guest
- Close-up: guest with eyes closed
- Wide shot: gator surfacing
- Closing wide shot: whole group's reaction

**SOURCE GROUNDING:** New birthday-group device, confirmed unused across all 300 prior pieces. Distinct from Pass 93 Piece 11 ("Timed to the Gator"), the only other eco-tour birthday piece on file, which is built around the guide singing happy birthday timed to a gator's surfacing; this piece has no song at all and is built around a private, silent wish-making moment instead.

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Halbert for the warm, conversational setup and Bencivenga for keeping the closing claim honest. `/copywriting-2.0` confirmed the closer, "Nobody checks if wishes on gators actually work. Nobody wants to know," passes the falsify test precisely because it refuses to claim the wish worked; it's a joke about not wanting to test the claim, not an unfalsifiable claim itself. The line to keep is "Gator surfaces twenty feet out, right on schedule. Or close enough," which is honest about the coincidence rather than overselling it as guaranteed.

**DEVICES CHECK:** Second eco-tour birthday piece in the series, structurally distinct from the first (see Source Grounding).

**PRODUCTION FLAG:** Illustrative bit a guide could plausibly do, not a confirmed existing company tradition. Confirm with ops/guides before treating the wish-timing device as an actual practice to promote. No gator baited, chased, or approached.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Piece 12 — "The Logbook Nobody Reads But Him"
**Lane:** Closing ritual, poetic · **Product:** Naturalist eco swamp tour
**Voice:** voice-en-US-BrianNeural · **Music:** quiet, warm strings, mood only · **Target:** 17.5s

```
 0.0s  Back at the dock, before he ties off, the guide writes one line in a notebook.   [close-up: worn notebook, pen, guide's hand writing]
 4.0s  Not the guest count. Not the weather. Just what he saw first that day.   [close-up: notebook page, handwriting, unreadable at this distance]
 8.5s  Six years of tours, six years of first sightings, one line at a time.   [medium shot: guide closing the notebook, tucking it away]
12.0s  Nobody's ever asked to read it. He'd probably let them.   [wide shot: guide securing the boat, notebook in a dry bag]
15.0s  Some things you keep for yourself, not for the guests.   [closing wide shot: dock at golden hour, boat tied off]
```

**ON-SCREEN TEXT TREATMENT:** No text overlay. The piece is deliberately quiet and closes on image, not a caption card.

**SHOT LIST:**
- Close-up: notebook and pen, guide writing (opener)
- Close-up: notebook page, handwriting
- Medium shot: guide closing and stowing the notebook
- Wide shot: guide securing the boat
- Closing wide shot: dock at golden hour

**SOURCE GROUNDING:** Confirmed unused across all 300 prior pieces. Deliberately reworded during the copy-mentors pass to avoid any echo of Pass 15 Piece 10 ("The Only Souvenir That Fits in a Pocket"): that piece is about a feather landing in the boat as a takeaway for guests; this piece is about a private, guest-facing-nothing ritual the guide keeps for himself. The word "souvenir" was removed from the closing line specifically to avoid even a thematic echo (see Status flags and Copy Passes below).

**COPY PASSES:** Drafted, then routed through `/copy-mentors`, channeling Sugarman for the quiet narrative build. During drafting, the original closer read "Some souvenirs aren't for the guests," which was flagged for echoing Pass 15 Piece 10's language too closely even though the underlying mechanic is distinct; rewritten to "Some things you keep for yourself, not for the guests," which keeps the sentiment without the word collision. `/copywriting-2.0` confirmed the remaining lines pass the 3-test filter. The line to keep is "Not the guest count. Not the weather. Just what he saw first that day," the most concrete and ownable line in the piece.

**DEVICES CHECK:** First "guide's private logbook" piece in the series, distinct from Pass 16 Piece 08 ("The Running Tally," a spoken guessing game during the tour) and from Pass 15 Piece 10 (a guest takeaway, not a guide ritual).

**PRODUCTION FLAG:** Illustrative bit, not a confirmed existing guide practice. The six-year tenure figure is illustrative, not a confirmed real guide's record. No guide identified by name or face without the standard filming ask.

**STATUS:** STAGED DRAFT — pending David's approval. No audio generated, no video rendered. Pass 94, 2026-08-16.

---

## Closing note

All 12 pieces above are concept scripts and shot plans only. Nothing has been recorded, no TTS audio has been generated (no ElevenLabs key on this machine), no video has been rendered (no ffmpeg on this machine), and nothing has been posted or scheduled. This document, and each piece's companion `NOTES.txt` file in `Marketing/Narrated/2026-08-16 Party & Boat Sayings — Pass 94/`, is a staged draft pending David's review and approval before any production step begins.
