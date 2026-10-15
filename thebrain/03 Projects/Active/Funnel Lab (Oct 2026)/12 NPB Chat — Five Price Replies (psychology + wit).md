# NPB chat: five ways to answer "how much?"

*Drafted 2026-10-14 for card 1 on the Funnel Lab Board, after David's note: "more split testing options, use some psychology, try using some wit." DRAFT. Nothing changed in OpenCX.*

52% of NPB shopper chats open with "how much" and 64% end with no link and no contact (01 Customer Truth). Every version below answers the price in the first sentence. Hiding the price is the one thing we know loses. What changes is what comes right after.

Prices used are the live FareHarbor prices from 2026-10-13: seats $59 (Twerkin' Tiki 6pm $63), Bayou Boogie $800, Party Queen $900, Freaky/Twerkin' Tiki $1,200, pontoon $350. Party Queen capacity is still open (chat says 22, site says 26) so the per-head math uses 22 and is marked.

---

### A. Straight shooter (control)
**Lever:** low friction. Answer, link, done.
> Seats are $59 a person, whole boats $800 to $1,200. Here's what's open: [link]. How many are you bringing?

### B. The group math (my pick from round one)
**Lever:** reframing a big number into a per-head number, then a reason to give a phone.
> Seats are $59 a person. Bigger crews usually save by taking the whole boat: the Party Queen is $900, about $41 a head for 22. How many of you, and what's the occasion? Drop your cell and I'll text the link plus a summary you can paste straight into the group chat.

### C. The wisecrack
**Lever:** humor lowers guard and gets a reply. Price lands as a joke with the real number in it.
> $59 a seat. That's roughly two Hurricanes and one bad decision, except this one comes with gators and a captain. Whole boat for your crew runs $800 to $1,200. What are we celebrating?

### D. The decoy
**Lever:** a middle option looks like the smart buy when there's a pricier one next to it.
> Three ways to do it:
> 1) Seats on a shared boat: $59 each
> 2) Bayou Boogie, whole boat for up to 18 [VERIFY cap, chat quotes 18]: $800
> 3) Freaky Tiki, whole boat, the full show: $1,200
> Most birthday crews of 10 to 18 grab the Boogie. How many are you?

### E. Real scarcity + crowd proof
**Lever:** social proof and loss aversion, only with true numbers. The bot pulls live seats from `/avail`; if the number isn't live, this version can't run.
> Seats are $59. Heads up, Saturday's 2pm has [N] seats left right now. 3,656 people have reviewed us on Google, and the common thread is the captain. Want me to hold the link for Saturday or check another day?

*Never fake the seat count. If `/avail` can't answer, E falls back to A.*

---

## How to run five at our volume

About 100 shopper chats a month. A fixed five-way test would take most of a year, so run it as a **knockout**:

1. **Weeks 1 to 4:** rotate A, B, C, D, E by day of the week (Mon A, Tue B ... and shift one day each week so no version is stuck on slow days).
2. **End of week 4:** drop the two lowest on "chat ends with link clicked or contact captured."
3. **Weeks 5 to 8:** the top three.
4. **End of week 8:** run the top two head to head until one leads by 10+ points with 80+ chats each.

This finds a winner faster and doesn't spend months on the losers. It's less rigorous than a clean A/B, and that tradeoff fits a small chat volume.

## Voice check

C is the brand at its best (NPB reviews say "party but fun info", "I even think the alligators were rocking with us"). If C wins, the wit goes into the ads and the quiz too. If C loses, keep the jokes for Reels and keep the bot plain.

## Before it can run

1. Fix the wrong prices in Nolan's knowledge base (Oct 13 plan, item 09). Otherwise every version quotes the old numbers.
2. Confirm Party Queen capacity.
3. Version E needs the bot to call `/avail` (exists on the capture-v2 branch, not deployed).
