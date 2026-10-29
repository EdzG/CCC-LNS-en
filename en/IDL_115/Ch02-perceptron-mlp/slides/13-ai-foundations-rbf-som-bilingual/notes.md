# Notes: Ch02 deck (13-ai-foundations-rbf-som-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1 17ccbc84a2d5: 奇幻漂流 alludes to the Chinese title of Life of Pi; rendered as “A Fantastic Voyage”.
- kp2 169d48a2a6ce: the big-question slide shows the Chinese question plus a <small> English paraphrase; EN keeps only the translated question (the <small> line dropped as a duplicate).
- kp3 a0a82968d01d etc.: professor's English renders 偷懶 as “clever shortcuts”; EN follows the Chinese (“lazy”) with quotes, keeping the joke.
- kp5 aa30fc1dea60: e^{-0.5} = 0.6065, which rounds to 0.607 (as the figures slide, quiz-adjacent explorer and readout use: 0.607, 1.213); this slide and the quiz answer use 0.606 and 1.212 (truncation). Translated as written.
- kp6 4f39d040fe0b: the professor's English (“solve the linear problem directly instead of iterating”) matches; Chinese 疊代 is a variant of 迭代.
- kp9 963dbc20ef82: 區域性性 is a doubled suffix (“locality-ness”); translated as “locality”. Professor's English heading was only “Precision figures”.
- kp9 47e2a59c4cb2: 衰減中的鄰域光暈 = decaying/shrinking neighborhood halos; rendered “shrinking”.
- kp11 ae7a3241e1c9: the bilingual-en sentence has no Chinese counterpart (adds content), so it was kept as is.
- kp12 dc1eab759885/7d1af8fb4c9c/527b2de4465a: professor's English questions paraphrase loosely (e.g. “What does the first RBF layer do?”); EN follows the Chinese wording. Quiz letters and correct answers (Q1 B, Q2 A, Q3 C) unchanged.
- kp12 3fb902b99903: AI image-prompt accordion summary translated (it was in the batch); the prompt text itself is already English.

## Runtime

- Runtime: the slider <output> elements inside translated labels are kept live across the swap, so the readouts keep updating.

## Images

- The 1 inline image(s) are English-only and shown as they are.
