# Notes: Ch03 deck (06-backpropagation-chain-rule-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (32 exact, 16 patterns). `_dynamic`: `#kp6-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp7 fb1ea6aca28e: the professor's English heading adds "Equation (18) vs Hidden Layer Equation (19)"; 3ce6678d2b2f: Chinese "local Jacobian" vs English "local gradient". Followed the Chinese.
