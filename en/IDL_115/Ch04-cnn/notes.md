# Notes: Ch04 lecture page (Ch04-cnn)

`kpN` = knowledge point N, `guide:N` its 教授祕笈 box; hex ids are strings.json keys.

## Translation choices and limitations

- Demo readouts and canvas labels are translated through `_runtime` (14 exact, 17 patterns).
- Canvas labels shortened to fit: 輸入 4×4（四色 = 不重疊窗）→ "input 4×4 (color = window)"; the KP5 bar-chart footnote → "Bars scale linearly to the larger value; numbers are exact integers."
- English-only blocks (13) stand alone and read correctly (quiz options like "Yann LeCun，1998" with a full-width comma, "Max pooling" buttons and options).
- 特徵向量 is "eigenvector" in the KP11 PCA-initialization context (the glossary's "feature vector" is for other contexts).
- The 祕笈 badge on guide buttons is "Notes" (the button itself says "Professor's Secret Notes: …").

## Errors and unclear points in the Chinese (translated faithfully)

- kp2 b8f1a16fff5d / 8b4c2a3179af / 98668ac3dbfa: LeNet input described as 28×28 with the first conv also giving 28×28×6; original LeNet-5 input is 32×32 (5×5 valid conv → 28×28). As written, 28→28 would need "same" padding, which the page never mentions.
- kp0 e9b50d583739: the TOC says 平移等價性 while the body says 平移等變性; both translated as "translation equivariance".
- guide:3 1cd09d0d41cf (guide 3): the exercise patch [[2,2,2],[2,2,2],[0,0,0]] is called "the same structure as the table above with dark and bright swapped"; the exact swap would be [[2,2,2],[1,1,1],[0,0,0]]. The answer (+6 vs −6) still holds; loose wording.
- kp4 ff6c8f5efa26 (KP4 demo): 「改 K 的對角線等價於抽「同位元素」」 is vague; translated literally.
- kp6 8dc4af72fc4f / 92aad3a2d7f4 / 8f7df7e20517 / cf7a13877d0d / 849639ffdb85: the page (after the textbook) calls the property "translation equivalence", giving "equivariance" as an alternative; the standard term is equivariance. Where the page gives its own English it is kept; elsewhere "equivariance" is used.
- kp5 1dc58ea7ea71: 「稀疏權重矩陣的秩通常也比全連接來得低」: sparsity does not imply low rank; loose claim.
- guide:6 a6c9e0f0735b: 「第二列幾乎就是第一列往右塞了一個 0」: the second feature map is the first shifted right with a 0 entering on the left and the last value dropped; loose wording.
- kp8 48c1f5d0c68a, table 320635781ee7, SVG/quiz dc905b9eb55a / 787a29c2ac06: median pooling is given as [[2, 5.5],[5, 1.5]], but the top-right window {7,5,2,4} has median 4.5. Guide 2 (9fd655703a3a, 112fb168662e) itself gives 4.5 and calls 5.5 an error ("adding 4 and 7"), so the page and its guide disagree.
- guide:8 d5c48529567c: "中間那格" (the middle cell) is given as max(1,7,3,2)=7, which is the top-middle window; the true centre cell of the 3×3 output is max(3,2,-1,-5)=3. Ambiguous wording.
- kp8 7bb9e15475c9, d5c48529567c: with one ring of zero padding (6×6) and 2×2/stride-2 max pooling, the top-left output is max(0,0,0,2)=2, but the quoted result [[3,7,5],[8,6,6],[7,6,6]] starts with 3. Not reproducible from the stated padding (probably inherited from the textbook example).
- kp10 7df3bce26893 (KP10): says 「高密度時」 ("in high density") no method can do well everywhere; the guide (47979d62fb49) says 「高維裡」 ("in high dimensions"), the usual statement of betting on sparsity. Probably a slip in the body; translated literally.
- guide:9 3f2a98a9c1d9 (guide): equivariance and invariance are said to point in "opposite directions"; invariance is really the special case of equivariance where the output transform is the identity.
- kp11 09a013838ac8 / 4062e24f000c / 715ebc91e290 / 8420ad520e6a: PCA initialization ties the patch size to the kernel *stride* $s$ (「與核步幅 $s$ 對應的 patch」, 「步幅 $s=5$ 的核」); kernel *size* is the natural reading. PCA on flattened $s\times s$ patches gives eigenvectors of length $s^2$, each reshaped into a kernel, not one "$s\times s$ eigenvector matrix" (0fb1041ad114, 89f9f2ac988e). "Cut a layer's weights into patches" is also odd: the patches come from the input data.
- guide:11 13f3ab1ccddb: "σ=1 is 16× too large … five layers ≈ 16⁵" multiplies standard-deviation ratios; fine as a std scale, but the variance ratio is 16² per layer.
- guide:12 e87fe184a2a0 / 0a3f431c6d90 / 375f95190def: Eq. (8) minimizes $-\mathbb{P}$ rather than $-\log\mathbb{P}$ (as in the source book); the AlexNet paper uses the log-probability.
- guide:14 1f176ab6572e: the KP-12 link says "the name honors LeNet", but LeNet is KP-2 (ac86d49c39b9); KP-12 is AlexNet/ILSVRC. Loose cross-reference.
- guide:14 f25b653e38fd: "1×1 is an order of magnitude cheaper" compares C_in×C_mid with 5×5×C_in×C_out (different output widths): a rough comparison, not like for like.
- kp16 e6f33770bb0e, 02c14c91d8ac: an l-layer DenseNet is said to have l(l+1)/2 "weight matrices"; the DenseNet paper counts l(l+1)/2 direct connections (the guide 05fa46378f24 says "connections").
- kp15 8972064251f8: the quiz option repeats its English after the Chinese (「反卷積／轉置卷積（deconvolution / transpose conv）」), so the English option is slightly redundant.
