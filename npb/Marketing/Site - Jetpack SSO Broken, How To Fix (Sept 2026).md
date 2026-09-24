# Jetpack SSO on nolapartybarges.com is broken

Diagnosed 2026-09-22 while trying to edit SEO titles in wp-admin.

## Symptom

At `https://nolapartybarges.com/wp-login.php`, clicking **"Log in with WordPress.com"**
authenticates correctly (the consent screen shows the right user), then redirects to:

```
https://nolapartybarges-dummy.fareharbor.site/wp-login.php?action=jetpack-sso&result=success&...
```

That host returns **Cloudflare error 526, "Invalid SSL certificate."** The session never
reaches nolapartybarges.com, and returning to the live wp-admin just shows the login screen
again. SSO is a dead end every time.

## What is actually wrong

Three separate facts, each verified:

1. **The Jetpack connection is registered against the wrong hostname.** Note the `-dummy`
   in the redirect. Jetpack builds its post-authentication redirect from the site URL stored
   in the connection, so it is sending you to a staging host rather than the live domain.
2. **That staging host is dead.** Loading `https://nolapartybarges-dummy.fareharbor.site/`
   directly returns the same 526. Cloudflare resolves the name, so DNS still exists, but the
   origin behind it is not serving a valid certificate. This is not just a cosmetic wrong
   redirect, the destination genuinely does not work.
3. **You cannot fix it from your side.** Your WordPress.com account
   (mrfischer80@gmail.com) lists only your personal free site, `mrfischer80-cxizd`. The
   nolapartybarges.com Jetpack connection does not appear in your site list at all, which
   means the connection is owned by FareHarbor, not you. SSO recognised you as a *user on
   the site*, but that is not the same as owning the Jetpack connection.

The likely history: FareHarbor provisions Lightning sites on a
`<client>-dummy.fareharbor.site` hostname, connects Jetpack while the site is still on that
hostname, then points the real domain at it. The Jetpack connection's stored site URL never
got updated, and later the staging host's certificate lapsed.

## Who fixes it and what to ask for

This is a **FareHarbor support ticket**. You are asking them to repoint the Jetpack
connection for nolapartybarges.com.

Suggested wording:

> Jetpack SSO on nolapartybarges.com is broken. Logging in with WordPress.com redirects to
> nolapartybarges-dummy.fareharbor.site, which returns Cloudflare error 526 (invalid SSL
> certificate on the origin), so the login never completes. It looks like the Jetpack
> connection is still registered against the old `-dummy` staging hostname instead of the
> live domain. Can you re-register the Jetpack connection against
> https://nolapartybarges.com so SSO resolves to the live site?

Ask them to **preserve Jetpack settings** when they do it. A plain disconnect and
reconnect can reset Jetpack-stored options, and if the page SEO titles live in Jetpack SEO
Tools (likely, since there is no Yoast, Rank Math, AIOSEO or SEOPress on the site) a careless
reconnect could wipe or alter them. See `Site - Pedal in SEO Titles (Sept 2026).md`.

## Worth having them check while they are in there

If the connection points at a dead host, other Jetpack features that phone home may be
silently broken too. Ask them to confirm **Stats, Backup, Scan and Activity Log** are
actually reporting for this site, rather than assuming they are.

## In the meantime

The **username and password** option on the same login screen bypasses SSO entirely and
works. That is the route for the SEO title edits, and for any other wp-admin work, until
FareHarbor repoints the connection.

## Update 2026-09-24

Ilco (FareHarbor) switched Jetpack to WordPress.com 2FA and pointed Michael at
`https://nolapartybarges.com/edit` with username `mrfischer` (2FA to email). Michael signed in;
the login still ended on the Jetpack SSO callback, now at a different dead host:

```
https://maunakea.fareharborsites.com/nolapartybarges-dummy/wp-login.php?action=jetpack-sso&result=success&...
```

That page says "This site has been archived or suspended." Going back to
`nolapartybarges.com/wp-admin/` shows the login screen again, so no session was set on the live
domain. The Jetpack connection is still registered to the `nolapartybarges-dummy` site, just on a
new FareHarbor host. Still blocked; reply to Ilco drafted in chat 2026-09-24, not yet sent.
