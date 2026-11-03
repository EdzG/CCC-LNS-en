# Notes: Ch03 deck (08-mini-batch-sgd-epoch-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (36 exact, 9 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp7 a15428056be1: the professor's English adds "at the cost of heavier per-step computation"; the Chinese instead mentions LR decay and Polyak averaging. Followed the Chinese.
- kp7 f838a4ea3507: the variance-ball radius is said to be proportional to ‖e_t‖² (dimensionally loose); 26b6fabe834f: with replacement the variance stays σ²/n > 0 as b → n (only when σ² > 0).
- kp9 814bafe12dea: full batch "gets stuck at sharp saddle points" (尖銳鞍點) mixes up saddle points and sharp minima.
