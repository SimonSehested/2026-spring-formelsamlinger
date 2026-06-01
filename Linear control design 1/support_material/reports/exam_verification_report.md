# Exam verification report: S20, F21, 2022, E23 and F25

## Mapping af alle eksamensopgaver

| Eksamenssæt/opgave | Opgavetype | Notesektion | Metode dækket? | Formler dækket? | Symboler forklaret? | Hurtigtjek/fælde? | Pythonstatus | Mangler? |
| ------------------ | ---------- | ----------- | -------------- | --------------- | ------------------- | ----------------- | ------------ | -------- |
| S20 Q1 | Stationær integrator/DC-model | ODE/fysisk model; Blokdiagram | Ja | Ja | Ja | Ja | `notes_only` | Figurparametre aflæses manuelt |
| S20 Q2 | Linearisering/førsteorden | ODE/fysisk model | Ja | Ja | Ja | Ja | `notes_only` | Driftspunkt fra figur/tekst |
| S20 Q3 | Blokdiagram med parallelgren | Blokdiagramreduktion | Ja | Ja | Ja | Ja | `notes_only` | Figurfortegn manuelt |
| S20 Q4 | Initial/final value fra stepplot | ODE/fysisk model; Steprespons | Ja | Ja | Ja | Ja | `notes_only` | Plotaflæsning |
| S20 Q5 | Overshoot til dæmpning | Steprespons | Ja | Ja | Ja | Ja | `second_order_characteristics` | Inversion kan gøres manuelt |
| S20 Q6 | Bode poler/zeros | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Plotaflæsning |
| S20 Q7 | Bandwidth fra -3 dB | Steprespons; Bode-plot | Ja | Ja | Ja | Ja | `notes_only` | Plotaflæsning |
| S20 Q8 | Steprespons til Bode | Steprespons; Bode-plot | Ja | Ja | Ja | Ja | `notes_only` | Valg mellem figurer |
| S20 Q9 | P-gain for PM | P-gain fra margin | Ja | Ja | Ja | Ja | `notes_only` | Bodeaflæsning |
| S20 Q10 | Lead zero-frekvens | PI-Lead design | Ja | Ja | Ja | Ja | `script_assisted` | Simpel formel, ingen ny funktion |
| S20 Q11 | P-Lead Kp | PI-Lead design; P-gain fra margin | Ja | Ja | Ja | Ja | `evaluate_transfer_function` | Plot/plant manuelt |
| S20 Q12 | Stabilitet efter P-Lead | Bode-plot; Nyquist-stabilitet | Ja | Ja | Ja | Ja | `notes_only` | Nyquist/peak manuelt |
| S20 Q13 | Kompleks polpar fra peak | Bode-plot; Steprespons | Ja | Ja | Ja | Ja | `notes_only` | Plotaflæsning |
| S20 Q14 | PI-Lead Kp | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Crossover/plot manuelt |
| S20 Q15 | Lead forward/back branch | Disturbance/sensitivity; PI-Lead design | Ja | Ja | Ja | Ja | `notes_only` | Konceptuel responsfortolkning |
| S20 Q16 | RHP-pol fra nævner | ODE/fysisk model | Ja | Ja | Ja | Ja | `transfer_function_poles` | Ingen |
| S20 Q17 | Nyquist for RHP-plant | Nyquist-stabilitet; P-Lead-Lag | Ja | Ja | Ja | Ja | `notes_only` | Kurveretning manuelt |
| S20 Q18 | Reduceret Kp og Nyquist | Nyquist-stabilitet; P-Lead-Lag | Ja | Ja | Ja | Ja | `notes_only` | Kurveskalering manuelt |
| S20 Q19 | Disturbance sensitivitykurver | Disturbance og sensitivity | Ja | Ja | Ja | Ja | `notes_only` | Kurver A/B/C aflæses manuelt |
| F21 Q1 | Blokdiagram | Blokdiagramreduktion | Ja | Ja | Ja | Ja | `notes_only` | Figur aflæses manuelt |
| F21 Q2 | RLC-blokdiagram | ODE/fysisk model; Blokdiagram | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| F21 Q3 | Pol/zero til Bode | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `script_assisted` | Plot manuelt |
| F21 Q4 | Kritisk P-gain | Bode-plot; P-gain fra margin | Ja | Ja | Ja | Ja | `closed_loop_poles` | Ingen |
| F21 Q5 | Bode til singulariteter | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| F21 Q6 | Gain for PM | P-gain fra margin | Ja | Ja | Ja | Ja | `evaluate_transfer_function` | Plotværdi manuelt |
| F21 Q7 | Masse/fjeder TF | ODE/fysisk model | Ja | Ja | Ja | Ja | `notes_only` | Figur/udledning manuel |
| F21 Q8 | ODE-poler | ODE/fysisk model | Ja | Ja | Ja | Ja | `transfer_function_poles` | Ingen |
| F21 Q9 | Overshoot/gain | Steprespons | Ja | Ja | Ja | Ja | `second_order_characteristics` | Afrunding dokumenteret |
| F21 Q10 | Bode til steprespons | Bode; Steprespons | Ja | Ja | Ja | Ja | `script_assisted` | Plot manuelt |
| F21 Q11 | Stabil gain | Bode/P-gain | Ja | Ja | Ja | Ja | `closed_loop_poles` | Ingen |
| F21 Q12 | Højordens ODE | ODE/fysisk model | Ja | Ja | Ja | Ja | `transfer_function_poles` | Ingen |
| F21 Q13 | Ustabil Nyquist | Nyquist-stabilitet | Ja | Ja | Ja | Ja | `notes_only` | Direction manuelt |
| F21 Q14 | PM fra Nyquistpunkt | Phase margin fra punkt | Ja | Ja | Ja | Ja | `phase_margin_from_point` | Punkt manuelt |
| F21 Q15 | P-gain koncept | Bode/P-gain; Stationær fejl | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| F21 Q16 | Stationær fejl | Stationær referencefejl | Ja | Ja | Ja | Ja | `unity_feedback_step_error` | Diagramcheck manuelt |
| F21 Q17 | P-Lead-Lag | P-Lead-Lag og limits | Ja | Ja | Ja | Ja | `solve_lag_beta` | Plantfase manuel |
| F21 Q18 | PI-Lead | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Kildeafvigelse dokumenteret |
| F21 Q19 | Cascaded DC-fejl | Blokdiagram; Stationær fejl | Ja | Ja | Ja | Ja | `script_assisted` | Diagram/DC plot manuelt |
| F21 Q20 | Feed-forward | Dynamisk feed-forward | Ja | Ja | Ja | Ja | `ideal_disturbance_feedforward` | Fortegn manuelt |
| 2022 Q1 | Ukendt/manglende tekst | Ikke dækket specifikt | Nej | Nej | Nej | Ja | `notes_only` | Q1 skal visuelt kontrolleres i original PDF |
| 2022 Q2 | RC førsteorden | Steprespons | Ja | Ja | Ja | Ja | `notes_only` | Ingen facit i kilde |
| 2022 Q3 | Udæmpet andenorden | Steprespons | Ja | Ja | Ja | Ja | `notes_only` | Ingen facit i kilde |
| 2022 Q4 | RHP-zero/Bode | Bode-plot | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| 2022 Q5 | Bode singulariteter | Bode-plot | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| 2022 Q6 | K for PM | P-gain fra margin | Ja | Ja | Ja | Ja | `evaluate_transfer_function` | Ingen facit i kilde |
| 2022 Q7 | DC gain i dB | ODE/fysisk model; Bode | Ja | Ja | Ja | Ja | `evaluate_transfer_function` | Ingen facit i kilde |
| 2022 Q8 | ODE-poler | ODE/fysisk model | Ja | Ja | Ja | Ja | `transfer_function_poles` | Ingen facit i kilde |
| 2022 Q9 | Parameterstabilitet | ODE/fysisk model | Ja | Ja | Ja | Ja | `script_assisted` | Ingen facit i kilde |
| 2022 Q10 | Ukendt/manglende tekst | Ikke dækket specifikt | Nej | Nej | Nej | Ja | `notes_only` | Q10 skal visuelt kontrolleres i original PDF |
| 2022 Q11 | Gain margin fra Nyquist | Bode/Nyquist margin | Ja | Ja | Ja | Ja | `script_assisted` | Ingen facit i kilde |
| 2022 Q12 | RHP Nyquist Kp | Nyquist-stabilitet | Ja | Ja | Ja | Ja | `notes_only` | Ingen facit i kilde |
| 2022 Q13 | Lead magnitude | PI-Lead design | Ja | Ja | Ja | Ja | `script_assisted` | Ingen facit i kilde |
| 2022 Q14 | Error response fra Bode | Steprespons; Stationær fejl | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| 2022 Q15 | P-gain koncept/to crossovers | Bode; Stationær fejl | Ja | Ja | Ja | Ja | `notes_only` | Ingen facit i kilde |
| 2022 Q16 | Kp fra `e_ss` | Stationær referencefejl | Ja | Ja | Ja | Ja | `unity_feedback_step_error` | DC-gain aflæses manuelt |
| 2022 Q17 | PI-Lead alpha | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Plantfase aflæses manuelt |
| 2022 Q18 | Proper feed-forward | Dynamisk feed-forward | Ja | Ja | Ja | Ja | `notes_only` | Filterorden/fortegn fra figur |
| 2022 Q19 | PI-Lead Kp | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Crossover skal findes |
| 2022 Q20 | Designkoncept | PI-Lead design; Bode | Ja | Ja | Ja | Ja | `notes_only` | Ingen facit i kilde |
| E23 Q1 | Open-loop transfer | Blokdiagramreduktion | Ja | Ja | Ja | Ja | `notes_only` | Figur manuelt |
| E23 Q2 | Closed-loop transfer | Blokdiagramreduktion | Ja | Ja | Ja | Ja | `notes_only` | Figur manuelt |
| E23 Q3 | Type/order | Blokdiagram; Stationær fejl | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| E23 Q4 | Static loopgain | Stationær referencefejl | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| E23 Q5 | PI-controller | PI-Lead design; Stationær fejl | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| E23 Q6 | State-space type/order | ODE/fysisk model | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| E23 Q7 | State-space TF | ODE/fysisk model | Ja | Ja | Ja | Ja | `transfer_function_poles` | Ingen |
| E23 Q8 | Bode poler/zero | Bode-plot | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q9 | Static gain fra Bode | Stationær referencefejl; Bode | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q10 | PM/GM | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q11 | `omega_c`, `omega_pi` | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q12 | Type-1 steptracking | Stationær referencefejl | Ja | Ja | Ja | Ja | `notes_only` | Stabilitet antaget |
| E23 Q13 | Kp for PM 90 | P-gain fra margin | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q14 | P-Lead crossover | PI-Lead design | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| E23 Q15 | Lead purpose | PI-Lead design | Ja | Ja | Ja | Ja | `notes_only` | Konceptuel |
| E23 Q16 | Step fra Bode | Steprespons; Bode | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| E23 Q17 | Damped eigenfrequency | Steprespons | Ja | Ja | Ja | Ja | `notes_only` | Plotperiode aflæses |
| E23 Q18 | Reference step error | Stationær referencefejl | Ja | Ja | Ja | Ja | `unity_feedback_step_error` | Diagramgain `a` |
| E23 Q19 | Disturbance output DC | Disturbance/sensitivity | Ja | Ja | Ja | Ja | `script_assisted` | Diagramfortegn manuelt |
| E23 Q20 | Disturbance error til `a` | Disturbance/sensitivity | Ja | Ja | Ja | Ja | `script_assisted` | Diagramfortegn manuelt |
| F25 Q1 | Initial/final value | Model/tidsrespons; blokdiagram | Ja | Ja | Ja | Ja | `script_assisted` | Diagram manuelt |
| F25 Q2 | TF til blokdiagram | Blokdiagramreduktion | Ja | Ja | Ja | Ja | `notes_only` | Figuralternativer manuelle |
| F25 Q3 | Parameterstabilitet | ODE/fysisk model | Ja | Ja | Ja | Ja | `find_stable_gain_ranges` | Simpel koefficienttest nok |
| F25 Q4 | System type | Stationær referencefejl | Ja | Ja | Ja | Ja | `notes_only` | Ramp/parabel kræver constants |
| F25 Q5 | Bode singulariteter | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| F25 Q6 | 1%-settling | Steprespons | Ja | Ja | Ja | Ja | `script_assisted` | Dominant pol vælges manuelt |
| F25 Q7 | Linearisering | ODE/fysisk model | Ja | Ja | Ja | Ja | `notes_only` | Arbejdspunkt manuelt |
| F25 Q8 | Ziegler-Nichols PID | Ziegler--Nichols PID | Ja | Ja | Ja | Ja | `script_assisted` | Ingen dedikeret script |
| F25 Q9 | GM efter gainjustering | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Konceptuel marginændring |
| F25 Q10 | Bodekoncept | Bode-plot og P-gain | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| F25 Q11 | P-gain for PM | P-gain fra margin | Ja | Ja | Ja | Ja | `notes_only` | Plot manuelt |
| F25 Q12 | Limited identification | P-Lead-Lag og limits | Ja | Ja | Ja | Ja | `notes_only` | Konceptuel |
| F25 Q13 | Nyquist RHP | Nyquist-stabilitet | Ja | Ja | Ja | Ja | `notes_only` | Direction manuelt |
| F25 Q14 | Stepfejl til gain | Stationær referencefejl | Ja | Ja | Ja | Ja | `unity_feedback_step_error` | DC gain fra Bode manuelt |
| F25 Q15 | Low-pass serie DC | Blokdiagram; Stationær fejl | Ja | Ja | Ja | Ja | `script_assisted` | DC gain fra figur manuelt |
| F25 Q16 | PI-Lead gain | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Crossover/plotdata manuelt |
| F25 Q17 | Lag beta | P-Lead-Lag og limits | Ja | Ja | Ja | Ja | `solve_lag_beta` | Plantfase manuelt |
| F25 Q18 | Koncept | Stationær fejl; Bode; Nyquist | Ja | Ja | Ja | Ja | `notes_only` | Ingen |
| F25 Q19 | Tracking feed-forward | Reference feed-forward | Ja | Ja | Ja | Ja | `notes_only` | Properness manuelt |
| F25 Q20 | Closed-loop stepplot | ODE/fysisk model; Steprespons | Ja | Ja | Ja | Ja | `script_assisted` | Plotvalg manuelt |

