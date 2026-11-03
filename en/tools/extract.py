"""Collect translatable units from a chapter (as toggle.js sees them) into strings.json.

    .venv/bin/python en/tools/extract.py IDL_115/Ch01-introduction-history
    .venv/bin/python en/tools/extract.py IDL_115/Ch01-introduction-history --browser firefox --dry-run

Keys are computed in the browser by toggle.js and re-checked here with the same
normalization. Existing translations are kept; units that vanished move to _stale.
"""
import argparse
import html
import re
import sys
from collections import Counter

from _common import (REPO, chapter_arg, close_guide, guide_keys, html_of, key_of, load_strings,
                     normalize, open_guide, open_page, save_strings, section_of, section_sort_key,
                     strings_path)


def strings_dir(chapter):
    return strings_path(chapter).parent

RESERVED = ('_runtime', '_dynamic', '_images', '_hide', '_zhText', '_stale')


def collect(chapter, browser):
    with open_page(chapter, lang='zh', browser=browser) as page:
        found = page.evaluate('window.__EN__.collect()')
        english = page.evaluate('window.__EN__.englishOnly()')
        for k in guide_keys(page):
            open_guide(page, k)
            found += [u for u in page.evaluate('window.__EN__.collect()') if u['ctx'] == 'guide']
            close_guide(page)
        if page.errors:
            print('page errors:', *page.errors, sep='\n  ', file=sys.stderr)
    return found, english


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter')
    ap.add_argument('--browser', default='chromium', choices=['chromium', 'firefox', 'webkit'])
    ap.add_argument('--dry-run', action='store_true', help='report only; compare keys with strings.json')
    ap.add_argument('--prune', action='store_true', help='delete vanished keys instead of moving them to _stale')
    args = ap.parse_args()
    chapter = chapter_arg(args.chapter)

    found, english = collect(chapter, args.browser)

    bad = [u for u in found if key_of(u['raw']) != u['key'] or normalize(u['raw']) != u['text']]
    for u in bad:
        print(f"HASH MISMATCH {u['key']} vs {key_of(u['raw'])}: {u['text'][:60]!r}", file=sys.stderr)

    raw_html = html_of(chapter).read_text(encoding='utf-8')
    raw_text = normalize(html.unescape(re.sub(r'</?[A-Za-z][^>]*>', '', raw_html)))
    for u in found:
        pieces = re.findall('[\u3400-\u9fff]{2,}', u['text'])
        if u['ctx'] in ('page', 'svg', 'chart') and any(p not in raw_text for p in pieces):
            print(f"WARN not in raw HTML (script-generated? add to _dynamic): {u['path']}: {u['text'][:60]!r}",
                  file=sys.stderr)

    # First occurrence (document order) wins for kp/ctx/path.
    units = {}
    for u in found:
        units.setdefault(u['key'], u)

    old = load_strings(chapter)
    if args.dry_run:
        old_keys = {k for k in old if not k.startswith('_')}
        new_keys = set(units)
        print(f'{args.browser}: {len(new_keys)} keys; strings.json: {len(old_keys)} keys')
        for k in sorted(new_keys - old_keys):
            print(f'  only in {args.browser}: {k} {units[k]["text"][:70]!r}')
        for k in sorted(old_keys - new_keys):
            print(f'  only in strings.json: {k} {normalize(old[k]["zh"])[:70]!r}')
        sys.exit(1 if bad or new_keys != old_keys else 0)

    out = {'_runtime': old.get('_runtime', {'exact': {}, 'patterns': []}),
           '_dynamic': old.get('_dynamic', []),
           '_images': old.get('_images', [])}
    for k in ('_hide', '_zhText'):
        if old.get(k):
            out[k] = old[k]
    stale = dict(old.get('_stale', {}))
    review = 0
    for k, u in units.items():
        prev = old.get(k) or stale.pop(k, None) or {}
        e = {'zh': u['zh'], 'en': prev.get('en', ''), 'kp': u['kp'], 'ctx': u['ctx']}
        if u['attr']:
            e['attr'] = u['attr']
        if prev.get('review') or (prev and prev.get('en') and prev.get('zh') != u['zh']):
            e['review'] = True
            review += 1
        out[k] = e
    for k, v in old.items():
        if not k.startswith('_') and k not in units:
            stale[k] = v
    if stale and not args.prune:
        out['_stale'] = stale
    save_strings(chapter, out)

    per = Counter()
    done = Counter()
    for k, u in units.items():
        s = section_of(u)
        per[s] += 1
        done[s] += bool(out[k]['en'])
    for s in sorted(per, key=section_sort_key):
        print(f'{s:10} {done[s]:4}/{per[s]:<4}')
    print(f'{len(units)} keys ({len(found)} occurrences), {sum(done.values())} translated, '
          f'{review} need review, {len(stale)} stale{" (pruned)" if args.prune else ""}')
    # Inline data: URI images (decks): print their _images keys and dump them for /redraw-chart.
    imgs = re.findall(r'<img[^>]*?src="(data:image/([a-z+]+);base64,([^"]+))"', raw_html)
    if imgs:
        import base64
        import hashlib
        dump = REPO / 'scratch' / 'img' / chapter.replace('/', '__')
        dump.mkdir(parents=True, exist_ok=True)
        listed = {i['key']: i['file'] for i in out['_images'] if isinstance(i, dict)}
        print(f'{len(imgs)} inline images (dumped to {dump.relative_to(REPO)}):')
        for n, (src, kind, b64) in enumerate(imgs):
            key = hashlib.sha1(src.encode('utf-8')).hexdigest()[:12]
            ext = 'jpg' if kind == 'jpeg' else kind.replace('+xml', '')
            (dump / f'{n:02d}-{key}.{ext}').write_bytes(base64.b64decode(b64))
            print(f'  #{n} key {key}  ' + (f'-> {listed[key]}' if key in listed else 'not in _images'))
    if english:
        # The professor's English that EN mode would show as is. Either it pairs a Chinese unit
        # (hide it: add a selector to _hide) or it stands alone (review it).
        rep = strings_dir(chapter) / 'english-only.txt'
        rep.write_text(''.join(f"kp{e['kp']}\t{e['path']}\t.{e['cls']}\n\t{e['text']}\n" for e in english), encoding='utf-8')
        print(f'{len(english)} English-only blocks visible in EN mode: see {rep.relative_to(REPO)}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
