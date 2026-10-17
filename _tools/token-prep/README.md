# Token prep: where the tokens go, and what the Mac can do first

Audit date: 2026-10-12. Source: the transcripts of the last ~60 sessions (CLI and iOS).
Numbers are per-turn context (what every reply re-reads, cached) and the
cache-read volume across the last 100 transcript events.

## 1. The five heaviest tasks

| # | Session | Context per turn | Cache reads (last ~100 events) | What was being read |
|---|---------|-----------------:|------------------------------:|---------------------|
| 1 | Elevatedtides.com website build | ~646k | 22.1M | Astro site source, CSS, npm/Lighthouse output, vault notes; very long session |
| 2 | FareHarbor Dec/2027 availability | ~400k | 18.0M | hundreds of Playwright click/wait/navigate/find results (200–7,000 chars each), 2 screenshots |
| 3 | Ebb and Ember marketing analytics | ~382k | 20.3M | Gmail search/get (7–9k chars each), vault markdown, Drive search, 1 image (2100x1600) |
| 4 | Private sauna builds Slack channel | ~313k | 7.8M | one 16k-char Bash dump of vault files, continuation of an earlier session |
| 5 | Tailscale / lease iMessage thread | ~232k | 9.0M | 4 iMessage conversation pulls (24k chars) + 2 searches (16k chars) ≈ 11k tokens of chat text |

Runners-up: Electric panel sauna drawings (285k, 5 drawing images), Unattended work (257k),
Blink camera timelapse (244k, 2 images), Cave Point cancellation text (205k: 21k chars of
`ls -R`/`cat` over the Marketing folder plus 4 Canva PNGs).

Two facts matter more than any single file:

* **A fresh session costs 110k–157k tokens before the first tool call.** Cave Point's first
  reply read 109k; the Tidebot trip-log session's first reply read 157k. That is the system
  prompt, every MCP server's tool schemas (playwright, imessage, imessage-send, several Gmail
  accounts, google-ebb, gbp...), CLAUDE.md, memory and skills. Every turn re-reads it.
* **Images are a small share.** A full-size image is ~1,500 tokens. The worst session had 5,
  under 8k tokens, or 1–3% of its context. Text dumps and turn count are the real sinks.

## 2. Could the Mac do it locally first?

| Input | Local, free, built in? | Tool | Verdict |
|-------|------------------------|------|---------|
| Vault folder `ls -R` + `cat` (6k–390k tokens) | Yes | python3 digest (headings, first line, sizes) + `mdfind` | **Biggest text win** |
| iMessage thread dumps (~11k tokens/task) | Yes | python3 + sqlite3 on chat.db, drops tapbacks, trims | **Second biggest** |
| Gmail search/get results (7–9k chars each) | Partly | MCP returns full bodies; ask for `max_results` 5 and snippets only | medium |
| Canva PNGs, build drawings (~1,500 tok each) | Yes | `sips -Z 1200` built in; one tiled sheet needs ffmpeg | small win |
| Screenshots of dashboards | Yes | Vision OCR via a 20-line Swift script (~300 tokens of text instead of ~1,600) | small win |
| Playwright page results | No | the page has to be seen; fewer, batched evaluate calls help | n/a |
| Session length / baseline | Yes | fewer MCP servers per project, `/clear` between tasks | **largest lever overall** |

## 3. The prep steps (nothing installed)

| Script | Replaces | Before | After |
|--------|----------|-------:|------:|
| `vault_digest.py <folder>` | `ls -R` + `cat *.md` | Cave Point: ~6,000 tok; whole `dckt` folder: 1.4M chars (~390k tok, would not fit) | 100 lines, ~1,200–2,600 tok |
| `imsg_digest.py --contact X --days 45` | 4 `get_conversation` + 2 `search_messages` | ~11,000 tok | ~1,200 tok (tested: 36.8k chars → 4.8k) |
| `contact_sheet.sh out.jpg a.png b.png ...` | reading 4–5 images | ~6,000–7,500 tok | one sheet, ~1,600 tok (ffmpeg needed for tiling; sips alone downsizes one image) |
| `swift vision_ocr.swift shot.png` | reading a screenshot | ~1,600 tok | ~300 tok of text |

Savings compound: a 10k-token dump read at turn 5 is re-read on every later turn, so in a
45-turn session it costs ~450k cached-read tokens, not 10k.

Usage from a Claude session on the Mac:

```bash
P=~/.claude/tools/token-prep   # installed copy on the Mac; this repo folder is the source
python3 "$P/vault_digest.py" "<vault folder>" --out /tmp/digest.md      # then read /tmp/digest.md
python3 "$P/vault_digest.py" --find "cave point wind" --in "<vault>"    # Spotlight instead of find
python3 "$P/imsg_digest.py" --contact "Catherine" --days 45 --out /tmp/thread.md
bash   "$P/contact_sheet.sh" /tmp/sheet.jpg img1.png img2.png img3.png
swift  "$P/vision_ocr.swift" screenshot.png
```

Requirements: python3, sqlite3, sips, mdfind and swift ship with macOS. `imsg_digest.py`
needs Full Disk Access for Terminal (System Settings > Privacy & Security) to read
`~/Library/Messages/chat.db`; it copies the DB to a temp dir and reads only. `contact_sheet.sh`
uses ffmpeg only for tiling and video frames and prints `brew install ffmpeg` if it is missing;
it does not install anything. Tested on Linux with python3/sqlite3/ffmpeg; the sips, mdfind
and Vision paths are macOS-only and untested here.

## 4. What to do before installing anything

1. On the Mac run `claude mcp list` and note which servers load in the vault project. Each one's
   schemas sit in every turn; disable the ones a project never uses.
2. Check `~/.claude/CLAUDE.md`, the vault's CLAUDE.md files and `~/.claude/projects/*/memory`
   sizes. Anything over ~10k chars is paid on every turn of every session.
3. Start a new session per task instead of continuing a 300k+ one; use `/clear` or `/compact`.
4. If the digests prove useful, add a CLAUDE.md line telling Claude to run `vault_digest.py`
   before `cat`-ing a folder and `imsg_digest.py` before pulling a thread.
