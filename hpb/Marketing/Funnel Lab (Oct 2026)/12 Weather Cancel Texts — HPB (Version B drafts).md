*Drafted 2026-10-15 by the HPB funnel session. DRAFT. Nothing sent, nothing changed in FareHarbor, OpenCX, Twilio or the site. Board card c04 is parked; these exist so David can say go without a second drafting round.*

# Weather cancel texts for HPB: Version B (guest picks refund or 120% credit)

## Why HPB needs its own set

- 17 of HPB's 19 low-star reviews are cancel or refund complaints. 9 one-stars landed after the Jun 6 2026 storm trip, 8 of them in one day. 6 of 72 chat sessions are that same event: refund promised in a public reply, not received, no answer in private. (01 Customer Truth)
- The live cruise page says only "72 hour cancellation policy" and has no weather line at all (checked 2026-10-15). The vault bot docs say weather cancel = full refund or free reschedule, guest's choice. Guests are finding out the rule at the dock.
- The vault Weather Hold Protocol is clear on the rule: lightning within 5 miles, visibility under half a mile, or a USCG advisory = cancel, no discretion. Rain without lightning = we go, both boats have roofs. Wind 20+ sustained = default cancel. That rule is what the texts below say out loud.
- The current guest template (SOP Guest Communication Templates) is an email: reschedule or "full refund, processed within 3-5 business days". It has no SMS version, no refund-status follow-up, and no credit option.

## What Version B changes and what it does not

