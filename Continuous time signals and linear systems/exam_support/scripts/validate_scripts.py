"""Smoke validation for the exam toolbox."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.circuits.instrumentation import instrumentation_gains
from scripts.circuits.node_equations import solve_node_circuit
from scripts.expand import expand_expr, same_after_expand
from scripts.filters.butterworth import butterworth_highpass_order, butterworth_lowpass_order, butterworth_poles_q, frequency_scale_rc
from scripts.fourier.properties import exponential_transform_variant, omega
from scripts.fourier.series import complex_fourier_coefficients
from scripts.frequency.bode import bode_values, classify_filter_limits, transfer_from_poles_zeros
from scripts.lti.responses import impulse_response_from_transfer, ramp_response_from_transfer, related_unit_responses, step_response_from_transfer, transfer_from_ode, zero_input_laplace_second_order
from scripts.lti.second_order import classify_second_order, estimate_from_overshoot_peak_time, step_features_from_zeta_wn
from scripts.sampling.adc import adc_lsb, alias_frequency, required_sampling_rate_for_lsb
from scripts.transforms.convolution import convolve_causal
from scripts.transforms.laplace import inverse_laplace_rational

t = sp.symbols("t", real=True)


def _assert_close(value: float, expected: float, tol: float = 1e-6) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{value!r} != {expected!r}")


def main() -> None:
    c = classify_second_order(2, 17)
    _assert_close(c["wn"], math.sqrt(17))
    assert c["stable"] and c["damping_class"] == "underdamped"

    f = step_features_from_zeta_wn(0.5, 4.0)
    _assert_close(round(f["percent_overshoot"], 1), 16.3, 0.1)

    est = estimate_from_overshoot_peak_time(45.59, 0.78543)
    _assert_close(round(est["wn"], 4), 4.1231, 1e-4)
    _assert_close(round(est["settling_time_2pct"], 4), 4.0, 1e-3)

    est_exact = estimate_from_overshoot_peak_time(45.59, 0.785)
    _assert_close(est_exact["zeta"], 0.24256, 1e-5)
    _assert_close(est_exact["wn"], 4.12522, 1e-5)
    _assert_close(est_exact["wd"], 4.00203, 1e-5)
    _assert_close(est_exact["a1"], 2.001, 1e-3)
    _assert_close(est_exact["a0"], 17.018, 1e-3)
    _assert_close(est_exact["poles"][0].real, -1.0, 2e-3)
    _assert_close(est_exact["poles"][0].imag, 4.0, 3e-3)
    _assert_close(est_exact["poles"][1].real, -1.0, 2e-3)
    _assert_close(est_exact["poles"][1].imag, -4.0, 3e-3)
    for key in ["zeta", "wn", "wd", "percent_overshoot", "peak_time", "settling_time_2pct", "input_percent_overshoot", "input_peak_time"]:
        assert key in est_exact
    for bad_po in [0, -1, 100, 120]:
        try:
            estimate_from_overshoot_peak_time(bad_po, 0.785)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for percent_overshoot={bad_po}")
    for bad_tp in [0, -1]:
        try:
            estimate_from_overshoot_peak_time(45.59, bad_tp)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for peak_time={bad_tp}")

    h = impulse_response_from_transfer([32, 0], [1, 8, 16])
    assert sp.simplify(h - 32 * (1 - 4 * t) * sp.exp(-4 * t) * sp.Heaviside(t)) == 0

    ystep = step_response_from_transfer([1], [1, 2, 1])
    assert sp.simplify(ystep - (1 - (t + 1) * sp.exp(-t)) * sp.Heaviside(t)) == 0

    yramp = ramp_response_from_transfer([1], [1, 1])
    assert sp.simplify(yramp - (t - 1 + sp.exp(-t)) * sp.Heaviside(t)) == 0

    related = related_unit_responses((1 - sp.exp(-t)) * sp.Heaviside(t), "step")
    assert sp.simplify(related["impulse"] - sp.exp(-t) * sp.Heaviside(t)) == 0
    assert sp.simplify(related["ramp"] - (t - 1 + sp.exp(-t)) * sp.Heaviside(t)) == 0

    yzi = zero_input_laplace_second_order(2, 17, 2, 4)
    s = sp.symbols("s", real=True)
    assert sp.simplify(yzi - (2 * s + 8) / (s**2 + 2 * s + 17)) == 0

    tf = transfer_from_ode([1], [1, 2, 17])
    assert "H" in tf and len(tf["poles"]) == 2

    conv = convolve_causal(2 * sp.exp(-2 * t), t * sp.exp(-3 * t))
    expected_conv = (2 * sp.exp(-2 * t) - 2 * t * sp.exp(-3 * t) - 2 * sp.exp(-3 * t)) * sp.Heaviside(t)
    assert sp.simplify(conv - expected_conv) == 0

    expanded = expand_expr(((2 * t - 4) * sp.exp(t / 2) + 4) * sp.exp(-t / 2) * sp.Heaviside(t))
    assert sp.simplify(expanded - (2 * t - 4 + 4 * sp.exp(-t / 2)) * sp.Heaviside(t)) == 0
    assert same_after_expand(sp.exp(t) * sp.exp(-t), 1)

    inv = inverse_laplace_rational([1], [1, 1])
    assert sp.simplify(inv - sp.exp(-t) * sp.Heaviside(t)) == 0

    coeffs = complex_fourier_coefficients(1, t, 2 * sp.pi, [-1, 0, 1])
    assert coeffs[0] == 1 and coeffs[-1] == 0 and coeffs[1] == 0

    variant = exponential_transform_variant(3, modulation=2)
    assert sp.simplify(variant - 1 / (3 + sp.I * (omega - 2))) == 0

    bode = bode_values([1], [1, 1], [0, 1])
    _assert_close(float(bode["magnitude_db"][0]), 0.0)

    flt = classify_filter_limits([1], [1, 1])
    assert flt["probable_class"] == "lowpass"

    pz = transfer_from_poles_zeros([0], [-1, -2], 2)
    assert np.allclose(np.real(pz["den"]), [1, 3, 2])

    assert butterworth_lowpass_order(500, 3000, 3, 72) == 5
    assert butterworth_highpass_order(100, 10, 3, 26) == 2
    poles_q = butterworth_poles_q(2)
    _assert_close(round(poles_q["section_Q"][0], 6), round(1 / math.sqrt(2), 6))
    scaled = frequency_scale_rc(1000, 1e-6, 100)
    _assert_close(scaled["C"], 1e-8)

    _assert_close(adc_lsb(16, 0, 5), 5 / 65536)
    _assert_close(alias_frequency(4, 6), 2)
    _assert_close(required_sampling_rate_for_lsb(16, 5, 4, 100), 3200)

    gains = instrumentation_gains(499.5, 1, alpha=0.9)
    _assert_close(gains["Gd"], 1000.0)
    _assert_close(gains["Gc"], 0.05)

    R1, R2, C1, C2, V1, VA, VB = sp.symbols("R1 R2 C1 C2 V1 VA VB", positive=True, real=True)
    eqA = sp.Eq((VA - V1) * s * C1 + VA / R1 + (VA - VB) / R2, 0)
    eqB = sp.Eq((VB - VA) / R2 + VB * s * C2, 0)
    node = solve_node_circuit([eqA, eqB], [VA, VB], input_signal=V1, output_node=VB, s_symbol=s)
    expected_H = C1 * R1 * s / (C1 * C2 * R1 * R2 * s**2 + s * (C1 * R1 + C2 * R1 + C2 * R2) + 1)
    assert sp.simplify(node["H"] - expected_H) == 0
    assert node["numerator_coeffs"] == [C1 * R1, 0]
    assert node["denominator_coeffs"] == [C1 * C2 * R1 * R2, C1 * R1 + C2 * R1 + C2 * R2, 1]

    print("Validated exam toolbox successfully.")


if __name__ == "__main__":
    main()
