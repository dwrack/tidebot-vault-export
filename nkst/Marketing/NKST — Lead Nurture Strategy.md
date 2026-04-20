# NKST — Lead Nurture Strategy

*Created: April 2026 | Source: Dylan onboarding session + email strategy frameworks*

---

## The Core Problem

Everyone is competing for the 3% of travelers who are ready to book right now. The other 97% are planning, browsing, dreaming — and they get ignored. By the time they're ready to book, they've forgotten you exist and whoever stayed in front of them wins.

The play: get into that 97% early, lead with value, and be the only brand they trust when they're finally ready to pull the trigger.

---

## The Lead Magnet

**"Win a Free Kayak Tour — Get the New Orleans Insider Guide"**

- **Channel:** Facebook ad targeting people who have expressed interest in New Orleans travel (not necessarily kayaking — wide top of funnel)
- **Ask:** Name, email, vacation month. Nothing else.
- **Platform:** GHL form → automatic tag → enters nurture sequence
- **Current status:** Form live in GHL. 3 contacts captured as of April 2026. Nurture sequence not yet activated.

The framing matters. We're not asking them to enter a contest. We're telling them: we're the locals. We know things the tourist blogs don't. Here's the insider guide to the city.

---

## Positioning: The New Orleans Insiders

NKST is not a tour company running a promotion. We are the people who actually live here, paddle these bayous, and know what's worth doing and what to skip.

The nurture sequence talks like that. Bayou St. John. The Lower Ninth. The bars the locals go to. Jazz Fest is not a secret — skip the generic stuff. What can't you Google?

When someone reads 6 emails from us that are genuinely useful and not salesy, we're not competing with anyone. We're the only name they remember when they decide to book an activity.

---

## Email Sequence Framework

**Cadence:** 2x per week from signup through trip date

**Tone:** Friendly local expert. Not a marketing department. Not a travel blog.

**Rule:** Never pitch in the first 3 emails. Lead with value. The tour is mentioned in passing — "by the way, this is what we do" — not as a CTA.

### Sequence Arc

| Email | Timing | Topic |
|---|---|---|
| 1 | Immediately | Welcome + "Here's what most tourists miss in New Orleans" |
| 2 | Day 3 | Neighborhoods worth leaving the French Quarter for (Bywater, Bayou St. John, Treme) |
| 3 | Day 7 | Food + bar guide — places that have been there 40 years and never showed up in a magazine |
| 4 | Day 10 | "You've probably seen the swamp tour ads. Here's what they don't tell you." (Differentiation — kayak vs. motorized) |
| 5 | Day 14 | Alligator culture, Manchac Swamp, the real ecosystem — educational, not a pitch |
| 6 | Day 21 | Social proof email: a few guest stories, what people said, guide spotlights |
| 7 | 6 weeks before trip date | First direct CTA: "You've got X weeks. Ready to book? Here's what's left." |
| 8 | 3 weeks before trip date | Upsell: Extended tour, Whitney Plantation Combo — framed as the difference between a good trip and an unforgettable one |
| 9 | 1 week before trip date | Final push: urgency, limited spots, direct booking link |

Trip date is captured on the form (vacation month). Use it to trigger the time-sensitive emails dynamically.

---

## The Upsell Path

The 2-hour tour is fine. The Extended tour is a masterpiece. The Combo (Whitney Plantation + Swamp) is something they'll talk about for years.

Don't introduce this in email 1. Earn the right to pitch it by delivering value first. By the time they're 3 weeks out from their trip, they trust us enough that the upsell lands like a recommendation, not a sales pitch.

---

## Ghost Tour Guide Partnership as Top-of-Funnel

Ghost tour guides are the single best referral source for this nurture sequence. They run at night, they have captive audiences of engaged tourists who just spent 2 hours getting into the culture of the city, and they ask "what are you doing tomorrow?"

The play:
1. Dylan goes on 2-3 tours, identifies the best guides
2. Takes one out for a beer, lays it out: "I want to send people your way. I want you to send people mine."
3. Propose adding a QR code to their tour materials or just a verbal mention: "If you want to see this city from the water, these are the people."
4. That ghost tour guest — now warm on NOLA culture, high-intent — gets the link to the free insider guide form and enters the nurture sequence

This is word-of-mouth that feeds a system, not just a one-time referral.

Full strategy in [[NKST — Affiliate & Partner Program]].

---

## CTA Placement on Website

Every blog post and activity page needs a secondary CTA below the fold:

> "Not ready to book yet? Get our free New Orleans Insider Guide — we'll show you the city the way the locals see it."

Links directly to the GHL lead capture form. This catches the 97% who landed on the site and weren't ready to book.

Priority page: the **alligators vs. crocodiles** blog post already gets thousands of organic views and currently has no CTA. That one first.

Action: email support@fareharbor.com with the CTA copy and ask them to add it to each page.

---

## Email Deliverability — What to Do Before Sending at Scale

Before this sequence runs to any real volume, the technical foundation needs to be right. One bad sender score wipes out all the work.

**The six things to fix:**

1. **Separate subdomains for marketing vs. transactional.** Transactional email (booking confirmations, receipts) and marketing email (nurture sequences) should never share a domain. One spam complaint on the marketing side will tank booking confirmation delivery. Use `mail.nolakakyaktours.com` for transactional, `news.nolakakyaktours.com` for marketing — or similar.

2. **DKIM + DMARC.** SPF alone is not enough. DKIM authentication + a DMARC policy (even `p=none` to start) can add 30%+ inbox placement. Set these up before the first broadcast goes out.

3. **Clean the list before activating.** Remove anyone who hasn't opened or clicked in 6 months. A clean list with 40% open rates beats a bloated list with 8% open rates every time — and the sender score reflects it.

4. **A/B test send times.** Don't assume Tuesday morning. One NOLA-specific travel audience may peak at 6am (coffee and planning mode), another at 8pm (evening browsing). GHL supports send time testing — use it.

5. **Preview text.** The default "View this email in your browser" appearing in inbox preview is wasted real estate. Good preview text (the 80-100 characters visible before opening) can add 10-15% to open rates. Write it intentionally for every email.

6. **Monitor blacklists weekly.** Check Spamhaus. A single listing can gut deliverability for weeks. Catch it early, delist before it compounds.

---

*Related: [[NKST — Affiliate & Partner Program]] | [[NKST — Customer Journey Map]] | [[Dylan — Onboarding Session (April 8 2026)]]*
