# Notes: Ch02 lecture page (Ch02-perceptron-mlp)

`kpN` = knowledge point N, `guide:N` its 教授祕笈 box; hex ids are strings.json keys.

## Known limitations

- Demos kp4 and kp8 redraw their canvases only when you click their buttons, so after a language switch their canvas labels stay in the previous language until you click (same limitation as Ch01 KP6). Readouts and all other text switch immediately.

## Errors and unclear points in the Chinese (translated faithfully), and translation choices

- kp0 e89ad055c1f2, c6e9682972b5, a2aa7c70004e: TOC entries contain leftover generator text 'kpN (badge X.Y)' duplicating the section number; kept as-is.
- kp1 guide a2b5ffd42d83: 'KP4: how the perceptron update rule is written', but the TOC puts the update rule and its derivations in kp5 (2.5); KP4 (2.3-2.4) only introduces the perceptron. Likely should be KP5.
- kp1 guide 0af9bbd5477d: says a deep enough stack can approximate 'any smooth function', while elsewhere the page says 'a broad class of functions'; the UAT is about continuous functions on compact sets (and is about width, not stacking height). Translated faithfully.
- kp1 guide b86ee5cff205: 'about 5 times more parameters' for 3 -> 17 (actually ~5.7x); acceptable rounding.
- kp2 25fd09fe40bc: demo instructions say watch whether z is ≥ θ, but the same block's correctness check (and the Principle block 55482816dc97) define firing as z > θ; translated faithfully.
- kp2 70888b6455f1: guide example uses 12 ≥ 10 ⇒ fire, inconsistent with the strict z > θ firing rule used elsewhere in KP2 (harmless here since 12 > 10).
- kp2 70888b6455f1 / 719147a2aca7: Chinese words 放電（fire） and 靜默（沉默） sit bare inside $$...$$ (not in \text{}); EN wraps them as \text{fire} / \text{silent} so they render upright; the rest of the math is unchanged.
- kp3 f1f4361e26a1 / 5f59b51b2ae6: Eq. (1) definitions (from the textbook's general neuron) say inputs x_i ∈ R and 'learnable' weights, contradicting the same section's statement that M-P has binary inputs and fixed, non-learned weights; translated faithfully.
- kp3 bea2efcae5ab vs 9881ae007bde: text says M-P activates when the sum 'exceeds' the threshold, but the guide's AND example with θ=2 and w=1 only works if the rule is sum ≥ θ (1+1=2 must fire).
- kp4 7184001715e5: calls Frank Rosenblatt a 生理學家 (physiologist); he was a psychologist. Translated faithfully as 'physiologist'.
- kp4 453b93879e13: says the signum form of the update simplifies to $2\eta y_{i}\boldsymbol{x}_{i}$; this holds only for misclassified samples (it is 0 when correct). This is not stated here, but likely covered in KP5.
- kp5 6a6137de275f: guide says 'we want the misclassified points to be as far from the line as possible' (我們想讓誤分點離線越遠越好); the objective is to maximize the signed distance of correctly classified points / minimize the (negated) distance of misclassified points, so this phrasing is inverted or at least misleading. Translated faithfully.
- kp5 3b1e2077d3c1: quiz explanation says the two gradients 'go up and down and exactly cancel out' (一升一降剛好抵消); nothing cancels: the minus sign in the error definition makes descent on -distance equal ascent on distance. Translated faithfully.
- kp5 f333127f8b97: the door-hinge analogy is confused (wanting 'door gaps of misclassified points' to exceed a safe width; 'reduce the error of being flush against the door' is unclear). Translated faithfully.
- kp5 ce2229d17e08 / 61c442597979: section text says maximize distance of correctly classified points and minimize distance of misclassified points, but then defines error as -1 times the correct points' distance; the sum in both should be over the relevant (misclassified) set, which the page only states afterwards (393161ef3d7b).
- kp5 1f8c89d04c40: Eq. 12 d = w^T(x − x0) = w^T x + w0 holds as signed distance only when ||w||=1 (stated); Eq. 14 d>=0 only for correctly classified points (stated). OK, just noting the unit-vector assumption is dropped later in the hand computation ab199573f455 (w=(2,1) is not unit, so d=5 is the unnormalized value, true distance is 5/sqrt(5)).
- kp6 4aaef2d056ae / kp7 b571d07217b4: the h3 headings literally contain an authoring leftover prefix 'kp6 (badge 2.6)' / 'kp7 (badge 2.7.1–2.7.2)' (also in the TOC). Kept as-is in English.
- kp6 245f495dc4ef: says the perceptron suits multilayer networks 'because it has a non-linear activation'; the step/sign activation is non-differentiable and is not what MLPs trained by backprop use. Translated faithfully.
- kp6 7c8da7584154 (guide): says ADALINE 'tries to keep the line centered, at a distance from both sides'. That describes max-margin (SVM); ADALINE/LMS minimizes squared error and does not explicitly maximize the margin. Translated faithfully.
- kp6 99e65acb3cfc: says XOR's two classes are +1 and −1, while the demo and guide label them 0/1. Minor inconsistency; translated faithfully.
- kp7 e810319e5bd3: says Rosenblatt proposed the MLP in 1958 'in the same paper as the perceptron'. Historically questionable (multilayer perceptrons are usually credited to Rosenblatt's 1962 book). Translated faithfully.
- kp7 0fe8aff4c1ce / 5296e03730f9 / quiz 8aaa0754f5d9: claims the input layer is 'usually counted as one of the hidden layers'. This is not the usual convention (the input layer is normally not called hidden, and is often not counted as a layer). Translated faithfully.
- kp7 d54af5704ac8: defines hidden layers as 'the intermediate layers other than the output layer', which taken literally would include the input layer (consistent with the claim above, but nonstandard).
- kp7 8bad421bee58 / dabd7c8584c6 vs acd31c403956: Eq. 17 sums weights times inputs with no bias term, but the guide's parameter count adds one bias per neuron. Minor inconsistency.
- kp8 a55286946c21/e066726993bb/88fa93e33a8d: 行空間 translated as 'column space' (Taiwan usage); strictly W_i^T x gives coordinates along the columns of W_i (projection onto its column space up to that basis), not the projected vector itself.
- kp8 95dde93d03c9/08ad21b3845f/39725aa323d6: V_i := sigma_i W_i^T treats the linear activation sigma_i as a matrix; with that definition y = V_3 V_2 V_1 x, so writing y = V_3^T V_2^T V_1^T x and V = V_1 V_2 V_3 (Eq. 20/21) mixes transposed and untransposed conventions (it is consistent only if V_i := W_i sigma_i^T). Translated as written.
- kp8 b0b2c8595528: demo lists W1 as 4x2, W2 3x4, W3 1x3 (i.e. W_i applied as W_i x), yet the formula and caption use W_i^T x; and 'collapsed V' is shown as 2x1 while the guide (80a064e44b35) says 1x2. The readout's M = W3 W2 W1 (9d3ddd8c6381) also differs in order from V = V1 V2 V3.
- kp8 80a064e44b35: says V = V1V2V3 has dimensions (1x3)(3x4)(4x2) = 1x2, but that product is V3 V2 V1; V1 V2 V3 with the stated shapes (4x2)(3x4)(1x3) is not even defined.
- kp8 46e4e5c58998: labels '$z_1=V_1 x$' as Eq. (20), but Eq. (20) elsewhere is y = V_3^T V_2^T V_1^T x = V^T x.
- kp8 e9438b122bac: the second misconception ('collapse is bad so all-linear is useless') is answered with 對 ('right') followed by a rebuttal; likely meant 不對/不全對 ('not quite'). Translated faithfully as 'right'.
- kp9 3f7d2acd2ac6/536f5c445a25: Binary Step range given as [0,1], but the output is only {0,1} (the guide 38febe7b18eb says {0,1}).
- kp9 459c54fa1bf8: Sign range given as [-1,1] and outputs 'only -1 or 1', while guide 38febe7b18eb says {-1,0,1}; inconsistent about sign(0).
- kp9 b53adab23536/ae1c8973716a: sigmoid range written as [0,1]; strictly it is (0,1) (guide 5ce1f14f62f6 says (0,1)). Similarly tanh [-1,1] vs (-1,1).
- kp9 2ebc6ad2e79e/193d4407a7d0: Softplus range written as [0,inf) while saying 'output always positive'; guide 5ce1f14f62f6 says (0,inf). Guide also lists Softplus under the 'S-shaped bounded' drawer although it is unbounded.
- kp9 8b51213f8280: softmax formula reuses i as both the output index and the summation index: e^{a_i}/sum_{i=1}^m e^{a_i} (should be sum over j or k).
- kp9 5c3978cda923: maxout formula sigma_i(a)=max_j(sigma_j) is unclear (max over sigma_j rather than over linear pieces). Page files maxout under 'cross-layer', but 13de2fff1f10 says softmax is 'the only cross-layer activation', and guide b4aa1f3336be puts Maxout in the ReLU/piecewise-linear family.
- kp9 5f4a0ef6def5 vs 28269e826b6f: guide speaks of three drawers but the summary says four broad classes (basic + S-shaped + piecewise + cross-layer).
- kp9 34cce9699c1d: 'σ(a) vs a — Linear 線性 (22)' is a chart title the demo likely rewrites when the dropdown changes; may need a _runtime entry (pattern on the option labels). Translated the dropdown option names without the redundant Chinese gloss, e.g. 'Linear  (22)', keeping the double spaces.
- kp10 6e3d6fb11384: says the hinge loss is 0 when |f_o| >= m; the correct condition is y_i f_o(x_i) >= m (a confidently wrong prediction with large |f_o| has a large loss). Translated as written.
- kp10 863cdc238fb1 (guide): says Hinge does not fine you 'if you made a mistake but still kept a safe distance'; actually hinge gives zero loss only for correct predictions beyond the margin. Translated as written.
- kp10 470d83e55ba2 (guide): opens with 「越準越要用力罰」 ('the more accurate, the harder you should penalize'), which seems to mean 'the bigger the error, the harder the penalty'. Translated literally.
- kp11 f60c6ef8e9b0 (guide): 「梯度假全 0」 looks like a typo for 「梯度就全 0」; translated as 'the gradient is then all 0'.
- kp11 5a2450581201 (guide): says ∂e/∂w_j 'is negative'; it carries a leading minus sign but its value can be either sign. Translated as written.
- kp11 b6baa631ef8e (guide): the condition $|r|<=δ$ comes after the formula in the English word order; math kept byte for byte, only reordered.
- kp12 b55b34608c0d / 9fedb3a3a005 (quiz expl): Newton update (57) is written as beta - (XWX^T)^{-1} X(y-p). Since the Hessian of the log-posterior is -XWX^T and the gradient is X(y-p), Newton ascent is beta + (XWX^T)^{-1} X(y-p); the minus sign is wrong (the guide's worked example cef3f50355db uses the correct sign implicitly). Translated faithfully. The expl also drops the (tau) superscript on the right-hand beta.
- kp12 a07f9c88a4ca (svg): says the log-posterior is convex; it is concave (the guide 39be1a17a2df correctly says concave). Translated faithfully as 'convex'.
- kp12 731434710c4d: source math contains '\\beta' (doubled backslash) in the denominator, a typo that renders as a line break + 'beta'. Kept byte for byte.
- kp12 bccf1d217932: mismatched parentheses '（48)(49)' in the source; rendered as (48)(49).
- kp12 774565cd3885 / bccf1d217932: the product prod p_i^{y_i}(1-p_i)^{1-y_i} is called the 'posterior' of the data (following the textbook); it is really the likelihood of the labels given beta. Translated as 'posterior'.
- kp12 c7a15f5cb3da: '貝氏定式' is likely a typo for '貝氏定理'; translated as Bayes' theorem.
- kp12 8c2febd9114d: 'then Bayes is used to derive the probability' is loose: logistic regression models the posterior directly rather than deriving it via Bayes. Translated faithfully.
- kp13 9f2d394c2497: calls the RBF output a 'weighted average' (加權平均) of the basis functions, but Eq. (61) is a weighted sum (weights are not normalized). Translated faithfully.
- kp13 81393e5a4f06 / 2e8a214504fe: winner rule written as sum_i ||x_i - w_ij||_2 (sum of norms of scalars = L1 distance), while the guide and SVG call it the closest prototype / argmin ||x - w_j||. Follows the source textbook's notation; kept as is.
- kp13 623a846dbbf0: Phi Phi^T is described as 分塊三角 (block triangular); it is actually block diagonal. Numbers checked: inverse, Phi Y^T and W ~ [1.33, -0.67, -1] are all correct. Translated as 'block triangular'.
- kp13 cf15f3c974b0: says the sigmoid goes 'from probability funnel to RBF bell', but the logistic/sigmoid basis is S-shaped, not bell-shaped (the bell is the Gaussian). Translated faithfully.
- kp13 221c28e48b8e: guide header cites Eqs. (59)-(65), while the guide body also uses (67)-(70); minor.
- kp14 ec8bcdd2e1a8: says the UAT establishes that neural networks can 'represent' any continuous function; the theorem only gives approximation to arbitrary precision on a compact domain (e.g. [0,1]^n), not exact representation of arbitrary continuous functions. Translated faithfully.
- kp14 d05dbc3b676d / 348c3615077f: the stated hypotheses (continuous, bounded, non-constant) match Hornik (1991); the Hahn-Banach/Riesz/'separates measures' sketch is Cybenko's (1989) argument, where Step 4's claim that such sigma is automatically 'discriminatory' is the nontrivial lemma, stated without justification here. Translated faithfully.

## Images

- The 17 `assets/orig-*.jpg` figures are English textbook crops; nothing to redraw.
