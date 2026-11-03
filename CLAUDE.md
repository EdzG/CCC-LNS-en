# CCC-LNS-en: English overlay for the NDHU IDL 115 lecture pages

## What this repo is
A private copy of the professor's course site (`ndhuccc/CCC-LNS`) with a 中/EN toggle added.
The goal is a study tool for an English speaker: English is the default, and one button switches the whole
page (prose, headings, quizzes, 教授祕笈 boxes, demo text, and chart images) to English.

Only `IDL_115/` (Introductory Deep Learning) is in scope. Ignore `PR_115/` unless asked.
Each chapter has a lecture page (`index.html`) and may have a condensed deck (`idl115-*.html`)
and slide decks (`slides/*.html`); all of them can get the overlay.

## Remotes (never break these)
- `origin` = `git@github.com:EdzG/CCC-LNS-en.git` (private, ours). Push here only.
- `upstream` = `https://github.com/ndhuccc/CCC-LNS.git` (professor). Push is disabled. Never re-enable it.
- Get professor updates with `git fetch upstream && git merge upstream/main`.

## The overlay rule (most important)
**Never hand-edit the professor's files.** All English lives under `en/`.
The only changes to upstream files are injected `<script>` lines before `</head>` in each
page, added by `en/tools/inject.py` (idempotent, so it can be re-run after a merge): nav.js in
**every** IDL_115 page (lecture pages, condensed decks, slides), toggle.js only in translated ones,
and `study/home.js` in the professor's root `index.html` (it redirects to the dashboard, so the
dashboard is the site's front page; `index.html?upstream` still shows his page).

```html
<script src="../../en/toggle.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
<script src="../../en/nav.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
```

Keeping upstream files untouched means `git merge upstream/main` stays conflict-free, and
only paragraphs the professor actually changed need re-translating.

## Layout
```
en/
├─ toggle.js                         # the 中/EN button + swapping engine (shared by all chapters)
├─ nav.js                            # study navigation (see "Study layer"); independent of toggle.js
├─ tools/
│  ├─ extract.py                     # pull translatable units from a chapter into strings.json
│  ├─ inject.py                      # add/verify the injected <script> lines in a chapter
│  ├─ coverage.py                    # headless check: any Chinese left visible in EN mode?
│  ├─ navcheck.py                    # headless check of nav.js on every chapter
│  ├─ _common.py                     # normalize/key_of (must match toggle.js), server, Playwright
│  └─ charts/<chapter>/<name>.py     # one matplotlib script per redrawn chart
└─ IDL_115/<chapter>/                  # = a page id; decks: IDL_115/<chapter>/slides/<stem>/ etc.
   ├─ strings.json                   # _runtime/_dynamic/_images + { key: { zh, en, kp, ctx } }
   ├─ notes.md                       # errors/ambiguities found in the Chinese source
   └─ assets/<same filename>.png     # English redraw of a chart with Chinese labels
study/
├─ index.html                        # personal dashboard (English UI), served at /study/
├─ build_chapters.py                 # stdlib-only: scan IDL_115/ -> chapters.json
├─ home.js                           # injected into the root index.html: redirect to /study/
├─ serve.py                          # local server: / -> /study/ (stdlib only)
├─ chapters.json                     # generated, committed; never hand-edit
└─ titles_en.json                    # hand-written English chapter titles (new chapter = add one)
```

## Page ids (lecture pages and decks)
Every tool takes a page: `IDL_115/<chapter>` (its `index.html`) or a deck file
(`IDL_115/<chapter>/slides/01-x.html`, `IDL_115/<chapter>/idl115-w1-x.html`). The page id is the
path without `.html` (lecture: the folder). It is toggle.js's `data-chapter` and the folder under
`en/` holding that page's `strings.json`, `notes.md` and `assets/`. Decks get toggle.js (once
translated) and nav.js, which shows only a small bottom-left bar there (⌂ Dashboard, ‹ Lecture).

## How the engine works (design decisions, keep consistent)
toggle.js runs synchronously when its deferred `<script>` executes: the whole page is parsed,
KaTeX has not rendered yet (the page renders at load+50 ms / auto-render onload+200 ms).

