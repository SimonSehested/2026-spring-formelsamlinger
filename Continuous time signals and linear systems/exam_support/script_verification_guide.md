# Script Verification Guide

Every generated Python function must be validated before it is considered part of the exam toolbox.

Validation does not need to prove mathematical completeness. It must show that the function imports, runs, returns plausible output, and matches at least one known, simple, or source-derived case.

## Required report

Create or update:

- `reports/script_verification_report.md`.

Use a table like:

| Function | File | Category | Validation command | Test input | Expected/plausible output | Result | Limitations |
|---|---|---|---|---|---|---|---|

## Minimum validation

For each generated function:

1. Import the module.
2. Call the function with representative input.
3. Check that the output type and shape are correct.
4. Check at least one simple known case, source-derived example, or internal consistency condition.
5. Record the result.

For each generated file:

- run import checks,
- run syntax checks,
- run any local smoke checks.

At project level, run:

```bash
python -m compileall scripts
```

If a validation runner exists, run:

```bash
python scripts/validate_scripts.py
```

If tests exist, run:

```bash
pytest
```

Only record commands that were actually run.

## Validation sources

Use the strongest available validation source:

1. official solution sets,
2. solved examples from lectures,
3. old exam solutions,
4. exercises with known answers,
5. simple constructed examples,
6. mathematical identities,
7. comparison between independent methods,
8. limiting cases or dimensional checks.

If no official answer exists, mark validation as based on constructed or consistency checks.

## Status values

Use these status values:

- `validated`: function ran and matched expected or plausible output,
- `partially_validated`: function ran, but validation coverage is weak,
- `failed`: function failed and needs fixing,
- `removed`: function was removed after failing or being judged low value,
- `needs_review`: function likely useful but insufficiently validated.

Do not leave failed functions in the toolbox unless clearly marked as not for exam use.

## Failure handling

If a function fails:

1. inspect the error,
2. fix the function if the task remains valuable,
3. rerun validation,
4. update the report,
5. update note references if function names or paths changed.

If the function cannot be fixed quickly and reliably:

- remove it from normal use,
- remove or mark note references,
- record it in `script_inventory.md` as `removed` or `rejected`.

## Plausibility checks

Use checks appropriate to the course. Examples include:

- dimensions and matrix shapes,
- units,
- sign and domain constraints,
- known special cases,
- residual size,
- conservation laws,
- probabilities between 0 and 1,
- monotonicity,
- convergence diagnostics,
- symbolic simplification equivalence,
- numerical comparison to an alternative method,
- plot axes and labels.

Infer the relevant checks from the course material.

## Script inventory consistency

After validation, ensure `reports/script_inventory.md` includes:

- function path,
- function name,
- category,
- source task types,
- validation status,
- risk level,
- note reference,
- limitations,
- rejected or removed candidates.

## Notes consistency

After validation, scan the LaTeX notes for Python references.

For every reference:

- file exists,
- function exists,
- function imported successfully,
- validation status is not `failed`,
- assumptions match note wording.

If a script was removed, update the notes.

## Final script verification statement

At the end of `reports/script_verification_report.md`, include a short final statement:

- commands run,
- number of functions validated,
- number partially validated,
- number removed or rejected,
- known limitations,
- whether the toolbox is ready for exam use.

Be honest. Do not overstate reliability.
