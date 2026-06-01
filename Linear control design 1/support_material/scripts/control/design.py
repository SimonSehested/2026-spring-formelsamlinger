"""Controller-design computations that expose, rather than choose, assumptions."""

from __future__ import annotations

from typing import Iterable

import numpy as np

from .lti import evaluate_transfer_function


def _require_positive_finite(name: str, value: float | None) -> float:
    if value is None:
        raise ValueError(f"{name} is required.")
    value = float(value)
    if not np.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite.")
    return value


def _optional_positive_finite(name: str, value: float | None) -> float | None:
    if value is None:
        return None
    return _require_positive_finite(name, value)


def _phase_near_negative_180(value: complex) -> float:
    phase = float(np.degrees(np.angle(value)))
    if phase > 0.0:
        phase -= 360.0
    return phase


def _normalize_loop_phase_deg(phase: float) -> float:
    while phase > 0.0:
        phase -= 360.0
    while phase <= -360.0:
        phase += 360.0
    return float(phase)


def eval_poly_tf(numerator: Iterable[float], denominator: Iterable[float], omega: float) -> complex:
    """Evaluate num(s)/den(s) at s=j*omega for polynomial coefficient lists."""

    return evaluate_transfer_function(numerator, denominator, omega)


def pi_lead_frequency_response(
    omega: float | np.ndarray,
    Kp: float,
    tau_i: float,
    alpha: float,
    tau_d: float,
) -> complex | np.ndarray:
    """Return C(j*omega) for the PI-lead controller."""

    Kp = _require_positive_finite("Kp", Kp)
    tau_i = _require_positive_finite("tau_i", tau_i)
    tau_d = _require_positive_finite("tau_d", tau_d)
    alpha = float(alpha)
    if not np.isfinite(alpha) or alpha <= 0.0:
        raise ValueError("alpha must be positive and finite.")

    omega_values = np.asarray(omega, dtype=float)
    if np.any(~np.isfinite(omega_values)) or np.any(omega_values <= 0.0):
        raise ValueError("omega must contain positive finite frequencies.")

    s = 1j * omega_values
    controller = Kp * ((tau_i * s + 1.0) / (tau_i * s)) * (
        (tau_d * s + 1.0) / (alpha * tau_d * s + 1.0)
    )
    if np.ndim(omega) == 0:
        return complex(controller)
    return controller


