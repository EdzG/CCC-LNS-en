# Notes: Ch02 deck (14-ai-foundations-uat-chapter4-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp2 48766334fe1e: kept the <small> English subtitle (no Chinese counterpart inside the unit).
- kp3 11f6f673e6e8 / 9668bc6b2e91: professor's English halves are one-line summaries; translated the full Chinese sentences (皮皮挫 = Taiwanese 'scared stiff').
- kp3 22d3886677f7: kept the professor's English <span> sub-label 'Biological neuron' (the sibling path nodes are English-only with the same structure).
- kp5 53da55cee2b7 (and kp19, kp1 chip context): 引數 is used for 'parameter' (a Simplified→Traditional conversion artifact; in Taiwan 引數 normally means 'argument'). Translated as 'parameters'.
- kp5 fb62162b8c59: professor's English 'three pillars of modern neural learning' vs Chinese '現代深度學習'; followed the Chinese (modern deep learning).
- kp8 57ba614bba47: professor's English 'causes a false positive' is not in the Chinese; followed the Chinese.
- kp11 604e703bba13 / 7ed10ed66431: these units contain #boundaryEquation, #boundaryStatus and #boundaryStatusEn, which the bias slider script rewrites. Kept the ids. Because the engine swaps the whole unit's innerHTML, the page script's element references may be detached in EN mode (the equation/status would stop updating), and runtime text inside static units is ignored; consider listing these elements (or their parent divs) in _dynamic. In 7ed10ed66431 the #boundaryStatusEn span was kept because the script always writes English into it (dropping it is harmless too); the result shows two English lines ('Currently N / 4 predictions correct' + English status).
- kp11 604e703bba13: dropped the professor's English duplicate 'The green line is the boundary.' and kept the single translated sentence in the <span>.
- kp13 73cb460e743c / ab7b3ecbb1b4 / 8480e6df9411: 區域性 is a conversion artifact for 局部 ('local'); 8480e6df9411 even has the doubled typo 區域性性. Translated as 'local'/'locality'.
- kp13 74f6ef47a419: this ADALINE description's heading (h3 'ADALINE') is outside the unit; unit translated as a sentence fragment starting 'Uses ...'.
- kp14 1bac0dd15851: Chinese says UAT 'establishes the limits (極限) of a network's function-expressing power' — it really establishes a lower bound/guarantee on expressive power, not a limit; translated faithfully.
- kp15 6424fc0ec1f7: 'continuous, bounded, non-constant σ is enough to separate measures' is the discriminatory property (Cybenko/Hornik); stated loosely in the source, translated faithfully.
- kp16 c5e535949112: professor's English 'learned basis' is not in the Chinese ('provide a basis like Fourier trigonometric functions'); followed the Chinese.
- kp16 e0cc6b2724c8 / c1b50dd7f28e: calling 'F is a finite weighted sum of sigmoids' a 'representation theorem' is loose (it is the approximating form in the UAT); translated faithfully.
- kp18: quiz option order and correct answers unchanged; dropped the professor's English option glosses ('Correct output', 'Incorrect sign'), which would give away the answer and do not match the Chinese.
- kp19 4d9ab6fa67a0: kept the professor's English 'Next: backpropagation, ...' span, which has no Chinese counterpart; 'Lesson Complete · 本章結束' became 'End of Chapter'.

## Images

- The "AND vs XOR geometry" chart (key f1c39c8261ce) is redrawn in English (`assets/img-f1c39c8261ce.png`, script `en/tools/charts/Ch02-perceptron-mlp/img-f1c39c8261ce.py`). 「XOR：對角線交錯的斷層」 is rendered "XOR: classes interleaved along the diagonals".
- The other 1 inline image(s) are English-only and shown as they are.
