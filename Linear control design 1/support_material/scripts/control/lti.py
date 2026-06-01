"""Small deterministic helpers for continuous-time SISO transfer functions."""

from __future__ import annotations

from collections import Counter
from typing import Callable, Iterable

import numpy as np
import sympy as sp
from scipy import signal
from scipy.optimize import brentq


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


def frequency_response_point(
    numerator: Iterable[float],
    denominator: Iterable[float],
    omega: float,
) -> dict[str, object]:
    """Return magnitude, phase and rectangular data at one frequency."""

    value = evaluate_transfer_function(numerator, denominator, omega)
    magnitude = float(abs(value))
    phase_deg = float(np.degrees(np.angle(value)))
    return {
        "value": value,
        "real": float(value.real),
        "imag": float(value.imag),
        "magnitude": magnitude,
        "magnitude_db": None if np.isclose(magnitude, 0.0) else float(20.0 * np.log10(magnitude)),
        "phase_deg": phase_deg,
        "omega": float(omega),
        "warnings": [],
    }


def transfer_function_poles(denominator: Iterable[float]) -> np.ndarray:
    """Use when a denominator polynomial is already derived from the task.

    Returns complex continuous-time poles. Stability interpretation remains the
    user's responsibility, especially for imaginary-axis poles.
    """
    den = _polynomial(denominator, "denominator")
    return np.roots(den)


def _polynomial_roots_and_stability(denominator: np.ndarray, tolerance: float = 1e-10) -> dict[str, object]:
    poles = np.roots(np.trim_zeros(denominator, trim="f"))
    return {
        "poles": poles,
        "stable": bool(np.all(np.real(poles) < -tolerance)),
        "has_rhp_poles": bool(np.any(np.real(poles) > tolerance)),
        "has_imaginary_axis_poles": bool(np.any(np.abs(np.real(poles)) <= tolerance)),
        "marginal_poles": [complex(pole) for pole in poles if abs(pole.real) <= tolerance],
    }


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


def closed_loop_analysis_from_coefficients(
    numerator: Iterable[float],
    denominator: Iterable[float],
    proportional_gain: float = 1.0,
    feedback_gain: float = 1.0,
) -> dict[str, object]:
    """Analyze the negative-feedback characteristic formed from coefficient lists."""

    num = _polynomial(numerator, "numerator")
    den = _polynomial(denominator, "denominator")
    loop_gain = float(proportional_gain) * float(feedback_gain)
    if not np.isfinite(loop_gain):
        raise ValueError("The loop gain must be finite.")
    characteristic = np.trim_zeros(np.polyadd(den, loop_gain * num), trim="f")
    if characteristic.size == 0 or np.allclose(characteristic, 0.0):
        raise ValueError("Closed-loop characteristic polynomial is identically zero.")

    stability = _polynomial_roots_and_stability(characteristic)
    numerator_dc = float(loop_gain * np.polyval(num, 0.0))
    denominator_dc = float(np.polyval(characteristic, 0.0))
    closed_loop_dc_gain = None if np.isclose(denominator_dc, 0.0) else float(numerator_dc / denominator_dc)
    return {
        "characteristic": characteristic.tolist(),
        "poles": stability["poles"],
        "stable": stability["stable"],
        "has_rhp_poles": stability["has_rhp_poles"],
        "has_imaginary_axis_poles": stability["has_imaginary_axis_poles"],
        "marginal_poles": stability["marginal_poles"],
        "closed_loop_dc_gain": closed_loop_dc_gain,
        "proportional_gain": float(proportional_gain),
        "feedback_gain": float(feedback_gain),
    }


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


def _error_from_constant(value: float | None) -> float | None:
    if value is None:
        return None
    if np.isinf(value):
        return 0.0
    if np.isclose(value, 0.0):
        return np.inf
    return float(1.0 / value)


def steady_state_error_analysis(
    numerator: Iterable[float],
    denominator: Iterable[float],
    proportional_gain: float = 1.0,
    input_type: str = "step",
) -> dict[str, object]:
    """Analyze standard negative-unity-feedback steady-state error."""

    num = _polynomial(numerator, "numerator")
    den = _polynomial(denominator, "denominator")
    gain = float(proportional_gain)
    if not np.isfinite(gain):
        raise ValueError("proportional_gain must be finite.")
    normalized_input = input_type.lower()
    if normalized_input not in {"step", "ramp", "parabolic"}:
        raise ValueError("input_type must be 'step', 'ramp' or 'parabolic'.")

    closed_loop = closed_loop_analysis_from_coefficients(num, den, gain)
    if not closed_loop["stable"]:
        raise ValueError("Final value theorem is not valid: the closed loop is not asymptotically stable.")

    variable = sp.Symbol("s")
    num_poly = sum(float(coeff) * variable ** power for power, coeff in enumerate(reversed(num)))
    den_poly = sum(float(coeff) * variable ** power for power, coeff in enumerate(reversed(den)))
    loop = sp.simplify(gain * num_poly / den_poly)

    def limit_or_inf(expr: sp.Expr) -> float | None:
        try:
            value = sp.limit(expr, variable, 0)
            if value is sp.oo:
                return np.inf
            if value is -sp.oo:
                return -np.inf
            return _safe_float(value)
        except Exception:
            return None

    position_constant = limit_or_inf(loop)
    velocity_constant = limit_or_inf(variable * loop)
    acceleration_constant = limit_or_inf(variable**2 * loop)

    poles = np.roots(den)
    system_type = int(sum(abs(pole) <= 1e-8 for pole in poles))
    if normalized_input == "step":
        error = None if position_constant is None else float(1.0 / (1.0 + position_constant)) if np.isfinite(position_constant) else 0.0
    elif normalized_input == "ramp":
        error = _error_from_constant(velocity_constant)
    else:
        error = _error_from_constant(acceleration_constant)

    return {
        "input_type": normalized_input,
        "steady_state_error": error,
        "system_type": system_type,
        "position_error_constant_Kp": position_constant,
        "velocity_error_constant_Kv": velocity_constant,
        "acceleration_error_constant_Ka": acceleration_constant,
        "closed_loop_stable": closed_loop["stable"],
        "closed_loop_poles": closed_loop["poles"],
        "warnings": [],
    }


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


