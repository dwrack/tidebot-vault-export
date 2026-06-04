# Do Not Contact List — Email + SMS

*Master suppression list. Scrub against this before EVERY email blast and every Twilio SMS blast. Email and SMS are treated as one opt-out: if someone opts out of one, they come off both.*

Last updated: 2026-06-04

---

## How this is enforced

- **Email (SendGrid):** all addresses below are in SendGrid's **global unsubscribe group**, so SendGrid will refuse to send to them no matter which list is uploaded. This is the hard backstop.
- **Master Contacts sheet:** the 2026-06-03 unsubscribers are flagged `Unsubscribed 2026-06-03` in the new **Status** column (F) of the "Sauna Boat Opt in Form (Responses)" → Master Contacts tab. Filter out any non-blank Status before sending.
- **SMS (Twilio):** no automated suppression exists yet. Before any SMS blast, manually drop anyone whose name/email/phone matches an entry below. None of the current opt-outs have a phone number on file, so there is no overlap with the SMS-capable list today, but that can change as the form collects more responses.

---

## June 2026 blast opt-outs (23) — replied "unsubscribe" to "Get a Free Friend Pass!"

These came in as email replies because the blast had no unsubscribe link (reply-to-unsubscribe only). All added to SendGrid global suppression 2026-06-04.

| Name | Email | Phone on file? |
|------|-------|----------------|
| Guillaume Chevallerau | g.chevallerau@gmail.com | no |
| Taylor Hemwall | taylorhemwall@gmail.com | no |
| Rebecca Dudeiros | rebadm@yahoo.com | no |
| Daniel Childs | daniel.louis.childs@gmail.com | no |
| Allie Smith | allieksmith@gmail.com | no |
| Terry Ku | terryku@utexas.edu | no |
| Serhan Ceran | serhanceran@pm.me | no |
| Marty Ripp | martyripp@gmail.com | no |
| Khang Dang | khdang25@gmail.com | no |
| Evan Carmi | evan.carmi@gmail.com | no |
| Bryce Basiliere | brycebasiliere@gmail.com | no |
| Tim Schuckers | tschuckers@gmail.com | no |
| Paul Bascom | paulbascom59@gmail.com | no |
| Sophia Nguyen | nguy0004@pacificu.edu | no |
| Rex Larsen | callmerex@gmail.com | no |
| Rita Sabler | ritasabler@gmail.com | no |
| Cullen Roberts | cullen.f.roberts@gmail.com | no |
| Adrienne Bridge | adrienne.bridge@gmail.com | no |
| Greg Bigelow | gregbglw@gmail.com | no |
| Mary Kate Tolan | mktolan@arizona.edu | no (not on master list) |
| Dale Connors | dcconnors5@gmail.com | no |
| Ben Koerbel | bkoerbel@gmail.com | no |
| Evelyn McLean (replied as "Normal Person") | goodnewsreporting@gmail.com | no |

## April 2026 blast opt-outs (7) — from "Did you win and a thank you"

| Name | Email |
|------|-------|
| Milan Griffes | milan.griffes@gmail.com |
| David Survilo | davidsurvilo@gmail.com |
| Karla Arria-Devoe | karriadevoe@gmail.com |
| Henry Gotjen | hgotjen@gmail.com |
| Margot Bigg | info@margotbigg.com |
| Kinsey Eriksen | kinseyeriksen@yahoo.com |
| Chad McDonald | chadm@probuilderswa.com |

---

## Lesson learned

The June blast went out with no footer unsubscribe link, just reply-to-unsubscribe. That works but it's manual, it clutters the inbox, and CAN-SPAM technically wants a clear opt-out mechanism. **Every future blast needs a real `{{unsubscribe}}` link in the footer** wired to SendGrid's subscription tracking so opt-outs are automatic and we stop having to mine the inbox by hand.
