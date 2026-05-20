# Coverage report

## Source inspection

Project material inspected:

- `input/exams/`: 02450 written multiple-choice exams with solutions from Spring/Fall 2017-2024.
- `input/lectures/`: 02451 lecture slides 01-13.
- `prompts/style_guide.md` and `prompts/verification_guide.md`.

The available exam material identifies the course as **02450 Introduction to Machine Learning and Data Mining**. The lecture material uses **02451 Introduction to Machine Learning** as the current course framing, with a schedule aligned to the same core topic sequence.

Exam format observed:

- Multiple choice, normally 27 equally weighted questions.
- Answer options A-D plus E = "Don't know".
- Scoring in recent exams: correct `+3`, wrong `-1`, don't know `0`.
- Recent Fall 2024 format allows two A4 sheets handwritten front/back; the generated sheet targets exactly four printed A4 pages.

## High-frequency topics found

Term frequency across extracted exam/solution text showed repeated emphasis on:

- PCA/SVD, explained variance, projections, loading interpretation.
- Bayes, Naive Bayes, conditional probabilities, Gaussian class densities.
- Linear/ridge regression, logistic regression, KNN classification/regression.
- Cross-validation, two-level validation, model selection and test-error interpretation.
- Confusion matrices, ROC/AUC, precision/recall/FPR/TPR.
- Decision trees, impurity/gain, AdaBoost, neural-network forward passes.
- K-means, hierarchical clustering, clustering comparison.
- GMM, KDE, KNN density, average relative density and outlier detection.
- Association rules, Apriori, Jaccard/cosine/text similarity.

## Final sheet structure

- `sources/01_exam_and_data.tex`
- `sources/02_pca_linear_algebra.tex`
- `sources/03_probability_bayes.tex`
- `sources/04_regression_classification.tex`
- `sources/05_validation_metrics.tex`
- `sources/06_trees_ensembles_ann.tex`
- `sources/07_clustering_density.tex`
- `sources/08_association_text_checks.tex`

## Excluded or compressed material

- Detailed proofs and derivations: excluded, not useful under 4-page exam backup constraint.
- Representation learning details beyond PCA/autoencoder recognition: excluded as lower observed exam frequency and high space cost.
- Deep optimization theory: excluded; only ANN forward-pass and model-complexity traps retained.
- Full EM algorithm derivation: compressed to GMM density/responsibility because exams mostly ask recognition, density, and assignment.
- Long worked examples: excluded; replaced by short recipes and plausibility checks.
