"""Small deterministic helpers for continuous-time SISO transfer functions."""

from __future__ import annotations

from typing import Iterable

import numpy as np
import sympy as sp


s = sp.Symbol("s")


def _polynomial(coefficients: Iterable[float], name: str) -> np.ndarray:
    values = np.asarray(list(coefficients), dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError(f"{name} must be a non-empty one-dimensional coefficient sequence.")
    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} contains non-finite values.")
    if np.isclose(values[0], 0.0):
        raise ValueError(f"{name} must have a non-zero leading coefficient.")
    return values


def evaluate_transfer_function(
    numerator: Iterable[float], denominator: Iterable[float], omega: float
) -> complex:
    """Use when evaluating a stated transfer function at s=j*omega.

    Coefficients are in descending powers of s. The function assumes a
    continuous-time rational SISO model and does not infer a model from plots.
    """
    num = _polynomial(numerator, "numerator")
    den = _polynomial(denominator, "denominator")
    if not np.isfinite(omega) or omega < 0:
        raise ValueError("omega must be a finite non-negative frequency in rad/s.")
    den_value = np.polyval(den, 1j * omega)
    if np.isclose(abs(den_value), 0.0):
        raise ValueError("The transfer function has a pole at the requested frequency.")
    return complex(np.polyval(num, 1j * omega) / den_value)


def transfer_function_poles(denominator: Iterable[float]) -> np.ndarray:
    """Use when a denominator polynomial is already derived from the task.

    Returns complex continuous-time poles. Stability interpretation remains the
    user's responsibility, especially for imaginary-axis poles.
    """
    den = _polynomial(denominator, "denominator")
    return np.roots(den)


def closed_loop_poles(
    numerator: Iterable[float],
    denominator: Iterable[float],
    proportional_gain: float = 1.0,
    feedback_gain: float = 1.0,
) -> np.ndarray:
    """Use when checking a proposed proportional gain in negative feedback.

    Returns poles of denominator + proportional_gain*feedback_gain*numerator.
    The caller must first verify that this matches the block diagram.
    """
    num = _polynomial(numerator, "numerator")
    den = _polynomial(denominator, "denominator")
    loop_gain = float(proportional_gain) * float(feedback_gain)
    if not np.isfinite(loop_gain):
        raise ValueError("The loop gain must be finite.")
    characteristic = np.polyadd(den, loop_gain * num)
    if np.allclose(characteristic, 0.0):
        raise ValueError("Closed-loop characteristic polynomial is identically zero.")
    return np.roots(np.trim_zeros(characteristic, trim="f"))


def unity_feedback_step_error(
    numerator: Iterable[float], denominator: Iterable[float], proportional_gain: float = 1.0
) -> float:
    """Use when computing unit-step error in a verified negative unity loop.

    Returns the final error for E/R=1/(1+K*G). It checks closed-loop
    asymptotic stability before applying the final value theorem.
    """
    num = _polynomial(numerator, "numerator")
    den = _polynomial(denominator, "denominator")
    if not np.isfinite(proportional_gain):
        raise ValueError("proportional_gain must be finite.")
    poles = closed_loop_poles(num, den, proportional_gain)
    if np.any(np.real(poles) >= -1e-10):
        raise ValueError("Final value theorem is not valid: the closed loop is not asymptotically stable.")
    denominator_dc = float(np.polyval(den, 0.0) + proportional_gain * np.polyval(num, 0.0))
    if np.isclose(denominator_dc, 0.0):
        raise ValueError("The error transfer function is singular at DC.")
    return float(np.polyval(den, 0.0) / denominator_dc)


def phase_margin_from_point(real_part: float, imaginary_part: float) -> float:
    """Use when a Nyquist point at the gain crossover has been read manually.

    Returns phase margin in degrees for the principal negative-frequency-lag
    representation used in the lecture examples.
    """
    if not np.isfinite(real_part) or not np.isfinite(imaginary_part):
        raise ValueError("Nyquist coordinates must be finite.")
    if np.isclose(real_part, 0.0) and np.isclose(imaginary_part, 0.0):
        raise ValueError("The origin has no defined phase.")
    phase_deg = float(np.degrees(np.arctan2(imaginary_part, real_part)))
    return 180.0 + phase_deg


