# 2025 new exam coverage assessment

Assessed files:

- `input/exams/02450ex_Spring2025.pdf`
- `input/exams/02450ex_Spring2025_sol.pdf`
- `input/exams/02452ex_Fall2025.pdf`
- Current sheet: `ml.pdf`, compiled as exactly 4 A4 pages.

## Executive assessment

The current notes are broadly well aligned with both new exams. Most questions can be attacked using the formulas and reading rules already present. The sheet is especially strong on the recurring backbone: standardization, scatter/correlation reading, PCA/SVD, KNN, Bayes, regression/logistic boundaries, CV, confusion matrices, ROC, trees, ANN forward passes, k-means, dendrograms, GMM, KDE/ARD, and association rules.

The weak points are not missing whole topics. They are mostly missing compact exam-procedure details for the way the newest exams ask questions:

1. PCA score variance and mean-centered projection wording should be strengthened.
2. Nested CV generalization-error calculation should be made more explicit.
3. Regularization bias/variance and nonlinear feature-map output reading should be clearer.
4. AdaBoost should support the class-label/vote-weight version used in the exams, not only signed-label notation.
5. ANN parameter counting should be added.
6. Gaussian covariance/scatter-ellipse reading should be added or strengthened.
7. GMM responsibility/EM wording is present but should be explicitly tied to "E-step/component assignment".

No major new topic needs to be added from these two exams. The correct response is targeted expansion plus cuts from lower-frequency material.

## Coverage by 02450ex Spring 2025

| Q | Topic | Current coverage | Assessment |
|---|---|---|---|
| 1 | Scatter plot matrix to correlation matrix | `01_exam_and_data`: covariance/correlation, scatter matrix reading | Good. Keep. |
| 2 | Match histograms from scatter/density panels | `01_exam_and_data`: histogram/density and scatter matrix | Good, but could use one short line: marginal distribution is read from the repeated axis of scatter-matrix panels. |
| 3 | 1-NN LOOCV error from distance table | `04_regression_classification`: KNN; `05_validation_metrics`: CV | Good. |
| 4 | Single/minimum-linkage dendrogram from distance table | `07_clustering_density`: hierarchical clustering | Good. |
| 5 | PCA projection variance, unbiased estimator | `02_pca_linear_algebra`: scores and explained variance | Partial. Add explicit `Var(z_k)=1/(N-1) sum_i z_{ik}^2 = v_k^T Xtilde^T Xtilde v_k/(N-1)` when data are centered. |
| 6 | Read signs/loadings in `V` | `02_pca_linear_algebra`: loading column reading | Good. |
| 7 | Association itemset support count | `08_association_text_checks`: support/Apriori | Good. |
| 8 | Naive Bayes from binary table | `03_probability_bayes`: counts and Naive Bayes | Good. |
| 9 | k-means convergence from 1D blocks | `07_clustering_density`: k-means assignment/centroid | Good. |
| 10 | Match decision-tree rules to axis-aligned boundary | `06_trees_ensembles_ann`: tree reading; `04`: boundary plots | Partial. Add compact tree-boundary reading: each internal node splits one axis; shaded/leaf regions are intersections of previous split inequalities. |
| 11 | KDE leave-one-out estimate | `07_clustering_density`: KDE/LOO | Good. |
| 12 | GMM component posterior from contours/covariances | `07_clustering_density`: GMM responsibilities | Good, but add "E-step" wording. |
| 13 | Match classifier type to boundary shape | `04_regression_classification`: boundary plots | Good. |
| 14 | Regularization action for high variance/low bias | `04`: ridge; but only lightly explains bias/variance | Partial. Add one line: larger lambda increases bias and reduces variance/weight norm; richer features reduce bias and increase variance. |
| 15 | CV statement / model selection | `05_validation_metrics`: CV and nested CV | Good. |
| 16 | Rand index from partitions | `07_clustering_density`: Rand/Jaccard | Good. |
| 17 | Bayes from binned histogram without Naive assumption | `03_probability_bayes`: conditional probability and counts | Good. |
| 18 | Two-level CV estimated generalization error | `05_validation_metrics`: nested CV | Partial. Formula should explicitly say outer estimate averages test error of the model selected by inner CV in each outer fold. |
| 19 | McNemar test | `05_validation_metrics`: McNemar | Good. |
| 20 | Match regularized regression feature maps to heatmaps | `04`: linear/ridge, boundary plots | Partial. Add nonlinear feature-map reading: constant/huge lambda -> flat mean; polynomial powers create curved/axis-shaped contours. |
| 21 | AdaBoost unnormalized weights after two rounds | `06_trees_ensembles_ann`: AdaBoost | Partial. Current update uses signed-class sign form and normalized weights; exam uses class labels, indicator votes, and asks unnormalized weights. Add class-label update line with `e^{-alpha}` for correct and `e^{alpha}` for wrong. |
| 22 | ANN output activation for standardized regression | `06_trees_ensembles_ann`: activations | Partial. Add output activation cue: linear for unconstrained regression; sigmoid for probability; ReLU only nonnegative outputs. |
| 23 | ANN parameter count | Not explicit | Missing. Add `(M+1)n_h + (n_h+1)C` or `(M+1)n_h+(n_h+1)` for one output. |
| 24 | Hunt algorithm / impurity gain statement | `06_trees_ensembles_ann`: split gain | Good. |
| 25 | Paired t-test from histogram | `05_validation_metrics`: paired regression CI | Good. |
| 26 | Confusion matrix metrics | `05_validation_metrics`: metrics + orientation | Good. |
| 27 | ROC from TP/TN/FP/FN threshold curves | `05_validation_metrics`: ROC | Good. |

