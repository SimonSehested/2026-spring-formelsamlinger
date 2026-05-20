"""Sampling, aliasing, and ADC helpers."""

from __future__ import annotations

import math


def adc_lsb(bits: int, v_min: float = 0.0, v_max: float = 5.0) -> float:
    """Return ideal ADC LSB size."""
    if bits <= 0:
        raise ValueError("bits must be positive.")
    if v_max <= v_min:
        raise ValueError("v_max must exceed v_min.")
    return (v_max - v_min) / (2**bits)


def alias_frequency(f_signal: float, f_sample: float) -> float:
    """
    Fold a positive tone frequency into [0, Fs/2].
    """
    if f_signal < 0 or f_sample <= 0:
        raise ValueError("f_signal must be nonnegative and f_sample positive.")
    folded = f_signal % f_sample
    return min(folded, f_sample - folded)


def required_sampling_rate_for_lsb(bits: int, v_range: float, filter_order: int, f_3db: float, worst_amplitude: float | None = None) -> float:
    """
    Minimum Fs so a high-frequency worst-case amplitude is below one LSB after
    Butterworth high-frequency asymptotic attenuation at Fs/2.
    """
    if filter_order <= 0 or f_3db <= 0 or v_range <= 0:
        raise ValueError("filter_order, f_3db, and v_range must be positive.")
    amp = v_range if worst_amplitude is None else worst_amplitude
    if amp <= 0:
        raise ValueError("worst_amplitude must be positive.")
    lsb = v_range / (2**bits)
    required_ratio = (amp / lsb) ** (1.0 / filter_order)
    return 2.0 * f_3db * required_ratio
