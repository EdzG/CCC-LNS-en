---
name: redraw-chart
description: Recreate one chart image that has Chinese text baked in as an English version for the overlay. Use when a chapter's assets/*.png contains Chinese labels, titles, or legends.
argument-hint: "[path to png, e.g. IDL_115/Ch17-graph-neural-networks/assets/diagram-kp5.png]"
---

Redraw `$ARGUMENTS` with English text. The original plotting scripts are private, so the
chart must be rebuilt from the image itself.

1. Open the image and write down everything it shows: chart type and layout (subplots, sizes),
   every title, axis label, tick label, legend entry, annotation, and the data. For curves,
   identify the function if it is a known one (e.g. Chebyshev polynomials, sigmoid) and compute
   it exactly rather than tracing it. For bars and points, read the values from the labels or
   the gridlines.
2. Find the surrounding paragraph in the chapter's `index.html` (search for the filename) so the
   English labels use the same terms as the translated text and `en/glossary.json`.
3. Write `en/tools/charts/<chapter>/<image-stem>.py` with matplotlib. Match the original's
   figure size and aspect ratio (same pixel dimensions at the same dpi), colors, line styles,
   and layout. Use an English font that supports math symbols (DejaVu Sans is fine).
4. Run it to save `en/IDL_115/<chapter>/assets/<same filename>.png`.
5. Put the original and the redraw side by side (one combined image in a scratch folder, not
   committed) and look at it. Check: every label translated, no Chinese left, data and curve
   shapes match, nothing clipped. Fix and re-run until it matches.
6. If something cannot be read reliably (blurry values, unknown data), keep the closest
   faithful version and add a line to `en/IDL_115/<chapter>/notes.md` saying what is uncertain.
   Never invent data that changes what the chart teaches.
7. Report the output path and any uncertainty. Do not commit; the calling workflow commits.
