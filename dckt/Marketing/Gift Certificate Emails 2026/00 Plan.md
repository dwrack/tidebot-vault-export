# Holiday Gift Certificate Emails, 2026

Status 2026-11-05: DRAFT. Nothing sent. Email 1 is built (`email-1-the-one-gift-nobody-returns.html`, preview `email-1-preview.png`). Emails 2 to 6 are outlined below and get built after David approves email 1.

## Bottom line

- 6 gift emails from Nov 17 to Dec 29, plus the 2027 early-bird email already planned for Dec 1. That is 7 touches in 6 weeks. More than that on a list we have never mailed is asking for spam complaints.
- No discount. Site standards say no discount codes yet, and gift cards sell on convenience in December anyway. The hooks are: easy, instant, never expires, nobody returns it.
- Every email has one job: click through to https://www.doorcountykayaktours.com/gift-cards/ (tagged `ref=nl_giftNN_...`).

## The schedule

| # | Send | Hook | Subject A | Subject B | Preview line |
|---|---|---|---|---|---|
| 1 | Tue Nov 17, 7am CT | Memory. You know what this feels like. | The one gift nobody returns | Give them a morning on the water | Lands in their inbox in about two minutes. Never expires. |
| 2 | Sat Nov 28 (Small Business Saturday) | Shop small. We are a local outfit, since 2002. | A small-shop favor to ask | Skip the mall today | One gift card keeps a Door County crew working next summer. |
| (Dec 1) | Tue Dec 1 | 2027 early-bird, separate email | (already planned) | | |
| 3 | Wed Dec 9 | Gift guide by person: the dad who has everything, the teenager, the couple, the in-laws visiting in July. | For the person who already has everything | Who on your list would love this? | Four people this solves. You probably have two of them. |
| 4 | Wed Dec 16 | Shipping deadlines. Ours has none. | Shipping cutoffs don't apply to this | Still time. No box, no tracking number. | It's an email. It can't be late. |
| 5 | Wed Dec 23, 6am CT | Last minute, zero shame. Print it, fold it in a card. | Done in two minutes (really) | Forgot someone? | Buy it, print it, put it in a card. Nobody will know. |
| 6 | Tue Dec 29 | Gift yourself. Spend the Christmas cash on July. | Did you get cash for Christmas? | Something to look forward to | Winter is long. Put a July morning on the calendar. |

Email 5 gets one resend on Dec 24 at 8am, only to people who did not open it, with subject B.

## Why these subject lines

- Short. All under 45 characters so they do not cut off on a phone.
- Curiosity or a plain benefit, never both, never ALL CAPS, no emoji (first contact with a cold list).
- A/B test: send A to 10 percent and B to 10 percent, wait 3 hours, send the winner to the rest. Judge on clicks, not opens. Apple Mail inflates opens.

## Who gets it and how it goes out

- List: 31,751 past guests in `~/Projects/dckt-tools/newsletter-2026/recipients.json`. Nothing has ever been sent to this list from SES (only three test sends to David in June).
- Sender: SES us-west-2, from info@doorcountykayaktours.com. Checked 2026-11-05: domain verified, DKIM on, SPF includes amazonses.com, DMARC record exists (p=none).
- Unsubscribe: the hosted one-click page plus the `List-Unsubscribe` URL header. No mailto.
- Ramp for email 1, because the list is cold: 500 on day one (2025 and 2026 guests only), 2,500 the next day, 10,000 the day after, then the rest. Stop if complaints pass 0.1 percent or bounces pass 3 percent. NPB's win-back got halted at 10 complaints in 1,475 sends, so start with recent guests.
- Anyone who buys a gift card drops out of emails 2 to 5 and still gets email 6. (Needs the buyer list from FareHarbor each week. Manual pull until there is a webhook.)

## Open questions for David

1. $20 promotional credit: drop it, or use it as a bonus in email 4? (It was never sent on Nov 3. FareHarbor may not allow a promo code on gift card purchases.)
2. Gift card amounts: FareHarbor lets the buyer type any amount, or are there presets? Email 1 says "any amount."
3. Footer address: emails use 8442 State Hwy 42, Fish Creek. The live site footer says 6329 State Highway 57, Jacksonport. Which one?
4. OK to say "if the wind is wrong on their day we move it for free"? It matches the brand voice doc, but the cancellation policy wording is still being settled.

## Email 1 copy (as built)

Subject: The one gift nobody returns
Preview: Lands in their inbox in about two minutes. Never expires. They pick the day next summer.

HOLIDAY GIFT CARDS
**Give them a morning on the water.**

You've been out there with us, so you already know. The lake goes flat early, the caves open up, and for two hours nobody looks at a phone.

That's a hard thing to wrap. So we made it easy.

[Gift card panel] Any amount. Any tour. Any summer. In their inbox fast. Never expires. Good on everything. Button: Send a gift card

WHAT IT TURNS INTO
Two seats on a kayak tour. $69 a person. Sea caves at Cave Point or the shipwreck at Door Bluff. Guided, and built for first-timers.
An afternoon on e-bikes. $30 an hour. Fat tires, shoreline roads, and no one arrives sweaty.

Not sure they're a kayaker? Most of our guests have never done this before. We use wide sit-on-top kayaks, the guide does the worrying, and if the wind is wrong on their day we move it for free.

They pick the day next summer. You're done shopping today.

See you on the water,
The crew at Door County Kayak Tours
