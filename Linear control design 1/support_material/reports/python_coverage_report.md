# Python coverage report

## Afgrænsning

Python-værktøjskassen er en regne- og kontrolhjælper. Den kræver, at brugeren først har udledt den rette transferfunktion, valgt den relevante metode og aflæst figur-/blokdiagramdata korrekt.

| Opgavetype | Support mode | Script/funktion | Hvad Python gør | Hvad brugeren selv skal gøre | Brug ikke når | Status |
| ---------- | ------------ | --------------- | --------------- | ---------------------------- | ------------- | ------ |
| Poler fra TF/ODE | `script_assisted` | `transfer_function_poles` | Beregner rødder | Udled nævner og fortolk stabilitet | Model ikke er opstillet | Valideret; dækker bl.a. S20 Q16, 2022 Q8 og E23 Q7 |
| Symbolsk stabilitetsinterval i gain | `script_primary` | `find_stable_gain_ranges` | Finder `j*w`-graenser og tester poleplacering i intervaller | Udled `p(s,K)` og kontroller at gain-interval er relevant | Graden i `s` aendres med gain eller model kun er figur | Valideret |
| P-gain closed-loop kontrol | `script_assisted` | `closed_loop_poles` | Beregner poler for foreslået gain | Kontrollér loopstruktur og vælg kandidat | Feedback ikke matcher formel | Valideret |
| TF ved frekvens | `script_assisted` | `evaluate_transfer_function` | Beregner kompleks værdi | Udled TF og vælg relevant frekvens | Plot skal fortolkes | Valideret; relevant for 2022 Q7/Q13 |
| Unit-step-fejl | `script_assisted` | `unity_feedback_step_error` | DC/slutværdi med stabilitetscheck | Bekræft error path | Ikke-unity/anden error-definition | Valideret; referencefejl dækkes, disturbance-fejl kræver manuel path |
| Andenordens overshoot | `script_assisted` | `second_order_characteristics` | `omega_n`, `zeta`, overshoot | Match nævner til standardform | Højereordensdomineret system | Valideret; relevant for S20 Q5 og 2022 Q3 |
| PM fra Nyquist-punkt | `script_assisted` | `phase_margin_from_point` | Beregner vinkel/margin | Aflæs rette punkt/kvadrant | Encirclement er spørgsmålet | Valideret |
| PI-Lead ved specificeret crossover | `script_primary` | `design_pi_lead_at_crossover` | Løser fase- og magnitudebalance | Vælg struktur/specifikation og check limits | Designvalget er åbent | Valideret |
| Lag-parameter | `script_primary` | `solve_lag_beta` | Løser `beta` fra krævet lagfase | Udled fasebalance | Det er PI, ikke Lag | Valideret |
| Ideal disturbance feed-forward | `script_assisted` | `ideal_disturbance_feedforward` | Danner ratio og checker proper/stable | Læs fortegn og vurdér model/måling | Ukendt/unmeasured disturbance | Valideret |
| Blokdiagram fra figur | `notes_only` | Ingen | Intet | Udled signalalgebra | Altid | Ikke automatiseret |
| Bode/Nyquist-figurfortolkning | `notes_only` | Ingen | Intet | Aflæs curves, direction, RHP/LHP | Altid | Ikke automatiseret |
| Limited system/windup | `notes_only` | Ingen | Intet | Vurder ikke-linearitet og mitigation | Altid | Ikke automatiseret |
| Systemtype/static loopgain | `notes_only` | Ingen | Intet | Saml open-loop og tæl origo-poler | Når kun figur/notation er givet | Ikke automatiseret |
| Bandwidth/steprespons fra plot | `notes_only` | Ingen | Intet | Aflæs -3 dB, peakperiode og slutværdi | Plotdata ikke struktureret | Ikke automatiseret |
| P-Lead zero/pole og leadbidrag | `script_assisted` | `evaluate_transfer_function` / manuelle formler | Kontrollerer evt. magnitude | Vælg `alpha`, `tau_d`, centerfrekvens | Designvalg eller plotaflæsning er opgaven | Ingen ny funktion nødvendig |

## Dækket af Python

- Pol-/gain-/DC-kontrol og symbolske stabile gain-intervaller efter at den matematiske model er opstillet.
- Simple phase-margin- og andenordensberegninger fra numeriske input.
- De gentagne designrelationer for PI-Lead og P-Lead-Lag.
- Nominal properness/stability-check af en udledt disturbance feed-forward ratio.

## Delvist dækket af Python

- F21 Q3-Q6, Q10-Q11 og Q14-Q16; S20 Q5,Q10-Q11,Q14,Q16; 2022 Q6-Q9,Q11,Q13,Q16-Q19; E23 Q7,Q18-Q20; F25 Q1,Q3,Q6,Q8,Q14-Q17,Q20: beregninger kan kontrolleres, men plot, loop eller metodevalg skal aflæses manuelt.
- F21 Q20 og 2022 Q18: ratio/properness kan kontrolleres, men disturbancefortegn, filtervalg og modelgyldighed er brugerens ansvar.

## Ikke dækket af Python

- S20 Q1-Q4,Q6-Q9,Q12-Q13,Q15,Q17-Q19; F21 Q1-Q2,Q5,Q7,Q13,Q15 og den faglige del af Q19; 2022 Q1,Q4-Q5,Q10,Q12,Q14-Q15,Q18,Q20; E23 Q1-Q6,Q8-Q17; samt figurbaserede F25-delopgaver: diagram-/koncept-/Bode-/Nyquistfortolkning.
- Rate limitation, saturation, windup mitigation, prefilterstruktur og feed-forward-valg ud fra fysisk risiko.

## Hvorfor ikke alt automatiseres

Kilderne indeholder mange figurer uden strukturerede data, og flere opgaver tester netop valg af signalvej, fortegn og gyldighedsbetingelser. Automatisk svarvalg ville skjule den faglige vurdering og være mindre sikkert end den korte manuelle opskrift.

## Minimum manuel kunnen, selv med scripts

- Reducere feedbackblokdiagrammer og afgøre disturbance-/sensorfortegn.
- Læse Bode- og Nyquist-plots, herunder RHP/LHP-fase og encirclement.
- Kontrollere final-value- og linearitetsantagelser.
- Vælge controllerstruktur, crossover og mitigation ved actuatorgrænser.
