# Notes: Ch04 deck (08-detector-and-pooling-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (12 exact, 7 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 f02fb7b9cda5, 7832a410ba7e: median of the top-right window [7,5,2,4] given as 5.5 (should be 4.5); the lab text repeats [[2,5.5],[5,1.5]]. Same error as the lecture page KP8.
- kp6 a53f0d2cbf21: SVG label typo 運運算元 (should be 運算元); translated "statistical operator".
