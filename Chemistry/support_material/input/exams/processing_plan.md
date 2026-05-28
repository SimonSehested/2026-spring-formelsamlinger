# Processing Plan: Chemistry Exam Calculation Toolbox

## Scope and source handling

This project builds a small reusable Python API only for computational support that is
justified by the exam PDFs in this folder. Marked PDFs, answer keys and solution PDFs
are companion materials for the same dated exam set, not separate exam sets. Where a
PDF page is image-based, the paired marked/solution material is used when it exposes
the task; any task that remains illegible or absent is explicitly logged as unresolved.

## Ordered exam sets

Processing order is chronological. Every set in this list will receive a processing-log
entry and coverage rows for all identifiable tasks/subtasks.

1. **26030 Winter 2021**
   - `26030 2021 Winter Answer Key.pdf` (answer key only; no corresponding question
     paper is present in this folder).
2. **26030 Winter 2022**
   - `26030 2022 Winter Exam.pdf` (exam paper).
   - `26030 2022 Winter Answer Key.pdf` (answer key).
3. **26020/26021 May 2024 (`202405`)**
   - `26020_26021_202405_exam_random_unmarked.pdf` (unmarked exam).
   - `26020_26021_202405_exam_random_marked.pdf` (marked companion).
4. **26020/26021 Winter/Fall 2024 (`202412`)**
   - `26020_26021_202412_exam_random_unmarked.pdf` (unmarked exam).
   - `26020_26021_202412_exam_random_marked.pdf` (marked companion).
   - `26020_2024_fall_exam_random_answers (1).pdf` (answer/annotation copy).
   - `26020 exam 2024F solutions.pdf` (typed solutions).
5. **26020/26021 May 2025 (`202505`)**
   - `26020_26021_202505_exam_random_unmarked.pdf` (unmarked exam).
   - `26020_26021_202505_exam_random_marked.pdf` (marked companion).
   - `ksp_solution_2025 - Copy.pdf` (annotated solution companion).
6. **26020/26021 August 2025 (`202508`)**
   - `26020_26021_202508_exam_random_unmarked.pdf` (unmarked exam).
   - `26020_26021_202508_exam_random_marked.pdf` (marked companion).
7. **26020/26021 December 2025 (`202512`)**
   - `26020_26021_202512_exam_random_unmarked.pdf` (unmarked exam).
   - `26020_26021_202512_exam_random_marked.pdf` (marked companion).

No notebooks, separate data files, or figure files were found in this exam folder at
initial inspection. Figures embedded in PDFs are treated as part of their exam file.

## Python usefulness classification

Each identifiable task or subtask is classified using these criteria:

| Classification | Criterion |
|---|---|
| `full` | Given the quantities/chemical representation stated in the task, a general numerical function or a short composition of functions can calculate the requested result or deterministically select its numerical option. |
| `partial` | Python can execute a meaningful calculation or check after a human supplies interpretation that is not reasonably represented by this minimal API, such as balanced stoichiometric coefficients, a formula parsed from an image, or a chosen chemical model. |
| `none` | The task is primarily visual recognition, nomenclature, conceptual selection, trend recall, Lewis/VSEPR interpretation, qualitative reasoning, or its question text is unavailable; a calculator API would not materially improve solving it. |

For multiple-choice tasks, computing a numeric result is `full` even though selecting
the displayed option is manual. For structural images or balancing/redox decisions,
post-interpretation arithmetic may be `partial`; the package will not attempt chemical
structure recognition or symbolic reaction balancing solely to cover one question type.

## Function minimization criteria

For each `full` or `partial` calculation pattern, make the following decision in order:

| Choice | Use when |
|---|---|
| `existing_function` | A current public function directly expresses the calculation with clear parameters and units. |
| `composition` | Two or three current public functions give a readable exam workflow without hiding required chemistry decisions. |
| `generalized_function` | A small, coherent extension to an existing public function covers the task without ambiguous parameters or task-specific branching. |
| `new_function` | No existing function or clear composition expresses a recurring or independently useful calculation pattern; its reason for being public is recorded in `function_inventory.md`. |
| `ignored` | Python usefulness is `none`, or the calculation cannot be responsibly specified from the available task text. |

Internal helpers may handle validation or routine algebra. They are not listed as
exam-facing functions and will not be demonstrated in the notebook.

## Exact `coverage_table.md` format

The file begins with a short heading and the following exact Markdown table header:

```markdown
| exam_set | task_id | short_description | python_usefulness | chosen_solution | function_or_composition | status | notes |
|---|---|---|---|---|---|---|---|
```

Requirements:

- One row per identifiable task/subtask.
- `python_usefulness` is exactly `full`, `partial`, or `none`.
- `chosen_solution` is exactly `existing_function`, `generalized_function`,
  `new_function`, `composition`, or `ignored`.
- `status` is `covered`, `not_applicable`, or `unresolved`.
- Unknown tasks from a key without a question paper are entered individually by
  question ID, with the source limitation in `notes`.

## Exact `processing_log.md` format

The file begins with `# Processing Log`, followed by one section per exam set in the
ordered list:

```markdown
## <exam set name>

- File name(s): `<file>`; `<file>`
- Tasks found: <task IDs and short identification>
- Tasks ignored and why: <task IDs plus reason, or `None`>
- Python-solvable tasks: <task IDs labeled `full`/`partial`, or `None identifiable`>
- Existing functions reused: <names, or `None`>
- Existing functions generalized: <names and change, or `None`>
- New functions added: <names and justification, or `None`>
- Compositions used: <functions and covered tasks, or `None`>
- Tests added: <test identifiers, or `None`>
- Unresolved issues: <issues, or `None`>
- Exam set complete: `yes` or `no`
```

An exam set may be complete with unresolved source limitation rows if the missing
question paper makes further classification impossible and that limitation is recorded.

## Planned package structure

The package will start with one implementation module to keep the API easy to audit;
additional modules will be introduced only if the final function set makes separation
clearer.

```text
exam_tools/
  __init__.py        # final public API exports only
  chemistry.py       # general calculation functions and private helpers
tests/
  test_exam_tools.py # tests for every public function using exam values where available
examples/
  README.md          # small runnable-use pointers if needed
README.md            # install/import/run guidance
coverage_table.md    # task-by-task mapping
function_inventory.md
processing_log.md
exam_toolbox.ipynb  # created only after API consolidation
```

Tests will use the standard-library `unittest` runner unless an already-installed test
framework becomes available. Verification commands will include:

```powershell
python -m unittest discover -s tests -v
python -c "from exam_tools import *"
```
