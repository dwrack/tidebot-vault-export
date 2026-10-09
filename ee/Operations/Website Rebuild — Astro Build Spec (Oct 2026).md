# Website Rebuild — Astro Build Spec (Oct 2026)

Living spec for the new ebbandember.com (Astro + Cloudflare Pages). Supersedes the feature list in `Website Rebuild — Static Site Plan (Sept 2026).md`; that doc still owns the cutover checklist.

**Status (2026-10-08):** spec drafted. **Design direction: Othership-inspired** (Davey, 2026-10-08): bold type, warm, social and playful, booking-first, photo/video-heavy. Not one of the three Aug prototypes; reuse their live-data pieces.

**Media:** vault library (`Assets/Photos/`, mostly pre-July 2026) + `Assets/Photos/2026 IG Pull (Jun-Oct)/` (80 IG originals, compressed) + 20 tagged UGC posts listed there (need creator OK). Hero video needs raw footage from Kimberlynn / Grant.

## v1: build now

### 1. Our own booking flow (replaces the jump to Periode)
The current handoff to minside.periode.no looks and feels like a different company. Fix: we own every step except payment.

1. **Pick:** session type, date, time on our site, using live Periode seat counts (see #2). Each day shows sunset time + moon phase; slots near sunset get a "Sunset session" tag, full-moon nights get flagged.
2. **Guests + contact:** name, email, phone on OUR form. Saved to our backend as soon as the email is valid (on blur, not per keystroke). Short notice under the field: "We'll hold your details so you can pick up where you left off."
3. **Pay:** Periode opens inside a branded bottom sheet (iframe, deep-linked to the exact slot `/booking/{org}/{product}/YYYY-MM-DD/HH:MM`). Periode sends no frame-blocking headers as of 2026-10-08; verify Stripe checkout works inside the iframe on iPhone Safari. Fallback: same-tab handoff with a branded interstitial.
4. **Abandoned booking:** contact saved in step 2 + no matching Periode booking within ~1 hr = recovery email via ActiveCampaign (needs AC API key, hidden-prompt script). Match completions via Periode booking emails / GA4 purchase.

Limit: we cannot see what people type inside Periode's own form (different domain). That's why capture happens in step 2.

To test: whether Periode accepts URL params to prefill name/email (avoids retyping).

### 2. Live availability (Periode internal data)
- Source: Firestore REST, `dateSlots/{org}/manifests/{product}/slots/{date}`. Details + working example: `Website Rebuild — Periode Live Availability (Oct 2026).md`.
- Unofficial. Built with:
  - Edge cache 60-120s (one read/min per product).
  - **Fallback:** widget hides, plain Book button shows. Never a broken widget.
  - **Health check:** cron Worker every 15 min validates the response shape; on failure, Slack DM to Davey (Claude bot, ET workspace) once, then again on recovery.
- Covers Social, Sunrise, Moonlight. Private Sauna uses a different structure, needs its own look.

### 3. Living sky (all client-side, SunCalc, no API)
- Palette follows the real sun for Portland (dawn blue-grey → golden-hour amber → night ember), continuous.
- Sunrise/sunset: hero glow ±20 min, "Sun sets over the Columbia in 12 min."
- Moon: real phase drawn in the night sky; phase + rise/set shown in the booking picker; full-moon nights promoted ("Full moon tonight. Moonlight Sauna at 9").
- Seasons: copy, photo set, mood rotate (fall mist/rain, winter steam/cold, spring green, summer river).
- Rule: Book button + text never move or lose contrast. Respect prefers-reduced-motion.

### 4. Live conditions strip
- Portland weather (Open-Meteo, free) + Columbia river temp (USGS 14105700).
- Rain = drops on glass + "Perfect sauna weather." Fog drift, frost on cold mornings, golden-hour glow.
- Easter eggs: solstice/equinox, longest night, first frost, meteor showers, fall salmon return, notable river temps.

### 5. Returning visitors
Cookie/localStorage after a booking click. Returning: "Welcome back" + their usual session + membership upsell instead of the first-timer pitch.

### 6. Measurement
- Microsoft Clarity (heatmaps + recordings). Install on current Squarespace now for a baseline.
- GA4 G-YF8FPEWW4S + port the Periode tracking bridge (fbclid/gclid/client_id) day one.
- A/B framework: cookie split at the edge, `experiment_view` / outcome events to GA4.

### 7. SEO / AEO
- LocalBusiness + FAQPage + Product (gift cards, memberships) JSON-LD, answer-first copy, Bathhouse-style titles, first-timer guide.
- Reviews shown next to Book (real GBP quotes). Note: Google does not show stars for self-reviews on our own site; GBP stars already show in Maps/local pack.

### 8. Email + SMS capture banners (A/B rotated)
Test no-giveaway "nature alerts" against classic offers. Hypothesis: alerts tied to real conditions convert without a discount and fit the brand better.

| Variant | Hook | Giveaway? |
|---|---|---|
| Rain alert | "Text me when it's pouring. Best sauna weather there is." | No |
| Full moon | "Full moon reminders, 2 days ahead." | No |
| Sunset seats | "Tell me when sunset sessions open up." | No |
| Last seats | "Text me when tonight's last seats are going." | No |
| First frost | "First frost of the year? We'll let you know." | No |
| First visit | "$X off your first session." | Yes |
| Gift drop | "Free guest pass on your 3rd visit." | Yes |

- Email-only, phone-only, and both versions of each; measure signup rate AND later bookings, not just signups.
- SMS: separate unchecked consent box with TCPA language ("msg & data rates, reply STOP"). No marketing texts until the Twilio A2P 10DLC campaign is approved (resubmitted Jun 3 2026, status to re-check).
- Alerts are automated off the same weather/moon/availability data as the site.

**Visit-count ladder (non-bookers):** first-party visit counter (localStorage + cookie, no login). Each visit shows a different ask, escalating:

| Visit | Show |
|---|---|
| 1 | Nothing pushy. Live sky/conditions, Book button only. |
| 2 | Nature alert signup (rain / full moon / sunset). |
| 3 | First-timer guide + "what to expect" + reviews. |
| 4+ | Small offer (first-session $ off or bring-a-friend), shown once. |

- Stops once they book or sign up (switch to the returning-member flow, #5).
- Count visits as sessions 30+ min apart, not page loads.
- Limits: Safari wipes script-set storage after 7 days without a visit and private browsing resets it, so the ladder favors people who come back within a week. Fine for this use.
- A/B the ladder itself vs a fixed banner.

## Ideas to weigh (from Othership, 2026-10-08)
- Members-only extended booking window (Othership: 3 weeks). Needs a Periode setting; ask Erik.
- Milestone gifts at visits 1/2/3/5/7/11.
- Give-X/Get-X referral.
- "Limited-time membership offer, $X in value" banner stacking perks.

## v2.0: after v1 is live
- **Weather-matched media:** hero photo/video swaps to footage that matches the real conditions (rain footage when it's raining, fog when foggy, snow, sunset). Needs a tagged media library per condition/season.
- Own chatbot (Twilio + our code).
- Book-by-text.
- Apple Wallet membership pass.

## Parked
- Email to Erik (abandoned bookings, member window, official availability endpoint). Paused by Davey 2026-10-08.