def nyquist_point_analysis(real_part: float, imaginary_part: float) -> dict[str, object]:
    """Analyze a manually read Nyquist point."""

    if not np.isfinite(real_part) or not np.isfinite(imaginary_part):
        raise ValueError("Nyquist coordinates must be finite.")
    if np.isclose(real_part, 0.0) and np.isclose(imaginary_part, 0.0):
        raise ValueError("The origin has no defined phase.")
    point = complex(real_part, imaginary_part)
    magnitude = float(abs(point))
    phase_deg = float(np.degrees(np.arctan2(imaginary_part, real_part)))
    warnings = []
    if not np.isclose(magnitude, 1.0, rtol=0.05, atol=0.05):
        warnings.append("Pointet ligger ikke tydeligt paa enhedscirklen; PM kraever et gain-crossover-punkt.")
    return {
        "point": point,
        "real": float(real_part),
        "imag": float(imaginary_part),
        "magnitude": magnitude,
        "magnitude_db": float(20.0 * np.log10(magnitude)),
        "phase_deg": phase_deg,
        "phase_margin_deg": float(180.0 + phase_deg),
        "distance_to_minus_one": float(abs(point + 1.0)),
        "near_unit_circle": bool(np.isclose(magnitude, 1.0, rtol=0.05, atol=0.05)),
        "warnings": warnings,
    }


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


def _poly_float_coefficients(poly: sp.Poly) -> list[float]:
    coefficients = []
    for coefficient in poly.all_coeffs():
        value = complex(sp.N(coefficient))
        if not np.isfinite(value.real) or not np.isfinite(value.imag):
            raise ValueError("Polynomial coefficients must be finite.")
        if abs(value.imag) > 1e-10:
            raise ValueError("Polynomial coefficients must be real for time-domain metrics.")
        coefficients.append(float(value.real))
    return coefficients


def _safe_float(value: object) -> float | None:
    try:
        numeric = complex(sp.N(value)) if isinstance(value, sp.Basic) else complex(value)  # type: ignore[arg-type]
    except Exception:
        return None
    if not np.isfinite(numeric.real) or not np.isfinite(numeric.imag):
        return None
    if abs(numeric.imag) > 1e-8:
        return None
    return float(numeric.real)


def _safe_complex(value: object, tol: float = 1e-12) -> complex | None:
    try:
        numeric = complex(sp.N(value)) if isinstance(value, sp.Basic) else complex(value)  # type: ignore[arg-type]
    except Exception:
        return None
    if not np.isfinite(numeric.real) or not np.isfinite(numeric.imag):
        return None
    real = 0.0 if abs(numeric.real) < tol else float(numeric.real)
    imag = 0.0 if abs(numeric.imag) < tol else float(numeric.imag)
    return complex(real, imag)


def _plain_float(value: float | np.floating | None) -> float | None:
    if value is None:
        return None
    value = float(value)
    return value if np.isfinite(value) else None


def _safe_limit(expr: sp.Expr, variable: sp.Symbol, point: object, warnings: list[str], name: str) -> object:
    try:
        return sp.limit(expr, variable, point)
    except Exception as exc:
        warnings.append(f"{name} kunne ikke beregnes: {exc}")
        return None


def _poly_degree(poly: sp.Poly) -> int:
    return int(poly.degree()) if not poly.is_zero else -sp.oo  # type: ignore[return-value]


def _numeric_roots_safe(
    poly: sp.Poly,
    warnings: list[str],
    used_numeric_fallbacks: list[str],
    name: str,
) -> list[complex]:
    if poly.degree() <= 0:
        return []
    try:
        coeffs = _poly_float_coefficients(poly)
        if "numpy.roots" not in used_numeric_fallbacks:
            used_numeric_fallbacks.append("numpy.roots")
        return [complex(root) for root in np.roots(coeffs)]
    except Exception:
        pass
    try:
        return [complex(root) for root in poly.nroots(n=30, maxsteps=200)]
    except Exception as exc:
        warnings.append(f"{name}: SymPy nroots fejlede; bruger numpy.roots fallback ({exc}).")
        if "numpy.roots" not in used_numeric_fallbacks:
            used_numeric_fallbacks.append("numpy.roots")
        coeffs = _poly_float_coefficients(poly)
        return [complex(root) for root in np.roots(coeffs)]


def _coerce_phase_margin_data(data: dict[str, object]) -> dict[str, object]:
    coerced = dict(data)
    for key in ("gain_crossover_frequency", "phase_at_gain_crossover_deg", "phase_margin_deg"):
        if key in coerced:
            coerced[key] = _plain_float(coerced[key])  # type: ignore[arg-type]
    return coerced


def _normalized_polys(numerator: sp.Poly, denominator: sp.Poly, variable: sp.Symbol) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    leading = denominator.LC()
    normalized_numerator = sp.simplify(numerator.as_expr() / leading)
    normalized_denominator = sp.simplify(denominator.as_expr() / leading)
    normalized_g = sp.factor(sp.cancel(sp.together(normalized_numerator / normalized_denominator)))
    return normalized_g, normalized_numerator, normalized_denominator


