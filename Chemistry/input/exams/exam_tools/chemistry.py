"""General numerical chemistry calculations used across the supplied exams."""

from __future__ import annotations

from math import exp, isfinite, log, log10, sqrt
import re
from typing import Sequence

GAS_CONSTANT_J_MOL_K = 8.314462618
FARADAY_C_MOL = 96485.33212

# Standard atomic weights rounded at ordinary exam-calculation precision.
ATOMIC_MASS_G_MOL = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "K": 39.098,
    "Ca": 40.078,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Ni": 58.693,
    "Cu": 63.546,
    "Br": 79.904,
    "Ag": 107.868,
    "I": 126.904,
    "Ba": 137.327,
    "Pb": 207.2,
}

_FORMULA_TOKEN = re.compile(r"([A-Z][a-z]?|\(|\)|\d+(?:\.\d+)?)")


def _positive(name: str, value: float) -> None:
    if not isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")


def _formula_counts(formula: str) -> dict[str, float]:
    tokens = _FORMULA_TOKEN.findall(formula.replace(" ", ""))
    if "".join(tokens) != formula.replace(" ", "") or not tokens:
        raise ValueError(f"Unsupported chemical formula: {formula!r}")
    stacks: list[dict[str, float]] = [{}]
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "(":
            stacks.append({})
        elif token == ")":
            if len(stacks) == 1:
                raise ValueError(f"Unmatched parenthesis in formula: {formula!r}")
            group = stacks.pop()
            factor = 1.0
            if i + 1 < len(tokens) and tokens[i + 1][0].isdigit():
                i += 1
                factor = float(tokens[i])
            for element, count in group.items():
                stacks[-1][element] = stacks[-1].get(element, 0.0) + factor * count
        elif token[0].isdigit():
            raise ValueError(f"Unexpected number in formula: {formula!r}")
        else:
            count = 1.0
            if i + 1 < len(tokens) and tokens[i + 1][0].isdigit():
                i += 1
                count = float(tokens[i])
            stacks[-1][token] = stacks[-1].get(token, 0.0) + count
        i += 1
    if len(stacks) != 1:
        raise ValueError(f"Unmatched parenthesis in formula: {formula!r}")
    return stacks[0]


def molar_mass(formula: str) -> float:
    """Return molar mass in g/mol for a neutral formula such as ``Ca(OH)2``.

    Element symbols and parenthesized groups are supported. Charges and hydrate-dot
    notation must be removed or handled separately before calling the function.
    """

    counts = _formula_counts(formula)
    try:
        return sum(ATOMIC_MASS_G_MOL[element] * count for element, count in counts.items())
    except KeyError as exc:
        raise ValueError(f"No atomic mass available for element {exc.args[0]!r}") from exc


def ideal_gas(
    *,
    pressure_pa: float | None = None,
    volume_m3: float | None = None,
    amount_mol: float | None = None,
    temperature_k: float | None = None,
) -> float:
    """Solve ``pV=nRT`` for the single missing SI-valued argument.

    Parameters use Pa, m3, mol and K. Exactly one parameter must be ``None``; the
    return value has the unit of that missing parameter.
    """

    values = (pressure_pa, volume_m3, amount_mol, temperature_k)
    if sum(value is None for value in values) != 1:
        raise ValueError("Exactly one ideal-gas parameter must be omitted")
    for name, value in zip(("pressure_pa", "volume_m3", "amount_mol", "temperature_k"), values):
        if value is not None:
            _positive(name, value)
    if pressure_pa is None:
        return amount_mol * GAS_CONSTANT_J_MOL_K * temperature_k / volume_m3  # type: ignore[operator]
    if volume_m3 is None:
        return amount_mol * GAS_CONSTANT_J_MOL_K * temperature_k / pressure_pa  # type: ignore[operator]
    if amount_mol is None:
        return pressure_pa * volume_m3 / (GAS_CONSTANT_J_MOL_K * temperature_k)  # type: ignore[operator]
    return pressure_pa * volume_m3 / (GAS_CONSTANT_J_MOL_K * amount_mol)


def equilibrium_constant(delta_g_kj_mol: float, temperature_k: float) -> float:
    """Return dimensionless equilibrium constant from standard ``delta G`` in kJ/mol."""

    _positive("temperature_k", temperature_k)
    return exp(-1000.0 * delta_g_kj_mol / (GAS_CONSTANT_J_MOL_K * temperature_k))


def unit_cell_volume(
    density_kg_m3: float,
    molar_mass_g_mol: float,
    particles_per_cell: float,
) -> float:
    """Return crystal unit-cell volume in m3 from density and cell content.

    ``molar_mass_g_mol`` is the molar mass of one atom or formula unit and
    ``particles_per_cell`` is the number of those units in one cell.
    """

    for name, value in (
        ("density_kg_m3", density_kg_m3),
        ("molar_mass_g_mol", molar_mass_g_mol),
        ("particles_per_cell", particles_per_cell),
    ):
        _positive(name, value)
    avogadro_mol_inverse = 6.02214076e23
    cell_mass_kg = particles_per_cell * molar_mass_g_mol / 1000.0 / avogadro_mol_inverse
    return cell_mass_kg / density_kg_m3


def clausius_clapeyron_pressure(
    initial_pressure_pa: float,
    initial_temperature_k: float,
    final_temperature_k: float,
    vaporization_enthalpy_kj_mol: float,
) -> float:
    """Return vapor pressure in Pa at a second temperature.

    Uses constant molar enthalpy of vaporization and the integrated
    Clausius-Clapeyron equation.
    """

    for name, value in (
        ("initial_pressure_pa", initial_pressure_pa),
        ("initial_temperature_k", initial_temperature_k),
        ("final_temperature_k", final_temperature_k),
        ("vaporization_enthalpy_kj_mol", vaporization_enthalpy_kj_mol),
    ):
        _positive(name, value)
    exponent = -(vaporization_enthalpy_kj_mol * 1000.0 / GAS_CONSTANT_J_MOL_K) * (
        1.0 / final_temperature_k - 1.0 / initial_temperature_k
    )
    return initial_pressure_pa * exp(exponent)


