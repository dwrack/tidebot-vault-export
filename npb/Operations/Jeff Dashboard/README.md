# Jeff Today page

Page: https://npb-dash-zoonn3.pages.dev/jeff/ (link only). David's twin: /david/ (needs `david-queue.json` here).

- `jeff-queue.json` = what shows on the page. Any Claude edits it (add items, set `status` to working/done, write a `reply`). The always-on Mac pushes it live every 10 min (launchd `com.djl.jeffq`, script `~/Projects/jeffq/jeffq.py`; source on David's laptop in `~/Projects/npb-dashboard-site/jeffq.py`).
- `Jeff Answers.md` = everything Jeff taps or types, appended every 10 min. Claude: read it at the start of any NPB session, act, then update the queue.
- Item fields: id, area, title, why, due, mins, plan (how Claude can take it), options (first one is the recommended button), ask (optional question), status, reply.
- Keep it to about 15 open items. One clear action each. Built 2026-11-13.