def _pole_zero_metrics(
    poles: list[complex] | None,
    zeros: list[complex] | None,
    order: int,
    tol: float,
) -> dict[str, object]:
    if poles is None or zeros is None:
        return {
            "dominant_poles": None,
            "dominant_pole": None,
            "fast_poles": None,
            "pole_time_constants": None,
            "zero_time_constants": None,
            "minimum_phase": None,
            "has_integrator": None,
            "integrator_count": None,
            "pole_zero_cancellations": None,
            "minimal_order_estimate": None,
        }

    stable_poles = [p for p in poles if p.real < -tol]
    if stable_poles:
        min_abs_real = min(abs(p.real) for p in stable_poles)
        dominant_poles = [p for p in stable_poles if abs(abs(p.real) - min_abs_real) <= max(tol, 1e-4 * min_abs_real)]
        dominant_pole = dominant_poles[0]
        fast_poles = [p for p in stable_poles if p not in dominant_poles]
    else:
        dominant_poles = []
        dominant_pole = None
        fast_poles = []

    def time_constant(root: complex) -> float | None:
        return float(-1.0 / root.real) if root.real < -tol else None

    cancellations = []
    unmatched_zeros = list(zeros)
    for pole in poles:
        if not unmatched_zeros:
            break
        distances = [abs(pole - zero) for zero in unmatched_zeros]
        index = int(np.argmin(distances))
        if distances[index] <= tol:
            zero = unmatched_zeros.pop(index)
            cancellations.append({"pole": pole, "zero": zero, "distance": float(distances[index])})

    return {
        "dominant_poles": dominant_poles,
        "dominant_pole": dominant_pole,
        "fast_poles": fast_poles,
        "pole_time_constants": [{"pole": p, "tau": time_constant(p)} for p in poles],
        "zero_time_constants": [{"zero": z, "tau": time_constant(z)} for z in zeros],
        "minimum_phase": all(z.real < tol for z in zeros),
        "has_integrator": any(abs(p) <= tol for p in poles),
        "integrator_count": int(sum(1 for p in poles if abs(p) <= tol)),
        "pole_zero_cancellations": cancellations,
        "minimal_order_estimate": int(order - len(cancellations)),
    }


def _simulation_horizon(poles: list[complex], stable: bool | None, minimum: float = 10.0) -> tuple[float, int]:
    stable_poles = [p for p in poles if p.real < -1e-10]
    if stable and stable_poles:
        max_tau = max(-1.0 / p.real for p in stable_poles)
        fastest = max(1.0, max(abs(p) for p in stable_poles))
        horizon = max(minimum, 8.0 * max_tau, 8.0 / fastest)
    else:
        scale = max([abs(p) for p in poles] + [1.0])
        horizon = max(minimum, 8.0 / scale)
    points = int(np.clip(max(5000, horizon * 500), 5000, 10000))
    return float(horizon), points


def _first_crossing_time(times: np.ndarray, values: np.ndarray, threshold: float, increasing: bool = True) -> float | None:
    if increasing:
        indices = np.flatnonzero(values >= threshold)
    else:
        indices = np.flatnonzero(values <= threshold)
    if indices.size == 0:
        return None
    i = int(indices[0])
    if i == 0:
        return float(times[0])
    t0, t1 = times[i - 1], times[i]
    y0, y1 = values[i - 1], values[i]
    if np.isclose(y0, y1):
        return float(t1)
    return float(t0 + (threshold - y0) * (t1 - t0) / (y1 - y0))


def _settling_from_samples(times: np.ndarray, values: np.ndarray, final_value: float, band_fraction: float) -> float | None:
    tolerance = band_fraction * max(abs(final_value), 1e-12)
    outside = np.flatnonzero(np.abs(values - final_value) > tolerance)
    if outside.size == 0:
        return 0.0
    last_outside = int(outside[-1])
    if last_outside >= len(times) - 1:
        return None
    return float(times[last_outside + 1])


def _compute_step_metrics(
    numerator: sp.Poly,
    denominator: sp.Poly,
    transfer_function: sp.Expr,
    variable: sp.Symbol,
    poles: list[complex] | None,
    stable: bool | None,
    final_value_expr: object,
    warnings: list[str],
    used_numeric_fallbacks: list[str],
    compute_symbolic: bool = True,
) -> dict[str, object]:
    result: dict[str, object] = {
        "step_response_expression": None,
        "rise_time_10_90": None,
        "rise_time_0_100": None,
        "peak_time": None,
        "peak_value": None,
        "overshoot_percent": None,
        "undershoot_percent": None,
        "steady_state_error_open_loop_step": None,
        "steady_state_error_unity_feedback_step": None,
        "monotonic_step_response": None,
        "initial_slope": None,
        "max_slope": None,
        "time_of_max_slope": None,
    }

    if compute_symbolic:
        t = sp.Symbol("t", positive=True, real=True)
        try:
            result["step_response_expression"] = sp.simplify(sp.inverse_laplace_transform(transfer_function / variable, variable, t))
        except Exception as exc:
            warnings.append(f"Symbolsk steprespons kunne ikke beregnes: {exc}")

    final_value = _safe_float(final_value_expr)
    if final_value is not None:
        result["steady_state_error_open_loop_step"] = float(1.0 - final_value)
        dc_gain = _safe_float(sp.limit(transfer_function, variable, 0))
        if dc_gain is not None:
            result["steady_state_error_unity_feedback_step"] = _finite_error_from_constant(dc_gain)

    if numerator.degree() > denominator.degree() or poles is None:
        return result

    try:
        num = _poly_float_coefficients(numerator)
        den = _poly_float_coefficients(denominator)
        horizon, points = _simulation_horizon(poles, stable)
        tout, response = signal.step(signal.TransferFunction(num, den), T=np.linspace(0.0, horizon, points))
        y = np.asarray(response, dtype=float)
        if not np.all(np.isfinite(y)):
            return result
        if "numeric_step_response" not in used_numeric_fallbacks:
            used_numeric_fallbacks.append("numeric_step_response")

        y0 = float(y[0])
        target = final_value if final_value is not None and np.isfinite(final_value) else float(y[-1])
        direction = 1.0 if target >= y0 else -1.0
        normalized = direction * (y - y0)
        total_change = direction * (target - y0)

        if abs(total_change) > 1e-12:
            t10 = _first_crossing_time(tout, normalized, 0.1 * total_change, True)
            t90 = _first_crossing_time(tout, normalized, 0.9 * total_change, True)
            t100 = _first_crossing_time(tout, normalized, total_change, True)
            result["rise_time_10_90"] = None if t10 is None or t90 is None else float(t90 - t10)
            result["rise_time_0_100"] = t100

        if direction >= 0:
            peak_index = int(np.argmax(y))
            trough = float(np.min(y))
            undershoot = max(0.0, (min(y0, target) - trough) / max(abs(target), 1e-12) * 100.0)
        else:
            peak_index = int(np.argmin(y))
            trough = float(np.max(y))
            undershoot = max(0.0, (trough - max(y0, target)) / max(abs(target), 1e-12) * 100.0)
        peak_value = float(y[peak_index])
        result["peak_time"] = float(tout[peak_index])
        result["peak_value"] = peak_value
        result["overshoot_percent"] = max(0.0, (direction * (peak_value - target)) / max(abs(target), 1e-12) * 100.0)
        result["undershoot_percent"] = undershoot

        slopes = np.gradient(y, tout)
        result["initial_slope"] = float(slopes[0])
        max_slope_index = int(np.argmax(np.abs(slopes)))
        result["max_slope"] = float(slopes[max_slope_index])
        result["time_of_max_slope"] = float(tout[max_slope_index])

        dy = np.diff(y)
        slope_tol = max(1e-8, 1e-6 * max(1.0, float(np.max(np.abs(y)))))
        significant = dy[np.abs(dy) > slope_tol]
        result["monotonic_step_response"] = bool(
            significant.size == 0 or np.all(significant >= 0) or np.all(significant <= 0)
        )
    except Exception as exc:
        warnings.append(f"Numerisk steprespons kunne ikke beregnes: {exc}")

    return result


