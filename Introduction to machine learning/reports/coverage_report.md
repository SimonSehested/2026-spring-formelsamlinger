# Coverage report

## Sources inspected

- `input/exams/`: 02450/02452 exam sets, with 2025 Spring/Fall weighted highest.
- `input/lectures/`: 02451 lecture slide sets 01--13 as support material.
- Existing source files, prior reports, and the 2025 coverage assessment.

## Current design

The sheet is now a fast printed lookup aid rather than a dense prose summary. It uses uppercase scan terms, compact tables, local symbol explanations, and short `MEANS / READ / CALC` rules. It is designed to be usable when copied by hand, so it does not depend on color or bold text.

## Included high-value coverage

| Object/task family | Final support |
|---|---|
| Lookup/navigation | Mini-index of scan terms and final concept/action tables for quick search. |
| Data, plots, matrices | Standardization, covariance/correlation, distances, histograms, scatter matrices, count tables, covariance-ellipse reading. |
| PCA/SVD | SVD objects, projection, score variance, explained variance, loadings, scores, biplots, orthonormal PC directions. |
| Probability/Bayes/density | Bayes rule, count-table probabilities, Naive Bayes, Gaussian density, GMM responsibility/E-step, KDE/LOO. |
| Prediction/boundaries | Linear/ridge, logistic regression, feature maps, heatmaps, KNN, softmax, boundary-shape recognition. |
| Validation/metrics | Hold-out, K-fold, nested CV, confusion matrix, accuracy/error/recall/precision/FPR/F1, ROC/AUC, paired tests. |
| Trees/ensembles/ANN | Hunt split impurities, tree-boundary reading, AdaBoost class-label weights/votes, ANN forward pass, output activations, parameter count. |
| Clustering/association | K-means, dendrogram linkage, Rand/Jaccard cluster agreement, local density/ARD, association support/confidence/lift/Apriori. |

## Compression and cuts

The rewrite shifts space toward 2025-tested concepts and interpretation tasks. Long prose was replaced by tables and scan-first labels. Low-priority material was compressed: text/tf-idf was removed, softmax reduced to one lookup row, Jaccard retained only where useful for cluster agreement, and ARD kept compactly.

Excluded: exam-format material / guessing strategy / warning-only text / long derivations / full EM derivation / full backpropagation / low-frequency text-mining details / broad textbook explanations.
