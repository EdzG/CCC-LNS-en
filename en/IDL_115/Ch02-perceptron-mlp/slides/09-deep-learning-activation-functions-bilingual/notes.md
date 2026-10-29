# Notes: Ch02 deck (09-deep-learning-activation-functions-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1 6908f098ff62: cover title 激活函數調色盤 = 'The Activation Function Palette'; professor's English line 'Activation Functions' dropped.
- kp1 e3270b242e96: professor's English 'depth is only a wider linear model' renders 變胖 as 'wider'; translated from the Chinese as 'a fatter linear model'.
- kp3/kp4/kp5/kp6/kp7: the professor's bilingual-en spans are short paraphrases, not translations (e.g. 'Stacked linear layers still collapse into one linear map' drops the transparent-sheets analogy); replaced with full translations of the Chinese.
- kp5 19cf8d0f7ee3: Chinese puts ELU and Softplus in the 'ReLU family' and later calls the repair variants Leaky ReLU/PReLU/ELU; kept as written.
- kp5 3c29905ef6b4: 'step and sign functions are almost non-differentiable' is loose: they are differentiable almost everywhere with zero derivative (non-differentiable only at 0); the practical issue is the zero gradient. Translated faithfully.
- kp7 c1635c87d2a5 section: the chain-rule step body is English-only ('The gradient remains strong.') and has no unit; left as is.
- kp8 f59bf30146e0: professor's English 'can permanently block updates' adds 'permanently', which the Chinese does not say; followed the Chinese.
- kp9 c1bf9f758f0b: professor's English 'normalizes all class scores together' is a paraphrase; translated the pie analogy fully.
- kp10 6e95bfb27be8: professor's English 'It never vanishes' is unclear; Chinese means 'it never suffers from vanishing gradients'.
- kp10 quiz: option order and data-correct unchanged (Q1 B, Q2 C, Q3 A).
- kp11 13d9520738fa: 正規化 here means normalization layers (BatchNorm/LayerNorm), not regularization; translated as 'normalization'.

## Images

- The 1 inline image(s) are English-only and shown as they are.