- **Units = leaf blocks, chosen generically.** The collector walks `<body>` top-down.
  *Boundary* elements are block tags (`p, li, h1-h6, td, th, figcaption, div, section, ul, ol,
  table, tr, figure, details, summary, pre, nav, header, footer, main, option, ...`) plus opaque
  ones (`input, select, textarea, button, canvas, svg, img, iframe, ...`). An element with no
  boundary descendants is one unit (innerHTML swap). A container that mixes inline content
  with boundary children is split into runs: a run of only elements gives one unit per element
  (e.g. each `nav a.toc-item`); a run with loose text is wrapped at runtime in
  `<span data-en-run>` (live DOM only, never the file). SVG `<text>`/`<tspan>` are units that
  swap `textContent` (`ctx: "svg"`, plain-text `en`). Units with no Han characters are ignored.
  Skipped entirely: `script, style, .katex, .ai-illustration` (AI 生圖 prompts stay Chinese),
  `#en-toggle`, `[data-en-skip]` (nav.js's own UI), and `_dynamic` selectors.
- **Keys:** `key = sha1(normalize(textContent))[:12]` of the text captured before KaTeX runs
  (so math is its raw `$...$` source). `normalize` = replace every run of
  `[ \t\n\r\f\v\u00a0\u3000\u2028\u2029\ufeff]` with one space, then strip one leading/trailing space.
  Text, not innerHTML, so attributes injected by browser extensions don't change keys.
  Python (`en/tools/_common.py`) has the identical `normalize`/`key_of`; extract.py re-checks
  every key. Keys are verified identical in Chromium and Firefox. Same text = same key
  everywhere (one translation covers all 40「檢查」buttons); if a key is used by an SVG unit,
  its `en` must be plain text.
- **`zh` = captured innerHTML** (raw math); swapping sets `innerHTML = en`, then
  `renderMathInElement(el)` with `$$`, `$`, `\(`, `\[` and `ignoredClasses:['katex']`. Back to 中
  restores `zh` and re-renders. If the professor changes only markup (same text, same key),
  extract.py updates `zh` and sets `"review": true`; re-check the inline tags in `en`, then delete
  the flag.
- **Math is never translated.** Keep every `$...$`, `$$...$$`, `\(...\)` exactly as in the source.
  One exception: Chinese inside a `\text{...}` argument (e.g. `\text{所有你願意考慮的函數}`) is
  translated, and nothing else in that formula changes. In a bilingual block whose two halves
  repeat a formula, the English keeps it once.
- **MathJax pages (the decks).** MathJax (SVG) may typeset before a deferred script runs, so
  inject.py puts toggle.js *without* `defer` right after the inline `window.MathJax = {...}` config.
  toggle.js then sets `MathJax.startup.typeset = false`, captures on DOMContentLoaded, and starts the
  typeset itself, once, after strings.json has loaded and the initial language is applied (a swap
  during a running typeset leaves MathJax with detached nodes and every later typeset fails).
  Swaps call `MathJax.typesetClear([el])` before replacing content, and every
  `MathJax.typesetPromise(els)` is queued on `MathJax.startup.promise`. `mjx-container` is skipped
  like `.katex`.
- **Sections on decks:** pages without `data-kp` number the outermost `section, .section` elements
  1..n in document order; that number is the unit's `kp` (and `kpN` in coverage `--shots`).
- **Chart.js:** chart strings are translated in the chart's config (`chart.config._config`, every
  string with Han, `ctx: "chart"`, plain-text `en`), never only on the canvas (Chart.js measures text
  first). Existing charts are walked on each switch and `update('none')`d; a global plugin
  (`beforeUpdate`) covers charts created or updated later. Strings computed in callbacks still go
  through the `fillText` hook and `_runtime`.
- **`_hide`** (list of CSS selectors, one simple selector each, no commas): hidden while EN is on
  (`html.en-on`). For the professor's English that sits in its own element next to a Chinese unit
  (`.en-sub` beside `.zh-sub`, a standalone `.bilingual-en` block): our translation of the Chinese
  replaces both. English inside a unit (`<h2>中文 <span class="en">…</span></h2>`) needs nothing:
  the unit's innerHTML is swapped. Our English is always translated from the Chinese; the
  professor's English is a reference only.
- **English-only blocks:** `extract.py` writes `en/<page>/english-only.txt` (not committed): visible
  blocks with English but no Chinese outside any unit. Each one is either a pair (add to `_hide`),
  or stands alone and stays as is (check it reads correctly; note errors in `notes.md`).
- **Attributes:** `title`, `alt`, `placeholder`, `aria-label` get their own entries
  (`ctx: "attr"`, `"attr": name`) and are swapped in place. **`data-expl`** (quiz explanation)
  is translated in strings.json (`ctx: "expl"`) but the attribute is **never mutated**,
  because the page's quiz JS reads it; the runtime pattern `$T1` (below) translates it.
