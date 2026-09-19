# Marina Fuel Watch (NPB)

Built 2026-09-19. Watches the NPB marina Blink cams and flags fuel headed for the
parking lot instead of the boats.

## The detection rule

Gas cans at the pump are normal. That's how the boats get fueled. The only thing that
gets flagged is a can moving from the pump toward a vehicle or the lot, a can going
into a trunk or truck bed, or a nozzle in a road vehicle. Two Claude passes on every
candidate, cheap model then strong model, and the prompt is deliberately biased toward
"no" because a false alarm here means someone gets accused.

## Where alerts go

`helm-ops` (C0ATFJY5QET, David + Michael). **Not** helm-npb. The crew reads helm-npb,
and if the person walking cans to a truck is on the crew, an alert in their channel is
a heads-up. One line in `config.json` moves it if that call is wrong.

## Code

`~/Projects/marina-watch/` (outside the vault, video files don't belong in iCloud).
See the README there. Schedule is `com.npb.marina-watch.plist`, every 15 minutes,
staged but not loaded.

## What's already done

Login was already there. The E&E camera review logged this Mac into the Blink account
back in August, and it's the same account, so no new credentials were needed. 27
cameras total; the marina is network 717084. Subscription is active, clips are flowing.

Watching two cameras:
- **Gas tank** - the dock. Water and slips right and center, grass and the TAG US gate
  on the left, red cans staged on the grass bottom-left.
- **Wired Floodlight - 047N** - the gravel lot. Parked cars, van and trucks across the
  top third; dock is behind the camera.

A can leaving the dock frame and showing up in the lot frame headed for the trucks is
the pattern worth catching.

Not watched: `Gas station` and `GAs station 2`. Despite the names those are the indoor
ticket counter with staff at the desk. No reason to point an AI judge at that.

**It runs free, entirely on the Mac.** No API, no cloud vision, no per-use cost. The
detector is numpy and ffmpeg: mask fuel-can red, filter to can-shaped blobs, track them
across frames, and score how far they travel toward the vehicles. A can sitting in
storage doesn't move, so requiring motion throws out every static red object for free.

Biggest false-alarm source was guests in orange and red clothing walking to their cars
after a tour. Capping green in the colour mask separates an orange shirt (240,140,40)
from a red jerrican (200,30,30), and a shape filter drops torsos, which are much taller
than wide. That took the lot camera from 7 false alarms in 24 clips down to zero.

Measured: fires on a can carried toward the lot on both cameras, stays silent on a can
carried back toward the boats, and 0 false alarms across 34 real clips.

## Still open

- [ ] Turn on the every-15-minutes schedule (`com.npb.marina-watch.plist`, staged, not
      loaded). Nothing has posted to Slack yet.
- [ ] **Night is the real gap.** Blink goes infrared after dark, colour disappears, and
      a colour-based detector is blind. If fuel is walking off at night this won't see
      it. Fixing that means either a brightness-and-shape detector for IR, or flipping
      `engine` to `claude` for the overnight hours only (a few dollars a month).
- [ ] A can that isn't red, or one inside a bag or cooler, goes straight past it. That's
      the honest ceiling of colour matching.

## Related

Ties into the Marina closeouts line on the NPB initiative board (Jeffrey, Blink cams,
tracker #16-18).
