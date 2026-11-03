# Notes: Ch03 deck (idl115-w3-backprop-optimization)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (1 exact, 0 patterns).

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp2 This condensed deck mostly writes "English | 中文" as plain text rather than in bilingual-en spans; our English translates the Chinese half and drops the professor's English half. In the Instructor/Student dialogue units (6feadc119faa, 89aa9d1f51d8, bd48a8dfb727, e9661a064ddf) the quote is translated from the Chinese 「…」 and the professor's English quote is dropped.
- kp45 6a640099ca25: the Chinese only says "match the five questions to their tools" without listing them (the English lists them), so the answer 448479f843de had nothing to refer to; the professor's five quoted questions are kept after the translation.
- kp1 c067177425b2: the English names the course code "IDL115 · CSIE3544AB"; the Chinese gives the semester (115 學年度第 1 學期) instead. Followed the Chinese.
- kp2 07c656c1dfb7: English "Certainty" vs Chinese 把握; used "Confidence". 4e63e3c575ac: English "generalization boundary" vs 泛化邊界; used "limits of generalization".
- kp21 a9bee360b757: the English half writes $a$, $z$, $\hat y$ separately, the Chinese $a,z,\hat y$; kept the Chinese form once.
- The 12 inline images already carry bilingual "English | 中文" labels, so they are not redrawn (6 are 3D renders).
