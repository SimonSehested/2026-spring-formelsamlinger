# Exam task taxonomy

| Task family | Object shown / cue | Calculation core | Interpretation required | Sheet support |
|---|---|---|---|---|
| Find a term fast | Unknown word/object in question | None or nearest formula | Meaning of term and first action | `LOOKUP` table and `FAST CONCEPT CHECKS` |
| Read data summaries | Data table, histogram, boxplot, scatter matrix | Standardization, covariance, correlation, distance | Axes, spread, sign, strength, row vs column comparison | `DATA, PLOTS, MATRICES` |
| Match matrix to plot | Scatter/covariance/correlation options | Correlation sign and magnitude | Up/down tilt, narrowness, covariance ellipse | `COVARIANCE / CORRELATION / DISTANCE` |
| Project with PCA | `Xtilde`, `S`, `V`, score/loading table | Projection, score variance, EVR | Columns of `V`, positive/negative scores, component meaning | `PCA / SVD / VECTORS` |
| Classify with probabilities | Count table, prior, likelihood, Gaussian density | Bayes, Naive Bayes, density times prior | Prior vs likelihood vs posterior; denominator from condition | `PROBABILITY / BAYES / DENSITY` |
| Read density models | KDE/GMM plot, component table, responsibility | KDE LOO, GMM responsibility | Density height, component assignment, covariance/weight reading | `GMM / EM RESPONSIBILITY`, `KDE` |
| Predict numeric/class output | Weight vector, test point, feature map | Linear/ridge/logistic/KNN formulas | Weight sign, threshold, heatmap, boundary type | `PREDICTION / BOUNDARIES` |
| Evaluate models | CV table, nested CV table | Fold averages and selected outer error | Model selection vs performance estimate | `VALIDATION / METRICS / MODEL OUTPUT` |
| Read classifier output | Confusion matrix, ROC, threshold counts | Accuracy, recall, precision, FPR, ROC point | Positive class, table orientation, threshold movement | `CONFUSION MATRIX`, `ROC / AUC` |
| Compare paired models | Same test rows for two classifiers/regressors | McNemar, paired loss CI | Disagreements, sign of difference, CI containing zero | `PAIRED MODEL COMPARISON` |
| Read trees/ensembles/ANN | Split table, boundary figure, boost weights, ANN diagram | Impurity gain, AdaBoost, forward pass, parameter count | Tree inequalities, weighted votes, activations, biases | `TREES / ADABOOST / ANN` |
| Cluster/read groups | Centroid table, dendrogram, partition comparison | K-means, linkage, Rand/Jaccard | Cluster profiles, merge heights, pair agreement | `CLUSTERING / ASSOCIATION` |
| Mine association rules | Binary basket table or itemsets | Support, confidence, lift | Frequency, conditional frequency, Apriori pruning | `ASSOCIATION RULES / APRIORI` |

## Rewrite audit result

The sheet now supports both calculation and concept-definition questions. Every retained formula is paired with nearby symbol explanations, and every major table/plot/output object has a reading rule. The 2025 exams drove additions for PCA score variance, nested CV, regularization bias/variance, feature-map heatmaps, tree-boundary reading, AdaBoost class-label weights, ANN parameter counts, GMM E-step responsibilities, and covariance/scatter interpretation.

Excluded: rare / derivable / low-value / exam-format only / warning-only / not worth 4-page space.
