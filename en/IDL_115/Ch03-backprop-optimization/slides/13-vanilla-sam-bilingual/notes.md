# Notes: Ch03 deck (13-vanilla-sam-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (30 exact, 7 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 777fe8b9ddb7: 「以幾何平坦度為正則化項…的現代最佳化正規化」 mixes 正則化 and 正規化; translated literally.
- kp8 82d52884abff: GSAM / ASAM are said to adapt ρ and improve "geometric gradient orthogonality": only roughly fits (ASAM rescales the neighborhood; GSAM uses an orthogonal decomposition for its surrogate gap).
- kp3 21c5ee20e656: the professor's English says flat minima "consistently yield superior" generalization, while the Chinese calls it a debated hypothesis; followed the Chinese.
