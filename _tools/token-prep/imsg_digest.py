#!/usr/bin/env python3
"""Compact one-page digest of iMessage threads from the local Messages database.

Replaces the 14-16k-character dumps the imessage MCP server returns per conversation
with a ~2k-character page: no tapbacks/reactions, no attachment blobs, one line per
message, long messages trimmed, oldest first.

Usage:
  python3 imsg_digest.py --contact "Catherine" --days 45 [--out lease.md] [--limit 80]
  python3 imsg_digest.py --search "lease" --days 60
Requires: python3 + sqlite3 (both ship with macOS). The Terminal app (or whatever runs
this) needs Full Disk Access in System Settings > Privacy & Security to read chat.db.
Nothing is sent anywhere; it only reads ~/Library/Messages/chat.db.
"""
import argparse, os, sqlite3, datetime, re, sys, shutil, tempfile

DB = os.path.expanduser('~/Library/Messages/chat.db')
APPLE_EPOCH = datetime.datetime(2001, 1, 1)

def to_dt(v):
    if v is None: return None
    v = v / 1e9 if v > 1e12 else v  # nanoseconds since 2001 on newer macOS
    return APPLE_EPOCH + datetime.timedelta(seconds=v)

def attributed_text(blob):
    """Best-effort text from attributedBody (used when message.text is NULL on Ventura+)."""
    if not blob: return ''
    i = blob.find(b'NSString')
    if i < 0: return ''
    j = blob.find(b'+', i)
    if j < 0: return ''
    k = j + 1
    ln = blob[k]
    if ln == 0x81: ln = int.from_bytes(blob[k+1:k+3], 'little'); k += 3
    else: k += 1
    return blob[k:k+ln].decode('utf-8', 'replace')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contact', help='substring of handle (phone/email) or chat display name')
    ap.add_argument('--search', help='substring in message text')
    ap.add_argument('--days', type=int, default=30)
    ap.add_argument('--limit', type=int, default=80)
    ap.add_argument('--width', type=int, default=160, help='max chars per message line')
    ap.add_argument('--out'); ap.add_argument('--db', default=DB)
    a = ap.parse_args()
    if not (a.contact or a.search): ap.error('give --contact and/or --search')
    if not os.path.exists(a.db): sys.exit(f'no database at {a.db}')
    # copy so a locked live DB still reads cleanly
    tmp = os.path.join(tempfile.mkdtemp(), 'chat.db'); shutil.copy(a.db, tmp)
    for ext in ('-wal', '-shm'):
        if os.path.exists(a.db + ext): shutil.copy(a.db + ext, tmp + ext)
    con = sqlite3.connect(tmp)
    since = (datetime.datetime.now() - datetime.timedelta(days=a.days) - APPLE_EPOCH).total_seconds() * 1e9
    q = '''SELECT m.date, m.is_from_me, h.id, c.display_name, m.text, m.attributedBody, m.associated_message_type, m.cache_has_attachments
           FROM message m
           LEFT JOIN handle h ON h.ROWID = m.handle_id
           LEFT JOIN chat_message_join cmj ON cmj.message_id = m.ROWID
           LEFT JOIN chat c ON c.ROWID = cmj.chat_id
           WHERE m.date > ? ORDER BY m.date ASC'''
    rows = con.execute(q, (since,)).fetchall()
    out, seen = [], set()
    for date, me, handle, chat, text, body, assoc, has_att in rows:
        if assoc and assoc != 0: continue  # tapbacks / reactions
        text = (text or attributed_text(body) or '').strip()
        if not text and not has_att: continue
        who_line = f'{handle or ""} {chat or ""}'
        if a.contact and a.contact.lower() not in who_line.lower(): continue
        if a.search and a.search.lower() not in text.lower(): continue
        key = (date, me, text[:40])
        if key in seen: continue
        seen.add(key)
        dt = to_dt(date)
        text = re.sub(r'\s+', ' ', text)
        if len(text) > a.width: text = text[:a.width - 1] + '…'
        if has_att and not text: text = '[attachment]'
        who = 'me' if me else (chat or handle or '?')[:18]
        out.append(f'{dt:%m-%d %H:%M} {who}: {text}')
    if len(out) > a.limit:
        out = [f'(showing last {a.limit} of {len(out)} messages)'] + out[-a.limit:]
    hdr = f'# iMessage digest  contact={a.contact!r} search={a.search!r} last {a.days}d  ({datetime.datetime.now():%Y-%m-%d %H:%M})'
    text = '\n'.join([hdr] + out) + '\n'
    if a.out:
        open(a.out, 'w').write(text); print(f'wrote {a.out}: {len(out)} msgs, {len(text)} chars (~{len(text)//4} tokens)')
    else: sys.stdout.write(text)

if __name__ == '__main__': main()
