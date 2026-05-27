# Style Guide for 4-Page Printed Formula-and-Interpretation Sheet

## Goal

Create a clean, dense, readable 4-page A4 exam sheet that combines formulas with short explanations in words.

The sheet must help a student both:

1. calculate with the required formulas, and
2. understand what the symbols, plots, matrices, axes, probabilities, scores, loadings, clusters, densities, and metrics mean.

This is not a pure formula sheet and not lecture notes. It is a printed exam aid for solving problems when the student needs both computation and interpretation.

## Core principle

Every important method should contain a calculation core and an interpretation core.

Use this pattern whenever possible:

```tex
\subsection*{Method or exam object}
\textbf{Purpose:} one short sentence explaining what the method is for.

\textbf{Formulas:}
\[
...
\]

\textbf{Symbols:} short explanations of only the symbols needed to use the formulas.

\textbf{How to read it:} short explanation of how to interpret matrices, plots, axes, numbers, weights, scores, loadings, probabilities, clusters, densities, or metrics.

\textbf{Do this:} 2--4 concrete steps for typical exam tasks.
```

Do not force every label if it adds noise. Prefer meaning and usability over rigid formatting.

## Mandatory content style

The sheet must include:

- central formulas needed for calculations
- short word explanations for formulas
- symbol meanings where notation is likely to be confusing
- how to read common plots, matrices, and model outputs
- short procedures for recurring task types
- method-selection cues where useful
- compact interpretation rules for numeric outputs

The sheet must avoid:

- `Trap:` sections
- exam-format descriptions
- guessing strategies
- multiple-choice scoring strategy
- long proofs
- long derivations
- long theory paragraphs
- formulas without explanations
- explanations without formulas when the topic requires calculation
- dense notation that is not explained in words
- generic checklist material that does not directly help solve or interpret a problem

## Label vocabulary

Preferred labels:

```tex
\textbf{Purpose:}
\textbf{Formulas:}
\textbf{Symbols:}
\textbf{How to read it:}
\textbf{Do this:}
\textbf{Use when:}
\textbf{Means:}
\textbf{Interpretation:}
\textbf{Decision:}
```

Avoid labels such as:

```tex
\textbf{Trap:}
\textbf{Exam format:}
\textbf{Guessing:}
\textbf{Check:}
```

Use `Check` only if it is a direct mathematical validation that helps calculate or interpret an answer, not as a negative warning.

## Formula style

Formulas must be present, but each formula block should be followed by words explaining what the formula does.

Good:

```tex
\[
P(y=c\mid x)=\frac{P(x\mid y=c)P(y=c)}{\sum_{c'}P(x\mid y=c')P(y=c')}
\]
\textbf{Means:} compute one score per class, then divide by the sum of all class scores so probabilities add to 1.
```

Bad:

```tex
\[
P(y=c\mid x)=\frac{P(x\mid y=c)P(y=c)}{\sum_{c'}P(x\mid y=c')P(y=c')}
\]
```

Good:

```tex
\textbf{How to read }V\textbf{:} in PCA, column $k$ is PC $k$. Large positive/negative values show which variables pull the observation along that PC.
```

Bad:

```tex
\textbf{Trap:} PC $k$ is column $k$, not row $k$.
```

## Explanation density

Use short sentences, not paragraphs.

Good:

```tex
\textbf{Purpose:} PCA replaces many original variables with fewer new axes that explain most variation.
\textbf{How to read scores:} each point is one observation in PC coordinates. Nearby points have similar profiles in the original variables.
```

Bad:

```tex
PCA is a dimensionality reduction technique that is useful because it transforms the original feature space into a new orthogonal basis where the axes are ordered by explained variance, which can then be used for visualization and compression.
```

## Plot and matrix interpretation

Prioritize objects the student may see in exam problems:

- data matrices
- covariance and correlation matrices
- PCA loading matrices
- PCA score plots
- loading plots and biplots
- histograms, boxplots, scatter plots
- confusion matrices
- ROC curves
- decision boundaries
- dendrograms
- cluster plots
- density plots
- GMM responsibilities
- association-rule tables
- text/vector similarity tables

For each object, include:

1. what the object represents,
2. how to read the numbers or axes,
3. the relevant formula if calculation is required,
4. a short procedure for the exam task.

## Tables

Use compact tables for visual lookup.

Recommended table types:

- plot/object to interpretation
- method to formula
- model output to meaning
- metric to formula and meaning
- clustering method to how it behaves
- matrix type to how it is read

Example:

```tex
\begin{tabularx}{\linewidth}{@{}lX@{}}
\toprule
\textbf{Object} & \textbf{How to read it} \\
\midrule
Score plot & points are observations in PC coordinates; nearby points have similar profiles \\
Loading vector & numbers show how much each original variable contributes to a PC \\
Biplot & combines observations and variable directions in the same PC plane \\
\bottomrule
\end{tabularx}
```

Keep table text short.

## Recipes

Use recipes for recurring exam tasks.

Example:

```tex
\subsection*{Naive Bayes classification}
\textbf{Purpose:} choose the class that best explains the observed attributes.
\[
score(c)=P(y=c)\prod_m P(x_m\mid y=c),\qquad
P(y=c\mid x)=\frac{score(c)}{\sum_{c'}score(c')}
\]
\textbf{Symbols:} $P(y=c)$ is the class prior. $P(x_m\mid y=c)$ is the probability of attribute value $x_m$ inside class $c$.
\textbf{Do this:} compute one score per class; normalize scores; choose the largest posterior probability.
```

Recipes should normally be 2--4 steps.

## What to include

Include content that helps the student answer:

- What does this method do?
- Which formula do I use?
- What do these symbols mean?
- What does this matrix or plot show?
- How do I compute the requested quantity?
- How do I interpret the result?
- What is the shortest reliable procedure?

## What to exclude

Exclude content that mainly answers:

- what the exam scoring format is
- how to guess multiple choice answers
- what not to do
- proofs or derivations
- broad motivational theory
- rare edge cases that cost too much space
- repeated formulas with no added meaning
- long lists of warnings

## Layout

Use a compact printable layout.

Recommended starting point:

```tex
\documentclass[9pt,a4paper]{article}
\usepackage[a4paper,margin=0.75cm]{geometry}
\usepackage{multicol}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage[most]{tcolorbox}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}
\setlength{\columnsep}{0.45cm}
\setlist{nosep,leftmargin=*}
\setlength{\abovedisplayskip}{2pt}
\setlength{\belowdisplayskip}{2pt}
\setlength{\abovedisplayshortskip}{1pt}
\setlength{\belowdisplayshortskip}{1pt}
```

Use 2 or 3 columns depending on readability. Prefer 3 columns for formula-heavy sections and 2 columns if explanations become unreadable.

## Page count

The final PDF must be exactly 4 A4 pages.

If too long:

- shorten wording before removing formulas
- merge related blocks
- use compact tables
- remove low-value warnings
- remove exam-format material
- remove rare topics
- reduce repeated notation explanations

If too short:

- add interpretation of plots and matrices
- add symbol explanations
- add compact calculation recipes
- add formulas that recur in exams
- add object-reading tables

Do not fill space with generic strategy or negative warnings.
