"""Controller-design computations that expose, rather than choose, assumptions."""

from __future__ import annotations

from typing import Iterable

import numpy as np

from .lti import evaluate_transfer_function


def design_pi_lead_at_crossover(
    numerator: Iterable[float],
    denominator: Iterable[float],
    omega_c: float,
    phase_margin_deg: float,
    n_i: float,
) -> dict[str, float]:
    """Use when PI-Lead structure, crossover and phase margin are specified.

    The PI zero satisfies n_i=omega_c*tau_i, and the lead maximum phase is
    centered at omega_c. Returns alpha, time constants, Kp and target checks.
    """
    if not np.isfinite(omega_c) or omega_c <= 0:
        raise ValueError("omega_c must be positive and finite.")
    if not np.isfinite(phase_margin_deg) or not 0 < phase_margin_deg < 180:
        raise ValueError("phase_margin_deg must lie strictly between 0 and 180 degrees.")
    if not np.isfinite(n_i) or n_i <= 0:
        raise ValueError("n_i must be positive and finite.")

    plant_value = evaluate_transfer_function(numerator, denominator, omega_c)
    plant_phase = float(np.degrees(np.angle(plant_value)))
    if plant_phase > 0:
        plant_phase -= 360.0
    phi_pi = float(np.degrees(np.arctan(n_i)) - 90.0)
    phi_lead = -180.0 + phase_margin_deg - plant_phase - phi_pi
    if not 0.0 < phi_lead < 90.0:
        raise ValueError(
            "The requested design needs a lead phase outside (0, 90) degrees; "
            "change the specified structure or crossover."
        )
    sine = float(np.sin(np.radians(phi_lead)))
    alpha = (1.0 - sine) / (1.0 + sine)
    tau_i = n_i / omega_c
    tau_d = 1.0 / (omega_c * np.sqrt(alpha))
    s = 1j * omega_c
    pi_without_gain = (tau_i * s + 1.0) / (tau_i * s)
    lead = (tau_d * s + 1.0) / (alpha * tau_d * s + 1.0)
    proportional_gain = 1.0 / abs(plant_value * pi_without_gain * lead)
    loop = proportional_gain * plant_value * pi_without_gain * lead
    achieved_phase = float(np.degrees(np.angle(loop)))
    if achieved_phase > 0:
        achieved_phase -= 360.0
    return {
        "plant_phase_deg": plant_phase,
        "pi_phase_deg": phi_pi,
        "required_lead_phase_deg": phi_lead,
        "alpha": float(alpha),
        "tau_i": float(tau_i),
        "tau_d": float(tau_d),
        "proportional_gain": float(proportional_gain),
        "loop_magnitude_at_crossover": float(abs(loop)),
        "achieved_phase_margin_deg": float(180.0 + achieved_phase),
    }


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
