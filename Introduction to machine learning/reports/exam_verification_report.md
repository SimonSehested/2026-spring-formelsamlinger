# Exam verification report

The verification pass used extracted text from the 2017-2024 exams and solutions. The goal was not full solution coverage; it was support for likely uncertainty moments under a four-page print budget.

| Exam/source | Problem pattern | Required concept or method | Likely uncertainty | Support on sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|
| Spring/Fall 2017-2024 | Early data plot/statistic questions | Standardization, covariance/correlation, histograms/boxplots | Signs, range, symmetry, standardized vs raw | Data checks section | No | Included |
| Spring/Fall 2017-2024 | PCA projection and variance questions | SVD, score matrix, explained variance | Column of `V`, sign, variance from singular values | PCA section | No | Included |
| Spring/Fall 2017-2024 | PCA interpretation statements | Loadings and projection signs | Sign convention and high/low standardized values | PCA reading recipe | No | Included |
| Several exams | Conditional probability/Bayes table | Count-based conditional probabilities | Wrong denominator or conditioning set | Bayes count recipe | No | Included |
| Several exams | Naive Bayes item/binary classification | Priors and conditional products | Independence assumption, zero factors | Naive Bayes block | No | Included |
| Several exams | Gaussian class density/GMM density | Normal density, mixture density | Variance vs width, weighted sum vs max | Gaussian/GMM sections | No | Included |
| Several exams | Linear/ridge regression | Prediction, weight shrinkage, RMSE | Intercept and lambda interpretation | Regression section | No | Included |
| Several exams | Logistic regression probability/boundary | Sigmoid and threshold | Positive class, weight dimension | Logistic section | No | Included |
| Several exams | KNN regression/classification | Neighbour vote/mean | Scaling, tie handling | KNN section | Partial | Tie rules excluded unless stated in problem |
| Spring/Fall 2017-2024 | Cross-validation statements | Hold-out/K-fold/two-level CV | Leakage and model-counting | Validation section | No | Included |
| Spring/Fall 2017-2024 | Confusion matrices/ROC/AUC | TPR, FPR, precision, ROC thresholds | Denominators and positive class | Metrics/ROC section | No | Included |
| Several exams | Decision trees/Hunt gain | Impurity and weighted split gain | Forgetting child weights | Tree section | No | Included |
| Several exams | AdaBoost rounds | Weighted error and alpha | Weight direction after mistakes | AdaBoost block | No | Included |
| Several exams | ANN forward computation | Activation and output layer | Bias and activation range | ANN block | No | Included |
| Several exams | K-means and dendrograms | Centroids, linkage, cut height | Linkage confusion | Clustering section | No | Included |
| Several exams | Cluster comparison | Rand/Jaccard pair counts | Whether to count different-different pairs | Cluster comparison block | No | Included |
| Several exams | KDE/KNN density/ARD outliers | Density formulas and LOO selection | Excluding self, bandwidth, low density | Density/outlier section | No | Included |
| Several exams | Association rules/Apriori | Support, confidence, lift, pruning | Confidence vs lift; supersets | Association section | No | Included |
| Several exams | Text similarity | Cosine/Jaccard | Shared zeros and sparse vectors | Text/similarity block | No | Included |
| Lecture-only lower-frequency content | Representation learning, t-SNE/UMAP, deep autoencoders | Conceptual definitions | Low formula value under 4-page constraint | Not on sheet | Yes | Excluded: rare/low exam frequency/not worth 4-page space |
| Lecture-only lower-frequency content | Full EM derivation and optimization details | Derivation steps | Too much space for low MC value | GMM responsibilities only | Yes | Excluded: derivable/too space-heavy |

Final build status:

- `main.tex` compiles with MiKTeX `pdflatex`.
- Output file: `main.pdf`.
- Page count from LaTeX log: exactly 4 pages.
- Layout: A4, two columns, narrow margins, compact print-oriented formula blocks.
- Remaining warning: one negligible overfull line below 1 pt; no undefined references or missing input files observed.
