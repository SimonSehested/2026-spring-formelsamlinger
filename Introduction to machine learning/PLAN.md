# PLAN.md

Build or rewrite a universal printed 4-page A4 formula-and-interpretation exam sheet in LaTeX.

The final compiled PDF must be exactly 4 A4 pages.

The sheet must contain formulas, but formulas must be paired with short explanations in words. The student should be able to calculate and also understand what symbols, plots, matrices, axes, probabilities, weights, loadings, scores, clusters, densities, and metrics mean.

This is not a pure formula collection, not lecture notes, and not an exam-strategy sheet.

## Phase 1: Inspect project structure

- Identify available input folders, such as:
  - `input/exams/`
  - `input/lectures/`
  - `input/exercises/`
  - `source_material/exams/`
  - `source_material/slides/`
  - `source_material/lectures/`
  - `source_material/exercises/`
- List all discovered source files.
- Identify existing LaTeX files, especially:
  - `main.tex`
  - `sources/*.tex`
  - `sections/*.tex`
  - `chapters/*.tex`
- Infer the current output structure.
- Do not assume folder names; inspect what exists.

## Phase 2: Infer course and exam structure

From the available source material:

- infer the course title
- infer the main topics
- infer standard notation and terminology
- infer recurring exam problem types
- infer recurring objects shown in problems, such as plots, matrices, tables, boundaries, outputs, and diagrams
- infer which formulas are repeatedly needed for calculation
- infer which symbol meanings and output interpretations are repeatedly needed
- infer which short procedures are useful under exam conditions

Write findings to:

- `reports/coverage_report.md`

If the `reports/` folder does not exist, create it.

Keep this report concise. It is a working note, not part of the 4-page sheet.

Do not prioritize exam-format descriptions or guessing strategy.

## Phase 3: Build object-and-task taxonomy

Inspect exam and exercise problems.

Group problems by the objects and tasks the student must handle, for example:

- read a covariance/correlation matrix
- match plots to statistics
- read a PCA loading matrix
- interpret score/loading/biplot plots
- compute explained variance
- compute Bayes or Naive Bayes posterior probabilities
- interpret Gaussian densities
- compute regression or logistic predictions
- read decision boundaries
- compute confusion-matrix metrics
- read ROC curves
- assign clusters with k-means, hierarchical clustering, or GMM
- compute density/outlier scores
- compute association-rule measures
- compute text/vector similarities

For each task type, record:

- recurring problem wording
- object shown in the problem
- required formula
- needed symbol meanings
- needed interpretation in words
- shortest calculation procedure
- source problems that use this task type
- priority for inclusion on a 4-page sheet

Write the taxonomy to:

- `reports/exam_task_taxonomy.md`

Do not use a hardcoded taxonomy from another course.

## Phase 4: Rank content by 4-page value

Before writing the sheet, rank candidate content.

Use this priority order:

1. Recurring formulas needed for calculation.
2. Short explanations that make those formulas usable.
3. Interpretation of recurring plots, matrices, tables, and outputs.
4. Short procedures for recurring task types.
5. Symbol explanations for confusing notation.
6. Compact method-selection cues.
7. Rare formulas only if there is remaining space.

Explicitly deprioritize:

- `Trap:` sections
- exam-format descriptions
- guessing strategies
- long warnings
- proofs
- long derivations
- generic checklist material

Mark low-value or rare content as excluded rather than forcing it into the sheet.

## Phase 5: Propose sheet structure

Create a proposed list of `.tex` files for the formula sheet.

Use one file per major topic, method group, or recurring object family.

Prefer organization by what the student sees in problems, not only by lecture topic.

A useful structure may include:

- data, plots, matrices, standardization
- PCA/SVD and dimensionality reduction outputs
- probability, Bayes, densities, regression, classification
- validation, metrics, ROC, model interpretation
- trees, ANN, ensembles, decision boundaries
- clustering, density, outliers, association rules, text similarity

Record the proposed structure in:

- `reports/coverage_report.md`

The structure must fit naturally into exactly 4 pages.

## Phase 6: Prepare LaTeX structure

- Create missing source `.tex` files.
- Preserve useful existing modular structure if present.
- Update `main.tex` so it inputs all formula source files in the correct order.
- Keep `main.tex` modular.
- Do not place substantial formula content directly in `main.tex`.

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

