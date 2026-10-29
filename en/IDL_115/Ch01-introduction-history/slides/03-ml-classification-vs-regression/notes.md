# Notes: Ch01 slide 03 (03-ml-classification-vs-regression.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- Runtime: the quiz explanation written by the page's script has `$\ell_2$` in the source, but JavaScript reads `\e` as `e`, so the page shows `$ell_2$` (broken math) in both languages. The English keeps the same text.

## Where our English departs from the professor's English, and other choices

- kp0: nav labels expanded: 'Reg View' → 'Regression View', 'Cls View' → 'Classification View', 'Shared s(x)' → 'Same Model s(x)' (同一模型), 'Quiz' → 'Thinking Questions' (思考題), 'Compare' → 'Comparison Summary'.
- kp2 0767fb80b8c8: the <small> repeated the title in English; the repeat was removed and the bilingual-en sentence with no Chinese counterpart kept ('That one choice decides classification vs. regression.').
- kp2-kp4: the professor's English is a heavily shortened paraphrase of the Chinese (e.g. 'Freshmen need seniors; models need labeled teachers.', 'Show 5+5 labeled bowls; model learns features → rule.'); translated the full Chinese.
- kp3 1d929ed629bb: 人情世故 rendered 'Real-Life Story' rather than the professor's 'Human Story'.
- kp4 655c52c13278: $k$ appeared only in the English half ('one of $k$ discrete boxes'); kept.
- kp4 4fc0717609bd: \text{資工, 電機} → \text{CS, EE}. The professor's English example left out the second set, {CS, EE}; restored.
- kp5-kp9: the professor's English is a terse summary in many units (e.g. 'Study hrs, absences, gaming hrs.', 'Loss differs too', 'Score is answer; continuous.'); translated in full from the Chinese. e9d2c3f96667 now names 0-1 / cross-entropy loss vs. MSE.
- kp6 3fa662bccecc: the professor's 'Grids vs Line' is vague. Translated 格子派 vs 數線派 as 'Team Boxes vs. Team Number Line', also in d180c6d8642a and dfc37897afe4.
- kp6 e30786b23245: the professor's 'Ramen shop vs appraisal' shortens the Chinese. Translated in full.
- kp8 91652cf738c3: the professor's English 'Shared s(x)' was plain text, not math; the translation keeps the Chinese half's $s(\mathbf{x})=x_1+x_2$.
- kp10 d865950add16: the professor's 'Hard Threshold' doesn't match the Chinese 硬分黑白 (a hard black-or-white split); translated from the Chinese.
- kp10 e6d275eb644a: the dropped English half had an extra $\ge0$; en keeps the Chinese half's math and states the slope $-1$ that the short English left out.
- kp11 0aab6d7abd04: the professor's 'Geometric View — Side by Side' is looser than 分類與回歸的幾何視角; used 'The Geometric View of Classification and Regression'.
- kp12 165d30936b49: 150.2 元 rendered as '150.2 dollars' (not NT$, which would read as math).
- kp14 7659b690b048: the joke 回歸，因為有湯 kept literally ('because there's soup'); the professor's '(regression due to soup)' is unidiomatic.
- kp15 946e6992b376: kept the English-only tagline, 'Grids' changed to 'Boxes' to match 格子 = boxes elsewhere in the deck.
- kp16 283f86433538: the professor's '(ice-crystal light, full-width)' says 'full-width', which isn't in the Chinese; dropped.

## Images

- Inline charts with Chinese labels get English redraws in a separate commit.
