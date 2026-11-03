"""Headless check of a chapter in EN mode: which blocks still show Chinese?

    .venv/bin/python en/tools/coverage.py IDL_115/Ch01-introduction-history
    .venv/bin/python en/tools/coverage.py IDL_115/Ch01-introduction-history \
        --expect-clean chrome,kp1,kp2,guide:1,guide:2 --shots kp1,kp2,guide:1 --out scratch/shots

Reports, per section (chrome, kpN, guide:N):
  static   units with no English in strings.json (incl. data-expl quiz explanations)
  runtime  script-written text (quiz feedback, readouts, progress) with no runtime rule,
           after clicking through every quiz and demo
  canvas   canvas text drawn in EN mode with no runtime rule
  redraw   demos whose canvas draws Chinese but does not redraw on toggle, or whose state
           changes when toggled
Exit status is 1 if any --expect-clean section has findings.
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

from _common import (REPO, chapter_arg, close_guide, guide_keys, is_lecture, open_guide, open_page,
                     section_of, section_sort_key)

# Decks (no .quiz/.demo conventions): click every button and fire every control once.
EXERCISE_GENERIC = """async () => {
  const tick = (ms) => new Promise(r => setTimeout(r, ms || 0));
  const skip = (el) => el.closest('#en-toggle, [data-en-skip], .theme-toggle, .back-to-top');
  for (const b of document.querySelectorAll('button, [role=button], .option, .quiz-option, .opt')) {
    if (skip(b)) continue;
    try { b.click(); } catch (e) {}
    await tick(20);
  }
  for (const c of document.querySelectorAll('input[type=range], input[type=number], input[type=radio], input[type=checkbox], select')) {
    if (skip(c)) continue;
    if (c.type === 'radio' || c.type === 'checkbox') { c.click(); continue; }
    c.dispatchEvent(new Event('input', {bubbles: true}));
    c.dispatchEvent(new Event('change', {bubbles: true}));
  }
  await tick(600);
}"""

EXERCISE_QUIZZES = """async () => {
  const tick = (ms) => new Promise(r => setTimeout(r, ms || 0));
  for (const qz of document.querySelectorAll('.quiz')) {
    const btn = qz.querySelector('.check'), radios = [...qz.querySelectorAll('input[type=radio]')];
    if (!btn) continue;
    radios.forEach(r => r.checked = false); btn.click(); await tick();
    const wrong = radios.find(r => r.value !== qz.dataset.ans);
    if (wrong) { wrong.checked = true; btn.click(); await tick(); }
    const right = radios.find(r => r.value === qz.dataset.ans);
    if (right) { right.checked = true; btn.click(); await tick(); }
  }
}"""

EXERCISE_DEMOS = """async () => {
  const tick = (ms) => new Promise(r => setTimeout(r, ms || 0));
  for (const d of document.querySelectorAll('.demo')) {
    for (const b of d.querySelectorAll('button')) { b.click(); await tick(30); }
    for (const c of d.querySelectorAll('input[type=range], input[type=number], select')) {
      c.dispatchEvent(new Event('input', {bubbles: true}));
      if (c.tagName === 'SELECT') c.dispatchEvent(new Event('change', {bubbles: true}));
    }
  }
  await tick(600);
}"""

REDRAW_CHECK = """async () => {
  const tick = (ms) => new Promise(r => setTimeout(r, ms || 0));
  const han = new Set(window.__EN__.hanCanvases());
  const demos = document.querySelector('.demo') ? [...document.querySelectorAll('.demo')]
    : [...document.querySelectorAll('canvas')].map(c => c.parentElement);
  const h = (s) => { let x = 0; for (let i = 0; i < s.length; i++) x = (x * 31 + s.charCodeAt(i)) | 0; return x; };
  const snap = () => demos.map(d => ({
    cv: [...d.querySelectorAll('canvas')].map(c => { try { return h(c.toDataURL()); } catch (e) { return 0; } }),
    ro: [...d.querySelectorAll('.demo-readout')].map(r => r.textContent).join('\\n')
  }));
  const a = snap(); window.__EN__.setLang('zh'); await tick(300);
  const b = snap(); window.__EN__.setLang('en'); await tick(300);
  const c = snap();
  return demos.map((d, i) => {
    const cvs = [...d.querySelectorAll('canvas')];
    const id = d.getAttribute('data-demo-id') || ('demo' + i);
    const sec = d.closest('[data-kp]');
    const out = {id, kp: sec ? +sec.dataset.kp : 0, issues: []};
    cvs.forEach((cv, j) => {
      if (han.has(cv) && a[i].cv[j] === b[i].cv[j]) out.issues.push('canvas ' + j + ' draws Chinese but did not redraw on toggle');
      if (a[i].cv[j] !== c[i].cv[j]) out.issues.push('canvas ' + j + ' differs after EN→中→EN (state changed by toggle?)');
    });
    if (a[i].ro !== c[i].ro) out.issues.push('readout differs after EN→中→EN (state changed by toggle?)');
    return out;
  });
}"""


def short(s, n=60):
    s = s.replace('\n', ' ')
    return s if len(s) <= n else s[:n - 1] + '…'


def check(chapter, browser):
    findings = defaultdict(list)          # section -> [(kind, detail)]
    with open_page(chapter, lang='en', browser=browser) as page:
        units = page.evaluate('window.__EN__.collect()')
        for k in guide_keys(page):
            open_guide(page, k)
            units += [u for u in page.evaluate('window.__EN__.collect()') if u['ctx'] == 'guide']
            close_guide(page)
        seen = set()
        for u in units:
            if u['translated'] or (u['key'], section_of(u)) in seen:
                continue
            seen.add((u['key'], section_of(u)))
            what = u['ctx'] + (f"[{u['attr']}]" if u['attr'] else '')
            findings[section_of(u)].append(('static', f"{u['key']} {what:12} {u['path']}\n{'':20}{short(u['text'])}"))

        if is_lecture(chapter):
            page.evaluate(EXERCISE_QUIZZES)
            page.evaluate(EXERCISE_DEMOS)
        else:
            page.evaluate(EXERCISE_GENERIC)
        redraw = page.evaluate(REDRAW_CHECK)
        for d in redraw:
            for issue in d['issues']:
                findings[f"kp{d['kp']}" if d['kp'] else 'chrome'].append(('redraw', f"demo {d['id']}: {issue}"))
        for m in page.evaluate('window.__EN__.misses'):
            sec = f"kp{m['kp']}" if m['kp'] else 'chrome'
            findings[sec].append((m['where'], f"{m['path']}\n{'':20}{short(m['text'], 90)}"))
        errors = page.errors
    return findings, errors


def shots(chapter, browser, sections, out):
    out.mkdir(parents=True, exist_ok=True)
    for lang in ('zh', 'en'):
        with open_page(chapter, lang=lang, browser=browser, viewport=(1280, 2400)) as page:
            page.add_style_tag(content='#guide-modal .modal,#guide-modal .modal-box{max-height:none!important}')
            for sec in sections:
                name = sec.replace(':', '')
                if sec.startswith('guide:'):
                    open_guide(page, sec.split(':')[1])
                    page.wait_for_timeout(300)
                    page.locator('#guide-modal .modal, #guide-modal .modal-box').first.screenshot(path=str(out / f'{name}-{lang}.png'))
                    close_guide(page)
                elif is_lecture(chapter):
                    page.locator(f'section#{sec}').screenshot(path=str(out / f'{name}-{lang}.png'))
                else:                   # kpN = Nth outermost section / .section, as toggle.js counts
                    el = page.evaluate_handle(f"""[...document.querySelectorAll('section, .section')]
                        .filter(s => !s.parentElement.closest('section, .section'))[{int(sec[2:]) - 1}]""")
                    el.as_element().scroll_into_view_if_needed()
                    page.wait_for_timeout(400)
                    el.as_element().screenshot(path=str(out / f'{name}-{lang}.png'))
    print(f'screenshots in {out}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter')
    ap.add_argument('--browser', default='chromium', choices=['chromium', 'firefox', 'webkit'])
    ap.add_argument('--expect-clean', default='', help='comma list of sections that must have no findings')
    ap.add_argument('--shots', default='', help='comma list of sections (kpN, guide:N) to screenshot in both modes')
    ap.add_argument('--out', default='scratch/shots')
    args = ap.parse_args()
    chapter = chapter_arg(args.chapter)

    findings, errors = check(chapter, args.browser)
    total = 0
    for sec in sorted(findings, key=section_sort_key):
        items = findings[sec]
        total += len(items)
        kinds = defaultdict(int)
        for kind, _ in items:
            kinds[kind] += 1
        print(f"\n== {sec}: {len(items)} untranslated ({', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))})")
        for kind, detail in items:
            print(f'  {kind:8} {detail}')
    print(f'\nTOTAL {total} untranslated in EN mode' + (' (0: chapter is clean)' if not total else ''))
    if errors:
        print('page errors:', *errors, sep='\n  ')

    if args.shots:
        out = Path(args.out)
        shots(chapter, args.browser, args.shots.split(','), out if out.is_absolute() else REPO / out)

    clean = [s for s in args.expect_clean.split(',') if s]
    dirty = [s for s in clean if findings.get(s)]
    if clean:
        print(f"expect-clean {','.join(clean)}: " + ('OK' if not dirty else 'FAILED: ' + ', '.join(dirty)))
    sys.exit(1 if dirty or (errors and clean) else 0)


if __name__ == '__main__':
    main()
