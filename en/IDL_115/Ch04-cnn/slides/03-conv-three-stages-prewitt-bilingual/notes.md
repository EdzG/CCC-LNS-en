# Notes: Ch04 deck (03-conv-three-stages-prewitt-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (21 exact, 5 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp4 2954c3d2fc05: the horizontal kernel is said to respond to a "brightness step in the horizontal direction"; it detects horizontal edges, i.e. an intensity change in the vertical direction. Ambiguous wording.
