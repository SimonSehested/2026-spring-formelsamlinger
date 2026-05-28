# PLAN.md

Build or rewrite a universal exam-friendly LaTeX formula collection.

The plan must work for any course where the project provides exams, lectures, exercises, or similar source material. Do not assume any specific subject in advance.

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
- infer the lecture or topic order
- infer standard notation and terminology
- infer the exam format
- infer recurring problem types
- infer recurring keywords from problem statements
- infer which formulas are repeatedly needed

Write findings to:

- `reports/coverage_report.md`

If the `reports/` folder does not exist, create it.

## Phase 3: Build exam task taxonomy

Inspect all exam and exercise problems.

Group problems by task type rather than only by lecture topic.

For each task type, record:

- common problem wording
- important Ctrl+F keywords
- required formulas
- fastest reliable solution method
- common traps
- quick checks
- source problems that use this task type

Write the taxonomy to:

- `reports/exam_task_taxonomy.md`

Do not use a hardcoded taxonomy from another course. The taxonomy must be inferred from the project source material.

## Phase 4: Propose formula collection structure

Create a proposed list of `.tex` files for the formula collection.

Use exam-relevant topic names.

Use one file per major topic, method group, or recurring task family.

Prefer a structure that makes the document fast to use during problem solving.

Record the proposed structure in:

- `reports/coverage_report.md`

## Phase 5: Prepare LaTeX structure

- Create missing source `.tex` files.
- Preserve useful existing modular structure if present.
- Update `main.tex` so it inputs all formula source files in the correct order.
- Keep `main.tex` modular.
- Do not place substantial formula content directly in `main.tex`.

## Phase 6: Rewrite or generate content for exam use

For each topic or task family:

- keep formulas needed for solving
- keep definitions needed for correct formula use
- remove or compress long theoretical prose
- remove proofs unless essential
- remove long derivations
- add compact exam recipes
- add recognition rules
- add common traps
- add one-line checks
- add Ctrl+F keyword lines
- use terminology from source material
- include useful aliases and synonyms used in exams and lectures

The document should read like a fast problem-solving reference, not a textbook.

## Phase 7: Add exam recipes

For every recurring problem type, add a compact recipe.

Use this format when useful:

```tex
\subsection{Exam recipe: task name}

\textbf{Use when:} ...

\textbf{Steps:}
\begin{enumerate}
    \item ...
    \item ...
    \item ...
\end{enumerate}

\textbf{Fast checks:} ...

\textbf{Common traps:} ...
```

Keep each recipe short and actionable.

Do not add generic recipes that are not supported by the source material.

## Phase 8: Add searchability layer

Audit headings and keyword lines for Ctrl+F usability.

For each recurring problem type, ensure that at least one heading or keyword line includes:

- the formal topic name
- common exam wording
- common abbreviations
- common notation
- useful synonyms
- relevant terms in the source language or languages

Avoid vague headings such as:

- Main result
- Important formula
- Theory
- Method

Use explicit headings such as:

- Formula name
- Problem type
- Input/output relation
- Transformation rule
- Stability test
- Error estimate
- Optimization condition
- Boundary condition

The exact headings must be inferred from the course material.

## Phase 9: Compile

- Compile `main.tex`.
- Fix LaTeX errors.
- Repeat until the document compiles, or until only non-critical warnings remain.

If the project has a build script or Makefile, use it.

## Phase 10: Exam verification

Inspect each exam and exercise set again.

For each problem, map it to:

- problem type
- required formulas
- fastest method
- formula collection section
- recipe section
- missing content, if any

Update:

- `reports/exam_verification_report.md`

Suggested table:

| Source | Problem | Problem type | Fast method | Covered in section | Missing recipe? |
|---|---|---|---|---|---|

If any problem cannot be solved efficiently using the formula collection, add or improve a compact recipe and recompile.

## Phase 11: Final cleanup

- Remove unnecessary duplication.
- Ensure notation is consistent with the source material.
- Ensure headings are searchable.
- Ensure recipes are short.
- Ensure the document is not lecture-note style.
- Ensure `main.tex` includes all generated files.
- Compile one final time.

## Final deliverables

The final project should contain:

- updated modular `.tex` source files
- updated `main.tex` if needed
- compiled PDF if the project supports compilation
- `reports/coverage_report.md`
- `reports/exam_task_taxonomy.md`
- `reports/exam_verification_report.md`

## Stop condition

Do not stop after planning.

The task is complete only when:

- the formula collection has been rewritten or generated
- the LaTeX document compiles
- the exam verification report maps problems to usable sections
- missing exam recipes have been added
