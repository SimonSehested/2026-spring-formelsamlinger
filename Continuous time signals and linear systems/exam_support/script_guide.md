# Script Guide for Exam Python Toolbox

## Purpose

Generate Python functions that help solve or check recurring exam task types.

The scripts are not a programming project for its own sake. They are an exam-speed toolbox.

The student will open the files in VSCode and call individual functions from a notebook. Internet must not be required.

## Admission test

Before writing a function, determine whether it should exist.

A function is admitted only if it satisfies at least one of:

- recurring in old exams or exercises,
- solves a whole stable task type,
- reduces long arithmetic, algebra, simulation, optimization, plotting, or table work,
- checks a manual answer,
- produces a required plot or diagnostic,
- converts between representations used repeatedly,
- prevents common computational mistakes.

Reject a function if:

- the task is mainly conceptual or proof-based,
- the input format is unclear,
- the result depends on interpretation not captured by parameters,
- manual solution is faster and safer,
- it only solves one old exam problem with no recurring pattern,
- it cannot be validated,
- it hides important assumptions.

Record admitted and rejected candidates in `reports/script_inventory.md`.

## Function style

Write importable functions, not only scripts.

Use:

- clear function names,
- type hints where practical,
- concise docstrings,
- explicit assumptions,
- input validation,
- deterministic outputs,
- common scientific packages when useful,
- short examples in docstrings,
- no internet access,
- no hidden file dependencies unless documented.

Avoid:

- long printed explanations,
- interactive `input()` prompts,
- hardcoded exam numbers,
- fragile parsing of natural language,
- excessive global state,
- unnecessary classes,
- notebook-only code,
- obscure packages unless clearly needed.

## File organization

Organize scripts by inferred topic or task family:

```text
scripts/
  __init__.py
  linear_algebra/
    __init__.py
    eigen_tasks.py
    matrix_checks.py
  statistics/
    __init__.py
    hypothesis_tests.py
  validate_scripts.py
```

Use the actual topic names inferred from the course. The example above is not a template for all courses.

Prefer one file per coherent task family. Do not create one huge file.

## Function naming

Use descriptive English names.

Good:

```python
solve_linear_system(...)
check_matrix_diagonalizable(...)
fit_ols_and_predict(...)
plot_bode_response(...)
compute_confidence_interval(...)
```

Bad:

```python
task1(...)
exam_solver(...)
calculate(...)
main(...)
```

## Inputs

Inputs must be explicit and notebook-friendly.

Prefer:

- numbers,
- lists,
- NumPy arrays,
- SymPy expressions,
- Pandas DataFrames,
- named keyword arguments,
- simple dictionaries when many named parameters are needed.

Validate inputs for:

- shape,
- dimension,
- domain,
- missing values,
- sign constraints,
- singular matrices,
- invalid probabilities,
- invalid parameter ranges,
- unsupported modes.

Raise informative `ValueError` messages for invalid inputs.

## Outputs

Return compact answers.

Acceptable outputs include:

- scalar values,
- vectors,
- matrices,
- SymPy expressions,
- Pandas DataFrames,
- Matplotlib figure/axis objects,
- dictionaries with named result fields,
- booleans plus diagnostic values.

Do not print long explanations by default.

If the function returns a dictionary, use stable and descriptive keys.

Example:

```python
{
    "estimate": ..., 
    "standard_error": ..., 
    "test_statistic": ..., 
    "p_value": ..., 
    "reject": ...
}
```

## Symbolic vs numerical behavior

Use symbolic computation when exact formulas or expressions are useful.

Use numerical computation when the exam task is computational, approximate, data-driven, simulation-based, plotting-based, or too slow by hand.

When relevant, allow a parameter such as:

```python
exact: bool = False
```

or separate symbolic and numerical functions if that is clearer.

## Plotting functions

Plotting functions should:

- return `(fig, ax)` or `ax`,
- not call `plt.show()` unless explicitly requested by an argument,
- label axes,
- include units when known,
- avoid unnecessary styling,
- be usable inside notebooks.

## Dependencies

Use common packages when useful:

- `numpy`,
- `scipy`,
- `sympy`,
- `pandas`,
- `matplotlib`,
- `statsmodels`,
- `scikit-learn`,
- other course-relevant packages if justified.

Create or update `requirements.txt`.

Do not require internet at exam time. Dependencies must be installable before the exam.

## Docstring format

Use concise docstrings:

```python
def function_name(...):
    """
    Solve/check [task type].

    Use when:
        [recognition rule]

    Parameters:
        ...

    Returns:
        ...

    Assumptions:
        ...

    Example:
        >>> function_name(...)
        ...
    """
```

Keep examples short.

## Notebook use

Ensure functions can be imported from a notebook:

```python
from scripts.topic.file import function_name
```

If imports require repository root setup, include a short example file showing how to run from the root directory.

## Validation

Every generated function must be run at least once with representative input.

Validation can be implemented with:

- `scripts/validate_scripts.py`,
- lightweight `pytest` tests,
- smoke checks in each file,
- examples executed from a validation runner.

Minimum validation for each function:

- import succeeds,
- representative call succeeds,
- output has expected type or shape,
- at least one known or simple case gives a plausible result.

Record validation in `reports/script_verification_report.md`.

Do not claim a function is verified unless it was actually run.

## Error handling

Prefer explicit failure over silent wrong results.

Raise clear exceptions for:

- invalid dimensions,
- singular systems where inversion is requested,
- non-convergence,
- invalid probability ranges,
- unsupported assumptions,
- missing required inputs.

If numerical methods may fail, return diagnostic information or expose tolerance/max-iteration parameters.

## Script inventory

For every generated or rejected candidate, record:

| Function or candidate | Category | Source task types | Status | Validation | Notes reference | Risk | Reason |
|---|---|---|---|---|---|---|---|

Status values:

- `generated`,
- `validated`,
- `partially_validated`,
- `rejected`,
- `removed`,
- `needs_review`.

Risk values:

- `low`,
- `medium`,
- `high`.

High-risk functions must either be improved, clearly documented, or removed.

## Relationship to notes

Every generated function must be referenced from at least one note recipe or the script index.

Every note reference must point to an existing function.

If a function is useful but dangerous, the note must state when not to use it.

## Final cleanup

Before finishing:

- remove dead functions,
- remove unvalidated functions,
- update `__init__.py` files,
- update dependency file,
- run compile/import checks,
- run validation checks,
- update script inventory,
- update note references.
