"""Headless check of en/nav.js on every IDL_115 chapter (or the ones given).

    .venv/bin/python en/tools/navcheck.py [IDL_115/Ch01-... ...] [--browser firefox]

Per chapter: sections and quizzes found == study/chapters.json; a wrong answer records 0,
a right one 1, and a later wrong one keeps 1 (all four quiz families); next/prev section
move; prev/next chapter links are set; the scroll position survives a reload; the drawer
opens at phone width; toggle.js (if present) ignores the nav UI; no page errors from nav.js.
"""
import argparse
import json
import sys

from _common import REPO, chapter_arg, serve

# Answer one quiz container right or wrong, whatever its family.
ANSWER_JS = r"""([sel, kp, i, right]) => {
  const c = document.getElementById(kp), q = window.__NAV__.quizzesOf(c)[i];
  if (q.dataset.ans) {                                   // A: radios with value, .check
    const r = [...q.querySelectorAll('input[type=radio]')].find(x => (x.value === q.dataset.ans) === right);
    r.click(); q.querySelector('.check').click(); return 'A';
  }
  const radios = q.querySelectorAll('input[type=radio][data-correct]');
  if (radios.length) {                                   // B: radios with data-correct, .quiz-check
    [...radios].find(x => (x.dataset.correct === '1') === right).click();
    q.querySelector('.quiz-check').click(); return 'B';
  }
  const btns = [...q.querySelectorAll('.quiz-option-btn')];
  if (q.hasAttribute('data-answer')) {                   // C: data-answer index
    btns.find(b => (b.dataset.index === q.dataset.answer) === right).click(); return 'C';
  }
  btns.find(b => (b.dataset.correct === 'true') === right).click(); return 'D';   // D
}"""


