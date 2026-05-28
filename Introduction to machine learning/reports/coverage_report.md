# Coverage report

## Sources inspected

- `input/exams/`: solved and unsolved 02450 exam sets, Spring/Fall 2017--2024.
- `input/lectures/`: 02451 lecture slide sets 01--13.
- Existing `sources/*.tex`, `PLAN.md`, `prompts/style_guide.md`, and `prompts/verification_guide.md`.

The course is 02450/02451 Introduction to Machine Learning and Data Mining / Introduction to Machine Learning. The sheet is organized around recurring calculation and output-reading tasks from the exam-derived reports.

## Included high-value coverage

| Object/task family | Final support |
|---|---|
| Standardization, plots, covariance/correlation, distances | Formula IDs for scaling, correlation and distances; explicit axis/matrix reading recipes plus plot-to-number matching. |
| PCA/SVD, projections, explained variance | Formula IDs for SVD/scores/reconstruction and EVR; explicit loading, score plot, biplot, PC-wording and projection instructions. |
| Bayes, Naive Bayes, Gaussian density | Posterior/count/log-score/density formulas with table-reading and class-score recipes. |
| Linear/ridge/logistic regression, KNN, softmax | Prediction and boundary formulas with explicit calculation order, coefficient reading and threshold/boundary rules. |
| Validation, confusion matrix, ROC, paired tests | CV/nested-CV selection rule, denominator/orientation rules, ROC update and threshold procedure, McNemar and paired-loss CI. |
| Trees, AdaBoost, ANN | Split gain, regression-tree cue, boosting weight normalization, weight reading and neural forward-pass recipes. |
| K-means, dendrograms, cluster agreement, GMM, KDE/ARD | Assignment, centroid reading, dendrogram group choice, responsibility normalization and outlier calculation recipes. |
| Association rules, sparse similarity, text vectors | Support/confidence/lift, Apriori pruning, Jaccard/SMC and tf-idf/cosine recipes. |

## Structure

- `sources/01_exam_and_data.tex`
- `sources/02_pca_linear_algebra.tex`
- `sources/03_probability_bayes.tex`
- `sources/04_regression_classification.tex`
- `sources/05_validation_metrics.tex`
- `sources/06_trees_ensembles_ann.tex`
- `sources/07_clustering_density.tex`
- `sources/08_association_text_checks.tex`

## Compression decisions

Included formulas and recipes were rewritten instead of left as vague reminders. After the first 10pt rewrite left unused page space, additional high-value reading rules and a final object-to-action table were added back. Repeated symbol prose and warning-only text remain removed.

Excluded: exam-format material / guessing strategy / warning-only text / long derivations / full EM derivation / low-frequency extensions beyond the recurring exam objects.
