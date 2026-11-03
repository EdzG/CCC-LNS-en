# Notes: Ch03 deck (02-gradient-descent-learning-rate-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (14 exact, 6 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- chrome 2b859e8bc773 / 00aef2ba58cb: the professor's English says "Cauchy's Intuition (1874)"; the year is 1847.
- kp4 1af2d6d60866: 「最最佳化」 duplicated character (最佳化); 4020121eb0d9: 「峽長山谷」 typo for 狹長山谷 (ravine).
- kp8 2c329ea81dfe, 378a6af9bab6, 235999afeae0: monotone loss decrease for convex functions is claimed without the step-size condition (η ≤ 1/L); 378a6af9bab6 says "strictly decreasing" but writes ≤.
