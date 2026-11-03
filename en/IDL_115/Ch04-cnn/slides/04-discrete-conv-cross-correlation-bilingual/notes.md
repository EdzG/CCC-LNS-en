# Notes: Ch04 deck (04-discrete-conv-cross-correlation-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (12 exact, 8 patterns). `_dynamic`: `#conv-readout`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 ab612d34410b, f4c642cd11c1: the 「正號」/「有加法」 (plus sign / addition) in K[m-i, n-j] is said to mean no flip, but m-i is still a subtraction.
- kp4 a3906146f8c1: 「（理論卷積後翻）」: 後翻 looks like a typo for 要翻; rendered "flipped in theoretical convolution".
- kp8 0b612a940f09: Eq. (2) a[t]=Σ x[a] w[t-a] uses `a` both as the output and the summation index.
- kp10 4624f7589de7: the professor's English "Master-Level Assessment" vs Chinese 觀念即時反饋 (instant concept feedback); followed the Chinese.
