---
name: translate-chapter
description: Translate one IDL_115 chapter into the English overlay (strings.json, runtime demo strings, chart redraws), verify it, and commit. Use when asked to translate or add English to a chapter.
argument-hint: "[chapter folder, e.g. Ch05-regularization-overfitting]"
disable-model-invocation: true
---

Translate chapter `$ARGUMENTS` into the English overlay. Follow CLAUDE.md for all design and
style rules. If `$ARGUMENTS` is empty, ask which chapter (list `IDL_115/`).

## 1. Prepare
1. Confirm `IDL_115/$ARGUMENTS/index.html` exists and the working tree is clean (`git status`).
2. Run `.venv/bin/python en/tools/extract.py IDL_115/$ARGUMENTS`. This creates or updates
   `en/IDL_115/$ARGUMENTS/strings.json`, keeping existing translations whose key still matches
   and listing new or changed units with an empty `"en"`.
3. Report: number of units, how many already translated, how many sections (KPs), and which
   `assets/*.png` files contain Chinese text (open each PNG to check; the hashed `*.jpg`
   textbook crops are already English).

## 2. Translate (fan out by section)
1. Split the untranslated units by `kp`. Give each subagent 2–4 sections so each batch stays
   small enough to translate carefully.
2. Each subagent gets: the units for its sections (key + zh), the full text of CLAUDE.md's
   "Translation style" section, and the current `en/glossary.json`. It writes its result to
   `en/IDL_115/$ARGUMENTS/.parts/kp<N>.json` as `{ key: en }` and returns any new glossary
   terms. Subagents must not edit strings.json directly.
3. Merge all parts into strings.json, merge new glossary terms (resolve conflicts toward the
   term already in the glossary), then delete `.parts/`.
4. Check every translation keeps its source's math exactly: the multiset of `$...$` / `$$...$$`
   segments in `en` must equal that in `zh`. Fix any mismatch.

## 3. Runtime (demo) strings
1. Read the chapter's inline `<script>` blocks and find string literals with Chinese that get
   written into the page (`textContent`, `innerHTML`, template literals, `alert`).
2. Add them to the `runtime` table in strings.json: exact strings, or regex patterns with
   capture groups for concatenations like `'已完成 '+done+' / '+n`.
3. Skip demos whose script files are missing upstream (see CLAUDE.md "Known upstream problems").

## 4. Charts
For each PNG with Chinese text, run the `/redraw-chart` workflow. If there are more than 4,
do them in subagents, one chart each.

## 5. Wire up and verify
1. `.venv/bin/python en/tools/inject.py IDL_115/$ARGUMENTS`.
2. Start `python3 -m http.server 8000` in the background.
3. `.venv/bin/python en/tools/coverage.py IDL_115/$ARGUMENTS` must report 0 untranslated
   blocks and 0 untranslated runtime strings after clicking through each demo and quiz.
4. Screenshot three sections (first, middle, last) in both modes and look at them: math
   renders, no layout breaks, images swapped, toggle visible in dark mode.
5. Stop the server.

## 6. Finish
1. Write `en/IDL_115/$ARGUMENTS/notes.md` with anything doubtful: errors you noticed in the
   Chinese, terms you were unsure of, charts you could not reproduce exactly.
2. `python3 study/build_chapters.py` so the dashboard shows the chapter's English status and
   English section titles.
3. Commit: `en($ARGUMENTS): translate KP1-KPn`, including `study/chapters.json` (one commit;
   charts may be a second commit).
4. Do not push unless the user asks. Report the counts, the notes, and the local URL.