- **`_dynamic`** (list of CSS selectors): elements whose content is written by page JS
  (Ch01: `.demo-readout`, `#ptxt`, `.fb`). Excluded from static units, handled by `_runtime`.
  extract.py warns "not in raw HTML" for units that look script-generated: add them here.
- **`_runtime`** = `{"exact": {zh: en}, "patterns": [{"re": "...", "en": "..."}]}`. Applied per
  line of each text node (multi-line readouts work) written while EN is on, by a
  MutationObserver, plus one pass over existing text on every switch. Lookup order per line:
  `exact`, then any static unit/attr/expl with the same normalized text, then the first matching
  pattern. In `en`, `$1` inserts capture group 1 as-is; `$T1` inserts it translated by that
  same lookup (e.g. `"^✗ 答錯：([\s\S]*)$" → "✗ Incorrect: $T1"`). The original Chinese is kept
  per text node so switching back restores it. Do not edit demo JavaScript.
- **Script text with rendered math:** when a page writes runtime text with `innerHTML` and renders
  KaTeX right away (Ch02 quiz feedback: `'✗ 答錯：'+expl` then `renderMath()`), the observer sees the
  line already split around `.katex` nodes. toggle.js rebuilds the line from each formula's TeX
  source (`annotation[encoding="application/x-tex"]`, as `$…$`), translates it whole, writes it back
  as text and re-renders; switching back restores it. Lookups treat `\(x\)` and `$x$` (and
  `\[x\]`, `$$x$$`) as equal, so `$T1` finds `expl` translations written with either delimiter.
  Decks do the same with MathJax (`fb.innerHTML = …` then `typesetPromise([fb])`): an
  `mjx-container`'s TeX comes from MathJax's math item (`getMathItemsWithin`). The rebuilt element
  is the one holding the formula (past KaTeX's bare wrapper `<span>`), so a formula inside one
  `<strong>` of a readout rebuilds only that `<strong>`. Deck quiz feedback therefore needs a
  whole-line pattern per prefix (`^❌ 答錯了！\s*請重新思考：([\s\S]*)$` → `❌ Incorrect! Think again: $T1`)
  plus an `exact` entry for each explanation.
- **`_zhText`** (list of CSS selectors): while EN is on, `innerText` of a matching element returns
  the original Chinese (units' captured text, runtime text's Chinese). For page JS that picks text by
  searching for Chinese keywords: the Ch03/Ch04 decks choose each quiz explanation with
  `card.innerText.includes('題目 1')` (or `.q-num`, `.q`), so their strings.json has
  `"_zhText": [".quiz-card", ".q-num", ".q"]`; without it most explanations come out empty in EN.
- **Live elements inside units:** swapping a unit keeps its live `[id]` descendants (e.g.
  `<output id=…>` in a `<label>`, `#boundaryStatus`): the new copies are replaced by the original
  nodes, which get `data-en-live`. Page scripts keep working on them, and text inside them counts
  as runtime text (translated through `_runtime`, misses reported by coverage).
- **Observer hygiene:** the observer is disconnected during bulk swaps and math re-rendering,
  and `takeRecords()` discards our own writes. It ignores nodes inside `.katex` and inside static
  units, and math records (added `.katex` / `mjx-container` nodes) never count as content changes.
- **教授祕笈 guides** live in `window.__GUIDES__` and are injected by `openGuide(n)` into
  `#guide-title`/`#guide-body`. The observer sees that childList change (a microtask, before the
  page's 50 ms renderMath), captures fresh units (`ctx: "guide"`, `kp` = guide number found by
  matching the title) and swaps them if EN is on. extract.py/coverage.py open every guide.
- **Canvas:** `CanvasRenderingContext2D.prototype.fillText/strokeText` are wrapped. In EN mode
  the text goes through `_runtime`; unmatched Han text is recorded as a miss. Because demos draw
  during parse, every language switch fires `input` on each `.demo`'s range/number/select
  controls (and `change` on selects; on decks, which have no `.demo`, every such control on the
  page outside `[data-en-skip]`) so canvases redraw at once. coverage.py reports demos
  that draw Chinese but don't redraw this way (Ch01: KP6 only redraws on its 計算 button).
- **`_images`** (list of filenames): only `img` whose src basename is listed is swapped to
  `en/<chapter>/assets/<file>` in EN mode. No HEAD checks. Decks embed their images as `data:`
  URIs: list those as `{"key": "<sha1(src)[:12]>", "file": "<name>.png"}`. extract.py prints each
  inline image's key and dumps it to `scratch/img/<page id with __>/` for `/redraw-chart`. Textbook figures (the hashed `*.jpg`
  crops) are already English and need no redraw.
