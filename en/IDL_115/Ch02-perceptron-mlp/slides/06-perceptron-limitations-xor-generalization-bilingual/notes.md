# Notes: Ch02 deck (06-perceptron-limitations-xor-generalization-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp0 801d1f6a7c04: footer's duplicate English line (span) dropped; the single English line translates the Chinese line.
- kp1 70dfc424dcf5: professor's English ('XOR breaks linearity; unstable boundaries hurt generalization') says something different from the Chinese ('XOR can't be split, and the boundary may be learned crooked'); followed the Chinese.
- kp2 9c6beffd7028: professor's English says the embryo 'freeze on a straight line'; the Chinese means it was frozen BY a straight line (the 1969 linear-separability result). Followed the Chinese.
- kp3 2f44b3599ef3: professor's English 'multi-layer lacked algorithm' drops 'efficient' and 'until Backprop'; translated the full Chinese.
- kp3 0464b17fcdfd / kp4 / kp5 / kp6: many professor English lines are terse summaries ('Co-fire → strengthen', 'Reward co-firing on error'); all translated from the fuller Chinese.
- kp3 b0a748aae861, b54cbcf37ed2: the English taglines 'First Brick' / 'Fire Together, Wire Together' have no Chinese counterpart in the unit, so they were kept in their styled span.
- kp6 0d93f73f60d5, c7d63a6fa7be: 有偏見 is a pun (opinionated / having biases); rendered as 'biased' / 'having biases', which also echoes the bias term.
- kp6 a825609728e5: uses b ← b − η(y−ŷ), i.e. b is a threshold (score compared against b), not an additive bias; consistent with the worked example (b: 0.5→0.4). Kept as is.
- kp8 8e1e2b98ad4b / kp9 1937e12293f5: figure captions say 'matplotlib 精準' (production note); translated literally as 'matplotlib, precise'.
- kp9 3290e1688e29: section numbers jump from 3 (Perceptron) to 5 (ADALINE); the Winter section has no number 4 in the source. Kept the source numbering.
- kp9 7cfd6b3108bc: professor's English 'ADALINE chases LMS' is loose (LMS is the rule; it minimizes MSE); followed the Chinese.
- kp9 0e818d74a73c: Chinese mixes 'Many ADALINEs' into the sentence; MR III = Madaline Rule III. Professor's English omits the 'no systematic theory until Backprop' clause; translated in full.
- kp9 55ced8805a57: 處女座學習 (Virgo = perfectionist joke) rendered as 'Perfectionist Learning'.

## Images

- The 3 inline image(s) are English-only and shown as they are.
