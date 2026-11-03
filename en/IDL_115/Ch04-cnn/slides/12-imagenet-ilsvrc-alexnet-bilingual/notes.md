# Notes: Ch04 deck (12-imagenet-ilsvrc-alexnet-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (27 exact, 13 patterns).
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp5 1c621d4cced5: Eq. (8) called a "negative log objective" but the formula has no log (minimizes −p). Same as the lecture page.
- kp4 6584d42413e9 vs 334679413de4: SVG says "ILSVRC 2012 winner, top-5 17.0%"; the lab says "ILSVRC 2010: top-1 37.5%, top-5 17.0%". 17.0% is the ILSVRC-2010 test result; the 2012 winning entry was 15.3%.
- kp4 140310015515: 「徹底解決了梯度消失問題」 (completely solved vanishing gradients) is overstated.
- kp4 2fdcf0d835ed: SVG label 「3×3 堆疊」 (stacked 3×3) for AlexNet; stacked 3×3 kernels are VGG's idea (AlexNet uses 11×11/5×5/3×3).
