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
