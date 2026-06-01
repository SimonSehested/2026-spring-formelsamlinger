# Notebook inventory

Notebook: `exam_toolbox.ipynb`. Notebooken er bevidst reduceret til kodeceller med et kommenteret funktionsindeks og korte kørbare kontrolcases. Alle importerede funktioner er opført som bestået i `script_validation_report.md`.

Runtime: Notebooken opretter eller kræver ikke et projektlokalt Python-miljø eller en projektspecifik kernelspec.

| Notebooksektion | Funktioner | Opgavetyper | Eksempel testet? | Input forklaret? | Output forklaret? | Manuelt tjek forklaret? | Begrænsninger |
| --------------- | ---------- | ----------- | ---------------- | ---------------- | ----------------- | ----------------------- | ------------- |
| Setup og imports | Alle offentlige | Alle script-assisted/primary | Ja, importtest | Ja | Ja | Ja | Finder kun projektrod med `scripts/control` |
| Kommenteret indeks: TF, feedback, respons | `evaluate_transfer_function`, `frequency_response_point`, `transfer_function_poles`, `analyze_transfer_function`, `closed_loop_poles`, `closed_loop_analysis_from_coefficients`, `closed_loop_characteristic`, `unity_feedback_step_error`, `steady_state_error_analysis`, `second_order_characteristics`, `second_order_analysis` | Q4,Q8,Q9,Q11,Q12,Q16 | Ja; kørbare cases nederst og validation | Ja | Ja | Ja | Ingen figurparser |
| Kommenteret indeks: Bode, Nyquist, design | `bode_to_transfer`, `phase_margin_from_point`, `nyquist_point_analysis`, `design_pi_lead`, `design_pi_lead_at_crossover`, `solve_lag_beta`, `design_lag`, `ideal_disturbance_feedforward`, `feedforward_analysis` | Q14,Q17,Q18,Q20 | Ja; kørbare cases nederst og validation | Ja | Ja | Ja | Metode/fortegn vælges manuelt |
| Symbolsk stabilitetsinterval | `find_stable_gain_ranges`, `solve_stability_interval_by_boundary` | Gain-afhaengigt `p(s,K)` | Ja; `(s+1)^3+K` | Ja | Ja | Ja | Konstant grad i `s` kraeves |

Verification: `scripts/validate_scripts.py` kontrollerer nu, at alle offentlige helpers er dokumenteret i både notebooken og notesektionerne.
