# E&E Incident Log (automated)

Backs the safety plan's "incidents reach management the same day" promise for the Capitol Specialty liability policy.

- **Sheet:** [E&E Incident Log](https://docs.google.com/spreadsheets/d/19GwwkJdwBB103Z6yHQu1NOysvkwN2hvysjAFnAuMQ3I) (davey@ owns, Jonah edits). Edit Action taken, Status, Notes by hand.
- **Runs on:** davids-mbp-2 `~/ee-incident-log/` every 15 min, 24/7 (launchd `com.ebbember.incident-log`). Reuses the in-flight watcher's readers in `~/ee-inflight-watch/watch.py`.
- **Reads:** the watcher's 13 Slack channels, sauna@ and davey@ email (Google Voice texts and voicemails arrive there), Davey's iMessages (watcher's people + keywords).
- **Alerts:** #founders (Davey + Jonah). Fire/gas any hour; other action-needed items 7am to 10pm, overnight ones held to 7am. Guest names and numbers only in the Sheet.
- **Fixes:** posted for Alex in #maintenance as "New job for the list" with scope questions; never for reports that came from #maintenance.
- **Weekly:** Monday 8am in #founders: counts, open items, up to 3 lessons.
- **Dashboard:** Command Center E&E tab, "Safety incidents" section.
- **Failures:** DM to Davey only (2 failed runs in a row per source; watchdog if no run in 45 min; DCKT Mac `com.ebbember.mbp2-alive` if mbp-2 itself is down for 60 min).
- **Pause:** set `"dry_run": true` in `~/ee-incident-log/config.json` on mbp-2.
- **Flags:** `--dry-run`, `--no-post`, `--lookback-hours N`, `--test-file PATH`, `--fail-test`, `--weekly`.
- **Gaps:** incidents told only by phone or in person never hit a channel. Staff rule for the safety plan: post every incident in #maintenance.
- Decision record: `TheBrain/07 Reference/Decisions/2026-11-06 E&E incident log.md`. `code/` here is a copy; deploy from it to mbp-2.
