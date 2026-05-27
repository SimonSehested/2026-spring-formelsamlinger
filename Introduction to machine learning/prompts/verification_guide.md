# Verification Guide for 4-Page Formula-and-Interpretation Sheet

## Purpose

Verify that the 4-page sheet supports both calculation and interpretation.

The goal is not full lecture coverage. The goal is the best possible printed 4-page aid for solving exam problems when the student needs formulas, symbol meanings, and guidance on reading plots, matrices, and model outputs.

## What to verify

For each exam problem or exercise, identify whether the sheet helps with:

- choosing the relevant method
- using the correct formula
- understanding the symbols in the formula
- reading a plot, matrix, table, boundary, density, or model output
- interpreting numeric quantities such as probabilities, weights, loadings, scores, variances, distances, responsibilities, metrics, and similarities
- following a short calculation procedure

Do not evaluate whether the sheet contains generic warnings, exam-format rules, or guessing strategies. These are not target content.

## Verification table

Create or update:

- `reports/exam_verification_report.md`

Use this table format:

| Exam/source | Problem | Object/method shown | Formula needed | Interpretation needed | Support on sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|---|

## Include/exclude rules

Include an item if:

- it appears repeatedly in exams or exercises
- it is needed to compute a requested answer
- it explains a matrix, plot, or output that students must read
- it explains symbols that are otherwise hard to remember
- it helps connect formulas to interpretation
- it gives a short reliable procedure for a recurring task
- a small amount of text makes a formula usable

Exclude an item if:

- it is only exam-format strategy
- it is mainly a warning about what not to do
- it is a proof or derivation
- it appears rarely and requires too much space
- it is easy to derive under exam pressure
- it repeats material already covered clearly
- it does not help compute or interpret anything

Mark excluded items explicitly:

```text
Excluded: rare / derivable / low value / exam-format only / warning-only / not worth 4-page space
```

## Verification questions

For each recurring problem type, ask:

1. Does the sheet contain the formula needed to calculate the answer?
2. Does it explain what the symbols in that formula mean?
3. If the problem shows a plot or matrix, does the sheet explain how to read it?
4. If the problem gives model output, does the sheet explain what the numbers mean?
5. Does the sheet give a short procedure for the task?
6. Is any included text actually helping calculation or interpretation?

## Required support categories

The final sheet should support common exam objects such as:

- data matrix and standardization
- covariance and correlation matrix
- histogram, boxplot, scatter plot, scatter matrix
- PCA/SVD matrices and explained variance
- score plots, loading plots, biplots
- Bayes and Naive Bayes probability tables
- Gaussian density values
- regression and logistic regression outputs
- KNN neighbour-based predictions
- validation/CV results
- confusion matrices and performance metrics
- ROC curves
- decision boundaries
- decision tree splits and leaves
- neural-network forward passes
- k-means centroids and cluster assignments
- hierarchical dendrograms
- GMM responsibilities
- KDE/KNN density and outlier scores
- association-rule tables
- binary similarity and text vectors

Only include categories that are supported by the actual source material and exam recurrence.

## Page-count discipline

If verification reveals missing content, do not simply add it.

First decide whether it deserves space under the 4-page limit.

If adding content makes the PDF longer than 4 pages, remove or compress lower-value content. Remove warning-only text and exam-format material before removing formulas or interpretation.

The final PDF must remain exactly 4 A4 pages.

## Final verification checklist

Before finishing, confirm:

- LaTeX compiles.
- The compiled PDF is exactly 4 A4 pages.
- The sheet is readable when printed.
- The sheet contains formulas needed for calculation.
- Important formulas have short explanations in words.
- Symbols that are easy to confuse are explained.
- Common plots and matrices are explained as objects to read.
- Recurring problem types have short procedures.
- No `Trap:` sections remain.
- No exam-format or guessing-strategy section remains.
- No long proof or derivation remains.
- Rare excluded items are documented in the report.
