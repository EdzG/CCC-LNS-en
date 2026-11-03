# Notes: Ch03 deck (09-sgd-convergence-analysis-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (42 exact, 8 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp1 4bebc1d35cea: the professor's English title adds "Monotonic O(1/t) vs Fixed SGD Stagnation Band O(η)"; followed the Chinese.
- kp6 e72c973aab5f: the single-sample gradient *norm* is said to "stay at the β² level"; β² bounds the second moment (squared norm).
- kp9 192e84fd57c6: n=10⁷, B=128 gives ≈78,000 updates, not the 「10 萬」 (100,000) claimed.
- kp9 af04d0e59ed4: O(1/√n) ≈ 10⁻³ implies n≈10⁶, inconsistent with n=10⁷; "meaningless overfitting" is overstated.
- kp8 cf0f1ef91c87: the O(1/√t) rate with 1/√τ steps holds for the averaged (or best) iterate, not mentioned; "compresses the residual band to zero".
- kp14 54a17f0fa180: 「全域性最優」 conversion artifact.
