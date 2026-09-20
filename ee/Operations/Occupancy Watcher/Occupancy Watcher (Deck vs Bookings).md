# Occupancy Watcher (Deck vs Bookings)

Built 2026-09-19. Counts guests on the deck cameras every 10 minutes, compares to seats booked in Periode for that session, and Slacks an alert when more people show up than booked.

## How it works

| Piece | Source |
|---|---|
| Bookings | Periode's notification emails to sauna@ ("New Booking", "Booking moved", "Cancelled booking"). Each has the booking ID in its admin link, so the script keeps a ledger keyed by ID and the latest email wins. The merchant API doesn't expose single-session bookings, the emails do |
| Headcount | Snapshots from Wired Floodlight 23BJ, Lounge and Ebb boat, read by headless Claude (sonnet). It de-dupes people across cameras and splits guests (swimwear, towel, robe) from clothed people (staff, Grant's crew, dock walkers) |
| Alerts | Slack bot (same token as the stove watchdog). Frames attached so you can check it in two seconds |

## Alert rules

- **Session over:** guests on camera > seats booked, on 2 sweeps in the same session. One alert per session.
- **Unbooked:** 1+ guests on the deck on 2 sweeps in the same hour with no session within 20 min either side.
- First 15 min and last 5 min of each session are ignored. Groups overlap at turnover and it would false-alarm all day.
- Private Sauna bookings count as 10 seats.
- Daily summary at 10:15pm: booked vs peak seen, per session.

## The honest limit

Nothing sees inside the sauna, so the camera count is a floor. If 6 booked and 3 are inside, we see 3. That means:

- An "over" alert is solid. We literally saw more guests at once than seats sold.
- It will miss some. A party of 4 on 2 seats only trips it if 3+ are on the deck together in a frame.
- It can't detect no-shows. Low count doesn't mean they didn't come.

Every sweep is logged to `log.csv`, which is the dataset the parked occupancy-vs-bookings analysis needs once V2 is on the water.

## Where it lives (always-on Mac, davids-mbp-2)

- Script: `~/ee-occupancy/occupancy.py` (canonical copy: this vault folder, deploy with scp)
- launchd: `com.ebbember.occupancy-watcher`, every 600s, sweeps 6:45am to 10:15pm Pacific
- Config overrides: `~/.config/ee-occupancy/config.json` (any key from `CONFIG` in the script)
- State + ledger: `~/.config/ee-occupancy/state.json`, `bookings.json`
- Logs: `~/ee-occupancy/occupancy.log`, `log.csv`, frames in `snaps/` (about 2 days kept)
- Reuses: stove watchdog venv, Blink creds `~/.config/blink-ee/creds.json`, sauna@ Google token, bridge's Claude setup-token

## Ops

```
ssh davidrack@100.113.229.1
cd ~/ee-occupancy && ~/ee-stove-watchdog/venv/bin/python occupancy.py today     # today's sessions + seats
... occupancy.py sweep       # one count right now, no alert
... occupancy.py summary     # send today's summary now
... occupancy.py test-alert
launchctl bootout gui/501/com.ebbember.occupancy-watcher                         # pause
launchctl bootstrap gui/501 ~/Library/LaunchAgents/com.ebbember.occupancy-watcher.plist   # resume
```

Send alerts to a channel instead of Davey's DM: put `{"slack_target": "C0XXXXXXX"}` in `config.json` (the Claude bot has to be in that channel).

## Open items

- Alerts go to Davey's DM while it calibrates. Move to a team channel once a few days of alerts look right.
- Lounge and Ebb boat are battery cams. 90+ snapshots a day each will drain them faster than normal, watch the battery level in the Blink app for the first two weeks. If it's ugly, drop those two to every other sweep.
- Bookings Jonah or staff create in the Periode admin: confirmed they generate the same email? Unverified. If not, those sessions will read as over.
- The Ebb boat cam still has two pilings down the middle of frame (see Camera Coverage Review). Re-aiming it would help this count more than anything else.
