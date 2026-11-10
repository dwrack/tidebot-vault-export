# Decisions Queue

The one input for the morning decision tap. The 5:45am PT `com.djl.chief-of-staff` run on mbp-2 reads this table through `python3 ~/.claude/scripts/decision-queue.py today --commit`, takes up to 3 open rows whose `day` is today or earlier, ranks physical then money then people then digital, and puts them in the Slack DM (and the DJL Morning Digest page when that tool is available). Each row carries its standing default. When a row has been shown twice with no answer, the default fires (status `defaulted`) and it is logged under handled. Money rows with `default` = `none` never fire; they come back until answered.

**Add a decision:** append a row. `id` is the next D-number, `day` is the first morning it may appear, `kind` is one of physical / money / people / digital, `options` are separated by ` ; ` with the recommended option first. Leave `shown` at 0 and `answer` blank.
**Answer one:** click the option on the Morning Digest tab of the DJL Command Center window, or put the option letter in `answer` (a, b, c), and the row stops appearing. Replying to the Slack DM with "D1a" works too; the next desktop session copies it here. The 5:45am run acts on answered rows and sets them to `applied`.
**Statuses:** open, answered, applied, defaulted, dropped.

| id | day | kind | decision | options (rec first) | default if skipped twice | shown | answer | status |
|---|---|---|---|---|---|---|---|---|
| D1 | 2026-11-01 | people | NOLA captain / assistant-manager role: post it (Indeed, FB, Craigslist) | (a) post Tue Nov 3 ; (b) post today ; (c) hold a week | post Tue Nov 3 | 2 |  | open |
| D2 | 2026-11-01 | money | Bike Bar sale: send Michael the four questions | (a) Claude drafts today, David sends Mon ; (b) send today ; (c) hold | Claude drafts, David sends Mon | 2 |  | defaulted |
| D3 | 2026-11-01 | digital | DCKT Astro swap: go / no-go for cutover wk of Nov 9 | (a) hold, recheck Nov 7 ; (b) go, cutover wk of Nov 9 ; (c) drop the swap | hold, recheck Nov 7 | 2 |  | open |
| D6 | 2026-11-02 | money | HPB June 6 refund, $927 (policy backs it) | (a) refund in full ; (b) partial credit ; (c) deny per policy | none | 8 |  | dropped |
| D5 | 2026-11-02 | money | BBK Meta awareness + HPB Followers Reboost: pause (~$990/mo, 0 purchases) | (a) pause both ; (b) pause BBK only ; (c) keep running | none | 8 |  | dropped |
| D7 | 2026-11-02 | people | NKST lead guide: Stephanie vs Michelle | (a) Stephanie (8 tours, 5 review mentions) ; (b) Michelle ; (c) co-leads | Stephanie | 1 | no one (david 11/2: no lead guide) | dropped |
| D4 | 2026-11-03 | money | Better Loans $190k | (a) take it ; (b) counter on terms ; (c) pass | none | 8 |  | open |
| D8 | 2026-11-05 | digital | NKST: close the 2:00 PM Manchac tour Monday to Thursday through February. 4 guests in 13 runs since Oct 15, and Tue and Wed sold zero. Only dates with no bookings get closed | (a) close Mon to Thu 2 PM ; (b) close Tue and Wed only ; (c) keep it daily | none | 0 |  | open |
| D9 | 2026-11-05 | digital | NKST: run the 9:30 AM Extended Manchac Friday to Sunday only through February. 9 guests in 13 weekday runs, 10 ran empty, and it pulls guests off the 9:00 AM tour next to it. Only dates with no bookings get closed | (a) Fri to Sun only ; (b) Fri and Sat only ; (c) keep it daily | none | 0 |  | open |
| D10 | 2026-11-05 | digital | NKST: run the Whitney Plantation combo Saturday and Sunday only, and remove the duplicate 8:30 AM slot. 1 guest in 8 weekday runs, 21 of its 27 guests came on Sundays, and the 8:30 sold zero. Only dates with no bookings get closed | (a) Sat and Sun only, drop 8:30 ; (b) only drop the 8:30 ; (c) keep as is | none | 0 |  | open |
| D11 | 2026-11-07 | digital | NKST email capture + drip funnel (your 11/5 window note). Nothing is live on NKST: the April lead-magnet form died with GHL, the Funnel Lab quiz/popup is still drafts. Fastest path is cloning the NPB newsletter funnel (live since 10/22, code-free) onto the NKST site. The 3 WIP slots are full through Nov 15 | (a) start now, swap it in for DCKT Astro on Sunday (Astro is on hold anyway) ; (b) queue it, start Nov 16 ; (c) skip it | queue it, start Nov 16 | 0 |  | open |
