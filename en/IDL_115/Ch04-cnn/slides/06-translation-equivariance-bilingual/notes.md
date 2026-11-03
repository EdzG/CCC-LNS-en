# Notes: Ch04 deck (06-translation-equivariance-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (12 exact, 7 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp9 56a630b67a05: quiz option B glosses 平移等價性 as "(equivalence)" while the deck elsewhere says equivariance; kept faithfully. Correct answer unchanged.
- kp2 9cb934f6e350: the professor's English adds "Convolution guarantees the former!", which the Chinese lacks; followed the Chinese.
- kp5 ead42887961d: the explanation of why scaling fails ("exceeds the receptive field of the 3×3 kernel") is loose.
