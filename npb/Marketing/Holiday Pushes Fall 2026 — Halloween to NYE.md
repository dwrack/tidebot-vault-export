---
type: plan
business: NOLA Party Barge
date: 2026-09-10
owners: David (approve), JT (FareHarbor + marina), Jeff (social + Nolan)
horizon: Sept 10 to Dec 31 2026
related: "[[2027 Sponsorship + Events Plan (Sept 2026)]]"
---

# Holiday Pushes, Fall 2026

Five pushes, stacked by date. Each one goes live about 5 weeks before its date, which matches the last-minute booking curve (33% book 30+ days out, the rest inside the month).

| Push | Date | Goes live | Email | Format |
|---|---|---|---|---|
| Halloween pirate weekend | Fri Oct 30, Sat Oct 31 | Now | h01, this week | Private charters both nights + one ticketed public boat Sat |
| Friendsgiving | Nov 20 to 22 | Oct 13 | h02, Tue Oct 27 | Private charters, potluck at the fire pits |
| Thanksgiving week + Bayou Classic | Nov 25 to 29 | Oct 20 | h02 (same email) | Family + alumni charters |
| New Year's Eve | Thu Dec 31 | Nov 10 | h03, Tue Nov 17 | Private charters into midnight, premium price |
| Office holiday parties | Nov 20 to Dec 23 | Now (corporate track) | h03 + Gmail 1:1s | See the flyer and the 2027 plan, Track B |

Email sender: the SendGrid win-back pipe (`.ses_campaign/winback_sender_sendgrid.py --week h01`). Keys h01 to h03 are in `winback_series.py`. The SES pipe has been failing since Aug 25 (boto3 missing for /usr/bin/python3), so don't use it until that's fixed.

---

## 1. Halloween pirate weekend (Oct 30 to 31)

Halloween is a Saturday. This is the first real use of the pirate concept, so it doubles as a test of whether "bass pirates" lands with real customers.

**Offer**
- Private charters Fri and Sat, all slots. Costumes encouraged, no surcharge. Boats dressed: sun-bleached flags, lanterns, skull-and-crossbones on the tiki roof.
- One ticketed public boat: "Bass Pirates Halloween" Sat Oct 31, 8pm to 10pm. 40 seats. $55 a seat (BYOB, fire pits after). Best costume wins a free charter.
- Fire pits lit both nights for the return.

**FareHarbor (JT)**
- New item: "Bass Pirates Halloween, Sat Oct 31, 8pm" public, 40 pax, $55. Description below. Photo: any night boat shot until we have pirate footage.
- Tag Oct 30 and 31 private slots with a "Halloween weekend" note in the item description so the calendar reads as an event, not a normal night.

**Copy**
- IG/FB post: "Halloween's on a Saturday. We're turning the bayou into pirate water Oct 30 and 31. Private boat for your crew, or grab a seat on the Bass Pirates boat Saturday at 8. Costumes required, obviously. Link in bio."
- FareHarbor description: "Halloween on a Saturday, on the water. Two hours on Bayou Bienvenue in the dark with a boat full of pirates, wenches, and whatever you came as. BYOB. Fire pits on the sand when we get back. Best costume wins a free private charter for 18."
- Nolan FAQ line: "Halloween weekend (Oct 30 and 31) we run private boats both nights plus a ticketed pirate boat Saturday at 8pm, $55 a seat. Costumes welcome on every boat."

**Meta (David)**
- Retargeting campaign already outperforms everything. Add one Halloween creative to it at the same $20/day. No new campaign.
- Creative: 9:16 video, night boat + costumes, hook text "Halloween is a Saturday this year." CTA to the FareHarbor item.

**Content (Jeff)**
- One reel this week: crew tries on pirate gear at the marina, "we're doing something for Halloween." No polish.
- Shoot a proper pirate night reel on Oct 30 for next year's push.

---

## 2. Friendsgiving (Nov 20 to 22)

**Offer.** Private boat, 2 hours, everybody brings a dish, potluck at the fire pits after. Boat-only rate, no add-ons. Locals, 20s and 30s, the birthday-organizer crowd that already books us.

**Copy.** "Friendsgiving on the water. Nov 20 to 22. Bring the food, we've got the boat and the fire pits. Somebody's apartment can't compete."

**FareHarbor.** No new item. Add "Friendsgiving weekend" note to the Nov 20 to 22 slots.

**Nolan.** "Friendsgiving weekend is Nov 20 to 22. Book any private boat, bring food, and use the fire pits at the marina after. No extra charge for the fire pits."

---

## 3. Thanksgiving week + Bayou Classic (Nov 25 to 29)

**Offer.** Family charters Wed through Sun. Bayou Classic (Southern vs Grambling, Sat Nov 28) brings a huge alumni crowd. Charter for alumni chapters, fraternity and sorority groups, families.

**Copy.** "Family's in town, nobody wants to cook again. Two hours on the bayou gets everybody out of the house." And a separate Bayou Classic post: "Bayou Classic weekend. Alumni boat, your chapter, your music, the bayou. Sat Nov 28."

**Outreach.** Southern and Grambling alumni chapters in NOLA and Baton Rouge get a Gmail 1:1 from Jeff in mid-October. Two emails, that's it.

**Nolan.** "Thanksgiving week we run every day except Thanksgiving Day. Bayou Classic Saturday is one of our busiest days, book early."

---

## 4. New Year's Eve (Thu Dec 31)

**Offer.** Private boats into midnight. 10pm to 12:15am slot, premium rate (suggest 1.5x boat rate). Fireworks over the skyline visible from the water. Champagne toast at midnight from the crew. Fire pits after.

**FareHarbor.** New item: "New Year's Eve Midnight Cruise" private, 10pm to 12:15am, premium rate. Also an early slot 7 to 9pm at normal rate for families.

**Copy.** "Midnight on the bayou. Private boat, your people, fireworks over the skyline at 12. Not a $200 ticket to stand in a hotel ballroom."

**Nolan.** "New Year's Eve we run a 7 to 9pm cruise at the normal rate and a 10pm to midnight cruise with a champagne toast at a premium rate. Both private."

---

## 5. Office holiday parties (Nov 20 to Dec 23)

Covered in `2027 Sponsorship + Events Plan (Sept 2026)`, Track B. Flyer at `Holiday Party Flyer 2026 — Mele Kalikimaka on the Bayou.html`. Corporate contact list at `Corporate Holiday — Past-Guest Company Domains (Sept 2026).csv`. 13 Gmail drafts staged in info@ on 2026-09-10 for David to review and send.

---

## Open items

- [ ] David: confirm heated boats, indoor room capacity, deposit terms before the flyer or any corporate email goes out.
- [ ] David: approve h01 (test sent to dwrack81 on 9/10), then full send.
- [ ] JT: build the Halloween ticketed item in FareHarbor.
- [ ] JT: NYE items in FareHarbor by Nov 1.
- [ ] Jeff: pirate gear reel this week.
- [ ] Jeff: send the 13 corporate Gmail drafts after David's ok.
- [ ] Fix SES sender (boto3) or retire it and rely on SendGrid.
