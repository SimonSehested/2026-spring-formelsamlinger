# Full Input Coverage Audit

## Scope

- Inputs audited: 3 exam PDFs in `input/exams/` and 13 lecture PDFs in `input/lectures/`.
- Text extraction: `pdftotext -layout -enc UTF-8` was used as audit work material. The persistent deliverable is this audit report, not the generated extraction files.
- Formula collections checked: `sources/` and the parallel Danish version `sources_da/`.
- Status meanings:
  - `covered`: formulas/recipes are directly searchable.
  - `covered + visual`: method is covered, but the student must interpret a circuit/plot image.
  - `fixed`: audit found a weak spot and the notes were improved.

## Exam Problem Coverage

| Source | Problem | Task type | Fast method needed | Covered in | Status |
|---|---:|---|---|---|---|
| 2023 trial | Q1 | LTIC classification | Superposition, time invariance, causality, stability checks | LTIC classification | covered |
| 2023 trial | Q2 | Differential equation from circuit | KCL and component laws | Circuit equations | covered + visual |
| 2023 trial | Q3 | Impulse response | \(H(s)\), inverse Laplace | Impulse response, Laplace | covered |
| 2023 trial | Q4 | Step to impulse/ramp | Differentiate/integrate response relations | Impulse/step/ramp | covered |
| 2023 trial | Q5 | Convolution | Causal Laplace product or support rule | Convolution | covered |
| 2023 trial | Q6 | System characteristic | Second-order poles, damping, stability | Second-order systems | covered |
| 2023 trial | Q7 | Fourier series statements | \(D_n\), periodic reconstruction, symmetry | Fourier series | covered |
| 2023 trial | Q8 | Fourier transform concepts | Transform existence, symmetry, transform pairs | Fourier transform | covered |
| 2023 trial | Q9 | Fourier properties | Differentiation, scaling, modulation | Fourier transform properties | covered |
| 2023 trial | Q10 | Fourier transform plot/property | Transform symmetry and property checks | Fourier transform | covered + visual |
| 2023 trial | Q11 | Unilateral Laplace | Definition, ROC, derivative rules | Laplace definitions | covered |
| 2023 trial | Q12 | Laplace and second order | Poles, \(Q\), damping | Laplace, second-order | covered |
| 2023 trial | Q13 | Step response via Laplace | \(Y(s)=H(s)/s\), inverse Laplace | Laplace response workflow | covered |
| 2023 trial | Q14 | Zero-input/zero-state | Separate initial-condition and input terms | Zero-input/zero-state | covered |
| 2023 trial | Q15 | Step response features | Overshoot, \(t_p\), \(t_s\) | Second-order step features | covered |
| 2023 trial | Q16 | System relations | LTIC response and transfer-function logic | LTIC, response relations | covered |
| 2023 trial | Q17 | Bode matching | Slopes, phase, break frequencies | Bode plot rules | covered + visual |
| 2023 trial | Q18 | Filter concepts | Butterworth and Sallen-Key true/false checks | Butterworth filters | covered |
| 2023 trial | Q19 | Sensitivity analysis | \(S_x^y\), \(\sigma,\omega_d\) sensitivities | Second-order sensitivity | fixed |
| 2023 trial | Q20 | Sallen-Key highpass design | HP transformation, Q sensitivity, RC scaling | Butterworth/Sallen-Key | fixed |
| 2024 re-exam | Q1 | System classification | LTIC and stability checks | LTIC classification | covered |
| 2024 re-exam | Q2 | Node equations | KCL and component laws | Circuit equations | covered + visual |
| 2024 re-exam | Q3 | Impulse response | Transfer function and inverse Laplace | Impulse response | covered |
| 2024 re-exam | Q4 | Impulse/ramp from step | Differentiate/integrate step response | Response relations | covered |
| 2024 re-exam | Q5 | Convolution | Causal convolution and support | Convolution | covered |
| 2024 re-exam | Q6 | System characteristic | Second-order damping and poles | Second-order systems | covered |
| 2024 re-exam | Q7 | Differential equation/circuit response | Circuit ODE and impulse/step implications | Circuit equations, responses | covered + visual |
| 2024 re-exam | Q8 | Fourier series/transform statements | Series vs transform, basis, continuity | Fourier | covered |
| 2024 re-exam | Q9 | Fourier transform | Property and transform-pair checks | Fourier transform | covered |
| 2024 re-exam | Q10 | Circuit equation by Fourier transform | Impedance algebra, \(H(j\omega)\) | Circuit phasor rules | covered + visual |
| 2024 re-exam | Q11 | Frequency characteristic | \(H(j\omega)\), magnitude/phase | Frequency response | covered |
| 2024 re-exam | Q12 | Fourier symmetry | Even/odd real signals and spectra | Fourier symmetry | covered |
| 2024 re-exam | Q13 | Laplace concepts | Bilateral/unilateral, ROC, \(0^-\) | Laplace definitions | covered |
| 2024 re-exam | Q14 | Zero-input/zero-state | Initial-condition Laplace terms | Zero-input/zero-state | covered |
| 2024 re-exam | Q15 | Inverse Laplace | Partial fractions | Inverse Laplace | covered |
| 2024 re-exam | Q16 | Step response plot features | Estimate \(\zeta,\omega_n\) from plot | Step features | covered + visual |
| 2024 re-exam | Q17 | Butterworth concepts | Definition, poles, cascaded sections | Butterworth filters | fixed |
| 2024 re-exam | Q18 | 5th-order Butterworth/Sallen-Key | Stage \(Q\), sensitivity, scaling | Butterworth/Sallen-Key | fixed |
| 2024 re-exam | Q19 | Bodeplot matching | Slopes and phase trends | Bode plot rules | covered + visual |
| 2024 re-exam | Q20 | ADC and aliasing | LSB, aliasing, anti-alias filter | Sampling/ADC | covered |
| May 2025 | Q1 | Circuit diagram information | KCL and filter limit checks | Circuit equations | covered + visual |
| May 2025 | Q2 | ODE coefficients and properties | LTIC, DC gain, second-order step | LTIC, second-order | covered |
| May 2025 | Q3 | Impulse response | Inverse Laplace from \(H(s)\) | Impulse response | covered |
| May 2025 | Q4 | Step response plots | Second-order response recognition | Step features | covered + visual |
| May 2025 | Q5 | Convolution statements | Zero-state use and support logic | Convolution | covered |
| May 2025 | Q6 | Fourier series | Orthogonality, coefficients, reconstruction | Fourier series | covered |
| May 2025 | Q7 | Fourier transform statements | Periodic signals, symmetry, transform pairs | Fourier transform | covered |
| May 2025 | Q8 | Fourier transform properties | Scaling/modulation from \(e^{-at}u(t)\) | Fourier properties | covered |
| May 2025 | Q9 | AC circuit | Impedance algebra | Circuit phasor rules | covered + visual |
| May 2025 | Q10 | Frequency characteristic | \(H(j\omega)\), magnitude/phase | Frequency response | covered |
| May 2025 | Q11 | Laplace concepts | Existence, Fourier vs Laplace, partial fractions | Laplace | covered |
| May 2025 | Q12 | Laplace statements | ODE transform, convolution theorem, step response | Laplace workflow | covered |
| May 2025 | Q13 | Inverse Laplace | Repeated poles and inverse pairs | Inverse Laplace | covered |
| May 2025 | Q14 | Laplace response | Zero-input/zero-state and step response | Laplace response | covered |
| May 2025 | Q15 | Filter/notch classification | Limits, \(Q\), real/complex poles | Filter limits, second-order | covered |
| May 2025 | Q16 | System identification | Step features vs Bode consistency | Second-order and Bode consistency | covered + visual |
| May 2025 | Q17 | Pole-zero filter design | Pole/zero distance and phase logic | Pole-zero interpretation | fixed |
| May 2025 | Q18 | Butterworth filter | \(H(s)H(-s)\), poles, Sallen-Key sensitivity | Butterworth/Sallen-Key | fixed |
| May 2025 | Q19 | Instrumentation amplifier | \(G_d,G_c,CMRR\) | Instrumentation amplifier | covered + visual |
| May 2025 | Q20 | Sampling and ADC | Sampling spectrum, quantization, anti-alias sizing | Sampling/ADC | covered |

