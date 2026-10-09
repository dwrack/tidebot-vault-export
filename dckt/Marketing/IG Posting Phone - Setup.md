# IG Posting Phone (Android on davids-mbp-2)

Why: trending/licensed songs (e.g. "The Night We Met") can only be added inside the Instagram app. No API or scheduler can do it. A dedicated Android plugged into the always-on Mac lets Claude post reels with in-app music on a schedule.

@doorcountykayaktours is a **Creator** account (same as @saunacamps), so it has the full music library. Don't switch it to Business; that cuts the library to royalty-free only.

## Buy (David)
- **Google Pixel 6a or 7a, used/unlocked, ~$100-150.** Stock Android is the easiest to automate. Any carrier is fine; no SIM needed, Wi-Fi only.
- A USB-C cable that fits davids-mbp-2's ports (check if it has USB-C or USB-A).

## One-time setup (about 10 min, David or whoever is at the always-on Mac)
1. Connect the phone to Wi-Fi and sign in with a Google account (a DCKT Google account is fine).
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
