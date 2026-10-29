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
│  └─ charts/<chapter>/<name>.py     # one matplotlib script per redrawn chart
└─ IDL_115/<chapter>/
   ├─ strings.json                   # { key: { "zh": source, "en": translation, "kp": n } }
   └─ assets/<same filename>.png     # English redraw of a chart with Chinese labels
```

## How the engine works (design decisions, keep consistent)
- **Unit = block element, not text node.** Translate whole leaf blocks (`p`, `li`, `h1`–`h4`,
  `td`, `th`, `figcaption`, `label`, `button`, `summary`, quiz options/feedback, callout bodies).
  Text-node-level translation breaks sentences that KaTeX splits apart.
- **Keys are content hashes.** `key = sha1(normalize(source innerHTML))[:12]`, where normalize
  collapses whitespace. If the professor edits a paragraph, its key changes and it shows up as
  untranslated; unchanged paragraphs keep working. Never use positional keys.
- **Capture source before KaTeX renders.** The pages use KaTeX auto-render. toggle.js must
  record each block's original innerHTML (with raw `$...$` math) before rendering runs, swap
  innerHTML on toggle, then call `renderMathInElement` on the swapped block.
- **Math is never translated.** Keep every `$...$`, `$$...$$`, `\(...\)` exactly as in the source.
- **Attributes too:** `title`, `alt`, `placeholder`, `aria-label`, `data-expl` (quiz explanations).
- **Demo text is generated at runtime** (e.g. `textContent='✓ 正確！'`,
  `'已完成 '+done+' / '+n`). Handle with a per-chapter `runtime` table in strings.json
  (exact strings and regex patterns with capture groups) applied by a MutationObserver
  while EN mode is on. Do not edit demo JavaScript.
- **Images:** if `en/IDL_115/<chapter>/assets/<file>` exists, swap `src` to it in EN mode.
  Textbook figures (the hashed `*.jpg` crops) are already English and need no redraw.
- **Toggle UI:** a fixed button (中 / EN), keyboard shortcut `Alt+L`, state saved in
  `localStorage` (wrapped in try/catch). Default is Chinese. Must work in light and dark themes.
- Missing translation in EN mode: leave the Chinese visible and outline the block with a dashed
  border so gaps are easy to spot. Never show an empty block.

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
- A chapter is done only when `.venv/bin/python en/tools/coverage.py IDL_115/<chapter>`
  reports 0 untranslated blocks in EN mode and you have screenshotted a few sections in both
  modes and looked at them.

## Git
- One commit per chapter (or per tool change). Message style: `en(Ch05): translate KP1-KP16`,
  `en(tools): ...`, `en(charts/Ch08): redraw diagram-kp3`.
- Never commit `.venv/`, screenshots, or other scratch output (keep them in `.gitignore`).
- Push to `origin` only.
