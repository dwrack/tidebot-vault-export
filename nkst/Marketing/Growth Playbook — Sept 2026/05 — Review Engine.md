# 05 — Review Engine

*Growth Playbook, September 2026. Facts come from [[00 — Fact Sheet & Open Questions]]. The shared SMS, email, sender and link rules are in [[04 — Abandoned Inquiry & Booking Follow-Up]] §0 and are not repeated here.*

**Status: DRAFT.** Nothing here is live. GHL, FareHarbor, GBP and SMS changes need David's sign-off. Items marked **PROPOSED** are ideas, not decisions.

**Builds on:** [[Marketing/2026-09-02 GBP Listing Audit & Improvement Plan — NKST]] (fix #5, review velocity), [[NKST — Sales Process & SMS Playbook]] §6, [[NKST — Customer Journey Map]] Stages 5–6, [[NKST — Affiliate & Partner Program]] Priority 4 (the guide end-of-tour ask), [[NKST — Chatbot & SMS Script v2]] (Messages 4–5), [[Operations/Incident Report Template]].
**Supersedes:** the review-request templates in Sales Playbook §6, Journey Map Stage 6 and Chatbot v2, and the guide script wording in the Affiliate doc. The reasons are in §13. The main one: several of the old scripts say "if you had a good/great time," and that conditions the ask on sentiment.

---

## 1. The goal

**Goal: net +40 Google reviews a month, to win back the review lead in the kayak swamp tour category.**

It's a goal, not a forecast.

### Where we are
| | Value | Source |
|---|---|---|
| Google reviews, Aug 11 | 1,416 | GBP audit |
| Google reviews, Sep 2 | **1,401** (4.9★) | GBP audit |
| Change in 22 days | **−15** | Reviews are being removed or filtered faster than new ones land |
| Top kayak competitor in the same category | 1,785 (5.0★) | GBP audit. Not named in guest-facing copy, per voice rules. |
| **Gap** | **384 reviews** | |

### What the goal takes
- **Gross new reviews needed per month = 40 + reviews removed per month.** At the Aug–Sep pace (−15 in 22 days), removals are at least ~20 a month. That puts the working gross target around **60 a month** until the removal rate is known.
- **Booking parties needed per month = gross target ÷ review rate per party.** At a 15% rate, 60 reviews needs about 400 completed booking parties a month. At 20% (the Sales Playbook target), it needs 300. **Open item for Ray:** pull the monthly completed-booking count from FareHarbor so this can be a real number instead of an estimate.
- **Time to close the gap = 384 ÷ (40 − the competitor's net monthly gain).** If they add 15 a month, that's about 15 months. If they add 30, it's about 38 months. **Record the competitor's count on the 1st of every month** (scorecard row 12). Without it, we don't know whether +40 is enough.
- **Seasonality:** winter volume is lower. Hold +40 as the monthly target and judge it on a rolling 3-month average.

### Why reviews might be disappearing (hypotheses, not findings)
Google doesn't say why a review is removed. The likely causes, and what this engine does about each:
1. **Bulk reviews from one place or device**, like a whole van reviewing on the same Wi-Fi within minutes. Mitigation: the SMS goes 1–2 hours after the tour, and later reminders spread across days. Guests use their own phones on their own data. **No company tablet, kiosk or van Wi-Fi review station, ever.**
2. **Anything that looks like an incentive or a selective ask.** Mitigation: §2 guardrails.
3. **Spillover from the 70116 listing cluster** (six controlled listings, one with a fabricated address). Mitigation: outside this file. It's GBP audit fixes #1 and #3.
4. **Normal spam-filter churn** on reviews from new or thin Google accounts. There's no fix. It's why the gross target sits above 40.

---

## 2. Guardrails (non-negotiable)

1. **No review gating.** Every guest who completed a tour gets the **same** review ask on the **same** schedule, whatever we think they felt. We never send a "how did we do?" filter first and then send the review link only to happy guests. That's prohibited by Google, and by the FTC's rule on consumer reviews (16 CFR Part 465, which bans review suppression).
2. **No incentives for reviews.** No discount, credit, drawing, gift or upgrade in exchange for a review, on Google or TripAdvisor. That includes "leave a review and show us for…". Incentives **are** allowed for **photo sharing** and **referrals**. Those always go in **separate messages** from the review ask, and they never depend on leaving a review.
3. **Ask for an honest review.** Never "5 stars," never "if you loved it."
4. **No reviews from conflicted people.** Staff, guides, family, affiliates and partners paid under [[10 — Referral Program]], and comped fam-trip guests don't get the review sequence. Tag them `no-review-ask`.
5. **The "anything off?" line is added to the review ask, never swapped in for it.** A guest who reports a problem keeps getting the same review messages as everyone else (see §9). The only things that stop the sequence are: they left a review (any rating), they opted out, or they asked us to stop.
6. **Guides never watch or help a guest write a review**, never ask to see it, and never type it for them.
7. **No review requests to guests whose tour we cancelled** (weather) and no requests to no-shows. They didn't have the experience.

---

## 3. Trigger and data (contractor spec)

**Trigger:** the FareHarbor booking status is **checked-in** (or "completed") **and** the availability end time has passed. Wait **75 minutes** after the scheduled end time, then start the workflow.

| Field | Source | Used for |
|---|---|---|
| `first_name`, phone, email | FH booking contact | Delivery |
| `tour_name`, `tour_date`, `end_time` | FH availability | Timing and copy |
| `guide_name` | FH staff assignment on the availability. If FH doesn't pass it by webhook, Ray sets it from the Guide Tour Log. (TourOpp GO pulls it natively per the Sales Playbook.) | Personalization and leaderboard |
| `booking_source` | FH (direct / Viator / Expedia / TripAdvisor / partner code) | Rotation (§6) |
| `party_size` | FH | Scorecard |
| `used_shuttle` | FH add-on | "on the ride back" wording |

**Excluded:** no-shows (not checked in), weather cancellations, tags `no-review-ask`, `staff`, `partner`, `do-not-market`, and anyone who got the review sequence in the last 90 days (repeat guests).

**One system only.** Before launch, **turn off** any FareHarbor-native post-trip review email, TourOpp GO review message, or guide-sent template review text that overlaps. Two review requests on the same evening reads as spam.

**Quiet hours:** a 4:30 PM tour ends around 6:45 PM, and +75 minutes puts R1 at about 8:00 PM. That's fine. **If R1 would land after 8:45 PM, hold it to 9:00 AM the next day and push R2 back to 11:00 AM.**

---

## 4. The guide's end-of-tour script

**When:** at the takeout once gear is stowed, or on the shuttle ride back for van guests. Give it to **everyone**, in the same words. It takes 30 seconds.

> "Before we head back, three quick things.
>
> One: you'll get a text from Ray at New Orleans Kayak Swamp Tours in a bit, with a link to Google. If you've got two minutes tonight or tomorrow, an honest review really helps a small crew like ours. And if you mention your guide by name, that's me, {{guide}}, we see it, and it means a lot.
>
> Two: if anything today wasn't right, tell me now or reply to that text. I'd much rather hear it from you.
>
> Three: that same text has a link to upload your photos. Send us your best ones and I'll add the group shots I took."

**Rules for the guide:**
- Same script for every group, including the quiet ones and the group that got rained on. **Don't pick who hears it.**
- Don't say "five stars," "if you loved it" or "if you had a great time."
- Don't pull out your phone to show them the review page, and don't pass around a QR code at the takeout. The text does that later, which spreads out when and where the reviews get posted (§1 hypothesis 1).
- **Accountability:** the post-tour guide check-in text asks "End-of-tour ask made? 1=yes 2=no." This is the check the Affiliate doc proposed. A "no" goes on the scorecard, but it isn't punished. We want to see the pattern.

**Short version for self-drive guests at the launch:**
> "You'll get a text from Ray later with a Google link. An honest review helps us a lot. And if anything was off today, reply to that text and tell us."

---

## 5. Sequence timeline

| Step | When | Channel | Purpose | Stops if… |
|---|---|---|---|---|
| **R0** | End of tour | Guide, spoken | Review + "anything off" + photos | — |
| **R1** | Tour end +75 min (quiet-hour rule applies) | SMS | Google review ask + "anything off" | — |
| **R2** | Next morning, 9:30 AM | Email | Review ask + photo upload + "what you saw today" | Review detected |
| **R3** | Day 3, 11:00 AM | SMS | Reminder. Platform per §6. | Review detected |
| **P1** | Day 5, 10:00 AM | Email | **Photo sharing (UGC)**. Separate from reviews. May carry the PROPOSED photo incentive. | Photos uploaded |
| **R4** | Day 7, 11:00 AM | SMS (email if no SMS consent) | Final review ask. Platform per §6. | Review detected |
| **F1** | Day 10, 10:00 AM | Email | **Referral launch** → hands off to [[10 — Referral Program]] | Referral code already issued |
| — | Day 30+ | — | Joins the past-guest list (seasonal newsletter and Chevy's Welcome Back flow) | — |

**"Review detected"** means a new Google or TripAdvisor review whose reviewer name matches the guest (first name + last initial), found by GHL Reputation Management if it can connect to GBP, or by Ray's daily manual check (§11). A match stops **only the review reminders**, for **any** star rating. P1 and F1 still send.

---

## 6. Platform rotation logic

Google is the priority. TripAdvisor is second. Rotation follows what the guest has already done, not a coin flip:

| Condition | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Default (booked direct or by partner code) | Google | Google | Google | Google, or TripAdvisor if they clicked the Google link at R1–R3 but no review was found |
| Clicked the Google link at R1 or R2 | Google | Google | **TripAdvisor** ("If you already did Google, thank you…") | TripAdvisor |
| Booked through **Viator or TripAdvisor** | Google | Google | Google | Google. **Never ask for TripAdvisor.** Viator already asks them, and Viator reviews feed TripAdvisor. |
| Booked through **Expedia** | Google | Google | Google | Google |
| Review detected on Google | stop | stop | TripAdvisor (one ask only) | stop |

**Why click-based:** someone who clicked the Google link has probably reviewed already, even if we can't match the name. Asking them for Google again is annoying, and TripAdvisor is a useful second place.

**Monthly check:** if TripAdvisor is falling behind (for example, no new TripAdvisor reviews in 30 days), send R3 as TripAdvisor to 25% of default contacts for the next month (GHL random split). Switch back once it recovers. Google stays about 80% or more of all asks.

---

## 7. Copy

Placeholders: `{{guide_name}}` has a fallback version for when it's empty. `{link:review_google}` points to the GBP "write a review" URL (`g.page/r/...`) behind the branded link domain. `{link:review_ta}` points to the TripAdvisor write-review page. `{link:anything_off}` is a short GHL form ("What was off? Ray reads every one."). `{link:photos}` is the upload form (§8).

### R1 — SMS (tour end +75 min)
**With a guide name:**
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Thanks for paddling with {{guide_name}}. An honest Google review helps: {link:review_google} Reply STOP to opt out.
```
*(~168 chars, so 2 segments with a long first name or guide name. We think the guide name is worth the second segment. In the first month, test it 50/50 against the version below, and measure review rate and guide mentions.)*

**Without a guide name:**
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Thanks for paddling with us. An honest Google review helps: {link:review_google} Reply STOP to opt out.
```
*(~158 chars)*

**Follow-on SMS, sent 1 minute later (same step. It's what makes it non-gating: the review ask goes out first and doesn't depend on the answer):**
```text
And if anything today was off, just reply here. I read every one. - Ray
```
*(~72 chars)*

### R2 — email (next morning, 9:30 AM)
**Subject:** Thanks for paddling with {{guide_name}} yesterday
*(no guide name: "Thanks for paddling Manchac with us yesterday")*
**Preview:** One small favor, your photos, and what you saw out there.

> Hi {{first_name}},
>
> Thanks for coming out to the swamp yesterday. {{guide_name}} said it was a good group.
> *(Only include that line if the guide confirms it in the check-in text. Otherwise leave it out.)*
>
> **One small favor.** We're a small local crew, and most people find us through Google reviews. If you've got two minutes, an honest review of your tour helps more than you'd think. Mentioning your guide by name helps too:
>
> **{link:review_google}**
>
> **Your photos.** Got good shots? Upload them here and {{guide_name}} will add the group photos from the tour: **{link:photos}**
>
> **What you saw.** Reading up on it afterward is half the fun:
> - The Maurepas Swamp is the second-largest bald cypress swamp in the U.S. It was clear-cut once, and everything you paddled through is regrowth.
> - Louisiana has about 40% of the country's coastal wetlands, and it loses land fast.
> - Alligators came back from near-extinction after hunting was banned. They're one of the great conservation comebacks.
> - Want the bird names? {link:blog_birds}
>
> **Anything off?** If something about your tour wasn't right, the van, the timing, anything, reply to this email. It comes straight to me, and I'd rather know.
>
> Ray
> New Orleans Kayak Swamp Tours · (504) 571-9975

*Fact-check note: the ecology lines come from the guide talking points in the Journey Map, Stage 5. Link the bird guide to the matching post in `Marketing/Blog Drafts - Staged/` once it's live.*

### R3 — SMS (Day 3)
**Google version:**
```text
{{first_name}}, Ray here from the swamp tour. If you haven't had a minute yet, an honest Google review would mean a lot: {link:review_google}
```
*(~140 chars)*

**TripAdvisor version (per §6):**
```text
{{first_name}}, if you already did Google, thank you. TripAdvisor is the other place travelers find us: {link:review_ta} - Ray
```
*(~125 chars)*

### P1 — email (Day 5) — photo sharing (UGC)
**Subject:** Got a good swamp photo?
**Preview:** Share your best shots. We'd love to feature them, with credit.

> Hi {{first_name}},
>
> The best photos of the swamp don't come from us. They come from guests. If you got a heron, a gator, or just the light through the cypress, we'd love to see it.
>
> **Upload here: {link:photos}**
> Or post it and tag **@neworleanskayakswamptours** on Instagram.
>
> [**PROPOSED incentive block. Needs David and a FareHarbor gift-card item:** *Upload 3 or more photos and we'll send you a $10 credit toward your next tour, or to pass to a friend. It's a thank-you for the photos, and it isn't connected to reviews.*]
>
> If we feature one, we'll credit you by first name or your handle, whichever you prefer.
>
> Ray

**Photo release line (on the upload form, as a required checkbox; legal review before launch):**
> ☐ *I took these photos, or I have permission from the people in them. I give New Orleans Kayak Swamp Tours permission to use them on its website, social media and ads, with credit if I ask. If anyone pictured is under 18, I'm their parent or guardian. I can ask for any photo to be taken down at any time by emailing Ray.*

### R4 — SMS (Day 7) — final
**Google version:**
```text
{{first_name}}, last nudge from me. If you have 2 min, an honest Google review of your swamp tour helps a lot: {link:review_google} Thanks - Ray
```
*(~145 chars)*

**TripAdvisor version:**
```text
{{first_name}}, last nudge from me. If you have 2 min, an honest TripAdvisor review helps travelers find us: {link:review_ta} Thanks - Ray
```
*(~140 chars)*

**Email fallback (no SMS consent). Subject:** Last favor, then I'll stop asking · **Preview:** Two minutes, an honest review, and thanks for paddling with us.
> Hi {{first_name}}, last note on this. If you haven't had a minute, an honest review of your tour would help us a lot: **{link:review_google}**. And if anything was off, reply here. — Ray

### F1 — email (Day 10) — referral hand-off
The copy is in [[10 — Referral Program]] §7 (email G1). It's sent as its own email, with no review ask in it.

---

## 8. Photo sharing and UGC mechanics

- **Upload form:** a GHL form with a file-upload field (multiple files), `tour_date` pre-filled, an optional Instagram handle, and a credit preference (first name / handle / none). The required release checkbox is in §7 P1. The files go to a shared "Guest Photos" folder, sorted by month.
- **Guide photos:** guides upload 2–3 group or wildlife shots per tour to the same folder the same day (the Journey Map idea, now standardized). R2 promises them, so the guide has to deliver them. The guide check-in text asks "Photos uploaded? 1=yes."
- **Use:** Instagram (with the credit the guest chose), GBP photo uploads (they help freshness; the GBP audit notes the last photo is 22 days old), and blog posts.
- **The incentive (PROPOSED)** is paid for photos, not reviews, and it's issued whether or not the guest ever reviews.

---

## 9. Negative-experience recovery (this is not a gate)

The review ask goes to everyone no matter what. This is a **separate, parallel** path, so problems get fixed and don't turn up for the first time as a 1-star review.

**It's triggered by any of these:**
- a reply to R1–R4 or R2 with complaint language (GHL keyword filter: "disappointed," "refund," "late," "rude," "unsafe," "didn't see," "waited," "wrong," or any reply Ray reads as a complaint)
- a submission on the `{link:anything_off}` form
- a guide check-in flag or an [[Operations/Incident Report Template]] filed for that tour
- a new review of 3 stars or fewer

**What happens:**
| When | Who | Action |
|---|---|---|
| Within 2 business hours | Ray | A personal reply (not a template): thank them, name the specific problem, say what happens next. Offer a call. |
| Same day | Ray | Log it in `Customer Issues/` with the date, tour, guide, issue and resolution. Tag the contact `issue-open`. |
| Within 48 hrs | Ray (David approves anything that costs money) | Resolve it: an apology, a rebook, or a partial or full refund per policy. **Nothing is conditioned on a review, or on changing a review.** |
| After it's resolved | Ray | Tag `issue-resolved`. Don't ask them to update or remove a review. If they bring it up themselves, "you're welcome to, but no pressure at all" is the only allowed answer. |
| Weekly | Ray | The scorecard shows the issues and the root cause (guide, van, timing, conditions) |

**What does not change:** an `issue-open` contact **stays in the review sequence** unless they ask us to stop messaging them. Stopping only unhappy guests would be gating by another name. **Exception:** if the guest is upset about the messages themselves, stop everything and tag `do-not-market`.

**Sample first reply (Ray, adapt it every time):**
> Hi {{first_name}}, thank you for telling me. I'm sorry about [specific thing]. That's not how it should go. Can I call you today or tomorrow to sort it out? Whatever time works for you. — Ray, New Orleans Kayak Swamp Tours, (504) 571-9975

---

## 10. Owner response templates

**Rules:** respond to every review. Reply to 1–3★ within **24 hours** (the Sales Playbook standard) and to 4–5★ within **72 hours**. Sign as `Ray, New Orleans Kayak Swamp Tours`. Name the guide if the guest did. Say one real thing about their review. Never argue, never share booking details, never name another company, and never stuff in keywords. Vary the wording, because copy-paste responses look automated.

### 5★ (three variants, rotate them)
> **A.** Thanks, {{reviewer_first_name}}. {{guide}} will be glad to hear the [heron / gator by the cypress knees / sunset paddle] made your day. Manchac never looks the same twice, so come back in a different season and see what's new. — Ray, New Orleans Kayak Swamp Tours

> **B.** {{reviewer_first_name}}, thank you for taking the time. We passed this to {{guide}}. Glad the group felt comfortable on the water, and first-timers are exactly who we love taking out. Hope to paddle with you again. — Ray

> **C.** Thank you, {{reviewer_first_name}}. Quiet kayaks and a good guide let the swamp do the talking, and it sounds like it did. See you next time you're in New Orleans. — Ray

### 3★
> Thank you for the honest review, {{reviewer_first_name}}. I'm glad [the positive thing they named] worked, and I hear you on [the specific issue]. That's something we're looking at. If you're open to it, I'd like to hear more. Call or text me at (504) 571-9975. — Ray, New Orleans Kayak Swamp Tours

*(Examples of what to name: the wait at pickup, fewer gators than hoped. For gators, say plainly that they're common, not guaranteed, and that we don't bait them. Don't make excuses.)*

### 1★
> {{reviewer_first_name}}, I'm sorry. This isn't the tour we want anyone to have, and I'd like to make it right. Please call or text me directly at (504) 571-9975 so I can hear the whole story and sort it out with you. — Ray, New Orleans Kayak Swamp Tours

*(Keep it this short in public. Don't argue facts. If the review is false or from someone who wasn't a guest, reply politely anyway, and separately flag it to Google through the GBP "report review" flow. Never pay, pressure or offer anything to get a review removed.)*

### TripAdvisor
Same templates. TripAdvisor shows management responses at the top of the review, so keep the 1★ reply especially calm.

---

## 11. Weekly scorecard

Ray fills this in every Monday for the prior Mon–Sun. It sits next to the 04 KPIs.

| # | Metric | This week | Last week | 4-wk avg | Target |
|---|---|---|---|---|---|
| 1 | Completed booking parties (FH checked-in) | | | | — |
| 2 | Review sequences started (R1 sent) | | | | = row 1 minus exclusions |
| 3 | End-of-tour ask made (guide check-in "1") | | | | **100%** |
| 4 | R1–R4 Google link clicks (unique) | | | | 35%+ of row 2 |
| 5 | **New Google reviews (gross)** | | | | **~15/wk** |
| 6 | **Google total count (Mon 9 AM, from the listing)** | | | | |
| 7 | **Net change (row 6 − last week's row 6)** | | | | **+10/wk (≈ +40/mo)** |
| 8 | Implied removals (row 5 − row 7) | | | | trending down |
| 9 | Avg star rating of new Google reviews | | | | ≥ 4.8 |
| 10 | New TripAdvisor reviews | | | | 2+/wk |
| 11 | Responses posted within SLA (1–3★ in 24 h, 4–5★ in 72 h) | | | | **100%** |
| 12 | Competitor Google count (1st of month only) | | | | log it |
| 13 | Issues opened / resolved (§9) | | | | resolved within 48 h |
| 14 | Photo uploads (guests) / guide uploads | | | | |
| 15 | SMS opt-out rate on R1 | | | | < 2% |
| 16 | Review rate per party (row 5 ÷ row 2) | | | | 15–20% |

**How to count reviews without API access:** the GBP API route is currently blocked (the GBP audit: no `node`, and the wrong Google account in Chrome). Until that's fixed, Ray reads the live count off Google Maps every Monday at 9 AM, and scrolls "Newest" to count gross new reviews and guide mentions. It takes about 10 minutes. Once GBP access works, move this to GHL Reputation Management or the `gbp` MCP.

---

## 12. Guide leaderboard

**What it counts:** new Google and TripAdvisor reviews in the period that **mention the guide by name**, divided by tours that guide led (from the Guide Tour Log). Existing reviews already name Nick, Stephanie and Jacob often. That's the profile we want more of.

| Guide | Tours led (month) | Reviews naming guide | Mentions per 10 tours | End-of-tour ask rate | Photo upload rate |
|---|---|---|---|---|---|
| Nick | | | | | |
| Stephanie | | | | | |
| Jacob | | | | | |
| *(others from the Guide Tour Log)* | | | | | |

**How it's used:**
- It's posted monthly in the guide group chat. Recognition first: the top guide gets a shout-out in the monthly GBP or Instagram post (with their consent).
- **PROPOSED bonus (David to decide):** pay for **process, not outcomes**. For example, $X for a month with a 100% end-of-tour ask rate and 90%+ photo uploads. **Don't pay per review or per star.** Per-review pay pushes guides to pick who they ask, or to pressure guests. That's gating, and Google or the FTC could see it as review manipulation.
- Misspellings count ("Stephenie," "Jake"). Ray matches them by hand.
- A 1–3★ review naming a guide goes to a private coaching conversation. It doesn't go on the public board.

---

## 13. Contradictions found and what this file supersedes

| # | Where | What it says | What this file does |
|---|---|---|---|
| 1 | Journey Map Stage 6 verbal ask: "**If you had a good time**, a Google or TripAdvisor review…"; Affiliate doc Priority 4: "**If you had a great time**, tell one person… And leave us a Google review" | Asking only if they had a good time is sentiment-conditioned. That's soft gating. | **Superseded** by the §4 script: the same unconditional ask for everyone. |
| 2 | Sales Playbook §6 Template 1 and Chatbot v2 Msg 4: the guide sends the review text from their personal number | vs. automated, Ray-signed, one system | **Superseded.** Automated from the main line with the guide's name inserted. Guides make the verbal ask. This keeps it consistent and trackable, and guide numbers stay off the A2P hook. |
| 3 | Sales Playbook §6 "At 384+ reviews"; target "1 review per 5 tours" | The count is 1,401. The rate is measured per party, not per tour (a tour holds several parties). | Custom value for the count. The target is 15–20% of booking parties. |
| 4 | Sales Playbook §9: TourOpp GO handles "review request automation"; FareHarbor may also send post-trip emails | Double-sending risk | **One system.** Turn off the others (§3). |
| 5 | Journey Map Stage 5: "The tip and review ask at the end" | Fine, but tipping and reviews shouldn't be one breath | The guide script leaves out tipping. Keep the tip mention separate, at gear return. |
| 6 | Journey Map Stage 6 re-engagement: D+1 email / D+7 "come back" / D+30 "bring a friend" | Timing overlaps this sequence | D+1 becomes R2 (it keeps the "what we talked about" content). D+7 "come back" moves to the past-guest newsletter. D+30 "bring a friend" moves up to **D+10 (F1)**, while the tour is still fresh. |
| 7 | Sales Playbook §6 Template 1: "that big one at the second dock" (a specific detail) | Automation can't know the detail, and a made-up detail would be false | Only a guide-confirmed line is used (R2). Otherwise the copy stays general. |
| 8 | Sales Playbook §6 Template 3 (negative review reply) says "reach out … through NolaKayakTours.com" | The domain doesn't match the fact sheet | §10 templates use the phone number only. |
| 9 | Journey Map Stage 5: "Offer optional waterproof phone cases at pickup" | Doesn't exist yet | Referenced only as PROPOSED (04 §2). |
| 10 | GBP audit fix #5: "the strongest point is on the shuttle ride back" | Agrees | The verbal ask is on the shuttle. The **SMS link** goes 75 minutes after the tour so reviews spread out (§1 hypothesis 1). That refines the audit, it doesn't contradict it. |

---

## 14. Contractor build checklist

- [ ] Confirm the FH webhook carries check-in status, end time and guide/staff. If it doesn't, build Ray's manual guide-name entry.
- [ ] Turn off overlapping review messages (FH native, TourOpp GO, guide templates)
- [ ] Create the GHL workflow "Review Engine" with steps R1–F1, the quiet-hour logic (§3) and the rotation branches (§6)
- [ ] Create forms: `anything_off` and `photos` (with the release checkbox)
- [ ] Create branded links: `review_google` (GBP write-review URL), `review_ta`, `photos`, `anything_off`, `blog_birds`
- [ ] Set up the complaint keyword filter → task for Ray + tag `issue-open`
- [ ] Add "End-of-tour ask made?" and "Photos uploaded?" to the guide check-in text
- [ ] Add the §4 script to guide training and the Guide SOP
- [ ] Build the scorecard sheet (§11) and leaderboard (§12). Ray's Monday 9 AM task.
- [ ] Resolve GBP access (the owning Google account) so review detection and responses can move off manual checks
- [ ] Get David's sign-off on: the copy, the photo incentive (PROPOSED), the guide process bonus (PROPOSED), the photo release wording (legal)