## Kontrol mod prioriterede opgavetyper

| Prioriteret type | Notesektion har Brug når/Input/Metode/Formler/Symboler/Antagelser/Hurtigtjek/Fælder? | Status |
| ---------------- | ------------------------------------------------------------------------------------ | ------ |
| Model/TF/poler/state-space | Ja | Dækket |
| Første-/andenordensrespons, bandwidth og dæmpet frekvens | Ja | Dækket |
| Bode/P-gain/margin og dB-konvertering | Ja | Dækket |
| Nyquist for RHP-planter og gain-skalering | Ja | Dækket |
| Blokdiagram, systemtype og static loopgain | Ja | Dækket |
| Stationær reference- og disturbancefejl | Ja | Dækket |
| P-Lead, PI-Lead og Lead zero/pole/magnitude | Ja | Dækket |
| Lag/limited systems | Ja | Dækket |
| Disturbance/sensitivity/prefilter | Ja | Dækket |
| Feed-forward og proper invers/lavpasfilter | Ja | Dækket |
| Ziegler--Nichols PID | Ja | Dækket |

## Kendte rester

- S20 Q1-Q19, F21 Q1-Q20, E23 Q1-Q20 og F25 Q1-Q20 er mappet.
- 2022 Q2-Q9 og Q11-Q20 er mappet. 2022 Q1 og Q10 er ikke brugbart tekstudtrukket og kræver visuel kontrol i original PDF; dette er markeret som kildebegrænsning.
- Visuelt aflæste oplysninger er bevidst ikke automatiseret; dette er en begrænsning i scriptdækning, ikke i notesektionen.
