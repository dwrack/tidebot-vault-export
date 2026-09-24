# "Pedal" in nolapartybarges.com SEO titles

Found 2026-09-22 while auditing the Meta campaign's landing page.

## The four titles to change

Paste-ready. Only the one word changes except on the Party Queen, noted below.

| Page | Current title | Change to |
|---|---|---|
| `/the-freaky-tiki/` | The Freaky Tiki \| New Orleans **Pedal** Barge | `The Freaky Tiki \| New Orleans Party Barge` |
| `/the-twerkin-tiki/` | The Twerkin' Tiki \| New Orleans **Pedal** Barge | `The Twerkin' Tiki \| New Orleans Party Barge` |
| `/bentley-bayou-cruiser/` | Bentley Pontoon Boat Rental New Orleans \| New Orleans **Pedal** Barge | `Bentley Pontoon Boat Rental New Orleans \| New Orleans Party Barge` |
| `/the-cajun-queen/` | The Party Queen \| **Pedal Bike** Party Booze Cruise | `The Party Queen \| New Orleans Party Booze Cruise` |

On the Party Queen, a straight pedal-to-party swap would read "Party Bike Party Booze
Cruise", which says party three times. The version above keeps the "Booze Cruise" keyword
and drops the awkward repeat.

The Bentley title runs 65 characters, so Google will truncate it around 60 either way.
Shortening it is a separate decision, not part of this fix.

## Where the field lives

The suffix is a **per-page override**, not the theme template. Evidence:

- 404 pages render "Page Not Found | New Orleans **Party** Barge", so the theme default is
  already correct.
- The homepage is clean: "New Orleans Swamp Tour Party Boat | Nola Party Barges".
- `og:site_name` on the Freaky Tiki page is correctly "New Orleans Party Barge" while
  `<title>` and `og:title` both say Pedal.

So four individual page fields are overriding a correct default.

Scanning the front end turned up **no Yoast, Rank Math, AIOSEO or SEOPress**. Only Jetpack
and the FareHarbor Lightning theme. The field is therefore most likely the **Jetpack SEO
Tools** title box or a **Lightning** page field in the editor sidebar. I could not confirm
which, because I could not get into wp-admin (below).

## Why I could not make the change

The Jetpack SSO login is broken. Clicking "Log in with WordPress.com" authenticates fine,
then redirects to:

```
https://nolapartybarges-dummy.fareharbor.site/wp-login.php?action=jetpack-sso&...
```

which returns **Cloudflare error 526, Invalid SSL certificate**. Note the hostname: the
Jetpack connection is registered against a **`-dummy`** staging host, not the live domain.
The redirect lands on a host with a bad certificate and the session never reaches
nolapartybarges.com. Going back to the live wp-admin just returns the login screen.

The other option on that screen is username and password, which I do not enter.

**Two ways forward:** log in yourself with username and password and paste the four titles
above, or fix the Jetpack connection so it points at the live domain instead of the dummy
host, which would also unblock this for next time.
