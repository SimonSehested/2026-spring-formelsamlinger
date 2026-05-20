# Exam Verification Report

## Exam-to-Task Mapping

| Source | Problems | Problem Type | Support Mode | Covered in Notes | Python Function | Script Validated? | Missing? | Risk |
|---|---|---|---|---|---|---|---|---|
| 2023 trial | Q1 | LTIC classification | notes_only | LTIC systems | none | n/a | no | low |
| 2023 trial | Q2 | circuit differential equation | notes_only | Circuit equations | rejected parser | n/a | no | medium |
| 2023 trial | Q3 | impulse response from ODE | script_assisted | Impulse/step/ramp | `impulse_response_from_transfer` | yes | no | medium |
| 2023 trial | Q4 | step to impulse/ramp relation | script_assisted | Impulse/step/ramp | `step_response_from_transfer` | yes | no | low |
| 2023 trial | Q5 | convolution of causal exponentials | script_primary | Convolution | `convolve_causal` | yes | no | low |
| 2023 trial | Q6 | second-order system characteristics | script_assisted | Second-order standard form | `classify_second_order` | yes | no | low |
| 2023 trial | Q7 | Fourier series concepts | script_assisted | Fourier series | `complex_fourier_coefficients` | yes | no | low |
| 2023 trial | Q8-Q10 | Fourier transform/property/plot reasoning | script_assisted | Fourier transform | `exponential_transform_variant` | yes | no | medium |
| 2023 trial | Q11-Q14 | unilateral Laplace, ROC, zero-input | script_assisted | Laplace transform | `zero_input_laplace_second_order`, `inverse_laplace_rational` | yes | no | low |
| 2023 trial | Q15 | second-order step features | script_primary | Second-order step features | `step_features_from_zeta_wn` | yes | no | low |
| 2023 trial | Q16-Q17 | system relation and Bode matching | script_assisted | Frequency response/Bode | `bode_values`, `transfer_from_poles_zeros` | yes | no | medium |
| 2023 trial | Q18 | filter concepts | notes_only | Butterworth filters | none | n/a | no | low |
| 2023 trial | Q19 | sensitivity | notes_only | Sallen-Key sensitivity | none | n/a | no | medium |
| 2023 trial | Q20 | Sallen-Key high-pass design | script_assisted | Butterworth/Sallen-Key | `frequency_scale_rc`, `butterworth_highpass_order` | yes | no | medium |
| August 2024 | Q1 | classification/stability | script_assisted | LTIC, second order | `classify_second_order` | yes | no | low |
| August 2024 | Q2 | node equations | notes_only | Circuit equations | none | n/a | no | medium |
| August 2024 | Q3 | impulse response | script_assisted | Impulse response | `impulse_response_from_transfer` | yes | no | medium |
| August 2024 | Q4 | impulse/ramp from step | script_assisted | Response relations | `step_response_from_transfer` | yes | no | low |
| August 2024 | Q5 | convolution | script_primary | Convolution | `convolve_causal` | yes | no | low |
| August 2024 | Q6-Q7 | system characteristic and circuit response | script_assisted | Second order, circuit rules | `classify_second_order` | yes | no | medium |
| August 2024 | Q8-Q12 | Fourier series/transform/symmetry | script_assisted | Fourier | `complex_fourier_coefficients`, `exponential_transform_variant` | yes | no | medium |
| August 2024 | Q13-Q15 | Laplace and inverse Laplace | script_assisted | Laplace | `inverse_laplace_rational`, `zero_input_laplace_second_order` | yes | no | low |
| August 2024 | Q16 | overshoot/peak-time identification | script_primary | Step features | `estimate_from_overshoot_peak_time` | yes | no | low |
| August 2024 | Q17-Q19 | filters and Bode | script_assisted | Frequency/Bode/Butterworth | `bode_values`, `butterworth_poles_q` | yes | no | medium |
| August 2024 | Q20 | ADC and aliasing | script_primary | Sampling/ADC | `adc_lsb`, `alias_frequency`, `required_sampling_rate_for_lsb` | yes | no | low |
| May 2025 | Q1 | circuit diagram information | notes_only | Circuit equations | none | n/a | no | medium |
| May 2025 | Q2 | ODE coefficients and system properties | script_assisted | Second order | `classify_second_order`, `step_features_from_zeta_wn` | yes | no | low |
| May 2025 | Q3-Q4 | impulse and step response | script_assisted | Response relations | `impulse_response_from_transfer`, `step_response_from_transfer` | yes | no | low |
| May 2025 | Q5 | convolution support/concepts | notes_only | Convolution | `convolve_causal` if explicit expression | yes | no | low |
| May 2025 | Q6-Q8 | Fourier series/transform | script_assisted | Fourier | `complex_fourier_coefficients`, `exponential_transform_variant` | yes | no | medium |
| May 2025 | Q9-Q10 | AC circuit and frequency response | script_assisted | Circuit equations, frequency response | `bode_values` | yes | no | medium |
| May 2025 | Q11-Q14 | Laplace transform and response | script_assisted | Laplace | `inverse_laplace_rational`, `zero_input_laplace_second_order` | yes | no | low |
| May 2025 | Q15-Q18 | filters, system identification, Butterworth | script_assisted | Frequency/Bode/Butterworth | `classify_second_order`, `estimate_from_overshoot_peak_time`, `butterworth_poles_q` | yes | no | medium |
| May 2025 | Q19 | instrumentation amplifier | script_assisted | Instrumentation amplifier | `instrumentation_gains` | yes | no | low |
| May 2025 | Q20 | sampling and ADC | script_primary | Sampling/ADC | `alias_frequency`, `adc_lsb`, `required_sampling_rate_for_lsb` | yes | no | low |

## Verification Summary

Every recurring exam task type has a searchable note section. Every script-assisted or script-primary task has at least one note reference to a validated function. Remaining medium risks are interpretation risks from image-based circuits and graphical MCQ matching, not missing formulas or broken scripts.

## Full Audit Update

`reports/full_input_coverage_audit.md` was added as a stricter problem-by-problem and lecture-by-lecture audit against all PDFs in `input/`.

The audit found weak coverage for a few compact MCQ traps and the notes were updated:

- 2023 Q19: added sensitivity formulas for underdamped pole coordinates.
- 2023 Q20 / 2024 Q18 / 2025 Q18: clarified lowpass vs highpass Sallen-Key component matching for low \(Q\)-sensitivity.
- 2025 Q17: added pole-zero phase trap for mirrored left/right half-plane zeros.
- 2025 Q18: added Butterworth \(H(s)H(-s)\) causal/anti-causal clarification.

After these changes, the remaining non-low risks are visual interpretation risks, not known missing formulas.
