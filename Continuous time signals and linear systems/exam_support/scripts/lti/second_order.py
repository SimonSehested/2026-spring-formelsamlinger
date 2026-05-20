"""Second-order LTIC system helpers."""

from __future__ import annotations

import math
from typing import Any

import numpy as np
import sympy as sp

s, t = sp.symbols("s t", real=True)
x = sp.Function("x")
y = sp.Function("y")


def classify_second_order(a1: float, a0: float, *, tol: float = 1e-10) -> dict[str, Any]:
    """
    Classify s^2 + a1*s + a0.

    Use when:
        An exam task gives a second-order denominator or differential equation.

    Returns:
        Dictionary with poles, wn, zeta, Q, damping_class, stable.
    """
    if a0 <= 0:
        raise ValueError("a0 must be positive for wn and zeta in the standard form.")
    wn = math.sqrt(a0)
    zeta = a1 / (2.0 * wn)
    q = math.inf if abs(zeta) < tol else 1.0 / (2.0 * zeta)
    poles = np.roots([1.0, float(a1), float(a0)])
    stable = bool(np.all(np.real(poles) < -tol))
    if abs(zeta - 1.0) <= tol:
        damping = "critically_damped"
    elif zeta > 1.0:
        damping = "overdamped"
    elif zeta > 0.0:
        damping = "underdamped"
    elif abs(zeta) <= tol:
        damping = "undamped"
    else:
        damping = "unstable_negative_damping"
    return {
        "wn": wn,
        "zeta": zeta,
        "Q": q,
        "poles": poles,
        "stable": stable,
        "damping_class": damping,
        "has_resonant_peak_lowpass": 0.0 < zeta < 1.0 / math.sqrt(2.0),
    }


def step_features_from_zeta_wn(zeta: float, wn: float) -> dict[str, float]:
    """
    Compute standard underdamped second-order step-response features.

    Assumptions:
        0 < zeta < 1 and wn > 0.
    """
    if not (0.0 < zeta < 1.0):
        raise ValueError("zeta must satisfy 0 < zeta < 1 for underdamped step features.")
    if wn <= 0:
        raise ValueError("wn must be positive.")
    wd = wn * math.sqrt(1.0 - zeta**2)
    po = 100.0 * math.exp(-zeta * math.pi / math.sqrt(1.0 - zeta**2))
    tp = math.pi / wd
    ts_2_percent = 4.0 / (zeta * wn)
    return {"zeta": zeta, "wn": wn, "wd": wd, "percent_overshoot": po, "peak_time": tp, "settling_time_2pct": ts_2_percent}


def estimate_from_overshoot_peak_time(percent_overshoot: float, peak_time: float) -> dict[str, float]:
    """
    Estimate zeta and wn from percent overshoot and first peak time.

    Use when:
        A second-order step plot gives PO and tp.
    """
    if not (0.0 < percent_overshoot < 100.0):
        raise ValueError("percent_overshoot must be between 0 and 100.")
    if peak_time <= 0:
        raise ValueError("peak_time must be positive.")
    log_po = math.log(percent_overshoot / 100.0)
    zeta = -log_po / math.sqrt(math.pi**2 + log_po**2)
    wd = math.pi / peak_time
    wn = wd / math.sqrt(1.0 - zeta**2)
    out = step_features_from_zeta_wn(zeta, wn)
    out["input_percent_overshoot"] = percent_overshoot
    out["input_peak_time"] = peak_time
    return out


