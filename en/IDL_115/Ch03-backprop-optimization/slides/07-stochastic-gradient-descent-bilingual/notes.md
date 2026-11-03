# Notes: Ch03 deck (07-stochastic-gradient-descent-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.sub-en`, `.bilingual-en` and `.bilingual-en-inline` lines are hidden via `_hide`).
`kpN` = the Nth section; hex ids are strings.json keys.

## Runtime and behaviour

- Demo readouts, canvas labels and quiz feedback are translated through `_runtime` (22 exact, 11 patterns). `_dynamic`: `#kp7-ro`.
- The deck's quiz JS picks each explanation by searching the card's text for Chinese keywords; `_zhText` makes those reads see the original Chinese, so explanations also appear in EN mode.

## Errors and unclear points in the Chinese, and where the professor's English differs (translated from the Chinese)

- kp4 6734e72398fc, b3e05395f07b, eff07ed86944: fixed schedules like η=1/k are called 「自適應」 (adaptive); they are predetermined decay schedules.
- kp11 958641f7995e vs c8940aca75ce: the single-sample gradient at the optimum is "never zero" in one place, "usually not zero" in the other; SGD "locks onto the global minimum" overstates it for non-convex losses.
- b7280eb16650: the lab readout labels -∇f(0) = 4.0 as the 「全梯度」 (full gradient); it is its negative.
- kp9 4546546a219b, fabd8626fd1f: a batch is said to cut the variance by B, ignoring the (1-B/n) correction introduced in deck 08.
- kp5 0d3f4e78a301: the formula $\mathbb{E}[\nabla f_i(\boldsymbol{w})] = \nabla f(\boldsymbol{w})$ appeared only in the professor's English span; moved into our heading so it still shows.
