# Coverage report

## Sources inspected

- `input/exams/`: solved and unsolved 02450 sets, Spring/Fall 2017--2024.
- `input/lectures/`: 02451 lecture slide sets 01--13.
- `AGENTS.md`, `PLAN.md`, `prompts/style_guide.md`, `prompts/verification_guide.md`.

The supplied sources identify the subject as 02450/02451 Introduction to Machine Learning and Data Mining / Introduction to Machine Learning. Text review of every available solved exam set was used to rank recurring calculation and interpretation tasks.

## Recurring high-value objects

| Object/task family | Evidence in solved exams | Included support |
|---|---|---|
| Standardized data, histograms/boxplots, covariance/correlation | Appears in early data questions across the exam series | Formula for standardization; plot/matrix reading rules |
| PCA/SVD, projections, explained variance | Appears in every reviewed year group | Loadings, scores, biplot interpretation; projection/EVR recipe |
| Bayes/Naive Bayes and Gaussian densities | Repeated classification questions | Posterior computation, table reading, Gaussian curve meaning |
| Linear/ridge/logistic regression and KNN | Repeated prediction/model-output questions | Prediction formulas, unpenalized intercept notation, boundary interpretation |
| Validation, confusion matrices, ROC and paired comparison | Repeated throughout 2017--2024; McNemar/CI occurs in several 2019--2024 sets | Fold/output reading, metrics, ROC, McNemar and paired-loss CI |
| Trees, AdaBoost and ANN forward calculation | Repeated model questions | Gain, boost update and forward-pass calculations |
| K-means, dendrograms, GMM, KDE and local density/ARD | Dense recurring cluster/outlier block in most sets | Cluster reading, responsibility, KDE/ARD formulas |
| Association rules and sparse similarity | Appears in several sets | Support/confidence/lift, Apriori cue, Jaccard/tf-idf/cosine |

## Final modular sheet structure

- `sources/01_exam_and_data.tex`: data, plots, matrices, distances and prediction loss.
- `sources/02_pca_linear_algebra.tex`: SVD/PCA, scores, loadings, plots and EVR.
- `sources/03_probability_bayes.tex`: Bayes, Naive Bayes and Gaussian density.
- `sources/04_regression_classification.tex`: regression, logistic, KNN and boundaries.
- `sources/05_validation_metrics.tex`: CV output, confusion matrices, ROC and paired model comparison.
- `sources/06_trees_ensembles_ann.tex`: trees, AdaBoost and ANN calculations.
- `sources/07_clustering_density.tex`: clustering, dendrograms, GMM, KDE and ARD.
- `sources/08_association_text_checks.tex`: association rules and sparse/text similarity.

## Selection decisions

Included material is tied to a formula plus how to read its table, plot, matrix or numerical output. The sheet prioritizes PCA, model prediction/evaluation and density/clustering because these recur most consistently.

Excluded: assessment-format material and answer-selection strategy; not part of a formula-and-interpretation aid.

Excluded: full EM derivation, optimization derivations and proofs; too space-heavy for calculation/reading value.

Excluded: lower-frequency representation-learning and visualization extensions beyond PCA; not worth 4-page space relative to recurring tasks.
