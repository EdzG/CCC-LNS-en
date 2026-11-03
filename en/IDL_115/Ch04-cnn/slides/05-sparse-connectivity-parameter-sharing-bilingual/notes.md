# Notes: Ch04 deck (05-sparse-connectivity-parameter-sharing-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (22 exact, 6 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 a20bc6559fec, 53b42790e0a8, 66a506b0eaaf, readout a8a94843fcaf: the conv layer's parameter count is given as k×n; with parameter sharing one kernel has only k parameters (k×n is a locally connected layer, or the runtime in Goodfellow). Contradicts the SVG label 442095438ad3 ("2 weights, shared") and c2bf106e8056.
- kp5 64d577b8cd4b: m ≈ 50,000 for a 224×224 colour input; that is 50,176 for one channel, ≈150,528 with 3 channels.
- kp6 487ff5bf5643: typo 「那隻不過是」 (只).
