# Notes: Ch03 deck (03-convergence-criteria-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (21 exact, 9 patterns). `_dynamic`: `#kp3-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp12 2b6ae358ed4b, fd58e2c4283f: w=0 of the 1-D f(w)=w⁴/4−w²/2 is called a 「局部最大鞍點」 (local-maximum saddle point); in 1-D it is a local maximum, not a saddle.
- kp13 7eb5a396abf9: typo 「隻適用於」 for 只適用於.
- kp5 44e368e6b62b: SGD gradient noise is said to be Gaussian; a simplification.
- kp5 d5edaee85f8c: a strictly convex function's zero gradient called "the unique global lowest point"; a strictly convex function need not have a minimizer (e.g. eˣ), though when the gradient is zero it is unique.
- kp3 24288b8c0fd6: the professor's English is a different summary; followed the Chinese.
