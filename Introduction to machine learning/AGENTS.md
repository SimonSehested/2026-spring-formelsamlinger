# AGENTS.md

You are building or rewriting a LaTeX exam aid for the course described by the project source material.

## Goal

Create a printed 4-page A4 formula-and-interpretation sheet.

The final compiled PDF must be exactly 4 A4 pages.

The sheet must contain formulas needed for calculation, but each important formula must be paired with short explanations in words. The student should be able to use the sheet to calculate answers and understand what symbols, plots, matrices, axes, probabilities, weights, loadings, scores, clusters, densities, and metrics mean.

This is not:

- a pure formula sheet
- lecture notes
- a textbook summary
- a proof-based theory document
- an exam-format or guessing-strategy sheet
- a list of traps and warnings

The primary user situation is:

- the student is sitting in a physical exam
- the student cannot search digitally
- the student must quickly identify the relevant method
- the student needs formulas for computation
- the student also needs words explaining how to read plots, matrices, tables, and outputs

## Source material

Use the source material provided by the project. Typical project inputs may include files such as:

- `input/exams/`
- `input/lectures/`
- `input/exercises/`
- `source_material/exams/`
- `source_material/slides/`
- `source_material/lectures/`
- `source_material/exercises/`

First inspect the available folders and infer the actual course title, topics, notation, terminology, recurring formulas, recurring plots/matrices, and recurring problem types.

Do not assume a fixed course, topic list, notation system, or exam style in advance.

Do not invent unsupported formulas or topics unless they are standard prerequisites clearly required to solve recurring exam or exercise problems.

If something is uncertain, mark it with:

```tex
% TODO: verify from source
```

## Core principle

Every item on the sheet must answer at least one of these questions:

1. What formula do I need to calculate this?
2. What do the symbols in the formula mean?
3. What does this plot, matrix, table, or model output represent?
4. How do I read the numbers, signs, axes, probabilities, weights, scores, loadings, or clusters?
5. What is the shortest reliable calculation procedure?
6. How do I interpret the result in words?

If an item does not support calculation or interpretation, remove it.

## Forbidden content

Do not include:

- `Trap:` sections
- exam-format descriptions
- guessing strategies
- multiple-choice score rules
- long warnings about what not to do
- long proofs
- long derivations
- broad motivational paragraphs
- generic strategy checklists
- formula blocks with no word explanation
- explanations that omit needed formulas

Negative warnings should usually be rewritten as positive reading instructions.

Bad:

```tex
\textbf{Trap:} PC $k$ is column $k$, not row $k$.
```

Good:

```tex
\textbf{How to read }V\textbf{:} column $k$ is PC $k$; read down the column to see which variables define that PC.
```

## Required block format

Use compact blocks such as:

```tex
\subsection*{Object or method}
\textbf{Purpose:} one short sentence.

\textbf{Formulas:}
\[
...
\]

\textbf{Symbols:} explain only the symbols needed to use the formulas.

\textbf{How to read it:} explain how to interpret the relevant plot, matrix, table, boundary, probability, output, or metric.

\textbf{Do this:} 2--4 concrete steps for typical exam tasks.
```

Do not force every label if it wastes space.

Preferred labels:

- `Purpose`
- `Formulas`
- `Symbols`
- `How to read it`
- `Do this`
- `Use when`
- `Means`
- `Interpretation`
- `Decision`

Avoid:

- `Trap`
- `Exam format`
- `Guessing`

## Formula requirements

Formulas are mandatory for computational topics.

Each formula should be close to a short explanation of what it does.

Example:

```tex
\subsection*{Confusion matrix metrics}
\[
\text{Accuracy}=\frac{TP+TN}{N},\quad
\text{Recall}=\frac{TP}{TP+FN},\quad
\text{Precision}=\frac{TP}{TP+FP},\quad
F_1=\frac{2PR}{P+R}
\]
\textbf{Symbols:} $TP$ = positive cases predicted positive; $FN$ = positive cases missed; $FP$ = negative cases predicted positive; $TN$ = negative cases predicted negative.
\textbf{How to read it:} recall measures how many true positives were found; precision measures how many predicted positives were actually positive.
```

## Interpretation requirements

Prioritize recurring objects the student may see in exam questions:

