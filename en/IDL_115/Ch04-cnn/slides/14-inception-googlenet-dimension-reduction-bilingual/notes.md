# Notes: Ch04 deck (14-inception-googlenet-dimension-reduction-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (13 exact, 16 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp8 1cec6920abfc: 「Pooling 後接 1×1 抑制作為」 garbled (probably 抑制作用).
- kp2 af355b292d21, 1cec6920abfc: the 1×1 bottleneck is said to save 70%; the lab readout 891f738d91ab says 87% (which matches its own numbers).