- **Toggle UI:** fixed 中 | EN pill (top-right, z-index 1000; moved left of any fixed page control
  it would cover, e.g. a deck's theme button), `Alt+L`, state in
  `localStorage['ccc-lns-lang']` (try/catch), default EN (only a saved `'zh'` shows 中), `<html lang>` updated, light/dark tokens.
  If the saved state is EN, the body stays hidden (pill visible) until strings.json arrives (1.5 s max).
- Missing translation in EN mode: the Chinese stays visible with class `en-missing` (dashed
  amber outline). Never show an empty block.
- **strings.json** reserved keys start with `_`: `_runtime`, `_dynamic`, `_images`, `_hide`, `_zhText`, `_stale`
  (keys that vanished from the page; `--prune` deletes them). Every other key is a unit:
  `{zh, en, kp, ctx: page|svg|attr|expl|guide|chart, attr?, review?}`; `kp: 0` = page chrome.
- `window.__EN__` exposes `setLang`, `collect()`, `rewritten()`, `misses`, `hanCanvases()`, `ready` for the tools.

## Tools
- `inject.py <page> [--check]`: adds the toggle.js and nav.js lines before `</head>`, byte-exact
  otherwise (upstream files are CRLF; keep it that way). `--nav` adds nav.js only (never removes
  toggle.js); `--all --nav` covers every IDL_115 page, decks included; `--home` injects
  `study/home.js` into the root `index.html` right after `<meta charset>` (run both after a sync).
- `extract.py <ch> [--prune] [--browser firefox --dry-run]`: merges units into strings.json,
  keeps existing `en`, prints translated/total per section. `--dry-run` compares the key set.
- `coverage.py <ch> [--expect-clean chrome,kp1,guide:1] [--shots kp1,guide:1 --out scratch/shots]`:
  EN mode, clicks through every quiz and demo (decks: scrolls the page, then clicks every button and
  fires every control), opens every guide, and lists per section
  (`chrome`, `kpN`, `guide:N`) the `static`, `runtime`, `canvas`, `redraw` and `rewritten` findings.
  `rewritten` = a translated unit whose visible text has Chinese again after the exercise: a page
  script fills that element (often before toggle.js captures it, so extract.py can't warn), and it
  belongs in `_dynamic`, with its strings in `_runtime`.

- `navcheck.py [<ch> ...] [--browser firefox]`: per chapter, sections/quizzes found == chapters.json,
  wrong/right/wrong quiz answers record 0/1/1, prev/next section, chapter links, scroll restore after
  reload, phone-width drawer, toggle.js ignores the nav UI, no errors from nav.js.
- `python3 study/build_chapters.py [--check]`: rebuild `study/chapters.json` (warns on chapters
  without an entry in `titles_en.json` or without sections).

## Study layer (dashboard + nav.js)
A personal study aid on top of the overlay, for an English-speaking reader: all of its UI is
English. Same rules: never edit upstream files; only the injected nav.js line.

- **nav.js is independent of toggle.js.** It never calls it or reads `window.__EN__`. Its UI
  (`#study-nav` bar, `#study-drawer`) carries `data-en-skip` so toggle.js ignores it; it is a
  `<div role="navigation">`, not `<nav>`, because pages style bare `nav`. The only coupling is
  through the DOM: it watches `<html lang>` and `html.en-pending` to keep the reading spot.
- **Sections** = `section.card[data-kp]` with `id="kpN"`, in every chapter. Badge: `.badge, .card-badge`;
  title: `.card-title, .card-head h3`.
- **The page's TOC is reused, never rebuilt.** Links `a[href="#kpN"]` outside the cards get
  `.study-active` (scroll-spy) and `.study-done` (CSS ✓ via `::after`, so no text changes and no
  key changes). Classes only: TOC links are toggle.js units whose innerHTML is swapped. The §
  button points at the page's TOC when it is a pinned sidebar on screen (sticky/fixed, narrower than
  half the viewport); otherwise (phones, and Ch10/14/19 whose TOC is only "KP 1 … KP n") it opens
  a drawer whose titles are copied from the live headings each time (so they follow the language).
- **Quiz families** (container selector `.quiz, .quiz-container, .quiz-sec`, same list in
  `build_chapters.py`; quiz id = `kpN.<index among top-level containers in that section>`):

  | Family | Chapters | Markup | Solved when |
  |---|---|---|---|
  | A | 01–05 07 11 13 15 18 22 | `.quiz[data-ans]` radios + `.check` | `.fb.ok` |
  | B | 06 09 12 16 17 20 21 | `.quiz` radios `[data-correct]` + `.quiz-check` | `.quiz-feedback.ok` |
  | C | 08 | `.quiz-container[data-answer]` `.quiz-option-btn` | `.quiz-feedback.correct` |
  | D | 10 14 19 | `.quiz-sec` `.quiz-option-btn[data-correct]` | clicked button `.correct` |

  A document click listener reads the page's result classes after its handler ran. Record only:
  answers are never restored into the page. Solved stays solved.
- **localStorage** (all try/catch, per browser): `ccc-lns-study:quiz:<ChID>` = `{q: {"kp3.1": 1|0}, t}`,
  `ccc-lns-study:pos:<ChID>` = `{kp, f, t}` (section + fraction through it, because KaTeX and the
  EN switch change heights), `ccc-lns-study:last` = `{ch, kp, badge, t}`, `ccc-lns-study:theme`.
  The dashboard's "Lectures: English | 中文" control writes toggle.js's `ccc-lns-lang` (unset = English,
  same as toggle.js).
- **Scroll restore:** skipped when the URL has `#kpN`, except on reload. Re-applied at load and
  while KaTeX/EN settle (up to 2.5 s) until the reader scrolls, clicks or types; re-anchored on
  every language switch.
- **Phones:** some pages are wider than the screen (demo canvases), so the layout viewport is
  wider than the visual one; nav.js translates its bar into the `visualViewport`.
- **Dashboard** reads only `chapters.json` and localStorage. EN status = translated/units from
  strings.json and whether toggle.js is injected. New upstream chapters appear after
  `build_chapters.py` + `inject.py --all --nav` (both in `/sync-upstream`).

## Translation style
- Translate every sentence faithfully. Never summarize, skip, or merge sentences.
- The page writes terms as `損失函數 (Loss Function)`. In English, write just "loss function";
  do not produce "loss function (Loss Function)".
- Use standard English deep-learning terminology (as in Goodfellow et al. or the source textbook,
  Ghojogh & Ghodsi, *Elements of Deep Learning*). Reuse the terms in `en/glossary.json`;
  add new ones there when you first translate them.
- Keep the professor's tone (casual analogies stay casual). Translate the 教授祕笈 boxes too.
- Quiz option letters (A–D) and the correct answer must not change.
- If the Chinese contains a technical error or is unclear, translate it faithfully and add an
  entry to `en/IDL_115/<chapter>/notes.md` instead of silently "fixing" it.
- Skip the "AI 生圖可用" image-prompt blocks (leave them in Chinese).

## Known upstream problems (do not try to fix)
- Ch05, Ch11, Ch15 reference `demos/demo_kpN.js` files that were never published
  (34 scripts total), so those demos do not run on the official site either. Translate their
  static text only. Do not recreate the demo code unless the user asks.
- At phone width Ch21's sticky TOC (720 px tall) covers the content, and several pages
  (e.g. Ch06) are wider than the screen, which also pushes the 中/EN pill off-screen.

## Running and checking
- Serve locally: `python3 study/serve.py` (port 8000; `--lan` to reach it from a phone) or plain
  `python3 -m http.server 8000`; `/` lands on the dashboard either way (serve.py redirects, and the
  injected `study/home.js` does it on any host). The professor's front page: `/index.html?upstream`.
  (`file://` blocks fetching strings.json and chapters.json.)
- Tooling uses a venv at `.venv/` with `playwright` and `matplotlib`
  (`python3 -m venv .venv && .venv/bin/pip install playwright matplotlib && .venv/bin/playwright install chromium`).
- Playwright needs `chromium` (and `firefox` for the cross-browser key check).
- A chapter is done only when `.venv/bin/python en/tools/coverage.py IDL_115/<chapter>`
  reports 0 untranslated blocks in EN mode and you have screenshotted a few sections in both
  modes and looked at them.

## Git
- One commit per chapter (or per tool change). Message style: `en(Ch05): translate KP1-KP16`,
  `en(tools): ...`, `en(charts/Ch08): redraw diagram-kp3`, `study: ...`, `en(nav): ...`.
- Never commit `.venv/`, screenshots, or other scratch output (keep them in `.gitignore`).
- Push to `origin` only.
