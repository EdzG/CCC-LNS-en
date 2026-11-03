# Notes: Ch03 deck (16-chapter3-synthesis-and-summary-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (28 exact, 9 patterns). `_dynamic`: `#lab-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp4 e459704c7011: GD's $O(1/t)$ rate called 「線性/次線性」 (linear/sublinear); O(1/t) is sublinear.
- kp4 7eb6838b14c7: the Hessian's 「退化方向」 (degenerate directions) are credited with opening escape routes; escaping relies on negative-curvature directions.
- kp3 f958a22324af: Du & Lee (2018) credited with proving global linear convergence of GD; that paper is mainly a landscape analysis.
- kp3 c817a49ba010 「線上性可分」, b1a15a1ede4e 「隻是」, d0222ea4e328 「推匯出」, 8e69c0d8dd0d / 4a23a63f442d 「擴充套件」, f958a22324af / 2b23c737fd67 / 191ce80beadb 「全域性」: simplified→traditional conversion errors; translated what was meant.
