# Script validation report

## Kørsel

- Kommando: `python -m scripts.validate_scripts`
- Resultat: `Validated 36 checks.`; alle checks bestået.
- Importtest: `python -c "from scripts.control import *; print('public import ok')"` bestået.
- Compiletest: `python -m compileall -q scripts` bestået.

| Funktion | Fil | Kategori | Testinput | Forventet resultat | Faktisk resultat | Status | Begrænsninger |
| -------- | --- | -------- | --------- | ------------------ | ---------------- | ------ | ------------- |
| `evaluate_transfer_function` | `scripts/control/lti.py` | Normal/invalid | `1/(s+1)`, `omega=1`; `omega=-1` | `0.5-0.5j`; fejl | Som forventet | Bestået | Kræver allerede opstillet TF |
| `analyze_transfer_function` | `scripts/control/lti.py` | Symbolsk/numerisk settling | `20/(s^2+5s+20)`, `1/(s+1)`, `k/(s^2+5s+k)` | Stabilitet, andenordensdata, 2%/1%-settling for numerisk stabil model | Som forventet | Bestået | Settling beregnes kun for stabile, proper, numeriske modeller med ikke-nul slutværdi |
| `transfer_function_poles` | `scripts/control/lti.py` | Known/invalid | `[1,2,1]`; ledende nul | `[-1,-1]`; fejl | Som forventet | Bestået | Fortolker ikke figur |
| `closed_loop_poles` | `scripts/control/lti.py` | Boundary/exam/invalid | Q4 `K=8`; Q11 `K=25`; infinite gain | Marginal; stabil; fejl | Q4 imaginærakse, Q11 alle LHP, fejl | Bestået | Struktur skal verificeres manuelt |
| `find_stable_gain_ranges` | `scripts/control/stability.py` | Boundary/interval/rational/invalid | `(s+1)^3+K`; `1+K/(s+1)^3`; gain-afhaengig ledende koefficient | `-1<K<8`, positivt `0<K<8`; rational form samme svar; fejl | Som forventet | Bestået | Kræver karakteristisk ligning med konstant grad efter samling |
| `unity_feedback_step_error` | `scripts/control/lti.py` | Exam/unstable | Q16; ustabil simpel loop | `0.2`; fejl | `0.2`; fejl | Bestået | Kun verificeret negativ unity loop |
| `phase_margin_from_point` | `scripts/control/lti.py` | Exam/invalid | Q14 `(0.134,-0.99)`; origo | `~97.7 deg`; fejl | `97.7083 deg`; fejl | Bestået | Punkt skal aflæses manuelt |
| `second_order_characteristics` | `scripts/control/lti.py` | Exam/known/invalid | Q9 ved `K=20`; `[1,2,1]`; forkert orden | `~12 %`; 0; fejl | `12.0265 %`; 0; fejl | Bestået | F21 afrunder Q9-grænsen |
| `design_pi_lead_at_crossover` | `scripts/control/design.py` | Exam/target/invalid | Q18; `N_i=0` | `alpha~0.08`, `K_P~200`, target; fejl | `0.08008`, `200.186`, target opfyldt; fejl | Bestået | Struktur/crossover vælges ikke |
| `solve_lag_beta` | `scripts/control/design.py` | Exam/invalid | Q17 `phi=-8.9193`, `N_i=3`; positiv fase | `beta~1.9886`; fejl | `1.98858`; fejl | Bestået | Krævet fase skal udledes manuelt |
| `ideal_disturbance_feedforward` | `scripts/control/design.py` | Exam/invalid | Q20, `sigma_D=-1`; ulovligt fortegn | Proper/stabil; fejl | Proper/stabil; fejl | Bestået | Nominal model; fortegn manuelt |

## Kildeafvigelser observeret ved validering

- Q9's facitoption accepterer `K=20` som 12 % overshoot; standardformlen giver `12.0265 %`. Dette er behandlet som afrunding, ikke som eksakt ulighed.
- Q18's trykte transferfunktion evalueres i scriptet til plantfase `-186.27 deg` ved `10 rad/s`; solutionteksten skriver `-184.98 deg`. Begge leder til samme valgbare design (`alpha=0.08`, `K_P` omkring `200`), så funktionen valideres mod de opgivne koefficienter og det korrekte svarvalg.
