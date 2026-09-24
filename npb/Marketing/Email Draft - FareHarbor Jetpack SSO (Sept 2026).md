# FareHarbor support ticket: Jetpack SSO

**STATUS: SUBMITTED 2026-09-22.** FareHarbor's form returned "Your ticket was
successfully submitted! We will get in touch with you shortly." Submitted through
`pages.fareharbor.com/submit/`, not by email.

Values submitted:

| Field | Value |
|---|---|
| What can we help you with | FareHarbor Hosted Website |
| Your name | Michael Fischer |
| Your email address | doorcountyzip@gmail.com |
| Your company name | New Orleans Party Barge |
| Website URL | https://nolapartybarges.com |
| Type of request | Technical update (DNS, Email troubleshooting, Script installation) |
| Describe your request | the body below |

Watch **doorcountyzip@gmail.com** for their reply, since that is the address on the ticket.

**What to check when they respond:** that SSO actually resolves to nolapartybarges.com
rather than the `-dummy` host, and that the per-page SEO titles survived. If they did a
disconnect and reconnect, the four boat-page titles may have been reset. See
`Site - Pedal in SEO Titles (Sept 2026).md`.

---

## Email version (if you would rather send it directly)

**To:** support@fareharbor.com
**From:** doorcountyzip@gmail.com
**Subject:** Jetpack SSO broken on nolapartybarges.com (redirects to a dead -dummy host)

---

Hi FareHarbor Support,

I can't log into wp-admin on our hosted site, nolapartybarges.com (New Orleans Party Barge).

**The problem**

On https://nolapartybarges.com/wp-login.php, clicking "Log in with WordPress.com"
authenticates correctly, then redirects to:

https://nolapartybarges-dummy.fareharbor.site/wp-login.php?action=jetpack-sso&result=success&...

That URL returns Cloudflare error 526, "Invalid SSL certificate." The login never
completes, and going back to https://nolapartybarges.com/wp-admin/ just returns the login
screen again.

**What I've already checked**

Loading https://nolapartybarges-dummy.fareharbor.site/ directly returns the same 526 error,
so the host itself is not serving a valid certificate. Cloudflare resolves the name, so the
DNS record still exists.

Note the "-dummy" in that hostname. It looks like the Jetpack connection is still
registered against the original staging hostname rather than the live domain, so Jetpack is
building its post-login redirect to a host that no longer works.

Logging in with username and password on the same screen works normally, so this is
specific to the WordPress.com SSO path.

**What I'm asking for**

Could you re-register the Jetpack connection for nolapartybarges.com against the live
domain, https://nolapartybarges.com, so SSO resolves to the real site?

One request: please preserve the existing Jetpack settings when you do it. We don't have
Yoast, Rank Math or a similar SEO plugin installed, so some of our per-page SEO titles may
be stored in Jetpack SEO Tools. I'd rather not lose those in a disconnect and reconnect.

**One more thing worth checking**

If the connection has been pointing at a dead host, other Jetpack features may be affected
too. Could you confirm that Stats, Backup, Scan and Activity Log are actually reporting for
this site?

Thanks,

Michael Fischer
New Orleans Party Barge
doorcountyzip@gmail.com

---

## Notes

- Support email **support@fareharbor.com** verified on
  `pages.fareharbor.com/submit` on 2026-09-22. Phone there is (855) 495-5551.
- They also take tickets through that form, and it has a **"FareHarbor Hosted Website"**
  category that fits this issue exactly. The form may route faster than plain email.