def compute_margins(
    numerator: Iterable[float],
    denominator: Iterable[float],
    Kp: float,
    tau_i: float,
    alpha: float,
    tau_d: float,
    omega_grid: Iterable[float] | None = None,
) -> dict[str, float | None]:
    """Estimate classical margins for G(s)C(s) from a dense frequency grid."""

    if omega_grid is None:
        omegas = np.logspace(-6, 6, 20000)
    else:
        omegas = np.asarray(list(omega_grid), dtype=float)
        if omegas.ndim != 1 or omegas.size < 2:
            raise ValueError("omega_grid must contain at least two frequencies.")
        if np.any(~np.isfinite(omegas)) or np.any(omegas <= 0.0):
            raise ValueError("omega_grid must contain positive finite frequencies.")
        omegas = np.sort(omegas)

    plant_values = []
    for w in omegas:
        try:
            plant_values.append(eval_poly_tf(numerator, denominator, w))
        except ValueError:
            plant_values.append(np.nan + 1j * np.nan)
    plant = np.array(plant_values, dtype=complex)
    controller = pi_lead_frequency_response(omegas, Kp, tau_i, alpha, tau_d)
    loop = plant * controller
    finite_loop = np.isfinite(loop.real) & np.isfinite(loop.imag)
    omegas = omegas[finite_loop]
    loop = loop[finite_loop]
    if omegas.size < 2:
        return {
            "gain_crossover_rad_s": None,
            "phase_margin_deg": None,
            "phase_crossover_rad_s": None,
            "gain_margin": None,
            "gain_margin_db": None,
        }
    magnitudes = np.abs(loop)
    phases = np.degrees(np.unwrap(np.angle(loop)))

    finite = np.isfinite(magnitudes) & (magnitudes > 0.0) & np.isfinite(phases)
    omegas = omegas[finite]
    magnitudes = magnitudes[finite]
    phases = phases[finite]
    if omegas.size < 2:
        return {
            "gain_crossover_rad_s": None,
            "phase_margin_deg": None,
            "phase_crossover_rad_s": None,
            "gain_margin": None,
            "gain_margin_db": None,
        }

    log_omega = np.log(omegas)
    log_mag = np.log(magnitudes)

    def interpolate_crossing(values: np.ndarray, target: float) -> tuple[float, int] | None:
        shifted = values - target
        exact = np.flatnonzero(np.isclose(shifted, 0.0, atol=1e-10))
        if exact.size:
            index = int(exact[0])
            return float(omegas[index]), index
        crossings = np.flatnonzero(shifted[:-1] * shifted[1:] < 0.0)
        if crossings.size == 0:
            return None
        index = int(crossings[0])
        x0, x1 = log_omega[index], log_omega[index + 1]
        y0, y1 = shifted[index], shifted[index + 1]
        fraction = -y0 / (y1 - y0)
        omega_crossing = float(np.exp(x0 + fraction * (x1 - x0)))
        return omega_crossing, index

    gain_crossing = interpolate_crossing(log_mag, 0.0)
    if gain_crossing is None:
        gain_crossover = None
        phase_margin = None
    else:
        gain_crossover, index = gain_crossing
        phase_at_gain = float(np.interp(np.log(gain_crossover), log_omega[index : index + 2], phases[index : index + 2]))
        phase_margin = float(180.0 + _normalize_loop_phase_deg(phase_at_gain))

    phase_crossing = interpolate_crossing(phases, -180.0)
    if phase_crossing is None:
        phase_crossover = None
        gain_margin = None
        gain_margin_db = None
    else:
        phase_crossover, index = phase_crossing
        mag_at_phase = float(np.exp(np.interp(np.log(phase_crossover), log_omega[index : index + 2], log_mag[index : index + 2])))
        gain_margin = None if np.isclose(mag_at_phase, 0.0) else float(1.0 / mag_at_phase)
        gain_margin_db = None if gain_margin is None else float(20.0 * np.log10(gain_margin))

    return {
        "gain_crossover_rad_s": gain_crossover,
        "phase_margin_deg": phase_margin,
        "phase_crossover_rad_s": phase_crossover,
        "gain_margin": gain_margin,
        "gain_margin_db": gain_margin_db,
    }