def check_chapter(ctx, base, chapter, meta, phone):
    probs, errors = [], []
    page = ctx.new_page()
    page.on('pageerror', lambda e: errors.append(f'{e}\n{e.stack or ""}'))
    url = f'{base}/{chapter}/index.html'
    page.goto(url, wait_until='load')
    page.wait_for_function('window.__NAV__', timeout=10000)
    page.evaluate('window.__NAV__.chaptersReady')
    page.wait_for_timeout(300)

    secs = page.evaluate("window.__NAV__.cards.map(c => [c.id, window.__NAV__.quizzesOf(c).length])")
    want = [[s['id'], s['quizzes']] for s in meta['sections']]
    if secs != want:
        probs.append(f'sections/quizzes differ from chapters.json: {secs} vs {want}')

    # quizzes: first section with a quiz
    target = next(((kp, n) for kp, n in secs if n), None)
    family = '-'
    if target:
        kp = target[0]
        key = f'{kp}.0'
        state = lambda: page.evaluate(f"window.__NAV__.quiz.q[{json.dumps(key)}]")
        family = page.evaluate(ANSWER_JS, ['', kp, 0, False]); page.wait_for_timeout(60)
        a = state()
        page.evaluate(ANSWER_JS, ['', kp, 0, True]); page.wait_for_timeout(60)
        b = state()
        page.evaluate(ANSWER_JS, ['', kp, 0, False]); page.wait_for_timeout(60)
        c = state()
        stored = page.evaluate(f"JSON.parse(localStorage.getItem('ccc-lns-study:quiz:{meta['id']}')).q[{json.dumps(key)}]")
        if (a, b, c, stored) != (0, 1, 1, 1):
            probs.append(f'quiz {key} (family {family}): wrong/right/wrong recorded {a}/{b}/{c}, stored {stored}')

    # next / prev section
    page.evaluate("window.scrollTo({top: 0, behavior: 'instant'})")
    page.mouse.wheel(0, 1)                                # ends any restore
    page.wait_for_timeout(200)
    page.click('#study-nav button[aria-label="Next section"]')
    page.wait_for_timeout(1200)
    i1 = page.evaluate('window.__NAV__.currentIndex()')
    page.click('#study-nav button[aria-label="Next section"]')
    page.wait_for_timeout(1200)
    page.click('#study-nav button[aria-label="Previous section"]')
    page.wait_for_timeout(1200)
    i2 = page.evaluate('window.__NAV__.currentIndex()')
    if i1 < 0 or i2 != i1:
        probs.append(f'next/prev: after next {i1}, after next+next+prev {i2} (want equal, >= 0)')

    # chapter links
    hrefs = page.evaluate("""[...document.querySelectorAll('#study-nav a')].map(a =>
        [a.getAttribute('aria-label'), a.getAttribute('href'), a.getAttribute('aria-disabled')])""")
    links = {h[0]: h for h in hrefs}
    first, last = meta['_index'] == 0, meta['_last']
    if not links['Study dashboard'][1]:
        probs.append('no dashboard link')
    if bool(links['Previous chapter'][1]) == first or bool(links['Next chapter'][1]) == last:
        probs.append(f'chapter links wrong: {hrefs}')

    # scroll restore across a reload: middle of the section ~60% down the page
    k = max(1, int(len(secs) * 0.6))
    page.evaluate(f"""(() => {{ const c = window.__NAV__.cards[{k}], r = c.getBoundingClientRect();
        window.scrollTo({{top: r.top + scrollY + r.height * 0.4 - innerHeight * 0.25, behavior: 'instant'}}); }})()""")
    page.wait_for_timeout(700)
    before = page.evaluate('window.__NAV__.position()')
    page.reload(wait_until='load')
    page.wait_for_function('window.__NAV__', timeout=10000)
    page.wait_for_timeout(3000)
    after = page.evaluate('window.__NAV__.position()')
    if after['kp'] != before['kp'] or abs(after['f'] - before['f']) > 0.05:
        probs.append(f'restore: saved {before["kp"]} f={before["f"]:.2f}, after reload {after["kp"]} f={after["f"]:.2f}')

    # toggle.js must not pick up the nav UI
    if page.evaluate('!!window.__EN__'):
        bad = page.evaluate("""window.__EN__.collect().filter(u => /study-nav|study-drawer/.test(u.path)).length""")
        if bad:
            probs.append(f'toggle.js collected {bad} units inside the nav UI')

    nav_errors = [e for e in errors if 'nav.js' in e]
    probs += [f'page error from nav.js: {e.splitlines()[0]}' for e in nav_errors]
    page.close()

    # drawer at phone width (fresh page, so restore doesn't interfere)
    p2 = phone.new_page()
    p2.goto(url, wait_until='load')
    p2.wait_for_function('window.__NAV__', timeout=10000)
    p2.click('#study-nav .sn-pos')
    n = p2.evaluate("document.querySelectorAll('#study-drawer.open a[data-i]').length")
    if n != len(secs):
        probs.append(f'phone drawer shows {n} of {len(secs)} sections')
    p2.close()
    return family, probs, len(errors) - len(nav_errors)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapters', nargs='*')
    ap.add_argument('--browser', default='chromium')
    args = ap.parse_args()
    data = json.loads((REPO / 'study' / 'chapters.json').read_text(encoding='utf-8'))
    allch = data['chapters']
    for i, c in enumerate(allch):
        c['_index'], c['_last'] = i, i == len(allch) - 1
    by_path = {f"{data['course']}/{c['id']}": c for c in allch}
    chapters = [chapter_arg(c) for c in args.chapters] or list(by_path)

    from playwright.sync_api import sync_playwright
    failed = 0
    with serve() as base, sync_playwright() as pw:
        b = getattr(pw, args.browser).launch()
        ctx = b.new_context(viewport={'width': 1280, 'height': 900})
        phone = b.new_context(viewport={'width': 375, 'height': 760}, is_mobile=args.browser == 'chromium')
        for ch in chapters:
            fam, probs, other = check_chapter(ctx, base, ch, by_path[ch], phone)
            extra = f'  ({other} page errors not from nav.js)' if other else ''
            print(f'{ch:<56} quiz {fam}  {"ok" if not probs else "FAIL"}{extra}')
            for p in probs:
                print('    -', p)
            failed += bool(probs)
        b.close()
    print(f'{len(chapters) - failed}/{len(chapters)} chapters ok')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
