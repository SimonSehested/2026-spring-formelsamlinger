# Script-note integration report

Kilde for valideringsstatus: `reports/script_validation_report.md`. Notesektioner henviser kun til offentlige funktioner eksporteret fra `scripts/control/__init__.py`.

| Script | Funktion | Notesektion | Support mode | Input | Output | Manuelt tjek | Brug ikke når | Valideret? |
| ------ | -------- | ----------- | ------------ | ----- | ------ | ------------ | ------------- | ---------- |
| `lti.py` | `transfer_function_poles` | Model og tidsrespons: ODE eller fysisk model til transferfunktion | `script_assisted` | Nævnerkoefficienter | Poler | Udledning og RHP/origo-fortolkning | Model kun er figur | Ja |
| `stability.py` | `find_stable_gain_ranges` | Model og tidsrespons: gain-afhaengigt karakteristisk polynomium | `script_primary` | `p(s,K), K, s` | Marginalpunkter, stabile intervaller | Udledning og tilladt gain-domain | Graden skifter med gain | Ja |
| `lti.py` | `evaluate_transfer_function` | Bode-plot og P-gain; P-gain fra margin | `script_assisted` | Tæller, nævner, `omega` | Kompleks respons | Valgt frekvens/plotfortolkning | TF ikke er kendt | Ja |
| `lti.py` | `closed_loop_poles` | Bode-plot og P-gain; Nyquist efter manuel beslutning | `script_assisted` | TF og foreslået gain | Closed-loop-poler | Loopstruktur og stabilitetskriterium | Diagram ikke reduceret | Ja |
| `lti.py` | `unity_feedback_step_error` | Blokdiagramreduktion; Stationær referencefejl | `script_assisted` | TF og gain | `e_ss` | Error path og stabilitet | Ikke standard unity error path | Ja |
| `lti.py` | `phase_margin_from_point` | Phase margin fra Nyquist-punkt | `script_assisted` | Real-/imaginærdel | `gamma_M` i grader | Punkt/kvadrant | Encirclement kræves | Ja |
| `lti.py` | `second_order_characteristics` | Første- og andenordens steprespons | `script_assisted` | Andenordensnævner | `omega_n,zeta,M_p` | Standardmodelmatch | Dominerende ekstra poler | Ja |
| `design.py` | `design_pi_lead_at_crossover` | PI-Lead design | `script_primary` | TF, `omega_c`, PM, `N_i` | `alpha,tau_i,tau_d,K_P`, checks | Struktur, limits, model | Metodevalg ikke fastlagt | Ja |
| `design.py` | `solve_lag_beta` | P-Lead-Lag og actuatorbegrænsning | `script_primary` | Krævet lagfase, `N_i` | `beta` | Fasebalance, `beta>1` | PI i stedet for Lag | Ja |
| `design.py` | `ideal_disturbance_feedforward` | Dynamisk feed-forward | `script_assisted` | `G,D,sigma_D` | Ratio, proper/stable | Fortegn, målelighed, usikkerhed | Ukendt disturbance/model | Ja |

## Kontrol

- Alle ti eksporterede funktioner er nævnt i noterne og i notebooken.
- Alle ti findes i `script_validation_report.md` med beståede cases.
- Noterne angiver manuel metode/ansvar ved hver Python-reference.
- Ingen notesektion henviser til en funktion, der ikke er implementeret.
