# Notes: Ch03 deck (01-backpropagation-and-optimization-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (7 exact, 6 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- Upstream bug: the deck's quiz-explanation strings write '\delta', '\boldsymbol', '\rho' with single backslashes in JS, so the page shows mangled TeX ("$delta_i …", control characters, a line break where \rho should be). Our runtime entries match the mangled text and the English uses the intended TeX.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp13 c0132741238c: "GD (1874)"; Cauchy proposed gradient descent in 1847.
- kp6 53d241e1e540: `\text{若否則 }` is garbled ("if / otherwise"); translated as `\text{otherwise }`.
- kp12 7f0f6e3755e9, de04e59cf431: the professor's English says different things from the Chinese (over-parameterization "convexifies trajectories"; "Newton plunges into brittle sharp spikes"); followed the Chinese.
- kp4 64ae3231e1d9: Newton's method said to generalize badly because it "converges too fast into sharp minima": a contested claim.
