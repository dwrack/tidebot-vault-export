# Stove Watchdog — Inkbird Auto-Relight

Automated fix for the misfire problem: when the sauna drops below 165°F during working hours (deliberately above the Inkbird app's 162°F alert — if that phone alert ever fires, the watchdog missed it and someone should look manually), the watchdog checks the stove cam, and if the flame is out it cycles the Inkbird set point (190 → 90 → 190) to force a re-ignition, then verifies the flame relit on camera. Retries every 5 minutes until it works. Davey gets a Slack DM when it misfires and again when it's confirmed relit.

## How it works

- Runs on the always-on Mac (davids-mbp-2) as launchd job `com.ebbember.stove-watchdog`, every 5 min, active 6:30am–10:00pm only.
- Temp read + set point changes go through the Tuya cloud API (the ITC-308-WIFI is a Tuya device; set point is DP 106, temp DP 104, values ×10).
- Flame verification: Blink "Stove" cam snapshot → Claude (haiku) answers ON / OFF / UNCLEAR.
- If temp is low but the flame IS lit (someone poured water on the sensor), it does nothing and just watches; only alerts if that state persists 45+ min.
- Alerts: Slack DM to Davey. Misfire → cycling → relit ✓, plus escalation after 3 and 6 failed attempts.

## Files (on davids-mbp-2)

- Script: `~/ee-stove-watchdog/watchdog.py` (`probe` and `test-alert` subcommands for debugging)
- Config: `~/.config/ee-stove-watchdog/tuya.env` (Tuya API creds — local only, never in the vault)
- Log: `~/ee-stove-watchdog/watchdog.log`, snapshots in `~/ee-stove-watchdog/snaps/`
- Blink creds: `~/.config/blink-ee/creds.json` (copy of the ones on Davey's MacBook)

## Setup status (2026-08-27)

- [x] Watchdog built, Blink snapshot + flame detection tested (correctly read ON from a live flame)
- [x] ~~Tuya IoT cloud API route~~ DEAD END: the INKBIRD iPhone app's QR scanner can't complete Tuya's "Link App Account" authorization (shows raw token text, no Confirm screen; app update didn't fix it). Re-pairing into Smart Life needs someone at the stove; Davey away for a week and doesn't want to depend on crew.
- [ ] Plan B in progress: Android emulator on the always-on Mac running the INKBIRD app; watchdog drives set point changes via adb UI automation. Play Store-image route (official channel) since APK sideloading was ruled out. SDK installing at `~/android/` on davids-mbp-2.
- [ ] Inside the emulator, first retry the two shortcuts that could still unlock the clean Tuya cloud API: Tuya Smart app login with INKBIRD credentials, and the Android INKBIRD app scanning the link QR via virtual camera.
- [ ] Davey: provide INKBIRD app login (via hidden-input command), be ready for a possible Google 2FA tap for Play Store sign-in
- [ ] Claude: calibration pass, supervised set point cycle, then arm (`touch ~/.config/ee-stove-watchdog/armed`)

## Known limits

- Tuya IoT trial subscription expires every ~6 months; renewing is a 2-click thing at iot.tuya.com when API calls start failing.
- Outside 6:30am–10pm the watchdog does nothing by design.
