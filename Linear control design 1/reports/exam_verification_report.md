# Exam verification report: F21

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

## Kendte rester

- Ingen F21-opgave er sprunget over.
- Visuelt aflæste oplysninger er bevidst ikke automatiseret; dette er en begrænsning i scriptdækning, ikke i notesektionen.
