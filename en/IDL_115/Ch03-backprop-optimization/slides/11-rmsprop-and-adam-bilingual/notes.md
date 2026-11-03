# Notes: Ch03 deck (11-rmsprop-and-adam-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (24 exact, 8 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp9 0d852d51e725: ε=1e-8 said to "sit right near the lower bound of single precision"; float32 machine epsilon is ≈1.2e-7 and the smallest normal ≈1.2e-38.
- kp4 aa8548db2a57: the RMSProp EMA is written with ‖∇f‖₂² (a scalar), conflicting with the per-coordinate v_i of 5dae30d4ee61.
- kp1 39bba1a57acb, 54236c651c89, 75e87e995a94, f4e0e5895501: the professor's English titles/headings differ from the Chinese; followed the Chinese.
