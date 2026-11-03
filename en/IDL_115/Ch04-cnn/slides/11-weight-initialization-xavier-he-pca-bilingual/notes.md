# Notes: Ch04 deck (11-weight-initialization-xavier-he-pca-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (20 exact, 7 patterns). `_dynamic`: `#init-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 ea38e1a698e2: 「阻斷了一半的負響應（均值歸零）」 is unclear: ReLU zeroes the negative half; it does not zero the mean.
- kp3 07a7c11f3a3f: "|w| > 1 → explosion" is a simplification (explosion depends on fan-in × variance).
