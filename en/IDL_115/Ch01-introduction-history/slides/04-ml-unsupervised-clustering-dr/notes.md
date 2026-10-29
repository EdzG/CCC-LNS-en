# Notes: Ch01 slide 04 (04-ml-unsupervised-clustering-dr.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- Unescaped `<` in `$p<d$` (several places): the browser parses `<d$…` as a tag. In 中 mode kp1 `b2b01a0d832f` and kp15 `369d13d6c5e3` lose part of their text, and the English-only Eq. 7 box in kp9 (`$$f_\theta: \mathbb{R}^d \to \mathbb{R}^p \quad (p`) shows raw, broken TeX in both modes (it has no Chinese, so it is not a unit and stays broken). Our English writes `$p&lt;d$`, which renders correctly.
- kp10 `f479818f32fb` / `cc19705ccb9e` vs kp15 `3a0a50942c2b`: the two clumps are at scores 5 and 16 in one place and 3.5 vs 16.0 in another; and `ba71bbf115b9` says red ends low and blue high while `f479818f32fb` says blue is at 5 and warm at 16. Translated as written.

## Where our English departs from the professor's English, and other choices

- kp1 b2b01a0d832f: the zh innerHTML is browser-mangled because the source has a raw '<' in $p<d$ (parsed as a tag '<d$<'). Markup kept byte for byte and only 找結構 -> 'find structure' changed; if a math checker treats '$< span=""> · <span>找結構</span></d$' as a segment, that segment changes by design. The page renders this unit garbled in both modes (upstream issue).
- kp1 6e3036e5ae68: the professor's English subtitle ('Unsupervised: Find Structure Without Labels') is not a translation of the Chinese title (把大笨蛋變聰明的幾何遊戲); kept it as the subtitle and translated the Chinese title above it.
- kp1 02f0763f8dbe: dropped the duplicate '(Scroll · self-study)' span; 中英雙語 Bilingual -> 'Chinese–English Bilingual'.
- kp2 df896393bc2d: dropped the duplicate 'No labels — how to learn?' from <small>, kept the bilingual-en span (no Chinese counterpart).
- kp2 1a17f725c072 / kp3 7e41640fb903, 65a5f64803ca, 935d7153e55f, a812a5e519b8: professor's English spans were terse summaries ('Drop novice in night market: group by look, compress by geometry.'); translated fully from the Chinese and dropped the spans.
- kp3 fd90ad403208, kp4 c99c0abc75c0: h2.section-title with <span class="en"> styles that span as a small italic subtitle, so the English title is written as plain h2 text (span dropped) rather than kept inside the span.
- kp4 2523d0752a24: zh contains $\mathbf{x}$ twice (Chinese half and English span); en keeps it once.
- kp4 bd84e2dceefd, ca579eb061db: dropped the '(Supervised)'/'(Unsupervised)' inline spans as duplicates.
- kp5 aacf803b44ec: professor's '(Grind)' is an unidiomatic label for 學霸; used 'Bookworms'. Same group called 'grind' in kp7 c2e366609dec; translated as 'bookworms' there too.
- kp5 7ae4f3bdc346: professor's English 'gaming hrs' drops that 電動間 is a place (arcade); followed the Chinese.
- kp6 44fc90c49f8a: professor's English title adds '— Eq.6', which the Chinese title lacks; dropped it (the next unit already says Eq.6).
- kp6 742fbb0b1948: professor's English ('Assign each x to a box ℓ_i', with math) differs from the Chinese, which has no math; followed the Chinese, so the English-only math segments were dropped.
- kp6/kp7/kp8/kp9: several professor's English lines are compressed summaries ('Blank paper, self-find.', 'Formula same; supervision differs.', 'm=2 coarse, m=5 fine.', 'Left: 2 ellipses; right: 5 mini-clusters.', 'Compress big vector to small embedding.', 'High-dim in, low-dim out.') that omit parts of the Chinese; translated the full Chinese.
- kp9 cb82ff8e52fc: in the source, the unescaped '<' in $p<d$ is parsed by the browser as a start tag ('<d$」。<span ...>'), so the captured zh innerHTML is mangled and the bilingual-en span ('High-dim in, low-dim out.') is swallowed. In en I wrote $p&lt;d$ (the textContent KaTeX sees is still $p<d$); writing a literal '<' would be eaten by the parser again. The math-segment check will flag $p<d$ vs $p&lt;d$ for this key: this is intentional.
- kp10 f479818f32fb: says 'score $y=5$ blue vs $16$ warm' while ba71bbf115b9 says 'red low, blue high'. The color mapping is inconsistent in the Chinese; translated faithfully.
- kp10 cc19705ccb9e: 低溫/高溫 (low/high temperature) refers to cool/warm colors, so it is rendered as 'a cool one at a score of 5 and a warm one at a score of 16'. His English '10 gray balls in [5,10] → tight 5 vs 16' left [5,10] outside math; the en keeps the zh `$[5,10]$`.
- kp10 93607486eb3e: his title 'Push Apart, Tighten' became 'Push Apart, Pull Together' (拉開、揉緊), to match the card titles.
- kp13 f761404608c0/ffda38709ace: the inline '(Eq.6)'/'(Eq.7)' spans have no Chinese, so they are kept as-is.
- kp15 369d13d6c5e3: upstream source bug. The raw HTML has an unescaped `$p<d$`, so the browser parses `<d$）在演示中…` as a bogus element. The live page shows only “Q3. 降維 $f…$（$p” followed by the English, and the rest of the Chinese question is swallowed. The zh innerHTML is mangled for the same reason. The en writes the full question with `$p&lt;d$` (it renders as p<d in MathJax). The `$p<d$` segment is therefore deliberately not byte-identical; the other math segment is kept.
- kp15 99d91f02309d/74be9180b124/692ad3e8b84d/e2fb0ae6422c etc.: the professor's inline English for the options is just terse keywords ('swapped', 'miscalc.', 'fixed'). Translated in full from the Chinese and dropped his parentheticals.
- kp15 ad85347a72d2: his English 'Reflection — Test Your Understanding' was replaced by a literal translation of 思考題 · 提取練習 ('Reflection Questions · Retrieval Practice').
- kp15 3a0a50942c2b: option A says 'low score 3.5 vs high score 16.0', but kp10 (f479818f32fb, cc19705ccb9e) says the clumps sit at scores 5 and 16 (and at points (3,3) and (16,16)). The Chinese is inconsistent; translated faithfully.
- kp16 f1398609db2a: the <small> line 'No teacher, still order.' duplicated the Chinese heading, so it was dropped. The extra bilingual-en line, which has no Chinese counterpart, is kept, following the precedent of decks 02/03.
- kp17 a3cf332a434b: '與前三講一致' = consistent with the previous three lectures (deck 03 said 'two'). His '(ice-crystal light, full-width)' was dropped; 'full-width' has no Chinese counterpart.

## Images

- Inline charts with Chinese labels get English redraws in a separate commit.
