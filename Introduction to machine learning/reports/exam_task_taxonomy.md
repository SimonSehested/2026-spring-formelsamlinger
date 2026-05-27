# Exam task taxonomy

| Task family | Object shown / recurring cue | Calculation core | Interpretation required | Sheet location | Priority |
|---|---|---|---|---|---|
| Standardize and identify summaries | Table, histogram, boxplot, scatter/correlation/distance matrix | `z=(x-mean)/s`, covariance/correlation, Euclidean/cityblock/max distance | Above/below mean; sign, spread and named distance | Data, summaries and distances | High |
| Project with PCA | `S`, `V`, observations or PC plot | `Z=XV`, EVR from `s_k^2` | Columns are loadings; points are scores | PCA and SVD | Very high |
| Classify from probabilities | Count/probability table or class density curve | Bayes/Naive Bayes/Gaussian score | Prior, likelihood, posterior, density height | Probability and Bayes classification | High |
| Predict a number/class | Weight vector, new input, boundary diagram | Linear/ridge, sigmoid, KNN | Weight sign, threshold, local boundary | Prediction models and boundaries | Very high |
| Choose/evaluate procedure | CV table and paired model errors | Fold mean error; McNemar; paired-loss CI | Validation selection, held-out estimate and evidence of difference | Validation and classifier output | Very high |
| Evaluate binary scores | Confusion matrix or ROC diagram | TPR/FPR/precision/F1, ROC point | Positive class and curve axes | Validation and classifier output | Very high |
| Calculate tree/ensemble output | Tree split, weighted labels, network diagram | Impurity gain, AdaBoost, ANN pass | Leaf output, observation weight, activation | Trees, ensembles and neural networks | High |
| Form/read clusters | Centroid table or dendrogram | K-means and linkage, Rand/Jaccard | Cluster profile, merge height, agreement | Clustering, density and outliers | High |
| Assign soft cluster/find outlier | GMM/KDE plot or distance table | Responsibility, KDE, KNN density, ARD | Membership strength and low local density | Clustering, density and outliers | Very high |
| Mine sparse items/text | Basket/rule table or word vectors | Support/confidence/lift, Jaccard/cosine | Rule association and sparse similarity | Associations and sparse similarity | Medium-high |

## Source anchoring

- PCA/SVD, regression, validation/ROC and density keywords occur across all inspected solved exam-year groups.
- Spring 2024 explicitly uses PCA, KDE, KNN density and GMM objects.
- Fall 2023--Fall 2024 explicitly use logistic/linear regression, ANN/AdaBoost and model-output interpretation.
- Spring/Fall 2018--2023 include dendrogram/clustering, density and association/similarity tasks.
- Fall 2018 and related sets state ARD as an average of relative local-density ratios; the sheet follows that notation.
- Fall 2019--Spring 2024 include McNemar and/or confidence-interval model-comparison objects; both binary and regression paired readings are supported.
