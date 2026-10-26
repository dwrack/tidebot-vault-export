# Comment research, 2026-10-22 (all verified live 10/22 unless noted)

## 1. NKST Instagram auto-poster: NOT running
- Decision record 2026-10-21 says to clone npb-ig-reels as nkst-ig-reels on davids-mbp-2, launchd daily 11:30.
- Live check on mbp-2 (ssh, 10/22): no `nkst-ig-reels` script dir (`~/.claude/scripts` has only hpb-ig-reels, npb-ig-reels, ebb-ig-yt), no igreels plist for NKST (only com.npb.igreels, com.hpb.igreels, com.djl.ig-dm-worker loaded). The job was never built or loaded. No log exists.
- Queue CSV exists in vault (40 rows). First row 2026-10-21 `reels/ad-01-reels-music.mp4` status=queued, posted_at empty, media_id empty. Next due 10/24, 10/26, 10/28, 10/31, all queued. So nothing has posted.
- @kayaknola (IG id 17841400497678116, 5,309 followers) last 6 posts via meta-organic:
  - 2026-07-14 carousel (cypress knees)
  - 2026-07-05 carousel (Eastern Lubber grasshopper)
  - 2026-06-11 reel (Sweat. Swamp. Summer.)
  - 2026-05-27 reel (murky water/gator)
  - 2026-05-09 reel (swamp quote)
  - 2026-03-26 reel (New Orleans nightlife)
- Answer: NO. Most recent post 2026-07-14 (about 100 days ago). Auto-poster has posted nothing. Decision record also says first post waits on David's OK on the sample.

## 2. TLDR learnings
Existing loop: "TLDR Watchdog" writes dated notes to `TheBrain/00 Dashboard/TLDR Watchdog/` (latest file 2026-10-17; others 8/28 to 10/16). It writes only to that vault folder (2 items per run, with a "first move"). Not found in any launchd plist on mbp-2 or scheduled-tasks; 2026-09-19 Vault Audit also could not locate its scheduler ("likely a machine-2 claude loop"). No new file since 10/17, so it is stale or stopped; nothing from the 10/20-10/22 editions was captured. No TLDR skill in `~/.claude/skills`. Also referenced in: Marketing Ideas (Tom Orbach) swipe file, Inbox Triage 2026-10-15, AEO Action Plan.

TLDR emails today (10/22): TLDR, TLDR Marketing, TLDR Design in dwrack81 inbox (a few unread). Useful items:
1. GEO is a distraction (Marie Haynes). AI tools = 0.73% of Google Organic traffic across 100 sites, Google Organic = 96.5% of conversions. Why: tempers our GEO/AI-citation spend, keep effort on Google Search incl. AI Overviews/AI Mode. https://www.mariehaynes.com/geo-is-a-distraction/
2. Creators rival search for Gen Z discovery; small creators convert as well as famous ones (33% discover via creator posts). Why: backs the small-creator invite plan (follower-personas / creator outreach). https://www.netinfluencer.com/creators-now-rival-search-for-gen-z-product-discovery-small-accounts-convert-as-well-as-famous-ones-survey-finds/
3. Animated infographics in Claude Code (HTML/CSS/JS, reusable repo with brand guidelines, fonts, past posts, batch 5 posts on Sunday). Why: copyable workflow for our carousel/reel batches. https://knowledge.gtmstrategist.com/p/diy-guide-animated-linkedin-infographics-claude-code
4. 8 tips to improve SEO & AEO: refresh low-CTR pages, reviews and consistent listings, monthly review. Why: matches our GBP/review/page-refresh playbook, checklist for audits. https://www.linkedin.com/posts/austinarmstrong90_im-begging-you-to-focus-on-seo-and-aeo-share-7516855098627571712-w31T/
5. Your newsletter has two readers now: Apple Mail/Outlook AI summaries use subject line and live text near the top, not images. Why: our win-back emails are image-heavy; put key offer in live text up top. https://www.audiencebridge.io/p/your-newsletter-has-two-readers-now
6. Claude Duet (Anthropic agent, 6,000 apps, shows plan before acting, wait list for Pro/Max) and "keep credentials out of your agent's context" (WorkOS, sponsor). Why: possible future ops agent; credential isolation fits our secrets rules. Source: TLDR main 10/22 (https://links.tldrnewsletter.com/0l3eSc).
Also: PHP critical RCE security release 10/21 (NSA says patch now). Why: our WordPress hosts run PHP; worth checking host PHP version. https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/

## 3. Danesh and the sauna injury (Ebb & Ember)
- Danesh Oleshko, email **doleshko@gmail.com** (E&E Gmail threads, 10/12 to 10/15). Role: Portland psychotherapist (LMFT) and ceremonialist who hosts Monday Banya sessions (and Borscht and Banya events) at E&E as an independent host; terms (slots, $50/slot, comped membership, waivers) still undefined. Source: `Ebb and Ember/Monday Banya with Danesh.md`; `Ebb and Ember/Operations/Total To-Do (Oct 8 2026).md` ("Danesh Banya terms + pricing revamp").
- Incident: Danesh's email 2026-08-27 (Gmail msg 1a046a4b56ead570, "Re: Upcoming availability", still UNREAD): "a guest stepped into the gap between the pier and the main platform and bruised her leg." Occurred Monday 8/24 (Banya session, her being Danesh's friend). Body truncated in the API; full text needs opening in Gmail.
- Vault: `Ebb and Ember/Operations/Slack Gap Scan (2026-09-19).md`: "Danesh's friend (8/24, stepped into the pier gap, bruised leg): read Danesh's 8/27 email (unread), check Periode for her waiver + payment, reply to Danesh". Not yet done. Guest name not in vault; waiver/booking in Periode not verified (no access checked).
- Related: Full Picture Board H2 (waiver update: pregnancy, heart, meds), and Weekly Overview 2026-08-20 notes the entrance camera is half blocked by pilings (footage gap).

## 4. HPB past-guest win-back: not sent in Oct 2026
- Memory (project_npb_hpb_winback_oct2026, 10/13): HPB 8-week series "never blasted, all June copy; rewrite before use". The only HPB job, dnswatch Father's Day test, was disabled 10/13 (plist `.disabled-20261013-fathers-day-test`). Only May 2026 spring sends exist (`send_log_20260520_*`, `send_log_20260529_*`). No Oct HPB send or staged Oct draft found.
- List: `Houston Pedal Barge/Houston Pedal Barge Contacts — Clean Backup.csv`, 16,964 rows, columns email,name,phone,optin. optin: Subscribed 575, No 4,883, blank 11,506. Also `.ses_campaign/subscribed_all.json` (35 KB).
- Sending path built: `Houston Pedal Barge/.ses_campaign/winback_sender.py` + `winback_series.py`, SES v2 us-west-2, from info@houstonpedalbarge.com, config set `hpb-campaign`, RFC 8058 one-click List-Unsubscribe via hosted API Gateway Lambda (https://7upwfzf3q0.execute-api.us-west-2.amazonaws.com), suppression list pre-filtered. Note: `config.py` holds a secret-looking key string in the vault (leak risk).
- Existing drafts: `Houston Pedal Barge/Marketing/Winback Email Previews/` (index.html, w01 to w08, a01-last-weekends.html; June copy, Aug 13-14 dates). NPB's Oct runner (mbp-2) is the template; HPB has no launchd runner or send schedule file. SES complaint rate was 0.158% on 10/13 (above 0.1% review line, shared across brands).