## Coverage by 02452ex Fall 2025

| Q | Topic | Current coverage | Assessment |
|---|---|---|---|
| 1 | Standardized histograms from scatter matrix | `01_exam_and_data` | Good. |
| 2 | One k-means update in 1D | `07_clustering_density` | Good. |
| 3 | 3-NN LOOCV accuracy with tie rule | `04` KNN and `05` CV | Good, but tie rule is not explicitly stated. Low priority. |
| 4 | ANN training / regularization concept | `06` ANN; `04` regularization | Partial. Needs the regularization/bias-variance cue above. |
| 5 | Single-linkage dendrogram | `07` | Good. |
| 6 | PCA first/second directions from projection densities | `02` PCA reading | Good. |
| 7 | PCA projection of point onto components 2 and 4 | `02` projection formula | Good. |
| 8 | SVD orthonormal eigenvectors / KNN distance / GMM model selection | `02`, `04`, `07` | Partial. Orthonormality is implied by SVD but not stated as a direct reading cue. Add one short line: distinct columns of `V` are unit length and perpendicular. |
| 9 | KNN under `d_1`, `d_2`, `d_infty` | `01` distances + `04` KNN | Good. |
| 10 | Model comparison from probability bars / McNemar | `05` | Good. |
| 11 | Nested CV estimated generalization error | `05` | Partial; same nested-CV expansion as Spring Q18. |
| 12 | Regularization concept, closed forms, bias/variance | `04` | Partial; same bias/variance expansion. |
| 13 | Decision tree split rules on PC axes | `06` + `04` | Partial; same tree-boundary expansion. |
| 14 | KDE LOO estimate | `07` | Good. |
| 15 | EM E-step responsibility for 1D GMM | `07` | Good but should explicitly say E-step = compute responsibilities. |
| 16 | CV bias / model selection statement | `05` | Good. |
| 17 | ANN forward pass with ReLU and output plot | `06` | Good for computation; partial for reading output contour signs. |
| 18 | GMM sample set from means/covariances/weights | `03` Gaussian + `07` GMM | Partial. Add covariance ellipse/scatter reading: diagonal variances set spread; off-diagonal sign sets tilt; mixture weight sets expected fraction. |
| 19 | Ensemble/AdaBoost concept | `06` | Partial. Add one conceptual line: more boosting iterations can overfit with flexible weak learners; bagging samples bootstrap datasets, boosting reweights errors. |
| 20 | Gaussian Naive Bayes with equal likelihood, unequal priors | `03` | Good. |
| 21 | Confusion matrix metrics | `05` | Good. |
| 22 | Bayes classifier from binary attributes | `03` | Good. |
| 23 | AdaBoost final prediction from alpha-weighted weak classifiers | `06` | Partial. Same AdaBoost class-label vote expansion. |
| 24 | Regularized linear regression prediction with standardized test point | `01` standardization + `04` linear/ridge | Good. |
| 25 | Covariance matrix from multivariate-normal scatter plots | `01` correlation reading + `03` Gaussian | Partial. Add covariance/correlation scatter reading for multivariate normal matrices. |
| 26 | Logistic regression feature-map heatmaps | `04` logistic + boundary plots | Partial. Add nonlinear feature-map/heatmap reading. |
| 27 | ROC/AUC from binned threshold counts | `05` ROC | Good. |

## Current note quality by section

