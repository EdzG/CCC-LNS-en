# Notes: Ch02 deck (02-ai-foundations-2-1-biological-neuron-bilingual)

Bilingual deck. EN mode shows our translation of the **Chinese**; the professor's English was a
reference only (his `.en-sub` subtitles are hidden via `_hide`). `kpN` = the Nth section;
hex ids are strings.json keys.

## Where our English departs from the professor's English, and other choices

- kp1 9332f6d39365: the professor's English says 'to an artificial abstraction'; the Chinese says 'to the artificial neuron'. Followed the Chinese.
- kp2 aead0ee3389f: the professor's English says 'inspired by'; the Chinese asks what the artificial neuron is 'imitating'. Followed the Chinese.
- kp3/kp4 Axon/Synapse/Dendrites/Nucleus · 中文 headings and SVG labels: kept the English name only, and wrote 'Soma (Cell Body)' to keep the gloss.
- kp4 14baba4cf87a: the card icon is the character 枝 (branch); replaced with the symbol ⑂ (a branching fork) to match the other symbol icons ◎ ◉ ⋯.
- kp4 6b6fbf340692: the title says five parts, but the slide has four cards (soma, nucleus, dendrites, synapse) plus the axon in a separate box below; translated as written.
- kp6 7c502774f3c2: this unit's innerHTML contains <span id="fireStatus">, which the slider script caches by reference at load. The innerHTML swap replaces it, so in EN mode the visible pill stops updating when the slider moves. Suggest adding '#fireStatus' (or '.status-pill') to _dynamic so _runtime handles it.
- kp9 5d043a4d10c2: the Chinese places the McCulloch–Pitts model 'around the 1950s' (1950 年代前後), but the model is from 1943. Translated faithfully as 'Around the 1950s'. Candidate for notes.md.
- kp9 e864efd83694: 'kp3 McCulloch–Pitts' seems to refer to the next deck (03-ai-foundations-mp-neuron), not to a KP3 in this deck. Kept 'in kp3' as written.
- kp10 1e3ccdd9682b: kept 'Chinese–English bilingual labels', which matches the professor's intent for the AI prompt.
- kp12 159a0840f312: the 'Next: formal neuron models and learnable weights.' line has no Chinese counterpart, so I kept it (in its bilingual-en span).

## Runtime

- Runtime: the #fireStatus pill sits inside a translated block and is rewritten by the slider script; the engine keeps it live and translates it through _runtime.

## Images

- The deck has no inline images.
