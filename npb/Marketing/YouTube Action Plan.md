# NOLA Party Barge - YouTube Action Plan
*Living plan. Started 2026-06-13. Companion to YouTube Strategy 2026.md and YouTube MCP Activation.md.*

## The one insight that matters

Pulled from real channel analytics (last 12 months):

- **409,688 views**
- **94% average retention** (top videos hit 78-103%, some over 100% from rewatches)
- **+10 subscribers**

Read that again. Elite reach, elite retention, almost zero subscribers. The top 3 videos pulled 100K-167K views each and converted **zero subs between them**. The content works and YouTube is rewarding it with reach. We've just been letting all of it walk out the door.

**So the goal is not more views. It's capturing the views we already get.** Every fix below points at that.

## Done already (2026-06-13)

- Built a YouTube MCP so Claude manages the channel directly (auth as the Party Barge brand account). See YouTube MCP Activation.md.
- Enabled YouTube Data + Analytics APIs in the Cloud project.
- **Repackaged the 11 biggest videos in place** (no re-uploads, no lost history): killed every "Pedal Barge" title, front-loaded the search term, added a hook, and for the first time put a booking link + keywords + tags in each description. That's ~700K lifetime views of content now actually pointing at a booking.
- New on-brand banner (sunset boat + logo).
- 5 pillar playlists created and seeded with the winners, so one view can become a binge:
  - New Orleans Party Boat / Bachelorette in New Orleans / Swamp Tours & Gators / BYOB Booze Cruise / Things to Do in New Orleans
- Channel description rewritten (was still pedal-era "Cycleboat" copy).

## Next, in priority order

### 1. Conversion plumbing (highest leverage, do first)
The reach exists. Capture it.
- **Pinned comment with a booking link on the top ~10 videos.** The API can post a comment but can't pin it, so this is a 5-minute manual pass in Studio, or Claude posts and you pin. Worth it on 100K+ view videos.
- **End screens + "Subscribe for more" cards** on the winners (manual in Studio, API can't).
- **Re-title sweep on the rest of the 84** using the same formula (search term + hook, booking link in every description). Claude can run this anytime, no Mac needed.
- Full playlist categorization of all 84 videos (Claude, anytime).

### 2. The recut batch (needs your Mac)
- Download the top winners + raw footage with yt-dlp into the pipeline.
- Re-cut hook-forward versions: hard hook in the first 2 seconds, tighter, with a payoff at the end so retention stays high AND there's a reason to act. These are NEW focused cuts, not duplicate re-uploads.
- Stage them private for your review, then publish on the cadence.

### 3. The subscriber fix (the real unlock)
Shorts barely convert subs, that's why 167K views got us nothing. Two moves:
- **Give people a reason to subscribe**: a recurring series with a name and a promise. "Things to Do in New Orleans This Weekend" is the obvious one (you already made episodes), it's a reason to come back.
- **Add some longer-form** (3-6 min): the booking-closer trip walkthroughs from the strategy doc. Long-form converts subs and bookings far better than a 15-second twerk clip ever will.

### 4. Repeatable engine
- 3-4 Shorts/week from the footage library + weekly crew clips (pipeline already built at ~/Projects/npb-youtube/pipeline/).
- Every upload: search-term title, description with booking UTM link, captions, into a playlist, pinned comment.
- Monthly: check Analytics for which pillar holds retention and converts, double down.

## Still manual (API can't touch)
- The **@handle** (still @neworleanspedalbarge3261). Change in Studio.
- The **profile avatar**. Upload in Studio.
- Pinning comments, end screens, info cards.

## Metric to watch
Not views. **Subscribers gained and clicks to the booking link.** If views stay flat but subs and booking clicks climb, we're winning. That's the whole game now.
