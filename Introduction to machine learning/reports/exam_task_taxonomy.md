# Exam task taxonomy

| Task family | Recurring wording/cue | Required rule | Likely uncertainty | Sheet support | Priority |
|---|---|---|---|---|---|
| Data/statistic matching | Histogram, boxplot, scatter matrix, correlation/covariance matrix | Standardization, covariance, correlation, visual sign/magnitude checks | Standardized vs raw units; sign and symmetry | `Exam format and data checks` | High |
| PCA/SVD | SVD of standardized `X`, projection, explained variance, PC direction statements | `X=USV^T`, scores `XV`, EVR from singular values | Column vs row of `V`; PC sign; fewest components | `PCA and linear algebra` | Very high |
| Bayes from counts | Conditional probability from binary table | Count numerator/denominator; Bayes normalization | Conditioning on wrong attributes; missing normalization | `Probability, Bayes and Naive Bayes` | Very high |
| Naive Bayes | Binary item attributes, class prediction | Prior times conditional factors | Independence assumption; zero factors | `Probability, Bayes and Naive Bayes` | High |
| Gaussian density/classifier | Multivariate normal contours/classes | Gaussian density and posterior score | Priors; variance vs standard deviation | `Probability, Bayes and Naive Bayes` | High |
| Regression | Linear/ridge prediction, RMSE/MSE, regularization plot | Linear model, ridge, validation error | Intercept, standardized inputs, lambda direction | `Regression and classification models` | High |
| Logistic regression | Probability from weights, boundary plots | Sigmoid, logit, threshold | Positive class, weight dimension, intercept | `Regression and classification models` | Very high |
| KNN prediction | KNN regression/classification from distance table | Majority vote or mean of neighbours | Standardization and ties | `Regression and classification models` | Medium-high |
| Validation | Hold-out, K-fold, leave-one-out, two-level CV | CV averaging and nesting | Test leakage; counting models | `Validation, metrics and ROC` | Very high |
| Confusion/ROC | Compare classifiers, calculate TPR/FPR/precision/AUC | Confusion matrix formulas, ROC threshold update | Positive class and denominators | `Validation, metrics and ROC` | Very high |
| Decision trees | Hunt split, purity gain, boundary plot | Impurity and weighted gain | Forget branch weights; class majority at leaf | `Decision trees, ensembles and ANN` | High |
| AdaBoost | Weight update over rounds | Weighted error, alpha, increased weights for mistakes | Sign of alpha; misclassified weights | `Decision trees, ensembles and ANN` | Medium-high |
| ANN forward pass | Given weights and activation | Hidden pre-activation, activation, output | Bias terms, activation range | `Decision trees, ensembles and ANN` | High |
| K-means/hierarchical | Distance table, dendrogram, linkage | Assign/centroid update; linkage definitions | Cut height; linkage type | `Clustering and density/outliers` | High |
| Cluster comparison | Rand/Jaccard from assignments | Pair counts | Including/excluding `f00` | `Clustering and density/outliers` | High |
| GMM/KDE/outliers | Density plots, likelihood, outlier candidate | Mixture/KDE density, LOO density | Sum vs max; bandwidth; low density | `Clustering and density/outliers` | Very high |
| KNN density/ARD | Outlier from distance table | Inverse average neighbour distance; ARD ratio | Excluding self; recomputing neighbour densities | `Clustering and density/outliers` | Very high |
| Association mining | Frequent itemsets, rules, support/confidence/lift | Apriori and rule metrics | Superset pruning; confidence vs lift | `Association mining, text and final checks` | High |
| Text/similarity | Cosine, Jaccard, sparse binary vectors | Cosine and Jaccard formulas | Shared zeros in sparse data | `Association mining, text and final checks` | Medium |

Selection principle used: include compact rules that prevent common multiple-choice traps, rather than rare formulas requiring large space.
