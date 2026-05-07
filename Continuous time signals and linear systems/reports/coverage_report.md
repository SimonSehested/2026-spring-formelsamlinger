# Coverage Report

## Detected Source Files

The requested `source_material/` directory was not present. The course source material was detected in `input/`.

Lecture slide packages:

- `input/lectures/22050 L01 Classification og signals and systems 260202.pdf`
- `input/lectures/22050 L02 Time domain - impulse response 260120.pdf`
- `input/lectures/22050 L03 Convolution 260120.pdf`
- `input/lectures/22050 L04 - Fourier Series 260120.pdf`
- `input/lectures/22050 L05 -  Fourier Transformation 260120.pdf`
- `input/lectures/22050 L06 - Sampling and Applications of Fourier Transformation 260120.pdf`
- `input/lectures/22050 L07 - ADC performance - V2 - 260311-1834.pdf`
- `input/lectures/22050 L08 - Laplace Transform 260323.pdf`
- `input/lectures/22050 L09 Applications of Laplace 260406-0801.pdf`
- `input/lectures/22050 L10 - 2nd order systems and Bode plot 1 260120.pdf`
- `input/lectures/22050 L11 - Bode Plot - part 2 Pole-zero filter design 260421.pdf`
- `input/lectures/22050 L12 - Butterworth filter design and sensitivity - part 1 - 260423 (1).pdf`
- `input/lectures/22050 L13 - Butterworth HP Filter and AC coupled in-amp - 260502.pdf`

Exam sets:

- `input/exams/22050 - 2023 Eksamen - trial version.pdf`
- `input/exams/eksamen20130530 uden svar.pdf`
- `input/exams/eksamen20140523 uden svar.pdf`
- `input/exams/eksamen20150526 uden svar.pdf`
- `input/exams/eksamen20160525 uden svar.pdf`
- `input/exams/eksamen20170519 uden svar.pdf`
- `input/exams/eksamen20180522 uden svar.pdf`
- `input/exams/eksamen20190522 uden svar.pdf`

No `input/exercises/` or `source_material/exercises/` folder was present.

## Inferred Course Title

The slide headers identify the course as:

`22050 Signals and Linear Systems in Continuous Time`

The Danish exam front matter identifies the same course as:

`22050 Signaler og lineære systemer i kontinuert tid`

## Inferred Topic Structure

The lecture package numbering gives the primary structure:

1. Classification of signals and systems
2. Time domain and impulse response
3. Convolution
4. Fourier series
5. Fourier transformation
6. Sampling and applications of Fourier transformation
7. ADC performance
8. Laplace transform
9. Applications of Laplace
10. Second-order systems and Bode plot
11. Bode plot part 2 and pole-zero filter design
12. Butterworth filter design and sensitivity
13. Butterworth highpass filter and AC-coupled instrumentation amplifier

## Generated Source Files

- `sources/01_classification_of_signals_and_systems.tex`
- `sources/02_time_domain_impulse_response.tex`
- `sources/03_convolution.tex`
- `sources/04_fourier_series.tex`
- `sources/05_fourier_transformation.tex`
- `sources/06_sampling_and_fourier_applications.tex`
- `sources/07_adc_performance.tex`
- `sources/08_laplace_transform.tex`
- `sources/09_applications_of_laplace.tex`
- `sources/10_second_order_systems_and_bode_plot.tex`
- `sources/11_bode_plot_and_pole_zero_filter_design.tex`
- `sources/12_butterworth_filter_design_and_sensitivity.tex`
- `sources/13_butterworth_highpass_and_ac_coupled_in_amp.tex`
- `sources/99_exam_required_extra_topics.tex`

`main.tex` inputs all generated source files in the inferred lecture order.

## Key Notation

- Time variable: \(t\)
- Angular frequency: \(\omega\)
- Complex frequency: \(s\)
- Input and output: \(x(t)\), \(y(t)\)
- Impulse response: \(h(t)\)
- Transfer function: \(H(s)\)
- Frequency response: \(H(j\omega)\)
- Fourier transform: \(X(\omega)\)
- Laplace transform: \(X(s)\)
- Unit step and impulse: \(u(t)\), \(\delta(t)\)
- Differential operator: \(D=d/dt\)
- Sampling period and frequency: \(T_s\), \(f_s\), \(\omega_s\)
- Natural frequency and damping factor: \(\omega_n\), \(\zeta\)
- Filter cutoff frequency: \(\omega_c=2\pi f_c\)

## Recurring Exam Concepts

The exam sets repeatedly require:

- LTIC classification from equations and system descriptions
- Differential equations from circuits
- Impulse response from transfer functions or differential equations
- Relations between impulse response, step response, and ramp response
- Convolution integral and table-style convolution of causal exponentials
- Fourier series coefficients, harmonic representation, and symmetry
- Fourier transform definitions, transform pairs, and symmetry properties
- Laplace transform rules, unilateral initial conditions, initial/final value theorems
- Transfer functions, poles, zeros, stability, and filter classification
- Second-order damping cases, natural frequency, pole locations, and resonance
- Bode magnitude/phase interpretation and asymptotic slope rules
- Pole-zero filter design, lowpass/highpass transformations, and tracking-filter numerator choices
- Butterworth coefficients, Sallen-Key stages, frequency scaling, and sensitivity
- AC coupling, instrumentation-amplifier differential/common-mode gain, and CMRR

## Notes

PDF text was extracted to `reports/extracted_text/` for source inspection and exam verification. Some extracted mathematical symbols were degraded by PDF encoding, so formulas in the final `.tex` files use standard course notation where the slide/exam wording clearly identified the concept.
