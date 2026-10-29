# Notes: Ch01 slide 07 (07-ml-regression-dimensionality-reduction-bilingual.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp4 `28acaddfb16a`: the formula block uses $\mathbf{w}$, $b$ but the sentence says $\theta$ may spiral out of control, without saying they are the same parameters. Translated as written.

## Where our English departs from the professor's English, and other choices

- kp1 ff6f34b17d5f: professor's English ('Teach machines to predict ... penalty & geometry') adds 'penalty & geometry', which is not in the Chinese; translated from the Chinese.
- kp2 6a506bd2cb96: professor's English renders 學歪 as 'overfit'; the Chinese is a casual 'learn crooked', kept as such (the page explains it as overfitting later).
- kp3 bdceaa290016 / kp3 1d9f54436165 / kp3 e4c4be1b6dcc / kp4 6746b1323642 / kp4 28acaddfb16a / kp4 15536b72f4c9: professor's English halves are heavily abbreviated summaries of the Chinese; translated the full Chinese.
- kp3 b2372db4b2f0 / kp4 90e1b462edeb / kp4 b00edf7420ce / kp3 bdceaa290016: math that appeared only in the professor's English half was dropped; all math from the Chinese half kept.
- kp4 28acaddfb16a: the formula block uses w and b ($\mathbf{w}^\top\mathbf{x}+b$) but the sentence says $\theta$ may spiral out of control; notation switches between w and θ without saying they are the same parameters (translated faithfully).
- kp5 0ee41e5616d3: 罪過值 (literally 'sin value', the professor's playful name for the MSE loss) rendered as 'sin score'; the professor's English elsewhere uses 'Sin Value'. Keep consistent across batches.
- kp6 fea21d954b48: the professor's English 'Big → bankruptcy; zero → free & sparse.' has no Chinese counterpart and was dropped with the bilingual-en half.
- kp6 c6ea8f7bfd25: professor's English 'Kink at 0 is sticky' is a loose paraphrase; translated from the Chinese ('sensitive to small coefficients, optimization path gets stuck at the corner').
- kp6 994bd11a0636, kp7 034d05085a93: kept the English-only '(drag)' / '(shifts scores)' spans since they have no Chinese counterpart.
- kp8 661e6745071d: Chinese 選「最鼓的方向」壓 is ambiguous (squash along/into the bulgiest direction); translated as 'pick the bulgiest direction to squash along', meaning the kept direction. The professor's English 'Stuff suitcase into paper' is unidiomatic.
- kp8 ab7f2cafbaa2, kp5 f0f8cf600d88, kp9 8a6db4e97eb9: dropped the trailing English summary after '·' (it paraphrases the Chinese).
- kp10 4c3d06e8cfd8: the professor's English half writes $d=2\\to p=1$ (double backslash, renders as a line break instead of an arrow); dropped, the Chinese half's $d=2\to p=1$ is kept.
- kp10 874995080c16: Chinese inside \text{} translated (監督目標 -> Supervised goal, 類間距離 -> between-class distance, 類內散佈 -> within-class scatter).
- kp10 512752c0c136: professor's English says supervised 'reshapes metric with y; b shifts, w orients' and omits that w gives the most discriminative direction; translated from the Chinese.
- kp11 9aa708a00bec: professor's English 'Penalties teach models' loses '教模型做人' (teach models to behave); 'predict or perceive' rendered as 'predict or understand' per the Chinese 看懂.
- kp11 94583b48e226: professor's English drops the last line (curved manifold -> nonlinear dimensionality reduction); translated all five lines.
- kp12 32a85c3ceadb: professor's English 'how does color-blind separate?' is ungrammatical; rewritten from the Chinese.
- kp13 f06e33f847cc: professor's English 'which direction does it keep' differs from the Chinese 壓哪個方向 (which direction does it squeeze along) and omits the final sentence; translated from the Chinese.
- kp13 e462955823be: professor's English says 'linear vs nonlinear'; the Chinese names PCA vs t-SNE/UMAP, kept.

## Images

- Inline image #00: NO-CHINESE (English-only; PC1 label overlaps the colorbar in the original)
- Inline image #01: NO-CHINESE (English-only; plain-text math such as "X in R2", "f_theta", "w'x" in the original)
- No redraw needed: the inline images have no Chinese text.
