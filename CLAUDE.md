# CCC-LNS-en: English overlay for the NDHU IDL 115 lecture pages

## What this repo is
A private copy of the professor's course site (`ndhuccc/CCC-LNS`) with a 中/EN toggle added.
The goal is a study tool: the Chinese stays the default, and one button switches the whole
page (prose, headings, quizzes, 教授祕笈 boxes, demo text, and chart images) to English.

Only `IDL_115/` (Introductory Deep Learning) is in scope. Ignore `PR_115/` unless asked.

## Remotes (never break these)
- `origin` = `git@github.com:EdzG/CCC-LNS-en.git` (private, ours). Push here only.
- `upstream` = `https://github.com/ndhuccc/CCC-LNS.git` (professor). Push is disabled. Never re-enable it.
- Get professor updates with `git fetch upstream && git merge upstream/main`.

## The overlay rule (most important)
**Never hand-edit the professor's files.** All English lives under `en/`.
The only change to an upstream file is ONE injected line in each translated chapter's
`index.html`, added by `en/tools/inject.py` (idempotent, so it can be re-run after a merge):

```html
<script src="../../en/toggle.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
```

Keeping upstream files untouched means `git merge upstream/main` stays conflict-free, and
only paragraphs the professor actually changed need re-translating.

## Layout
```
en/
├─ toggle.js                         # the 中/EN button + swapping engine (shared by all chapters)
├─ tools/
│  ├─ extract.py                     # pull translatable units from a chapter into strings.json
│  ├─ inject.py                      # add/verify the single <script> line in a chapter
│  ├─ coverage.py                    # headless check: any Chinese left visible in EN mode?
│  ├─ _common.py                     # normalize/key_of (must match toggle.js), server, Playwright
│  └─ charts/<chapter>/<name>.py     # one matplotlib script per redrawn chart
└─ IDL_115/<chapter>/
   ├─ strings.json                   # _runtime/_dynamic/_images + { key: { zh, en, kp, ctx } }
   ├─ notes.md                       # errors/ambiguities found in the Chinese source
   └─ assets/<same filename>.png     # English redraw of a chart with Chinese labels
```

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
  `#en-toggle`, and `_dynamic` selectors.
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
- **Observer hygiene:** the observer is disconnected during bulk swaps and math re-rendering,
  and `takeRecords()` discards our own writes. It ignores nodes inside `.katex` and inside static
  units, and KaTeX records (added `.katex` nodes) never count as content changes.
- **教授祕笈 guides** live in `window.__GUIDES__` and are injected by `openGuide(n)` into
  `#guide-title`/`#guide-body`. The observer sees that childList change (a microtask, before the
  page's 50 ms renderMath), captures fresh units (`ctx: "guide"`, `kp` = guide number found by
  matching the title) and swaps them if EN is on. extract.py/coverage.py open every guide.
- **Canvas:** `CanvasRenderingContext2D.prototype.fillText/strokeText` are wrapped. In EN mode
  the text goes through `_runtime`; unmatched Han text is recorded as a miss. Because demos draw
  during parse, every language switch fires `input` on each `.demo`'s range/number/select
  controls (and `change` on selects) so canvases redraw at once. coverage.py reports demos
  that draw Chinese but don't redraw this way (Ch01: KP6 only redraws on its 計算 button).
- **`_images`** (list of filenames): only `img` whose src basename is listed is swapped to
  `en/<chapter>/assets/<file>` in EN mode. No HEAD checks. Textbook figures (the hashed `*.jpg`
  crops) are already English and need no redraw.
- **Toggle UI:** fixed 中 | EN pill (top-right, z-index 1000), `Alt+L`, state in
  `localStorage['ccc-lns-lang']` (try/catch), default 中, `<html lang>` updated, light/dark tokens.
  If the saved state is EN, header/main stay hidden until strings.json arrives (1.5 s max).
- Missing translation in EN mode: the Chinese stays visible with class `en-missing` (dashed
  amber outline). Never show an empty block.
- **strings.json** reserved keys start with `_`: `_runtime`, `_dynamic`, `_images`, `_stale`
  (keys that vanished from the page; `--prune` deletes them). Every other key is a unit:
  `{zh, en, kp, ctx: page|svg|attr|expl|guide, attr?, review?}`; `kp: 0` = page chrome.
- `window.__EN__` exposes `setLang`, `collect()`, `misses`, `hanCanvases()`, `ready` for the tools.

## Tools
- `inject.py <ch> [--check]`: adds the one line before `</head>`, byte-exact otherwise
  (upstream files are CRLF; keep it that way).
- `extract.py <ch> [--prune] [--browser firefox --dry-run]`: merges units into strings.json,
  keeps existing `en`, prints translated/total per section. `--dry-run` compares the key set.
- `coverage.py <ch> [--expect-clean chrome,kp1,guide:1] [--shots kp1,guide:1 --out scratch/shots]`:
  EN mode, clicks through every quiz and demo, opens every guide, and lists per section
  (`chrome`, `kpN`, `guide:N`) the `static`, `runtime`, `canvas` and `redraw` findings.

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

## Running and checking
- Serve locally: `python3 -m http.server 8000` from the repo root, open
  `http://localhost:8000/IDL_115/<chapter>/`. (`file://` blocks fetching strings.json.)
- Tooling uses a venv at `.venv/` with `playwright` and `matplotlib`
  (`python3 -m venv .venv && .venv/bin/pip install playwright matplotlib && .venv/bin/playwright install chromium`).
- Playwright needs `chromium` (and `firefox` for the cross-browser key check).
- A chapter is done only when `.venv/bin/python en/tools/coverage.py IDL_115/<chapter>`
  reports 0 untranslated blocks in EN mode and you have screenshotted a few sections in both
  modes and looked at them.

## Git
- One commit per chapter (or per tool change). Message style: `en(Ch05): translate KP1-KP16`,
  `en(tools): ...`, `en(charts/Ch08): redraw diagram-kp3`.
- Never commit `.venv/`, screenshots, or other scratch output (keep them in `.gitignore`).
- Push to `origin` only.
