# Notes: Ch01 slide 01 (01-ml-theory-surrogate-bias-loop.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section.

## Possible errors in the source

- kp9 `17df5d1bc3c4`: "an error of 5 hurts six times as much as an error of 2" (25 vs 4) is
  6.25×. Kept as a casual approximation.
- kp11 `6f574e9790cc`: No Free Lunch is stated as "no algorithm does well on every problem without
  prior assumptions"; the theorem says all algorithms have equal average performance over all
  problems. Translated as written.
- kp13 `0e337fa8640d`: 梯度下降 SGD is rendered "gradient descent (SGD)"; SGD is *stochastic* gradient descent.
- kp13 `c3357e9e3eaf`: the Chinese caption reads like a note to the professor ("your lecture
  notes' SVG redrawn…"), not to students. Translated faithfully.

## Where our English departs from the professor's English (following the Chinese)

- kp0 nav: where the professor's short English label lost meaning, fuller labels were written: 'Two Criteria for a Good Map', 'The Trilogy: Overview', 'Scoring Mechanism (Loss)', 'Search Strategy (Optimization)', 'Generalization and Overfitting', 'Questions to Ponder'.
- kp2 64af8ec5dc9e: the <small> held the professor's English for the main question plus a second question with no Chinese counterpart ('If every map is "false", what makes a map "good"?'); main question translated from the Chinese, second question kept.
- kp2 5d1b3268daf7: the professor's English ('good maps explain now and predict next') does not match the Chinese (fried chicken vs wishing fountain). Translated from the Chinese.
- kp3 566456b13e9c / e412521309f1 / 9bf393a002f7 / a6ff9e3fdb3c / 6844c37f88ba: the professor's English halves are short summaries, not translations; translated the full Chinese.
- kp4-7: the professor's English halves are much shorter summaries than the Chinese (e.g. kp5 2d04f79bd4c8 'Science = bold conjecture + severe attempts to refute', kp4 83d70c08a513 'Good map = low training error + low test error', kp6 c94fb09785e0 'Pick cuisine → judges score → crown winner'); translated the full Chinese.
- kp4 28f394cd2f04: the professor's English 'overfitting = great map, wrong world' is not what the Chinese says ('follow the map and fall into the wishing well = overfitting'). Followed the Chinese.
- kp6 e6dc6f2356a0: the Chinese title 假設空間 (hypothesis space) does not match the professor's subtitle 'Hypothesis Class'; kept 'Hypothesis space $\mathcal{F}$' with the subtitle 'Hypothesis class', matching the other two cards.
- kp6 2e2c07dfb84a: the professor's English title ('Hypothesize · Score · Search') leaves out the Chinese jokes (開菜單、請評委、抓戰犯); translated as 'write the menu, call in the judges, find the culprit'.
- kp6 c94fb09785e0: 熱炒店 translated as 'Taiwanese stir-fry joint'.
- kp7 2a72f438dc01: the display math contains Chinese (\text{所有你願意考慮的函數}); only the \text{} argument was translated ('all the functions you are willing to consider'), the rest of the formula is unchanged.
- kp7 c6315a87604f: $\mathcal{F}$ appears only in the professor's English half ('Larger $\mathcal{F}$ ≠ better'); the Chinese says 菜單 (menu), so the translation of the Chinese has no math.
- kp8 74dea38cb0a6: the professor's English subtitle ('Scoring $S(f)$ — Loss Function') leaves out the Chinese 'the harsh judge hands out scores'; translated the Chinese.
- kp8 5e0b83511f6d: the English half wrote $\hat y_i$ and the Chinese half $\hat{y}_i$; kept the Chinese half's segments.
- kp8-11: many professor bilingual-en lines are clipped summaries; each was replaced by a full translation of the Chinese.
- kp9 db6b6600d0f7: the English subtitle 'Worked Example: MSE = 15' differs from the Chinese 'the sin scores (罪孽值) of three classmates'; followed the Chinese, 'sin score' for 罪孽值 throughout.
- kp11 1a03a25622dc: the professor's 'No Bias, No Learning' does not match the Chinese 沒有智慧 ('no intelligence'); wrote 'No Bias, No Intelligence'.
- kp12 74bbff28ad7d: the professor's 'ML is not to remove bias, but to choose it' leaves out 選對 ('choose the RIGHT bias'); fixed.
- kp12 8608fe9564fd: 'paralysis: anything goes' compresses 寸步難行（2,4,6 怎麼猜都可）; translated in full.
- kp12 f13fac8633fc / 0576a62e556f: professor's '(Myth)' / '(Reality)' replaced with translations of 錯誤想像 / 正確理解 ('Misconception' / 'Correct understanding').
- kp12 5c330c35657b: professor's English drops 'bold' (大膽猜) and 'choosing' (選 F); translated from the Chinese.
- kp13 feb8a70df6ce: the professor's English mentions 'solid = forward', which the Chinese does not say; translated from the Chinese.
- kp14 0b1fb933406b / f7cfe54090f0 / d7bf56e94fd5: professor's English ('good map', 'Fits noise as if it's signal', 'new paper') is heavily condensed; translated in full from the Chinese.
- kp16 ad85347a72d2: the professor's English 'Test Your Understanding' doesn't match the Chinese 提取練習; translated it as 'Retrieval Practice'.
- kp16 option labels: dropped the professor's terse inline English glosses ('(map not pretty)' and similar) and translated the full Chinese option text. Option letters and contents are unchanged.
- kp16 5e923ddbe12f: the professor's inline English '($4+16+25)/3; ...' has a misplaced '$', which leaves an unmatched dollar sign and broken math. Kept only the Chinese half's correct $(4+16+25)/3$.
- kp16 4136e0fc9115: the professor's English 'why 2,4,6 → 8 not guaranteed?' has unmathed 2,4,6/8. Kept the Chinese half's $2,4,6$ and $8$.
- kp17 42f963268285: the <small> line 'Pick the right bias to understand the world.' just repeated the main Chinese line in English, so it was removed. Kept the English-only span 'Models aren't truth — good maps predict.'
- kp17 c2c240686e78: the English half repeats $\mathcal{F}$ and $S(f)$ and has $\hat f$ ('search $\hat f$'). Kept the Chinese half's math only ($\mathcal{F}$, $S(f)$, $\hat f = \arg\min S(f)$).

## Math

- Formulas that appear only in the professor's English half were dropped where our English
  follows the Chinese (5e0b83511f6d, a98b40c31861, c2c240686e78, c6315a87604f).
- kp7 `2a72f438dc01`: only the `\text{}` argument of the display formula was translated.

## Images

- The four inline charts (#0–#3) have Chinese labels; English redraws follow in a separate commit.
