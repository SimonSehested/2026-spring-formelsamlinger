# AGENTS.md

You are building or rewriting a LaTeX formula collection for the course described by the project source material.

## Goal

Create a printed 4-page A4 exam backup sheet.

The final compiled PDF must be exactly 4 A4 pages.

This is not a digital Ctrl+F reference. It is a physical printed aid for use during an exam.

The document must help the student quickly regain confidence when uncertain about:

- which formula applies
- which assumptions must hold
- sign conventions
- notation
- boundary cases
- units and dimensions
- common traps
- fast plausibility checks
- short solution procedures for recurring task types

The document must not become:

- lecture notes
- a textbook summary
- a proof-based theory document
- a complete coverage document
- a long formula catalogue

The primary user situation is:

- the student is sitting in a physical exam
- the student cannot search digitally
- the student needs to visually locate the relevant topic quickly
- the student needs confirmation, not explanation
- the student wants confidence that their method, assumptions, signs, and result are reasonable

## Source material

Use the source material provided by the project. Typical project inputs may include files such as:

- `input/exams/`
- `input/lectures/`
- `input/exercises/`
- `source_material/exams/`
- `source_material/slides/`
- `source_material/lectures/`
- `source_material/exercises/`

First inspect the available folders and infer the actual course title, topics, notation, terminology, exam format, and recurring problem types.

Do not assume a fixed course, topic list, notation system, or exam style in advance.

Do not invent unsupported formulas or topics unless they are standard prerequisites clearly required to solve recurring exam or exercise problems.

If something is uncertain, mark it with:

    % TODO: verify from source

## Core principle

Every item on the sheet must answer at least one of these questions:

1. What formula or rule do I need right now?
2. When is this formula allowed?
3. What sign convention or notation detail might I forget?
4. What common mistake should I avoid?
5. How can I quickly check whether my answer is plausible?
6. What is the shortest reliable method for this recurring task?

If an item does not support one of these questions, remove it.

## 4-page print constraint

The compiled PDF must be exactly 4 A4 pages.

This is a hard requirement.

If the document is longer than 4 pages:

- remove long prose
- remove proofs and derivations
- merge duplicate formulas
- convert explanations into labels such as `Condition`, `Trap`, `Check`
- replace long recipes with compact tables
- remove rare formulas
- remove low-value definitions
- remove content included only for completeness
- reduce vertical whitespace before reducing readability

If the document is shorter than 4 pages:

- add high-value uncertainty support
- add common traps
- add assumptions and conditions
- add sign/unit/domain checks
- add edge cases
- add compact decision rules
- add recurring task recipes
- add notation reminders
- add formula variants that students often confuse

Do not stop until the compiled PDF is exactly 4 pages.

## Output files

Create or update modular LaTeX source files in the project’s formula-collection source directory, typically:

- `sources/`
- `sections/`
- `chapters/`

Use the existing project structure if one exists. If no structure exists, create a `sources/` directory.

Use one `.tex` file per major exam-relevant topic or task family inferred from the source material.

Use clear numbered filenames such as:

    01_topic_name.tex
    02_topic_name.tex
    03_topic_name.tex

Topic names must be inferred from the provided source material, not hardcoded from another course.

Do not write large amounts of formula content directly in `main.tex`.

Keep `main.tex` modular and use `\input{...}` or `\include{...}`.

## Organization for paper lookup

Organize for visual navigation on printed paper.

Prefer a structure that lets the student quickly flip to the right area:

- broad topic headings
- compact subsections
- visually consistent blocks
- tables for formula families
- boxed high-risk rules
- short labels such as `Use`, `Condition`, `Trap`, `Check`

Do not optimize for Ctrl+F.

Do not add keyword-only headings just for searchability.

Use clear, human-readable headings that make sense on paper.

Good headings:

```tex
\section*{Fourier and Laplace transforms}
\subsection*{Transform pairs}
\subsection*{Differentiation and integration rules}
\subsection*{Initial and final value checks}
```

Bad headings:

```tex
\subsection*{misc keywords search terms}
\subsection*{important theory}
\subsection*{main result}
```

## Content priority

Prioritize content in this order:

1. Recurring exam methods and formulas.
2. Formulas where misuse causes wrong answers.
3. Conditions, assumptions, domains, signs, units, and boundary cases.
4. Short exam recipes for common task types.
5. Fast sanity checks.
6. Definitions that prevent ambiguity.
7. Rare formulas only if there is remaining space.

When forced to choose, prefer one compact decision rule that prevents several common mistakes over several isolated rare formulas.

## Recommended block format

Use compact blocks such as:

```tex
\subsection*{Topic or task}

\textbf{Formula:}
\[
...
\]

\textbf{Use:} ...
\textbf{Condition:} ...
\textbf{Trap:} ...
\textbf{Check:} ...
```

Do not force all labels if they add noise.

For families of related results, prefer tables:

```tex
\begin{tabularx}{\linewidth}{@{}lX@{}}
\textbf{Case} & \textbf{Rule / formula} \\
...
\end{tabularx}
```

## Exam recipes

For recurring exam or exercise task types, create compact recipes.

A recipe should usually have this form:

```tex
\subsection*{Task: name}

\textbf{Use:} short recognition cue.

\begin{enumerate}[leftmargin=*,nosep]
    \item Step 1.
    \item Step 2.
    \item Step 3.
\end{enumerate}

\textbf{Trap:} ...
\textbf{Check:} ...
```

Keep recipes short, normally 2--5 steps.

A recipe is better than a derivation.

## Style

Use concise mathematical reference style:

- no long prose
- no proofs
- no long derivations
- no historical or motivational explanations
- no lecture-note summaries
- no large paragraphs
- no Markdown inside `.tex` files
- no duplicated formulas unless needed to prevent mistakes
- no examples unless they prevent a recurring error

Prefer:

- compact formula blocks
- short tables
- assumption lists
- condition labels
- common-trap labels
- sanity checks
- decision rules
- visual grouping

## Layout

The PDF must be printable and readable.

Prefer:

- A4 paper
- small but readable font
- 2 or 3 columns
- narrow margins
- compact spacing
- clear section separators
- minimal whitespace
- no decorative graphics

Do not make the text so small that it is uncomfortable to read during an exam.

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

Adjust layout only if needed to reach exactly 4 pages while remaining readable.

## Multiple-choice and exam-strategy support

If the exam format includes multiple choice, true/false statements, numerical answer options, or one-best-answer logic, include compact elimination rules and answer-checking strategies.

Examples of useful rules:

- one false clause makes a statement false
- check limiting cases
- check units and dimensions
- check signs and domains
- check assumptions before using a formula
- test boundary cases
- eliminate answers with impossible units or signs

Only include rules supported by the observed exam format.

## Coverage and selection

Inspect exams and exercises to identify recurring problem types.

For each recurring type, determine:

1. problem type
2. required formulas or definitions
3. fastest reliable method
4. common mistakes
5. whether it deserves space on the 4-page sheet

Do not add material solely because it exists in the lecture slides.

Do not attempt full coverage if full coverage conflicts with the 4-page limit.

If a source item is excluded because of the page budget, that is acceptable.

## Reports

Create or update concise reports in `reports/`:

- `coverage_report.md`
- `exam_task_taxonomy.md`
- `exam_verification_report.md`

Reports are working notes. They must not cause the formula sheet to grow beyond 4 pages.

In the verification report, mark excluded material explicitly, for example:

    Excluded: rare / low exam frequency / derivable / not worth 4-page space

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
- ensure the document is readable when printed
- ensure headings support fast visual lookup
- ensure the document is not lecture-note style

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
