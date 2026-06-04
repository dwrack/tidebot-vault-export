# Guest Experience Survey — Email Campaign

*Drafted 2026-06-02. Sends via SendGrid from sauna@ebbandember.com.*

**Goal:** Drive completions of Jess and Hannah's Guest Experience Survey to learn who our guests actually are, feeding the brand-messaging work.

**Incentive:** Everyone who submits gets promo code `BRINGAFRIEND` = one free friend pass, any day, expires July 31. Code revealed on the form's confirmation screen.

**Survey link:** https://docs.google.com/forms/d/e/1FAIpQLScZ81zuHMWxGGq7Gn_CvH1s6I-V-kni1iGYJGcT0r7E62fBgA/viewform

---

## Email 1 — The blast

*Revised per Jess/Hannah feedback: tighter, leads with the friend pass, CTA up top.*

**Subject:** Get a Free Friend Pass!
**Preheader:** Ten questions, about five minutes.

Hi there,

We've put together a short Guest Experience Survey. As a thank you for providing your input, everyone who completes the 10-question survey gets a free friend pass: bring someone on the float with you, any day through July 31. You'll see the code onscreen after you submit the survey.

**[ Take the survey → ]**

We opened the float on January 1, and in these first months you've been part of figuring out what Ebb and Ember actually is. We want to keep getting it right, and that starts with knowing you a little better.

Your answers stay confidential and we'll never sell your information.

Whether you've made the float part of your week or came by once on a cold morning, your answer counts the same.

Thanks for being here in the early days.

The Ebb and Ember team
Ebb and Ember
Portland's floating sauna on the Columbia River
173 NE Bridgeton Rd, Portland OR 97211

*(Footer auto-appended by SendGrid Subscription Tracking, see fix note below.)*

---

## Email 2 — Reminder (non-openers, ~5 days later)

**Subject:** Last call on the float survey
**Preheader:** A few minutes, and a free friend pass.

Hi {{first_name}},

Quick nudge: our Guest Experience Survey is still open, and we'd really like your read on it.

Five minutes, ten questions. Finish it and you'll get a free friend pass to bring someone on the float, good any day through July 31.

**[ Take the survey → ]**

Already filled it out? Thank you, that's all we needed.

{{SIGN_OFF}}
Ebb and Ember
Portland's floating sauna on the Columbia River
173 NE Bridgeton Rd, Portland OR 97211

*(Unsubscribe footer is now auto-appended by SendGrid. See note below. Do not paste a literal `{{unsubscribe}}` into the body.)*

---

## Unsubscribe footer — FIXED 2026-06-04

The first blast went out with NO footer link, just reply-to-unsubscribe, which forced us to mine the inbox by hand (23 opt-outs). Fixed now:

- **SendGrid Subscription Tracking is ON** and auto-appends a footer with a working one-click unsubscribe link + mailing address to every send. Opt-outs now drop straight into SendGrid suppression automatically. No body tag needed.
- The footer reads: "Ebb and Ember · 173 NE Bridgeton Rd, Portland OR 97211 / You are receiving this because you opted in at ebbandember.com. / Unsubscribe from these emails".
- **DMARC is now live** (`v=DMARC1; p=none; rua=mailto:sauna@ebbandember.com`) after fixing a doubled-host typo in Squarespace DNS. Combined with the existing SendGrid DKIM/SPF, alignment is now complete.

---

## Before sending — checklist

**Form fixes (Jess / Hannah):**
- [ ] Remove the old drawing/giveaway language (the "drawn June 1" prize copy is stale)
- [ ] Set the confirmation message to reveal the code: "Thanks for filling this out. Use code BRINGAFRIEND for a free friend pass, good any day through July 31."
- [ ] Make the email field genuinely optional or remove it (no drawing means it's not needed)
- [ ] Fix "Ebb & Ember" → "Ebb and Ember" in the form title

**Periode:**
- [ ] Confirm `BRINGAFRIEND` is live as a free-friend-pass code, any day, expiring 2026-07-31

**Suppression list (scrub before every send):**
The master opt-out list now lives in `Marketing/Do Not Contact List.md` (30 people: 7 from April + 23 from the June blast). All are in SendGrid's global suppression, so SendGrid won't send to them regardless, but scrub the sheet too. The 23 June opt-outs are also flagged `Unsubscribed 2026-06-03` in the Master Contacts Status column (F), so just filter out non-blank Status before sending.

**Send:**
- [ ] Test send to Jess (jess@ours-here.com), Hannah (hannah@ours-here.com), Jonah (jonah@ohanaequities.com)
- [ ] Confirm sign-off name with Jess and Hannah
- [ ] Pull + clean recipient list from "Sauna Boat Opt in Form (Responses)" sheet, Master Contacts tab (~2,307), minus the 7 suppressions above
- [ ] A/B subject on a ~10% slice, send winner to the rest
- [ ] Throttle in waves (300-500/hour) to protect the fresh domain reputation
- [ ] Reminder to non-openers ~5 days after
