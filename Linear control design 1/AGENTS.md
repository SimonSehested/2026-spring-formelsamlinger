# AGENTS.md

You are building or rewriting a LaTeX formula collection for the course described by the project source material.

## Goal

Create a compact, searchable, exam-friendly formula collection.

The document must function as a Ctrl+F problem-solving reference during exam preparation and exams. It must not become a textbook, lecture summary, or proof-based theory document.

The primary user situation is:

- the student is solving an exam-style problem
- the student recognizes a task type or keyword from the problem statement
- the student needs the relevant formula, decision rule, or solution recipe immediately
- the student does not want long derivations, proofs, or lecture-style explanations

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

Do not invent unsupported formulas or topics unless they are standard prerequisites clearly required to solve the exam or exercise problems.

If something is uncertain, mark it with:

    % TODO: verify from source

## Core principle

Every section must help answer at least one of these questions:

1. What type of problem is this?
2. Which formula do I need?
3. What is the fastest reliable solution method?
4. What assumptions or conditions must hold?
5. What common trap should I avoid?
6. How can I quickly check whether an answer is plausible?

## Output files

Create or update modular LaTeX source files in the project’s formula-collection source directory, typically:

- `sources/`
- `sections/`
- `chapters/`

Use the existing project structure if one exists. If no structure exists, create a `sources/` directory.

Use one `.tex` file per major exam-relevant topic inferred from the source material.

Use clear numbered filenames such as:

    01_topic_name.tex
    02_topic_name.tex
    03_topic_name.tex

Topic names must be inferred from the provided source material, not hardcoded from another course.

Do not write large amounts of formula content directly in `main.tex`. Keep `main.tex` modular and use `\input{...}` or `\include{...}`.

## Organization

Organize primarily for exam usability.

This may follow lecture order if lecture order is useful. If exam problem types cut across lectures, prefer an exam-task organization or add cross-topic recipe sections.

Each topic should contain some or all of the following, when relevant:

```tex
\section{Topic name}

\subsection{Ctrl+F keywords}
...

\subsection{Core formulas}
...

\subsection{Exam recipe: specific task type}
...

\subsection{Recognition rules}
...

\subsection{Common traps}
...

\subsection{One-line checks}
...
```

Do not force every subsection if it adds noise. Use the structure when it improves speed and searchability.

## Style

Use concise engineering/mathematical reference style:

- no long prose
- no proofs unless absolutely necessary for correct use
- no long derivations
- no historical or motivational explanations
- no lecture-note summaries
- no large paragraphs
- no images unless explicitly required by the project
- no Markdown inside `.tex` files
- no duplicated formulas unless duplication improves exam usability

Prefer:

- boxed formulas
- short formula blocks
- compact tables
- short enumerated recipes
- recognition rules
- fast checks
- common traps

Use explanations only when they help the student choose or apply a formula correctly.

## Searchability

Optimize for Ctrl+F.

Use headings and keyword lines that contain words from:

- exam problem titles
- exam question wording
- lecture headings
- exercise headings
- common synonyms
- notation used in the course

When the course uses multiple languages, include useful aliases from those languages.

Example:

```tex
\subsection{Impulse response, impulsrespons, delta input, direct feedthrough}
```

Good headings:

```tex
\subsubsection{Transfer function from differential equation}
\subsubsection{Impulse response from transfer function}
\subsubsection{Direct feedthrough and delta impulse term}
\subsubsection{Bode plot slope to poles and zeros}
\subsubsection{Stability from pole locations}
```

Bad headings:

```tex
\subsubsection{Main result}
\subsubsection{Important theorem}
\subsubsection{Theory}
```

## Exam recipes

For every recurring exam or exercise task type, create a compact recipe.

A recipe should usually have this form:

```tex
\subsection{Exam recipe: task name}

\textbf{Use when:} short description.

\textbf{Steps:}
\begin{enumerate}
    \item Step 1.
    \item Step 2.
    \item Step 3.
\end{enumerate}

\textbf{Fast checks:} short checks.

\textbf{Common traps:} short traps.
```

Keep recipes short, normally 3--7 steps.

A recipe is better than a derivation.

## Multiple-choice and exam-strategy support

If the exam format includes multiple choice, true/false statements, numerical answer options, or one-best-answer logic, include compact elimination rules and answer-checking strategies.

Examples of useful rules:

- If one clause in an answer option is false, the whole option is false.
- Check limiting cases before doing full algebra.
- Check units and dimensions.
- Check signs, domains, assumptions, and boundary cases.
- Check whether special cases invalidate a general statement.

Only include rules supported by the observed exam format.

## Coverage verification

After writing or rewriting the formula collection, inspect the exams and exercises.

For each problem, determine:

1. problem type
2. required formulas or definitions
3. fastest reliable method
4. formula collection section that supports it
5. whether a searchable recipe exists
6. missing content, if any

Create or update a report such as:

- `reports/exam_verification_report.md`

Suggested table:

| Source | Problem | Problem type | Fast method | Covered in section | Missing recipe? |
|---|---|---|---|---|---|

If a problem cannot be solved quickly using the formula collection, add or improve a compact recipe in the relevant `.tex` file.

## Coverage report

Create or update a report such as:

- `reports/coverage_report.md`

Include:

- detected source files
- inferred course title
- inferred topic structure
- recurring exam and exercise concepts
- standard notation
- proposed output structure
- known uncertainties

## LaTeX quality

The final document must compile.

Before finishing:

- run the LaTeX build if available
- fix compile errors
- check for undefined references
- check for missing input files
- check for broken math syntax
- ensure `main.tex` inputs all generated files in the correct order
- ensure the document is not lecture-note style
- ensure headings and keyword lines are searchable

## Do not

- do not assume a fixed course structure
- do not hardcode topics from another course
- do not write textbook chapters
- do not include long proofs
- do not include long derivations
- do not include unsupported material
- do not duplicate formulas unnecessarily
- do not place raw notes in final files
- do not make the document longer just to appear complete
- do not remove useful formulas unless replacing them with more exam-usable equivalents
