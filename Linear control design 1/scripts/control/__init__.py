"""Public control-analysis helpers used by the exam notebook."""

from .design import (
    design_pi_lead_at_crossover,
    ideal_disturbance_feedforward,
    solve_lag_beta,
)
from .lti import (
    analyze_transfer_function,
    bode_to_transfer,
    closed_loop_characteristic,
    closed_loop_poles,
    evaluate_transfer_function,
    phase_margin_from_point,
    second_order_characteristics,
    transfer_function_poles,
    unity_feedback_step_error,
)
from .stability import find_stable_gain_ranges, solve_stability_interval_by_boundary

__all__ = [
    "analyze_transfer_function",
    "bode_to_transfer",
    "closed_loop_characteristic",
    "closed_loop_poles",
    "design_pi_lead_at_crossover",
    "evaluate_transfer_function",
    "find_stable_gain_ranges",
    "ideal_disturbance_feedforward",
    "phase_margin_from_point",
    "second_order_characteristics",
    "solve_lag_beta",
    "solve_stability_interval_by_boundary",
    "transfer_function_poles",
    "unity_feedback_step_error",
]