def design_pi_lead(
    numerator: Iterable[float],
    denominator: Iterable[float],
    omega_c: float | None = None,
    phase_margin_deg: float | None = None,
    n_i: float | None = None,
    tau_i: float | None = None,
    alpha: float | None = None,
    tau_d: float | None = None,
    Kp: float | None = None,
    verbose: bool = True,
    full_margin_check: bool = True,
) -> dict[str, object]:
    """Design or check a PI-lead controller from the quantities given."""

    del verbose
    warnings: list[str] = []
    omega_c = _optional_positive_finite("omega_c", omega_c)
    n_i = _optional_positive_finite("n_i", n_i)
    tau_i = _optional_positive_finite("tau_i", tau_i)
    tau_d = _optional_positive_finite("tau_d", tau_d)
    Kp = _optional_positive_finite("Kp", Kp)

    if phase_margin_deg is not None:
        phase_margin_deg = float(phase_margin_deg)
        if not np.isfinite(phase_margin_deg) or not 0.0 < phase_margin_deg < 180.0:
            raise ValueError("phase_margin_deg must lie strictly between 0 and 180 degrees.")

    if alpha is not None:
        alpha = float(alpha)
        if not np.isfinite(alpha):
            raise ValueError("alpha must be finite.")
        if alpha <= 0.0:
            raise ValueError("alpha must be positive. alpha <= 0 cannot define a PI-lead controller.")
        if alpha > 1.0:
            warnings.append("alpha > 1: controllerdelen er ikke et lead-led, men check/analyse fortsaetter.")

    if tau_i is None and n_i is not None:
        if omega_c is None:
            raise ValueError("omega_c is required to compute tau_i from n_i.")
        tau_i = n_i / omega_c
    elif n_i is None and tau_i is not None and omega_c is not None:
        n_i = omega_c * tau_i
    elif tau_i is not None and n_i is not None and omega_c is not None:
        implied = omega_c * tau_i
        if not np.isclose(implied, n_i, rtol=1e-5, atol=1e-9):
            warnings.append(f"n_i={n_i:.6g} does not match omega_c*tau_i={implied:.6g}; tau_i is used.")
            n_i = implied

    if tau_i is None:
        raise ValueError("tau_i is required, either directly or via n_i and omega_c.")

    plant_mag = None
    plant_phase = None
    pi_phase = None
    lead_phase = None
    loop_mag = None
    loop_phase = None
    estimated_pm = None
    required_lead_phase = None

    if omega_c is not None:
        plant_value = eval_poly_tf(numerator, denominator, omega_c)
        plant_mag = float(abs(plant_value))
        plant_phase = _phase_near_negative_180(plant_value)
        pi_at_crossover = pi_lead_frequency_response(omega_c, 1.0, tau_i, 1.0, 1.0)
        pi_phase = _phase_near_negative_180(pi_at_crossover)

    if alpha is None:
        if omega_c is None or phase_margin_deg is None:
            raise ValueError("alpha is required unless omega_c and phase_margin_deg are supplied for design.")
        if plant_phase is None or pi_phase is None:
            raise ValueError("Could not compute plant and PI phase at omega_c.")
        required_lead_phase = -180.0 + phase_margin_deg - plant_phase - pi_phase
        if required_lead_phase <= 0.0:
            alpha = 1.0
            warnings.append("No positive lead phase is required; alpha is set to 1.0.")
        else:
            if required_lead_phase >= 80.0:
                warnings.append("Required lead phase is >= 80 deg; a single lead-led is likely unrealistic.")
            if required_lead_phase >= 90.0:
                warnings.append("Required lead phase is >= 90 deg; alpha is clipped to a very small positive value.")
                required_lead_phase = 89.999
            sine = float(np.sin(np.radians(required_lead_phase)))
            alpha = float((1.0 - sine) / (1.0 + sine))

    if tau_d is None:
        if omega_c is None:
            raise ValueError("omega_c is required to compute tau_d from alpha.")
        tau_d = float(1.0 / (omega_c * np.sqrt(alpha)))

    if omega_c is not None:
        s = 1j * omega_c
        lead_at_crossover = (tau_d * s + 1.0) / (alpha * tau_d * s + 1.0)
        lead_phase = _phase_near_negative_180(lead_at_crossover)
        if lead_phase < -90.0:
            lead_phase += 360.0

    if Kp is None:
        if omega_c is None:
            raise ValueError("Kp is required unless omega_c is supplied so |L(j*omega_c)| can be set to 1.")
        plant_value = eval_poly_tf(numerator, denominator, omega_c)
        controller_without_gain = pi_lead_frequency_response(omega_c, 1.0, tau_i, alpha, tau_d)
        magnitude_without_gain = abs(plant_value * controller_without_gain)
        if np.isclose(magnitude_without_gain, 0.0):
            raise ValueError("Cannot compute Kp because the open-loop magnitude without Kp is zero at omega_c.")
        Kp = float(1.0 / magnitude_without_gain)

    if omega_c is not None:
        plant_value = eval_poly_tf(numerator, denominator, omega_c)
        controller = pi_lead_frequency_response(omega_c, Kp, tau_i, alpha, tau_d)
        loop = plant_value * controller
        loop_mag = float(abs(loop))
        loop_phase = _phase_near_negative_180(loop)
        estimated_pm = float(180.0 + loop_phase)

    margin_data = {
        "gain_crossover_rad_s": None,
        "phase_margin_deg": None,
        "phase_crossover_rad_s": None,
        "gain_margin": None,
        "gain_margin_db": None,
    }
    if full_margin_check:
        try:
            margin_data.update(compute_margins(numerator, denominator, Kp, tau_i, alpha, tau_d))
        except Exception as exc:
            warnings.append(f"Full margin check failed: {exc}")

    result: dict[str, object] = {
        "Kp": float(Kp),
        "tau_i": float(tau_i),
        "n_i": None if n_i is None else float(n_i),
        "alpha": float(alpha),
        "tau_d": float(tau_d),
        "omega_c_target": omega_c,
        "phase_margin_target_deg": phase_margin_deg,
        "plant_mag_at_omega_c": plant_mag,
        "plant_phase_at_omega_c_deg": plant_phase,
        "pi_phase_at_omega_c_deg": pi_phase,
        "lead_phase_at_omega_c_deg": lead_phase,
        "loop_mag_at_omega_c": loop_mag,
        "loop_phase_at_omega_c_deg": loop_phase,
        "estimated_pm_at_omega_c_deg": estimated_pm,
        "gain_crossover_rad_s": margin_data["gain_crossover_rad_s"],
        "phase_margin_deg": margin_data["phase_margin_deg"],
        "phase_crossover_rad_s": margin_data["phase_crossover_rad_s"],
        "gain_margin": margin_data["gain_margin"],
        "gain_margin_db": margin_data["gain_margin_db"],
        "warnings": warnings,
        "required_lead_phase_deg": required_lead_phase,
        "proportional_gain": float(Kp),
        "plant_phase_deg": plant_phase,
        "pi_phase_deg": pi_phase,
        "loop_magnitude_at_crossover": loop_mag,
        "achieved_phase_margin_deg": estimated_pm,
    }
    return result


