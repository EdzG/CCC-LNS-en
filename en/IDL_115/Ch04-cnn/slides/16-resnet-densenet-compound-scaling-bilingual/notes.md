# Notes: Ch04 deck (16-resnet-densenet-compound-scaling-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (18 exact, 9 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- Canvas title shortened to "Residual sum & gradient flow (H = F + x):" so it doesn't overlap the "Residual F" label.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp3 91c297461f41: "when overfitting, the training error should be zero" overstates it.
