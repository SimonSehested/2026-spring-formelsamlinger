# PLAN.md

Build or rewrite a universal printed 4-page A4 exam backup sheet in LaTeX.

The plan must work for any course where the project provides exams, lectures, exercises, or similar source material.

Do not assume any specific subject in advance.

The final compiled PDF must be exactly 4 A4 pages.

The sheet is for physical printing, not digital search.

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
- infer recurring mistakes or ambiguity points
- infer which formulas are repeatedly needed
- infer which conditions, assumptions, sign conventions, and checks are high-value

Write findings to:

- `reports/coverage_report.md`

If the `reports/` folder does not exist, create it.

Keep this report concise. It is a working note, not part of the 4-page sheet.

## Phase 3: Build exam uncertainty taxonomy

Inspect exam and exercise problems.

Group problems by what the student is likely to become uncertain about during the exam.

For each task or uncertainty type, record:

- recurring problem wording
- required formula or rule
- when the formula applies
- assumptions and conditions
- sign conventions
- common traps
- fast plausibility checks
- source problems that use this task type
- priority for inclusion on a 4-page sheet

Write the taxonomy to:

- `reports/exam_task_taxonomy.md`

Do not use a hardcoded taxonomy from another course.

## Phase 4: Rank content by 4-page value

Before writing the sheet, rank candidate content.

Use this priority order:

1. Recurring exam methods and formulas.
2. Formulas where misuse causes wrong answers.
3. Conditions, assumptions, domains, signs, units, and boundary cases.
4. Short exam recipes for common task types.
5. Fast sanity checks.
6. Definitions that prevent ambiguity.
7. Rare formulas only if there is remaining space.

Mark low-value or rare content as excluded rather than forcing it into the sheet.

Do not optimize for complete lecture coverage.

## Phase 5: Propose formula sheet structure

Create a proposed list of `.tex` files for the formula sheet.

Use one file per major topic, method group, or recurring task family.

Prefer a structure that makes the printed sheet fast to browse visually.

Record the proposed structure in:

- `reports/coverage_report.md`

A good structure should fit naturally into exactly 4 pages.

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
\usepackage[a4paper,margin=0.8cm]{geometry}
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
```

Use 2 or 3 columns depending on readability and page count.

## Phase 7: Draft the 4-page sheet

For each topic or task family:

- keep formulas needed for solving recurring problems
- keep definitions needed to avoid ambiguity
- include when-to-use conditions
- include assumptions
- include sign conventions
- include common traps
- include one-line plausibility checks
- include compact exam recipes
- use terminology from the source material
- avoid long explanations

The document should read like a printed exam safety net, not like notes.

Use compact labels:

- `Formula`
- `Use`
- `Condition`
- `Trap`
- `Check`
- `Units`
- `Sign`
- `Boundary`
- `Recipe`

## Phase 8: Add compact recipes

For every recurring problem type that deserves space, add a compact recipe.

Use this format when useful:

```tex
\subsection*{Task: task name}

\textbf{Use:} recognition cue.

\begin{enumerate}[leftmargin=*,nosep]
    \item Step 1.
    \item Step 2.
    \item Step 3.
\end{enumerate}

\textbf{Trap:} ...
\textbf{Check:} ...
```

Keep each recipe short and actionable.

Do not add generic recipes that are not supported by the source material.

## Phase 9: Add visual navigation layer

Audit the sheet for paper usability.

Ensure:

- clear topic headings
- consistent formatting
- compact tables where useful
- no dense paragraphs
- enough visual separation between topics
- important formulas are easy to spot
- high-risk traps and conditions stand out
- the student can quickly flip to the right area

Do not add keyword-only headings for Ctrl+F.

## Phase 10: Compile and measure page count

Compile `main.tex`.

Check the compiled PDF page count.

The PDF must be exactly 4 pages.

If the PDF is longer than 4 pages:

- compress prose
- merge formulas
- remove low-priority content
- replace lists with tables
- remove repeated explanations
- reduce spacing carefully
- adjust columns and margins if readability remains acceptable

If the PDF is shorter than 4 pages:

- add high-value exam backup material
- add traps
- add checks
- add conditions
- add boundary cases
- add notation reminders
- add compact recipes
- add recurring formula variants

Repeat until the compiled PDF is exactly 4 pages.

## Phase 11: Exam verification under page budget

Inspect each exam and exercise set again.

For each problem, map it to:

- problem type
- required formulas or methods
- likely uncertainty points
- whether the sheet supports it
- whether missing content is worth including
- whether missing content is excluded due to page budget

Update:

- `reports/exam_verification_report.md`

Suggested table:

| Source | Problem | Required concept | Support on 4-page sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|

If a recurring high-value uncertainty is missing, add or improve a compact rule, formula, trap, or recipe and recompile.

If rare content is missing, mark it as excluded.

Do not exceed 4 pages.

## Phase 12: Final cleanup

- Remove unnecessary duplication.
- Ensure notation is consistent with the source material.
- Ensure headings support fast visual lookup.
- Ensure recipes are short.
- Ensure the document is readable when printed.
- Ensure the document is not lecture-note style.
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

- the formula sheet has been rewritten or generated
- the LaTeX document compiles
- the compiled PDF is exactly 4 A4 pages
- the document is visually usable on paper
- the exam verification report maps problems to the sheet or explicitly excludes them due to page budget
