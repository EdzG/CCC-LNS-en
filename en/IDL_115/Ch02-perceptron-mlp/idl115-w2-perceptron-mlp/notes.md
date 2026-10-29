# Notes: Ch02 deck (idl115-w2-perceptron-mlp)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp0 fed869e3c421: the Chinese and English halves of the title were duplicates, so I kept one English version.
- kp1 ab2a9f1b68b0: the update example uses b ← -0.4 - 0.1 = -0.5, but the only bias given on the preceding slides is b = -0.9 (Example A), and Example A needed no update. The misclassified example (y - ŷ = -1, x = (1,0), b = -0.4) never appears in this KP. Translated as written.
- kp1 903b2a096add: the professor's English ('the error pushes the score down') does not match the Chinese, which only states η = 0.1, y - ŷ = -1 and the resulting Δw_i, Δb. Translated from the Chinese.
- kp1 15227d366573: the Chinese 非線性可分 literally means 'nonlinearly separable'. Here it means 'not linearly separable', so it is translated that way.
- kp1 7ed10ed66431 / 604e703bba13: page JS caches #kp01_boundaryStatus, #kp01_boundaryStatusEn and #kp01_boundaryEquation and writes their textContent ('目前 N / 4 筆預測正確'). Swapping innerHTML would detach those cached nodes, so these blocks should probably go in _dynamic, with a _runtime pattern '^目前 (\d+) / 4 筆預測正確$' → 'Currently $1 / 4 predictions correct'. I kept the professor's English #kp01_boundaryStatusEn span because it has an id the JS writes to. It overlaps a little with the translated status line.
- kp1 604e703bba13: the batch zh holds the JS-written equation '0.6x₁ + 0.8x₂ -0.9 = 0', but the raw HTML has '$0.6x_1+0.8x_2-0.9=0$'. I kept the batch zh text exactly.
- kp1 most bilingual-en lines: the professor's English is a loose one-line paraphrase (e.g. 'Weights encode importance.', 'Old but Complete'). I translated the full Chinese instead and dropped the English span, following the Ch01 convention. Titles are plain English with no <span class="en">.
- kp1 1c4f4d0a374d: 'Biological signal → weighted sum → activation' is the professor's English and the Chinese half says 'biological signals are abstracted into computation'. I merged both into one English line.
- kp2 5d043a4d10c2: Timeline label says 「1950 年代前後」(around the 1950s) for the emergence of the mathematical neuron that seeds the M-P model; the M-P model is from 1943 (kp3 and the kp4 note say so). Translated faithfully as 'Around the 1950s'.
- kp2 51224c5f873d: Chinese inside \text{...} translated (accumulated signal / compare with threshold / fire or stay silent); the math segment therefore differs from zh by those arguments only.
- kp2 14baba4cf87a: card icon is the Chinese character 枝 (branch); replaced with the branch-like glyph ⑂.
- kp2 d3f1dd0e3e3f / 7c502774f3c2 / 46bfa8d0b7ee etc.: dropped the duplicated professor English in chips and labels, kept one English version.
- kp2-kp4 general: the professor's bilingual-en lines are heavy condensations, not translations (e.g. kp2 311004d1807e 'loosely inspired by biology' vs Chinese 'extracted from biological mechanisms'; kp2 75db1d25c357 omits 'which part of the causal chain the artificial version keeps'; kp3 c2a8263a1098 'Before the Ferrari, learn the wheel'); translated in full from the Chinese.
- kp3 de0388bc678d: professor's English adds 'no learning', not in this sentence of the Chinese; followed the Chinese.
- kp4 2b0c91a261d6: professor's English 'Stack deep, carve complex worlds' differs from the Chinese (add the right nonlinearity to distinguish complex real-world data structures); followed the Chinese.
- kp4 62895d1115d8: the Chinese's own note flags upstream slips (M-P dated 1958 vs 1943; AND threshold 2 vs plot threshold 1.5); translated as is.
- kp4 25a61f3b3f6d: $a_i$ appears twice in zh (once in the professor's English half); kept once.
- kp4 7d441b4330ee: $\sigma$ and a second $z_i$ appear only in the professor's English half; kept $\sigma(\cdot)$ and $z_i$ once each.
- kp5 general: most of the professor's bilingual-en lines are short summaries rather than translations; I translated the full Chinese instead.
- kp5 a62f469f8f15: dropped the duplicated English accent2 subtitle and kept a single 'Signum · Updates · Geometry' line.
- kp5 a2df9af97b92: the <small> English repeated the formula $+1$/$-1$; I kept each formula once, as in the Chinese half.
- kp5 7e891d3cedd6: the professor's English 'The error gap is less symmetric' says something different from the Chinese ('the error difference does not settle at one fixed magnitude'); I followed the Chinese.
- kp5 2017217f3942: the Chinese '分班格子' (class-sorting boxes) became 'sorting into class boxes'; his English 'A crisp two-bin decision' left out the analogy.
- kp5 d16e1ad0d1fa/1bb9c2deb4a2/36a08d5acd56/2cde485fad92: I read '$a$ 猜 $b$' as true label a, predicted b (this matches the formulas in the next lines) and wrote it as '$a$ guessed as $b$'.
- kp5 1441b47b9d57: the title's English span ('Decision Boundary and Normal Vector') does not match the Chinese question ('Is the Perceptron a Geometric Sculptor?'); I kept both, joined as 'Is the Perceptron a Geometric Sculptor? Decision Boundary and Normal Vector'.
- kp5 f4dff9e806fa: the professor's English 'Name the loss correctly' is wrong, since y_i-o_i is an error, not a loss; I used 'Name the Term Correctly', following 名詞辨識.
- kp5 dd8a46a369df: his English says 'Class A/B', while the Chinese says '資料點 A/B' (data point A/B); I followed the Chinese.
- kp5 ad3fd9e4d43e: his English asks for the 'error magnitude', but the Chinese asks what y_i-o_i is (a signed value, ±2); I followed the Chinese.
- kp6 013019224e7f: '線性終數' looks like a typo (perhaps 線性終局/線性極限); translated as 'linear limit' per glossary.
- kp6 e9995141998a: '差正確時' is garbled (probably 答不正確時 'when the answer is wrong'); translated with that reading.
- kp6 3502d9fbb3e9, 9d222dbeae73, f404dd36d891 etc.: professor's English was telegraphic ('Corners diagonal same class — no line', '1969 proof killed hype'); replaced with full translations of the Chinese.
- kp6 9c6beffd7028: professor's English 'freeze on a straight line' misreads the Chinese (frozen BY a straight line); followed the Chinese.
- kp6 0b56a62b1b4e: '有偏見' (literally 'prejudiced') rendered as 'has a bias' (bias term); professor's 'tunable biased' was unclear.
- kp6 sec-tag units (S2 · 中文 · ENGLISH): kept the professor's uppercase English tag after the translated Chinese name, since they say different things (e.g. 'S2 · Stick and Candy · LEARNING IDEA'). Trailing ' · English' duplicates in captions/labels were dropped.
- kp6 e9995141998a/078e4af4b908: book titles put in quotes (no <i> added, to avoid new tags).
- kp7 516b0a1d369c: '錯 1 次或沒錯' is odd (meaning the error is either 1 or 0); translated as 'Either Wrong (1) or Not Wrong'. Professor's 'Hard and brittle' does not match.
- kp7 1171a4e9a1b2: '經典訓練物件' likely means 訓練對象/目標 (training target); translated as 'training target'.
- kp7 5b21ea587b07: claim that LMS is the prototype of 'every modern gradient-descent optimizer' is an overstatement; translated faithfully.
- kp7 numbers checked: sigma(1)=0.731, sigma'(1)=0.1966, (0.731-1)*8=-2.152, 0.5+0.1*2.152=0.715 are all correct.
- kp8/kp9 general: the bilingual-en / small / span.en English halves are terse summaries, not translations; each en is a full translation of the Chinese with that span dropped (titles carry the English as the title text itself).
- kp8 22575d75b491, f42afb53a9f8: Chinese inside \text{} translated: $w_{\text{等效}}$ -> $w_{\text{equiv}}$.
- kp8 902cab84c7cd: 引數 (Taiwan usage: function argument) is used where 參數 (parameters) is meant; translated as 'Fewer parameters', following the professor's English and the intent.
- kp8 88a3641fc1d8: professor's English 'With sigma' rendered as 'With nonlinearity' (Chinese 含非線性).
- kp9 3c29905ef6b4: 'step and sign functions are practically non-differentiable' kept faithfully; strictly, their derivative is 0 almost everywhere and undefined at 0, which is what makes them useless for gradient training.
- kp9 6021197161f4: Maxout labeled 跨層特殊款 'special cross-layer type' faithfully; Maxout is not really cross-layer (it takes a max over several linear pieces within one layer).
- kp9 6e95bfb27be8: professor's English 'It never vanishes' is ambiguous; Chinese means 'it never has vanishing gradients'.
- kp9 e0c3db6f67f6: 'BIG QUESTION · 大問句' rendered as just 'BIG QUESTION' (Chinese half is the same phrase).
- kp10 196a9b2f430b: Chinese inside \text{...} translated, so that $$...$$ segment differs from zh by design.
- kp10 314b627d3ec7: professor's English 'Target' for 標籤; translated as 'Label' to follow the Chinese.
- kp10 256d8d1e50f4: professor's English 'Classification' drops 多類別／二元 (multiclass/binary); translated in full.
- kp10 e71997f488fd: professor's English 'Needs probability outputs' omits softmax/sigmoid; translated from the Chinese.
- kp10 1c9ae82a8f93 / 314b627d3ec7: the checklist uses 'label format' (標籤格式) where the professor's English says 'target format'.
- kp10 e0b35a931b6b, kp12 7977dee116a9: English span/small dropped; English written as the title text itself.
- kp12 533e5fd4c5ce, 041a9348f82e: the page itself notes errors in the source handout (garbled chain-rule notation, sigmoid saturation mislabeled as ReLU); translated faithfully.
- kp13 d62af4e2cbac / ae7a3241e1c9: the worked example shows ŷ = 1.212 (2 × 0.606), while the demo readout shows 1.213 (2 × 0.6065); kept both values as in the source.
- kp13 aa30fc1dea60 vs 2468977e65a6: e^{-0.5} is given as ≈0.606 in one place and ≈0.607 in another (true value 0.6065); kept as in the source.
- kp13 dfd890b2b64c, e62c747748f1, 7f18a71a5286 and most bilingual-en spans: the professor's English is a loose paraphrase (e.g. 'fixed local responses first'); translated from the Chinese instead.
- kp13 a0a82968d01d / c0aecbdfe6a5: professor's English 'Two clever shortcuts' / 'Retrieval practice' drops the 「偷懶」 (lazy) motif the Chinese uses throughout; kept 'lazy'.
- kp13 bc0048961420: professor's English writes plain z and h; Chinese text kept with math $z$, $h_{zj}(t)$, $j$; expanded BMU as best matching unit.
- kp13 169d48a2a6ce: quote's small English line dropped; translated the Chinese question as the main text without the <small> wrapper.
- kp14 c5e535949112: professor's English says 'learned basis', the Chinese only says neurons provide a basis like Fourier trigonometric functions; followed the Chinese.
- kp14 0e5530e91f12: this hint (about error sign and z = w1x1+w2x2+b) does not obviously match the Q1 it follows (AND vs XOR); translated faithfully.
- kp14 4d9ab6fa67a0: the 'Next: backpropagation, gradient descent, and deeper architectures.' line has no Chinese counterpart, so it is kept in its bilingual-en span.

## Runtime

- Runtime: the submit button's script writes the mojibake 'å·²æäº¤' (a broken encoding of 已提交, "submitted"); it has no Chinese characters, so it shows as is in both languages.
- Runtime: #kp01_boundaryStatus / #kp01_boundaryEquation are rewritten by the slider script inside translated blocks; the engine keeps those live elements across the swap and translates their text at runtime.

## Images

- The "AND vs XOR geometry" chart (key f1c39c8261ce) is redrawn in English (`assets/img-f1c39c8261ce.png`, script `en/tools/charts/Ch02-perceptron-mlp/img-f1c39c8261ce.py`). 「XOR：對角線交錯的斷層」 is rendered "XOR: classes interleaved along the diagonals".
- The other 14 inline image(s) are English-only and shown as they are.
