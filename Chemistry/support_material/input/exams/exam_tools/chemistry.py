"""General numerical chemistry calculations used across the supplied exams."""

from __future__ import annotations

from math import exp, isfinite, log, log10, sqrt
import re
from typing import Sequence

GAS_CONSTANT_J_MOL_K = 8.314462618
ATM_TO_PA = 101325.0
FARADAY_C_MOL = 96485.33212
AVOGADRO_MOL = 6.02214076e23
PLANCK_J_S = 6.62607015e-34
LIGHT_SPEED_M_S = 299792458.0

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
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.630,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.62,
    "Y": 88.906,
    "Zr": 91.222,
    "Nb": 92.906,
    "Mo": 95.95,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.906,
    "Pd": 106.42,
    "Ag": 107.868,
    "Cd": 112.414,
    "In": 114.818,
    "Sn": 118.710,
    "Sb": 121.760,
    "Te": 127.60,
    "I": 126.904,
    "Xe": 131.293,
    "Cs": 132.905,
    "Ba": 137.327,
    "La": 138.905,
    "Ce": 140.116,
    "Pr": 140.908,
    "Nd": 144.242,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.249,
    "Tb": 158.925,
    "Dy": 162.500,
    "Ho": 164.930,
    "Er": 167.259,
    "Tm": 168.934,
    "Yb": 173.045,
    "Lu": 174.967,
    "Hf": 178.486,
    "Ta": 180.948,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.967,
    "Hg": 200.592,
    "Tl": 204.38,
    "Pb": 207.2,
    "Bi": 208.980,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.038,
    "Pa": 231.036,
    "U": 238.029,
    "Np": 237,
    "Pu": 244,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 262,
    "Rf": 267,
    "Db": 268,
    "Sg": 271,
    "Bh": 272,
    "Hs": 270,
    "Mt": 276,
    "Ds": 281,
    "Rg": 280,
    "Cn": 285,
    "Nh": 284,
    "Fl": 289,
    "Mc": 288,
    "Lv": 293,
    "Ts": 294,
    "Og": 294,
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


def freezing_point_depression(
    solute_mol: float | None = None,
    solute_mass_g: float | None = None,
    molar_mass_g_mol: float | None = None,
    solvent_mass_kg: float | None = None,
    vant_hoff_factor: float = 1.0,
    kf: float = 1.86,
    pure_freezing_point_c: float = 0.0,
) -> dict[str, float]:
    """Return freezing-point depression results for a solution.

    ``solute_mol`` is in mol. Alternatively give ``solute_mass_g`` in g and
    ``molar_mass_g_mol`` in g/mol. ``solvent_mass_kg`` is in kg,
    ``vant_hoff_factor`` is dimensionless, ``kf`` is in degC kg/mol and
    ``pure_freezing_point_c`` is in degC. Returned temperatures are in degC
    and molality is in mol/kg.
    """

    if solvent_mass_kg is None:
        raise ValueError("solvent_mass_kg must be provided")
    _positive("solvent_mass_kg", solvent_mass_kg)
    _positive("vant_hoff_factor", vant_hoff_factor)

    if solute_mol is not None:
        _positive("solute_mol", solute_mol)
    else:
        if solute_mass_g is None or molar_mass_g_mol is None:
            raise ValueError("Provide solute_mol or both solute_mass_g and molar_mass_g_mol")
        _positive("solute_mass_g", solute_mass_g)
        _positive("molar_mass_g_mol", molar_mass_g_mol)
        solute_mol = solute_mass_g / molar_mass_g_mol

    molality_mol_kg = solute_mol / solvent_mass_kg
    delta_tf_c = vant_hoff_factor * kf * molality_mol_kg
    freezing_point_c = pure_freezing_point_c - delta_tf_c
    return {
        "solute_mol": solute_mol,
        "molality_mol_kg": molality_mol_kg,
        "vant_hoff_factor": vant_hoff_factor,
        "delta_tf_c": delta_tf_c,
        "freezing_point_c": freezing_point_c,
    }


