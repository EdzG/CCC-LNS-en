# Notes: Ch02 deck (04-ai-foundations-mp-to-mlp-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp0: TOC links were 'Chinese · English' pairs; the English labels were replaced with translations of the Chinese (e.g. 動手算蘋果 'Compute the Apples by Hand' instead of 'Calc').
- kp1 39cc810f7c6e: professor's English 'Where one line fails, stack a space.' compresses the Chinese; translated from the Chinese.
- kp3 8ffa0391a3c3/b9945dd65852/efa173068d8e, kp4-kp7: the bilingual-en spans are one-line summaries of the Chinese (e.g. 'M-P was 1943, before computers went mainstream' drops McCulloch and Pitts simulating neurons with math); full Chinese translated instead.
- kp4 c8c84d7fe237: SVG label 加總 sits above an existing English 'sum' label; rendered as 'Total' to avoid 'Sum / sum'.
- kp8 fe55a7054db3: Chinese says XOR needs a 'curved boundary'; strictly a 2-2-1 MLP with threshold units gives a piecewise-linear boundary, translated faithfully.
- kp9 22285b55802b: professor's English 'Hidden layers fold space separable.' is ungrammatical; translated from the Chinese.
- kp10 25a61f3b3f6d: $a_i$ appears in both halves; kept once (Chinese half).
- kp10 7d441b4330ee: the English half's $\sigma$ is dropped (only in professor's English); Chinese half keeps $\sigma(\cdot)$ and $z_i$.
- kp12 894b8912666d: professor's English 'Next: depth that moves.' does not match the Chinese (stack hidden layers, fold space with nonlinearity, next class get the neurons moving); translated from the Chinese.
- kp13 b2b171c66dd5: professor's English '— more data only' adds 'only', not in the Chinese 更多資料; translated as 'More data'.

## Images

- The 1 inline image(s) are English-only and shown as they are.
