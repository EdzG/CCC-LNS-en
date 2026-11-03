# Notes: Ch03 deck (04-line-search-steepest-descent-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (23 exact, 9 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp10 835f847ee901: the comparison table says halving backtracking "guarantees sufficient decrease (Armijo)", but Algorithm 1 / Eq. (5) only checks simple decrease, which the deck itself says is not sufficient decrease.
- kp4 ce09a8ed21ba: "the objective must decrease when η<1/L" is sufficient but stricter than needed (the descent lemma gives decrease for η<2/L).
- kp4 729c0a77d6b0: 「無量綱二次模型」 (dimensionless quadratic model) is vague.
- kp2 3fab36c6089f, 023c190716b0, 3ff8e02f0fd1, 2bb33ea28a4e: the professor's English paraphrases or adds content (e.g. the Wolfe conditions); followed the Chinese.
