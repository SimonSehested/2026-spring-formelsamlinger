# Notes and Python Script Integration Guide

The LaTeX formula collection is the primary exam reference.

Python scripts are secondary tools that support recurring exam task types. They must never replace formulas, definitions, assumptions, method-selection rules, recipes, common traps, or fast checks in the notes.

## Core hierarchy

1. The PDF/LaTeX notes are primary.
2. Python scripts are secondary aids.
3. Script references may supplement note sections.
4. Script references must never replace note content.
5. Every relevant note section must remain useful even if Python is unavailable.

## Core rule

A script may be referenced in the notes only after the relevant LaTeX section contains:

1. Recognition keywords.
2. The required formula, definition, or method.
3. Assumptions and conditions for use.
4. A compact exam recipe when the task is procedural.
5. Fast checks or common traps when relevant.

Only then may the section include a script reference.

## Purpose of script references

Script references must answer:

- When should I use this script?
- What task type does it solve?
- What inputs do I need from the exam problem?
- What output should I expect?
- What must I check manually before trusting the output?
- When should I not use it?

## Required LaTeX format

Use this compact format inside the relevant recipe or concept section:

```tex
\textbf{Python aid:} Use \texttt{scripts/path/to/script.py} when the problem asks for [specific task type] and the required inputs are [specific inputs]. The script returns [specific output]. Check [manual condition/check] before using the result.
```

For more complex cases, use:

```tex
\textbf{Python aid.}
Use \texttt{scripts/path/to/script.py} when:
\begin{itemize}
    \item the problem asks for ...
    \item the given inputs are ...
    \item the task is computational rather than conceptual.
\end{itemize}
The script returns ...
Check manually that ...
Do not use it when ...
```

Keep script references compact. Do not let them dominate the notes.

## Script reference requirements

A script may be referenced only if:

- the file exists
- the relevant function exists
- it is usable from a notebook
- it has been run successfully
- it appears in `reports/script_inventory.md`
- it appears in `reports/script_validation_report.md`
- its intended task type matches the LaTeX section

Do not reference unvalidated scripts.

## Notes must remain self-contained

Bad:

```tex
\subsubsection{Eigenvalues}
Use \texttt{scripts/linear_algebra/eigenvalues.py}.
```

Good:

```tex
\subsubsection{Eigenvalues and characteristic polynomial}
\[
\det(A-\lambda I)=0
\]
The eigenvalues are the roots of the characteristic polynomial. They determine invariant directions and often control stability, diagonalization, or principal modes.

\textbf{Python aid:} Use \texttt{scripts/linear_algebra/eigenvalues.py} when the exam gives a numeric matrix and asks for eigenvalues or a quick spectral check. Check matrix dimensions and whether exact symbolic eigenvalues are required before relying on numerical output.
```

## When to reference scripts

Reference scripts for:

- repeated numerical computations
- symbolic algebra that is tedious but standard
- matrix calculations
- equation solving
- optimization computations
- probability/statistics formulas
- plotting or graph interpretation
- numerical sanity checks
- simulation-style task types
- recurring exam task types where automation saves time

Do not reference scripts for:

- purely conceptual questions
- proof questions
- tasks where method choice is the main challenge
- tasks where the script assumptions are hard to verify
- one-off scripts with no recurring task type
- unvalidated scripts

## Required task categories

Use these categories consistently:

- `notes_only`: solved from formulas, definitions, and recipes. No script reference.
- `script_assisted`: notes explain the method; script helps compute, verify, plot, simplify, or check.
- `script_primary`: script can solve a well-defined recurring task type directly, but notes must still state assumptions and checks.

## Report consistency

When a LaTeX section references a script, ensure the reports are consistent:

- `reports/script_inventory.md` must list the script.
- `reports/script_validation_report.md` must show that it runs.
- `reports/exam_verification_report.md` must mark the relevant problem type as `script_assisted` or `script_primary`.
- `reports/exam_task_taxonomy.md` must contain the corresponding task type.

## Required integration report

Create or update:

```text
reports/script_note_integration_report.md
```

Use this table format:

```markdown
| Script | Function | LaTeX section | Task category | When to use | Required inputs | Output | Manual check | Do not use when |
|---|---|---|---|---|---|---|---|---|
```

Every script referenced in the notes must appear in this report.

## Final audit

Before finishing, audit every script reference in the notes:

1. Does the referenced file exist?
2. Is the referenced function usable from a notebook?
3. Has it been validated?
4. Does the LaTeX section explain when to use it?
5. Does the LaTeX section explain what input is needed?
6. Does the LaTeX section explain what output is returned?
7. Does the LaTeX section explain what to check manually?
8. Would the section still be useful if Python failed?

If any answer is no, fix the note or remove the script reference.

## Anti-patterns

Do not do this:

- Do not replace formulas with script references.
- Do not make the PDF a script index.
- Do not reference every script automatically.
- Do not reference scripts that are merely convenient but exam-irrelevant.
- Do not let Python-specific concerns override the LaTeX style guide.
- Do not expand notes into long programming explanations.
- Do not include Python code blocks inside the LaTeX notes unless explicitly required.