def design_pi_lead_at_crossover(
    numerator: Iterable[float],
    denominator: Iterable[float],
    omega_c: float,
    phase_margin_deg: float,
    n_i: float,
) -> dict[str, object]:
    """Backward-compatible wrapper for the classical PI-lead design case."""

    return design_pi_lead(
        numerator=numerator,
        denominator=denominator,
        omega_c=omega_c,
        phase_margin_deg=phase_margin_deg,
        n_i=n_i,
    )


def solve_lag_beta(lag_phase_deg: float, n_i: float) -> float:
    """Use when the required Lag phase at crossover and N_i are known.

    Solves phi_lag=atan(N_i*(1-beta)/(1+beta*N_i**2)).
    A valid Lag compensator must produce beta > 1.
    """
    if not np.isfinite(lag_phase_deg) or not -90.0 < lag_phase_deg < 0.0:
        raise ValueError("lag_phase_deg must be negative and greater than -90 degrees.")
    if not np.isfinite(n_i) or n_i <= 0:
        raise ValueError("n_i must be positive and finite.")
    tangent = float(np.tan(np.radians(lag_phase_deg)))
    divisor = n_i + tangent * n_i**2
    if np.isclose(divisor, 0.0):
        raise ValueError("The supplied phase produces no finite beta.")
    beta = (n_i - tangent) / divisor
    if beta <= 1.0:
        raise ValueError("The supplied phase and N_i do not define a Lag compensator with beta > 1.")
    return float(beta)


def ideal_disturbance_feedforward(
    plant_numerator: Iterable[float],
    plant_denominator: Iterable[float],
    disturbance_numerator: Iterable[float],
    disturbance_denominator: Iterable[float],
    disturbance_sign: int,
) -> dict[str, object]:
    """Use when an ideal measured-disturbance cancellation path is specified.

    For output contribution sigma_D*D*d + G*F_d*d, returns F_d=-sigma_D*D/G.
    The caller must read sigma_D from the diagram and assess model uncertainty.
    """
    if disturbance_sign not in (-1, 1):
        raise ValueError("disturbance_sign must be -1 or +1 from the summing junction.")
    g_num = np.asarray(list(plant_numerator), dtype=float)
    g_den = np.asarray(list(plant_denominator), dtype=float)
    d_num = np.asarray(list(disturbance_numerator), dtype=float)
    d_den = np.asarray(list(disturbance_denominator), dtype=float)
    for name, values in (
        ("plant_numerator", g_num),
        ("plant_denominator", g_den),
        ("disturbance_numerator", d_num),
        ("disturbance_denominator", d_den),
    ):
        if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
            raise ValueError(f"{name} must be a finite non-empty coefficient sequence.")
        if np.isclose(values[0], 0.0):
            raise ValueError(f"{name} must have a non-zero leading coefficient.")
    ff_num = -disturbance_sign * np.polymul(d_num, g_den)
    ff_den = np.polymul(d_den, g_num)
    ff_num = np.trim_zeros(ff_num, trim="f")
    ff_den = np.trim_zeros(ff_den, trim="f")
    poles = np.roots(ff_den)
    proper = ff_num.size <= ff_den.size
    stable = bool(np.all(np.real(poles) < 0.0))
    return {
        "numerator": ff_num.tolist(),
        "denominator": ff_den.tolist(),
        "proper": proper,
        "stable": stable,
        "nominal_cancellation": proper and stable,
    }
