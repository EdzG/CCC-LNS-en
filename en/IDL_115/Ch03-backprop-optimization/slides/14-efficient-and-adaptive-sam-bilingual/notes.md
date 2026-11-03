# Notes: Ch03 deck (14-efficient-and-adaptive-sam-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (21 exact, 17 patterns). `_dynamic`: `#kp14-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- Canvas label 「銳度 = X (嚴格不變 ★)」 shortened to "Sharpness = X (invariant ★)" to fit its box.
- The weight-sampling (SWP) demo draws a new random mask whenever its slider fires, so the canvas changes after each language switch.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp6 a6802d9fd6c3: T_{Aw} = A T_w with T_w = diag(|w_i|+γ) holds only for γ = 0 (and s_i > 0); "always holds" is not exact.
- kp11 30f853f3e7d9 (quiz A): E[ε*_i] — ε* is deterministic given w; the expectation is redundant.
- kp3 1525ff74662b, 7b5acf945cb5: SWP "cuts the weight dimension in half" only for β = 0.5.
- kp7 ab3f95b2391f (SVG): SDS saves backprop on "50%–70%" of samples; the lab default and text show 50%.
