# Script Inventory

| Function or Candidate | Category | Source Task Types | Status | Validation | Notes Reference | Risk | Reason |
|---|---|---|---|---|---|---|---|
| `scripts/lti/second_order.py::classify_second_order` | diagnostic_helper | 2nd-order poles, damping, stability | validated | `python scripts/validate_scripts.py` | `sources/01_ltic_time_domain.tex` | low | Recurs across exams |
| `scripts/lti/second_order.py::step_features_from_zeta_wn` | numeric_helper | step-response features | validated | same | `sources/01_ltic_time_domain.tex` | low | Standard formulas |
| `scripts/lti/second_order.py::estimate_from_overshoot_peak_time` | primary_solver | infer \(\zeta,\omega_n,t_s\) from plot | validated | same | `sources/01_ltic_time_domain.tex` | low | Repeated plot-reading task |
| `scripts/lti/responses.py::impulse_response_from_transfer` | symbolic_helper | impulse response from \(H(s)\) | validated | same | `sources/01_ltic_time_domain.tex` | medium | Symbolic output still needs MCQ interpretation |
| `scripts/lti/responses.py::step_response_from_transfer` | symbolic_helper | step response from \(H(s)\) | validated | same | `sources/01_ltic_time_domain.tex` | medium | Assumes zero-state response |
| `scripts/lti/responses.py::ramp_response_from_transfer` | symbolic_helper | ramp response from \(H(s)\) | validated | same | `sources/01_ltic_time_domain.tex` | medium | Assumes zero-state response |
| `scripts/lti/responses.py::related_unit_responses` | conversion_helper | convert between impulse/step/ramp responses | validated | same | `sources/01_ltic_time_domain.tex` | medium | Assumes causal zero-state LTIC response |
| `scripts/lti/responses.py::zero_input_laplace_second_order` | symbolic_helper | zero-input Laplace expression | validated | same | `sources/03_laplace.tex` | low | Formulaic and recurring |
| `scripts/lti/responses.py::transfer_from_ode` | conversion_helper | ODE to transfer function/poles | validated | same | script index | low | Useful check from differential equations |
| `scripts/transforms/convolution.py::convolve_causal` | primary_solver | causal exponential convolution | validated | same | `sources/01_ltic_time_domain.tex` | low | Directly matches exam convolution tasks |
| `scripts/transforms/laplace.py::inverse_laplace_rational` | symbolic_helper | inverse Laplace partial fraction check | validated | same | `sources/03_laplace.tex` | medium | Must supply coefficients correctly |
| `scripts/expand.py::expand_expr` | symbolic_helper | match algebraically equivalent answer forms | validated | same | `exam_toolbox.py` | low | Useful for comparing MCQ expressions |
| `scripts/expand.py::same_after_expand` | diagnostic_helper | check whether two symbolic answer forms match | validated | same | `exam_toolbox.py` | low | Prevents algebraic-form traps |
| `scripts/fourier/series.py::complex_fourier_coefficients` | symbolic_helper | Fourier series coefficients | validated | same | `sources/02_fourier.tex` | low | Stable integral formula |
| `scripts/fourier/properties.py::exponential_transform_variant` | conversion_helper | transform property MCQs | validated | same | `sources/02_fourier.tex` | medium | Limited to positive time scaling |
| `scripts/frequency/bode.py::bode_values` | numeric_helper | Bode numeric checks | validated | same | `sources/04_frequency_bode_filters.tex` | low | Direct evaluation |
| `scripts/frequency/bode.py::classify_filter_limits` | diagnostic_helper | filter type by limits | validated | same | `sources/04_frequency_bode_filters.tex` | medium | Not enough for all-pass/notch alone |
| `scripts/frequency/bode.py::transfer_from_poles_zeros` | conversion_helper | pole-zero to transfer function | validated | same | `sources/04_frequency_bode_filters.tex` | low | Useful for plot matching |
| `scripts/filters/butterworth.py::butterworth_lowpass_order` | primary_solver | Butterworth order | validated | same | `sources/04_frequency_bode_filters.tex` | low | Standard design inequality |
| `scripts/filters/butterworth.py::butterworth_highpass_order` | primary_solver | high-pass Butterworth order | validated | same | script index | low | Low-pass transform |
| `scripts/filters/butterworth.py::butterworth_poles_q` | numeric_helper | Butterworth poles and Q values | validated | same | `sources/04_frequency_bode_filters.tex` | low | Repeated stage design |
| `scripts/filters/butterworth.py::frequency_scale_rc` | conversion_helper | RC frequency scaling | validated | same | `sources/04_frequency_bode_filters.tex` | low | Common design trap |
| `scripts/sampling/adc.py::adc_lsb` | numeric_helper | ADC resolution | validated | same | `sources/05_sampling_adc_inamp.tex` | low | Formulaic |
| `scripts/sampling/adc.py::alias_frequency` | primary_solver | alias folding | validated | same | `sources/05_sampling_adc_inamp.tex` | low | Recurring tone alias task |
| `scripts/sampling/adc.py::required_sampling_rate_for_lsb` | primary_solver | anti-alias rate vs LSB | validated | same | `sources/05_sampling_adc_inamp.tex` | low | Matches 2024/2025 ADC tasks |
| `scripts/circuits/instrumentation.py::instrumentation_gains` | numeric_helper | in-amp gain/CMRR | validated | same | `sources/05_sampling_adc_inamp.tex` | low | Formula supplied in exam |
| `scripts/circuits/node_equations.py::solve_node_circuit` | symbolic_helper | node-equation circuits to transfer function/differential equation | validated | same | `exam_toolbox.py` | medium | Requires user to write correct KCL equations |
| Full circuit parser | rejected_unclear_input | circuit diagrams | rejected | not run | none | high | Image interpretation and topology extraction are too fragile |
| MCQ answer selector | rejected_high_risk | all exams | rejected | not run | none | high | Encourages blind use and cannot handle mixed statements reliably |
| Screenshot plot matcher | rejected_unverifiable | graphical Bode/pole/step tasks | rejected | not run | none | high | No robust image extraction pipeline in repo |
