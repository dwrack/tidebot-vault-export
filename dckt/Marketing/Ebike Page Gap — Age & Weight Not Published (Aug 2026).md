# E-Bike Page Gap — Age & Weight Limits Aren't Published

**Filed Aug 11 2026 from the dump. Source: contact form screenshot, Jul 22 2026.**

---

## What happened

Michael Parham (parhmic@yahoo.com) submitted the Door County Kayak contact form on Jul 22 at 9:16 PM with exactly two questions:

1. What is the minimum age for someone to go on the ebike tour?
2. Is there a weight limit for the ebike tour?

**Both answers already exist** in `Door County Kayak Tours — FAQ Database.md`, where this question is logged at **725 emails, high priority**:

> **E-Bikes:** Maximum rider weight is 285 lbs (rider + cargo). Minimum age to ride is 12, as long as the rider physically fits the bike. Guide confirms fit at check-in. Parent/guardian signs the waiver for anyone under 18.

**Correction, Aug 11:** the FAQ Database previously said 16. David corrected it to **12, if they fit the bike**. The database is now updated. Fit is the gate, not age. Anything published before this date that says 16 is wrong and needs pulling.

725 emails asking a question the page doesn't answer is not a customer service volume problem. It's a page that's been generating support load for years.

## The actual problem

I fetched `doorcountykayaktours.com/e-bike-tours/` on Aug 11. **Neither answer appears anywhere on the page.** No weight figure, no age minimum, no link to a policies page that has them.

So this isn't a customer service miss. It's a page failure. Michael was the one person motivated enough to email. Everyone else who wondered about the weight limit and didn't feel like asking a stranger just closed the tab. That's the invisible version of this problem, and it's the larger one.

This is the first confirmed case for the complaints-as-research play in `TheBrain/06 Learning/Complaints as Research — Mining OpenCX Tickets for Page Fixes (Aug 2026).md`.

---

## 🔴 Blocker — the waivers say 16, not 12

Swept the vault after David's correction. The age-16 rule isn't only in the FAQ. It's in three more places, two of which are legal instruments:

| Where | What it says |
|---|---|
| `Waiver — Guided E-Bike Tour (Wisconsin, Draft for Attorney Review).md` §191 | Minimum age to operate independently: **16**. Riders 16-17 need guardian signature. |
| `Waiver — Self-Checkout E-Bike Rental (Wisconsin, Draft for Attorney Review).md` §227, §263 | Same. Plus a note: Wisconsin sets no state minimum for Class 2, but the operator may set its own, **and "confirm with the carrier whether the policy ties to a specific minimum age."** |
| `Guide Certification Quiz (May 2026).md` §119, §264 | Quiz answer key teaches guides that 16 is the minimum. |

**I did not change the waivers.** They're pending attorney review and they're the document that actually governs what happens after an incident. Changing a legal instrument off a one-line message is the wrong call.

**Publishing 12 on the site while the waiver says 16 is worse than either number alone.** It hands a plaintiff a contradiction between our marketing and our own signed agreement, and it puts guides in the position of turning away a 13-year-old whose parent booked based on the website.

The real question is whether **16 was the insurance carrier's number or ours.** The waiver draft flags that as unconfirmed. If the carrier set it, 12 isn't ours to give.

**Carrier identity resolved, Dump pass 41 (2026-08-15).** "World Insurance" in earlier passes was a placeholder guess, not a real name. The actual policy sits in the vault: carrier is **Western National Insurance Group**, producer is **Leavitt Select Insurance Services, Inc.** (serviceboise@leavitt.com, (435) 752-1351), certificate #26-27 dated 05/29/2026. DCKT's own training docs (Guide Cert Quiz, Manager Cert Quiz) name **Kurt Rupnow** as the broker to call, but no direct contact info for him individually exists anywhere in the vault.

**Fleet class — RESOLVED, Dump pass 40 (2026-08-15).** One of the two sequence steps below is done. The self-checkout waiver draft self-declares the fleet: `Waiver — Self-Checkout E-Bike Rental (Wisconsin, Draft for Attorney Review).md` line 23, "The e-bike is a Class 2 fat-tire pedal-assist electric bicycle with a top assisted speed of approximately 20 mph," and line 263 confirms "Wisconsin does not impose a state-level minimum age for Class 2 e-bikes on public roads." Only Class 3 carries the state's 16-year floor. The fleet is Class 2, so the state-law side of the age question clears for 12. (Searched the vault for the actual bike brand/model/invoice to double-check the waiver's self-description — none exists anywhere, no RadPower/Aventon/QuietKat/Pedego/Trek hit, no purchase record. The waiver's own Class 2 declaration is the only source, but it's the same document David's team would rely on in an actual incident, so it's a legitimate basis to act on.)

