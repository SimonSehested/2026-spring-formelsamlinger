# Chemistry Exam Tools

Small standard-library Python toolbox derived from the calculation-bearing tasks in
the supplied `26020/26021` and `26030` chemistry exams.

## Use

Run from this folder; no installation or third-party runtime dependency is needed:

```powershell
python -c "from exam_tools import *; print(molar_mass('NaBr'))"
python -m unittest discover -s tests -v
```

In a notebook or script:

```python
from exam_tools import *

# Saturated Mg(OH)2, Ksp = 5.61e-12
s = solubility_from_ksp(5.61e-12, (1, 2))
ph = 14.0 + __import__("math").log10(2 * s)

# Concentration cell: Ni2+ high/low concentrations
q = 3e-5 / 0.5
voltage_v = cell_potential(0.0, 2, q)
```

Open `exam_toolbox.ipynb` for the final Danish working notebook with editable
examples and an exam-task index.

## Final API

The aggressively consolidated public API contains 10 functions:

```python
arrhenius_ratio
cell_potential
clausius_clapeyron_pressure
equilibrium_constant
ideal_gas
kinetic_linear_fit
molar_mass
solubility_from_ksp
unit_cell_volume
weak_solution_ph
```

## Files

| File | Purpose |
|---|---|
| `exam_tools/chemistry.py` | Implementation of the final public calculation API. |
| `exam_tools/__init__.py` | Public exports for `from exam_tools import *`. |
| `tests/test_exam_tools.py` | Exam-value tests for every public function. |
| `processing_plan.md` | Exam order, source grouping and decision rules. |
| `coverage_table.md` | One row per identifiable task/subtask. |
| `processing_log.md` | Per-exam decisions and verification history. |
| `function_inventory.md` | Final function catalogue and API rationale. |
| `exam_toolbox.ipynb` | Practical notebook interface. |

## Scope

The package performs only calculations that benefit from reusable implementation:
formula parsing, gas/electrochemical equations, nonlinear equilibrium solving and
data reduction. Short textbook arithmetic such as Henderson-Hasselbalch,
`Delta G = Delta H - T Delta S`, colligative shifts and signed enthalpy sums is
left visible in notebook cells. It intentionally does not automate Lewis structures,
VSEPR recognition, reaction balancing, nomenclature, periodic trends, or organic
isomer enumeration.