def _compute_impulse_metrics(
    numerator: sp.Poly,
    denominator: sp.Poly,
    transfer_function: sp.Expr,
    variable: sp.Symbol,
    poles: list[complex] | None,
    stable: bool | None,
    warnings: list[str],
    used_numeric_fallbacks: list[str],
) -> dict[str, object]:
    result: dict[str, object] = {
        "impulse_response_expression": None,
        "impulse_peak_value": None,
        "impulse_peak_time": None,
        "impulse_area": None,
    }
    t = sp.Symbol("t", positive=True, real=True)
    try:
        result["impulse_response_expression"] = sp.simplify(sp.inverse_laplace_transform(transfer_function, variable, t))
    except Exception as exc:
        warnings.append(f"Symbolsk impulsrespons kunne ikke beregnes: {exc}")

    if numerator.degree() > denominator.degree() or poles is None:
        return result
    try:
        num = _poly_float_coefficients(numerator)
        den = _poly_float_coefficients(denominator)
        horizon, points = _simulation_horizon(poles, stable)
        tout, response = signal.impulse(signal.TransferFunction(num, den), T=np.linspace(0.0, horizon, points))
        y = np.asarray(response, dtype=float)
        if not np.all(np.isfinite(y)):
            return result
        if "numeric_impulse_response" not in used_numeric_fallbacks:
            used_numeric_fallbacks.append("numeric_impulse_response")
        index = int(np.argmax(np.abs(y)))
        result["impulse_peak_value"] = float(y[index])
        result["impulse_peak_time"] = float(tout[index])
        result["impulse_area"] = float(np.trapezoid(y, tout))
    except Exception as exc:
        warnings.append(f"Numerisk impulsrespons kunne ikke beregnes: {exc}")
    return result


def _finite_error_from_constant(value: float | None) -> float | None:
    if value is None or np.isnan(value):
        return None
    if np.isposinf(value) or value == np.inf:
        return 0.0
    if np.isneginf(value) or value == -np.inf:
        return 0.0
    denominator = 1.0 + value
    if np.isclose(denominator, 0.0):
        return None
    return float(1.0 / denominator)


def _inverse_or_none(value: float | None) -> float | None:
    if value is None or np.isnan(value):
        return None
    if np.isinf(value):
        return 0.0
    if np.isclose(value, 0.0):
        return None
    return float(1.0 / value)


def _steady_state_error_constants(G: sp.Expr, variable: sp.Symbol, warnings: list[str]) -> dict[str, object]:
    values: dict[str, object] = {}
    for key, expr in (
        ("position_error_constant_Kp", G),
        ("velocity_error_constant_Kv", variable * G),
        ("acceleration_error_constant_Ka", variable**2 * G),
    ):
        try:
            limit_value = sp.limit(expr, variable, 0)
            values[key] = _safe_float(limit_value)
            if values[key] is None and limit_value in (sp.oo, -sp.oo):
                values[key] = float("inf")
        except Exception as exc:
            values[key] = None
            warnings.append(f"{key} kunne ikke beregnes: {exc}")
    kp = values["position_error_constant_Kp"]
    kv = values["velocity_error_constant_Kv"]
    ka = values["acceleration_error_constant_Ka"]
    values["steady_state_error_unity_feedback_step"] = _finite_error_from_constant(kp if isinstance(kp, float) else None)
    values["steady_state_error_unity_feedback_ramp"] = _inverse_or_none(kv if isinstance(kv, float) else None)
    values["steady_state_error_unity_feedback_parabolic"] = _inverse_or_none(ka if isinstance(ka, float) else None)
    return values


