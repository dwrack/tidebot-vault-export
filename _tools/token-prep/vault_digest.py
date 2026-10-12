#!/usr/bin/env python3
"""One-page digest of a vault folder, so Claude reads this instead of `ls -R` + `cat`.

Usage:
  python3 vault_digest.py "<folder>" [--out digest.md] [--max-lines 120] [--depth 3]
  python3 vault_digest.py --find "cave point wind" [--in "<folder>"]   # Spotlight (mdfind) lookup

What it emits (capped at --max-lines, default 120 lines ~ 1,200 tokens):
  * folder tree with file counts and sizes (no per-file listing past --depth)
  * for each .md/.txt/.csv: size, modified date, frontmatter keys, H1/H2 headings, first content line
  * images/PDFs/videos: counted, with dimensions via `sips` when available (never opened)
Nothing is installed; python3, mdfind and sips ship with macOS.
"""
import argparse, os, re, subprocess, sys, datetime, shutil

TEXT = {'.md', '.txt', '.csv', '.json', '.yaml', '.yml'}
IMG = {'.png', '.jpg', '.jpeg', '.heic', '.gif', '.webp', '.tif', '.tiff'}
MEDIA = {'.mp4', '.mov', '.m4v', '.mp3', '.m4a', '.wav', '.pdf'}

def human(n):
    for u in ('B', 'K', 'M', 'G'):
        if n < 1024: return f'{n:.0f}{u}'
        n /= 1024
    return f'{n:.0f}T'

def sips_dims(path):
    if not shutil.which('sips'): return ''
    try:
        out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path],
                             capture_output=True, text=True, timeout=5).stdout
        w = re.search(r'pixelWidth: (\d+)', out); h = re.search(r'pixelHeight: (\d+)', out)
        return f' {w.group(1)}x{h.group(1)}' if w and h else ''
    except Exception:
        return ''

def digest_text(path, max_chars=20000):
    try:
        with open(path, 'r', errors='replace') as f: s = f.read(max_chars)
    except Exception as e:
        return [f'(unreadable: {e})']
    lines = s.splitlines()
    out = []
    fm_keys = []
    if lines and lines[0].strip() == '---':
        for i, l in enumerate(lines[1:], 1):
            if l.strip() == '---': lines = lines[i + 1:]; break
            m = re.match(r'^([A-Za-z0-9_-]+):', l)
            if m: fm_keys.append(m.group(1))
    if fm_keys: out.append('fm: ' + ', '.join(fm_keys[:10]))
    heads = [l.strip() for l in lines if re.match(r'^#{1,2} ', l)]
    if heads: out.append('h: ' + ' | '.join(h.lstrip('# ')[:50] for h in heads[:8]))
    first = next((l.strip() for l in lines if l.strip() and not l.startswith('#')), '')
    if first: out.append('> ' + first[:140])
    return out

def walk(root, depth, max_lines):
    lines = []
    root = os.path.abspath(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.'))
        rel = os.path.relpath(dirpath, root)
        level = 0 if rel == '.' else rel.count(os.sep) + 1
        files = sorted(f for f in filenames if not f.startswith('.'))
        if level > depth:
            dirnames[:] = []  # stop descending
            continue
        n_img = sum(1 for f in files if os.path.splitext(f)[1].lower() in IMG)
        n_media = sum(1 for f in files if os.path.splitext(f)[1].lower() in MEDIA)
        total = sum(os.path.getsize(os.path.join(dirpath, f)) for f in files)
        lines.append(f"{'  ' * level}{'/' if rel == '.' else rel.split(os.sep)[-1] + '/'}  ({len(files)} files, {human(total)}; {n_img} img, {n_media} media)")
        if level == depth:
            continue
        for f in files:
            p = os.path.join(dirpath, f); ext = os.path.splitext(f)[1].lower()
            try: st = os.stat(p)
            except OSError: continue
            mod = datetime.date.fromtimestamp(st.st_mtime).isoformat()
            pad = '  ' * (level + 1)
            if ext in TEXT:
                lines.append(f'{pad}{f}  [{human(st.st_size)}, {mod}]')
                for d in digest_text(p): lines.append(f'{pad}  {d}')
            elif ext in IMG:
                lines.append(f'{pad}{f}  [img {human(st.st_size)}{sips_dims(p)}, {mod}]')
            else:
                lines.append(f'{pad}{f}  [{ext or "file"} {human(st.st_size)}, {mod}]')
            if len(lines) > max_lines * 3: break
    if len(lines) > max_lines:
        lines = lines[:max_lines] + [f'... truncated ({len(lines) - max_lines} more lines); re-run with a subfolder or larger --max-lines']
    return lines

def spotlight(query, folder):
    if not shutil.which('mdfind'):
        return ['mdfind not available on this machine (macOS only)']
    cmd = ['mdfind']
    if folder: cmd += ['-onlyin', folder]
    cmd.append(query)
    out = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
    return [f'{len(out)} match(es) for {query!r}'] + out[:40]

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('folder', nargs='?')
    ap.add_argument('--find'); ap.add_argument('--in', dest='inside')
    ap.add_argument('--out'); ap.add_argument('--max-lines', type=int, default=120)
    ap.add_argument('--depth', type=int, default=3)
    a = ap.parse_args()
    if a.find:
        lines = spotlight(a.find, a.inside)
    elif a.folder:
        lines = [f'# Digest of {a.folder}  ({datetime.datetime.now():%Y-%m-%d %H:%M})'] + walk(a.folder, a.depth, a.max_lines)
    else:
        ap.error('give a folder or --find')
    text = '\n'.join(lines) + '\n'
    if a.out:
        open(a.out, 'w').write(text); print(f'wrote {a.out}: {len(lines)} lines, {len(text)} chars (~{len(text)//4} tokens)')
    else:
        sys.stdout.write(text)
