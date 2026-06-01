# Script-note integration report

Kilde for valideringsstatus: `scripts/validate_scripts.py`. Notesektioner henviser kun til offentlige funktioner eksporteret fra `scripts/control/__init__.py`.

| Script | Funktion | Notesektion | Support mode | Input | Output | Manuelt tjek | Brug ikke når | Valideret? |
| ------ | -------- | ----------- | ------------ | ----- | ------ | ------------ | ------------- | ---------- |
| `lti.py` | `transfer_function_poles` | Model og tidsrespons: ODE eller fysisk model til transferfunktion | `script_assisted` | Nævnerkoefficienter | Poler | Udledning og RHP/origo-fortolkning | Model kun er figur | Ja |
| `lti.py` | `analyze_transfer_function` | Model og tidsrespons: samlet TF-analyse | `script_assisted` | Symbolsk `G(s)` | Poler, nulpunkter, DC-gain, type, stabilitet, responsdata | Rigtigt input/outputpar | Diagram ikke reduceret | Ja |
| `lti.py` | `frequency_response_point` | Model/frekvens: punktrespons | `script_assisted` | Tæller, nævner, `omega` | Kompleks værdi, magnitude, dB, fase | Valgt frekvens | Plot skal aflæses | Ja |
| `stability.py` | `find_stable_gain_ranges` | Model og tidsrespons: gain-afhaengigt karakteristisk polynomium | `script_primary` | `p(s,K), K, s` | Marginalpunkter, stabile intervaller | Udledning og tilladt gain-domain | Graden skifter med gain | Ja |
| `stability.py` | `solve_stability_interval_by_boundary` | Nyquist/stabilitet: kompakt boundary-workflow | `script_primary` | `p(s,K), K, s` | Boundary equations og stabile intervaller | Udledning og gain-domain | Graden skifter med gain | Ja |
| `lti.py` | `evaluate_transfer_function` | Bode-plot og P-gain; P-gain fra margin | `script_assisted` | Tæller, nævner, `omega` | Kompleks respons | Valgt frekvens/plotfortolkning | TF ikke er kendt | Ja |
| `lti.py` | `closed_loop_poles` | Bode-plot og P-gain; Nyquist efter manuel beslutning | `script_assisted` | TF og foreslået gain | Closed-loop-poler | Loopstruktur og stabilitetskriterium | Diagram ikke reduceret | Ja |
| `lti.py` | `closed_loop_analysis_from_coefficients` | Feedback og stationær fejl | `script_assisted` | TF og foreslået gain | Karakteristisk polynomium, poler, stabilitet, DC-gain | Loopstruktur | Ikke standard negativ feedback | Ja |
| `lti.py` | `closed_loop_characteristic` | Feedback og stabilitet | `script_assisted` | Symbolsk forward/feedback | Karakteristisk polynomium | Feedbackfortegn | Diagram ikke reduceret | Ja |
| `lti.py` | `unity_feedback_step_error` | Blokdiagramreduktion; Stationær referencefejl | `script_assisted` | TF og gain | `e_ss` | Error path og stabilitet | Ikke standard unity error path | Ja |
| `lti.py` | `steady_state_error_analysis` | Stationær referencefejl | `script_assisted` | TF, gain, inputtype | Systemtype, fejlkonstanter, `e_ss` | Standardloop og stabilitet | Disturbance path uden reduktion | Ja |
| `lti.py` | `phase_margin_from_point` | Phase margin fra Nyquist-punkt | `script_assisted` | Real-/imaginærdel | `gamma_M` i grader | Punkt/kvadrant | Encirclement kræves | Ja |
| `lti.py` | `nyquist_point_analysis` | Phase margin fra Nyquist-punkt | `script_assisted` | Real-/imaginærdel | Magnitude, fase, PM, afstand til -1 | Punkt/kvadrant | Encirclement kræves | Ja |
| `lti.py` | `second_order_characteristics` | Første- og andenordens steprespons | `script_assisted` | Andenordensnævner | `omega_n,zeta,M_p` | Standardmodelmatch | Dominerende ekstra poler | Ja |
| `lti.py` | `second_order_analysis` | Første- og andenordens steprespons | `script_assisted` | Andenordensnævner | Udvidede andenordensmetrics | Standardmodelmatch | Højereordensdominans | Ja |
| `lti.py` | `bode_to_transfer` | Bode-plot og asymptoter | `script_assisted` | DC-gain dB, breaks | Symbolsk TF | RHP/LHP fasefortolkning | Kurven ikke aflæst | Ja |
| `design.py` | `design_pi_lead` | PI-Lead design | `script_primary` | TF og kendte PI-lead-størrelser | Parametre, checks, margins, warnings | Struktur, limits, model | Metodevalg ikke fastlagt | Ja |
| `design.py` | `design_pi_lead_at_crossover` | PI-Lead design | `script_primary` | TF, `omega_c`, PM, `N_i` | `alpha,tau_i,tau_d,K_P`, checks | Struktur, limits, model | Metodevalg ikke fastlagt | Ja |
| `design.py` | `solve_lag_beta` | P-Lead-Lag og actuatorbegrænsning | `script_primary` | Krævet lagfase, `N_i` | `beta` | Fasebalance, `beta>1` | PI i stedet for Lag | Ja |
| `design.py` | `design_lag` | P-Lead-Lag og actuatorbegrænsning | `script_primary` | Lagfase, `N_i`, evt. `omega_c/tau_i/beta` | `beta`, tider/frekvenser, warnings | Fasebalance, `beta>1` | Limit/windupdesign | Ja |
| `design.py` | `ideal_disturbance_feedforward` | Dynamisk feed-forward | `script_assisted` | `G,D,sigma_D` | Ratio, proper/stable | Fortegn, målelighed, usikkerhed | Ukendt disturbance/model | Ja |
| `design.py` | `feedforward_analysis` | Dynamisk feed-forward | `script_assisted` | `G,D,sigma_D` | Ratio, poler, zeros, realiserbarhed | Fortegn, målelighed, usikkerhed | Ukendt disturbance/model | Ja |

## Kontrol

- Alle offentlige funktioner er nævnt i noterne og i notebooken.
- Alle offentlige funktioner dækkes af `scripts/validate_scripts.py`, inkl. dokumentationskonsistens.
- Noterne angiver manuel metode/ansvar ved hver Python-reference.
- Ingen notesektion henviser til en funktion, der ikke er implementeret.
