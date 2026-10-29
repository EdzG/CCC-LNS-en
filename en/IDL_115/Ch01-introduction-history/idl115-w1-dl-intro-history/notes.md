# Notes: Ch01 condensed deck (idl115-w1-dl-intro-history.html)

The deck is bilingual. EN mode shows our translation of the **Chinese**; the professor's English
was used only as a reference. Below: places where his English and his Chinese disagree, or where
either is doubtful. `kpN` = the Nth `.section` of the page; the hex id is the strings.json key.

## Possible errors in the source

- kp20 `649a1dd6a970`: "77 years" from the perceptron to the Transformer does not add up
  (1958 → 2017 is 59 years; 1943 McCulloch–Pitts → 2020 would be 77). Translated as written.
- kp18 `fbc688b961e9`: the first neural-network winter is attributed to Minsky & Papert; their
  result concerns single-layer perceptrons, which neither language version says.

## Where our English departs from the professor's English (following the Chinese)

- kp1 c067177425b2: the English half leaves out the semester (115 學年度第 1 學期) and the Chinese half leaves out 'IDL115 · CSIE3544AB'; the en keeps both: '... · Academic Year 115, Semester 1'.
- kp2 996e68a6805d: the professor's 'how this course runs' / '30,000-foot view' is changed to follow the Chinese 怎麼玩 / 空拍鳥瞰圖: 'how this course works' / 'bird's-eye view'.
- kp2 76396607e9e3: the professor's 'basically magic and math at the same time' is changed to follow the Chinese 又像魔法又像數學: 'like magic and like math at the same time'.
- kp4 c3c5cf58e613: professor's 'Schedule' for 上課時間 changed to 'Class Time' (the Chinese means class meeting time).
- kp4 e7dc3400a87b: Chinese says 共 17 教學週 (17 teaching weeks in total); rendered as such.
- kp4 76a396cad907: professor's 'Semester: 115-1, starting 9/7 (Mon), ending with final exams the week of 12/28–12/31' reworded to follow the Chinese ('Fall semester of academic year 115: classes start on 9/7 (Mon), and 12/28–12/31 is the final exam week'). 115 is the ROC (Taiwan) year, i.e. 2026; no Gregorian gloss added.
- kp5 4924dac895d5: professor's 'Optimizers' changed to 'Optimization' to match 最佳化; 'Backprop' expanded to 'Backpropagation'.
- kp5 460f3ff4b0a9: Chinese 於課後線上觀看 = watched online after class; professor wrote 'afterward'.
- kp5 8c50336c8052: 'the whole schedule simply shifts by one week' changed to 'the rest of the schedule shifts back by one week' (Chinese: 後續進度整體順延一週, i.e. what follows is pushed later).
- kp6 e02e704d8aa5: professor's heading 'What You'll Be Able to Do' replaced with the literal 'Course Objectives' (課程目標).
- kp6 fd586b43566f: 'optimizers and regularizers' changed to 'optimization and regularization methods'; 'reason about training stability vs. generalization' changed to 'weigh training stability against generalization' (權衡).
- kp6 db22940b60fe: dropped 'all in' (Chinese is just 用 PyTorch).
- kp6 d548c6971249: 'Build' changed to 'Implement' (實作), 'judge their output quality' changed to 'evaluate the quality of what they generate' (評估生成品質).
- kp6 fb5bf6dad571: kept professor's '<strong>As a team</strong>' bold, although the Chinese half has no bold.
- kp7 26ad5940024e: 'Grading Breakdown' shortened to 'Grading' (評分方式).
- kp7 80a00037d605: 平時成績 means the regular coursework grade; written as 'Coursework (attendance & participation)', keeping the professor's description in parentheses.
- kp7 ac9eb5d92ea6, 75e17b1e3e82: '(Wk 9)' and '(Wk 17)' appear only in the English half and were kept.
- kp8 1c097ecfd483: the professor's English says 'Teams of 3–4', but the Chinese says 3–4 is the recommended size (建議) and that topics are chosen by interest (依興趣自訂). Followed the Chinese.
- kp8 d335ff3d92a1: 'a short write-up' in the English is 實驗報告 in the Chinese, so Wrote 'experiment report'.
- kp9 aa234b626466: the English says thinking must be 'visible in the repo'. The Chinese only says 你自己的思考過程必須看得見 (your own thinking process must be visible), so Dropped 'in the repo'.
- kp9 a749d4f2cd38: the English says 'not one giant final commit'. The Chinese says 不要一次性上傳完成品 (don't upload the finished product all at once), which is what Wrote.
- kp9 30523390d50f: the English is passive ('You may be asked'). The Chinese names the instructor as the one asking (教師可能隨機抽問), so Made it explicit.
- kp10 ebd609ba885f: the English says students watch each other's videos 'after grades close'. The Chinese says 課後自行上網 (online on their own time, after/outside class) and says nothing about grades. Followed the Chinese. The English also leaves out 'final-project' before presentations.
- kp10 d302cb81bd32: Translated e 學苑 as 'the e-course system' (the professor's term) and left the Chinese name out so no Han text stays visible.
- kp11 5059f354ea74: 'Quick FAQ' became just 'FAQ' (常見問題); 'quick' is not in the Chinese.
- kp13 1708063869c3: professor's English heading says "Loss Function" but the Chinese is 評分機制; translated as "Scoring Mechanism" (glossary term).
- kp13 9b825d59e777: professor's English says "Optimization" but the Chinese is 搜尋策略; translated as "Search Strategy" (glossary term).
- kp13 ded435869c5f: Chinese 不必然要「為真」 is softer than the professor's "doesn't have to be true"; used "doesn't necessarily have to be".
- kp13 2ff45e4b8ba0: professor's English adds the first name "Karl" Popper, which the Chinese doesn't have; followed the Chinese ("Popper's").
- kp15 d1dd9c805bfb: professor's "sort it" is vague for 分類標記 (label it into classes); followed the Chinese.
- kp17 d30e6c4d59ac: professor's title 'Clustering vs Dimension Reduction' changed to the standard 'Clustering vs. Dimensionality Reduction'.
- kp17 003a2cc0cfb8: professor's alt text says 'assigns the same points differently when the requested number of groups m changes'; rewritten from the Chinese ('different groupings of the same data depending on the specified number of clusters m').
- kp18 666d71a1af74: Chinese says 單層神經元 (single-layer neuron); professor wrote 'A single neuron'. Followed the Chinese.
- kp18 fbc688b961e9: Chinese says 'the first winter for neural networks'; professor wrote 'the first AI winter for neural nets'. Followed the Chinese. Historically, Minsky & Papert's result applies to single-layer perceptrons, which neither version says.
- kp19 51813b893a8f: professor's 'From One Neuron to a Universe of Them' does not match the Chinese (一整片神經網路 = a whole neural network). Translated as 'From One Neuron to an Entire Neural Network'.
- kp20 1557e9f3dfb7: his English says 'Deep Learning Boom'; the Chinese 全面爆發 means a full-blown explosion, not specifically deep learning, so Wrote 'From Winter to Full-Blown Boom'.
- kp20 821b14362b8d / 8e3f4fd5c55f / b471513c02f4 / 93102224c68a / 3e47691f1709 / 92f2fa89bcd7: each Chinese half is only a short tagline (DBN 復興, AlexNet 突破, 生成模型元年, 注意力時代, 擴散模型崛起, 對話式生成式 AI 普及), not a translation of the English title. Merged both into one English heading, e.g. '2014 · VAE & GAN: Year One of Generative Models'.
- kp20 d9cf81049938: his English says 'dominate instead'; the Chinese just says they became the mainstream. Followed the Chinese.
- kp20 698d8e95bffb: his English ('iterative denoising') leaves out the forward noising step that the Chinese describes (逐步加噪、再學習反向去噪). Translated the Chinese.
- kp21 5d2f2d781eaa: his English 'task-useful representations' drops 內部 (internal); Kept 'internal representations'.
- kp21 3ee37ad2683b: the <strong> markup differs between the halves; kept the English half's markup.
- kp23 70364cb66997: the unit is laid out oddly as 'False. | 錯。English | Chinese'. Output one clean English answer. The Chinese 一律 and 不受理補交 are stronger than his 'with no late exceptions'.
- kp23 aa52db94ea7e: his English says 'to get an extension'; the Chinese 要求延期補交 means asking to submit late. Wrote 'ask to submit it late'.
- kp23 f722a8f1a7f8: his English adds 'after decades of AI winter', which is not in the Chinese. Followed the Chinese and dropped it.
- kp23 d03bb49c4282: his English uses 'generalize better', but the Chinese is about average performance over all problems. Followed the Chinese.

## Not translated

- The nav dots' `aria-label` ("跳至第N章節") is set by the page's script at runtime; the engine only
  translates script-written text, not attributes. Screen-reader only.
- Formulas that appear in both halves of a bilingual block are kept once in English.

## Redrawn images (`assets/`)

Only two of the deck's five PNGs have Chinese text; the other three (neuron scaling, traditional
vs. deep, vectors) are already English-only and are shown as they are.

- `idl115-w1-learning-frameworks-imagegen.png`: the original's English labels match its Chinese,
  so the redraw only drops the "| 中文" halves. "representation / grouping" (表徵／分群) keeps
  "grouping" rather than the glossary's "clustering", because the box below already says
  "clusters" (群集).
- `idl115-w1-clustering-vs-dim-reduction.png` (Chinese only in the original): points are
  regenerated from formulas, not copied. The original's m = 5 panel shows six colors (an artifact
  of the AI image); the redraw shows exactly five clusters. Fonts and box positions are close,
  not exact.
