"""Add (or verify) the injected <script> lines in a page. Idempotent.

    .venv/bin/python en/tools/inject.py IDL_115/Ch01-introduction-history [--check]
    .venv/bin/python en/tools/inject.py IDL_115/Ch01-introduction-history/slides/01-x.html
    .venv/bin/python en/tools/inject.py --all --nav [--check]
    .venv/bin/python en/tools/inject.py --home [--check]

Lecture page (index.html): toggle.js and nav.js. --nav: nav.js only (every chapter gets it;
toggle.js only goes into translated ones); an existing toggle.js line is never removed.
--all --nav: nav.js into every IDL_115 page (lecture pages, condensed decks, slides).
Other pages (decks): toggle.js and nav.js (nav.js shows only a dashboard/lecture bar there).
On a page with an inline MathJax config the toggle.js line has no defer and goes right after
that config script, so toggle.js can hold MathJax's startup typeset (see toggle.js).
--home: the professor's root index.html gets study/home.js (redirect to the dashboard), as
the first thing after <meta charset>, so his page never paints.
"""
import argparse
import re
import sys

from _common import REPO, chapter_arg, html_of, is_lecture

SCRIPTS = {
    'toggle': re.compile(r'<script[^>]*\ben/toggle\.js\b[^>]*>\s*</script>'),
    'nav': re.compile(r'<script[^>]*\ben/nav\.js\b[^>]*>\s*</script>'),
}
HOME_RE = re.compile(r'<script[^>]*\bstudy/home\.js\b[^>]*>\s*</script>[ \t]*\r?\n?')
HOME_LINE = '<script src="study/home.js"></script>'


def process_home(check):
    path = REPO / 'index.html'
    with open(path, encoding='utf-8', newline='') as f:
        html = f.read()
    nl = '\r\n' if '\r\n' in html else '\n'
    found = [m.group(0).strip() for m in HOME_RE.finditer(html)]
    if found == [HOME_LINE]:
        print('index.html: home ok')
        return True
    if check:
        print(f'index.html: home MISSING or wrong: {found!r}')
        return False
    html = HOME_RE.sub('', html)
    m = re.search(r'<meta charset[^>]*>[ \t]*\r?\n', html, re.I) or re.search(r'<head[^>]*>[ \t]*\r?\n', html, re.I)
    if not m:
        sys.exit('index.html: no <meta charset> or <head> line')
    html = html[:m.end()] + HOME_LINE + nl + html[m.end():]
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(html)
    print('index.html: home injected')
    return True


def all_pages():
    out = []
    for d in sorted((REPO / 'IDL_115').iterdir()):
        if not (d / 'index.html').is_file():
            continue
        out.append(d.relative_to(REPO).as_posix())
        decks = sorted(f for f in d.glob('*.html') if f.name != 'index.html') + sorted((d / 'slides').glob('*.html'))
        out += [f.relative_to(REPO).as_posix()[:-5] for f in decks]
    return out


MATHJAX_CONFIG = re.compile(r'<script>\s*(?:window\.)?MathJax\s*=\s*\{.*?</script>[ \t]*\r?\n', re.S)


def wanted(chapter, name, mathjax=False):
    up = '../' * (len(html_of(chapter).relative_to(REPO).parts) - 1)
    defer = '' if mathjax else ' defer'
    return f'<script src="{up}en/{name}.js" data-chapter="{chapter}"{defer}></script>'


def process(chapter, names, check):
    path = html_of(chapter)
    with open(path, encoding='utf-8', newline='') as f:   # keep upstream line endings byte-exact
        html = f.read()
    nl = '\r\n' if '\r\n' in html else '\n'
    status = []
    for name in names:
        mj = name == 'toggle' and MATHJAX_CONFIG.search(html)
        tag_re, line = SCRIPTS[name], wanted(chapter, name, bool(mj))
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
        mj = name == 'toggle' and MATHJAX_CONFIG.search(html)
        if mj:
            html = html[:mj.end()] + line + nl + html[mj.end():]
        else:
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
    ap.add_argument('--home', action='store_true', help='root index.html: redirect to the dashboard')
    ap.add_argument('--check', action='store_true', help='exit 1 if a line is missing or wrong')
    args = ap.parse_args()
    if args.home:
        sys.exit(0 if process_home(args.check) else 1)
    if bool(args.chapter) == args.all:
        ap.error('give a chapter, --all or --home')
    if args.all and not args.nav:
        ap.error('--all needs --nav (toggle.js only goes into translated pages)')
    chapters = all_pages() if args.all else [chapter_arg(args.chapter)]
    ok = all([process(ch, ['nav'] if args.nav else ['toggle', 'nav'], args.check) for ch in chapters])
    if args.check:
        sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
