# Notes: Ch03 deck (05-momentum-acceleration-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (23 exact, 11 patterns). `_dynamic`: `#kp5-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp4 607616c91e64: with κ=1000 (rate 0.998) the error "barely budges" after 1000 iterations; actually 0.998¹⁰⁰⁰ ≈ 0.135. Overstated.
- kp10 c285b774ee02: α=0 labelled 「過阻尼質點 · 劇烈震盪」 (overdamped particle, violent oscillation); an overdamped system does not oscillate. α=0.9 "critically damped" (19fad3852d8e) / α=0.99 "underdamped" is a loose analogy.
- kp6 9d00ad6f62ee 「一沒有外力」 (一旦), 5cf9d9246a41 「純純不足以」: typos.
- kp9 49b9cfe55c4f: vectors "meeting at an acute/obtuse angle and cancelling" is vague (acute angles don't cancel).
- kp11 05d102f4ed66, 60543d32c25c, ea6e545541cd, 6ed4c4f287d8: the professor's English adds or leaves out content (e.g. "Vanilla SGD vs Momentum SGD" where the Chinese says plain GD vs classical momentum); followed the Chinese.
