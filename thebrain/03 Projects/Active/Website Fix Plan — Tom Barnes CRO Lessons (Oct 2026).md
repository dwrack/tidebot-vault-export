# Website Fix Plan: Tom Barnes CRO Lessons (Oct 2026)

Source: all 51 posts on @tombarnesss_ (pulled 2026-10-18 via Apify, `ee` key). About half are lifestyle (cars, travel, Cyprus move). The useful stuff is his Aug-Sep 2026 CRO carousels plus ~16 business reels. He's a UK Shopify/e-com growth guy (TheSocialElevator), so everything below is translated from "product page / Shopify" to "tour page / FareHarbor lightframe."

## What he actually teaches (the 7 that matter for us)

1. **Surprise costs kill checkout.** 48% of abandons are fees that show up late (Baymard). Show the full landed price on the product page. A $45 all-in price beats $40 + $5.
2. **Diagnose before you redesign.** Conversion rate alone is useless. Find the leakiest stage (add-to-cart, cart to checkout, checkout completion), fix the earliest broken one first.
3. **Mobile is where the money leaks.** ~80% mobile cart abandonment vs ~68% desktop. Buy from your own site on your own phone, on cell data.
4. **Checkout friction:** express wallets (Apple/Google Pay) first, guest checkout, 8 fields or fewer.
5. **Pay-later messaging on the product page, not just checkout.** "or 4 payments of $29" under the price shrinks the decision.
6. **Never retire a best seller.** Keep the proven winner front and center; new stuff exists to find the next winner.
7. **Fix the site before buying more traffic.** His case: same spend, 2x to 3.45x ROAS from cutting leaks + CRO. More visitors into a leaky funnel = more expensive leaks.

His reels (15 described with Gemini, 2026-10-18) back up the same points: "stop charging for shipping, put it in the price" (our version: stop adding fees at checkout), "offer every payment option" (Apple Pay, PayPal), a **three-color rule** for site design (less is more), and "if ROAS drops when you raise budget, the problem is the funnel, not the ads." The rest is lifestyle flex (Cyprus, Lambos) built for loops, not lessons. Full reel breakdowns: scratchpad only, ask if you want them filed.

Content lesson for us too: every post is one problem, one stat, one free fix, then "Comment WORD and I'll send the checklist." Value first, ask second. That's the opposite of an email gate (see bottom).

## What I found on our sites (checked live 2026-10-18)

| Check | Result |
|---|---|
| Prices visible on homepages | Yes, all 6 FH sites (NPB, NKST, BBK, AKT, HPB, DCKT) |
| Fee disclosure near price | None found on any homepage ("fee"/"tax"/"per person" basically absent) |
| **HPB real checkout** | Advertised **$50/person**. 2 people: subtotal $101.50 (1.5% card fee) + **$14.45 taxes & fees** = **$115.95**. That's **16% more than the sticker**, revealed only at the last step. This is exactly his #1 leak. |
| HPB checkout length | Trip protection upsell per person, "how did you hear" dropdown, 5 add-on products, card disclaimer checkbox, SMS consent, a long cancellation block, then contact + payment fields. Way over 8 fields. |
| Pay-later / Affirm messaging | None on any site |
| Free cancellation / refund line near price | Only NKST mentions refunds |

Not yet checked: the other 5 brands' checkout totals (likely the same FH fee setup), GA4 funnel stage rates, Clarity mobile recordings.

## The plan (in order)

### Week 1: measure the leak (no site changes)
- Pull each brand's GA4 funnel for the last 90 days: tour page view, lightframe open, begin_checkout, purchase. Split mobile vs desktop. Find the worst stage per brand. (Watch out: E&E showed most "abandons" are expired holds that rebook, so cross-check against real bookings before panicking.)
- Run one live checkout per brand on a phone, on cell data, and log: sticker price, final total, % markup, number of fields, taps to pay.
- Pull 10 Clarity mobile recordings per brand that opened the lightframe and didn't book.

### Week 2: kill the surprise fee (biggest, cheapest win)
Pick one, per brand:
- **Best: all-in pricing.** Fold taxes + fees into the ticket price in FH so $50 means $50 at checkout (HPB's $50 would become ~$58). Test it on HPB first.
- **Fallback:** keep the fee but say it right under every price: "$50/person + tax & fees, about $58 all-in."
- Drop the separate 1.5% card fee line if margin allows. It reads as nickel-and-diming at the worst moment.

### Week 2-3: shorten the FH checkout
- Move add-on products (cups, sunscreen, hats) to the post-booking confirmation/reminder flow, not the checkout.
- Make "how did you hear about us" optional or move it post-purchase.
- Collapse the cancellation policy into one line + "details" link.
- Confirm Apple Pay / Google Pay are on and show first in the FH flow (ask our FH rep if not).

### Week 3: trust + pay-later at the price
- Under each price: rating (4.9 from 981 Google reviews already shows inside FH, put it on our page next to the price too), one cancellation line ("Free reschedule up to 72 hrs out"), and "Book now, pay the rest on arrival" where deposits exist.
- Ask FH about Affirm/pay-later for private charters ($725+). That's where "or 4 payments of $181" changes the decision. Not worth it on $50 tickets.

### Ongoing: protect the winners
- Each brand's #1 seller (by FH revenue) gets the top homepage slot and the main ad budget. Seasonal/new tours go below it, never replace it.

### After the hosting move (Nov-Feb, see [[project_own_hosting_migration]])
- A/B test all-in vs + fees price display, and "pay on arrival" copy. Those become test #1 and #2 once we control the sites.

## Should we ask for an email before showing prices?

**No. Bad idea for us.** Reasons:
- Price is the first thing a tour shopper wants. Hide it and they bounce to Viator/GetYourGuide, which show our price openly (and we pay them commission).
- Google and AI answers (ChatGPT, Gemini, AI Overviews) can't read gated prices, so we'd drop out of "how much is a party barge in Houston" answers. That cuts against the AI visibility work.
- It's the opposite of what Tom does: he gives the full answer free, then asks.
- Our tickets are $50-$145, a quick decision. Gates work for big considered purchases (B2B software, $5k+ projects), not a Saturday kayak trip.

**Do this instead to get emails:**
- **Private charters / groups / weddings / corporate:** a "get a custom quote" form is a natural email capture. That's the one place gating makes sense.
- **Opt-in with a reason:** "Text me when Saturdays open" or "$10 off your first trip" pop-up after 30+ seconds or on exit, not before prices.
- **Abandoned checkout follow-up:** FH captures email at checkout. Check if FH can send an abandoned-booking email (or pull those emails like we did for E&E) and send one reminder within 24 hrs, with a hosted unsubscribe link.
