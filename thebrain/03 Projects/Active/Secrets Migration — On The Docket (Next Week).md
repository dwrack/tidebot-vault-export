# Secrets Migration — On The Docket (week of 2026-06-22)

*Created 2026-06-19. David said: get this on the docket for next week. Plan/prep only until then — no execution today.*

## The problem
~24 of the iCloud-synced vault `.mcp.json` files carry secrets in **plaintext**:
- A shared `GOOGLE_CLIENT_SECRET` (the same value reused across every vault).
- Per-workspace `OPENCX_API_KEY` JWTs.

Because these vaults sync through iCloud/Obsidian, those secrets sit in plaintext on every synced device. This violates the standing rule (secrets never in synced vault files; local/user scope only).

## The fix (David chose: migrate to local/user scope)
1. **Move MCP secrets out of synced `.mcp.json` files.** Either:
   - register the affected MCP servers at **user scope** (`claude mcp add --scope user`, which writes to local-only `~/.claude.json`), or
   - replace the literal values in vault `.mcp.json` with `${ENV_VAR}` references and keep the real values in a local-only profile (`~/.zshrc` / `~/.config`).
2. **Strip the literal secret values** from every synced `.mcp.json` once the server resolves from local/user scope.
3. **Do it with the hidden-prompt `.command` pattern** (per global CLAUDE.md): a Desktop `.command` script that `read -s` prompts for the secret and runs the registration — no secret on screen, in the transcript, or in shell history. The script itself holds no secret, so it's safe to trash after.

## Note / recommendation
- David chose migrate, not rotate. Flagging once more: the shared `GOOGLE_CLIENT_SECRET` has been syncing in plaintext across many devices for months, so **rotating it** is the stronger move. Migration relocates the risk; rotation retires it. Decide at execution time.

## Checklist (run next week)
- [ ] Enumerate every vault `.mcp.json` containing a secret (grep for `GOOGLE_CLIENT_SECRET`, `OPENCX_API_KEY`).
- [ ] Decide user-scope vs. `${ENV}`-ref approach per server type.
- [ ] Build the one-click `.command` migration script (Claude can do this when David's ready).
- [ ] Migrate, then verify: `claude mcp list` still resolves the servers; grep across synced `.mcp.json` shows **no** literal secret values.
- [ ] (Decide) rotate the shared Google secret.

## Related security hygiene (surfaced from the archived April plan)
- [ ] Delete the LastPass CSV from Desktop.
- [ ] Rotate weak passwords: NKST `Cool6006!`, GT PayPal `Cheesy97`.
