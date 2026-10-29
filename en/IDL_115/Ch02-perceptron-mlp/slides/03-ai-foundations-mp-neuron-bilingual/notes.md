# Notes: Ch02 deck (03-ai-foundations-mp-neuron-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1/kp2/kp3+: section, cover and takahashi titles drop the professor's small English span; the English title is written as the title itself.
- kp3 789657df0564 / de7c721f3c80 / 14b22160f930: the professor's English halves are heavy abridgements of the Chinese (e.g. drop the coffee anecdote, 'study the wheel' vs 'how the wheel was invented'); translated the full Chinese.
- kp4 267fe38b4a43: professor's 'relay' for 傳聲筒 rendered as 'messenger' (a relay passes everything on; the point is it speaks only past a threshold).
- kp6 c7b25f4abab6: professor's 'Threshold 2 encodes the AND logic' is fine; full Chinese adds 'total reaches it -> 1, else 0'.
- kp6 cc4fd4fb8af8: section heading says 加權和 (weighted sum) though M-P has equal fixed weights; translated faithfully.
- kp8 c9f8158c06c6: professor's English 'Lower the bar; the boundary shifts' omits the new equation and that only (0,0) maps to 0; translated the full Chinese.
- kp8 69b661858e97: the caption refers to an inline base64 matplotlib PNG; if that image has Chinese labels it needs a redraw (not checked here).
- kp9 e1c2b144a9f1: professor's English is a 6-word abridgement; translated full Chinese.
- kp11 quiz options: the professor's inline English glosses (e.g. '— math too hard') were dropped as duplicates; option order and correct answer (Q1: B '2', Q2: C) unchanged. Q1 buttons with numerals only + English gloss ('1 — fires too easily') contain no Chinese and are not units, so they stay as-is.

## Runtime

- Runtime: the wrong-answer hint '間值決定誰能鳴火' has typos (間值 → 閾值 threshold, 鳴火 → fire); translated as meant. The same 'correct' message is shown for both quiz cards, so Q2's reads oddly (upstream).

## Images

- The 1 inline image(s) are English-only and shown as they are.
