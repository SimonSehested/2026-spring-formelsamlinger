# Exam Task Taxonomy

| Task Type | Keywords / Danish Aliases | Sources | Support Mode | Fast Method | Python Support | Traps |
|---|---|---|---|---|---|---|
| LTIC classification | systemklassifikation, lineært, tidsinvariant, kausal | 2023 Q1, 2024 Q1, 2025 Q2 | notes_only | Check superposition, constant coefficients, no future input | Rejected as conceptual | Time-varying coefficient vs time-varying signal |
| Circuit equation recognition | knudepunkt, kredsløb, differentialligning | 2023 Q2, 2024 Q2/Q7/Q10, 2025 Q1/Q9 | notes_only | KCL with \(i_R,i_C,v_L\), then DC/HF checks | Rejected natural-language/circuit parsing | Sign convention and capacitor current direction |
| Impulse/step/ramp response | impulsrespons, steprespons, ramperespons | 2023 Q3/Q4/Q13/Q15, 2024 Q3/Q4/Q16, 2025 Q3/Q4/Q14 | script_assisted | Convert \(H(s)\), use inverse Laplace and response relations | `scripts/lti/responses.py` | Improper \(H(s)\) can contain impulse terms |
| Convolution | foldning, convolution, tabelopslag | 2023 Q5, 2024 Q5, 2025 Q5 | script_primary | Laplace product for causal signals or support interval rule | `scripts/transforms/convolution.py::convolve_causal` | Support interval vs explicit convolution are different questions |
| Fourier series | Fourierrække, orthogonale basisfunktioner | 2023 Q7, 2024 Q8, 2025 Q6 | script_assisted | Use \(D_n\) formula and symmetry rules | `scripts/fourier/series.py::complex_fourier_coefficients` | A finite aperiodic segment reconstructs periodically |
| Fourier transform properties | Fourier-transformation, skalering, modulation | 2023 Q8-Q10, 2024 Q9/Q12, 2025 Q7/Q8 | script_assisted | Apply definition and property table | `scripts/fourier/properties.py::exponential_transform_variant` | Scaling uses \(1/|a|\) and \(X(\omega/a)\) |
| Laplace transform concepts | unilateral, konvergensområde, partialbrøk | 2023 Q11-Q14, 2024 Q13-Q15, 2025 Q11-Q14 | script_assisted | Use unilateral derivative rules, partial fractions, value theorems | `scripts/transforms/laplace.py`, `scripts/lti/responses.py` | Final value theorem needs stable poles of \(sY(s)\) |
| Second-order classification | anden orden, dæmpningsfaktor, Q, poler | 2023 Q11/Q12/Q15, 2024 Q6/Q16, 2025 Q2/Q15/Q16 | script_primary | Extract \(a_1,a_0\), compute \(\zeta,\omega_n,Q\), roots | `scripts/lti/second_order.py` | Positive real poles are unstable |
| Bode/filter matching | Bodeplot, frekvenskarakteristik, pol-nulpunkt | 2023 Q16/Q17, 2024 Q11/Q19, 2025 Q10/Q17 | script_assisted | Read slopes, phase, breaks; check sample values numerically | `scripts/frequency/bode.py` | \(H(\omega)\) should be \(H(j\omega)\) in calculations |
| Butterworth design | Butterworth, Sallen-Key, filterdesign | 2023 Q18/Q20, 2024 Q17/Q18, 2025 Q18 | script_assisted | Use magnitude formula, order inequality, pole/Q table, RC scaling | `scripts/filters/butterworth.py` | Butterworth is magnitude-flat, not phase preserving |
| ADC and sampling | sampling, aliasering, ADC, LSB | 2024 Q20, 2025 Q20, L06-L07 | script_primary | Fold tones; compute LSB; size anti-alias sampling rate | `scripts/sampling/adc.py` | Down-rounding quantization error is biased |
| Instrumentation amplifier | instrumenteringsforstærker, common mode, CMRR | 2025 Q19, L13 | script_assisted | Apply \(G_d,G_c,CMRR\) formulas | `scripts/circuits/instrumentation.py` | Input buffer stage is non-inverting in the exam model |

## Rejected or Notes-Only Candidates

- Full circuit-to-equation parser: rejected_unclear_input. Circuit diagrams are images and require interpretation.
- MCQ truth-table solver: rejected_high_risk. The decisive work is reading and judging mixed true/false statements.
- Automatic graphical plot matcher from PDF screenshots: rejected_high_risk and rejected_unverifiable.
- Natural-language transform pair checker: rejected_unclear_input. Property-specific helpers are safer.
