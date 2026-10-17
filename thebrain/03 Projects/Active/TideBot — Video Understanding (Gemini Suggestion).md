# TideBot — Video Understanding (Gemini Suggestion)

*Logged 2026-10-17. Status: idea, not started. Bot code lives in `dwrack/tidebot`.*
*Related: `Content Engine/Daily Video Factory — 4-5 Per Brand Per Day (Aug 2026)`, `Secrets Migration — On The Docket (Next Week)`.*

---

## Where it came from

An Instagram comment from sz.peak (Oct 2026):

> Another suggestion - Connect Google Gemini Api too, that can help your AI understand any video and will give claude multi modal capabilities

## The real gap

Claude reads images and text, but it can't take a video file directly. That means it can't watch a clip or hear its audio on its own. Gemini's API accepts whole video files, sound included.

## Recommendation: frames + transcript first

Before adding Gemini, use ffmpeg to pull frames from each clip and a speech-to-text model (Whisper or similar) to turn the audio into text. Claude then gets the frames and the transcript.

- **Most of it already exists.** `narrate2.mjs` already uses ffmpeg, so this mainly adds a transcription step.
- **One model, one bill, one key.** Gemini adds another API key and service to manage, and the secrets migration isn't done yet.
- **It covers the jobs we'd actually use it for** (see below).

## Where it pays off

- [ ] Pre-screen Daily Video Factory drafts so the morning review pass goes faster
- [ ] Tag the Crew Clips library so TideBot can search footage
- [ ] Check tagged guest/UGC videos before reposting
- [ ] Break down competitor TikToks

## When Gemini is worth adding

When timing matters across a long video, e.g. "what happens at 2:14 in this 40-minute tour recording?" Sampled frames can miss quick moments. Add it later as an optional tool TideBot calls only for those cases.

## Next step

Attach `dwrack/tidebot` to a Claude session and build the video-analysis step (frames + transcript, Gemini optional).
