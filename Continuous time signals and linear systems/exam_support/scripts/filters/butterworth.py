"""Butterworth and RC scaling helpers."""

from __future__ import annotations

import math
from typing import Any

import numpy as np


def butterworth_lowpass_order(fp: float, fs: float, ap_db: float, as_db: float) -> int:
    """
    Minimum Butterworth lowpass order from passband/stopband specs.
    """
    if not (0 < fp < fs):
        raise ValueError("Require 0 < fp < fs for lowpass design.")
    if ap_db <= 0 or as_db <= ap_db:
        raise ValueError("Require 0 < ap_db < as_db.")
    ratio = (10 ** (as_db / 10.0) - 1.0) / (10 ** (ap_db / 10.0) - 1.0)
    n = math.log10(ratio) / (2.0 * math.log10(fs / fp))
    return int(math.ceil(n))


def butterworth_highpass_order(fp: float, fs: float, ap_db: float, as_db: float) -> int:
    """Minimum Butterworth highpass order where fs < fp."""
    if not (0 < fs < fp):
        raise ValueError("Require 0 < fs < fp for highpass design.")
    return butterworth_lowpass_order(1.0 / fp, 1.0 / fs, ap_db, as_db)


def butterworth_poles_q(order: int, cutoff: float = 1.0) -> dict[str, Any]:
    """
    Stable Butterworth poles and second-order section Q values.
    """
    if order < 1:
        raise ValueError("order must be at least 1.")
    if cutoff <= 0:
        raise ValueError("cutoff must be positive.")
    poles = []
    for k in range(order):
        angle = math.pi / 2.0 + (2 * k + 1) * math.pi / (2.0 * order)
        poles.append(cutoff * np.exp(1j * angle))
    qs = []
    for p in poles:
        if np.imag(p) > 1e-10:
            zeta = -np.real(p) / abs(p)
            qs.append(float(1.0 / (2.0 * zeta)))
    return {"poles": np.array(poles), "section_Q": qs}


def frequency_scale_rc(R: float, C: float, omega_c: float, *, mode: str = "keep_R") -> dict[str, float]:
    """
    Scale normalized RC values from 1 rad/s to target omega_c.
    """
    if R <= 0 or C <= 0 or omega_c <= 0:
        raise ValueError("R, C, and omega_c must be positive.")
    if mode == "keep_R":
        return {"R": R, "C": C / omega_c}
    if mode == "keep_C":
        return {"R": R / omega_c, "C": C}
    raise ValueError("mode must be 'keep_R' or 'keep_C'.")
