# Occupancy Watcher (Deck vs Bookings)

Built 2026-09-19. Counts guests on the deck cameras every 10 minutes, compares to seats booked in Periode for that session, and Slacks an alert when more people show up than booked.

## How it works

| Piece | Source |
|---|---|
| Bookings | Periode's notification emails to sauna@ ("New Booking", "Booking moved", "Cancelled booking"). Each has the booking ID in its admin link, so the script keeps a ledger keyed by ID and the latest email wins. The merchant API doesn't expose single-session bookings, the emails do |
| Headcount | Snapshots from Wired Floodlight 23BJ, Lounge and Ebb boat, read by headless Claude (sonnet). It de-dupes people across cameras and splits guests (swimwear, towel, robe) from clothed people (staff, Grant's crew, dock walkers) |
| Alerts | Slack bot (same token as the stove watchdog). Frames attached so you can check it in two seconds |

## Alert rules

Changed 2026-09-22 per Davey: alerts only when there are more people than there should be, posted to #periode, tagging Davey and Jonah.

- **The one rule:** guests on camera > seats booked (0 when nothing is booked), on 3 sweeps spanning at least 20 minutes. The 20-minute part is deliberate: sailboaters cut through the deck to use the restroom and are gone in 5, guests settle in. One alert per session, or per 2-hour block when nothing is booked.
- Street clothes never count as guests, so a boater walking through in a jacket is "clothed" and ignored either way.
- **Monday Banya quiet block:** Mondays 4:45pm to 9:30pm are logged but never alerted. Danesh's Banya sessions don't go through Periode, so the ledger reads them as unbooked (that's what fired 4 alerts on 2026-09-21).
- **Boat watch (added 2026-09-22):** the vision pass also reports any boat/dinghy/kayak/jet ski tied off or holding at the swim float or alongside the sauna boat (marina slips and the channel don't count). If it's still there on the next sweep (2 in a row, ~10 min) it alerts, any time of day, Banya block included. One per 2-hour block. Weekend boaters walking into the sauna off a boat was the trigger for this.
- Sunrise, sunset, moonlight, equinox and any other Periode product are covered automatically, the ledger doesn't care about product name (Private Sauna is the only special case, 10 seats). Banya is the gap: it isn't in Periode, so there's nothing to compare against.
- First 15 min and last 5 min of each session are ignored. Groups overlap at turnover and it would false-alarm all day.
- Private Sauna bookings count as 10 seats.
- Daily summary is off (`daily_summary: true` in config.json turns it back on).

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

Alerts go to #periode (`C0BJR4XS03V`). To move them: `{"slack_target": "C0XXXXXXX"}` in `config.json` (the Claude bot has to be in that channel). Who gets tagged: `"mention": ["U0B1CAVT1TM", "U0B1H0WRHJ8"]` (Davey, Jonah).

## Open items

- The always-on Mac went offline 2026-09-19 ~5pm to 2026-09-20 9:16am (asleep or off network, not rebooted), so nothing was watched overnight and the Sunday 7am unbooked group (stills in `Incidents/`) was only found by hand afterward.
- Lounge and Ebb boat are battery cams. 90+ snapshots a day each will drain them faster than normal, watch the battery level in the Blink app for the first two weeks. If it's ugly, drop those two to every other sweep.
- Bookings Jonah or staff create in the Periode admin: confirmed they generate the same email? Unverified. If not, those sessions will read as over.
- The Ebb boat cam still has two pilings down the middle of frame (see Camera Coverage Review). Re-aiming it would help this count more than anything else.
