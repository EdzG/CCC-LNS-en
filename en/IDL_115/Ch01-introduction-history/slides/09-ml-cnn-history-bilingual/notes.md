# Notes: Ch01 slide 09 (09-ml-cnn-history-bilingual.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- Typos read as intended: 誊號 → 訊號 (kp6), 欸歸不動 → 學不動 (kp6), 紂凍 → 解凍 (kp7), 樫空出世 → 橫空出世 (kp8, kp10), 需花 → 雪花 and 生成形模 → 生成模型 (kp9), 拉據 → 拉鋸 (kp12), 攪平 → 攤平 (kp10, kp11, quiz), CNN 興生成流形 → CNN 與生成流形 (kp0).
- kp7 `8d2db5b39a08`: a display formula has Chinese directly in math mode (`$$單層 RBM 逐層無監督預訓練 \to …$$`); our English wraps it in `\text{}`.
- kp4 `3aae12d1de22`: LeNet is dated 1989 (LeNet-5 is usually 1998; the 1989 net was its precursor). Translated as written.
- Runtime: 攪平 ('stir flat') in a quiz answer is almost certainly a typo for 攤平 (flatten), used everywhere else; translated as 'flatten'.

## Where our English departs from the professor's English, and other choices

- kp0 87099ee251cf: 'CNN 興生成流形' looks like a typo for 'CNN 與生成流形' (CNN and the generative manifold); translated as such and the professor's English line dropped.
- kp3 fd617708095e: the professor's English 'no data' drops 'no compute' (無算力資料 = no compute or data); followed the Chinese.
- kp3 31f2987ef421: 'GAN 對抗互傷害' (adversarial mutual harm) is casual; rendered as two networks fighting and hurting each other.
- kp4 c6c91a4a69c0: $W$ and $X$ appear in both halves; kept once each (Chinese half only).
- kp4 a8a58abb974e: 'Vision Transformer 的對手' is odd: CNNs are the rival of ViT, not ResNet's rival; translated literally as 'the rivals of the Vision Transformer'.
- kp4 6ba74f208ebe: 'apart by 4900 positions' is given without stating the image size; translated faithfully.
- kp4 3aae12d1de22: LeNet-5 is usually dated 1998 (LeCun's 1989 net was a precursor); translated the 1989 date faithfully.
- kp5 eb58cf991fec / 6e8b8e85588c: these caption a matplotlib chart embedded as a base64 data: URI, so _images (which matches by filename) cannot swap it. If the chart has Chinese labels, it needs another approach.
- kp5 9b22692fac97 etc.: the professor's English halves were telegraphic ('Flatten breaks; sliding preserves'); the translation follows the fuller Chinese. kp5 8033cde110d4 and kp9 5620d41764fc keep the English-only inner span, because it has no separate Chinese counterpart ('(map ≥ thr → 1)', 'Add Noise, Denoise').
- kp5 20532b4eaf17: the static text matches the existing _runtime pattern ('$1/9 high-score cells lit').
- kp6 3a1170246b8f, 12db3baad3c3: typo 誊號 in the source, read as 訊號 (signal).
- kp6 d71d1809e53a: typo 欸歸不動, read as 學不動 (can't learn), matching the SVG label 前層學不動.
- kp6 0b49d242bd04: the professor's English 'Deep won't learn' leaves out the data shortage (沒算力資料); the translation includes it.
- kp7 8d2db5b39a08: the display formula has Chinese written directly in math mode outside \text{} ($$單層 RBM 逐層無監督預訓練 \to \text{Backprop 微調}$$). To keep the output Chinese-free, the left side was wrapped in \text{...} and translated: $$\text{Single-layer RBM unsupervised layer-wise pretraining} \to \text{Backprop fine-tuning}$$. The math segment therefore differs from zh by design.
- kp7 861f39488f28: typo 紂凍, read as 解凍 (thaw).
- kp8 77cfb6e1035a: typo 樫空出世, read as 橫空出世 (burst onto the scene).
- kp9 e72034ccc44a, 7736c40ba494: typo 需花, read as 雪花 (snow); 生成形模 read as 生成模型 (generative models).
- kp9 adf2dab8fc8f: 給雪花變名畫 read as 將雪花變名畫 (turn snow into a masterpiece).
- kp9 8e0601170727: the tag says 生成流形 (generative manifolds), but the section covers GANs and diffusion, not manifolds; translated literally as 'Generative Manifolds'.
- kp10 c9072478de12: Chinese has a typo 樫空出世 for 橫空出世 ('burst onto the scene'); translated as intended. Professor's English 'Ignites deep learning.' drops the 'bursts onto the scene at ImageNet' half.
- kp10 52ca167e4ddf, kp11 89b6bf845c3b etc.: the page writes 攪平 (lit. 'stir flat') where the TOC/subtitle uses 攤平 ('flatten'); both translated as 'flatten'.
- kp10/kp11/kp12: the professor's English halves are telegraphic fragments ('Deep hard; SVM wins.', 'Why flatten destroys?', 'Vary thr/filter, watch map.', 'AlexNet trio?'); replaced with full translations from the Chinese.
- kp10 c35fd278a65e: 'SVM 以核一刀切主流' is a pun (kernel cuts cleanly / SVM cuts into the mainstream); rendered as SVMs with kernels that cut cleanly in one stroke taking over the mainstream.
- kp10 b9d3d84315ff: 雪花還原術 refers to diffusion restoring an image from 'snow' (noise); kept the snow metaphor.
- kp12 15fb818bcc6f: Chinese typo 拉據 for 拉鋸 (tug-of-war); translated as intended.

## Images

- Inline image #00: NO-CHINESE: no Chinese in the image (title "Flattened  (silly) — 16-D vector loses geometry" has a double space where a Chinese word, probably 大笨蛋, was dropped upstream; the "horizontal detector" label overlaps the "Filter W 2×2" title in the original)
- No redraw needed: the inline images have no Chinese text.
