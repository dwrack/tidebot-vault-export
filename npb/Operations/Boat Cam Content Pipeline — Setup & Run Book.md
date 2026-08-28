# Boat Cam Content Pipeline — Setup & Run Book

*Built 2026-08-28. Brand: NOLA Party Barge (first). Tool: `/boatcam`.*

The idea: the boat already has three hours of people having a good time on it every
shift. That's the cheapest content we will ever own. The problem was never the footage,
it was that nobody is going to scrub three hours to find the eleven seconds worth posting.
This does the scrubbing.

---

## Part 1 — Getting footage off a boat with no wifi

The constraint David named: no wifi on the water, and it has to be automated, because
anything that depends on a captain remembering to pull an SD card will die in two weeks.

**The pattern that works: record local, upload at the dock.**

The camera writes to its own SD card all shift with no connectivity at all. When the boat
comes back, the camera comes off the mount and goes into a charging cradle in the marina
office, on the marina wifi. It uploads overnight while it charges. Nobody pulls a card,
nobody plugs into a laptop. The only human step is "put the camera in the dock," which is
one line on the closeout checklist Jeffrey is already building.

**Hardware, in priority order:**

| Piece | What | Why |
|---|---|---|
| Camera | GoPro HERO13 Black | It has the exact feature this needs: with a GoPro Premium subscription it auto-uploads to the cloud while charging on a known wifi network, then clears the SD card itself. Nothing else does this cleanly out of the box. |
| Subscription | GoPro Premium | Required for auto-upload. This is the whole reason to pick GoPro over a cheaper cam. |
| Mount | Hard-mounted, forward-facing, above head height | Above head height is what makes the shot read as "the boat," not "a guy's chest." |
| Power on the boat | 12V USB-C off the house battery, or 2-3 swap batteries | HERO13 will not survive a full day of shifts on one battery in New Orleans heat. |
| Dock | Charging cradle in the marina office, on marina wifi | Same breaker as the Blink cams (tracker item #18). |

**Notes and honest caveats:**

- Marina wifi has to actually exist and be stable. If it doesn't yet, that's the real
  first task, and it's cheap: a consumer router on the office connection.
- Heat and salt will kill cameras. Budget for replacing one a season and don't buy the
  most expensive body.
- Reolink and similar fixed marina cams are the right tool for *security* at the dock, and
  Jeffrey's Blink install covers that. They're the wrong tool for *content* — the footage is
  low bitrate, badly placed, and looks like what it is. Use the action cam for content.
- Do not run a second "content" camera at the marina hoping to double-dip. One camera on
  the boat, doing one job well, is what actually gets maintained.

**If GoPro's ecosystem is a dealbreaker:** the fallback is any cam recording to SD plus a
cheap always-on Mac mini or Pi in the marina office with an SD reader, auto-copying to a
synced folder. More moving parts, more to break, but no subscription. Only worth it if
we're running four-plus cameras across brands.

---

## Part 2 — The processing pipeline

Installed and tested end to end on 2026-08-28. ffmpeg 9.0.1 static build at
`~/.local/bin/ffmpeg` (this Mac has no Homebrew, don't try to install it).

Media lives at `~/BoatCam`, deliberately outside the iCloud vault so we're not syncing
gigabytes of video across devices.

```bash
# 1. drop a shift's footage in ~/BoatCam/inbox/npb/ then:
python3 ~/.claude/scripts/boatcam.py scan   npb
python3 ~/.claude/scripts/boatcam.py detect npb --window 6 --spacing 60 --top 20
python3 ~/.claude/scripts/boatcam.py sheets npb
# 2. look at the contact sheets in ~/BoatCam/sheets/, pick the good numbers
python3 ~/.claude/scripts/boatcam.py cut    npb "1,4,9,14" --tag 2026-08-30
# 3. hand the clips to /social-captions
```

**How detection works.** Every few seconds of footage gets scored on scene-change (motion)
and EBU R128 momentary loudness (cheering, music, engine), normalised per file, motion
weighted about two to one over audio. Then a greedy non-overlapping pick so you don't get
twelve versions of the same thirty seconds. Benchmark on the test footage: it found the
single active segment at 00:50 with a score of 0.998 against roughly 0.00 for everything
else. Speed is about 3 minutes of processing per hour of footage.

**What detection cannot do.** It finds *activity*. It cannot find a *moment*. That's why
the contact sheet step exists and why it isn't optional. Expect 3-6 keepers out of 20
candidates.

**What the cut does.** 9:16 crop, upscale to 1080x1920, denoise, sharpen, warm the grade,
force 30fps. Camera footage graded flat reads as surveillance; a little contrast and
saturation is the difference between "our boat" and "evidence." Audio is stripped by
default.

---

## Part 3 — Standing rules

- **No release, no post.** Guests are recognisable. See the staged photo/video release
  (Part 4) — nothing from this pipeline goes public until that's live in the booking flow.
- **Audio off by default.** Recording guest conversations is a consent problem we don't
  need, and the track is engine noise anyway. Music goes on in the edit.
- **Auto-cut list:** minors, visible license plates, visible phone screens, anyone being
  sick, anyone who looks unflatteringly drunk. Not a judgment call, just cut it.
- **Clips are drafts.** They go to David or JT before anything gets scheduled.

## Part 4 — Open items

| # | Item | Owner |
|---|---|---|
| 1 | Confirm marina wifi exists and is stable enough to upload overnight | Jeffrey |
| 2 | Order HERO13 Black + Premium sub + mount + 12V power | David |
| 3 | Add "camera into the dock" to the closeout checklist | Jeffrey |
| 4 | Get the photo/video release live in the FareHarbor booking flow | David |
| 5 | First real run: one weekend shift, measure keepers per hour | David |
