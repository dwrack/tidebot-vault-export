# IG Posting Phone (Android on davids-mbp-2)

Why: trending/licensed songs (e.g. "The Night We Met") can only be added inside the Instagram app. No API or scheduler can do it. A dedicated Android plugged into the always-on Mac lets Claude post reels with in-app music on a schedule.

@doorcountykayaktours is a **Creator** account (same as @saunacamps), so it has the full music library. Don't switch it to Business; that cuts the library to royalty-free only.

## Buy (David)
- **Google Pixel 6a or 7a, used/unlocked, ~$100-150.** Stock Android is the easiest to automate. Any carrier is fine; no SIM needed, Wi-Fi only.
- A USB-C cable that fits davids-mbp-2's ports (check if it has USB-C or USB-A).

## One-time setup (about 10 min, David or whoever is at the always-on Mac)
1. **Factory reset first** (used phones came from a reseller farm; this gives a fresh Android ID + advertising ID and drops the prior-owner accounts). Then connect to Wi-Fi and sign in with the Google account of the phone's brand family (see Fingerprint rules below).
2. Settings > About phone > tap **Build number** 7 times to unlock Developer options.
3. Settings > System > Developer options: turn on **USB debugging** and **Stay awake** (screen stays on while charging).
4. Plug into davids-mbp-2 and tap **Allow** on the "Allow USB debugging?" prompt (check "Always allow from this computer").
5. Install Instagram from the Play Store and log into **@doorcountykayaktours** (David handles the login and any 2FA).
6. Settings > Display: set screen timeout to max; turn off the lock screen (Security > Screen lock > None).
7. Tell Claude it's plugged in. Claude checks it with `~/android/platform-tools/adb devices`.

## Already done
- 2026-10-08: Android platform-tools (adb 37.0.1) installed on davids-mbp-2 at `~/android/platform-tools/` and added to PATH.

## How posting will work (Claude builds this after setup)
1. The approved video is pushed to the phone's camera roll over USB.
2. Claude drives the Instagram app (Reels > pick video > Add audio > search the song > set the start point > caption > Share) by reading the screen layout and tapping. No guessing pixel positions.
3. **Approval gate:** each reel posts only after David approves that exact video, caption and song. The script stops before Share otherwise.
4. Every post is logged with a screenshot of the final screen.

Fallback if Instagram changes its UI and breaks the flow: Lea posts by hand from the same prepped files.

## Phones connected (2026-10-10)
| Name | Model | Serial | Android | Status |
|---|---|---|---|---|
| moto | Moto G Play 2024 (XT2413V) | ZY22KTCGZC | 14 | Paired. Drops off when Wireless debugging turns off |
| tcl | TCL T434D | NRVGQWD6WCLV9TWW | 14 | Paired + connected |
| galaxy | Samsung Galaxy A15 (SM-S156V) | R5CXC3B1R4H | 14 | Paired + connected 2026-10-10 |

- Connected over **Wireless debugging** (the USB cable at the always-on Mac didn't carry data). Pairing is saved; if a phone drops, just turn Wireless debugging back on.
- `~/android/reconnect.sh` runs every 5 min via launchd `com.djl.adb-reconnect` on davids-mbp-2 and reconnects any paired phone it sees.
- Control a phone with `~/android/p moto|tcl|galaxy ...` (picks it by hardware serial, so changing ports don't matter).
- Each phone still needs its own Google account (David creates it) before the Play Store installs Instagram. Then assign brands per phone using the family allocation below (the IG app holds up to 5 accounts). Lock the family BEFORE the first login; it can't be undone.

## Cleanup 2026-10-12 (verified)
Backups of every device's DCIM/Pictures/Download/Music are on davids-mbp-2 at `~/android/backups/2026-10-12/<device>/`.

| Device | Before | After | Removed |
|---|---|---|---|
| tcl | 27% | 21% | 16 apps (carrier games, Cash App, TextNow, 1Weather, VoidFix SMS gateway), leftover APKs, old photos |
| galaxy | 31% | 21% | 28 apps (games, Cash App, Pandora, Outlook/Office, Tracfone, VoidFix, Samsung Pay/Health/AR Zone/SmartThings/Wearable/Kids Home/Global Goals/Samsung Free, YouTube Music), old music + photos |
| moto | 31% | 24% | 19 apps (games, Cash App, DT Ignite carrier installer, Fitness, Tracfone, VoidFix), old photos |
| taba1 (Tab A) | 87% | 37% | all 15 third-party apps (kids games, Spotify, Amazon Video, SwipeSimple, Homebase, iWaivers, Yelp, TripAdvisor, Alaska), 3.9GB Netflix downloads, 2017-2021 screenshots |

Kept on purpose: MacroDroid, Aurora Store, TikTok, Facebook, Pinterest, Google Photos, Maps, Wallet, Google basics. Caches trimmed on the three Android 14+ phones (`pm trim-caches` is not allowed over adb on the Tab A's Android 7).

Flag: all three posting phones shipped with the same `VoidFix Solution.apk` (May 2025) plus `org.voidfix.smsgateway`, an SMS-forwarding app, from before David owned them (reseller bulk load). Uninstalled; copies in the backup folder if ever needed.

Still pending: moto2 and taba2 were offline during the cleanup (run the same pass when they reconnect); the two prior-owner Google accounts (tracysmilesalot9@, j84153448@) stay until David adds the brand accounts.

## Fingerprint rules (added 2026-10-12)
Full note: `TheBrain/06 Learning/Device Fingerprinting — Posting Phone Rules (Oct 2026).md` (from royfish.dev "Fingerprints are the new cookies"). Short version:
- A phone is one fingerprint (GPU, CPU, screen, audio, model, fonts, time zone, Android/advertising ID). Reinstalls, new accounts, and VPNs don't change it. Every account that logs in on a phone is permanently linked to the others on it.
- So: group accounts by blast radius (same entity + region per phone), never move an account between phones, never put personas or experiment accounts on a brand phone.
- Stay boring: stock, un-rooted, Play Store only, no spoofers, no VPN, time zone/locale left automatic so they agree with the IP (a Pacific clock on a Wisconsin IP is the VPN tell). Spoofing makes a phone rarer, not safer.
- Behavior counts too: stagger posts across accounts by hours, vary captions, don't fire the same file to 5 accounts in one minute.

Proposed families (pending David): moto = Door County · galaxy = NOLA · tcl = Texas · moto2 = E&E + NOLA Bike Bar + Houston Booze Cruise · tablets = TikTok mirrors of the same families.
Before brand logins: factory reset each phone, remove Aurora Store (non-Play install source is a rare signal), keep MacroDroid only if it never touches IG/TikTok.
- Account creation: no two phone families share a name, email, recovery email/phone, birth date, card, or creation device. Create each account on its own phone, one family per day. Per-family values go in a local-only file on mbp-2, never the vault. Table in the TheBrain note.
