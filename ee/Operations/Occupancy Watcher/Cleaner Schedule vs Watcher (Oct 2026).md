# Cleaner schedule vs occupancy watcher (Oct 2026)

Source: calendar Jonah posted in #periode 2026-11-03. LR = regular cleaning, DC = deep clean (Jonah's read).

## October 2026 cleaning days
- Mondays: LR every week (10/5, 10/12, 10/19, 10/26)
- Fridays: LR 10/2, 10/16, 10/30; DC 10/9, 10/23 (deep clean every other Friday)
- Saturdays: LR every week (10/3, 10/10, 10/17, 10/24, 10/31)

## What the cameras show (log.csv on mbp-2, 9/26 to 11/2)
- Monday: cleaner arrives about 9:30pm after Banya, mopping visible 9:35 to 10:07pm on 11/2, clothed-only sweeps 9:06 to 9:17pm on 10/19, 9:14pm on 10/12, 8:58pm on 10/5. This is the only cleaning inside watcher hours (6:45am to 10:15pm).
- Friday and Saturday: last session ends 10pm, nobody but session guests on deck 9pm to 10:13pm, next-morning 6:45 to 7:30am sweeps are clear. Cleaners work after 10:15pm, outside watcher hours. Zero Fri/Sat alerts in 5 weeks.
- DC Fridays (10/9, 10/23): nothing visible in watcher hours either.

## Alerts fired since 9/26
Tue 9/29 (2), Sun 10/11 9pm session, Tue 10/20 1:29pm, Mon 11/2 9:45pm (the cleaner). Only the Monday one is cleaning-related.

## Fix status
- 2026-11-03: Jonah said go in #periode. Patch applied to the vault copy of occupancy.py (this folder), compile-checked. NOT yet on mbp-2: the Slack bridge is read/draft only, so Davey deploys.
- Deploy (from the laptop, one line):
  `scp "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Ebb and Ember/Operations/Occupancy Watcher/occupancy.py" davidrack@100.113.229.1:~/ee-occupancy/occupancy.py`
  No launchd restart needed; the next 10-min run picks it up. Verify: `ssh davidrack@100.113.229.1 "grep -n '22:15' ~/ee-occupancy/occupancy.py"`.
- What changed: Monday quiet block end 21:30 -> 22:15 (CONFIG default), and quiet-block sweeps now reset the over-count streak instead of accumulating toward an alert after the block.

## Proposed fix (as discussed 2026-11-03)
1. Monday quiet block 16:45 to 22:15 (was 16:45 to 21:30).
2. Reset the unbooked streak at a quiet-block boundary.
No change needed for Friday or Saturday. Re-check if the cleaners move to a daytime slot or the schedule changes in November.