def _frequency_response_metrics(
    G: sp.Expr,
    variable: sp.Symbol,
    poles: list[complex],
    zeros: list[complex],
    dc_gain: object,
    relative_degree: int,
    warnings: list[str],
) -> dict[str, object]:
    result: dict[str, object] = {
        "gain_margin": None,
        "gain_margin_db": None,
        "phase_crossover_frequency": None,
        "bandwidth_3db": None,
        "resonant_peak": None,
        "resonant_peak_db": None,
        "resonant_frequency": None,
        "low_frequency_gain_db": None,
        "high_frequency_rolloff_db_per_decade": float(-20 * relative_degree),
        "break_frequencies": None,
        "bode_asymptote_description": None,
        "nyquist_stability_hint": None,
    }
    breaks = sorted(
        float(abs(root.real) if abs(root.imag) < 1e-8 and root.real < 0 else abs(root))
        for root in [*zeros, *poles]
        if abs(root) > 1e-12
    )
    result["break_frequencies"] = breaks
    result["bode_asymptote_description"] = (
        f"Lavfrekvent gain starter ved DC-gain; haeldningen aendres ved break-frekvenserne "
        f"{breaks} og ender med {result['high_frequency_rolloff_db_per_decade']:.0f} dB/dekade."
    )
    dc = _safe_float(dc_gain)
    if dc is not None and abs(dc) > 0 and np.isfinite(dc):
        result["low_frequency_gain_db"] = float(20.0 * np.log10(abs(dc)))

    try:
        Gjw = sp.lambdify(variable, G, "numpy")

        def H(w: float) -> complex:
            return complex(Gjw(1j * w))

        roots_for_grid = [abs(x) for x in [*poles, *zeros] if abs(x) > 1e-9]
        w_min = max(1e-6, min(roots_for_grid + [1.0]) / 1000.0)
        w_max = max(1e3, max(roots_for_grid + [1.0]) * 1000.0)
        ws = np.logspace(np.log10(w_min), np.log10(w_max), 20000)
        values = np.array([H(float(w)) for w in ws])
        mags = np.abs(values)
        phases = np.unwrap(np.angle(values)) * 180.0 / np.pi
        finite = np.isfinite(mags) & np.isfinite(phases)
        if not np.any(finite):
            return result
        ws, mags, phases = ws[finite], mags[finite], phases[finite]
        peak_index = int(np.argmax(mags))
        result["resonant_peak"] = float(mags[peak_index])
        result["resonant_peak_db"] = float(20.0 * np.log10(mags[peak_index])) if mags[peak_index] > 0 else None
        result["resonant_frequency"] = float(ws[peak_index])

        if dc is not None and dc != 0 and np.isfinite(dc):
            threshold = abs(dc) / np.sqrt(2.0)
            below = np.flatnonzero(mags <= threshold)
            if below.size:
                result["bandwidth_3db"] = float(ws[int(below[0])])

        shifted = phases + 180.0
        crossings = []
        for i in range(len(ws) - 1):
            if shifted[i] == 0 or shifted[i] * shifted[i + 1] < 0:
                def phase_error(w: float) -> float:
                    return float(np.angle(H(w), deg=True) + 180.0)

                try:
                    wc = brentq(phase_error, float(ws[i]), float(ws[i + 1]))
                    crossings.append(wc)
                except Exception:
                    pass
        if crossings:
            wpc = float(crossings[0])
            mag_at_wpc = abs(H(wpc))
            result["phase_crossover_frequency"] = wpc
            if mag_at_wpc > 0 and np.isfinite(mag_at_wpc):
                gm = 1.0 / mag_at_wpc
                result["gain_margin"] = float(gm)
                result["gain_margin_db"] = float(20.0 * np.log10(gm))

        rhp_poles = sum(1 for pole in poles if pole.real > 1e-7)
        result["nyquist_stability_hint"] = (
            "Open-loop har ingen RHP-poler; Nyquist kan vurderes direkte omkring -1."
            if rhp_poles == 0
            else f"Open-loop har {rhp_poles} RHP-pol(er); lukket stabilitet kraever korrekt Nyquist-indkredsning."
        )
    except Exception as exc:
        warnings.append(f"Frekvensanalyse kunne ikke beregnes: {exc}")
    return result


def _differential_equation_from_polynomials(
    numerator: sp.Poly,
    denominator: sp.Poly,
    variable: sp.Symbol,
) -> dict[str, object]:
    t = sp.Symbol("t")
    y = sp.Function("y")
    u = sp.Function("u")

    def side(poly: sp.Poly, fn: Callable[[sp.Symbol], sp.Expr]) -> sp.Expr:
        degree = poly.degree()
        expression = 0
        for index, coefficient in enumerate(poly.all_coeffs()):
            power = degree - index
            term = fn(t) if power == 0 else sp.diff(fn(t), t, power)
            expression += coefficient * term
        return sp.simplify(expression)

    lhs = side(denominator, y)
    rhs = side(numerator, u)
    equation = sp.Eq(lhs, rhs)
    return {
        "differential_equation": str(equation),
        "differential_equation_latex": sp.latex(equation),
    }


