# Ch01 translation notes

Issues in the Chinese source, translated faithfully and recorded here instead of fixed.

## KP1
- **SVG title overlaps the "No Free Lunch" box** (upstream layout): the title
  `假設 → 評分 → 搜尋 → 泛化 的學習循環` is already clipped in Chinese; the English
  "The learning loop: hypothesize → score → search → generalize" is clipped a bit more.
- **教授祕笈 1, "highest" vs. argmin**: the restaurant analogy says to "pick the dish with the
  *highest* score" (挑出分數最高的那道), and the house-hunting example picks "the highest total
  score (`$\arg\min$`)". Everywhere else (and Eq. (1)) the score is a loss, so lower is better
  and argmin picks the *lowest*. Translated as written.

## KP2
- **SVG "p = 參數個數" (p = number of parameters)**: in the figure, `p` is labeled as the
  number of model parameters, but the text, Eq. (2), the quiz and 教授祕笈 2 all use `p` as the
  **output dimension** (`f_θ: R^d → R^p`). Translated as written.
- **Demo "projection onto w"**: the instructions say the output equals "the point's projection
  onto the direction of w + shift b". Strictly, `w·x` is the projection scaled by `‖w‖`.
- **行 / 列**: the page uses Taiwan convention (列 = row, 行 = column), so 「按『行』排成矩陣」
  is "stacked column-wise". This matches the textbook (`X ∈ R^{d×n}`, one column per point).

## KP3
- **教授祕笈 3, heading "3 apples"** (3 顆蘋果): the table below it includes a cucumber row
  (green, long → ℓ₂). Translated literally as "3 Apples".
- **教授祕笈 3, rain probability as regression**: "tomorrow's chance of rain" is called regression
  because a probability is continuous in [0,1]; usually this is classification with a probabilistic
  output (cf. the same guide's KP-6 link). Also, the size-threshold example ("size > 5") uses
  numeric sizes while the table above uses qualitative ones (large, long, medium).
- **教授祕笈 3, p = m for classification**: true only for score/one-hot outputs; Eq. (3) maps to a
  single label.
- **坪數 / 萬**: rendered as "floor area (in ping)" and "ten-thousands of NT dollars".

## KP4
- **Demo "What to observe"**: with m=2 the left cluster has 9 points; for m=3 it says it splits into a
  1-point and a 6-point cluster (7 points). The counts don't add up.

## KP5–KP6
- **教授祕笈 6 worked table is numerically wrong**: N(0.8, 0.1²) at x=0.7 has density ≈2.42, not
  ≈0.24; N(0.2, 0.1²) at x=0.7 is ≈1.5e-5, not ≈0.0001. The posteriors should be ≈0.99999 / 6e-6,
  not 0.9996 / 0.0004 (the table looks like the pdf divided by 10). The conclusion (apple) holds.
  The numbers are math-only cells and are unchanged.
- **KP6 demo bug (upstream)**: the readout prints `P(C₂)=NaN` (in both languages) because it reads
  `p.p2`, which `readParams()` never sets. Not fixed (demo JS is off-limits).
- **KP6 demo canvas** only redraws on 計算, so its legend (`C₁ 密度`) stays Chinese after switching
  to EN until the button is pressed (known coverage `redraw` finding).
- **SVM history**: "Vapnik proposed the SVM in 1974" simplifies (V&C 1974; optimal hyperplane
  1963–64; kernel SVM 1992; soft margin 1995). "Best generalization" overstates; hard-margin SVM is
  *feasible* only for separable data rather than "converges only when".
- **LDA/QDA boundary wording** varies: 二次曲線 (quadratic curve) vs 二次曲面 (quadric surface); LDA
  "straight line" is a hyperplane in general. Each translated literally.

## KP7
- **"Row space of the coefficients"** (係數的列空間): linear regression projects the labels onto the
  column space of the data matrix; both the word and the object look wrong.
- **Factor analysis "via variational inference (EM)"**, dated "1950s" (origins: Spearman 1904).
- **Sammon mapping (1969) as "the first nonlinear DR method"**: textbook claim, debatable.
- **Johnson–Lindenstrauss "explains why random initialization of neural networks is reasonable"**:
  a loose analogy, not a consequence of the lemma.
- **教授祕笈 7** says "the whole chapter" is variations on feature selection/DR → prediction; probably
  means this section.

## KP8
- **McCulloch–Pitts neuron** described with equal fixed weights yet able to do NOT; NOT needs an
  inhibitory input. 教授祕笈 8 then says "change the weights and threshold" (only the threshold
  changes in its example).
- **教授祕笈 8** sets up "stack layers → unbeatable?" but the twist is about a single layer failing XOR.

## KP9–KP10
- **2006 DBN** attributed to Hinton & Salakhutdinov; the DBN paper is Hinton, Osindero & Teh (2006).
  Hinton & Salakhutdinov (Science 2006) is the deep-autoencoder pretraining paper.
- **LeNet-5 / MNIST** read as late-1980s; LeNet is 1989, LeNet-5 and MNIST are 1998.
- **Bahdanau/Luong attention "solved" RNN non-parallelizability**: that came with the Transformer.
- **教授祕笈 10** lists BERT/GPT with the 2017 Transformer; KP9 correctly gives 2018. Its self-check
  says to pick the lowest score for likelihood (true only as negative log-likelihood).
- **Diffusion models dated 2020** (DDPM); first was Sohl-Dickstein et al. 2015.
- **教授祕笈 9 "≈355×" parameter comparison**: arithmetic is right, comparison is loose.
- **Fullwidth punctuation left in EN**: blocks with no Han characters (e.g. `Perceptron（Rosenblatt）`,
  `Transformer、BERT、GPT`, `Deep Belief Networks（DBN）`) are not units, so they keep `（）`/`、`.