| Section | Quality against 2025 exams | Keep / expand / cut |
|---|---|---|
| `01_exam_and_data` | Strong. Directly supports scatter, histogram, distance, covariance, standardization, and regression loss tasks. | Keep. Expand slightly with covariance-matrix/scatter-ellipse reading if space allows. |
| `02_pca_linear_algebra` | Strong but one important exam formula is implicit: unbiased variance of PCA scores. | Expand. Add score variance and orthonormality of `V`. Do not cut. |
| `03_probability_bayes` | Strong. Covers Bayes, Naive Bayes, Gaussian classifier. | Keep. Maybe add one phrase that equal likelihoods do not imply equal posteriors if priors differ. |
| `04_regression_classification` | Good but conceptually thin for the 2025 feature-map/regularization heatmap questions. | Expand. Add bias-variance effect of lambda and a compact feature-map/contour reading rule. |
| `05_validation_metrics` | Strong. Covers CV, nested CV, metrics, ROC, McNemar, paired t-test. | Keep. Expand nested-CV formula by one line. |
| `06_trees_ensembles_ann` | Good coverage but the largest 2025 gaps are here: AdaBoost notation, ANN parameter count, output activation choice. | Expand. This is the highest-priority section to improve. |
| `07_clustering_density` | Strong. Covers k-means, dendrograms, Rand, GMM, KDE/ARD. | Keep. Expand GMM with E-step wording and covariance ellipse reading. |
| `08_association_text_checks` | Association support is tested in Spring 2025, but text/tf-idf is not touched in either new set. | Keep association rules. Cut or compress text vectors first if space is needed. |

## What to expand first

High priority:

1. Add PCA score variance:
   `z_k = Xtilde v_k`, `Var(z_k)=sum_i z_{ik}^2/(N-1)=v_k^T Xtilde^T Xtilde v_k/(N-1)`.
2. Add ANN parameter count:
   one hidden layer, one output: `(M+1)n_h + (n_h+1)`.
   with `C` output units: `(M+1)n_h + (n_h+1)C`.
3. Add AdaBoost class-label update:
   weighted error = sum weights of wrong rows; `alpha=1/2 log((1-eps)/eps)`; correct rows multiply by `e^{-alpha}`, wrong rows by `e^{alpha}`; final class maximizes sum of `alpha_t` votes for that class.
4. Add nested-CV estimator:
   in each outer fold choose model/complexity using inner folds, then take that chosen model's outer test error; average outer test errors.
5. Add regularization bias/variance cue:
   increasing `lambda` shrinks weights, increases bias, usually reduces variance; adding features does the opposite.

Medium priority:

6. Add covariance/scatter ellipse reading:
   positive covariance tilts up, negative tilts down, near zero is axis-aligned/round; diagonal entries are marginal variances.
7. Add nonlinear feature-map output reading:
   logistic heatmap is sigmoid of transformed features; contours follow where `w^T x_tilde` is constant; huge regularization gives nearly flat output.
8. Add decision-tree boundary reading:
   every internal node is one axis-aligned inequality; a leaf region is the intersection of inequalities along the root-to-leaf path.
9. Add output activation choice:
   linear for real-valued regression, sigmoid for probability/binary class, softmax for multiclass, ReLU only if target is constrained nonnegative.

Low priority:

10. Add KNN tie rule only if space remains.
11. Add one line on SVD orthonormality: columns of `V` have norm 1 and are mutually perpendicular.

## What to cut or compress

Cut/compress first if the PDF exceeds 4 pages after expansions:

1. `08_association_text_checks`: compress or remove `Text vectors and cosine`. Neither 2025 exam uses tf-idf/text. Cosine is already covered in `02_pca_linear_algebra`.
2. `08_association_text_checks`: compress `Binary attributes and Jaccard` if space is still tight. Association support is current; Jaccard/SMC is less central in these two sets.
3. `07_clustering_density`: compress `Compare clusterings` prose, but keep Rand formula because Spring 2025 tests it.
4. `07_clustering_density`: ARD/local-density is not in these two newest sets; keep only if older exams justify it. If space is needed, compress ARD before touching KDE/GMM.
5. `04_regression_classification`: softmax is not directly used in the two new sets. Keep only a very compact line unless older exams need it.
6. `05_validation_metrics`: paired regression t-test is tested in Spring 2025, so do not cut it before text/tf-idf or ARD.
7. Do not cut PCA, KNN, Bayes, CV, confusion metrics, ROC, tree, AdaBoost, ANN, k-means, dendrograms, KDE, or GMM. They are all active in 2025.

## Bottom line

The notes are good, roughly 80--85% coverage for direct exam use against the two new sets. The missing 15--20% is mostly "procedure sharpness": small formulas and reading rules that decide multiple-choice options quickly. The best next edit is not a rewrite. It is a surgical reallocation of space from text/tf-idf, Jaccard/SMC prose, ARD prose, and softmax prose into PCA variance, ANN parameter count, AdaBoost class-label weights, nested-CV outer-error calculation, bias/variance regularization, and covariance/feature-map plot reading.

Excluded from recommended expansion: exam-format instructions, guessing strategy, long derivations, full EM derivation, full ANN backpropagation, full proofs of PCA/SVD, and broad textbook explanations.
