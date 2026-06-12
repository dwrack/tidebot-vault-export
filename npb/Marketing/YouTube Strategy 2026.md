# NPB YouTube Strategy - 2026

*Written 2026-06-12. Companion docs: YouTube Footage Inventory.md (same folder), pipeline at ~/Projects/npb-youtube/pipeline/.*

## Why YouTube, in order of weight

1. **Video carousels inside Google SERPs.** We already rank page 1-2 for "party boat new orleans" (pos 3.4), "boat ride new orleans" (pos 7.5), "swamp tours new orleans" (pos 7-8), "booze cruise new orleans" (pos 9-16). Google shows a video carousel on most of these. A ranking video means two listings on the same results page. We currently occupy zero video slots.
2. **YouTube is where trip planners qualify the experience.** "Is this a booze cruise or a swamp tour? Will my group like it? Is there a bathroom?" A 90-second video answers all of it and the under-35 bachelorette planner watches video, not blog posts.
3. **Embeds raise conversion.** Each booking-closer video gets embedded on its matching site page. The bathroom-moat page (/swamp-tours-with-onboard-restrooms/, 11.4% CTR) is first in line.

## Channel state and rebrand

The existing channel (UCZeNzE2p4AvC0wdMRdNk7PA) is still branded "New Orleans Pedal Barge." That name is retired. Full rebrand kit lives in `Marketing/YouTube Channel Rebrand Kit.md`. Nothing publishes until the rebrand is done, one weekend of old-name uploads next to new content would look broken.

## Positioning

**Channel name:** NOLA Party Barge
**One-liner:** Private BYOB party boats and real bayou swamp cruises, 7 miles from the French Quarter.
**The thesis (from the social content bank): real NOLA happens on the water.**

We are not a generic New Orleans tourism channel. Every video is about our boats, our bayou, our crew, and what it feels like to be on board. Narrow brand, wide content within it.

## Content pillars

**1. Party energy / trip POV - 40%, Shorts.** Dancing, bachelorettes, group reactions, champagne moments, raft-ups. This is what the existing library already is. Job: stop the scroll, transmit the feeling, make someone send it to their group chat with "THIS."

**2. Booking closers - 20%, long-form 3-6 min.** "What a NOLA Party Barge trip is actually like," boat walkthroughs, BYOB rules, what to bring. These kill pre-booking objections. Each one embeds on its matching site page.

**3. NOLA + bachelorette guides - 20%, long-form, scripted.** "Things to do in New Orleans on the water," "Bachelorette weekend itinerary," "Boat ride options in New Orleans compared." Maps directly to the GSC queries above. Script with /seo-blog-writer voice rules, narrate in the Nolan voice.

**4. Swamp + wildlife - 10%, both formats.** Alligators off the boat, real bayou vs theme-park swamp tour, what lives in Bayou St. John. Gator content is the most reliably viral thing we own.

**5. Crew + behind the scenes - 10%, both.** Captains telling stories, day in the life, marina life. Parasocial trust is half of why a group picks one operator over another. Crew on camera, not David.

## SEO / GEO system (every upload, no exceptions)

**Titles:** front-load the search phrase, then the curiosity gap. "Party Boat in New Orleans: what your group actually gets" beats "BEST DAY EVER on the bayou!!" Pull phrasing from GSC top queries and YouTube autosuggest before writing.

**Descriptions, in this order:**
1. Two to three sentences with the target phrase and location words (New Orleans, Bayou St. John, French Quarter) in the first 150 characters
2. Booking link with UTMs: `?utm_source=youtube&utm_medium=video&utm_campaign=<video-slug>`
3. Chapters (long-form only)
4. Three-question FAQ block written in plain Q and A. This is the GEO play: AI answer engines lift clean Q and A text verbatim
5. Location block: marina address area, "7 miles from the French Quarter, 15-20 minute ride"

**Captions:** whisper-generated SRT uploaded on every video that has speech. Search engines and LLMs index transcripts, not vibes.

**Playlists:** one per pillar. Pinned comment on every video: one line + booking link.

**Hashtags:** #neworleans #partyboat #swamptour, max 3, in the description not the title.

**Banned:** any pedal reference, anywhere, ever. Also no "Pedal Barge" in tags even though it still gets brand searches; the site catches those, the channel should not reinforce the old name.

## Cadence

- **Shorts: 3-4 per week.** Library + weekly #crew-content drops can sustain this indefinitely.
- **Long-form: 2 per month** to start, monthly review. Long-form is gated on footage: the Drive pull list and the horizontal-pass capture rule have to happen first.
- Shorts schedule slots: Thu 7pm, Sat 10am, Sun noon, Tue 3pm (CT). Bookings skew in-week and last-minute now, so Tue/Thu slots stay even if weekend performance is better.

## Production model

Same three-layer split that works for DCKT:

- **Real footage is the spine.** Vault library + Drive originals + deckhand capture (one horizontal 16:9 pass per trip, now in the capture playbook). Never replaced by AI.
- **ffmpeg pipeline does the repetitive work.** ~/Projects/npb-youtube/pipeline/: grade, blur-pad Shorts conversion, caption burn-in, concat. Low-res legacy clips get blur-pad treatment, not hard crops.
- **Higgsfield fills impossible gaps only (~15% max).** Aerials we don't have a drone in the air for, atmospheric hooks (mist on the bayou, neon reflections), off-season filler. Never AI-generate guest or crew faces or multi-person party scenes. Disclose where required.

Packaging and hook decisions route through /video-mentors. Captions and descriptions through /social-captions.

## Launch slate (first 6)

1. Short - bride backhandspring (best HD moment in the library)
2. Short - alligators off the party boat
3. Short - paddlewheel sunset b-roll, text hook: "the part of New Orleans tourists never see"
4. Short - group dance energy (tik tok dance whole group or tiki dance off)
5. Long-form - "What a NOLA Party Barge trip is ACTUALLY like" (booking closer; embeds on the main tour page). Needs: Drive pull + one fresh horizontal trip pass.
6. Long-form - "Real bayou vs tourist-trap swamp tours" (positioning piece; targets "swamp tours new orleans")

## Measurement

Monthly: YouTube Studio (CTR, retention, traffic sources), GSC video impressions, GA4 sessions from youtube/video UTMs, FareHarbor bookings on tagged links. Double down on whichever pillar holds retention. 90-day review: cadence, YouTube Data API direct upload, extending the Creator Outreach Playbook to YouTube collabs.

## Open items

1. Channel ownership: which Google account has Studio access (rebrand is blocked on this)
2. Drive pull: sync the priority list from YouTube Footage Inventory.md locally
3. Jeff: weekly best-of drop from #crew-content + horizontal-pass buy-in
4. Higgsfield plan: confirm active tier (~$39/mo for volume)
