# Exam task taxonomy

| Task family | Object shown / cue | Calculation core | Interpretation required | Sheet support |
|---|---|---|---|---|
| Standardize/read summaries | Data table, histogram, boxplot, scatter/correlation/distance matrix | `F1`, `F2`, `F3` | Above/below mean, plot spread, correlation sign/strength, named distance, plot-to-number matching | Data, plots, matrices |
| Project with PCA | `S`, `V`, score/loading/biplot | `F4`, `F5` | Columns are PCs, rows are scores, loadings define variable direction and positive/negative PC meaning | PCA, SVD, vectors |
| Compare vectors | Norm/cosine table or sparse vectors | `F6`, `F27`, `F28` | Direction similarity versus length/distance | PCA and associations |
| Classify from probabilities | Count table, prior/likelihood table, density curve | `F7`, `F8`, `F9` | Prior, likelihood, posterior, density height | Probability, Bayes, densities |
| Predict number/class | Weight vector, new input, class scores | `F10`--`F14` | Coefficient sign/unit, threshold, 2D boundary, local KNN boundary, softmax probabilities | Prediction and boundaries |
| Select/evaluate model | Hold-out/CV/nested-CV table | `F15` | Minimum validation/inner-CV error; held-out/outer error after selection | Validation and output |
| Read binary classifier output | Confusion matrix, metric request, ROC curve | `F16`--`F18` | Positive class, matrix orientation, denominators, ROC threshold movement | Validation and output |
| Compare paired models | Same test rows for two models | `F19`--`F21` | Disagreements, sign of loss difference, CI containing zero | Validation and output |
| Calculate tree/ensemble/ANN output | Split table, boost weights, network diagram | `F22`--`F24` | Node impurity, normalized weights, hidden activations | Trees, ensembles, ANN |
| Form/read clusters | Centroids, dendrogram, clustering comparison | `F25`, `F26` plus linkage table | Nearest centroid, merge height, pair agreement | Clustering and outliers |
| Soft cluster/outlier | GMM/KDE/local-density table | `F27`--`F29` | Responsibility sums, density height, smallest density/ARD as outlier | Clustering and outliers |
| Mine item/text data | Basket/rule table, binary or tf-idf vectors | `F30`--`F32` | Co-occurrence, sparse similarity, rare term weighting | Associations and sparse vectors |

## Rewrite audit result

Every final displayed formula block has a compact formula ID. Every retained procedure line now either cites an `F#` formula or states the concrete operation directly, for example plot matching, PC wording, denominator selection, ROC updates, boost-weight normalization, centroid recomputation, ARD ratio calculation, or Apriori pruning.

Excluded: rare / derivable / low-value / exam-format only / warning-only / not worth 4-page space.
