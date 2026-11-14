# Boat Cam v2 — Hardwired, Hands-Off Build Spec

*Written 2026-11-13. Supersedes the capture half of `Boat Cam Content Pipeline — Setup & Run Book.md` (Aug 2026). The processing half (`/boatcam` detect, sheets, cut) is unchanged and this design feeds it.*

## What David asked for

A camera wired to the boat battery that records all day while the boat is on, and when the boat gets back to the dock the video files upload themselves. No cradle, no SD card pulls, no captain remembering anything. Really good quality video. He will build it.

## The design in one paragraph

A GoPro HERO13 Black does the filming (that is where the picture quality comes from). A Raspberry Pi 5 in a sealed box on the boat is the brain: it powers the GoPro over USB, tells it to start when the key turns on and stop when the key turns off, then pulls the day's files off the camera over the same USB cable onto its own SSD, runs the `/boatcam` scrubbing itself overnight, and pushes the candidate clips and contact sheets to davids-mbp-2 over Tailscale when it sees the dock Wi-Fi. The whole rig hangs off the house battery behind a low-voltage disconnect so it can never strand the boat.

Why not the Aug plan (GoPro Premium cloud upload from a cradle): it needs a human to dock the camera every night, GoPro's own Wi-Fi upload is 2 to 10 MB/s so a full day (100 to 160 GB) takes all night or longer, and there is no clean API to get footage from GoPro's cloud back to our Mac. Wired USB to a Pi fixes all three.

Why not an IP / security camera: it never overheats and records straight to a drive, but the footage looks like evidence footage (flat color, no HDR, fisheye, no stabilization). The whole point is content. Keep it as the fallback if the GoPro cannot take the summer heat.

## Why the Pi does the scrubbing on the boat

The real bottleneck is not the camera, it is the marina's upload speed. A full day of 4K is 100 to 160 GB. On a typical 20 to 50 Mbps business upload that is 7 to 18 hours a night, every night. It does not fit.

So the Pi keeps the full footage on its own 1 TB SSD (about 6 days of shifts, rolling), runs `boatcam detect` on it overnight, and uploads only the top 20 to 30 candidate windows plus contact sheets: 1 to 3 GB. That works on any marina connection, even an LTE hotspot in the box if the marina Wi-Fi turns out to be bad. If a full raw file is ever wanted, pull it from the Pi over Tailscale.

## Hardware (one boat)

| Part | Pick | Approx | Notes |
|---|---|---|---|
| Camera | GoPro HERO13 Black | $350-400 | Open GoPro API over USB (wired control + media download, ~30 MB/s). 8:7 full-sensor mode crops to 9:16 reels without losing height. |
| Card | 512 GB microSD, V30/U3 (SanDisk Extreme or Samsung Pro Plus) | $50-60 | ~18 hours of 4K before the Pi has to clear it. |
| Mount | Hard mount above head height, forward-facing, plus a small sun hood | $40-60 | RAM ball + GoPro adapter, through-bolted. No housing: airflow is the heat fix. |
| Brain | Raspberry Pi 5 (8 GB) + active cooler | $90 | Hardware HEVC decode handles GoPro 4K for scene detection. |
| Storage | M.2 HAT+ or Pimoroni NVMe Base + 1 TB NVMe | $90 | SD cards die under constant video writes; NVMe does not. |
| USB hub | Powered USB 3 hub with 12 V input (industrial / DIN-rail style) | $40-60 | GoPro draws up to 2 A on USB; the Pi cannot supply that. Hub feeds the GoPro power, passes data to the Pi. |
| Pi power | Wide-input (6-36 V) 12 V to 5 V 5 A buck with USB-C PD, sealed | $25 | Wide input rides through starter-crank dips without rebooting the Pi. |
| Protection | Victron Smart BatteryProtect 12/24 65 A (or Blue Sea 7635 LVD), set to 12.0 V cut | $55-65 | Hard guarantee the rig cannot drain the house bank. |
| Ignition sense | Optocoupler module (12 V in, 3.3 V logic out) on a Pi GPIO | $8 | Tells the Pi "boat on / boat off." Wire to the ignition-switched circuit. |
| Box | IP67 polycarbonate enclosure (Polycase WC-22F class), 2 cable glands, 10 A inline fuse, marine tinned wire | $70 | Mount inside the console or under the canopy, out of direct sun. |
| Dock side | Nothing new if marina Wi-Fi reaches the slip. Else an outdoor AP on the office connection, or an LTE hotspot in the box. | $0-120 | Needs a speed test at the slip first (see open items). |
| **Total** | | **~$850-1,000** | Plus a second GoPro body in the budget by year two; heat and salt eat them. |

