"""Executable validation cases for all public exam helper functions."""

from __future__ import annotations

import math

import numpy as np
import sympy as sp

from scripts.control import (
    analyze_transfer_function,
    bode_to_transfer,
    closed_loop_characteristic,
    closed_loop_poles,
    design_pi_lead_at_crossover,
    evaluate_transfer_function,
    find_stable_gain_ranges,
    ideal_disturbance_feedforward,
    phase_margin_from_point,
    second_order_characteristics,
    solve_lag_beta,
    solve_stability_interval_by_boundary,
    transfer_function_poles,
    unity_feedback_step_error,
)


RESULTS: list[tuple[str, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    RESULTS.append((name, detail))


def expect_value_error(name: str, call) -> None:
    try:
        call()
    except ValueError:
        RESULTS.append((name, "ValueError raised as expected"))
        return
    raise AssertionError(f"{name}: expected ValueError")


def main() -> None:
    value = evaluate_transfer_function([1.0], [1.0, 1.0], 1.0)
    check("evaluate_transfer_function normal", np.isclose(value, 0.5 - 0.5j), str(value))
    expect_value_error("evaluate_transfer_function invalid omega", lambda: evaluate_transfer_function([1], [1, 1], -1))

    poles = transfer_function_poles([1.0, 2.0, 1.0])
    check("transfer_function_poles known", np.allclose(np.sort(poles), [-1, -1]), str(poles))
    expect_value_error("transfer_function_poles invalid", lambda: transfer_function_poles([0, 1]))

    s, k = sp.symbols("s k", real=True)
    bode_model = bode_to_transfer(20, poles=[10, 150], zeros=[100], variable=s)
    expected_bode_model = 150 * (s + 100) / ((s + 10) * (s + 150))
    check(
        "bode_to_transfer known breaks",
        sp.simplify(bode_model - expected_bode_model) == 0
        and bode_model.subs(s, 0) == 10,
        str(bode_model),
    )
    expect_value_error(
        "bode_to_transfer zero break frequency",
        lambda: bode_to_transfer(0, poles=[0], variable=s),
    )

    q4_boundary = closed_loop_poles([1.0], [1.0, 3.0, 3.0, 1.0], 8.0)
    check("closed_loop_poles boundary", np.any(np.isclose(np.real(q4_boundary), 0.0, atol=1e-8)), str(q4_boundary))
    q11 = closed_loop_poles([120.0], [1.0, 43.0, 120.0, 0.0], 25.0)
    check("closed_loop_poles F21 Q11", np.all(np.real(q11) < 0), str(q11))
    expect_value_error("closed_loop_poles invalid gain", lambda: closed_loop_poles([1], [1, 1], math.inf))

    symbolic_analysis = analyze_transfer_function(20 / (s**2 + 5 * s + 20), s)
    check(
        "analyze_transfer_function second order",
        symbolic_analysis["stable"] is True
        and symbolic_analysis["order"] == 2
        and symbolic_analysis["omega_n"] == 2 * sp.sqrt(5),
        str(symbolic_analysis),
    )
    first_order_analysis = analyze_transfer_function(1 / (s + 1), s)
    check(
        "analyze_transfer_function settling time",
        np.isclose(first_order_analysis["settling_time_2_percent"], -math.log(0.02), atol=0.01)
        and np.isclose(first_order_analysis["settling_time_1_percent"], -math.log(0.01), atol=0.01),
        str(first_order_analysis),
    )
    parameterized_analysis = analyze_transfer_function(k / (s**2 + 5 * s + k), s)
    check(
        "analyze_transfer_function parameterized",
        parameterized_analysis["stable"] is None
        and parameterized_analysis["stability_text"] == "afhaenger af parametre",
        str(parameterized_analysis),
    )
    characteristic = closed_loop_characteristic(k / (s * (s + 5)), variable=s)
    check(
        "closed_loop_characteristic negative feedback",
        sp.expand(characteristic - (s**2 + 5 * s + k)) == 0,
        str(characteristic),
    )
    positive_characteristic = closed_loop_characteristic(
        k / (s * (s + 5)), variable=s, negative_feedback=False
    )
    check(
        "closed_loop_characteristic positive feedback",
        sp.expand(positive_characteristic - (s**2 + 5 * s - k)) == 0,
        str(positive_characteristic),
    )

    gain_ranges = find_stable_gain_ranges((s + 1) ** 3 + k, k, s)
    check(
        "find_stable_gain_ranges known boundaries",
        gain_ranges["boundary_gains"] == [-1, 8],
        str(gain_ranges["boundary_points"]),
    )
    check(
        "find_stable_gain_ranges known stable interval",
        gain_ranges["stable_gain_intervals"] == [sp.Interval.open(-1, 8)],
        str(gain_ranges["stable_gain_intervals"]),
    )
    check(
        "find_stable_gain_ranges positive gain interval",
        gain_ranges["positive_stable_gain_intervals"] == [sp.Interval.open(0, 8)],
        str(gain_ranges["positive_stable_gain_intervals"]),
    )
    rational_ranges = find_stable_gain_ranges(1 + k / (s + 1) ** 3, k, s)
    check(
        "find_stable_gain_ranges rational characteristic equation",
        sp.expand(rational_ranges["characteristic"] - ((s + 1) ** 3 + k)) == 0
        and rational_ranges["stable_gain_intervals"] == [sp.Interval.open(-1, 8)],
        str(rational_ranges),
    )
    expect_value_error(
        "find_stable_gain_ranges changing degree",
        lambda: find_stable_gain_ranges(k * s**2 + s + 1, k, s),
    )
    boundary_interface = solve_stability_interval_by_boundary((s + 1) ** 3 + k, k, s)
    check(
        "solve_stability_interval_by_boundary stable interval",
        boundary_interface["boundary_gains"] == [-1, 8]
        and boundary_interface["stable_gain_intervals"] == [sp.Interval.open(-1, 8)],
        str(boundary_interface),
    )

    q16_error = unity_feedback_step_error([1224.0], [1.0, 30.0, 257.0, 612.0], 2.0)
    check("unity_feedback_step_error F21 Q16", np.isclose(q16_error, 0.2), str(q16_error))
    expect_value_error("unity_feedback_step_error unstable", lambda: unity_feedback_step_error([1], [1, -1], 0))

    margin = phase_margin_from_point(0.134, -0.99)
    check("phase_margin_from_point F21 Q14", np.isclose(margin, 97.71, atol=0.1), str(margin))
    expect_value_error("phase_margin_from_point origin", lambda: phase_margin_from_point(0, 0))

    metrics = second_order_characteristics([1.0, 5.0, 20.0])
    # F21 rounds the multiple-choice boundary K=20 to 12%; the exact value is 12.026%.
    check("second_order_characteristics Q9 rounded limit", metrics["overshoot_percent"] <= 12.1, str(metrics))
    check("second_order_characteristics known critical", second_order_characteristics([1, 2, 1])["overshoot_percent"] == 0, "critical damping")
    expect_value_error("second_order_characteristics invalid", lambda: second_order_characteristics([1, 2]))

    q18 = design_pi_lead_at_crossover(
        [0.7, 0.35],
        np.polymul(np.polymul([5.0, 1.0], [1.0, 0.2, 0.6]), [0.01, 1.0]),
        10.0,
        45.0,
        8.0,
    )
    check("design_pi_lead_at_crossover alpha Q18", np.isclose(q18["alpha"], 0.08, atol=0.005), str(q18))
    check("design_pi_lead_at_crossover Kp Q18", np.isclose(q18["proportional_gain"], 200, atol=2), str(q18))
    check("design_pi_lead_at_crossover target", np.isclose(q18["loop_magnitude_at_crossover"], 1), str(q18))
    expect_value_error(
        "design_pi_lead_at_crossover invalid Ni",
        lambda: design_pi_lead_at_crossover([1], [1, 1], 1, 60, 0),
    )

    beta = solve_lag_beta(-8.9193, 3.0)
    check("solve_lag_beta F21 Q17", np.isclose(beta, 1.9886, atol=1e-3), str(beta))
    expect_value_error("solve_lag_beta wrong phase", lambda: solve_lag_beta(10, 3))

    feedforward = ideal_disturbance_feedforward(
        [10.5, 21.0], [1.0, 4.0, 21.0], [1.0], [0.01, 1.0], -1
    )
    check("ideal_disturbance_feedforward Q20 proper", bool(feedforward["proper"]), str(feedforward))
    check("ideal_disturbance_feedforward Q20 stable", bool(feedforward["stable"]), str(feedforward))
    expect_value_error(
        "ideal_disturbance_feedforward sign",
        lambda: ideal_disturbance_feedforward([1], [1, 1], [1], [1, 1], 0),
    )

    print(f"Validated {len(RESULTS)} checks.")
    for name, detail in RESULTS:
        print(f"PASS | {name} | {detail}")


if __name__ == "__main__":
    main()