Use 2 or 3 columns depending on readability.

## Phase 7: Draft the 4-page sheet

For each topic or task family, include:

- purpose in one short sentence
- formulas needed for calculation
- short word explanation of what each formula does
- symbol meanings only where needed
- how to read related plots, matrices, tables, and outputs
- short procedure for typical exam tasks

Use this compact block format when useful:

```tex
\subsection*{Object or method}
\textbf{Purpose:} ...
\textbf{Formulas:} ...
\textbf{Symbols:} ...
\textbf{How to read it:} ...
\textbf{Do this:} ...
```

Do not write `Trap:` sections.

Do not include exam-format or guessing-strategy sections.

## Phase 8: Add compact calculation-and-reading recipes

For every recurring task that deserves space, add a recipe that includes both computation and interpretation.

Example structure:

```tex
\subsection*{Task: read a PCA loading matrix}
\textbf{Formulas:} $\tilde X=USV^\top$, $Z=\tilde XV$.
\textbf{Symbols:} column $k$ of $V$ is PC $k$; entries are loadings for original variables.
\textbf{How to read it:} large absolute values show variables that define the PC; signs show direction along the PC.
\textbf{Do this:} choose the column; find largest absolute loadings; use signs to describe positive/negative direction.
```

Keep recipes short, normally 2--4 steps.

## Phase 9: Add visual navigation layer

Audit the sheet for paper usability.

Ensure:

- clear topic headings
- consistent block labels
- compact tables for object interpretation
- formulas are easy to spot
- explanations sit close to the relevant formulas
- matrix and plot reading rules are visually findable
- no dense paragraphs
- no large warning/checklist sections

Do not optimize for digital search.

## Phase 10: Compile and measure page count

Compile `main.tex`.

Check the compiled PDF page count.

The PDF must be exactly 4 pages.

If the PDF is longer than 4 pages:

- shorten word explanations
- merge related blocks
- replace lists with compact tables
- remove low-priority topics
- remove warning-only content
- remove exam-format material
- reduce repeated symbol explanations
- reduce spacing carefully

If the PDF is shorter than 4 pages:

- add high-value formulas
- add short formula explanations
- add plot/matrix/output interpretation
- add symbol meanings
- add compact task recipes

Do not fill space with traps, guessing, or exam-format strategy.

Repeat until the compiled PDF is exactly 4 pages.

## Phase 11: Verification under page budget

Inspect each exam and exercise set again.

For each problem, map it to:

- problem type
- object shown
- required formula
- required interpretation
- whether the sheet supports calculation
- whether the sheet supports reading/interpretation
- whether missing content is worth including
- whether missing content is excluded due to page budget

Update:

- `reports/exam_verification_report.md`

Suggested table:

| Source | Problem | Object/method | Formula needed | Interpretation needed | Support on 4-page sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|---|

If a recurring high-value formula or interpretation is missing, add or improve a compact block and recompile.

If rare content is missing, mark it as excluded.

Do not exceed 4 pages.

## Phase 12: Final cleanup

- Remove unnecessary duplication.
- Ensure notation is consistent with source material.
- Ensure formulas and explanations are paired.
- Ensure headings support fast visual lookup.
- Ensure recipes are short.
- Ensure the document is readable when printed.
- Ensure no `Trap:` sections remain.
- Ensure no exam-format or guessing section remains.
- Ensure no long derivation remains.
- Ensure `main.tex` includes all generated files.
- Compile one final time.
- Confirm the final PDF is exactly 4 pages.

## Final deliverables

The final project should contain:

- updated modular `.tex` source files
- updated `main.tex` if needed
- compiled PDF with exactly 4 A4 pages
- `reports/coverage_report.md`
- `reports/exam_task_taxonomy.md`
- `reports/exam_verification_report.md`

## Stop condition

Do not stop after planning.

The task is complete only when:

- the formula-and-interpretation sheet has been rewritten or generated
- formulas and short explanations are both present
- the LaTeX document compiles
- the compiled PDF is exactly 4 A4 pages
- the document is visually usable on paper
- the verification report maps problems to the sheet or explicitly excludes them due to page budget