def second_order_calculator(
    *,
    percent_overshoot: float | None = None,
    peak_time: float | None = None,
    zeta: float | None = None,
    wn: float | None = None,
    wd: float | None = None,
    q: float | None = None,
    a1: float | None = None,
    a0: float | None = None,
    dc_gain: float | None = None,
    final_value: float | None = None,
    numerator_type: str = "lowpass",
    settling_factor: float = 4.0,
) -> dict[str, Any]:
    """
    Infer common second-order quantities from whichever values are known.

    The denominator is assumed to be
        s**2 + a1*s + a0 = s**2 + 2*zeta*wn*s + wn**2.

    Step-response quantities such as percent overshoot, peak time and settling
    time use the standard underdamped lowpass formulas. If ``numerator_type`` is
    ``"lowpass"`` and ``dc_gain`` or ``final_value`` is supplied, ``b0`` is
    computed as ``gain*a0``.

    Examples:
        second_order_calculator(percent_overshoot=45.59, peak_time=0.785, final_value=2)
        second_order_calculator(a1=2, a0=17, final_value=2)
        second_order_calculator(zeta=0.24, wn=4.12)
    """
    notes: list[str] = []

    if wn is None and a0 is not None:
        if a0 < 0:
            notes.append("a0 < 0: wn is not real in the standard second-order form.")
        else:
            wn = math.sqrt(a0)

    if zeta is None and q is not None:
        if q == 0:
            notes.append("Q = 0: zeta cannot be computed as 1/(2Q).")
        else:
            zeta = 1.0 / (2.0 * q)

    if q is None and zeta is not None:
        q = math.inf if zeta == 0 else 1.0 / (2.0 * zeta)

    if zeta is None and a1 is not None and wn is not None:
        zeta = a1 / (2.0 * wn)

    if zeta is None and percent_overshoot is not None:
        if percent_overshoot <= 0:
            notes.append("percent_overshoot <= 0: zeta cannot be found from the overshoot formula.")
        else:
            log_po = math.log(percent_overshoot / 100.0)
            zeta = abs(log_po) / math.sqrt(math.pi**2 + log_po**2)
            q = 1.0 / (2.0 * zeta)

    if wd is None and peak_time is not None:
        if peak_time <= 0:
            notes.append("peak_time <= 0: wd cannot be computed.")
        else:
            wd = math.pi / peak_time

    if wn is None and wd is not None and zeta is not None:
        if zeta < 1:
            wn = wd / math.sqrt(1.0 - zeta**2)
        else:
            notes.append("zeta >= 1: peak-time/wd formulas do not apply to non-oscillatory systems.")

    if wd is None and wn is not None and zeta is not None:
        if zeta < 1:
            wd = wn * math.sqrt(1.0 - zeta**2)
        else:
            notes.append("zeta >= 1: there is no damped oscillation frequency wd.")

    if a1 is None and zeta is not None and wn is not None:
        a1 = 2.0 * zeta * wn

    if a0 is None and wn is not None:
        a0 = wn**2

    if q is None and zeta is not None:
        q = math.inf if zeta == 0 else 1.0 / (2.0 * zeta)

    po_calc = None
    peak_time_calc = None
    settling_time_calc = None
    theta_rad = None
    theta_deg = None
    poles = None
    damping_type = None

    if zeta is not None:
        if zeta < 1:
            damping_type = "underdamped"
            po_calc = 100.0 * math.exp(-zeta * math.pi / math.sqrt(1.0 - zeta**2))
            theta_rad = math.acos(zeta)
            theta_deg = math.degrees(theta_rad)
        elif math.isclose(zeta, 1.0):
            damping_type = "critically_damped"
        else:
            damping_type = "overdamped"

    if wd is not None and wd != 0:
        peak_time_calc = math.pi / wd

    if zeta is not None and wn is not None and zeta > 0:
        settling_time_calc = settling_factor / (zeta * wn)

    if zeta is not None and wn is not None:
        if zeta < 1:
            real = -zeta * wn
            imag = wn * math.sqrt(1.0 - zeta**2)
            poles = (complex(real, imag), complex(real, -imag))
        elif math.isclose(zeta, 1.0):
            poles = (-wn, -wn)
        else:
            root = wn * math.sqrt(zeta**2 - 1.0)
            poles = (-zeta * wn + root, -zeta * wn - root)

    b0 = None
    if numerator_type == "lowpass":
        gain = dc_gain if dc_gain is not None else final_value
        if gain is not None and a0 is not None:
            b0 = gain * a0
    else:
        notes.append("Numerator is not assumed lowpass; b0 is not computed from gain/final value.")

    denominator = None
    transfer_function = None
    differential_equation = None
    if a1 is not None and a0 is not None:
        denominator = s**2 + sp.Float(a1) * s + sp.Float(a0)
        if b0 is not None:
            transfer_function = sp.simplify(sp.Float(b0) / denominator)
            differential_equation = sp.Eq(
                sp.diff(y(t), t, 2) + sp.Float(a1) * sp.diff(y(t), t) + sp.Float(a0) * y(t),
                sp.Float(b0) * x(t),
            )

    return {
        "zeta": zeta,
        "Q": q,
        "wn": wn,
        "wd": wd,
        "a1": a1,
        "a0": a0,
        "percent_overshoot": po_calc,
        "peak_time": peak_time_calc,
        "settling_time": settling_time_calc,
        "theta_deg": theta_deg,
        "theta_rad": theta_rad,
        "poles": poles,
        "b0": b0,
        "damping_type": damping_type,
        "denominator": denominator,
        "transfer_function": transfer_function,
        "differential_equation": differential_equation,
        "notes": notes,
    }
