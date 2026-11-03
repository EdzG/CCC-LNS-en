# Notes: Ch04 deck (02-lenet-cnn-skeleton-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (20 exact, 6 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp8 c4ce6d9e66b9 vs 001903fb2466: the readout says Conv+Pool ~2,616 and FC ~59,134; the observation text says "about 3,000" and "57,000+". Loosely inconsistent.
- kp2 8a6c0c2d4ec9: the professor's English ("Local scanning first, global classification last…") does not translate the Chinese ("extract features before spatial info disappears; FC is not the star, the later the better"); followed the Chinese.