Sequence before anything goes live:
1. ~~Confirm the fleet's e-bike class (Wisconsin does set 16 for Class 3)~~ **Done — Class 2, no state minimum.**
2. **Ask the carrier whether the policy specifies a minimum operator age.** This is now the only open blocker. **Identity confirmed and a draft email staged, Dump pass 41 (2026-08-15):** `Operations/Insurance/2026-08-15 — DRAFT Email to Broker — E-Bike Minimum Age Confirmation (STAGED, pending David approval).md` (symlinked to Desktop). Nobody has sent it. David needs to review, decide who to address it to (agency general line vs. Kurt Rupnow directly if he has that contact), sign it or hand it to Isabella/Bella, and send. Nothing else moves until a reply comes back.
3. If the carrier clears it, update the two waivers and the guide quiz **before** the page
4. Then publish

If 12 clears, it's a genuinely better answer for family bookings and worth the paperwork. Just not in that order.

---

## Actions

- [ ] **David: review and send the staged broker email** (`Operations/Insurance/2026-08-15 — DRAFT Email to Broker — E-Bike Minimum Age Confirmation (STAGED, pending David approval).md`, symlinked to Desktop). Confirms whether the policy ties to a minimum operator age. Blocks everything below — the only remaining blocker as of pass 41.
- [x] ~~Confirm the e-bike fleet class~~ **Class 2, confirmed in the vault's own waiver draft (pass 40, Aug 15 2026). No Wisconsin state minimum applies.**
- [ ] Once cleared: update both e-bike waivers + the Guide Certification Quiz answer key to match
- [ ] **Confirm Michael got a reply.** Jul 22 to now is 20 days. Check info@doorcountykayaktours.com. If nobody answered, that booking is gone and it's worth knowing.
- [ ] **Add the block below to the e-bike tour page** above the booking button, not in a footer policies link
- [ ] **Add the FAQ schema** to the page's Schema Markup field
- [ ] **Add both answers to the OpenCX knowledge base** so the bot handles this without a human
- [ ] **Sweep the other product pages for the same gap.** Kayak weight limits (275 single / 450 tandem) and the age-5 minimum are almost certainly missing too. Same fix, same afternoon.

---

## Copy-paste: page block

Put this directly under the tour description, above the Book Now button.

> **Good to know before you book**
>
> **Minimum age:** 12, as long as the rider fits the bike. We check fit at check-in, and if a kid can reach the pedals and handlebars comfortably they're good to go. A parent or guardian signs the waiver for anyone under 18 and rides along with anyone under 16. Smaller kids can still come, either in a trailer or on a tag-along hooked to an adult's bike.
>
> **Weight limit:** 285 lbs per rider, including anything you're carrying.
>
> Not sure your kid will fit, or close to the weight limit? Message us before you book and we'll tell you straight.

Two things that line does. It converts a disqualifying constraint into a reason to contact us instead of a reason to close the tab, and "12 if they fit" is a materially better answer for family bookings than "16." That's a whole segment the old number was turning away.

**Flag before publishing:** confirm which e-bike class the fleet is. Wisconsin sets a 16-year minimum for **Class 3** e-bikes (throttle/pedal-assist to 28 mph); Class 1 and 2 have no state age minimum. If any bike in the fleet is Class 3, 12 doesn't hold for that bike and the page has to say so. Worth ten minutes with the spec sheet before this goes live, since it's the kind of thing that only ever comes up after an incident.

---

## Copy-paste: FAQ schema

Paste raw into the **Schema Markup** ACF field. No script wrapper. No escaped inner double quotes.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the minimum age for the Door County e-bike tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Riders can be as young as 12, as long as they physically fit the bike. Our guide confirms fit at check-in. A parent or legal guardian must sign the waiver for any rider under 18 and must ride along with anyone under 16. Kids too small to fit a bike can still join in a properly fitted trailer or on a tag-along attached to an adult's bike."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a weight limit for the e-bike tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Maximum rider weight is 285 pounds, including any cargo you carry. If you are close to that limit, contact us before booking and we will let you know whether the tour will work for you."
      }
    },
    {
      "@type": "Question",
      "name": "Can kids ride on the Door County e-bike tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Kids 12 and up can ride their own e-bike as long as they fit it, which the guide checks at check-in. A parent or guardian rides along with anyone under 16 and signs the waiver for anyone under 18. Younger or smaller kids can ride in a properly fitted trailer or on a tag-along attached to an adult's bike."
      }
    }
  ]
}
```

After saving, fetch the live page and run the embedded JSON-LD through a parser before calling it done. The CMS accepts invalid output silently.

---

## Draft reply to Michael (if he was never answered)

Send from info@doorcountykayaktours.com, signed by Bella. Not David.

> Hey Mike,
>
> Sorry for the slow reply on this, that one got away from us.
>
> Two answers for you:
>
> Kids can ride as young as 12, as long as they fit the bike. We check that at check-in and it's usually pretty obvious. A parent signs the waiver for anyone under 18 and rides along with anyone under 16. If you've got a smaller one, they can still come in a trailer or on a tag-along hooked to your bike.
>
> Weight limit is 285 lbs per rider, including whatever you're carrying.
>
> If you're still thinking about a ride this season, let me know roughly when and I'll tell you what's open.
>
> Thanks,
> Bella
> Door County Kayak Tours

---

## Related
- [[532 Content Grid — 30 Videos (Aug 2026)]] rows 27 and 28 cover the same questions on video. Fix the page first, then post.
