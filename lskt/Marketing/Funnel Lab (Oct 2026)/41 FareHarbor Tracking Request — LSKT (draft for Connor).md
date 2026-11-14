# FareHarbor Tracking Request — SENT 2026-11-13

**Status: SENT.** Michael's call: skip the Connor hand-off and David sign-off, send it directly.

- **Sent** 2026-11-13 from mrfischer80@gmail.com to **support@fareharbor.com**
- Subject: "Tracking setup — Lone Star Kayak Tours (3 sites)"
- Gmail thread id `1a1d668aaf38ab0f`
- Signed from Michael, not Connor. Otherwise the body below went as written.

This closes Funnel Lab open questions 8 and 10 as *asked* (not yet as *answered*), after sitting since Oct 15.

**Watch for:** a generic support inbox is slower than a named rep. If there's no reply in about a week, Connor should chase it through his own FareHarbor account manager — who still isn't recorded anywhere and should be, once we learn who it is.

Why now: Meta is off for the winter across all three brands (`Houston Pedal Barge/Ads/2026-11-12 Winter Plan - Meta Ads (HPB + BBK + Austin).md`). The dark window is the whole point — this ask is the gate on any March 2027 relaunch, and nothing else is competing for the booking flow until then. One request covers **four** stalled projects: the Meta pixel fix, the lead-capture popup, the quiz, and on-site A/B tests.

Scope: the LSKT-side FareHarbor accounts only — shortnames `lonestarkayaktours`, `houstonpedalbarge`, `buffalobayoukayak`. **NPB and NKST need the same ask sent separately** on the Gravity Trails side; different entity, likely a different rep and account.

