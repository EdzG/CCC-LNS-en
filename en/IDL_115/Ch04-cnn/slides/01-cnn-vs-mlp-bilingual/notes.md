# Notes: Ch04 deck (01-cnn-vs-mlp-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (17 exact, 8 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.
- The hover readout mixes the professor's English hint ("Hover output cell…") into the same text block as the Chinese, so it can't be hidden; our translation appears just above it.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp3 ba6bf8c97962: a 224×224 RGB photo is said to have "150,528 pixels"; that is 150,528 values (50,176 pixels × 3 channels).
- kp4 b50f18447cdc: 1,728 CNN parameters called "more than 4400 times" fewer; against ~77M it is ~44,600×, against 401,408 ~232× (probably a dropped digit).
- kp6 77a041a53e5f / b50f18447cdc: the same 64 3×3 kernels are counted as 576 (grayscale) and 1,728 (RGB) without explanation.
- kp7 36a99ee63e63: 「從億級到千級」 (hundreds of millions → thousands), but the slide's own example is ~77M (tens of millions).
- kp11 63166033ea8f: the professor's English sits in a plain styled span (no bilingual class); dropped like the others.
- kp3 20d971009427, d688cacdb35e, 23d396cbb16d, dcf34b31ed19, 63aa0f0743c9, 387f167c3408: section kickers pair a Chinese label with a different English one (e.g. 動機背景 vs "Image Structure"); followed the Chinese.
