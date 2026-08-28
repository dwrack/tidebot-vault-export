# Daily Video Factory — 4-5 Videos Per Brand Per Day

*Built Aug 27, 2026. Owner: David. Status: Phase 1 starting.*
*Companion docs: `06 Learning/532 Content Method` (idea grids), `06 Learning/Headline Typography` (cover-line rule), per-vault `Marketing/532 Content Grid`, `Marketing/UGC Outreach & Repost Playbook`.*

---

## The honest math first

4-5/day per brand across 7 active-social brands is ~30 videos/day, ~900/month. Nobody hand-crafts that. It only works as a **factory with tiers**: most volume comes from cheap remixes and AI generation, a thin top layer is real creative. And the bottleneck is not making videos, it's approving them (the quota-burn rig proved that in August: 1,604 good drafts, zero throughput). So the factory is rate-limited by the review loop, not the render queue.

**Approval design (agreed):** David does one 10-minute morning pass on a visual review board (Tier 1 pattern from `reference_visual_review_boards`), then each brand's manager clears their own lane in Slack. Nothing posts unseen. Next day's batch for a brand only generates if yesterday's was reviewed — the hard rule that keeps the queue from exploding.

Brand → approval lane:
| Brand | Manager lane |
|---|---|
| NPB | Jeffrey / JT |
| NKST | Jeffrey (interim, no manager) |
| DCKT (+ ebike) | Lea (social) — no manager since Bella left |
| HPB, BBK, AKT | Connor — batch his 3 brands into ONE weekly-rhythm message, he's stretched |
| Ebb & Ember | Kimberlyn |

---

## The daily mix (per brand)

Five slots a day. The mix is designed so only ~1 slot/day needs anything resembling a shoot.

| Slot | Source | Cost per video |
|---|---|---|
| 1. Real-footage remix | Crew Clips library + vault footage, recut | ~5 min automated |
| 2. Narrated faceless reel | narrate2.mjs (ElevenLabs + ffmpeg) over owned b-roll | ~10 min automated |
| 3. Higgsfield generation | Seedance/image-to-video from prompts + owned stills | ~5 min + render |
| 4. UGC / repost | Tagged guest content, permission via playbook DMs | ~0 min creation |
| 5. Trend / guerilla | Trend-jack, duet/stitch, comment-bait, text-on-screen take | ~10 min |

When slot 4 has no UGC that day (common early), backfill with a second Higgsfield or remix. 4/day is the floor, 5 the target.

---

## The format ladder — easiest fruit first

### Rung 1 — Zero new tooling, start today
All from assets already sitting in the vaults.

1. **Crew Clips remix** — 196 graded clips (`~/Library/Mobile Documents/com~apple~CloudDocs/Crew Clips/`), DCKT 102, BBK 37, NPB 33, AKT 21. Recut to 9:16, cover line in brand display face, trending audio. The 1-great and 2-good tiers alone fund weeks.
2. **Text-on-screen silent** — big-type take over any usable clip. "No, you don't have to pedal." Lowest effort format in the 532 library, performs sound-off.
3. **Static Q&A** — answer one real OpenCX ticket / FAQ on screen as text over b-roll.
4. **Screen-recording content** — booking flow, live weather/tide, the map to the launch. Weirdly high-trust.
5. **Review overlay** — 5-star GBP review as animated text over footage. Reviews are already pulled via GBP MCP.
6. **UGC repost** — playbook + DM templates already in every vault's Marketing folder. Free trust.

### Rung 2 — Existing pipelines, small setup
7. **Narrated faceless reels** — the Admire NOLA format, 16 already shipped. `narrate2.mjs` on both machines, `fit:"pad"` for 1080p boat footage. Footage exists for NPB (220 files) + HPB in-vault; Admire NOLA 4K drone in ~/Downloads on primary. Gap: DCKT/NKST/E&E b-roll needs harvesting from Crew Clips into per-vault Assets/Videos.
8. **Ranking / listicle b-roll cuts** — "5 things to bring," cut with `~/Projects/video-tools/` (repoint the hardcoded BASE first).
9. **Data-drop reels** — a real number from FareHarbor reports over footage. Nobody else can say it (passes the copywriting-2.0 falsifiability test).

### Rung 3 — Higgsfield on existing assets (the multiplier)
Account is paid; MCP auth in progress. Every format here starts from something we already own, so it stays on-brand.

10. **Photo → motion** — animate existing hero stills, drone frames, GBP photos. Cheapest Higgsfield win; instant b-roll for the footage-poor brands (NKST, E&E, AKT).
11. **Impossible-camera hooks** — 3-second AI opener (camera dives underwater past the gator, rockets off the dock) cut into real footage. Hook is AI, proof is real. This combo is the scroll-stopper.
12. **AI b-roll for unshootable scenes** — swamp at dawn in fog, Door County in February, historical New Orleans, the sauna from a bird's eye. Faceless-channel style file covers it.
13. **Seedance full prompts** — the `seedance-video` skill's 7 styles (viral-hook, before-after, luxury-aesthetic, faceless, testimonial, personal-brand, podcast-visual) with Director's Lens variants. Paste-ready prompts already its output.
14. **AI narrator character** — a recurring "Davey Jones" style brand character (Higgsfield Speak-type avatar) fronting the faceless educational formats. Episodic = follow-worthy. Persona names are already an accepted pattern.
15. **UGC-style AI ads** — Higgsfield's ad-style generations for paid, fed by `/ad-research` → `/ad-scripter` angle banks. Doubles as organic when soft.

