"""Instrumentation amplifier helpers."""

from __future__ import annotations

import math


def instrumentation_gains(R2: float, RG: float, alpha: float = 1.0) -> dict[str, float]:
    """
    Compute ideal differential gain and single-mismatch common-mode gain.
    """
    if R2 <= 0 or RG <= 0:
        raise ValueError("R2 and RG must be positive.")
    gd = 1.0 + 2.0 * R2 / RG
    gc = (1.0 - alpha) / 2.0
    cmrr_db = math.inf if gc == 0 else 20.0 * math.log10(abs(gd / gc))
    return {"Gd": gd, "Gc": gc, "CMRR_dB": cmrr_db}
