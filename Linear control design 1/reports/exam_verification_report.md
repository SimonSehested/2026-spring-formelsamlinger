# Exam verification report: F21 and F25

## Mapping af alle eksamensopgaver

| Eksamenssæt/opgave | Opgavetype | Notesektion | Metode dækket? | Formler dækket? | Symboler forklaret? | Hurtigtjek/fælde? | Pythonstatus | Mangler? |
| ------------------ | ---------- | ----------- | -------------- | --------------- | ------------------- | ----------------- | ------------ | -------- |
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
| F21 Q17 | P-Lead-Lag | P-Lead-Lag og limits | Ja | Ja | Ja | Ja | `solve_lag_beta` | Plantfase/phasebalance manuel |
| F21 Q18 | PI-Lead | PI-Lead design | Ja | Ja | Ja | Ja | `design_pi_lead_at_crossover` | Kildeafvigelse dokumenteret |
| F21 Q19 | Cascaded DC-fejl | Blokdiagram; Stationær fejl | Ja | Ja | Ja | Ja | `script_assisted` | Diagram/DC plot manuelt |
| F21 Q20 | Feed-forward | Dynamisk feed-forward | Ja | Ja | Ja | Ja | `ideal_disturbance_feedforward` | Fortegn manuelt |
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
| Model/TF/poler | Ja | Dækket |
| Tidsrespons/overshoot | Ja | Dækket |
| Bode/P-gain/margin | Ja | Dækket |
| Nyquist/stabilisering og punktmargin | Ja | Dækket |
| Blokdiagram/stationær fejl | Ja | Dækket |
| PI-Lead/P-design | Ja | Dækket |
| Lag/limited systems | Ja | Dækket |
| Disturbance/sensitivity/prefilter | Ja | Dækket |
| Feed-forward | Ja | Dækket |
| Initial/final value | Ja | Dækket |
| Ziegler--Nichols PID | Ja | Dækket |
| Reference feed-forward med proper invers | Ja | Dækket |

## Kendte rester

- Ingen F21- eller F25-opgave er sprunget over.
- Visuelt aflæste oplysninger er bevidst ikke automatiseret; dette er en begrænsning i scriptdækning, ikke i notesektionen.