### Rung 4 — Vibe filmmaking originals (the ceiling)
16. **Multi-scene narrative reels** — scripted 30-60s minis: scenario/skit, confession/rant, origin story from the 532 storytelling formats, storyboarded shot-by-shot, each shot generated or matched from the library, assembled with ffmpeg. One per brand per WEEK, not per day.
17. **Director's Lens series** — same trip, Wes Anderson vs Malick vs Bourdain treatment. The series concept IS the hook.
18. **Brand trailers** — one cinematic 45s anthem per brand per season; pinned, run as paid, cut into 3 teasers.

### Rung 5 — Guerilla (digital now, stunts later phase)
Digital, start with the factory:
19. **Trend-jacking lane** — daily slot 5. Apify trend wiring + IG saved-ideas bank already exist for detection.
20. **Duets/stitches** — stitch viral kayak fails with "our guides on why that happened." Commentary formats need no footage.
21. **Comment-section plays** — deliberately underexplained videos ("we don't talk about slip 7"); reply-to-comment videos as their own content stream.
22. **Local seeding** — reddit-finder engine + FB group poster already built; feed them the winners, approval flow already agreed.

Physical stunts, later phase (one per brand per month once the factory hums; needs manager buy-in per city):
23. Dock theater (costumed greeter, over-the-top sendoff filmed for the feed) · mystery installs (a message in a bottle wall, "paddle here" stencils where legal) · a ridiculous world-record attempt (most people in pirate hats on one barge) · free-ride-if-you-find-us drops teased on Stories. Each stunt is planned AS content first: the video is the point, the stunt is the set.

---

## Pipeline (idea → posted)

1. **Idea**: 532 grid rows (already 30/brand/month) + trend lane + UGC inbox. Grids refresh monthly.
2. **Script/prompt**: `seedance-video` for Higgsfield prompts, `video-mentors` for packaging/hook checks, timed-script NOTES format for narrated pieces.
3. **Produce**: Higgsfield (rung 3-4) / narrate2.mjs (rung 2) / ffmpeg recuts (rung 1). Batch by layout, not by day — one session per format covers the week.
4. **Gate**: `content-gate` score + mandatory cover line per the typography standard. No cover line = not finished.
5. **Review**: nightly build of a per-day review board (HTML, plays media); David's 10-min AM pass approves/kills; survivors route to the brand's manager lane in ONE Slack message per brand (no stub floods).
6. **Post**: YouTube via per-brand MCPs (all 10 wired). IG Reels via Graph API (`META_IG_TOKEN`). TikTok has no API path — post via the logged-in Chrome bridge or a scheduler; solve in Phase 2.
7. **Learn**: weekly winners report; boost top organic by saves (shares for NPB/HPB) per the paid+organic single loop.

## Skills — have vs build

**Already in-house and used by this plan:** seedance-video, video-mentors, social-captions, social-content, content-gate, ffmpeg-usage, ad-research/ad-scripter, copy-mentors, copywriting-2.0, marketing-ideas, shareability framework, 532 method.

**To build:**
- **`/daily-slate` (the missing orchestrator)** — the content-engine mega skill scoped in April, now with a concrete job: for one brand, read the 532 grid + Crew Clips INDEX + UGC inbox, emit the day's 5 briefs, produce what's automatable, build the review board. This is the single highest-leverage build.
- **Higgsfield MCP wiring** — auth, then map which generations can be driven from the terminal vs pasted in the web app.
- **TikTok posting path** — bridge-driven upload or third-party scheduler decision.
- **Winners report** — weekly per-brand retention/saves pull feeding the boost loop.

## Rollout

- **Week 1 (now):** Pilot DCKT only (most clips, Lea can own the lane). Rungs 1-2 + first Higgsfield generations. Prove 4-5/day for 5 straight days INCLUDING the review loop. Build `/daily-slate` against this pilot.
- **Week 2:** Add NPB + NKST (Jeffrey lane). Higgsfield photo→motion for NKST's footage gap. TikTok posting path decided.
- **Week 3:** Add the Texas three as one Connor-rhythm batch + E&E (Kimberlyn). Full 7-brand slate.
- **Week 4:** Rung 4 originals begin (1/brand/week). First AI narrator character episodes. Winners report live.
- **Later phase:** physical stunts, one brand at a time, video-first planning.

**Guardrails (non-negotiable, learned the hard way):** next batch conditional on last batch reviewed · hard cap 5/brand/day · nothing posts without a human tap · no unreviewable pile-ups — if a lane goes 3 days unreviewed, its generation pauses and the weekly report says so.
