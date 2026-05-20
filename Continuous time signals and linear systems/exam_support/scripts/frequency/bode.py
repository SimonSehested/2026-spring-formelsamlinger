"""Bode and pole-zero helpers."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np


def bode_values(num: Sequence[float], den: Sequence[float], omega: Sequence[float]) -> dict[str, np.ndarray]:
    """
    Evaluate H(jw) and return magnitude in dB and phase in degrees.
    """
    w = np.asarray(omega, dtype=float)
    if np.any(w < 0):
        raise ValueError("omega values must be nonnegative.")
    jw = 1j * w
    numerator = np.polyval(np.asarray(num, dtype=float), jw)
    denominator = np.polyval(np.asarray(den, dtype=float), jw)
    if np.any(np.isclose(denominator, 0.0)):
        raise ValueError("frequency grid includes a pole.")
    H = numerator / denominator
    return {"omega": w, "H": H, "magnitude_db": 20 * np.log10(np.abs(H)), "phase_deg": np.angle(H, deg=True)}


def classify_filter_limits(num: Sequence[float], den: Sequence[float], *, tol: float = 1e-9) -> dict[str, Any]:
    """
    Classify a proper rational filter from DC and high-frequency limits.
    """
    n = np.trim_zeros(np.asarray(num, dtype=float), "f")
    d = np.trim_zeros(np.asarray(den, dtype=float), "f")
    if len(n) == 0:
        raise ValueError("numerator must not be all zeros.")
    dc_den = np.polyval(d, 0.0)
    dc_gain = np.inf if abs(dc_den) < tol else np.polyval(n, 0.0) / dc_den
    deg_n = len(n) - 1
    deg_d = len(d) - 1
    if deg_n < deg_d:
        hf_gain = 0.0
    elif deg_n == deg_d:
        hf_gain = n[0] / d[0]
    else:
        hf_gain = np.inf
    if abs(dc_gain) > tol and abs(hf_gain) <= tol:
        cls = "lowpass"
    elif abs(dc_gain) <= tol and np.isfinite(hf_gain) and abs(hf_gain) > tol:
        cls = "highpass"
    elif abs(dc_gain) <= tol and abs(hf_gain) <= tol:
        cls = "bandpass_or_notch_check_zeros"
    elif abs(dc_gain) > tol and np.isfinite(hf_gain) and abs(hf_gain) > tol:
        cls = "allpass_or_notch_or_shelving"
    else:
        cls = "requires_context"
    return {"dc_gain": dc_gain, "high_frequency_gain": hf_gain, "degree_num": deg_n, "degree_den": deg_d, "probable_class": cls}


def transfer_from_poles_zeros(zeros: Sequence[complex], poles: Sequence[complex], gain: float = 1.0) -> dict[str, np.ndarray]:
    """
    Build numerator and denominator coefficients from zeros, poles, and gain.
    """
    num = gain * np.poly(np.asarray(zeros, dtype=complex)) if len(zeros) else np.array([gain], dtype=complex)
    den = np.poly(np.asarray(poles, dtype=complex)) if len(poles) else np.array([1.0], dtype=complex)
    return {"num": np.real_if_close(num), "den": np.real_if_close(den)}
