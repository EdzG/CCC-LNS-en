# Notes: Ch01 slide 10 (10-ml-overview-treasure-map-bilingual.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp6: 邏輯開 is likely a typo for 邏輯閘 (logic gate); 相關性學 is cut short (相關性學習).
- kp7 `b7151a6750f8`: in the dark "key message" box the formulas $ℋ$ and $S$ are drawn in the page's default dark gray and are nearly invisible in both languages (page CSS).
- 線性終數 is rendered "the fate of linearity" here and "the linear limit" in slide 08; it is a coinage of the professor's.
- Runtime: in two quiz answers `$s\to a\to r$` sits in single-quoted JavaScript, so `\t` becomes a TAB and the page shows `$s<TAB>o a<TAB>o r$`. The English keeps the same broken text so the lookup matches.

## Where our English departs from the professor's English, and other choices

- kp0 6e0ed77c7795: dropped the professor's English second line (a shortened duplicate of the first).
- kp1 500cc96362ee: 線性終數 ('the end/fate of linearity', referring to Minsky 1969 and XOR) is an unusual coinage; rendered as 'The Fate of Linearity'.
- kp1 17784e6a823c: professor's English 'supervised, unsupervised, RL' replaces the Chinese analogy (with a teacher / without a teacher / learning the hard way); followed the Chinese.
- kp2 151534b42534: 滿漢全席 (Manchu-Han imperial feast) rendered as 'full imperial banquet'; the professor's English drops 'menu' and 'model' framing slightly.
- kp3 75a5a1c2740a: professor's English subtitle 'Hypothesis, Scoring, Search' differs from the Chinese title (order, taste, find the master chef); followed the Chinese.
- kp3 42cdd74b7ccb, 0522c99ea564, 7bf416db5146, 006e9df5bcca, f9abe27246df: the professor's English is a terse summary that drops sentences (e.g. 'the set F is the menu', 'goal is to minimize loss', 'blind men and the elephant'); translated the full Chinese.
- kp3 7bf416db5146: the Chinese uses 盲人摸象 (blind men and the elephant) for gradient descent, which normally means seeing only part of the whole; the intended sense is probably 'groping in the dark'. Translated faithfully.
- kp3 73682046d1d8: $:=$ and $\arg\min$ appear twice (once in each half); kept once each from the Chinese half. Professor's English '$:=$ defines' omits the f in F part.
- kp3 8573fbc9d12b, 14c42d3708d6, a0089d51e10a: kept the professor's analogy label span (Menu/Critic/Search in Fog) as a parenthetical gloss, since it is not a translation of the term; kp4 labels (Supervised etc.) were dropped as duplicates.
- kp4 5fc3fc4fc516: $s$, $a$, $r$ appear in both halves; kept once each from the Chinese half.
- kp5-9: the professor's English halves were telegraphic ('No map, lost mountain.', 'Line cannot cut diagonal', etc.); all rewritten as full sentences from the Chinese. The .en/.bilingual-en wrappers were dropped so the single English version shows as main text (same as kp0-4).
- kp6 44e906cb46c0/fea45ccc98f8/1758d0137722/6183393c5f54: the Chinese writes 邏輯開, an apparent typo for 邏輯閘 (logic gate); translated as 'logic gates'. Professor's title English 'Gradient Loop' differs from the Chinese 最佳化迴路 (optimization loop); followed the Chinese.
- kp6 094c6d575515: 相關性學 is truncated (相關性學習); translated as 'correlation learning'.
- kp7 f14b6a6b5594: 'the bigger the loss, the higher the score' reads oddly next to 'find the lowest-scoring dish' (S is a loss to be minimized); translated faithfully.
- kp8 a14f1d64f7fa: professor's English 'White-box meaning?' is wrong; the Chinese asks for the plain-language (白話) meaning.
- kp8 81e3534bbc5d: the English half's $s\to a\to r$ is dropped; kept the Chinese half's $s$, $→$, $a$, $→$, $r$.

## Images

- Inline image #00: NO-CHINESE (perceptron AND vs XOR plot, English-only)
- No redraw needed: the inline images have no Chinese text.
