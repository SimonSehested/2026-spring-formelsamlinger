# Script Validation Report

| Function | File | Category | Validation Command | Test Input | Expected/Plausible Output | Result | Limitations |
|---|---|---|---|---|---|---|---|
| `classify_second_order` | `scripts/lti/second_order.py` | diagnostic_helper | `python scripts/validate_scripts.py` | \(a_1=2,a_0=17\) | stable underdamped, \(\omega_n=\sqrt{17}\) | validated | Standard denominator only |
| `step_features_from_zeta_wn` | same | numeric_helper | same | \(\zeta=0.5,\omega_n=4\) | \(PO\approx16.3\%\) | validated | Underdamped only |
| `estimate_from_overshoot_peak_time` | same | primary_solver | same | \(PO=45.59,t_p=0.78543\) | \(\omega_n\approx4.1231,t_s\approx4\) | validated | Requires reliable plot readings |
| `impulse_response_from_transfer` | `scripts/lti/responses.py` | symbolic_helper | same | num `[32,0]`, den `[1,8,16]` | \(32(1-4t)e^{-4t}u(t)\) | validated | Symbolic simplification may vary |
| `step_response_from_transfer` | same | symbolic_helper | same | num `[1]`, den `[1,2,1]` | \((1-(1+t)e^{-t})u(t)\) | validated | Zero-state response |
| `zero_input_laplace_second_order` | same | symbolic_helper | same | \(a_1=2,a_0=17,y_0=2,\dot y_0=4\) | \((2s+8)/(s^2+2s+17)\) | validated | Second order only |
| `transfer_from_ode` | same | conversion_helper | same | num `[1]`, den `[1,2,17]` | symbolic \(H(s)\), two poles | validated | Coefficients must be descending |
| `convolve_causal` | `scripts/transforms/convolution.py` | primary_solver | same | \(2e^{-2t}\), \(te^{-3t}\) | \(2e^{-2t}-2te^{-3t}-2e^{-3t}\) times \(u(t)\) | validated | Causal signals only |
| `inverse_laplace_rational` | `scripts/transforms/laplace.py` | symbolic_helper | same | `[1]`, `[1,1]` | \(e^{-t}u(t)\) | validated | Rational expressions only |
| `expand_expr` | `scripts/expand.py` | symbolic_helper | same | equivalent exponential forms | simplified expanded expression | validated | Symbolic simplification may vary |
| `same_after_expand` | `scripts/expand.py` | diagnostic_helper | same | \(e^t e^{-t}\) and 1 | `True` | validated | Symbolic equivalence check only |
| `complex_fourier_coefficients` | `scripts/fourier/series.py` | symbolic_helper | same | \(x=1,T=2\pi,n=-1,0,1\) | \(D_0=1,D_{\pm1}=0\) | validated | Symbolic integration must be tractable |
| `exponential_transform_variant` | `scripts/fourier/properties.py` | conversion_helper | same | \(a=3,\omega_c=2\) | \(1/(3+j(\omega-2))\) | validated | Positive time scaling only |
| `bode_values` | `scripts/frequency/bode.py` | numeric_helper | same | \(H=1/(s+1)\), \(\omega=0,1\) | 0 dB at \(\omega=0\) | validated | Does not choose MCQ answer |
| `classify_filter_limits` | same | diagnostic_helper | same | \(1/(s+1)\) | lowpass | validated | Not sufficient for every notch/all-pass case |
| `transfer_from_poles_zeros` | same | conversion_helper | same | zero 0, poles -1,-2, gain 2 | denominator `[1,3,2]` | validated | Numeric coefficients |
| `butterworth_lowpass_order` | `scripts/filters/butterworth.py` | primary_solver | same | \(f_p=500,f_s=3000,A_p=3,A_s=72\) | order 5 | validated | Magnitude specs only |
| `butterworth_highpass_order` | same | primary_solver | same | \(f_p=100,f_s=10,A_p=3,A_s=26\) | order 2 | validated | Requires \(f_s<f_p\) |
| `butterworth_poles_q` | same | numeric_helper | same | order 2 | \(Q=1/\sqrt{2}\) | validated | Stable LHP poles only |
| `frequency_scale_rc` | same | conversion_helper | same | \(R=1000,C=1\mu F,\omega_c=100\) | \(C=10\,nF\) with keep_R | validated | Normalized RC assumption |
| `adc_lsb` | `scripts/sampling/adc.py` | numeric_helper | same | 16 bit, 0-5 V | \(5/65536\) | validated | Ideal ADC |
| `alias_frequency` | same | primary_solver | same | \(f=4, F_s=6\) | 2 Hz | validated | Single-tone folding |
| `required_sampling_rate_for_lsb` | same | primary_solver | same | 16 bit, 5 V, 4th order, 100 Hz | 3200 Hz | validated | Uses high-frequency asymptote |
| `instrumentation_gains` | `scripts/circuits/instrumentation.py` | numeric_helper | same | \(R_2=499.5,R_G=1,\alpha=0.9\) | \(G_d=1000,G_c=0.05\) | validated | Uses simplified exam mismatch model |
| `solve_node_circuit` | `scripts/circuits/node_equations.py` | symbolic_helper | same | two-node RC KCL from notebook | \(H(s)=C_1R_1s/(C_1C_2R_1R_2s^2+s(C_1R_1+C_2R_1+C_2R_2)+1)\) | validated | KCL equations must be written correctly |

## Commands Actually Run

- `python -m compileall exam_toolbox.py scripts`
- `python scripts/validate_scripts.py`
- `python exam_toolbox.py`

Final statement: 27 public helper functions are covered by the exam toolbox/import smoke checks, 0 partially validated, 0 failed functions left in the toolbox. Rejected candidates are recorded in `reports/script_inventory.md`. `exam_toolbox.py` imports the validated helpers successfully and is ready for exam-support use within the stated limitations.
