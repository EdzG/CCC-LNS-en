# Notes: Ch04 deck (15-unet-contracting-expansive-segmentation-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (24 exact, 13 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp6 9322e721b268, 27541e9b98a8: 568 − 392 = 176, so the crop is 88 px per side, but the page says "88-pixel difference" and "Crop 44px per side" (both half the real values).
- kp4 2d8a3e949a59, 43ebe5b2868d: the U-Net paper used momentum 0.99, not 0.9.
