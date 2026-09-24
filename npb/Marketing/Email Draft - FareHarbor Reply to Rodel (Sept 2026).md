# Reply to Rodel, FareHarbor ticket 5805496

**Status: wp-admin is completely unreachable.** Username and password, WordPress.com SSO,
and an explicit live-domain `redirect_to` all end at the dead staging host. Nothing can be
edited in WordPress until FareHarbor fixes this.

**Diagnosis corrected 2026-09-23.** The earlier read, that this was only the Jetpack SSO
connection, was too narrow. New evidence: logging in with **username and password** at the
live URL also redirects to the dummy host. Since the front-end HTML and the login page
contain zero references to the dummy hostname, and the login form posts to the live domain,
the redirect is coming from WordPress's own **WordPress Address (siteurl)** option, which
appears to be set to the staging host while the Site Address (home) stays live. That single
misconfiguration explains every symptom: the front end works, but every successful login of
any kind lands on a dead host.

This is stronger evidence than the SSO version, and it directly answers Rodel's "just use
the live URL" reply, because the live URL is exactly what was used.

---

**Reply text**

Hi Rodel,

Thanks for checking, but I think the diagnosis is off, and I have a clearer test now.

I am not navigating to the staging URL. I never type it. Here is what happens:

1. I go to **https://nolapartybarges.com/wp-login.php**, the live URL
2. I log in with **username and password**, not the WordPress.com button
3. The login succeeds
4. WordPress then redirects me, on its own, to
   **https://nolapartybarges-dummy.fareharbor.site/wp-admin/**
5. That page fails with `ERR_SSL_PROTOCOL_ERROR` and I never reach the dashboard

So this is not about which URL I start from. I start on the live one. Something on the
server is sending every successful login to the staging host.

What points at the cause:

- The front-end HTML on nolapartybarges.com contains **no references** to
  nolapartybarges-dummy.fareharbor.site. The public site is entirely on the live domain.
- The login form itself posts to https://nolapartybarges.com/wp-login.php, also live.
- Only the **post-login destination** is on the staging host.
- I also tried forcing it. I loaded
  `https://nolapartybarges.com/wp-login.php?redirect_to=https%3A%2F%2Fnolapartybarges.com%2Fwp-admin%2Fedit.php%3Fpost_type%3Dpage`
  so the login form carried an explicit destination on the live domain. WordPress
  **ignored it** and still sent me to the staging host.

That last point is the clearest signal. WordPress only honours `redirect_to` when the
target host is on its allowed list, which is built from siteurl. If siteurl is the staging
host, then a redirect to nolapartybarges.com looks *external* to WordPress, gets rejected,
and it falls back to the default admin URL, which is the staging host again. That is exactly
the behaviour I am seeing.

That pattern fits the **WordPress Address (siteurl)** option being set to
https://nolapartybarges-dummy.fareharbor.site while the Site Address (home) is correctly
https://nolapartybarges.com. WordPress builds the admin URL from siteurl, so every
successful login goes to the staging host regardless of how I log in. It would also explain
why the WordPress.com SSO button fails the same way.

Separately, https://nolapartybarges-dummy.fareharbor.site/ returns Cloudflare error 526 on
its own, so that host is not serving a valid certificate at all.

Could you check the siteurl value for this site and point it at https://nolapartybarges.com?
If the Jetpack connection is also registered against the staging hostname, that likely needs
re-registering against the live domain too.

One request: please preserve existing Jetpack settings if you reconnect anything. We do not
have Yoast, Rank Math or a similar SEO plugin, so some per-page SEO titles may live in
Jetpack SEO Tools and I would rather not lose them.

When you say you were able to log in successfully, could you tell me what URL you landed on
after logging in? If you reached the dashboard, you may be hitting it through an internal
route that bypasses this.

Thanks,
Michael Fischer
New Orleans Party Barge

---

## Heads up: there may be two tickets

This thread is request **5805496**. A separate ticket went in through
`pages.fareharbor.com/submit/` on 2026-09-22 under doorcountyzip@gmail.com covering the same
issue. Reference the other number so they merge them.