def _closed_loop_analysis(
    numerator: sp.Poly,
    denominator: sp.Poly,
    variable: sp.Symbol,
    tol: float,
    warnings: list[str],
    used_numeric_fallbacks: list[str],
) -> dict[str, object]:
    defaults = {
        "closed_loop_T": None,
        "sensitivity_S": None,
        "closed_loop_poles": None,
        "closed_loop_zeros": None,
        "closed_loop_stable": None,
        "closed_loop_dc_gain": None,
        "closed_loop_step_final_value": None,
        "closed_loop_step_settling_time_2_percent": None,
        "closed_loop_step_overshoot_percent": None,
        "closed_loop_step_rise_time_10_90": None,
    }
    try:
        char_expr = sp.expand(denominator.as_expr() + numerator.as_expr())
        T = sp.factor(sp.cancel(sp.together(numerator.as_expr() / char_expr)))
        S = sp.factor(sp.cancel(sp.together(denominator.as_expr() / char_expr)))
        cl_num_expr, cl_den_expr = sp.fraction(T)
        cl_num = sp.Poly(sp.expand(cl_num_expr), variable)
        cl_den = sp.Poly(sp.expand(cl_den_expr), variable)
        cl_poles = _numeric_roots_safe(cl_den, warnings, used_numeric_fallbacks, "closed-loop poler")
        cl_zeros = _numeric_roots_safe(cl_num, warnings, used_numeric_fallbacks, "closed-loop nulpunkter")
        cl_stable = all(p.real < -tol for p in cl_poles)
        cl_final = sp.limit(T, variable, 0)
        step_metrics = _compute_step_metrics(
            cl_num,
            cl_den,
            T,
            variable,
            cl_poles,
            cl_stable,
            cl_final,
            warnings,
            used_numeric_fallbacks,
            compute_symbolic=False,
        )
        return {
            "closed_loop_T": T,
            "sensitivity_S": S,
            "closed_loop_poles": cl_poles,
            "closed_loop_zeros": cl_zeros,
            "closed_loop_stable": bool(cl_stable),
            "closed_loop_dc_gain": cl_final,
            "closed_loop_step_final_value": cl_final,
            "closed_loop_step_settling_time_2_percent": _step_settling_time(cl_num, cl_den, 0.02) if cl_stable else None,
            "closed_loop_step_overshoot_percent": step_metrics.get("overshoot_percent"),
            "closed_loop_step_rise_time_10_90": step_metrics.get("rise_time_10_90"),
        }
    except Exception as exc:
        warnings.append(f"Closed-loop analyse kunne ikke beregnes: {exc}")
        return defaults


def _root_locus_analysis(
    numerator: sp.Poly,
    denominator: sp.Poly,
    poles: list[complex],
    zeros: list[complex],
    tol: float,
    warnings: list[str],
) -> dict[str, object]:
    n_poles = len(poles)
    n_zeros = len(zeros)
    asymptotes = n_poles - n_zeros
    centroid = None
    angles: list[float] = []
    if asymptotes > 0:
        centroid = complex((sum(poles) - sum(zeros)) / asymptotes)
        angles = [float((2 * k + 1) * 180.0 / asymptotes) for k in range(asymptotes)]

    real_points = sorted([x.real for x in [*poles, *zeros] if abs(x.imag) <= tol])
    segments = []
    if real_points:
        bounds = [-float("inf"), *real_points, float("inf")]
        for left, right in zip(bounds[:-1], bounds[1:]):
            test = right - 1.0 if np.isneginf(left) else left + 1.0 if np.isposinf(right) else (left + right) / 2.0
            count_right = sum(1 for x in real_points if x > test + tol)
            if count_right % 2 == 1:
                segments.append({"from": float(left), "to": float(right)})

    samples = []
    gains = [0, 0.1, 0.5, 1, 2, 5, 10, 50, 100]
    try:
        num = np.asarray(_poly_float_coefficients(numerator), dtype=float)
        den = np.asarray(_poly_float_coefficients(denominator), dtype=float)
        for gain in gains:
            characteristic = np.polyadd(den, gain * num)
            roots = [complex(root) for root in np.roots(np.trim_zeros(characteristic, trim="f"))]
            samples.append({"gain": float(gain), "poles": roots})
    except Exception as exc:
        warnings.append(f"Root locus sample-poler kunne ikke beregnes: {exc}")
        samples = None

    return {
        "root_locus_asymptote_centroid": centroid,
        "root_locus_asymptote_angles_deg": angles,
        "root_locus_real_axis_segments": segments,
        "root_locus_sample_poles": samples,
    }


def _state_space_analysis(
    numerator: sp.Poly,
    denominator: sp.Poly,
    warnings: list[str],
) -> dict[str, object]:
    defaults = {
        "state_space_A": None,
        "state_space_B": None,
        "state_space_C": None,
        "state_space_D": None,
        "controllable": None,
        "observable": None,
        "controllability_rank": None,
        "observability_rank": None,
    }
    try:
        if numerator.degree() > denominator.degree():
            return defaults
        num = _poly_float_coefficients(numerator)
        den = _poly_float_coefficients(denominator)
        A, B, C, D = signal.tf2ss(num, den)
        n = A.shape[0]
        controllability = B
        for i in range(1, n):
            controllability = np.hstack((controllability, np.linalg.matrix_power(A, i) @ B))
        observability = C
        for i in range(1, n):
            observability = np.vstack((observability, C @ np.linalg.matrix_power(A, i)))
        cr = int(np.linalg.matrix_rank(controllability))
        orank = int(np.linalg.matrix_rank(observability))
        return {
            "state_space_A": A.astype(float).tolist(),
            "state_space_B": B.astype(float).tolist(),
            "state_space_C": C.astype(float).tolist(),
            "state_space_D": D.astype(float).tolist(),
            "controllable": bool(cr == n),
            "observable": bool(orank == n),
            "controllability_rank": cr,
            "observability_rank": orank,
        }
    except Exception as exc:
        warnings.append(f"State-space analyse kunne ikke beregnes: {exc}")
        return defaults


