# system-map, all brands (2026-11-13)

Run 2026-11-13T13:30:06 from the Command Center skills panel. Read-only; nothing was sent or changed.

David's note: test run, keep it very short


BOTTOM LINE: I couldn't run a live scan this time because shell access was denied. The last saved map (2026-11-07) reported 138 high, 189 medium and 69 low findings. Most of the high ones are jobs enabled on both the laptop and davids-mbp-2.

ACTIONS:
- Re-run `sysmap.py --findings` on mbp-2 to get a live scan. Claude does this, and it needs shell access that this test run didn't have.
- Check the double-active jobs live with `launchctl list | grep`. Start with the ones that send or post: `com.davidrack.engage`, `com.bikebar.socialposter`, `com.davidrack.dckt-carousel-drip` and `com.admirenola.clean-post`. Claude checks, then David approves disabling the laptop copies.
- Fix or retire `com.djl.idea-radar` on the laptop. Its script `/Users/davidrack/idea-radar.js` is missing. Claude does this once David approves.
- Add the laptop copies that are meant to stay on to `laptop-ok.txt` so they stop flagging. Claude does this.

DETAIL:
- The 11/7 report shows the laptop and mbp-2 both with 137 enabled jobs and 34 disabled. That near-identical count looks like duplicated plists, not 137 separate loops.
- The `double-active` rows in the first 25 findings are jobs enabled on both Macs. Examples are `docuseal-backup`, `docker-desktop`, `maps-rank`, `competitor-watch` and the Admire NOLA jobs. Some of these may be harmless, since the laptop sleeps and some jobs only back up or probe. Others would double-send or double-post.
- I didn't verify any of this live. Both the 11/7 numbers and the "double-active" flags are leads, not confirmed failures.
- I did not check the DCKT Mac's state beyond the 11/7 report, which showed 2 jobs and 4.5 days uptime. I also did not check drift since 11/7 or log freshness.
