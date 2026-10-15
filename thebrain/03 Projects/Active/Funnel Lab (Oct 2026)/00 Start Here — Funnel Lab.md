# Funnel Lab (Oct 2026): start here

*Built overnight 2026-10-14 by David's Claude. Everything here is a draft. Nothing sent, posted, deployed or changed on any site, ad account, FareHarbor or OpenCX.*

**Pick on the board:** https://claude.ai/artifact/LTjN8HJcPoE3g8RnCKKLrY (16 cards, each built two ways: pick A, pick B, or split-test both)

| File | What it is |
|:-|:-|
| 01 Customer Truth | 10,900 Google reviews + 981 chats, counted per brand. Who buys, what they ask first, what stops them, real phrases |
| 02 Funnel Baselines | Live GA4 / Ads / Meta numbers per brand, last 30 days vs last year, biggest leak each |
| 03 Testing Infrastructure | What can run a split today (almost nothing), sample sizes, the cheapest build |
| 03a Code Sketch | sample_size.py and the original sketches |
| 04 A-B Test Backlog | The 16 tests with full copy for both versions, evidence, how to measure |
| 10 Play 1 | Weather credit vs refund, both versions + a test that can start this week |
| 11 Play 3 | "How did you hear about us", both versions |

**Code:** `~/Projects/fh-lead-engine-ab`, branch `ab-variants` (commit 4453149). Variant assignment, report script, `ab.js`. 36 tests pass. Ships with zero running tests, so merging changes nothing live. Not merged, not deployed. Steps to go live are in its `EXPERIMENTS.md`.

**Night shift (local model, 1am):** 3 jobs queued: paired ad hooks per brand, honest ad lines from 2-3 star reviews, paired email subject lines. Output lands in `_Ops/Night Shift/Output/2026-10-15/`.

## The five things that surprised me

1. **Price is NPB's #1 chat question (52%), and 64% of chats end with nothing.** The fastest money is in the chat, not the site.
2. **Paid social brings sessions, not bookings.** NPB 10,966 sessions for 8 purchases; BBK and LSKT 0.
3. **Most brands are too small for purchase-level A/B tests.** NKST would need 211 days. So tests read chat replies, leads and Book taps instead.
4. **The personas are off in places.** NPB: birthdays beat bachelorettes. NKST: lead-form people are mostly locals. E&E: nobody says "recovery".
5. **NKST and HPB can't see purchases in GA4 at all.** Fix that (card 16) before trusting any of their numbers.

## Open questions for David

1. Confirm live NPB prices and Party Queen capacity (chat 22, site 26).
2. OK to email the FareHarbor rep for a header-script slot on NPB, NKST, HPB, LSKT, AKT?
3. What's the E&E bring-a-friend offer?
4. Who has GTM publish access on BBK and DCKT?
