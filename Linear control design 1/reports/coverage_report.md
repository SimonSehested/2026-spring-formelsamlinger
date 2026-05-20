# Coverage report

## Detected source files

`source_material/` is not present in this checkout. The available course material is under `input/`.

### Lectures

| File | Inferred topic |
|---|---|
| `input/lectures/1_Welcome_Lecture.pdf` | Course overview, feedback control, PID-based design |
| `input/lectures/2_block_control_concept.pdf` | Block diagrams, feedback concepts, hand tuning |
| `input/lectures/3_Laplace_TF.pdf` | Laplace transform, transfer functions, characteristic equations |
| `input/lectures/4_Frequency_and_Time_Analysis_WSol.pdf` | Frequency response, time response, poles, stability |
| `input/lectures/5_Modelling.pdf` | Mechanical/electrical modelling, linearization |
| `input/lectures/6_Bode_plot&Stability.pdf` | Bode plots, stability margins, P-controller design |
| `input/lectures/Lecture_07_Nyquist plot and stability.pdf` | Nyquist plots and stability criterion |
| `input/lectures/Lecture_08_PI_LEAD_design.pdf` | PI and Lead controller design |
| `input/lectures/Lecture_09_PI_LEAD_design_specifications.pdf` | Design specifications and PI-Lead tuning |
| `input/lectures/Lecture_10_Unstable_systems (1).pdf` | Open-loop unstable systems and nested loops |
| `input/lectures/Lecture_11_Limited_systems (1).pdf` | Limited systems, actuator limits, P-Lead-Lag |
| `input/lectures/Lecture_12_Disturbances_sensitivity_prefilters.pdf` | Disturbances, sensitivity, prefilters |
| `input/lectures/Lecture_13_Feed_forward.pdf` | Feed-forward control and disturbance cancellation |

### Exams

| File | Notes |
|---|---|
| `input/exams/F21.pdf` | F21 exam, Q1-Q20, recurring controller-design and analysis tasks |
| `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf` | F21 part 2, Q11-Q20, no answers |

### Exercises

No `input/exercises/` or `source_material/exercises/` directory was present.

## Inferred course title

`34721/34722 Linear Control Design 1`, Spring 2026.

## Inferred formula-collection structure

The existing lecture-aligned modular structure was preserved because the lecture PDFs are numbered and the exam tasks map cleanly to those topics. The content was rewritten to be exam-friendly: short formulas, recognition keywords, recipes, fast checks, and common traps.

| File | Primary exam use |
|---|---|
| `sources/01_course_overview_and_control_concepts.tex` | Exam map, notation, controller templates, answer-option checks |
| `sources/02_block_diagrams_and_feedback.tex` | Block reduction, feedback signs, non-unity feedback error |
| `sources/03_laplace_transform_and_transfer_functions.tex` | ODE to transfer function, characteristic equations, poles/zeros |
| `sources/04_frequency_and_time_domain_analysis.tex` | Final value, step response, overshoot, pole stability |
| `sources/05_modelling_and_linearization.tex` | RLC and mechanical modelling, linearization |
| `sources/06_bode_plots_and_stability_margins.tex` | Bode interpretation, phase margin, gain margin, P gain range |
| `sources/07_nyquist_plot_and_stability.tex` | Nyquist encirclement, unstable open-loop stability, margins from Nyquist |
| `sources/08_pi_lead_controller_design.tex` | PI-Lead equations and design recipe |
| `sources/09_design_specifications_and_tuning.tex` | Steady-state error, system type, design-spec interpretation |
| `sources/10_unstable_systems.tex` | Open-loop unstable checks, nested loops |
| `sources/11_limited_systems_and_lag_control.tex` | Saturation/rate limits and P-Lead-Lag beta recipe |
| `sources/12_disturbances_sensitivity_and_prefilters.tex` | Sensitivity paths, disturbance transfer functions, prefilters |
| `sources/13_feed_forward_control.tex` | Dynamic/static feed-forward disturbance cancellation |

## Key notation

| Symbol | Meaning |
|---|---|
| \(r(t), R(s)\) | reference signal |
| \(e(t), E(s)\) | control error |
| \(u(t), U(s)\) | controller/plant input |
| \(y(t), Y(s)\) | output |
| \(y_m(t), Y_m(s)\) | measured output |
| \(G(s)\) | plant transfer function |
| \(C(s)\) | controller transfer function |
| \(H(s)\) | measurement transfer function |
| \(L(s)=C(s)G(s)H(s)\) | loop transfer function |
| \(S(s)=1/(1+L(s))\) | sensitivity |
| \(T(s)=L(s)/(1+L(s))\) | complementary sensitivity |
| \(\omega_c\) | gain crossover frequency |
| \(\gamma_M\) | phase margin |
| \(A_M\) | gain margin |
| \(K_P,\tau_i,\tau_d\) | controller parameters |
| \(\alpha,\beta,N_i\) | Lead/Lag design parameters |

## Recurring exam concepts

The recurring exam tasks are block diagram reduction; RLC transfer functions; coupled-mass equations of motion; ODE-to-transfer-function conversion; pole stability; Bode plot to transfer function; proportional gain from phase margin; proportional stability range; second-order overshoot; Nyquist stability for open-loop unstable systems; phase margin from Nyquist; PI-Lead design; P-Lead-Lag beta selection; steady-state error; sensitivity/disturbance transfer functions; and feed-forward disturbance cancellation with diagram-dependent summing-junction sign.

## Searchability changes

Each source file now starts with a `Ctrl+F keywords` subsection. Recipe headings include exam task wording such as `Exam recipe: infer transfer function from Bode plot`, `Exam recipe: choose K_P for desired phase margin`, and `Exam recipe: design dynamic disturbance feed-forward`. Danish aliases were added where useful, including regulering, tilbagekobling, forstyrrelse, maaling, stationaer fejl, bodeplot, and begraensning.

## Known uncertainties

The Nyquist sign convention is marked in the LaTeX with `% TODO: verify sign convention from source` because convention depends on clockwise/counter-clockwise definitions in the slides.
