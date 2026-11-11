# Party Room Mockup (Nov 2026)

Made 2026-11-10 for David's talk with Jeff (`Meetings/Jeff Talk - Party Room Look + Photo (2026-11-11).md`). It shows the gas station party room with the check-in counter and clutter removed and six round high-tops with black spandex covers. The benches are moved to the walls, and the string lights are sharp.

- `before-after-for-jeff.jpg`: the current photo next to mockup D (styled high-tops with palms and florals, image David supplied 2026-11-10). Show Jeff this one.
- `mockup-a-six-high-tops.jpg`, `mockup-b-cluster.jpg`: earlier 6-table layouts (too crowded). `mockup-c-four-spaced.jpg`: current pick (prompt_v3.txt, seed 21).
- `before-current-room.jpg`: the source photo (`Assets/Photos/Marina Property 2026-11/NPB indoor lounge bar string lights.jpg`).

**AI concept only.** Do not use it in ads, email or on the site. The real photo gets shot once the high-tops are in (see the Nov 19 plan shot list).

How it was made: FLUX.2 Klein 4B (Apache 2.0) via mflux 0.24 on the bigly Mac, `~/claude-jobs/npb-mockup/` (venv, prompt.txt). Ollama on bigly can't run image models: its Homebrew build returns "image generation models are not currently supported", so `x/flux2-klein` was pulled but is unusable there. Each edit takes about 1 to 2 minutes.
- `mockup-d-styled-high-tops.jpg`: current pick, supplied by David 2026-11-10 (replaces C).
