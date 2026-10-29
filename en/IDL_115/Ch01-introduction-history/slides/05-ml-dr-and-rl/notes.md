# Notes: Ch01 slide 05 (05-ml-dr-and-rl.html)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Possible errors in the source

- kp5 `f9c2b02377cd` / `a24e54210f0c`: step 1 says red ends up low and blue high, step 3 says $y=5$ is blue and 16 warm. Translated as written.
- kp5 `a079cc4bee8a` / `a24e54210f0c`: the clusters are given as (3,3) and (16,16) but scored 5 and 16; the projection $y=x_1+x_2$ of kp7 would give 6 and 32. Translated as written.
- Runtime: quiz 3's explanation `$f_\theta(x)=a$` is written via textContent, so it shows as raw TeX in both languages.

## Where our English departs from the professor's English, and other choices

- kp1 f98bb9523a5f: kept the professor's English-only subtitle span (no Chinese counterpart); '棍棒的教養' (upbringing by the rod, i.e. learning from punishment/reward) translated literally to keep the joke.
- kp2 77bb349cc835, kp3 67b25d2d2922, kp3 1601846c639e: the formula(s) appear in both the Chinese and the dropped English half; kept once, as in the Chinese half.
- kp2 77bb349cc835, kp3 67b25d2d2922/18b53d2ebb2a/1601846c639e, kp4 6b71b7885677/3ec1f3b99f07/d2b375a34282/e4858464ddd4: the professor's English (bilingual-en) is a terse summary that omits much of the Chinese; replaced by a full translation of the Chinese.
- kp4 01c71aa8534c: English 'Find Pattern Alone' is unidiomatic; rendered as 'finds patterns on its own'.
- kp5 f9c2b02377cd / a24e54210f0c: the Chinese is internally inconsistent: step 1 says red ends up low and blue high, but step 3 says y=5 is blue and 16 is warm (blue low). Translated faithfully.
- kp5 a079cc4bee8a / a24e54210f0c: the clusters are given as (3,3) and (16,16), but the scores in step 3 are 5 and 16, which do not match the y=x1+x2 projection used on kp7 (that would give 6 and 32). Translated faithfully.
- kp5 124d3a310354, f9c2b02377cd, a079cc4bee8a, a24e54210f0c, f9e4c1b97656: the professor's English lines are terse summaries (e.g. 'Pull apart.', 'Score = label.'); translated the full Chinese instead.
- kp6 2d31d64e50ca: professor's English '(Left: LLE-like; Right: FDA-like)' differs from the Chinese (neighbor intuition vs label-driven push/pull); followed the Chinese.
- kp7 e3ee71904977: heading's English 'Same Demo' does not match the Chinese 本圖參數 (parameters of this plot); followed the Chinese.
- kp8 b567036d835a: $\mathbb{R}^1$ appears in both halves; kept once (the half kept). Professor's 'Tight is Answer' rendered as 'tight means you have the answer'.
- kp10 29612c3a4e79: the professor's English half repeats $\mathbf{x}$, $a$, $A$; kept once each (the Chinese half's count), so en has 4 math segments vs 7 in zh.
- kp10 1f6092937f60: professor's English 'No tidy → no candy; tidy → candy' drops the negative/positive reward labels and the 'learns a knack from random fumbling' sentence; translated the full Chinese.
- kp11 svg labels: 環境回饋新狀態 shortened to 'Env returns new state' to fit the diagram.
- kp12 bc1beb873617: professor's English says 'self-driving'; the Chinese says 自動導航 (autonomous navigation). Followed the Chinese.
- kp12 676bb646d5f2 / kp11 3558f95d97c6 / kp13 / kp14 / kp15: professor's English halves are heavily abbreviated notes (e.g. 'Push & tighten.', 'Unsupervised DR goal?'); translated the Chinese in full instead.
- kp15 9134766efe26: $p$ appears in both halves; kept once.
- kp16 d982a3c1f122: 'Compress to see; roll to learn.' was the professor's translation of the headline and is replaced by the translated headline; the extra English line '$p&lt;d$ for insight, $r$ for policy.' has no Chinese counterpart, so it is kept with its span.
- kp16 da39d2d8fdde: English 'two arts of learning' has no Chinese counterpart; dropped, followed the Chinese.
- kp17 2616c9789746: English '(ice-crystal light, full-width)' adds 'full-width', which the Chinese doesn't say; followed the Chinese.

## Images

- Inline charts with Chinese labels get English redraws in a separate commit.