def bode_to_transfer(
    dc_gain_db: sp.Expr,
    poles: Iterable[sp.Expr] | None = None,
    zeros: Iterable[sp.Expr] | None = None,
    variable: sp.Symbol = s,
) -> sp.Expr:
    """Build a symbolic transfer function from Bode asymptote data.

    ``dc_gain_db`` is the low-frequency gain in dB. Each positive break
    frequency defines a left-half-plane factor ``1 + s/omega``.
    """
    if not isinstance(variable, sp.Symbol):
        raise ValueError("variable must be a SymPy symbol.")

    pole_breaks = [] if poles is None else list(poles)
    zero_breaks = [] if zeros is None else list(zeros)
    transfer_function = sp.Pow(10, sp.sympify(dc_gain_db) / 20)

    for name, breaks in (("zeros", zero_breaks), ("poles", pole_breaks)):
        for break_frequency in breaks:
            omega = sp.sympify(break_frequency)
            if omega.is_zero is True:
                raise ValueError(f"{name} may not contain a zero break frequency.")
            if omega.is_number and omega.is_positive is not True:
                raise ValueError(f"{name} must contain positive break frequencies.")
            factor = 1 + variable / omega
            if name == "zeros":
                transfer_function *= factor
            else:
                transfer_function /= factor

    return sp.factor(sp.simplify(sp.together(transfer_function)))


import sympy as sp
import numpy as np
from scipy.optimize import brentq


def analyze_transfer_function(G: sp.Expr, variable: sp.Symbol | None = None) -> dict[str, object]:
    """Analyze a symbolic continuous-time rational transfer function."""

    if variable is None:
        free_symbols = list(sp.sympify(G).free_symbols)
        candidates = [x for x in free_symbols if x.name == "s"]
        if not candidates:
            raise ValueError("Could not infer Laplace variable. Pass variable explicitly.")
        variable = candidates[0]

    if not isinstance(variable, sp.Symbol):
        raise ValueError("variable must be a SymPy symbol.")

    transfer_function = sp.factor(sp.cancel(sp.together(sp.sympify(G))))
    numerator_expression, denominator_expression = sp.fraction(transfer_function)

    try:
        numerator = sp.Poly(sp.expand(numerator_expression), variable)
        denominator = sp.Poly(sp.expand(denominator_expression), variable)
    except sp.PolynomialError as exc:
        raise ValueError("G must be rational and polynomial in variable.") from exc

    if denominator.is_zero:
        raise ValueError("G may not have an identically zero denominator.")

    zeros_exact = sp.roots(numerator.as_expr(), variable)
    poles_exact = sp.roots(denominator.as_expr(), variable)

    parameters = (
        numerator.as_expr().free_symbols
        | denominator.as_expr().free_symbols
    ) - {variable}

    zeros_numeric: list[complex] | None
    poles_numeric: list[complex] | None
    stable: bool | None

    if parameters:
        zeros_numeric = None
        poles_numeric = None
        stable = None
        stability_text = "afhaenger af parametre"
    else:
        zeros_numeric = (
            [complex(root) for root in numerator.nroots()]
            if numerator.degree() > 0
            else []
        )
        poles_numeric = [complex(root) for root in denominator.nroots()]

        stable = all(pole.real < -1e-10 for pole in poles_numeric)
        has_rhp_poles = any(pole.real > 1e-10 for pole in poles_numeric)
        has_imaginary_axis_poles = any(
            abs(pole.real) <= 1e-10 for pole in poles_numeric
        )

        if stable:
            stability_text = "asymptotisk stabil"
        elif has_rhp_poles:
            stability_text = "ustabil"
        elif has_imaginary_axis_poles:
            stability_text = "marginalt stabil / paa stabilitetsgraensen"
        else:
            stability_text = "uklar"

    y0 = sp.limit(transfer_function, variable, sp.oo)
    yinf = sp.limit(transfer_function, variable, 0, "+")

    result: dict[str, object] = {
        "G(s)": transfer_function,
        "numerator": numerator.as_expr(),
        "denominator": denominator.as_expr(),
        "zeros_exact": zeros_exact,
        "poles_exact": poles_exact,
        "zeros_numeric": zeros_numeric,
        "poles_numeric": poles_numeric,
        "dc_gain": sp.limit(transfer_function, variable, 0),
        "order": denominator.degree(),
        "numerator_order": numerator.degree(),
        "system_type": poles_exact.get(sp.Integer(0), 0),
        "stable": stable,
        "stability_text": stability_text,
        "y(0+)": y0,
        "y(inf)": yinf,
    }

    if not parameters:
        phase_margin_data = phase_margin(transfer_function, variable)
        result.update(phase_margin_data)

    if denominator.degree() == 2:
        a2, a1, a0 = denominator.all_coeffs()
        omega_n = sp.sqrt(sp.simplify(a0 / a2))
        zeta = sp.simplify((a1 / a2) / (2 * omega_n))
        overshoot = sp.exp(-sp.pi * zeta / sp.sqrt(1 - zeta**2))

        result.update(
            {
                "omega_n": omega_n,
                "zeta": zeta,
                "overshoot_fraction_formula": sp.simplify(overshoot),
                "overshoot_percent_formula": sp.simplify(100 * overshoot),
            }
        )

    return result


