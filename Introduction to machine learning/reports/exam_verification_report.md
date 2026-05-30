# Exam verification report

## Verification basis

The final sheet was checked against the 2025 coverage assessment, the recurring 2017--2024 task taxonomy, and the rewritten `sources/*.tex`. The target was quick printed lookup: formulas, symbol meanings, plot/table/output reading rules, and short calculation procedures.

## Verification results

- `ml.pdf` compiles to exactly 4 A4 pages.
- The final layout uses 12pt body text so it is large enough to copy by hand from print.
- The sheet no longer relies on color or bold text for navigation.
- The rewrite adds 2025-critical gaps: PCA score variance, nested-CV outer-error calculation, regularization bias/variance cues, feature-map/heatmap reading, decision-tree boundary reading, AdaBoost class-label updates, ANN parameter count, GMM E-step responsibility, and covariance/scatter-ellipse interpretation.
- Long prose blocks were replaced by local `MEANS`, `READ`, and `CALC` instructions.
- Every displayed formula block has a formula ID and nearby explanation of the symbols needed to use it.
- No `Trap:` sections, exam-format material, or guessing strategy remain.

## Build verification

- Ran `pdflatex -interaction=nonstopmode -halt-on-error -jobname=ml main.tex` twice after the 12pt readability update.
- Ran `pdfinfo ml.pdf`; result: 4 pages, A4 page size.
- Scanned `ml.log`; no `Undefined`, `Overfull`, `Warning`, or `Error` lines remain in the final log scan.
- Rendered page PNGs for visual inspection; formulas stay inside columns and the four-page structure is readable.

## Included / excluded decisions

Included: all 2025-heavy task families plus older recurring fundamentals: data/plot/matrix reading, PCA/SVD, Bayes/Gaussian/GMM/KDE, regression/logistic/KNN, validation/metrics/ROC/model comparison, trees/AdaBoost/ANN, k-means/dendrogram/Rand, association support/confidence/lift.

Excluded or compressed: fast concept checks, broad scan/cue tables, paired model-comparison tests, ensemble terminology, text/tf-idf details, long EM derivations, full ANN backpropagation, broad lecture prose, warning-only material, multiple-choice/exam-format content, and low-frequency material not worth 4-page space.
