# NKST Shorts — Upload Schedule & Metadata

✅ **ALL 4 UPLOADED & SCHEDULED (2026-06-23).** Private until their publish time, so you can preview or pull any before it goes public. Edit anything in YouTube Studio.

| Short | Video | Goes public |
|---|---|---|
| Gator | https://youtube.com/watch?v=P5PxTLxR7G4 | Wed Jun 24, 6pm CT |
| Wildlife | https://youtube.com/watch?v=CovFBJkOcRc | Sat Jun 27, 6pm CT |
| Scenery | https://youtube.com/watch?v=ARwDkZy9QDc | Tue Jun 30, 6pm CT |
| Quote | https://youtube.com/watch?v=lWVR6Dk78fU | Fri Jul 3, 6pm CT |

Channel: New Orleans Kayak Swamp Tours (`UCNLC1hBSxXF0zqCzndY8rig`)
Cadence: every ~3 days, 6:00pm CT (good Shorts window). Ordered strongest-hook first.

---

### 1. Gator Short — `NKST Gator Short - can you spot it.mp4`
- **Publish:** Wed Jun 24, 6:00pm CT (`2026-06-25T00:00:00Z` UTC... see note*)
- **Title:** Can you spot the gator? 🐊 New Orleans swamp kayak tour #shorts
- **Description:**
  Real wild alligator, 30 minutes from the French Quarter. This is what a guided kayak swamp tour outside New Orleans actually looks like.
  Book your paddle: neworleanskayakswamptours.com
  #neworleans #swamptour #kayaking #alligator #louisiana #nola #manchac #shorts
- **Tags:** new orleans kayak, swamp tour, alligator, kayaking new orleans, manchac swamp, louisiana swamp, nola things to do, cypress swamp

### 2. Wildlife Short — `NKST Wildlife Short - 30 min from Bourbon.mp4`
- **Publish:** Sat Jun 27, 6:00pm CT
- **Title:** Everything you'll see 30 min from Bourbon Street 🐊🐢 #shorts
- **Description:**
  Gators, turtles, herons, tanagers and more, all on a guided kayak tour in the cypress swamps just outside New Orleans.
  Book your paddle: neworleanskayakswamptours.com
  #neworleans #swamptour #kayaking #wildlife #louisiana #nola #shorts
- **Tags:** new orleans wildlife, swamp wildlife, kayak tour, alligator, turtle, summer tanager, louisiana nature, nola

### 3. Scenery Short — `NKST Scenery Short - peaceful 30 min.mp4`
- **Publish:** Tue Jun 30, 6:00pm CT
- **Title:** The most peaceful 30 minutes near New Orleans 🛶 #shorts
- **Description:**
  Mirror-still water, Spanish moss, golden light. The calm side of New Orleans most visitors never see.
  Book a swamp kayak tour: neworleanskayakswamptours.com
  #neworleans #swamptour #kayaking #cypress #relaxing #louisiana #nola #shorts
- **Tags:** new orleans swamp, cypress swamp, peaceful, kayak tour, manchac, louisiana, nature, asmr

### 4. Quote Short — `NKST Quote Short - to love a swamp.mp4`
- **Publish:** Fri Jul 3, 6:00pm CT
- **Title:** To love a swamp 🌿 New Orleans kayak swamp tour #shorts
- **Description:**
  "To love a swamp is to love what is muted and marginal, what exists in the shadows, what shoulders its way out of mud."
  Paddle the cypress: neworleanskayakswamptours.com
  #neworleans #swamptour #kayaking #louisiana #nature #nola #shorts
- **Tags:** new orleans swamp, kayak tour, cypress, louisiana, nature, nola, manchac

\* Times are 6pm Central (CDT = UTC-5), so publishAt is 23:00 UTC the same calendar day. I'll set them exactly at upload.

---

## Booking URL — set
All four descriptions now link **neworleanskayakswamptours.com**. Flagship deep link if we ever want it: `neworleanskayakswamptours.com/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/`. Once auth is back I can also copy the exact UTM-tagged link your existing video descriptions use, if you'd rather keep tracking consistent.

## BLOCKER: YouTube re-auth required
The `youtube-nkst` connection's token expired June 14 and can't refresh (Google kills refresh tokens after ~7 days while the OAuth app is in "Testing" mode). Nothing uploads until it's renewed.

**Fix (about 30 seconds):** double-click **`NKST YouTube Re-Auth.command`** on your Desktop. A browser opens, sign in as the Google account that owns the NKST YouTube channel, click Allow. It reuses the stored client credentials so you don't paste anything, and it has a safety lock that refuses to save if you pick the wrong channel.

Then tell me "done" and I'll schedule all 4.

**Permanent fix:** publish that project's OAuth consent screen to "In production" in Google Cloud and the 7-day expiry goes away. I can walk you through it if you want to stop this from recurring.
