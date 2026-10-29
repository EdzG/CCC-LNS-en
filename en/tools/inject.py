"""Add (or verify) the injected <script> lines in a chapter's index.html. Idempotent.

    .venv/bin/python en/tools/inject.py IDL_115/Ch01-introduction-history [--check]
    .venv/bin/python en/tools/inject.py --all --nav [--check]

Default: toggle.js and nav.js (a chapter being translated). --nav: nav.js only (every chapter
gets it; toggle.js only goes into translated ones). --all: every IDL_115 chapter. An existing
toggle.js line is never removed by --nav.
"""
import argparse
import re
import sys

from _common import REPO, chapter_arg

SCRIPTS = {
    'toggle': re.compile(r'<script[^>]*\ben/toggle\.js\b[^>]*>\s*</script>'),
    'nav': re.compile(r'<script[^>]*\ben/nav\.js\b[^>]*>\s*</script>'),
}


def wanted(chapter, name):
    up = '../' * len(chapter.split('/'))
    return f'<script src="{up}en/{name}.js" data-chapter="{chapter}" defer></script>'


def process(chapter, names, check):
    path = REPO / chapter / 'index.html'
    with open(path, encoding='utf-8', newline='') as f:   # keep upstream line endings byte-exact
        html = f.read()
    nl = '\r\n' if '\r\n' in html else '\n'
    status = []
    for name in names:
        tag_re, line = SCRIPTS[name], wanted(chapter, name)
        found = tag_re.findall(html)
        if found == [line]:
            status.append(f'{name} ok')
            continue
        if check:
            status.append(f'{name} MISSING or wrong: {found!r}')
            continue
        if found:
            html = tag_re.sub('', html)
            html = re.sub(r'\r?\n[ \t]*\r?\n(?=</head>)', nl, html)
        if html.count('</head>') != 1:
            sys.exit(f'{chapter}: expected exactly one </head>')
        html = html.replace('</head>', line + nl + '</head>')
        status.append(f'{name} injected')
    if not check and any(s.endswith('injected') for s in status):
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(html)
    print(f'{chapter}: {", ".join(status)}')
    return all(s.endswith(' ok') for s in status)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter', nargs='?')
    ap.add_argument('--all', action='store_true', help='every IDL_115 chapter')
    ap.add_argument('--nav', action='store_true', help='nav.js only')
    ap.add_argument('--check', action='store_true', help='exit 1 if a line is missing or wrong')
    args = ap.parse_args()
    if bool(args.chapter) == args.all:
        ap.error('give a chapter or --all')
    chapters = ([d.relative_to(REPO).as_posix() for d in sorted((REPO / 'IDL_115').iterdir())
                 if (d / 'index.html').is_file()] if args.all else [chapter_arg(args.chapter)])
    names = ['nav'] if args.nav else ['toggle', 'nav']
    ok = all([process(ch, names, args.check) for ch in chapters])
    if args.check:
        sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
