# HPB Lead Capture & Nurture System (Plan, Sep 29 2026)

**The short version:** the site gets ~9,000 visits a month and has zero way to catch the 99% who leave. Fix that with a $25 gift for an email + phone, a 7-day email/SMS sequence that expires the gift, auto-stop the second someone books, and a slow always-on drip for everyone else. Reactivate the old list in controlled waves. Run it all in a cloud tool, not on a laptop.

---

## 1. What the numbers say

| Metric | Number | Source |
|---|---|---|
| Site sessions, last 90 days | 27,331 | GA4 |
| Organic Social share of that | 19,003 (70%), only 13% engaged | GA4 |
| Paid Social sessions | 1,383, only **38 engaged (3%)** | GA4 |
| Organic Search / Paid Search engaged rate | 57% / 57% | GA4 |
| Revenue trailing 90 days | $41,447 | FareHarbor |
| 2026 YTD | 278 bookings, $67.6k, avg $243/booking | FareHarbor |
| 2025 / 2024 full year | 849 / 1,192 bookings | FareHarbor |
| Next 90 days forecast | ~$9.9k vs $25.7k same window last year | Forecast 2026-09-24 |
| Email capture on the site right now | **None** (old getsitecontrol popup is gone) | site scan |

Read: the "clicks with no conversions" are mostly social taps from people who were never going to book today. Search traffic behaves fine. The problem isn't the checkout, it's that a group-outing decision takes days (organizer has to wrangle 10-20 friends) and we have no way to follow up. Paid social clicks at 3% engagement are basically wasted.

**Unblocked today:** the email DNS records FareHarbor was supposed to add are actually live. SES had given up checking back in June. I re-triggered verification on Sep 29 and it came back **SUCCESS**. Email sending is unblocked. The daily DNS watcher on davids-mbp-2 has been failing because it can't find the `aws` command, so it never noticed.

---

## 2. The system in one picture

```
Visitor / social click / Meta lead ad
        |
   [Capture: $25 gift popup, email + phone]
        |
   "New Lead" flow (SES + Twilio) (7 days, email + SMS)
        |------------- books? --> FareHarbor sync --> exits flow --> Post-trip flow
        |
   gift expires day 7
        |
   "Long nurture" (1 email/week, 1-2 texts/month, re-gift every 90 days max)

Past customers --> Post-trip flow --> review, photos, referral, "next occasion" reminder
Old dormant list --> SES re-permission waves --> clickers join the lead system, non-clickers suppressed
```

