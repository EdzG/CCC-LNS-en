# Notes: Ch03 lecture page (Ch03-backprop-optimization)

`kpN` = knowledge point N, `guide:N` its 教授祕笈 box; hex ids are strings.json keys.

## Translation choices and limitations

- Demo readouts and canvas labels are translated through `_runtime` (14 exact, 18 patterns); `#kp5-ro` and `#kp7-ro` start with static text but are rewritten by the demos, so all `.demo-readout` are `_dynamic`.
- Canvas label 橫軸 w is shortened to "axis w" so it fits the canvas edge.
- English-only blocks (9) stand alone and read correctly (the TOC title, quiz options like "Cauchy，1874" with a full-width comma, table cells such as "Vanilla SAM").
- The 祕笈 badge on guide buttons is "Notes" (the button itself says "Professor's Secret Notes: …").

## Errors and unclear points in the Chinese (translated faithfully)

- guide:1 a4fecbc76ddd (guide 1): says the §2 gradient-descent foundation is "KP-2 to KP-4", but §2.4 Momentum is KP5 in the TOC, so it should be KP-2 to KP-5.
- kp4 ace38a5af121 / a0d77fa42115: the Armijo rule is called "also known as backtracking line search". Strictly, Armijo is the sufficient-decrease condition usually paired with backtracking, not a synonym for it.
- kp4 f192bf1848fc: 「深度學習實務較少用固定學習率或自適應方法代替」 is garbled (literally: rarely uses fixed or adaptive rates). Translated the intended meaning: deep learning uses line search less, and fixed or adaptive learning rates instead.
- guide:4 684127ed9f0c / adbac92c3da6 / f690fa308166: descent is said to be guaranteed for η < 1/L, but the worked example accepts η = 0.5 = 1/L. The condition is sufficient, not necessary; minor imprecision.
- kp5 047d4cbbd3ba, eecee1b36946, 7b543540f9ac, 90a8656df687, 099736f9090c: momentum is credited to Rumelhart et al. as its first proposers; historically it is Polyak's heavy-ball method (1964), popularized for neural networks by Rumelhart, Hinton and Williams (1986). The KP5 quiz's correct answer depends on this attribution.
- kp5 c563bb89f5ea vs e64862b22191: the body points to "§5" for RMSProp/Adam, the guide to KP-11; the cross-references disagree.
- kp6 5b506b885289 and others: "activation function σ_i" while the demo (448c8d69a798) and guide use σ(a)=a², a toy activation for easy arithmetic. Unusual, not wrong.
- kp8 56cbfa4ededd: cites Eq. (31) for "convergence rate approaches full-batch", but KP8 only shows Eqs. (23)–(30).
- kp8 9e969fb574b2 / 4dceed7c078d: one rate O(1/t + ||e_t||²) is given for "non-convex or convex" f without saying which quantity converges at that rate (for non-convex f usually a gradient-norm bound).
- kp9 8ccea5592474 (KP9 quiz): the source has a literal carriage return where `\r` should be in `$t \rightarrow \infty$` (index.html ~line 1702), so the browser sees `$t \nightarrow \infty$` and the formula renders broken in both languages. Math kept byte-identical.
- kp11 65c707bc658d, f6a6a18708d3 (correct quiz option): Adam's second moment is called a "variance" estimate; it is the uncentered second moment (running mean of g²).
- kp11 a31220ea4c04 vs 0665bcbb2771, 6af1521d9a8c, 57762e0c34e6: $v$ is defined as a scalar ($\|\nabla f_i\|^2$), yet $\sqrt{\hat v}$ is said to adjust the step "per dimension", which only holds for element-wise Adam.
- guide:11 0543288664e6: "squashed by a full factor of three"; the actual ratio is 1/0.316 ≈ 3.16.
- guide:11 141bdb02ef44: the exercise uses uncorrected $m=0.58$ at $k=2$, unrelated to the guide's running example ($g=4$ gives $m=0.76$); may confuse.
- kp12 4df2f25d40b7, d07b9a6d0ac6: reference [20] is cited both for the empirical flat-minima study and as the SAM paper; possible citation mix-up.
- kp13 6891657f6a77 (expl): "a unit direction vector along the gradient, of length ρ, multiplied by ρ" is self-contradictory (a unit vector has length 1); probably means the unit gradient direction scaled by ρ.
- kp13 06928ee22277, 6985846293aa: "Eq. (52) is an upper bound on the error rather than an exact bound" is vague (upper bound on what?).
- guide:14 9583d86a394a (guide 14): continues from KP-13 with ε* = (0.06, 0.08, 0.10, 0.12) for four weights, but KP-13's example ε* is two-dimensional, (0.06, 0.08).
- kp14 c2ad71eeb5c6: the unbiasedness argument mentions only E[m_i] = β and omits the 1/β factor of Eq. (54) that makes the expectation work (the guide and fd69bd3df400 include it).
- kp16 cfe15fe47a7e (expl): the source uses Markdown `**訓練**`, which shows as literal asterisks; kept as `**training**`.
- guide:15 e5e2f0830d9b (guide): 1.2e-3 vs 9e-4 are said to "differ in the fourth decimal place"; 0.0012 and 0.0009 first differ in the third.
- kp15 6240dfec2882 (expl): iteration count said to depend "logarithmically on log(ε⁻¹)", double-counting the log; it should be logarithmic in ε⁻¹ (linear in log ε⁻¹).
- kp15 5c5b5493bee4 (Prop 5): no width/separation condition before "Then:"; the guide states δ > 0 explicitly, the page only later.