def _modal_analysis(poles: list[complex] | None, tol: float) -> dict[str, object]:
    if poles is None:
        return {"modes": None, "dominant_mode_description": None}

    def key(pole: complex) -> tuple[int, int]:
        return (round(pole.real / tol), round(pole.imag / tol))

    counts = Counter(key(pole) for pole in poles)
    representatives: dict[tuple[int, int], complex] = {}
    for pole in poles:
        representatives.setdefault(key(pole), pole)

    modes = []
    for group_key, multiplicity in counts.items():
        pole = representatives[group_key]
        tau = float(-1.0 / pole.real) if pole.real < -tol else None
        omega_n = float(abs(pole)) if abs(pole.imag) > tol else None
        damping = float(-pole.real / abs(pole)) if abs(pole.imag) > tol and abs(pole) > tol else None
        base = f"exp({pole.real:.4g} t)" if abs(pole.imag) <= tol else f"exp({pole.real:.4g} t) sinus/cosinus med omega={abs(pole.imag):.4g}"
        if multiplicity > 1:
            base = f"t^k {base}, k=0..{multiplicity - 1}"
        modes.append(
            {
                "pole": pole,
                "multiplicity": int(multiplicity),
                "time_constant": tau,
                "damping": damping,
                "natural_frequency": omega_n,
                "description": base,
            }
        )
    stable_modes = [mode for mode in modes if isinstance(mode["time_constant"], float)]
    dominant = max(stable_modes, key=lambda mode: mode["time_constant"])["description"] if stable_modes else None
    return {"modes": modes, "dominant_mode_description": dominant}


def _step_settling_time(
    numerator: sp.Poly,
    denominator: sp.Poly,
    band_fraction: float,
) -> float | None:
    """Return unit-step settling time for a stable, proper numeric model."""

    if numerator.degree() > denominator.degree():
        return None

    num = _poly_float_coefficients(numerator)
    den = _poly_float_coefficients(denominator)
    poles = np.roots(den)
    stable_poles = poles[np.real(poles) < -1e-10]
    if stable_poles.size != poles.size:
        return None

    final_value = float(np.polyval(num, 0.0) / np.polyval(den, 0.0))
    if np.isclose(final_value, 0.0):
        return None

    slowest_decay = float(np.min(-np.real(stable_poles)))
    fastest_frequency = float(max(1.0, np.max(np.abs(poles))))
    base_horizon = max(10.0 / slowest_decay, 8.0 / fastest_frequency)
    tolerance = band_fraction * abs(final_value)
    system = signal.TransferFunction(num, den)

    for multiplier in (1, 2, 4, 8):
        horizon = base_horizon * multiplier
        points = int(np.clip(2500 * multiplier, 2500, 40000))
        times = np.linspace(0.0, horizon, points)
        tout, response = signal.step(system, T=times)
        error = np.abs(response - final_value)
        outside = np.flatnonzero(error > tolerance)

        if outside.size == 0:
            return 0.0
        last_outside = int(outside[-1])
        if last_outside < len(tout) - 1:
            t0, t1 = float(tout[last_outside]), float(tout[last_outside + 1])
            e0, e1 = float(error[last_outside]), float(error[last_outside + 1])
            if not np.isclose(e0, e1):
                fraction = (tolerance - e0) / (e1 - e0)
                if 0.0 <= fraction <= 1.0:
                    return t0 + fraction * (t1 - t0)
            return t1

    return None


