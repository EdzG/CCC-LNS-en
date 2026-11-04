# Notes: Ch05 lecture page (Ch05-regularization-overfitting)

`kpN` = knowledge point N, `guide:N` its 教授祕笈 box; hex ids are strings.json keys.

## Translation choices and limitations

- The 16 demos load `demos/demo_kpN.js`, which was never published upstream, so their canvases and readouts are empty in both modes. Only their static text (headings, slider labels, Principle / What this does) is translated. `_runtime` covers only the quiz feedback and the progress bar (same strings as Ch04).
- The professor's "English recap" blocks (49 English-only blocks) stand alone and are kept as they are; they read correctly.
- The 祕笈 badge on guide buttons is "Notes", the same as Ch01–Ch04.
- 60db6ab4f027 / ee7923d7ec67 (kp16): the proverb 三個臭皮匠，勝過一個諸葛亮 is "two heads are better than one (three cobblers beat one Zhuge Liang)".
- f9d2497cdfed, cf12ca08aed1 vs 22316bff87bf (kp9/kp10): the practice-exam analogy calls the error a "score" (lower is better) in two places, then uses "score" in the usual sense; kept literally, so "the score keeps dropping" means improving.

## Errors and unclear points in the Chinese (translated faithfully)

- kp1 e9c3790aa617 (takeaways): "classification labels come from a finite set; regression labels are continuous" has nothing to do with data splitting; looks left over from Ch01.
- kp0 TOC: two entries are numbered 3.2 (c9d475e4c2b2 Stein's Lemma, ba7d3abb8eea Case II).
- Typos rendered with the intended word: 812319147b86 正確分功 (分工); 70b7de2c9e9c 變熒數 (變異數); 3bb3bb919231 反直直覺 (反直覺); 懲罼 for 懲罰 in e1fce4b098ec, 8385f85cbf22, 847ac76ad551, b1e7d7063aa8; 5164b9794397 模組 for 模型 (kept "a single module"); cfa291b61e4d uses simplified 二维; 2b3486a92f86 「梯度 descent」.
- 9e062b2e3fb6: the source has a literal `Stein\'s` (stray backslash, visible on the page).
- kp3 70b7de2c9e9c / 03dad751c287: "Covariance 是第三個變數" means the third *term* of Var(aX+bY); kept as "the third variable".
- guide:3 931a78da05fb: "one is the square of the other" gives zero covariance only if X is symmetric about 0; not stated.
- guide:3 45f571642224: loose link from KP12's Hessian eigendirections to variance decomposition.
- guide:5 79f017a6c5b1: the noise floor makes the empirical error larger than the true error only in expectation.
- kp6 bb6ad094910d: says "average" over the n_tr training instances, but Eq. (28) is a sum.
- guide:6 597599ddf0e6: "Misconception one" (Stein's Lemma only works for Gaussian noise) is answered "Right", so it is not a misconception.
- guide:6 ecd8643c851f: "被高估到 3.6" is odd wording; rendered "would be estimated higher, at 3.6".
- guide:8 d0abec77071d: the true function is quadratic (0746daef7322), yet the cubic fit is called "closest to the true function"; the table has only degrees 1, 3, 10.
- guide:8 4aeffbaeb238: the "second misconception" (overfitting = high variance, low bias) is answered "Right".
- guide:8 1b9e1dcbf449, kp7 e7e31a1cdce0: "the complexity penalty grows as err is minimized" mixes the Eq. (28) sensitivity with training dynamics.
- kp10 de4926b4d082: "from Eq. (28), dropping the constant term", while the section and its guide call the formula Eq. (36).
- kp11 c2f507ac64e6: the explanation says "no method can do well on dense problems"; the correct option 528cc753f67d says "there is no silver bullet otherwise".
- kp12 8385f85cbf22: Ω = w² with w† = w*/(1+α) holds only if J = ½(w−w*)² or Ω = ½w².
- guide:11 b158c1c10d69: odd analogy for ℓ1 ("mandatory layoffs down to a whole number of people"); kept literally.
- kp13 b2ba3f4ece4b (svg): 菱形約束讓權重積分變零 ("the weights' integral becomes zero"), 積分 is likely a typo; rendered "drives weights to zero".
- guide:14 cbe785adc131: says input noise ≈ weight decay "only under a first-order Taylor approximation"; the σ²‖∇ₓŷ‖² term comes from a second-order expansion.
- kp16 4ad68275f00a: the errors are called i.i.d. and also given pairwise covariance c (contradiction; independence means c = 0).
- kp16 de40d4213281: "variance drops to 1/k when c = 0"; by Eq. (64) it is s/k (the quiz and demo text say s/k).
- guide:16 e3539bf4f61e: test-time weight scaling is said to *be* the geometric mean of the subnetworks; it only approximates it (exact for special cases).
