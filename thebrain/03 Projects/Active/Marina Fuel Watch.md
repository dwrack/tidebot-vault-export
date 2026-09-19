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

## Still open

- [ ] Blink login (Desktop shortcut `Marina Watch Setup`, needs the account password + 2FA)
- [ ] Which camera name covers the fuel pump -> `config.json` `camera`
- [ ] Scene map: run `calibrate`, look at the frame on the Desktop, say which side is
      the dock and which is the lot -> `config.json` `scene_map`. Nothing works without this.
- [ ] Confirm NPB has an active Blink Subscription Plan. No plan, no cloud clips, no watcher.
- [ ] Load the launchd job

## Related

Ties into the Marina closeouts line on the NPB initiative board (Jeffrey, Blink cams,
tracker #16-18).
