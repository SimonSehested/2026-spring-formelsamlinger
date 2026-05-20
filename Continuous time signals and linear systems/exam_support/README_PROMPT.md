# README_PROMPT.md

Use these markdown files as the instruction set for Claude Code when building an exam-preparation repository.

## Intended workflow

Start from a fresh folder containing course material such as:

```text
input/
  exams/
  solutions/
  lectures/
  slides/
  exercises/
```

Folder names do not have to match exactly. Claude Code must inspect the repository and infer the structure.

Copy this prompt pack into the repository root:

```text
AGENTS.md
PLAN.md
style_guide.md
script_guide.md
verification_guide.md
script_verification_guide.md
```

Then ask Claude Code to follow `AGENTS.md` and `PLAN.md` until the stop condition is satisfied.

## Expected outputs

Claude Code should produce:

- a compact PDF reference collection,
- modular LaTeX source files,
- validated Python functions under `scripts/`,
- a dependency file,
- a short import/demo file or notebook if useful,
- reports connecting exam task types to notes and scripts.

## Important behavior

Claude Code must:

- infer the course from source material,
- avoid internet requirements,
- write notes in English,
- include useful Danish Ctrl+F keywords,
- generate Python only for justified task types,
- validate every generated function,
- remove or reject weak scripts,
- reference scripts from the relevant note recipes,
- compile the PDF if possible,
- write honest reports about limitations.

## Suggested Claude Code prompt

Use this prompt in Claude Code after adding the markdown files and source material:

```text
Follow AGENTS.md and PLAN.md exactly.

Build a general exam-preparation project from the source material in this repository.

Produce both:
1. a compact searchable PDF reference collection, and
2. validated Python functions that can solve or check recurring exam task types.

Do not assume the course topic. Infer the course, notation, task types, and computational patterns from the repository.

All notes should be in English, but include useful Danish Ctrl+F aliases from the material.

Scripts must be importable from notebooks in VSCode. Generate individual Python functions for individual recurring task types. Use scientific Python packages when useful. Internet must not be required.

Be strict and self-critical. Do not generate weak scripts. Every generated script must be validated by running it, or removed/rejected and recorded.

Do not stop after planning. Continue until the stop condition in AGENTS.md and PLAN.md is satisfied.
```

## Minimal source folder suggestion

A good starting structure is:

```text
course_project/
  AGENTS.md
  PLAN.md
  style_guide.md
  script_guide.md
  verification_guide.md
  script_verification_guide.md
  input/
    exams/
    solutions/
    lectures/
    slides/
    exercises/
```

The exact names are not required, but consistent folders improve source inspection.

## Final check

Before trusting the output, inspect:

- `reports/exam_task_taxonomy.md`,
- `reports/script_inventory.md`,
- `reports/script_verification_report.md`,
- `reports/exam_verification_report.md`,
- generated note references to Python functions,
- whether the generated scripts actually run locally.
