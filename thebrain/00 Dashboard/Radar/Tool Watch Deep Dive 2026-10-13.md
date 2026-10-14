# Tool Watch Deep Dive (2026-10-13)

One-time catch-up on what shipped May to Oct 2026. From here on, the Monday radar has a "Tool Watch" section that does this automatically.

Tags: **[V]** = read on the vendor's own page. **[U]** = third-party source only, confirm before spending money.

## Do these first (biggest $ or hours)

| # | What | Action | Brands |
|---|---|---|---|
| 1 | **Google AI books & calls businesses for searchers** (I/O, May 19). Louisiana reportedly excluded from the calling feature. [U] | Check GBP > Advanced > "Google automated calls and text messages" on every profile. Put real prices + hours on GBP, no "call for quote." Make sure the OpenCX phone agent handles a robot caller. | All TX + WI brands. NOLA brands: check anyway |
| 2 | **Viator is inside Gemini** (Jul 30) and **GetYourGuide is inside Gemini, ChatGPT and Claude** (Sep 15). AI assistants now send tour bookings through OTAs first. [V] | Decide per brand: list on Viator/GYG (eat commission, get AI visibility) or not. If already listed, refresh photos, copy, reviews. GYG has a free listing-quality checker. | Every tour brand |
| 3 | **FareHarbor Agent** (Apr 27, limited rollout): AI answering phone, email, chat, SMS, IG, WhatsApp with live availability. [V] | Ask the FareHarbor rep for access + price. Compare cost per resolution with OpenCX (~$0.75-0.90/ticket [U]). Use it as OpenCX pricing leverage even if you don't switch. | All FH brands |
| 4 | **Google Ads auto-promotions** (opt-out started Oct 12): Google can invent discounts on Search/PMax campaigns with location assets. [U] | Opt out on every campaign today unless you want Google setting promos. | Every Google Ads account |
| 5 | **Meta image-to-video GA + bigger Ads MCP** (Oct 6). [U] | One test per brand: best static ad turned into video vs the static as control. | NPB, HPB, DCKT first |
| 6 | **Claude Sonnet 5.5 + Haiku 5.5** (Sep 28 / Oct 7). Haiku is now the cheap default for subagents. [V] | Already fine: headless loops use `--model sonnet`, which picks up 5.5. Nothing pins the retiring Sonnet 4.5 (retires Nov 30). Verified today. | n/a |
| 7 | **Monthly API credits for Max/Team plans** (Oct 7): link a Console org, get free API credit every month. [V] | Claim it. Free money for scripted jobs. | n/a |

## Claude features you're probably not using yet

- **`/usage` + `/skill-doctor`**: shows which of your ~40 skills and ~30 MCP servers eat context and plan limits. Run it once; prune the heavy ones. Probably the best 10 minutes on this list.
- **Routines** (cloud scheduled agents): run jobs in Anthropic's cloud, so the Monday radar or morning brief survives mbp-2 being down. Worth moving one job as a test.
- **Claude Tag** (official Claude in Slack, Team/Enterprise only): could replace the homemade Slack bridge if you're on Team. Check plan tier.
- **`/goal`**: "keep going until every GBP review has a drafted reply." Good for review and inbox sweeps.
- **Claude Motion** (beta, Oct 8): report or deck to animated explainer MP4. Season recap content. Already flagged in last Monday's radar.
- **Dynamic workflows**: one command fans out dozens of agents. Example: audit every brand's GBP, reviews and ads in parallel in one run.
- **Memory in claude.ai chat** (Jul/Aug): set per-brand preferences once on the phone app.

## Watch, don't act yet

- Google AI Mode booking covers restaurants, tickets, hotels (Aug 27) and appointments. Tours not confirmed. The sauna might fit "wellness appointments" later.
- ChatGPT checkout: retail only, OpenAI pulled back in March. Nothing for tours.
- Sora 2 API reportedly sunset Sep 24 [U]. Don't build on it. Higgsfield/Seedance/Kling/Veo are the lanes.
- Threads ads open to everyone. Cheap test someday, not urgent.
- SES moved to tiered plans (Jul 21). Base rate unchanged [U]. Glance at the us-west-2 account to confirm no paid tier got turned on.
- T-Mobile 10DLC fee went to $0.004/SMS (Jan). Rounding error unless winback volume grows.

## How this stays current (no more asking)

- **Every Monday 6:10am**, `/radar` runs on davids-mbp-2. It now has a **Tool Watch** section: checks Claude's changelogs, Google/Meta/FareHarbor/Viator/Skift/AWS/OpenAI feeds, drops anything you already use, and lists up to 8 items with a brand-specific action.
- Brief lands in `00 Dashboard/Radar/{date}.md`, same as before. First run with Tool Watch: **Mon Oct 19**.
- Feed list lives in `~/.claude/skills/radar/data/watch-config.json` under `tool_watch` (both Macs). Add or cut a source there.
