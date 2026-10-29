# Notes: Ch02 deck (10-ai-foundations-loss-functions-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp0 nav items: dropped the professor's short English labels (e.g. 'Regression', 'Curves', 'Explorer', 'Selection') and translated the Chinese labels so they match the slide titles.
- kp1 e0b35a931b6b: cover title written as English title text; the small .en span 'Common Loss Functions' was dropped and its content merged into the title.
- kp2 e42b5aafc40a: professor's 'What should a wrong prediction cost?' replaced by a translation of the Chinese ('The model got it wrong: how should we penalize it?').
- kp2-kp7: most .bilingual-en spans are one-line summaries, not translations; the Chinese sentences were translated in full (e.g. kp4 f8308444d509 omits subgradient; kp4 9e3bd7609a25 omits 'not a core guarantee in ordinary regression'; kp6 4b8800e39981 omits 'hyperparameter tied to data scale').
- kp3 196a9b2f430b: Chinese inside the two \text{...} arguments was translated; the rest of the $$...$$ is unchanged.
- kp3 52ea3b847e55 / 9cdbe7d6bd8f: the professor's English half repeats $i$ / $l$; kept each math segment only as many times as it appears in the Chinese half.
- kp4 effe0fe17e71: kept the casual 'three brothers' (回歸三兄弟) instead of the professor's 'Regression Trio'.
- kp6 207bcbbbab7b / 4b8800e39981, kp8 26f9ec194f87: the English half repeats $\delta$ / $m$; kept the count from the Chinese half.
- kp8 26f9ec194f87: professor's English 'Zero loss requires the signed margin to reach $m$' dropped; Chinese says loss is 0 only when y f >= m (math kept from Chinese half).
- kp9 8aa6a946aa7b: professor's English says the gradient 'can' shape features; Chinese says it 'also' shapes them. Followed the Chinese.
- kp10 88676674576f: this <label> contains <output id="residualValue">, which the page JS caches by getElementById at load; swapping the label's innerHTML in EN mode replaces that element, so the residual value readout may stop updating in EN mode (the marginSlider/deltaSlider labels are not units because they have no Han text). Engine-level issue, worth checking in coverage.
- kp11 ecf534ae8a3d: English half repeats $\delta$; kept it once (count from the Chinese half).
- kp11 table cells: professor's English is often a looser paraphrase (e.g. 'Needs probability outputs' for 輸出需 softmax／sigmoid, 'Classification' for 多類別／二元分類); translated the Chinese.
- kp12 314b627d3ec7: 標籤 rendered as 'Label' (professor wrote 'Target') to match the 'label format' step in 1c9ae82a8f93.
- kp12 quiz buttons: only the Chinese half dropped; order and correct answers (Q1=B MAE, Q2=C, Q3=A Equal) unchanged.

## Runtime

- Runtime: the <output id="residualValue"> inside a translated label is kept live across the swap, so the readout keeps updating.

## Images

- The 2 inline image(s) are English-only and shown as they are.
