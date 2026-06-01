"""Public control-analysis helpers used by the exam notebook."""

from .design import (
    design_pi_lead,
    design_pi_lead_at_crossover,
    design_lag,
    feedforward_analysis,
    ideal_disturbance_feedforward,
    solve_lag_beta,
)
from .lti import (
    analyze_transfer_function,
    bode_to_transfer,
    closed_loop_analysis_from_coefficients,
    closed_loop_characteristic,
    closed_loop_poles,
    evaluate_transfer_function,
    frequency_response_point,
    phase_margin_from_point,
    nyquist_point_analysis,
    second_order_analysis,
    second_order_characteristics,
    steady_state_error_analysis,
    transfer_function_poles,
    unity_feedback_step_error,
)
from .stability import find_stable_gain_ranges, solve_stability_interval_by_boundary

__all__ = [
    "analyze_transfer_function",
    "bode_to_transfer",
    "closed_loop_analysis_from_coefficients",
    "closed_loop_characteristic",
    "closed_loop_poles",
    "design_lag",
    "design_pi_lead",
    "design_pi_lead_at_crossover",
    "evaluate_transfer_function",
    "feedforward_analysis",
    "find_stable_gain_ranges",
    "frequency_response_point",
    "ideal_disturbance_feedforward",
    "nyquist_point_analysis",
    "phase_margin_from_point",
    "second_order_analysis",
    "second_order_characteristics",
    "solve_lag_beta",
    "solve_stability_interval_by_boundary",
    "steady_state_error_analysis",
    "transfer_function_poles",
    "unity_feedback_step_error",
]
