# Notes: Ch02 deck (12-ai-foundations-sigmoid-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1 f35bb152394a: professor's second English line 'Gentle Switch, Honest Odds' has no Chinese counterpart ('honest odds' is extra); dropped, title rendered as 'The Gentle Switch: Sigmoid'.
- kp3 7b44f96ba522 / 7f8c9c2e7f17 / 533f98dee201: professor's English halves are one-line compressions that drop most of the Chinese; translated in full from the Chinese.
- kp3 7f8c9c2e7f17, kp5 c0e7441309a4, kp5 3cbd533254a9: professor's English says 'odds' for sigmoid's output; it is a probability, not odds (odds = p/(1-p)). Used 'probability'.
- kp4 4d458092611b: professor's English 'Hard and brittle' differs from the Chinese ('59 points and 9 points get the same scolding'); followed the Chinese.
- kp5 3cbd533254a9: the bilingual-en span 'Drag and watch odds move smoothly.' has no Chinese counterpart; kept as an English instruction with 'odds' fixed to 'probability'. The live spans #zVal/#oVal inside the math are kept as-is.
- kp7 533e5fd4c5ce: the slide says the gradient is recomputed with the MSE loss, but the formula box above it shows only do/dβ1 = σ'(z)x1 without writing L; the -2(0.269)(0.197)(8) line below implies L = (y - o)^2 (no 1/2). Arithmetic checks out (-0.848 → -0.85, β1 → 0.585).
- kp8 7b7abaf477fc: uses $a$ for the pre-activation, while the previous slides (kp5-kp7) use $z$ for the same quantity; kp10 then uses $a_i$ for the score and $z_i$ for the output, the reverse of kp5's $\sigma(z)$. Translated faithfully; notation is inconsistent across the deck.
- kp8 7b7abaf477fc: values check out (σ(-10) ≈ 4.54e-5, σ' = σ(1-σ) ≈ 4.54e-5).
- kp9-kp13: professor's English halves are terse slogans ('depth must fold', 'carve complex worlds', 'saturated, stalled'); translated in full from the Chinese.
- kp12 a7993ba76d56, kp13 2391467faf5e: title English span ('Roadmap', 'Reflection') dropped; English title written from the Chinese.
- kp13 quiz Q1/Q2 options are math/number-only units with English-only spans ('— that's tanh', etc.) and are not in this batch; they contain no Chinese and stay as the professor wrote them.

## Images

- The 2 inline image(s) are English-only and shown as they are.
