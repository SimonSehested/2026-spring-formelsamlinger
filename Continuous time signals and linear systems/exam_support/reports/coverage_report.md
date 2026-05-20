# Coverage Report

## Course Inference

- Course: 22050 Signals and linear systems in continuous time / Signaler og lineære systemer i kontinuert tid.
- Exam format: 4-hour written MCQ exam, all aids allowed except internet, one-best-answer scoring, 20 equally weighted tasks.
- Languages in source material: lectures mostly English, exams Danish with English technical aliases.
- Notation: \(x(t)\) input, \(y(t)\) output, \(h(t)\) impulse response, \(H(s)\) transfer function, \(H(j\omega)\) frequency characteristic, \(j\) imaginary unit, unilateral Laplace unless stated.

## Source Files Inspected

| Folder | Files | Coverage Signal |
|---|---:|---|
| `input/exams` | 3 PDFs | Strongest signal: 2023 trial/self assessment, August 2024 re-exam, May 2025 exam |
| `input/lectures` | 13 PDFs | Topic order, notation, definitions, worked design examples |

Exam text was extracted with `pdftotext -layout` for inspection. No separate solution-set folder exists, but the 2024 and 2025 extracted exam files include marked/correct choices in several places, and the 2024 file includes student annotations. Validation therefore uses a mixture of source-derived examples and constructed identities.

## Lecture Topic Structure

| Lecture | Inferred Topic |
|---|---|
| L01 | Signal and system classification, LTIC, basic filters |
| L02 | Time-domain response, impulse response |
| L03 | Convolution |
| L04 | Fourier series |
| L05 | Fourier transform |
| L06 | Sampling and Fourier applications |
| L07 | ADC performance, anti-alias filtering |
| L08 | Laplace transform |
| L09 | Applications of Laplace |
| L10 | Second-order systems and Bode plot |
| L11 | Bode plot, pole-zero filter design |
| L12 | Butterworth filter design and sensitivity |
| L13 | Butterworth high-pass filter and AC-coupled instrumentation amplifier |

## Recurring Exam Topics

- LTIC classification: linearity, time invariance, causality, stability.
- Circuit KCL/KVL and differential equation or frequency-characteristic recognition.
- Impulse, step, ramp, zero-input, zero-state responses.
- Convolution of causal exponentials and support intervals.
- Fourier series coefficients, periodic reconstruction, orthogonality, symmetry.
- Fourier transform definition and properties: scaling, modulation, differentiation, time shift.
- Unilateral Laplace transform, initial/final value theorems, partial fractions.
- Second-order systems: poles, damping, \(Q\), overshoot, peak time, settling time.
- Bode plots, pole-zero diagrams, filter type recognition.
- Butterworth filter order, poles, Sallen-Key stages, sensitivity and scaling.
- Sampling, aliasing, ADC LSB, quantization noise, anti-alias filter sizing.
- Instrumentation amplifier differential/common-mode gain and CMRR.

## Generated Note Structure

| File | Purpose |
|---|---|
| `main.tex` | Compact PDF shell and input order |
| `sources/01_ltic_time_domain.tex` | LTIC, circuits, convolution, second-order time domain |
| `sources/02_fourier.tex` | Fourier series and transform lookup |
| `sources/03_laplace.tex` | Unilateral Laplace, zero-input/zero-state, inverse transforms |
| `sources/04_frequency_bode_filters.tex` | Frequency response, Bode, filters, Butterworth |
| `sources/05_sampling_adc_inamp.tex` | Sampling, ADC, anti-aliasing, instrumentation amplifier |
| `sources/99_python_script_index.tex` | Compact script index |

## Coverage Risks

- Circuit diagrams in the PDFs are image-based; notes include the reusable KCL/component rules but do not reproduce each circuit.
- Several exam questions are graphical matching tasks; scripts can compute Bode values and pole-zero responses, but final MCQ matching still requires visual interpretation.
- No official standalone solution PDFs are present; validation is strongest for tasks with marked answers or standard constructed cases.

## Full Audit Follow-Up

A stricter audit is available in `reports/full_input_coverage_audit.md`. It checks all 60 exam problems plus lecture coverage and records the few compact note improvements made after the audit:

- second-order pole-coordinate sensitivity,
- pole-zero phase traps,
- Butterworth causal/anti-causal pole split,
- Sallen-Key lowpass/highpass component matching rules.

## Build Verification

- `latexmk -version` was attempted, but MiKTeX reported that Perl is missing for `latexmk`.
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex` was run twice and produced `main.pdf`.
- The PDF build completed with layout warnings from long script paths and compact two-column formulas, but no LaTeX errors remained.