**Recipient:** no FareHarbor rep is on file in any vault — Connor should send it to his own account manager. Fallback is `support@fareharbor.com`, but a named rep will move faster. (The one `@indexic.net` address in HPB Key Contacts is a competitor's marketing email, not FareHarbor.)

---

## The email

> **Subject:** Tracking setup — Lone Star Kayak Tours (3 sites)
>
> Hi [rep],
>
> Two setup questions, both about getting our ad tracking working. Right now we can't attribute any of our Facebook/Instagram ad spend to bookings, because the Purchase event fires on fareharbor.com rather than on our own domain — so Meta never sees which ad produced a booking.
>
> Accounts: `lonestarkayaktours`, `houstonpedalbarge`, `buffalobayoukayak`
>
> **1. Meta (Facebook) conversion tracking**
>
> Our pixels are installed and firing PageView on our own pages, but the booking itself completes inside the FareHarbor checkout. Could you tell us which of the following FareHarbor supports, and switch on whatever is available?
>
> - Meta Conversions API — server-side Purchase events sent to our pixel
> - Advanced matching — passing hashed email/phone with the Purchase event
> - Passing the `fbc` and `fbp` cookies from our site through into the booking flow
>
> Pixel IDs:
> - `buffalobayoukayak` — 381452300055179
> - `lonestarkayaktours` — 1559188957448084
> - `houstonpedalbarge` — 1559188957448084 (same pixel; it's already live on the site)
>
> Separately: **austinkayaktours.com has no Meta pixel on it at all.** Since that site books through the `lonestarkayaktours` shortname, could you add pixel 1559188957448084 to it as well? That one may need the header slot in ask 2.
>
> If any of these aren't supported, just tell us which, and we'll handle the rest on our end.
>
> **2. Header script slot**
>
> Could you add one line inside `<head>` on these three sites?
>
> - houstonpedalbarge.com
> - lonestarkayaktours.com
> - austinkayaktours.com
>
> (buffalobayoukayak.com already runs Google Tag Manager, so it doesn't need this.)
>
> It's a single `<script>` tag — we'd use it for an on-site popup and some A/B testing. I'll send the exact snippet once you confirm the slot is available. Elfsight and OpenCX are already installed on houstonpedalbarge.com, so I believe the slot exists there at least.
>
> Thanks,
> Connor

---

## Notes for David before this goes out

**What's deliberately not in it.** No mention of ad budgets, performance, or that Meta is currently switched off. Reps route on "what do you support," not on our strategy. It also doesn't ask for GA4 or FareHarbor-side changes — those we control.

**Why ask rather than instruct.** The Oct 30 BBK fix spec flagged FareHarbor's Conversions API support as **unverified**. Asking which of the three options exists gets a usable answer in one round trip; specifying one and being told no costs another week.

**Correction (2026-11-13): HPB is not missing a pixel.** The Oct 31 audit said HPB had no live pixel and that the dead "Houston PBarge Pixel" 4992293504182167 was the problem. Checking the live site says otherwise:

houstonpedalbarge.com fires `fbq('init', '1559188957448084')` — the **LSKT Pixel** — and it is healthy. Over the last 7 days that pixel logged 3,557 PageViews and 40 Purchases:

| Domain | Events, last 7d |
|:-|-:|
| houstonpedalbarge.com | 2,546 |
| lonestarkayaktours.com | 771 |
| fareharbor.com (Purchase) | 40 |

HPB is the **largest single source of traffic to that pixel.** Pixel 4992293504182167 is a red herring — a genuinely dead 2023 asset that nothing references any more.

The real problem is narrower and easier: **pixel 1559188957448084 is assigned only to the Austin ad account** (`act_638850950128825`). HPB's campaigns live in the Houston account (`act_1015419897308486`), which can only see Buffalo Bayou's pixel. So HPB's ads cannot optimize against the pixel HPB's own website is already firing.

**Fix: share pixel 1559188957448084 with `act_1015419897308486`.** Both accounts belong to the same business ("Daves Businesses", 10153674406626399), so it's an internal assignment — no new pixel, no site change, and it does not wait on FareHarbor. **Done 2026-11-13** — `act_1015419897308486` now lists both pixels. Nothing else in Meta was touched, and no money moved: the account still has zero ad sets that can spend.

Do *not* create a new HPB pixel. A new pixel would need its code onto houstonpedalbarge.com, which requires the header-script slot in ask 2 — the very thing this email is trying to unblock. Sharing the working pixel sidesteps that loop entirely.

**One real caveat:** 1559188957448084 is shared across HPB *and* Lone Star. Signal from two brands lands in one pixel. That is workable — separate them with URL-based custom conversions — but it is the "three brands in one account muddies the pixel" problem the Oct 31 Austin audit flagged, and it is worth splitting properly once the header slot exists.

## What to do with the reply

| If they say | Then |
|:-|:-|
| Conversions API is supported | Best case. Turn it on for all three pixels, send test events, run the acceptance test below |
| Only advanced matching | Take it. Worth having, but it won't fully close the gap — pair it with the GTM route for BBK |
| None of it | Fall back to **GTM-TKMN5XSX** on buffalobayoukayak.com: fire `Purchase` with value when the FareHarbor lightframe confirms a booking. Needs Connor or David in tagmanager.google.com; publish access is still unverified. For HPB/LSKT/AKT this makes the header-script slot (ask 2) load-bearing — it becomes the only way to get a tag on those sites |
| Header slot yes | Send the snippet. It carries `ab.js` and the popup, and serves the quiz too |
| Header slot no | The popup, quiz and A/B tests stay blocked on those three sites. Escalate, or move the sites off the FareHarbor WordPress theme — a much bigger decision that belongs with the website rebuild |

## Acceptance test — the thing that actually closes this

Whatever they enable, it isn't done until this passes:

1. Create a Meta Test Events code in Events Manager.
2. Click a live ad, complete one real booking through the FareHarbor flow.
3. Within 24 hours, that Purchase must appear in Events Manager **attributed to its campaign** — not just as an unattributed event.

Until step 3 passes, treat Meta as unmeasurable and keep it at $0. That is the Part 5E relaunch gate.

Alongside it, regardless of what FareHarbor does: add `?utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign}}&utm_content={{ad.name}}` to every ad URL, and a `ref=` value on every FareHarbor book link (Website Standards rule 9). Those are ours, they cost nothing, and they give a second read on paid social that doesn't depend on Meta at all.

## Related

- `Houston Pedal Barge/Ads/2026-11-12 Winter Plan - Meta Ads (HPB + BBK + Austin).md` — Part 5D, the measurement work this unblocks
- `Buffalo Bayou Kayak/FDE/Meta Zero Purchases Diagnosis + Fix Spec 2026-10-30.md` — the evidence that the Purchase event fires on the wrong domain
- `00 Start Here — Funnel Lab LSKT.md` — open questions 8 and 10
- `31 Popup A-B Plan — HPB.md` — card c03, the popup half of the header-slot ask