| | Today | Version B |
|:-|:-|:-|
| Weather cancel offer | Reschedule or full refund | Reschedule, full refund, or a credit worth 120% of what you paid (12 months, shareable) |
| Policy change needed | none | none. Full refund stays on the menu, so the live and vault promises stay true |
| SOP line "Full refund for any weather cancellation, no partial credits" | as is | needs one added sentence: "A credit worth more than the booking, offered as a choice beside the refund, is not a partial credit." [David to OK] |
| Refund status | silent after the promise | an automatic "your refund is on its way" text with the date the money moves |
| Who gets which arm | n/a | EVEN FareHarbor booking number = control (today's offer), ODD = Version B |

Credit math at HPB's live prices (120%):

| Paid | Credit |
|:-|:-|
| 1 public seat, $55 | $66 |
| 4 public seats, $220 | $264 |
| Private barge deposit only, $150 | $180 |
| Private barge paid in full, $800 | $960 |

If FareHarbor cannot issue a gift card above the booking value, the credit becomes a promo code tied to the guest's email (same as file 10, step 1).

## The texts (plain ASCII, paste-ready, signed as the business)

Placeholders in [BRACKETS]. Every text goes only to guests who gave a mobile number at booking. Under 320 characters each so they stay at two SMS segments. Sender number: [VERIFY, see open question 7].

**T0. Morning weather watch (day of, by 7am, only when the forecast is in doubt)**
> Houston Party Barge: Heads up, we're watching the radar for your [TIME] cruise today. Rain alone doesn't stop us (the barge has a roof). Lightning within 5 miles or a Coast Guard advisory does. We'll text a final call by [TIME MINUS 90 MIN]. No text means we're going.

**T1-B. Weather cancel, Version B arm (ODD booking numbers)**
> Houston Party Barge: We have to cancel your [TIME] cruise on [DATE]. [REASON: lightning within 5 miles / fog on the lake / Coast Guard advisory], and we don't gamble with that. Sorry, we know you planned around it. Pick one, just reply with the word:
> REFUND = full refund to your card, back in 3-5 business days
> CREDIT = $[CREDIT] (20% extra) good 12 months, use it any day or give it away
> Or move your date now: [REBOOK LINK]

**T1-A. Weather cancel, control arm (EVEN booking numbers, today's offer written cleanly)**
> Houston Party Barge: We have to cancel your [TIME] cruise on [DATE]. [REASON], and we don't gamble with that. Sorry, we know you planned around it. Reply REFUND for a full refund (3-5 business days) or move your date now: [REBOOK LINK]

**T2. Reply to REFUND (both arms)**
> Houston Party Barge: Done. $[AMOUNT] is going back to the card ending [LAST4]. We sent it [TODAY]; most banks post it in 3-5 business days, some take up to 10. If it hasn't landed by [DATE PLUS 10 BUSINESS DAYS], text this number and a person will chase it the same day.

**T3. Reply to CREDIT (Version B arm only)**
> Houston Party Barge: Your $[CREDIT] credit is set. Code [CODE], good through [DATE PLUS 12 MONTHS], on any public seats or the whole barge, and you can hand it to a friend. If you can't use it before then, text us before it expires and we'll refund the $[ORIGINAL] you paid. Book here: [REBOOK LINK]

**T4. No reply after 24 hours (both arms)**
> Houston Party Barge: Quick follow-up on your cancelled [DATE] cruise. We haven't heard which you'd like, so we'll send a full refund of $[AMOUNT] to your card on [DATE PLUS 1 DAY] unless you reply CREDIT or pick a new date first: [REBOOK LINK]

Note for T4 in the control arm: drop "or reply CREDIT". Defaulting to the refund keeps the SOP true and stops the "promised, never received" review.

**T5. Refund landed (both arms, sent when FareHarbor shows the refund settled)**
> Houston Party Barge: Your $[AMOUNT] refund has been sent and should be on your statement now or within a couple of days. Sorry again about the weather. When the sky behaves, we'd love to have you out: [BOOK LINK]

**T6. Shortened trip (came back early for lightning, both arms, Version B wording shown)**
> Houston Party Barge: Thanks for rolling with the early return today, lightning moved in faster than the radar said. We're giving you [FULL REFUND / HALF BACK] for the cut-short cruise. Reply REFUND for cash to your card, or CREDIT for $[CREDIT] (20% extra) good 12 months.
> [VERIFY: the Weather Hold Protocol says a shortened tour gets a full refund. Keep that unless David changes it.]

**T7. Public cruise cancelled for low seats (not weather, but the same refund complaint)**
> Houston Party Barge: Your [DATE] [TIME] public cruise didn't reach the minimum of 5 seats, so it can't run. Sorry about that. Reply MOVE and we'll put you on another public time this week at no charge, reply REFUND for a full refund (3-5 business days), or reply CREDIT for $[CREDIT] (20% extra) good 12 months.

## Credit confirmation email (goes with T3)

> Subject: Your $[CREDIT] Houston Party Barge credit is ready
>
> Hi [FIRST NAME],
>
> Weather won on [DATE], so here is your credit: $[CREDIT], good through [EXPIRATION]. Code: [CODE].
>
> Use it on public seats or the whole barge, hand it to a friend, or reply here and we'll book it for you. Fall is the best weather of the year on Clear Lake, and the sunset cruises fill first.
>
> If your plans change and you can't use it, reply before it expires and we'll refund the $[ORIGINAL] you originally paid.
>
> Houston Party Barge
> (832) 974-0365 | houstonpedalbarge@gmail.com

## How the split runs

1. Cancel decision is made per the Weather Hold Protocol (captain or manager). Reason logged in FareHarbor as WEATHER, LOW-SEATS, GUEST, STAFFING or NO-SHOW. Without the reason tag nothing below can be counted.
2. Whoever texts checks the booking number. Odd = T1-B. Even = T1-A. Same person, two saved templates.
3. T2, T3, T4, T5 fire from the same saved set. T4 is the one that stops the "promised, never received" review: it sets a date and a default.
4. Monthly read, 1st of the month, from FareHarbor: weather cancels per arm, credit-take rate, credits redeemed at 30/90/180 days, rebook within 45 days, refund dollars, and any 1-2 star reviews mentioning refunds. One row per month on the board card.
5. Stop rule: 2 or more angry reviews about the credit offer in a month, pause and look.

Sample reality at HPB: the boats cancel for weather less than the kayak brands. Expect this to read over a season, not a month. The refund-status texts (T2, T4, T5) are worth running in both arms from day one regardless of what the credit arm shows, because they fix the review problem on their own.

## Open questions for David (also in the session's numbered list)

- Run Version B at HPB this fall, or hold until NKST/BBK/LSKT read first?
- 120% or 115%?
- Who sends weather texts today at HPB, and from what number? The lead engine has sms_enabled false and no HPB number; the Lone Star Twilio reuse is still open. [VERIFY]
- OK to amend the one SOP line about partial credits?
- Refund timing: is "3-5 business days" true for HPB's FareHarbor refunds, or does it run longer? The texts promise it, so it has to be real.
