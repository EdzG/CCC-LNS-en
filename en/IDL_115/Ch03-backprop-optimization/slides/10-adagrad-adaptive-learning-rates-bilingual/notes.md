# Notes: Ch03 deck (10-adagrad-adaptive-learning-rates-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (29 exact, 7 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- Quiz explanations: the deck's getExplanation() picks the explanation by searching the card's text for Chinese keywords ('梯度長期偏大', '式 58', …). In EN mode the card text is already English, so most searches fail and only the "✅ Correct!" / "Think it over again:" prefix shows (switch to 中 to see the explanation). Explanations that do appear are translated.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp9 abddb33495f1 「取樣取樣」 duplicated word; b9198b12b507 「無法擴充套件」 conversion artifact (擴展).
- kp4 e5bfcb58fad7 / 62a054c84f95: AdaGrad's accumulated squared gradients presented as a diagonal Hessian approximation: a loose heuristic.
- kp3 569d8a8e8432, 8c09c0982227, 0dcbd6f79af7, fc38e4c59f54, 3e167257bff2, 5a9aa6a56cc1: the professor's English summarizes the whole card rather than the Chinese sentence; followed the Chinese.
