# Stove Watchdog — Inkbird Auto-Relight

Automated fix for the misfire problem: when the sauna drops below 162°F during working hours, the watchdog checks the stove cam, and if the flame is out it cycles the Inkbird set point (190 → 90 → 190) to force a re-ignition, then verifies the flame relit on camera. Retries every 5 minutes until it works. Davey gets a Slack DM when it misfires and again when it's confirmed relit.

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
- [ ] Davey: create Tuya IoT account, link INKBIRD app by QR, run the Desktop setup script
- [ ] Claude: calibration pass (`probe`), confirm live temp read + set point write, then enable the launchd job

## Known limits

- Tuya IoT trial subscription expires every ~6 months; renewing is a 2-click thing at iot.tuya.com when API calls start failing.
- Outside 6:30am–10pm the watchdog does nothing by design.
