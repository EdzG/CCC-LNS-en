# Notes: Ch03 deck (15-overparameterized-convergence-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (25 exact, 11 patterns). `_dynamic`: `#sim-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- Quiz explanations: the deck's getExplanation() picks the explanation by searching the card's text for Chinese keywords ('梯度長期偏大', '式 58', …). In EN mode the card text is already English, so most searches fail and only the "✅ Correct!" / "Think it over again:" prefix shows (switch to 中 to see the explanation). Explanations that do appear are translated.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp7 760ad17ba647, 8a44c75012d1: "a negative eigenvalue" is written as $\nabla^2 \mathcal{L} \prec 0$, which means negative definite (stronger).
- kp7 e9fd555db380: promises 「四大幾何轉變」 (four geometric shifts) but lists only ①–③.
- kp12 c90c9c20789d (option A): $O(1/\epsilon)$ labelled 指數 (exponential); 1/ε is polynomial (it is a wrong option anyway).
- Prop 5 is a deep fully connected ReLU network here (Allen-Zhu et al.), but deck 16 (289fee47b584, 7eb6838b14c7, svg 2699d4a3b2d7) calls it "deep residual networks".
- kp4 06aa0f86ca41, 354dd2446113: the professor's English differs from the Chinese; followed the Chinese.
