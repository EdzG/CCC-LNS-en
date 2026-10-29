"""Shared helpers for the overlay tools: normalization/keys (must match en/toggle.js),
a throwaway local HTTP server, and Playwright page setup."""
import contextlib
import functools
import hashlib
import http.server
import json
import re
import threading
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EN = REPO / 'en'

# Same whitespace class and trimming as normalize() in en/toggle.js.
WS = re.compile('[ \t\n\r\f\v\u00a0\u3000\u2028\u2029\ufeff]+')
HAN = re.compile('[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')


def normalize(s):
    s = WS.sub(' ', s)
    if s.startswith(' '):
        s = s[1:]
    if s.endswith(' '):
        s = s[:-1]
    return s


def key_of(text):
    return hashlib.sha1(normalize(text).encode('utf-8')).hexdigest()[:12]


def has_han(s):
    return bool(HAN.search(s))


def chapter_arg(arg):
    """'IDL_115/Ch01-x/' or a path to it -> 'IDL_115/Ch01-x'."""
    p = Path(arg)
    if p.is_absolute():
        p = p.relative_to(REPO)
    if p.name == 'index.html':
        p = p.parent
    ch = p.as_posix().strip('/')
    if not (REPO / ch / 'index.html').exists():
        raise SystemExit(f'no index.html in {ch}')
    return ch


def strings_path(chapter):
    return EN / chapter / 'strings.json'


def load_strings(chapter):
    p = strings_path(chapter)
    if p.exists():
        return json.loads(p.read_text(encoding='utf-8'))
    return {}


def save_strings(chapter, data):
    p = strings_path(chapter)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def section_of(u):
    if u.get('ctx') == 'guide':
        return f"guide:{u.get('kp', 0)}"
    return f"kp{u['kp']}" if u.get('kp') else 'chrome'


def section_sort_key(sec):
    if sec == 'chrome':
        return (0, 0)
    if sec.startswith('kp'):
        return (1, int(sec[2:]))
    return (2, int(sec.split(':')[1]))


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


@contextlib.contextmanager
def serve():
    handler = functools.partial(_Quiet, directory=str(REPO))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        yield f'http://127.0.0.1:{srv.server_address[1]}'
    finally:
        srv.shutdown()


@contextlib.contextmanager
def open_page(chapter, lang='zh', browser='chromium', color_scheme='light', viewport=(1280, 900)):
    """Yield a Playwright page with the chapter loaded, toggle.js ready, KaTeX rendered."""
    from playwright.sync_api import sync_playwright
    with serve() as base, sync_playwright() as pw:
        b = getattr(pw, browser).launch()
        ctx = b.new_context(color_scheme=color_scheme,
                            viewport={'width': viewport[0], 'height': viewport[1]})
        ctx.add_init_script(f"try{{localStorage.setItem('ccc-lns-lang','{lang}')}}catch(e){{}}")
        page = ctx.new_page()
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.goto(f'{base}/{chapter}/index.html', wait_until='load')
        page.wait_for_function('window.__EN__ && window.__EN__.ready', timeout=15000)
        page.wait_for_timeout(500)      # page renderMath runs at load+50ms / onload+200ms
        if lang == 'en':
            page.wait_for_function("window.__EN__.lang === 'en'")
        page.errors = errors
        try:
            yield page
        finally:
            b.close()


def guide_keys(page):
    return page.evaluate("Object.keys(window.__GUIDES__ || {})")


def open_guide(page, k):
    page.evaluate(f"window.openGuide({json.dumps(k)})")
    page.wait_for_timeout(120)


def close_guide(page):
    page.evaluate("window.closeGuide && window.closeGuide()")
