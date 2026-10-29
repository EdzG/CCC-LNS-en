# Notes: Ch01 slide 08 (08-ml-ai-history-mp-perceptron-bilingual.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp4 `332a655b4525`: the M-P unit is said to fire when the sum *exceeds* the threshold; the classic M-P unit fires at sum ≥ threshold.
- kp9 `24b787851cbe`: MR III (Widrow et al., ~1988) came after backprop was popularized (1986), so "no systematic theory until backprop" is chronologically loose.
- kp6 `f5b46cff032e`: the 1958 Mark I perceptron demo recognized simple shapes and letters; the Chinese says digits.
- kp13 `0c8178d118ad`: simplified 几 in 几何 (should be 幾何); kp7 `a42192cb6701`: 遙認, likely a typo for 辨認.
- Runtime: quiz 1's answer 感知機可調有偏見 (literally 'is prejudiced') is read as 'has a bias term' and translated so.

## Where our English departs from the professor's English, and other choices

- kp1 b60d0615d259: professor's English ('One neuron, one motto, one embryo, one winter') drops the years and turns '一盆冷水' (a bucket of cold water) into 'one winter'; followed the Chinese.
- kp3 0464b17fcdfd / a14661cdff0f / 360be30f9331 / dff6959658e0 / bfd838b305c6 / 2bfd5c3d29b2: professor's English halves are telegraphic summaries ('Co-fire → strengthen.', 'Linear cannot do XOR; multi-layer lacked algorithm.', 'Before Ferrari, understand wheel'); translated the full Chinese.
- kp3 b0a748aae861 / b54cbcf37ed2 / 3a311ac75a78: card headings' English subtitles ('First Brick', 'Fire Together, Wire Together') differ from the Chinese titles; used the Chinese titles (M-P Model, Hebbian Learning, The Winter).
- kp4 332a655b4525: professor's English says 'fire if sum > threshold'; Chinese says 超過門檻 (exceeds), consistent; kept 'exceeds'. Classic M-P actually fires at sum >= threshold, a minor point.
- kp4 096cabf98dc3 / 76614819c6aa / bd7afaa0e771 / 736858a98dee: professor's English omits most content (McCulloch/Pitts, megaphone analogy, Hebb/Rosenblatt); translated the full Chinese.
- kp5 4667c9a5096e/3b7f4e7a1b19: SVG circle is only ~64px wide, so 前/後神經元 rendered as 'Pre-neuron'/'Post-neuron' (presynaptic/postsynaptic) to fit.
- kp6 0d93f73f60d5/c7d63a6fa7be: 偏見 is a pun (weights = preferences/opinions, not only the bias term b); kept as 'bias' to preserve the joke.
- kp6 f5b46cff032e: the 1958 Mark I perceptron demo recognized simple shapes/letters, while the Chinese says digits; translated faithfully.
- kp7 a42192cb6701: 遙認 ('recognize from afar') looks like a typo for 辨認; translated as 'recognizing'.
- kp7 fac338ede2a6: SVG label shortened to fit ('want 1, got 0 → boost x=1').
- kp7 0508a59e5435, 66a95495fa17: math repeated in the professor's English half ($x=(1,1)$, $\Delta w$, $\Delta b$, $\eta$) kept once.
- kp7 49b605e5e4ec/51ea917e9ed4: says the model now 'favors red', but the same update also raises w2 0.3→0.4 (round) equally; the Chinese stresses red only.
- kp9 d7e741982048: $\hat s$ appears only in the professor's English half; the Chinese half starts with the full $\hat s=\mathbf{w}^\top\mathbf{x}$, which is kept.
- kp9 7cfd6b3108bc: professor's English says 'chases LMS'; the Chinese says it minimizes the mean squared error between score and target, translated from the Chinese.
- kp9 24b787851cbe: historically MR III (Widrow et al., ~1988) came after backprop was popularized (1986), so 'no systematic theory until Backprop' is chronologically loose; translated faithfully.
- kp9 55ced8805a57: 處女座學習 (Virgo = perfectionist stereotype) rendered as 'Learning like a perfectionist'.
- kp10 af5c143bc540 / 3eecbd91541f, kp11 196412252011: the professor's English is a telegraphic summary ('group stuck until Backprop', 'linear caps at teaching a crowd') and leaves out parts of the Chinese; translated in full from the Chinese.
- kp10 b6999548af2e: 放電時間差 translated as 'differences in spike timing'.
- kp11 9d3369db283c / 196412252011, kp12 013019224e7f: 「線性終數」 is a nonstandard coinage (likely 'linearity as the end point/ceiling'); rendered as 'the linear limit', in line with the professor's 'Linear Limit'.
- kp11 5d611b05e770: the Chinese 'MADALINE 直到 Sigmoid 才可導' is compressed. It means MADALINE (multilayer) could not be trained by gradients until a differentiable sigmoid replaced the step function. Translated faithfully and kept short to fit the SVG.
- kp12 156f90e175b3: the professor's English option text is just 'Swapped'; translated the full Chinese statement instead.
- kp12 60b523b94890: the professor's 'always LMS' hint is dropped; followed the Chinese ('error in the total score', i.e. the error of the linear output).
- kp13 0c8178d118ad: the source has a simplified character 几 in 几何 (should be 幾何); translated as 'geometry'.

## Images

- Inline image #00: NO-CHINESE
- Inline image #01: NO-CHINESE ("Linear Separable" title should read "Linearly Separable"; left as is)
- Inline image #02: NO-CHINESE
- No redraw needed: the inline images have no Chinese text.
