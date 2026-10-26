# The Go-Cup: Answer Inside the Email

*Drafted 2026-10-16 by David's Claude. Spec only, nothing built. David's ask: make it super quizzy, every tap saves to the person's record, and nobody gets bounced to a webpage.*

## The answer

**Yes, for most of the list, using AMP for Email.** AMP is a second version of the email that Gmail (and, per the AMP docs, Yahoo) renders with live buttons and forms *inside the message*. Tap an answer and it saves to our server, then the email itself updates ("Got it. 61% of locals agree with you."). No tab opens.

Everyone else gets the normal email, where a tap opens one small "Got it" page that shows the next question. They answer in one place and close it.

**Our list by email provider** (counted 2026-10-16 from `NOLA Party Barge Contacts — Clean Backup.csv`, 49,370 addresses):

| Provider | Share | What they see |
|:-|:-|:-|
| Gmail | **61.8%** | Native in-email quiz (if they read in the Gmail app or on gmail.com) |
| Yahoo / AOL | 23.6% | Native, if Yahoo still renders AMP (verify when registering) |
| Microsoft | 4.6% | Fallback: tap opens a one-question page |
| Apple (iCloud) | 4.3% | Fallback, plus trivia "reveals" that work inside Apple Mail |
| Other / work | 5.8% | Fallback |

Caveat: a Gmail address read in the iPhone Mail app shows the fallback. The provider is a ceiling, not a promise. The first sends will tell us the real split.

## What a tap does

1. Tap "I'm visiting Nov 14" or "Casamento's" or "I'm in" in the email
2. AMP posts `{contact_token, question, answer}` to our answers endpoint
3. The endpoint saves it to the contact's profile, updates tags, and replies with the result
4. The email updates in place: a checkmark, the live poll split, or the next question
5. Within a minute the same profile syncs to **OpenCX** (contact structured fields), so when they DM or chat, Nolan already knows "visiting Nov 14, group of 8, loves music"

The "CRM" here is the profile store behind the endpoint, which is the same engine as the survey contest funnel (`fh-lead-engine-survey`) plus the OpenCX sync. FareHarbor bookings attach by email, so a booking flips them from Just Visiting to the right edition automatically.

## Who's reading: four editions, switched by date

| They tell us | Edition | Content | When it flips |
|:-|:-|:-|:-|
| "I'm coming" + date | **Just Visiting** | The week they're here, countdown, what to book before they land | Trip date arrives: In Town |
| "I'm here right now" | **In Town** | Tonight and tomorrow only, short, where to go next | 3 days after the trip date: Another Round |
| "I've been" | **Another Round** | What's new since they were here, bring the crew back, Buy Your Friend a Round | They pick a new date: Just Visiting |
| "I live here" | **Yeah You Right** | This weekend, new openings, Locals' Pour first dibs | Never (unless they move) |

The date comes from the answer, from a FareHarbor booking, or from the funnel's `trip_month`. Without a date, it asks again in the next issue ("When's the trip?" as month buttons).

## The quizzy bits (every section has a tap)

| Section | The tap | Saves as |
|:-|:-|:-|
| **Who's Pouring?** (top, until we know) | Coming / Here now / Been / Live here, plus month buttons | `audience`, `trip_date` |
| **First Round** | "I'm in" on each pick, and we send a reminder the day before | `rsvp:<event>` + interest tag |
| **Pour Decisions** | Pick a side, and the live split shows right away | `poll:<id>` + tag |
| **Lagniappe** | True/false trivia, the answer reveals in place | `trivia_score` (bragging rights, a streak) |
| **Bartender's Choice** | 3-tap personality quiz, result in the email ("You're a Frenchmen Street Night Owl") | `persona` |
| **Last Call** | "Save me a seat" (hold interest, no payment) | `boat_interest`, a hot-lead alert to staff |
| **Next Round** | "What do you want next week?" | `topic_next` |
| **Your Tab** (bottom) | Shows what we know about them ("Visiting Nov 14 · into music · Night Owl"), with a fix-it button | Builds trust, corrects bad data |

Results come back in the next issue: "Last week's bar argument: 61% said Casamento's. You were with the majority." That's the reason to open next Thursday.

## Build list (the order matters)

1. **Answers endpoint**: a Cloudflare Worker + D1 (or the mbp-2 engine behind the Tailscale Funnel it already uses for the FareHarbor webhook). AMP needs HTTPS and its CORS headers. A Worker is sturdier than a laptop. Signed `contact_token` per recipient, so nobody can answer as someone else
2. **Profile store + OpenCX sync** (structured fields: audience, trip_date, tags, persona, last_answers)
3. **The fallback page**: `/a?t=<token>&q=..&a=..` records the answer, shows "Got it" plus the next question, mobile-first, the Go-Cup look
4. **The AMP template** (`text/x-amp-html` MIME part) beside the normal HTML. SES sends raw MIME, so `winback_sender_ses_v2.py` needs a third part. Gmail strips AMP from forwarded emails (fine, the forward gets the normal version)
5. **Register the sender with Google**: one from-address (`info@nolapartybarges.com` or a dedicated `gocup@`), SPF/DKIM/DMARC passing, then send a real production AMP email to Google's review address. Third-party guides say approval takes 1 to 4 weeks. **Start this first, it's the long pole**
6. **Apple Mail extras**: CSS tap-to-reveal for trivia (works offline). It does NOT record, because Apple's privacy proxy pre-loads images and makes image-based tracking unreliable

Until Google approves us, everyone gets the fallback, and the quiz still works with one tab.

## Rules

- Taps never sign anyone up for anything new. Unsubscribe stays the hosted one-click link (never by email)
- No payment or personal data inside the AMP form. Answers only
- "Save me a seat" creates a staff follow-up, not a booking or a hold in FareHarbor
- Show people their own tab. If we say "we know you love music," let them fix it

## Sources checked 2026-10-16

- [AMP for Gmail, Google developers](https://developers.google.com/gmail/ampemail/) (page updated 2026-08-28, still supported)
- [AMP sender registration walkthrough, Mailtarget](https://docs.mailtarget.co/amp-sender-registration-for-interactive-email) (secondhand: per-address approval, test send to Google)
- [Braze AMP docs](https://braze.com/docs/user_guide/channels/email/customize/amp_for_email/) (DKIM/SPF/DMARC needed)
- [Apple Mail Privacy Protection, SendGrid docs](https://docs.sendgrid.com/for-developers/tracking-events/understanding-apple-mail-privacy-protection-and-open-events) (images pre-fetched, so no reliable image-based click tracking)