def kinetic_linear_fit(
    times_s: Sequence[float],
    concentrations_m: Sequence[float],
    order: int,
) -> tuple[float, float, float]:
    """Fit an integrated rate-law transform and return ``(slope, intercept, r2)``.

    ``order`` may be 0, 1 or 2, fitting ``[A]``, ``ln([A])`` or ``1/[A]``
    against time in seconds. A value of ``r2`` close to 1 identifies the compatible
    kinetic order; slope units follow the selected transform.
    """

    if order not in {0, 1, 2}:
        raise ValueError("order must be 0, 1 or 2")
    if len(times_s) != len(concentrations_m) or len(times_s) < 2:
        raise ValueError("times_s and concentrations_m need equal length of at least two")
    if any(not isfinite(time) for time in times_s):
        raise ValueError("times_s must be finite")
    for concentration in concentrations_m:
        _positive("concentration", concentration)
    if order == 0:
        transformed = [float(value) for value in concentrations_m]
    elif order == 1:
        transformed = [log(value) for value in concentrations_m]
    else:
        transformed = [1.0 / value for value in concentrations_m]
    x_mean = sum(times_s) / len(times_s)
    y_mean = sum(transformed) / len(transformed)
    variance_x = sum((x - x_mean) ** 2 for x in times_s)
    if variance_x == 0:
        raise ValueError("times_s must contain distinct times")
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(times_s, transformed)) / variance_x
    intercept = y_mean - slope * x_mean
    residual = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(times_s, transformed))
    total = sum((y - y_mean) ** 2 for y in transformed)
    r_squared = 1.0 if total == 0 else 1.0 - residual / total
    return slope, intercept, r_squared


def weak_solution_ph(concentration_m: float, dissociation_constant: float, kind: str = "acid") -> float:
    """Return pH of a monoprotic weak acid or base solution.

    ``concentration_m`` and ``dissociation_constant`` are in mol/L and the
    corresponding ``Ka`` or ``Kb``. Set ``kind='acid'`` or ``kind='base'``. The
    quadratic equilibrium solution is used instead of the small-dissociation
    approximation; ``pKw=14.00`` is assumed for bases.
    """

    _positive("concentration_m", concentration_m)
    _positive("dissociation_constant", dissociation_constant)
    if kind not in {"acid", "base"}:
        raise ValueError("kind must be 'acid' or 'base'")
    ion_m = (-dissociation_constant + sqrt(dissociation_constant**2 + 4 * dissociation_constant * concentration_m)) / 2
    log_value = -log10(ion_m)
    return log_value if kind == "acid" else 14.0 - log_value


def solubility_from_ksp(
    ksp: float,
    dissolution_coefficients: Sequence[float],
    background_concentrations_m: Sequence[float] | None = None,
) -> float:
    """Return molar solubility in mol/L from a solubility product.

    ``dissolution_coefficients`` lists ion coefficients in one formula-unit
    dissolution, for example ``(1, 2)`` for ``M(OH)2``. Optional background
    concentrations in mol/L allow a common-ion calculation.
    """

    _positive("ksp", ksp)
    if not dissolution_coefficients:
        raise ValueError("At least one dissolution coefficient is required")
    coefficients = tuple(float(value) for value in dissolution_coefficients)
    for value in coefficients:
        _positive("dissolution coefficient", value)
    if background_concentrations_m is None:
        backgrounds = (0.0,) * len(coefficients)
    else:
        if len(background_concentrations_m) != len(coefficients):
            raise ValueError("Background concentrations must match dissolution coefficients")
        backgrounds = tuple(float(value) for value in background_concentrations_m)
        if any(value < 0 for value in backgrounds):
            raise ValueError("Background concentrations must not be negative")

    def product(s: float) -> float:
        result = 1.0
        for coefficient, background in zip(coefficients, backgrounds):
            result *= (background + coefficient * s) ** coefficient
        return result

    lo, hi = 0.0, 1.0
    while product(hi) < ksp:
        hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if product(mid) < ksp:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def cell_potential(
    standard_potential_v: float,
    electrons: int,
    reaction_quotient: float,
    temperature_k: float = 298.15,
) -> float:
    """Return cell potential in V using the Nernst equation.

    ``reaction_quotient`` must be written for the overall cell reaction in its
    spontaneous direction; ``electrons`` is the transferred electron count.
    """

    if electrons <= 0:
        raise ValueError("electrons must be positive")
    _positive("reaction_quotient", reaction_quotient)
    _positive("temperature_k", temperature_k)
    return standard_potential_v - GAS_CONSTANT_J_MOL_K * temperature_k * log(reaction_quotient) / (
        electrons * FARADAY_C_MOL
    )


def arrhenius_ratio(
    activation_energy_kj_mol: float,
    initial_temperature_k: float,
    final_temperature_k: float,
) -> float:
    """Return ``k_final/k_initial`` using Arrhenius activation energy in kJ/mol."""

    for name, value in (
        ("activation_energy_kj_mol", activation_energy_kj_mol),
        ("initial_temperature_k", initial_temperature_k),
        ("final_temperature_k", final_temperature_k),
    ):
        _positive(name, value)
    return exp((activation_energy_kj_mol * 1000.0 / GAS_CONSTANT_J_MOL_K) * (
        1.0 / initial_temperature_k - 1.0 / final_temperature_k
    ))