**Tool: custom SES + Twilio (David's call, Sep 29).** Reuses what's already built: SES us-west-2 sending, the unsubscribe Lambda, the suppression list, the weekly reel email, and the Railway SMS responder. New pieces: a lead-capture endpoint (Lambda + small DynamoDB table of leads, consent, and flow step), and a scheduled flow runner that sends the next email/text for each lead. **Everything runs in AWS/Railway, not on a Mac,** so nothing stalls when a laptop sleeps. The flow runner needs a daily health check that alerts on failure, because the silent DNS-watcher failure (June to September) is exactly the risk with a custom build.

**SMS number:** David wants to reuse the Twilio number already set up for Lone Star Kayak Tours. **Open issue:** A2P registrations are tied to a brand and use case, so HPB marketing texts from a number registered to Lone Star can get filtered, and that could hurt Lone Star's texting too. Customers would also see a sender they don't recognize. Cheapest fix: keep the same Twilio account and add an HPB marketing campaign/number next to it (toll-free is about $2/mo). Either way, do NOT market from +1 832-261-4678, the HPB answering + waiver line.

---

## 3. Email capture on the site

### The offer
**"$25 toward your party."** Minimum 2 guests on the booking for it to apply. Ask FareHarbor to create the code with that rule and a hard expiration a few weeks to a month out (David, Sep 29). The emails keep counting down: "your $25 credit disappears on {date}." At a $243 average booking that's about 10%, big enough to matter, small enough to protect margin. Framed as a gift that expires, not a coupon. Call it a "credit" or "code," not money "in your account," since there's no actual account balance.

Why this is different from MAY20 (which got 0 bookings): MAY20 was a blind blast to a cold list. This gift goes to someone who was on the site in the last 60 seconds. Intent is already there, the gift just gives them a deadline.

### Placements (in priority order)
1. **Popup, two-step.** Step 1 = email only ("Where should we send your $25?"). Step 2 = phone with SMS consent checkbox ("Want the code texted too? We'll text you dates that open up."). Two steps convert better than one long form, and you keep the email even if they skip the phone.
   - Desktop: exit intent.
   - Mobile: after 20 seconds or 50% scroll. Never on the first second.
   - Hide for anyone already captured or who booked.
   - Don't show on the FareHarbor checkout itself.
2. **Mobile sticky bar** at the bottom: "Get $25 off your cruise" (tap opens the same form). Most traffic is phones from Instagram/Facebook.
3. **"Text me dates & prices"** button on the tour page next to Book Now, for the organizer who needs to check with the group first. Captures phone + email, starts the same flow.
4. **Party planner lead magnet** (later, week 3-4): "Bachelorette / birthday on the water checklist" (what to bring, cooler rules, split-the-cost math, sample playlist). Gated by email. Good for Pinterest and blog traffic.
5. **Meta lead ads (instant forms).** Since paid social site visits engage at 3%, stop paying to send people to the site. Run lead-form ads that collect email + phone inside Facebook/Instagram and push into the lead table (Meta webhook to the capture Lambda). Same $25 gift.
6. **Google Business Profile + IG bio link** to a simple landing page with the offer.

### Form copy (draft)
- Headline: **Your crew's $25 is waiting.**
- Sub: Clear Lake's BYOB party barge, captained, up to 26 people. Grab $25 toward your date, good for 7 days.
- Button: Send my $25
- SMS consent (required wording, unchecked by default): "Yes, text me offers and updates from Houston Party Barge. Msg frequency varies, msg & data rates may apply. Reply STOP to cancel. Consent not required to purchase."

### Tracking
- Every link in every message gets UTMs (`utm_source=klaviyo&utm_medium=email|sms&utm_campaign=lead-flow&utm_content=d0`). Remember `/sms` 301s to `/` and loses attribution.
- Gift redemptions = FareHarbor promo code report. That's the real scoreboard.

---

## 4. New Lead flow (7 days, the money flow)

Exits the instant they book (see section 6). Texts only 10am-8pm Central.

| When | Channel | Message |
|---|---|---|
| Instant | Email + SMS | Here's your $25, code, expiry date spelled out ("good through Tue Oct 7"). One Book Now button. |
| Day 1 | Email | Social proof: one real reel + 3 short reviews. "Here's what a Saturday out here looks like." |
| Day 2 | SMS | Reply bait, not a pitch: "Quick q, what's the occasion? Birthday, bach, work thing, just because?" Replies go to the AI responder / OpenCX, which answers and pushes a date. |
| Day 3 | Email | Kill the objections: BYOB, fully captained (no work), bathroom on board, weather policy, how to split cost with the group. |
| Day 4 | Email | "Forward this to your crew." Built for the organizer: date options, per-person price math, link. |
| Day 6, 5pm | SMS | "Heads up {first name}, your $25 expires tomorrow at midnight. Weekend dates going fast: {link}" |
| Day 7, 9am | Email | Last call, subject "Your $25 expires tonight." |
| Day 8 | (moves to Long Nurture) | |

Expiration mechanics (David's version): one FareHarbor code per wave (e.g. `CREW25-OCT`), 2-guest minimum, hard expiry 3-4 weeks out, created by FareHarbor support. The 7-day flow above becomes a countdown that runs until the code's real expiry: extra reminders at 2 weeks left, 1 week left, 3 days, and "last day." New leads who sign up close to an expiry get the next wave's code.

---

## 5. Long Nurture (everyone who didn't book, runs forever)

- **Weekly email, Thursday:** the reel newsletter already built in `.ses_campaign/winback_series.py` (8 done). Keep it on SES and extend to a 12-week rotating library so it never runs dry.
- **SMS: 1-2 per month max.** Only timely stuff: a date that just opened, Spooky Singles cruise (Oct), Christmas cruise, 4th of July, spring break. SMS lists burn fast (the June blasts ran 5-7.5% opt-outs), so treat each text like it costs $5.
- **Re-gift every 90 days, max.** "Your $25 is back, good 7 days." Keeps the gift feeling like a gift.
- **Sunset:** no opens/clicks in 120 days, one "should we stop?" email, then suppress. Protects deliverability.

---

## 6. Booking sync (what makes it hands-off)

The flow has to know when someone books or it keeps texting paying customers "your $25 expires tomorrow," which is the fastest way to annoy them.

- **Best:** ask FareHarbor support to enable a booking webhook to a small endpoint (AWS Lambda, same account as the unsubscribe Lambda) that marks the email/phone as "Booked" in the lead table. That exits them from the lead flow and starts post-trip.
- **Fallback:** a nightly job on davids-mbp-2 using the existing `fareharbor-brief` dashboard session to pull new bookings and push them to the lead table. Works, but it breaks when the login expires, so it needs a health alert.

---

## 7. Post-trip + repeat customers

| When | Channel | Message |
|---|---|---|
| 2 days before | SMS | Logistics (dock address 2515 E NASA Pkwy, parking, what to bring). Transactional, from the ops line is fine. |
| Day after | SMS | "How was it?" 4-5 stars goes to Google review link, anything lower goes to OpenCX for a human. |
| Day 3 | Email | Photos/reel from their date if available + **referral**: "Send a friend's crew out, they get $25, you get $50 toward your next one." |
| Day 3 | Email | Ask the one question that powers next year: "What were you celebrating, and when is it next year?" Save as a date field. |
| 6 weeks before that date next year | Email + SMS | "{Name}'s birthday is coming up. Same crew, same boat?" + $25 gift. |
| Day 60 | Email | "Run it back" offer, $25, good 30 days. |
| Then | Long Nurture | Customers get the weekly email but not the lead-flow stuff. |

The occasion-anniversary reminder is the single best repeat tool for a birthday/bach business. Almost nobody does it.

---

## 8. Bringing in this year's customers

- **Who:** everyone who booked in 2026 (278 bookings) plus their passengers who signed waivers (much larger group, since one person books for 10-20).
- **How:** FareHarbor Dashboard export (Reports, Bookings, 2026 date range, include contact email + phone). Waiver signer export from wherever waivers are stored. Import into the lead table as a segment "Customers 2026."
- **Consent:** bookers can get email (existing customer relationship, unsubscribe link on everything). SMS **only** for people with a documented marketing SMS opt-in, which per the June attestation includes the waiver checkbox. Keep that attestation file current.
- **Going forward:** automatic via the booking sync in section 6. Nobody exports anything again.

---

## 9. Waking up the dormant list

The list: 16,963 emails. **575 Subscribed, ~11,400 blank/unknown, ~4,900 "No" (never mail these, ever).** A lot of it goes back to 2014.

Blasting all 12k at once on a domain that just got fixed is how you land in spam permanently. Do it in waves through the existing SES setup:

1. **Week 1:** test sends to David, confirm inbox (not spam) in Gmail + iCloud.
2. **Week 1-2:** the 575 Subscribed. Warms the domain.
3. **Weeks 2-4:** the 11.4k blanks, 1,000-2,000/day, ramping. One email: "Still want party boat stuff from us? Here's $25 to say thanks." Two buttons: "Yes, keep me" and hosted one-click unsubscribe (URL-based List-Unsubscribe, no mailto, per the standing rule).
4. Anyone who clicks either "yes" or the Book button gets added to the lead system and joins Long Nurture.
5. One reminder 5 days later to non-openers. Then everyone who never opened or clicked is suppressed. Expect maybe 10-20% to survive. That's fine, those are the people who'll actually book.
6. Stop the send if bounces pass 3% or complaints pass 0.1% in any batch.

**Dormant SMS:** don't blast the 17k phone list again. The data is clear: 0 bookings from MAY20, 0 replies from the 30-variant test, 5-7.5% opt-outs. Only text old contacts who re-engage via email and opt in fresh.

---

## 10. Other conversion levers (beyond the gift)

Ranked by bang for effort:

1. **Missed-call text-back.** 33% of calls go unanswered (56% in 2024), mostly during evening cruise hours. Auto-text every missed caller within 60 seconds with the booking link and "reply here, we'll answer." These are the hottest leads in the whole business.
2. **Speed-to-lead on replies.** When someone replies to a text, answer in under 5 minutes. The AI responder already on Railway handles this; point the new marketing number at it too.
3. **Solve the organizer problem.** The person booking has to collect money from 15 friends. Show per-person price everywhere ("from $X/person"), and if FareHarbor supports deposits or split payment on the private charter, turn it on and say so on the page.
4. **Real scarcity.** "3 Saturdays left in October." Pull it from availability, never fake it.
5. **Reviews on the tour page,** right next to the Book button.
6. **Referral program** (section 7). Party customers are the best acquisition channel you have, because every guest is a future organizer.
7. **Seasonal calendar** so there's always a reason to message: Spooky Singles (Oct), Christmas cruise (Dec), spring break, Mother's Day, graduation, 4th of July fireworks.

---

## 11. Keeping it hands-off

- Flows run in AWS (Lambda + scheduled runner) and Railway. No laptop jobs in the critical path.
- The weekly email library is pre-built 12 weeks deep.
- **Monthly auto-report** (Claude job on davids-mbp-2, first Monday): leads captured, capture rate, gift redemptions from the FareHarbor promo report, flow revenue, unsubscribe/complaint rates, and anything broken. Lands in `Marketing/` and pings David only if something's off.
- **Every 90 days:** swap the gift code month, refresh 3-4 reels in the weekly rotation. 30 minutes, Connor can own it.

---

## 12. Rollout

| Week | What ships |
|---|---|
| 1 (now) | SES MAIL-FROM is Success (done). Inbox placement test. Settle the SMS number question. Email FareHarbor to create `CREW25-OCT` ($25, 2-guest min, expiry ~4 weeks out). Build the lead-capture Lambda + table. |
| 2 | Popup + mobile bar live (email only until SMS number approved). New Lead flow emails live. Start 575 Subscribed send. |
| 3 | Import 2026 customers. Post-trip flow live. Booking sync (webhook or nightly). Begin dormant re-permission waves. Missed-call text-back. |
| 4 | SMS steps switch on once number is approved. Meta lead-form ads. Referral offer. |
| 5+ | Party planner lead magnet. First monthly report. |

---

## 13. What success looks like (honest math)

- Off-season traffic ~9,000 sessions/mo. A decent popup catches 2-4% → **180-360 leads/month.**
- Lead flow with an expiring gift typically converts 4-8% → **7-29 extra bookings/month**, about **$1.7k-7k/month** at $243 avg, less the $25 gifts.
- Spring/summer traffic roughly doubles, so does this.
- The dormant list is a one-time bump, not a machine. The machine is capture + nurture + repeat.

---

## 14. Decisions

- **Decided (Sep 29):** $25 code with a 2-guest minimum, FareHarbor-created, expires 3-4 weeks out, with countdown emails. Custom SES + Twilio build.
- **Open:** reuse the Lone Star Twilio number, or add an HPB number on the same account (recommended).
- **Open:** Connor owns the 30-min quarterly refresh?
- **Status:** David is reviewing the plan before any build starts.

---

## Build status (Sep 29, 2026)

- **Live in AWS:** capture API, 15-min flow runner, popup widget, per-brand unsubscribe, booked-stop endpoint, error alerts. Code: `~/Projects/fh-lead-engine` (multi-brand rollout: `ROLLOUT.md` there).
- **Tested:** welcome email landed in Gmail inbox (not spam). Booked, unsubscribe, and runner paths verified.
- **Previews:** `Marketing/Lead Gift Flow Previews/index.html`
- **Waiting on FareHarbor** (draft in houstonpedalbarge@gmail.com, not sent): create CREW25 ($25, 2+ guests, expires Oct 31), add the header script, gift card promo question, booking webhook.
- **Must build before Oct 17:** booking sync (first countdown email goes out that day).
- **SMS:** off until the number question is settled.
