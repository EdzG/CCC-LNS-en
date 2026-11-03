# Notes: Ch04 deck (09-pooling-invariance-downsampling-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (14 exact, 10 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp4 7cd2378fb166 / 126b3073b2ee vs 644ef0acc93e / 85c34bd7c653: the SVG's pooled values (before 4,8,9,4; after 4,8,5,9) don't match the lab readout (baseline [[4,8],[7,9]]; shift=1 [[4,8],[5,7]]).
- kp2 95d84be0ea5d, b17d0888f0d8: "all four (input) pixels change", but the figure's input is 4×4.
