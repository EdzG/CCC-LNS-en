# Notes: Ch02 deck (01-ai-foundations-perceptron-to-uat-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1 707c0eaf21e7: professor's English 'A map from biological inspiration to mathematical expressivity.' does not match the Chinese ('one big-picture map of the perceptron, XOR, MLP and UAT'); translated from the Chinese.
- kp1 a0fb99cf43e2: badge '人工智慧基礎理論 · AI FOUNDATIONS' rendered as one version, 'Foundations of Artificial Intelligence'.
- kp2 48766334fe1e: dropped the professor's <small> subtitle ('From one straight line to universal approximation.'), which only restates the Chinese heading.
- kp2 93c8380ff7aa: professor's English adds 'first build the map', which is not in this Chinese sentence; translated the Chinese only.
- kp3 11f6f673e6e8, 9668bc6b2e91: the professor's English lines are one-line summaries, not translations; translated the full Chinese.
- kp3 22d3886677f7: the path-node keeps its English sub-label 'Biological neuron'; 生物原型 rendered 'Biological prototype'.
- kp5-kp7: 引數 (Taiwan term for program arguments) is used in the sense of 參數 'parameters'; translated as 'parameters'.
- kp8-kp17: the professor's bilingual-en lines are mostly short summaries, not translations; translated the full Chinese and dropped them.
- kp10 d85bcb068f82: the AND/XOR precision plot is an inline data-URI image; it may contain labels that need checking for Chinese.
- kp11 604e703bba13, 7ed10ed66431: these static units contain the script-updated elements #boundaryEquation, #boundaryStatus and #boundaryStatusEn. Swapping the unit's innerHTML replaces those nodes, so the slider script (which holds references captured at load) will write to detached nodes in EN mode and after switching back. Kept ids/markup; kept the English-only #boundaryStatusEn span, which is a separate status line written by the script.
- kp11 7ed10ed66431: '目前 4 / 4 筆預測正確' translated as 'Currently 4 / 4 predictions correct', matching the _runtime pattern.
- kp12 7d902f00c368: SVG label '非線性特徵折疊 · Nonlinear folding' rendered once as 'Nonlinear feature folding'.
- kp12 7aeec4b45697: professor's English 'Several nonlinear boundaries can solve XOR' differs from the Chinese (lines that cross and fold); translated the Chinese.
- kp13 8480e6df9411: Chinese typo '區域性性' (duplicated 性); translated as 'locality'.
- kp14 01685222d078: dropped the professor's <small> subtitle, which restates the Chinese heading; strictly, the UAT needs a nonlinear (e.g. sigmoidal) activation and a compact domain, which this slide leaves out.
- kp16 d2c326ac7070, 1c2fd878133c: professor's English 'Correct output' / 'Incorrect sign' would give away the answer; translated the Chinese only.
- kp17 4d9ab6fa67a0: kept the English-only 'Next: ...' line (no Chinese counterpart).

## Runtime

- Runtime: #boundaryStatus / #boundaryEquation (inside translated blocks) are rewritten by the slider script; the engine keeps them live and translates "目前 N / 4 筆預測正確" at runtime.

## Images

- The "AND vs XOR geometry" chart is redrawn in English (`assets/img-f1c39c8261ce.png`, script `en/tools/charts/Ch02-perceptron-mlp/img-f1c39c8261ce.py`).
