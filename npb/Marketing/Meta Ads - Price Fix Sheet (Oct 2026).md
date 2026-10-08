# Meta Ads price fix sheet - 2026-10-01

> **STATUS: COMPLETED AND PUBLISHED 2026-10-01.** All 10 fields below were
> changed and published. Each field was read first, retyped in full, and verified by
> reading it back before publishing. Kept as the record of what was changed and why.

Campaign `NPB | Purchase | Gator Collision | Sept 2026` (52578687844700), ad account act_87863118.

**Why:** site and FareHarbor were corrected to **$59 / $1,200** on 2026-09-30. All 8 ads in this
campaign still advertise **$63 / $1,250**.

**Scope, verified ad by ad on 2026-10-01:** 8 ads, **10 fields**. Every ad set words the price
differently, so there is no single find and replace that covers it. The v2 ads are duplicates of
their v1, so each pair below is identical and gets the same edit twice.

## FIRST: discard the bad draft

`NPB | Gator Collision v1 | 9x16 video` (52578763738900) has an **unpublished draft whose Primary
text is corrupted** (the closing price paragraph overwrote the opening hook line). Open that ad and
click **Discard draft** before doing anything else. Do not publish it. The live ad is fine.

## The edits

### 1. Gator Collision (ads: `...v1 | 9x16 video` and `...v2 | Fifteen Minutes`)

Primary text, last paragraph:

- FROM: `$63 a seat, or take the whole boat for your group at $1,250. Pick a date and we'll see you at the dock.`
- TO:   `$59 a seat, or take the whole boat for your group at $1,200. Pick a date and we'll see you at the dock.`

Description (**this is the only ad set whose description carries a price**):

- FROM: `$63 a seat. BYOB on the bayou. 4.9 stars, 3,800+ reviews.`
- TO:   `$59 a seat. BYOB on the bayou. 4.9 stars, 3,800+ reviews.`

### 2. Weather Kill (ads: `...| 9x16 video` and `...v2 | Fifteen Minutes`)

Primary text, last paragraph:

- FROM: `$63 a seat, or $1,250 for the whole boat. Book the date and let the weather do what it does.`
- TO:   `$59 a seat, or $1,200 for the whole boat. Book the date and let the weather do what it does.`

Description is `Covered, heated, BYOB. 4.9 stars, 3,800+ reviews.` No price, leave it.

### 3. Planner's Win (ads: `...| 9x16 video` and `...v2 | Fifteen Minutes`)

Primary text, last paragraph:

- FROM: `Whole boat for your group, $1,250 for up to 25. Or $63 a seat if it's a smaller crew.`
- TO:   `Whole boat for your group, $1,200 for up to 25. Or $59 a seat if it's a smaller crew.`

Description is `Private BYOB boat on the bayou. 4.9 stars.` No price, leave it.

> Also worth a separate check: this is the only ad that makes a **capacity** claim, "up to 25".
> Nobody has verified that against the current FareHarbor listing. Not changed here.

### 4. Anti-Bourbon (ads: `...| 9x16 video` and `...v2 | Fifteen Minutes`)

Primary text, last paragraph:

- FROM: `4.9 stars, 3,800+ reviews. $63 a seat, $1,250 for the whole boat.`
- TO:   `4.9 stars, 3,800+ reviews. $59 a seat, $1,200 for the whole boat.`

Description is `Private BYOB boat, 15 min from the Quarter.` No price, leave it.

## Do not script the Primary text field

Ads Manager's Primary text is a Lexical contenteditable. On 2026-10-01
`document.execCommand('insertText', ...)` over a correct one-word selection **duplicated the
containing paragraph to the top of the field**, wiping the opening line. Reproduced twice.
Descriptions are plain textareas and are safe to script.

If editing by hand, click directly into the Primary text box and confirm the caret is inside it
before pressing Cmd+A, because otherwise Cmd+A selects the whole page and the typing goes nowhere.
Safest is to click just before the `$` and edit the digits directly, rather than replacing the
whole field.

## After editing

Editing copy restarts the learning phase and resets the 9-day v1 copy comparison. That tradeoff was
accepted on 2026-10-01 in order to stop advertising a price nobody charges.

When publishing, open **Review and publish** and **deselect "New Orleans Kayak Swamp - Video views"**
(Updated: Ad status). It is a different brand's stale draft, it carries an error, and it has been
deliberately left alone.
