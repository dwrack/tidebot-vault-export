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

Tested against 10 real clips from today's boarding rush. All ten correctly cleared,
zero false positives, and it read the scene right ("some walking toward boats, some
toward parking area; no fuel containers"). Measured volume is 48 clips/day across the
two cameras, about $1/day to judge.

## Still open

- [ ] **Where does fueling actually happen?** No frame I pulled shows a fuel pump or
      dispenser. It looks like fuel moves in portable cans, not off a dock pump. If
      there's a pump somewhere, say which camera sees it.
- [ ] Turn on the every-15-minutes schedule (`com.npb.marina-watch.plist`, staged, not
      loaded)
- [ ] Nothing has been posted to Slack yet

## Related

Ties into the Marina closeouts line on the NPB initiative board (Jeffrey, Blink cams,
tracker #16-18).