## Lecture Coverage

| Lecture | Main exam-relevant topics | Covered in | Status |
|---|---|---|---|
| L01 | Signal/system classification, LTIC, basic filters | LTIC, filter classification | covered |
| L02 | Time-domain response, impulse response, step/ramp | Response relations | covered |
| L03 | Convolution | Convolution | covered |
| L04 | Fourier series | Fourier series | covered |
| L05 | Fourier transform | Fourier transform pairs/properties | covered |
| L06 | Sampling and Fourier applications | Sampling, Fourier properties | covered |
| L07 | ADC performance, quantization, anti-aliasing | Sampling/ADC | covered |
| L08 | Laplace transform | Laplace definitions and rules | covered |
| L09 | Applications of Laplace | Zero-input/zero-state, inverse Laplace | covered |
| L10 | Second-order systems and Bode | Second-order features, Bode consistency | covered |
| L11 | Bode and pole-zero filter design | Bode, pole-zero interpretation | fixed |
| L12 | Butterworth lowpass and sensitivity | Butterworth, Sallen-Key matching | fixed |
| L13 | Butterworth highpass and AC-coupled in-amp | Highpass Sallen-Key, instrumentation amplifier | fixed |

## Findings and Fixes Applied

- Added underdamped pole-coordinate sensitivity formulas for 2023 Q19:
  \(S_{\zeta}^{\sigma}=1\), \(S_{\omega_n}^{\sigma}=1\),
  \(S_{\zeta}^{\omega_d}=-\zeta^2/(1-\zeta^2)\), \(S_{\omega_n}^{\omega_d}=1\).
- Added pole-zero phase trap for mirrored left/right half-plane zeros, relevant to May 2025 Q17.
- Added Butterworth \(H(s)H(-s)\) causal/anti-causal clarification, relevant to May 2025 Q18 and L12.
- Added course-specific Sallen-Key sensitivity rules:
  lowpass unity-gain: match \(R_1=R_2\);
  highpass unity-gain: match \(C_1=C_2\).

## Remaining Risks

- Circuit diagrams and plots are image-based; the collection covers reusable solution methods, not each drawing.
- Graphical matching tasks still require manual reading of slopes, peaks, phase wraps, and pole-zero locations.
- No separate official solution PDFs are present, so correctness is checked against marked answers where visible, lecture formulas, and standard identities.