def analyze_transfer_function(G: sp.Expr, variable: sp.Symbol | None = None) -> dict[str, object]:
    """Analyze a symbolic continuous-time rational transfer function."""
    tol = 1e-7
    analysis_warnings: list[str] = []
    used_numeric_fallbacks: list[str] = []

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
        zeros_numeric = _numeric_roots_safe(numerator, analysis_warnings, used_numeric_fallbacks, "nulpunkter")
        poles_numeric = _numeric_roots_safe(denominator, analysis_warnings, used_numeric_fallbacks, "poler")

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

    y0 = _safe_limit(transfer_function, variable, sp.oo, analysis_warnings, "y(0+)")
    yinf = _safe_limit(transfer_function, variable, 0, analysis_warnings, "y(inf)")
    normalized_g, normalized_numerator, normalized_denominator = _normalized_polys(numerator, denominator, variable)
    numerator_order = numerator.degree()
    denominator_order = denominator.degree()
    relative_degree = denominator_order - numerator_order
    dc_gain = _safe_limit(transfer_function, variable, 0, analysis_warnings, "DC-gain")
    coefficient_values = numerator.all_coeffs() + denominator.all_coeffs()
    is_symbolic_exact = not any(coefficient.is_Float for coefficient in coefficient_values)

    result: dict[str, object] = {
        "G(s)": transfer_function,
        "numerator": numerator.as_expr(),
        "denominator": denominator.as_expr(),
        "zeros_exact": zeros_exact,
        "poles_exact": poles_exact,
        "zeros_numeric": zeros_numeric,
        "poles_numeric": poles_numeric,
        "dc_gain": dc_gain,
        "order": denominator_order,
        "numerator_order": numerator_order,
        "system_type": poles_exact.get(sp.Integer(0), 0),
        "stable": stable,
        "stability_text": stability_text,
        "y(0+)": y0,
        "y(inf)": yinf,
        "settling_time_2_percent": None,
        "settling_time_1_percent": None,
        "settling_time_text": "ikke beregnet",
        "normalized_G": normalized_g,
        "normalized_numerator": normalized_numerator,
        "normalized_denominator": normalized_denominator,
        "static_gain": dc_gain,
        "relative_degree": relative_degree,
        "proper": bool(numerator_order <= denominator_order),
        "strictly_proper": bool(numerator_order < denominator_order),
        "biproper": bool(numerator_order == denominator_order),
        "analysis_warnings": analysis_warnings,
        "numerical_tolerance": tol,
        "is_symbolic_exact": is_symbolic_exact,
        "used_numeric_fallbacks": used_numeric_fallbacks,
    }

    if not parameters:
        phase_margin_data = _coerce_phase_margin_data(phase_margin(transfer_function, variable))
        result.update(phase_margin_data)

        if stable:
            settling_2 = _step_settling_time(numerator, denominator, 0.02)
            settling_1 = _step_settling_time(numerator, denominator, 0.01)
            result.update(
                {
                    "settling_time_2_percent": settling_2,
                    "settling_time_1_percent": settling_1,
                    "settling_time_text": (
                        "unit-step settling time relativt til slutvaerdien"
                        if settling_2 is not None or settling_1 is not None
                        else "settling time ikke veldefineret for denne transferfunktion"
                    ),
                }
            )

        result.update(_pole_zero_metrics(poles_numeric, zeros_numeric, denominator_order, tol))
        result.update(
            _compute_step_metrics(
                numerator,
                denominator,
                transfer_function,
                variable,
                poles_numeric,
                stable,
                yinf,
                analysis_warnings,
                used_numeric_fallbacks,
            )
        )
        result.update(
            _compute_impulse_metrics(
                numerator,
                denominator,
                transfer_function,
                variable,
                poles_numeric,
                stable,
                analysis_warnings,
                used_numeric_fallbacks,
            )
        )
        result.update(_steady_state_error_constants(transfer_function, variable, analysis_warnings))
        result.update(
            _frequency_response_metrics(
                transfer_function,
                variable,
                poles_numeric or [],
                zeros_numeric or [],
                dc_gain,
                relative_degree,
                analysis_warnings,
            )
        )
        result.update(_differential_equation_from_polynomials(numerator, denominator, variable))
        result.update(_closed_loop_analysis(numerator, denominator, variable, tol, analysis_warnings, used_numeric_fallbacks))
        result.update(_root_locus_analysis(numerator, denominator, poles_numeric or [], zeros_numeric or [], tol, analysis_warnings))
        result.update(_state_space_analysis(numerator, denominator, analysis_warnings))
        result.update(_modal_analysis(poles_numeric, tol))
    else:
        parameter_warning = "Numeriske udvidede analyser springes over, fordi transferfunktionen afhaenger af parametre."
        analysis_warnings.append(parameter_warning)
        result.update(_pole_zero_metrics(None, None, denominator_order, tol))
        result.update(
            {
                "step_response_expression": None,
                "rise_time_10_90": None,
                "rise_time_0_100": None,
                "peak_time": None,
                "peak_value": None,
                "overshoot_percent": None,
                "undershoot_percent": None,
                "steady_state_error_open_loop_step": None,
                "steady_state_error_unity_feedback_step": None,
                "monotonic_step_response": None,
                "initial_slope": None,
                "max_slope": None,
                "time_of_max_slope": None,
                "impulse_response_expression": None,
                "impulse_peak_value": None,
                "impulse_peak_time": None,
                "impulse_area": None,
                "gain_margin": None,
                "gain_margin_db": None,
                "phase_crossover_frequency": None,
                "bandwidth_3db": None,
                "resonant_peak": None,
                "resonant_peak_db": None,
                "resonant_frequency": None,
                "low_frequency_gain_db": None,
                "high_frequency_rolloff_db_per_decade": float(-20 * relative_degree),
                "break_frequencies": None,
                "bode_asymptote_description": None,
                "nyquist_stability_hint": None,
                "position_error_constant_Kp": None,
                "velocity_error_constant_Kv": None,
                "acceleration_error_constant_Ka": None,
                "steady_state_error_unity_feedback_ramp": None,
                "steady_state_error_unity_feedback_parabolic": None,
                "closed_loop_T": None,
                "sensitivity_S": None,
                "closed_loop_poles": None,
                "closed_loop_zeros": None,
                "closed_loop_stable": None,
                "closed_loop_dc_gain": None,
                "closed_loop_step_final_value": None,
                "closed_loop_step_settling_time_2_percent": None,
                "closed_loop_step_overshoot_percent": None,
                "closed_loop_step_rise_time_10_90": None,
                "root_locus_asymptote_centroid": None,
                "root_locus_asymptote_angles_deg": None,
                "root_locus_real_axis_segments": None,
                "root_locus_sample_poles": None,
                "state_space_A": None,
                "state_space_B": None,
                "state_space_C": None,
                "state_space_D": None,
                "controllable": None,
                "observable": None,
                "controllability_rank": None,
                "observability_rank": None,
                "modes": None,
                "dominant_mode_description": None,
            }
        )
        try:
            result.update(_differential_equation_from_polynomials(numerator, denominator, variable))
        except Exception as exc:
            analysis_warnings.append(f"Differentialligning kunne ikke beregnes: {exc}")
            result.update({"differential_equation": None, "differential_equation_latex": None})

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

    if used_numeric_fallbacks:
        result["is_symbolic_exact"] = False

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


def second_order_analysis(denominator: Iterable[float]) -> dict[str, object]:
    """Return common exam metrics for a standard second-order denominator."""

    base = second_order_characteristics(denominator)
    den = _polynomial(denominator, "denominator")
    normalized = den / den[0]
    omega_n = float(base["omega_n"])
    zeta = float(base["zeta"])
    poles = np.roots(normalized)
    if zeta < 1.0:
        omega_d = float(omega_n * np.sqrt(1.0 - zeta**2))
        peak_time = float(np.pi / omega_d)
        damping_class = "underdamped"
    elif np.isclose(zeta, 1.0):
        omega_d = 0.0
        peak_time = None
        damping_class = "critically damped"
    else:
        omega_d = None
        peak_time = None
        damping_class = "overdamped"

    settling_time_2_percent = float(4.0 / (zeta * omega_n)) if zeta > 0.0 else None
    settling_time_5_percent = float(3.0 / (zeta * omega_n)) if zeta > 0.0 else None
    return {
        **base,
        "overshoot_fraction": float(base["overshoot_percent"] / 100.0),
        "poles": poles,
        "omega_d": omega_d,
        "peak_time": peak_time,
        "settling_time_2_percent": settling_time_2_percent,
        "settling_time_5_percent": settling_time_5_percent,
        "damping_class": damping_class,
    }