def ideal_gas(
    *,
    p: float | None = None,
    p_Pa: float | None = None,
    p_atm: float | None = None,
    pressure_pa: float | None = None,
    V: float | None = None,
    V_m3: float | None = None,
    V_L: float | None = None,
    V_mL: float | None = None,
    volume_m3: float | None = None,
    n: float | None = None,
    amount_mol: float | None = None,
    T: float | None = None,
    T_K: float | None = None,
    T_C: float | None = None,
    temperature_k: float | None = None,
    temperature_c: float | None = None,
) -> float:
    """Solve ``pV=nRT`` for the single missing variable.

    Pressure can be supplied as ``p``/``p_Pa``/``pressure_pa`` in Pa or
    ``p_atm`` in atm. Volume can be supplied as ``V``/``V_m3``/``volume_m3`` in
    m3, ``V_L`` in L or ``V_mL`` in mL. Temperature can be supplied as
    ``T``/``T_K``/``temperature_k`` in K or ``T_C``/``temperature_c`` in deg C.
    Exactly one of pressure, volume, amount and temperature must be omitted; the
    return value is always in the SI unit of the missing variable.
    """

    def _single_value(
        name: str,
        values: tuple[tuple[str, float | None, float, float], ...],
    ) -> float | None:
        supplied = [
            (unit_name, value, scale, offset)
            for unit_name, value, scale, offset in values
            if value is not None
        ]
        if len(supplied) > 1:
            supplied_names = ", ".join(unit_name for unit_name, _, _, _ in supplied)
            raise ValueError(f"Provide only one {name} unit, got {supplied_names}")
        if not supplied:
            return None
        unit_name, value, scale, offset = supplied[0]
        converted = value * scale + offset
        _positive(unit_name, converted)
        return converted

    pressure_pa_value = _single_value(
        "pressure",
        (
            ("p", p, 1.0, 0.0),
            ("p_Pa", p_Pa, 1.0, 0.0),
            ("pressure_pa", pressure_pa, 1.0, 0.0),
            ("p_atm", p_atm, ATM_TO_PA, 0.0),
        ),
    )
    volume_m3_value = _single_value(
        "volume",
        (
            ("V", V, 1.0, 0.0),
            ("V_m3", V_m3, 1.0, 0.0),
            ("volume_m3", volume_m3, 1.0, 0.0),
            ("V_L", V_L, 1e-3, 0.0),
            ("V_mL", V_mL, 1e-6, 0.0),
        ),
    )
    amount_mol_value = _single_value(
        "amount",
        (
            ("n", n, 1.0, 0.0),
            ("amount_mol", amount_mol, 1.0, 0.0),
        ),
    )
    temperature_k_value = _single_value(
        "temperature",
        (
            ("T", T, 1.0, 0.0),
            ("T_K", T_K, 1.0, 0.0),
            ("temperature_k", temperature_k, 1.0, 0.0),
            ("T_C", T_C, 1.0, 273.15),
            ("temperature_c", temperature_c, 1.0, 273.15),
        ),
    )

    values = (pressure_pa_value, volume_m3_value, amount_mol_value, temperature_k_value)
    if sum(value is None for value in values) != 1:
        raise ValueError("Exactly one ideal-gas parameter must be omitted")
    if pressure_pa_value is None:
        return (
            amount_mol_value
            * GAS_CONSTANT_J_MOL_K
            * temperature_k_value
            / volume_m3_value
        )  # type: ignore[operator]
    if volume_m3_value is None:
        return (
            amount_mol_value
            * GAS_CONSTANT_J_MOL_K
            * temperature_k_value
            / pressure_pa_value
        )  # type: ignore[operator]
    if amount_mol_value is None:
        return pressure_pa_value * volume_m3_value / (
            GAS_CONSTANT_J_MOL_K * temperature_k_value
        )
    return pressure_pa_value * volume_m3_value / (GAS_CONSTANT_J_MOL_K * amount_mol_value)


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


