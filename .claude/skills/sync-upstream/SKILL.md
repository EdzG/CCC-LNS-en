---
name: sync-upstream
description: Pull the professor's latest changes from upstream and report which translated chapters now have new or changed text that needs translating. Use when asked to update, sync, or pull the professor's changes.
disable-model-invocation: true
---

1. Check the working tree is clean. If not, stop and show `git status`.
2. `git fetch upstream`, then show `git log --oneline main..upstream/main` and the list of
   changed files under `IDL_115/` (`git diff --stat main upstream/main -- IDL_115`).
3. `git merge upstream/main`. If there is a conflict, stop and explain it; do not resolve it
   by discarding either side without asking.
4. For every chapter that has `en/IDL_115/<chapter>/strings.json`:
   - re-run `.venv/bin/python en/tools/inject.py IDL_115/<chapter>` (in case the professor's
     new version of index.html dropped the script line),
   - re-run `.venv/bin/python en/tools/extract.py IDL_115/<chapter>`,
   - count new, changed, and orphaned units (orphaned = keys whose source no longer exists;
     keep them in an `orphaned` section rather than deleting, in case the text comes back).
5. Check for new chapters, new slides, and new or changed `assets/*.png` in translated chapters
   (a changed chart needs a new redraw).
6. Study layer:
   - `.venv/bin/python en/tools/inject.py --all --nav` (new chapters, decks and slides get
     nav.js; pages the professor replaced get it back) and `.venv/bin/python en/tools/inject.py --home`
     (his root index.html must keep redirecting to the dashboard),
   - `python3 study/build_chapters.py`. For each warning about a missing English title, add the
     chapter to `study/titles_en.json` (a short English title from the page's heading) and re-run.
     A "no section.card[data-kp]" warning means the new page has a different structure: report it.
   - `.venv/bin/python en/tools/navcheck.py <new or changed chapters>`. If a chapter fails (new
     quiz markup, say), report it and see CLAUDE.md "Study layer"; do not edit the page.
7. Commit the merge plus any tool output, including `study/chapters.json`
   (`en(sync): merge upstream <short hash>`).
8. Report a table: chapter | new units | changed | orphaned | charts to redraw, then a line per
   new chapter (sections, quizzes, slides, navcheck result) and any section/quiz count changes
   shown by `git diff study/chapters.json`. Suggest
   `/translate-chapter <chapter>` for any chapter with work to do. Do not translate in this
   skill. Do not push unless the user asks.
