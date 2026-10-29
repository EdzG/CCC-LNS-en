# Notes: Ch01 slide 06 (06-pattern-recognition-statistical-classification-bilingual.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp4 `fa69da7e5691`: "the prior pulls the boundary toward the minority class" is correct (the boundary moves toward the less likely class's mean, so the majority's region grows) but reads confusingly. Translated as written.
- kp9 `909dab49a271`: random forests are said to reduce variance "without increasing bias"; feature subsampling can raise bias slightly. Translated as written.
- 成見 is translated "prior belief" / "preconception" in this deck, where it means the prior, rather than the glossary's "bias".

## Where our English departs from the professor's English, and other choices

- kp1 d0282148f558: the professor's English renders 極致美學 as 'max-margin'; the Chinese literally says 'the ultimate in aesthetics' (an allusion to SVM's max margin). Followed the Chinese.
- kp2 e8841eb3bbd8 / kp1 / kp3 / kp4 headings: the separate English <small>/<span class="en"> duplicate was dropped; one English version written from the Chinese.
- kp3 c4767f8c8e96: the professor's English ('Linear, quadratic, staircase — each reflects an assumption about the world') omits the model lists and adds a sentence not in the Chinese; followed the Chinese.
- kp3 65a808b5a2aa: professor's English calls it 'No free lunch'; the Chinese just says there is no universal model, so no theorem name was added.
- kp4 fa69da7e5691: the Chinese says the prior pulls the boundary 'toward the minority class' (成見直接把邊界拉向少數類). Translated faithfully; this is correct in the sense that the boundary moves toward the less likely class's mean (enlarging the majority's region), but readers may find 'toward the minority' confusing. Worth a notes.md entry.
- kp5 18f9ae7fe7aa, eeb5b22d15ad, 4b5a5ca8d96c, kp7 1702d1a663e0: some math segments appear only in the professor's English half ($C_1$, $C_2$, $1/d$, $L$, $f_\theta$, $P(Y\mid X)$) and were dropped with it; the Chinese half's math is all kept ($w=1/d$, $d_M(x,y)=\|Lx-Ly\|_2$, $f_\theta(x)$, $P(Y=1\mid X)$ cover them). $\Sigma$, $\Sigma_k$ (kp6) and $P(X\mid C)$ (kp7) were worked into the English naturally.
- kp5 d98984a43ec7: professor's English “With 0.9 vs 0.1, same x=5 gives 0.9 vs 0.1 posterior” is garbled; followed the Chinese. Kept the Chinese half's math only ($0.9$/$0.1$ once each instead of twice).
- kp5 18f9ae7fe7aa: 「成見」(prejudice) rendered as “bias” per glossary; professor's English says “belief”.
- kp5 33441669bdf0: 「長相」似然 translated literally as the “looks” likelihood (the class's appearance), kept the professor's metaphor.
- kp8 72a88f4caa33: SVG label lengthened slightly (“inside dashed circle”); check it fits.
- kp9 04f56ddb5495: 50萬 rendered as 500K (NT$ implied, not stated).
- kp9 909dab49a271: Chinese claims random forests reduce variance “without increasing bias”; strictly, feature subsampling can slightly increase bias. Translated faithfully.
- kp10 f200f99a586f: $K$ appears only in the English half; kept it as 'a kernel $K$, i.e. $K(x_i,x_j)$' so every math segment survives.
- kp10 8d8b0fb3a0c4 and similar: professor's English is a terse summary throughout kp10-14 (drops sentences, e.g. 'in the big-data era it is often replaced by deep networks', the 'stubborn holdouts' metaphor, the KP11 'dark-background version keeps the original design' clause); translated the full Chinese instead.
- kp10: 蚊香 rendered 'mosquito coil'/'mosquito-coil spiral', consistent with the existing _runtime translation of the Q3 feedback.
- kp11 53cdfa7cddd9: Chinese says '看兩軸' (look at two axes) but then lists four questions; translated as 'Look at the axes' to avoid the mismatch (professor's English repeats 'Two axes').
- kp12 aa0e4b1f3e32: professor's English 'Classify not with the flashiest model' is unidiomatic and drops the knife metaphor; followed the Chinese.
- kp12 9cbd4b83adea: 對數勝算線性 rendered as 'Linear log-odds' (logistic regression assumption).
- kp13 b5d1d0d6bb6f, kp13 d34d410c3633: the same math ($P(Y\mid X)$, $k$) appears in both halves; kept once.
- kp14 d34122caf3e5: Chinese writes the example as $X=5$, the professor's English as $x=5$; kept the Chinese $X=5$ (matches the rest of the page's $P(X=5\mid C_1)$), so $x=5$ is intentionally absent from en.
- general: in this deck 成見 means prior belief (glossary maps 成見 to 'bias'); translated as 'prior belief'/'preconception' here, since the page equates it with the prior.
- math: segments that appear only in the professor's English half were dropped with that half, as the rules require; the distinct-segment check will flag them: kp3 3c3fe0f54395 ($y$), kp4 ab983d8ab5e3 ($\arg\max$; the Chinese half's $ \arg\max_j P(C_j\mid X)$ is kept), kp4 58a85586ad2a ($C_j$), kp4 15ff8a8f4e4a ($\mathcal{N}(3,1)$, $\mathcal{N}(7,1)$, $x=5$; the Chinese half uses $C_1\sim\mathcal{N}(3,1)$ etc. and never mentions x=5), kp4 fa69da7e5691 ($0.9$, $0.1$). Duplicate counts were reduced to the Chinese half's count in 866dae32d0dc, d80c93158eb0, f2299c08eaa6, b62f7f27d115, 834cb833118d, 5bc6581749c3, a9b1f9287878.
- Headings with a <span class="en"> subtitle: where the span only duplicated the title (kp7 ed0d7b44cd02, kp8 de9cd8a7b479, kp9 0d760aa6a6a0) it was removed; in kp5 3893d7756044 and kp6 ebd1306f95a8 it keeps the non-duplicated part (“Interactive Demo”, “Covariance Decides Linear or Curved”).

## Images

- Inline charts with Chinese labels get English redraws in a separate commit.
