"""Add (or verify) the single toggle.js line in a chapter's index.html. Idempotent.

    .venv/bin/python en/tools/inject.py IDL_115/Ch01-introduction-history [--check]
"""
import argparse
import re
import sys

from _common import REPO, chapter_arg

TAG_RE = re.compile(r'<script[^>]*\ben/toggle\.js\b[^>]*>\s*</script>')


def wanted(chapter):
    up = '../' * len(chapter.split('/'))
    return f'<script src="{up}en/toggle.js" data-chapter="{chapter}" defer></script>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter')
    ap.add_argument('--check', action='store_true', help='exit 1 if the line is missing or wrong')
    args = ap.parse_args()
    chapter = chapter_arg(args.chapter)
    path = REPO / chapter / 'index.html'
    with open(path, encoding='utf-8', newline='') as f:   # keep upstream line endings byte-exact
        html = f.read()
    nl = '\r\n' if '\r\n' in html else '\n'
    line = wanted(chapter)
    found = TAG_RE.findall(html)

    if args.check:
        ok = found == [line]
        print(f'{chapter}: {"ok" if ok else "MISSING or wrong: " + repr(found)}')
        sys.exit(0 if ok else 1)

    if found == [line]:
        print(f'{chapter}: already injected')
        return
    if found:
        html = TAG_RE.sub('', html)
        html = re.sub(r'\r?\n[ \t]*\r?\n(?=</head>)', nl, html)
    if html.count('</head>') != 1:
        sys.exit(f'{chapter}: expected exactly one </head>')
    html = html.replace('</head>', line + nl + '</head>')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(html)
    print(f'{chapter}: injected')


if __name__ == '__main__':
    main()
