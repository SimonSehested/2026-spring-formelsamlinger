# Exam verification report

## Verification basis

The final sheet was checked against the existing exam-derived coverage reports and the rewritten `sources/*.tex`. The verification target was not just topic presence, but whether the sheet says how to compute or read the object.

| Exam/source family | Object/method shown | Formula needed | Interpretation needed | Final support | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|
| 2017--2024 solved sets | Standardized observations, plots, correlation/distance matrices | `F1`--`F3` | Scale, axes, spread, sign/strength, row distance | Explicit recipes and plot-to-number matching in data section | No | Included |
| 2017--2024 solved sets | PCA `S,V`, scores, EVR, biplots | `F4`, `F5` | Loading column, score point, biplot direction, PC wording | Projection, PC interpretation and plot reading rules | No | Included |
| Multiple sets | Bayes/Naive Bayes probability tables | `F7`, `F8` | Prior/likelihood/posterior and normalization | Table recipe says exactly which factors to multiply and normalize | No | Included |
| Multiple sets | Gaussian class density | `F9` | Density height versus probability, centre/spread | Density-class score recipe | No | Included |
| Multiple sets | Linear/ridge/logistic/KNN/softmax prediction | `F10`--`F14` | Weight sign/unit, threshold, local neighbours, boundary type | Explicit prediction, coefficient and threshold/boundary recipes | No | Included |
| 2017--2024 solved sets | CV/model-error table | `F15` | Selection versus final reporting; nested CV | Minimum validation/inner-CV rule and held-out/outer rule | No | Included |
| 2017--2024 solved sets | Confusion matrix and ROC | `F16`--`F18` | Positive class, matrix orientation, denominators, threshold path | Denominator/orientation lookup and ROC update recipe | No | Included |
| Fall 2019--Spring 2024 recurring sets | Paired classifier/regression comparison | `F19`--`F21` | Disagreements, sign, CI/p-value reading | McNemar and paired-loss procedures | No | Included |
| Multiple sets | Tree split, AdaBoost, ANN diagram | `F22`--`F24` | Node fractions, normalized weights, activations, weight sign | Mechanical recipes for each calculation | No | Included |
| Multiple sets | Centroids, dendrograms, cluster agreement | `F25`, `F26` | Cluster profile, cut height, pair agreement | K-means, centroid, linkage and agreement recipes | No | Included |
| Spring 2024 and repeated earlier sets | GMM, KDE, KNN density, ARD | `F27`--`F29` | Responsibility, bandwidth, low-density outliers, global/local density distinction | Responsibility normalization and ARD ratio recipe | No | Included |
| Several sets | Association rules, Jaccard, tf-idf/cosine | `F30`--`F32` | Rule meaning, sparse zeros, rare term weighting | Count/prune/similarity recipes | No | Included |
| Lecture-only or rare extensions | Full derivations, EM details, low-frequency visualization extensions | Varies | Low immediate exam calculation value | None | Yes | Excluded: low frequency / derivable / not worth 4-page space |

## Build verification

- `pdflatex -jobname=ml -interaction=nonstopmode -halt-on-error main.tex` was run twice.
- `ml.pdf` is exactly 4 pages and A4 size.
- Body text is true `10pt`/`\normalsize`; no global `\footnotesize` or `\scriptsize` is used.
- Formula references resolve; log scan found no `Undefined`, `Reference`, `Error`, or `Overfull` lines.
- One non-fatal underfull table message remains in the final object-to-action table; it does not affect page count or formula references.
- Source scan found no `Trap:` label, exam-format section, guessing strategy, or multiple-choice strategy.
- Every displayed formula block in `sources/*.tex` has a compact `F#` formula ID.
