# Notebook inventory

Notebook: `exam_toolbox.ipynb`. Notebooken er bevidst reduceret til kodeceller med et kommenteret funktionsindeks og korte kørbare kontrolcases. Alle importerede funktioner er opført som bestået i `script_validation_report.md`.

Runtime: Notebooken opretter eller kræver ikke et projektlokalt Python-miljø eller en projektspecifik kernelspec.

| Notebooksektion | Funktioner | Opgavetyper | Eksempel testet? | Input forklaret? | Output forklaret? | Manuelt tjek forklaret? | Begrænsninger |
| --------------- | ---------- | ----------- | ---------------- | ---------------- | ----------------- | ----------------------- | ------------- |
| Setup og imports | Alle offentlige | Alle script-assisted/primary | Ja, importtest | Ja | Ja | Ja | Finder kun projektrod med `scripts/control` |
| Kommenteret indeks: TF, feedback, respons | `evaluate_transfer_function`, `transfer_function_poles`, `closed_loop_poles`, `unity_feedback_step_error`, `second_order_characteristics` | Q4,Q8,Q9,Q11,Q12,Q16 | Ja; kørbare cases nederst | Ja | Ja | Ja | Ingen figurparser |
| Kommenteret indeks: Bode, Nyquist, design | `phase_margin_from_point`, `design_pi_lead_at_crossover`, `solve_lag_beta`, `ideal_disturbance_feedforward` | Q14,Q17,Q18,Q20 | Ja; kørbare cases nederst | Ja | Ja | Ja | Metode/fortegn vælges manuelt |
| Symbolsk stabilitetsinterval | `find_stable_gain_ranges` | Gain-afhaengigt `p(s,K)` | Ja; `(s+1)^3+K` | Ja | Ja | Ja | Konstant grad i `s` kraeves |

Verification: Notebookens fire kodeceller er kontrolleret sekventielt med tilgængelige dependencies; ingen celle indeholder gemte controllerfejl.
