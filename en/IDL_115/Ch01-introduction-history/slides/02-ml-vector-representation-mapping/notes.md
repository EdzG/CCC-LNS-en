# Notes: Ch01 slide 02 (02-ml-vector-representation-mapping.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp5 `1d606482143a`: 降維打擊 ("dimension-reduction strike") is used for the cat image going *up* to 10,000 dimensions; kept as the joke it is.

## Where our English departs from the professor's English, and other choices

- kp2 b9f72df1e574: the professor's 'Computer is near-sighted — how does it see the world?' leaves out 大笨蛋 ('big dummy'); replaced with a full translation of the Chinese heading.
- kp2 8af6bf31a82e: 'Violent trick' is a literal mistranslation of 暴力解法; rendered as 'brute-force approach'.
- kp3 9aa1f7b8363f, 11043c1ad5b0, kp4 6a610f6efb1b, 312f85415034: the professor's English summaries ('Doctor measures, not portraits — features.', 'Four numbers → point in 4D space.') are terse fragments; replaced with full translations of the Chinese.
- kp4 f2d20543231e: \text{小明} inside the display math translated to \text{Xiao Ming}.
- kp5 1d606482143a: 降維打擊 ('dimension-reduction strike', a Three-Body Problem meme) is a pun; the cat actually goes UP to 10,000 dimensions. Kept the joke.
- kp7 31dc955a1d1a / 7eb78045ba4a: the English half's formulas ($d=2 \to p=1$, $d=10 \to p=1$) differ from the Chinese half's, so they are kept in a short closing clause.
- kp8 64a7de54a7c8: the professor's English 'Weights & bias' does not match the Chinese 齒輪、加權比重 ('gears, weighting proportions'; bias is not mentioned). Translated from the Chinese.
- kp8 839fce476ac3: 在數據庫裡 literally 'in the database'; translated as 'on the data', which is what is meant.
- kp10-kp12: the student names 小愛/小華/小美/小明 are romanized Xiao Ai / Xiao Hua / Xiao Mei / Xiao Ming (text, table and chart labels).
- kp10 71d98f3d943a: 降維打擊 is a pun on the Three-Body 'dimension-reduction strike'; kept. The professor's 'Hand Calc: $f(x)=x_1+x_2$' leaves out the parameters and the pun.
- kp10 7835fa104f3b, 6790cb199fdd; kp11 7b97dd2f0ef5, 3788dd3b7d8b, c3813b773b1e: the professor's English lines are telegraphic summaries; replaced with full translations of the Chinese.
- kp12 a40989b8e2ff: 'Connect three protagonists into a pipeline' is unidiomatic; now 'Let's chain today's three main characters into one pipeline.'
- kp12 d6f62666e598/9aa170b5b31b: 欄 = columns (samples n), 列 = rows (features d), Taiwanese usage, consistent with $X\in\mathbb{R}^{d\times n}$.
- kp13 9b75a6ea5a48: the professor's 'Summary — Three Pillars' adds 'Three Pillars', which is not in the Chinese (今日精要總結); translated as 'Today's key takeaways'.
- kp13 f1ef13d558d1, 04aec4fd9127; kp14 aa2c86d81813, d3277eeeaacd, 77bf7ae4c063: the professor's English are fragments ('$w$ directs, $b$ shifts.'); replaced with full translations.
- kp15 ad85347a72d2: the professor's 'Reflection — Test Your Understanding' doesn't match 提取練習 (retrieval practice); translated 'Reflection · Retrieval Practice'.
- kp15 0a35dd364242 / 98b014330e53: '$n\times d$' and '$d\times n$' appear only in the professor's English half; kept through an 'i.e.' clause.
- kp15 e7ed5a90a92b: the English 'Shape of $X$? Cat dims?' is far too terse; translated the full Chinese question.
- kp16 676dbfc89835: the professor's 'Vectors are the cane' drops 'the computer's'; 拐杖 rendered 'crutch'. His extra line '$b$ shifts the baseline.' has no Chinese counterpart and is kept.
- kp16 8e77271bac41: the English recap's '$X$' and '$f_\theta$' appear only in the English half; kept as a short legend.

## Images

- Inline charts with Chinese labels get English redraws in a separate commit.