No GoPro Premium subscription needed.

## How a day runs

1. **Key on.** Ignition sense goes high. Pi boots (about 20 s), hub powers the GoPro, Pi sends `start recording` over Open GoPro USB. GoPro chapters files every ~4 GB, so a crash never loses more than ~10 minutes.
2. **All day.** GoPro records to its card. Pi logs health (camera temp, free space, battery voltage) once a minute. Nothing else.
3. **Key off.** Pi sends `stop recording`, waits for the file to close, then downloads every new file off the camera over USB (full day: 60 to 90 minutes), checks sizes, deletes them from the card, powers the GoPro down through the hub.
4. **Overnight.** Pi runs `boatcam scan` and `detect` on the day's files (expect 10 to 15 min per hour of 4K on a Pi 5, so a 6-hour day finishes well before morning), builds contact sheets, and queues the candidate windows as short raw cuts.
5. **Upload.** Whenever the dock Wi-Fi (or hotspot) is up, `rsync` over Tailscale pushes the queue to davids-mbp-2 `~/BoatCam/inbox/npb/<date>/`. Existing `/boatcam` sheets + cut + `/social-captions` steps take it from there. Slack summary to David: "Nov 14: 5 h 50 m recorded, 24 candidates, sheets ready."
6. **Shutdown.** Pi halts with `POWER_OFF_ON_HALT=1` (near-zero draw). The LVD is the backstop if anything hangs.

Full raw files stay on the Pi 6 days, then roll off. If the key turns on again before the overnight job is finished, recording takes priority and the job resumes at the next key-off.

## GoPro settings

- 4K, 8:7, 30 fps, HEVC. About 27 GB/hour. If heat is a problem: 2.7K 8:7 first, then 1080p.
- HyperSmooth off (hard mount) or Standard at most; it is the biggest heat and battery cost.
- Screen off, GPS off, Wi-Fi off (USB does the work), beeps off, auto power-off never.
- USB connection mode: GoPro Connect (not MTP), or Open GoPro cannot see it.
- Battery OUT in summer (runs as a battery eliminator on USB power, noticeably cooler). Battery in during cool months as brown-out insurance.
- Audio records; the pipeline strips it by default. Keep it that way (guest conversations).

## Risks, in order

1. **Heat.** A GoPro recording 4K for three straight hours in a Louisiana July will thermal-shutdown unless it has airflow and conservative settings. Mitigations above. It is November, so a test now proves nothing; treat May as the real test, build with the fallbacks ready (drop resolution, then IP cam).
2. **Marina internet.** If the slip has no usable Wi-Fi, the LTE hotspot route still works because the upload is only a few GB a night.
3. **Mid-trip downloads.** Open GoPro blocks media operations while encoding, so the day's pull happens after key-off. Test once whether finished chapters can be pulled while recording; if they can, the post-trip pull shrinks to minutes.
4. **Salt and vibration.** Sealed box, glands, tinned wire, a drop of Loctite on the mount. Budget a replacement GoPro body per season.
5. **Consent.** Unchanged from the run book: nothing posts without the photo/video release in the booking flow, no minors, no phone screens, audio off.

## Build order

1. Order the parts. (David)
2. Speed test at the slip on the marina Wi-Fi, both directions, phone is fine. (Jeff)
3. Bench build at home: Pi + hub + GoPro on a 12 V power supply, run the software end to end against a fake "ignition" switch. (David + Claude writes the software)
4. Install on one boat (the one Jeff was re-powering the old camera on; it already has the outlet conversation started). Wire: fused always-live from the house bank into the LVD, LVD out to the buck and hub, ignition-switched wire to the optocoupler.
5. Two weeks of shifts, watch the Slack summaries, then decide on boats two through four.

## Software (Claude builds)

Repo `~/Projects/npb-boatcam-edge`, runs on the Pi as a systemd service:

- `ignition.py`: GPIO watcher, state machine (OFF, RECORDING, OFFLOADING, PROCESSING, IDLE).
- `gopro.py`: Open GoPro wired HTTP client: start/stop, media list, download with resume, delete, camera status and temperature.
- `offload.py`: pull, verify, delete, write a manifest per day.
- `boatcam.py`: the existing detector, ported to run here (same scoring, same JSON).
- `sync.py`: rsync over Tailscale to mbp-2 inbox, retry forever, Slack summary when done.
- Health: a one-line heartbeat to mbp-2 so the existing `/system-map` sweep shows it.

Secrets (Tailscale auth key, Slack token) live on the Pi in `/etc/npb-boatcam/env`, never in this vault.
