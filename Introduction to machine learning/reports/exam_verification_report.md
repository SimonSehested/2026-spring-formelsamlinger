# Exam verification report

## Review basis

All provided solved exam PDFs from Spring/Fall 2017--2024 were text-inspected for recurring methods and objects. Recent sets were additionally spot-checked around PCA, regression, ROC, clustering and density formulas. Verification targets calculation and reading support under the four-page constraint.

| Exam/source | Problem/object family | Formula needed | Interpretation needed | Support on sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|
| 2017--2024 solved sets | Standardized observations; histogram/boxplot/scatter/correlation or distance object | Standardization, covariance/correlation, Euclidean/cityblock/max distance | Scale, plot spread, correlation sign and named metric | Data section | No | Included |
| 2017--2024 solved sets | PCA `S,V`, projections and variance plots | `X=USV^T`, `Z=XV`, EVR | Loading column, score point, biplot direction | PCA section | No | Included |
| Multiple 2017--2024 sets | Conditional/Naive Bayes table | Posterior and factorized score | Prior versus likelihood versus posterior | Bayes section | No | Included |
| Multiple 2017--2024 sets | Gaussian density/class curves | Normal density and class score | Centre/spread and density versus probability | Bayes section | No | Included |
| Multiple 2017--2024 sets, notably 2023--2024 | Linear/ridge/logistic prediction output | Prediction, ridge with unpenalized intercept, sigmoid | Coefficient sign, standardized input, boundary | Prediction section | No | Included |
| Multiple sets | KNN prediction or boundary | Vote/mean of neighbours | Local smoothness and distances | Prediction section | No | Included |
| 2017--2024 solved sets | CV/model-error table | Fold/test error mean | Selection result versus generalization estimate | Validation section | No | Included |
| 2017--2024 solved sets | Confusion matrix and ROC curves | TPR/FPR/precision/F1 and ROC coordinates | Rows/columns, threshold motion, AUC | Validation section | No | Included |
| Fall 2019--Spring 2024 recurring sets | Paired classifier/regression comparison | McNemar disagreement counts; paired-loss CI | Sign of difference, CI containing zero, p-value | Validation section | No | Included |
| Multiple sets, notably 2018 and 2023--2024 | Tree, AdaBoost or ANN diagram/table | Gain, boost update, network forward pass | Leaf result, weights and activations | Trees/ANN section | No | Included |
| Multiple 2018--2024 sets | Centroid/dendrogram/cluster assignments | K-means, linkage, Rand/Jaccard | Cut height and pair agreement | Clustering section | No | Included |
| Spring 2024 and repeated earlier sets | GMM/KDE/local density table or plot | Mixture responsibility, KDE, KNN density, ARD | Soft membership and outlier reading | Density section | No | Included; ARD verified against printed formula |
| Several solved sets | Association-rule or text/binary similarity table | Support/confidence/lift, Jaccard/cosine | Co-occurrence and sparse similarity | Association section | No | Included |
| Lecture material beyond repeated exam objects | Full EM/optimization derivations | Lengthy derivation | Limited immediate output-reading value | None | Yes | Excluded: not worth 4-page space |
| Lower-frequency supplementary methods | Extra representation/visualization methods | Varies | Limited recurrence | None | Yes | Excluded: low exam frequency |

## Build verification

- `pdflatex -interaction=nonstopmode -halt-on-error -jobname=ml main.tex` compiles successfully.
- `ml.pdf` is checked with `pdfinfo` for A4 size and exactly four pages.
- Formula-symbol audit completed: a shared notation line defines recurring dimensions, indexes, inputs and targets, and every computational formula group has an adjacent `Symbols`, `Symbols/means` or `Symbols/use` explanation for its method-specific quantities.
- The additional symbol explanations fit the print constraint using `\footnotesize` body text; the log contains no overfull lines.
- Final source scan checks that the sheet contains no forbidden strategy block or `Trap:` label.
- Long formulas are split for two-column print readability; only non-fatal short-table underfull box messages may remain.
