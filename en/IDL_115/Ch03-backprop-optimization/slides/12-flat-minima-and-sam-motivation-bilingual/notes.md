# Notes: Ch03 deck (12-flat-minima-and-sam-motivation-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (24 exact, 13 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 e7af5ced7955: ΔL said to "explode exponentially", but under the page's second-order Taylor model it grows quadratically in Δw.
- kp12 d563ff502258: the lab readout computes L = k·Δw² (20×0.36 = 7.2) without the ½ of the ½ΔwᵀHΔw form in section 05.
- kp6 687899a3f5aa: SAM said to "explore along the principal eigenvector of λ_max"; loose — SAM's perturbation follows the normalized gradient.
- kp2 a1a77eb91efe 「不是隻有」, 8bebbbccb70f 「最大麴率」, 3e46a19be3d7 「推匯出」, 019ea9d38e7d / 6e222aaecb4d 「全域性」: character-conversion typos; translated the intended meaning.
- kp4 0ba195c54029: the professor's English heading adds "(Foret et al., 2020)"; followed the Chinese.