def solubility_complete_check(
    salt_formula: str,
    ksp: float,
    added_mass_g: float | None = None,
    added_mass_mg: float | None = None,
    solution_volume_l: float = 1.0,
    common_ion_concentration_m: float = 0.0,
    stoich_metal: int = 1,
    stoich_common_ion: int = 1,
    molar_mass_g_mol: float | None = None,
) -> dict[str, float | str | bool]:
    """Check whether all of an added sparingly soluble salt can dissolve.

    The salt is treated as ``M_aX_b``, where ``stoich_metal=a`` and
    ``stoich_common_ion=b``. Mass inputs are in g or mg, volume is in L,
    concentrations are in mol/L, molar mass is in g/mol, and ``ksp`` is the
    concentration-based solubility product.

    With an existing common-ion concentration ``[X] > 0``, the supplied
    common-ion approximation is used:
    ``[M]_max = (Ksp/[X]^b)^(1/a)`` and ``s_max = [M]_max/a``.
    With ``[X] = 0``, maximum formula concentration is calculated from the
    full pure-solvent solubility equation. Complete dissolution means required
    formula concentration is less than or equal to the maximum concentration.
    """

    _positive("ksp", ksp)
    _positive("solution_volume_l", solution_volume_l)
    if not isfinite(common_ion_concentration_m) or common_ion_concentration_m < 0:
        raise ValueError("common_ion_concentration_m must be finite and non-negative")
    for name, value in (("stoich_metal", stoich_metal), ("stoich_common_ion", stoich_common_ion)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if (added_mass_g is None) == (added_mass_mg is None):
        raise ValueError("Exactly one of added_mass_g or added_mass_mg must be provided")
    mass_g = added_mass_g if added_mass_g is not None else added_mass_mg / 1000.0  # type: ignore[operator]
    if not isfinite(mass_g) or mass_g < 0:
        raise ValueError("Added mass must be finite and non-negative")
    if molar_mass_g_mol is None:
        molar_mass_g_mol = molar_mass(salt_formula)
    else:
        _positive("molar_mass_g_mol", molar_mass_g_mol)

    added_mol = mass_g / molar_mass_g_mol
    required_formula_concentration_m = added_mol / solution_volume_l
    required_metal_concentration_m = stoich_metal * required_formula_concentration_m
    if common_ion_concentration_m > 0:
        max_metal_concentration_m = (
            ksp / common_ion_concentration_m**stoich_common_ion
        ) ** (1.0 / stoich_metal)
        max_formula_concentration_m = max_metal_concentration_m / stoich_metal
    else:
        max_formula_concentration_m = solubility_from_ksp(
            ksp, (stoich_metal, stoich_common_ion)
        )
        max_metal_concentration_m = stoich_metal * max_formula_concentration_m
    dissolves_completely = required_formula_concentration_m <= max_formula_concentration_m
    excess_formula_concentration_m = max(0.0, required_formula_concentration_m - max_formula_concentration_m)
    excess_mol = excess_formula_concentration_m * solution_volume_l
    excess_mass_g = excess_mol * molar_mass_g_mol
    return {
        "salt_formula": salt_formula,
        "molar_mass_g_mol": molar_mass_g_mol,
        "added_mass_g": mass_g,
        "solution_volume_l": solution_volume_l,
        "added_mol": added_mol,
        "required_formula_concentration_m": required_formula_concentration_m,
        "required_metal_concentration_m": required_metal_concentration_m,
        "common_ion_concentration_m": common_ion_concentration_m,
        "ksp": ksp,
        "max_metal_concentration_m": max_metal_concentration_m,
        "max_formula_concentration_m": max_formula_concentration_m,
        "dissolves_completely": dissolves_completely,
        "excess_formula_concentration_m": excess_formula_concentration_m,
        "excess_mol": excess_mol,
        "excess_mass_g": excess_mass_g,
    }


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