def phase_margin(G: sp.Expr, variable: sp.Symbol) -> dict[str, object]:
    """Find phase margin numerically for a SISO open-loop transfer function."""

    Gjw = sp.lambdify(variable, G, "numpy")

    def H(w: float) -> complex:
        return complex(Gjw(1j * w))

    def mag_db(w: float) -> float:
        return 20 * np.log10(abs(H(w)))

    # Search over a wide frequency interval
    ws = np.logspace(-6, 6, 20000)
    mags = np.array([mag_db(w) for w in ws])

    crossings = []

    for i in range(len(ws) - 1):
        if np.isfinite(mags[i]) and np.isfinite(mags[i + 1]):
            if mags[i] == 0:
                crossings.append(ws[i])
            elif mags[i] * mags[i + 1] < 0:
                try:
                    wc = brentq(mag_db, ws[i], ws[i + 1])
                    crossings.append(wc)
                except ValueError:
                    pass

    if not crossings:
        return {
            "gain_crossover_frequency": None,
            "phase_at_gain_crossover_deg": None,
            "phase_margin_deg": None,
            "phase_margin_text": "ingen gain crossover fundet",
        }

    # Usually the first gain crossover is used for classical phase margin
    wc = crossings[0]
    phase_deg = np.angle(H(wc), deg=True)

    # Convert phase to the equivalent value near -180 degrees
    if phase_deg > 0:
        phase_deg -= 360

    pm = 180 + phase_deg

    return {
        "gain_crossover_frequency": wc,
        "phase_at_gain_crossover_deg": phase_deg,
        "phase_margin_deg": pm,
        "phase_margin_text": f"{pm:.3f} grader ved omega = {wc:.3f} rad/s",
    }


def closed_loop_characteristic(
    forward: sp.Expr,
    feedback: sp.Expr = 1,
    variable: sp.Symbol = s,
    negative_feedback: bool = True,
) -> sp.Expr:
    """Return the characteristic polynomial for a symbolic feedback loop.

    For negative feedback the equation is ``1 + forward*feedback = 0``;
    for positive feedback it is ``1 - forward*feedback = 0``.
    """
    if not isinstance(variable, sp.Symbol):
        raise ValueError("variable must be a SymPy symbol.")

    loop_transfer = sp.cancel(sp.together(sp.sympify(forward) * sp.sympify(feedback)))
    numerator, denominator = sp.fraction(loop_transfer)
    characteristic = denominator + numerator if negative_feedback else denominator - numerator
    try:
        sp.Poly(sp.expand(characteristic), variable)
    except sp.PolynomialError as exc:
        raise ValueError(
            "The closed-loop characteristic must be polynomial in variable."
        ) from exc
    return sp.factor(sp.expand(characteristic))


def second_order_characteristics(denominator: Iterable[float]) -> dict[str, float]:
    """Use when a denominator is of the form a*s^2+b*s+c with a,b,c>0.

    Returns natural frequency, damping ratio and percent step overshoot for
    the standard unit-gain second-order model.
    """
    den = _polynomial(denominator, "denominator")
    if den.size != 3:
        raise ValueError("A second-order denominator must contain exactly three coefficients.")
    normalized = den / den[0]
    if normalized[2] <= 0:
        raise ValueError("The constant coefficient must be positive for this standard form.")
    omega_n = float(np.sqrt(normalized[2]))
    zeta = float(normalized[1] / (2.0 * omega_n))
    if zeta <= 0:
        raise ValueError("The damping ratio must be positive for this response calculation.")
    overshoot = (
        float(100.0 * np.exp(-np.pi * zeta / np.sqrt(1.0 - zeta**2)))
        if zeta < 1.0
        else 0.0
    )
    return {"omega_n": omega_n, "zeta": zeta, "overshoot_percent": overshoot}