- data matrices
- standardized values
- covariance/correlation matrices
- histograms, boxplots, scatter plots, scatter matrices
- PCA/SVD matrices
- explained variance tables
- score plots
- loading plots
- biplots
- probability tables
- Gaussian density curves
- regression and logistic regression outputs
- decision boundaries
- confusion matrices
- ROC curves
- validation/CV tables
- decision trees
- neural-network diagrams or weight tables
- k-means centroid tables
- dendrograms
- GMM component tables and responsibilities
- density/outlier tables
- association-rule tables
- text/vector similarity tables

For each object that appears repeatedly in the source material, include how to read it.

## Tables

Use tables aggressively for compact lookup.

Good table types:

- object to interpretation
- method to formula
- model output to meaning
- metric to formula and meaning
- clustering method to behavior
- plot type to reading rule
- matrix type to reading rule

Example:

```tex
\begin{tabularx}{\linewidth}{@{}lX@{}}
\toprule
\textbf{Object} & \textbf{How to read it} \\
\midrule
Correlation matrix & diagonal is 1; sign gives direction; magnitude gives strength of linear relation \\
Score plot & each point is an observation in PC coordinates; nearby points have similar profiles \\
Loading vector & entries show how original variables contribute to one PC \\
\bottomrule
\end{tabularx}
```

Keep table text short.

## Content priority

Prioritize content in this order:

1. Recurring formulas needed to compute exam answers.
2. Short explanations that make those formulas usable.
3. Interpretation of recurring plots, matrices, tables, and model outputs.
4. Short calculation procedures for recurring tasks.
5. Symbol explanations for confusing notation.
6. Compact method-selection cues.
7. Rare formulas only if there is remaining space.

When forced to choose, prefer a formula plus a useful interpretation over several isolated formulas with no explanation.

## 4-page print constraint

The compiled PDF must be exactly 4 A4 pages.

If the document is longer than 4 pages:

- shorten wording
- merge related formulas
- combine object explanations in tables
- remove low-frequency topics
- remove warning-only content
- remove exam-format content
- remove repeated symbol explanations
- reduce vertical whitespace carefully

If the document is shorter than 4 pages:

- add high-value formulas
- add short formula explanations
- add symbol explanations
- add plot/matrix/output reading rules
- add compact calculation recipes

Do not fill space with traps, guessing strategies, or exam-format descriptions.

## Output files

Create or update modular LaTeX source files in the project’s formula-collection source directory, typically:

- `sources/`
- `sections/`
- `chapters/`

Use the existing project structure if one exists. If no structure exists, create a `sources/` directory.

Use one `.tex` file per major exam-relevant topic, method group, or object family inferred from the source material.

Use clear numbered filenames such as:

```text
01_data_plots_matrices.tex
02_pca_svd.tex
03_probability_regression_classification.tex
04_validation_metrics_models.tex
05_clustering_density_association_text.tex
```

Topic names must be inferred from the provided source material, not hardcoded from another course.

Do not write large amounts of formula content directly in `main.tex`.

Keep `main.tex` modular and use `\input{...}` or `\include{...}`.

## Reports

Create or update concise reports in `reports/`:

- `coverage_report.md`
- `exam_task_taxonomy.md`
- `exam_verification_report.md`

Reports are working notes. They must not cause the formula sheet to grow beyond 4 pages.

In the verification report, mark excluded material explicitly, for example:

```text
Excluded: rare / low exam frequency / derivable / warning-only / exam-format only / not worth 4-page space
```

## LaTeX quality

The final document must compile.

Before finishing:

- run the LaTeX build if available
- fix compile errors
- check for undefined references
- check for missing input files
- check for broken math syntax
- check the compiled PDF page count
- ensure the compiled PDF is exactly 4 pages
- ensure the compiled PDF is readable when printed
- ensure formulas and short explanations are paired
- ensure headings support fast visual lookup
- ensure no `Trap:` sections remain
- ensure no exam-format or guessing-strategy section remains

## Do not

- do not optimize for Ctrl+F
- do not include keyword spam
- do not assume a fixed course structure
- do not hardcode topics from another course
- do not write textbook chapters
- do not include long proofs
- do not include long derivations
- do not include unsupported material
- do not duplicate formulas unnecessarily
- do not place raw notes in final files
- do not make the document longer for completeness
- do not sacrifice readability just to add more content
- do not stop before the PDF is exactly 4 pages
