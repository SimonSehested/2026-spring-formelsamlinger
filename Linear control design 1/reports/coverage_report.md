# Coverage report

## Detected source files

Expected `source_material/` was not present in this checkout. The available course material was found under `input/` and used as the source tree.

### Lectures

| File | Inferred topic |
|---|---|
| `input/lectures/1_Welcome_Lecture.pdf` | Introduction, course overview, feedback control, PID-based design |
| `input/lectures/2_block_control_concept.pdf` | Block diagrams, control concepts, hand tuning |
| `input/lectures/3_Laplace_TF.pdf` | Laplace transform, transfer functions, block diagram manipulation |
| `input/lectures/4_Frequency_and_Time_Analysis_WSol.pdf` | Frequency response, steady-state gain, time-domain response, pole stability |
| `input/lectures/5_Modelling.pdf` | White-box and black-box modelling, linearization, transfer function from data |
| `input/lectures/6_Bode_plot&Stability.pdf` | Bode plots, poles and zeros, stability margins, P design |
| `input/lectures/Lecture_07_Nyquist plot and stability.pdf` | Nyquist plot, stability criterion, margins from Nyquist |
| `input/lectures/Lecture_08_PI_LEAD_design.pdf` | PI and Lead design |
| `input/lectures/Lecture_09_PI_LEAD_design_specifications.pdf` | Design specifications, phase margin, crossover, tuning |
| `input/lectures/Lecture_10_Unstable_systems (1).pdf` | Open-loop unstable systems, stabilization, nested loops |
| `input/lectures/Lecture_11_Limited_systems (1).pdf` | Rate-limited and amplitude-limited systems, P-Lead-Lag design |
| `input/lectures/Lecture_12_Disturbances_sensitivity_prefilters.pdf` | Disturbances, sensitivity functions, prefilters |
| `input/lectures/Lecture_13_Feed_forward.pdf` | Feed-forward control and disturbance rejection |

### Exams

| File | Notes |
|---|---|
| `input/exams/F21.pdf` | Questions Q1-Q20 with answers/solutions in extracted text |
| `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf` | Questions 11-20 without answers |

### Exercises

No `source_material/exercises/` or `input/exercises/` directory was present.

## Inferred course title

`34721/34722 Linear Control Design 1`, Spring 2026.

## Inferred topic structure

1. Course overview and control concepts
2. Block diagrams and feedback
3. Laplace transform and transfer functions
4. Frequency and time-domain analysis
5. Modelling and linearization
6. Bode plots and stability margins
7. Nyquist plot and stability
8. PI-Lead controller design
9. Design specifications and tuning
10. Unstable systems
11. Limited systems and Lag control
12. Disturbances, sensitivity, and prefilters
13. Feed-forward control

## Generated source files

| File | Source basis |
|---|---|
| `sources/01_course_overview_and_control_concepts.tex` | Lecture 1 |
| `sources/02_block_diagrams_and_feedback.tex` | Lecture 2 and exam Q1, Q16, Q19 |
| `sources/03_laplace_transform_and_transfer_functions.tex` | Lecture 3 and exam Q2, Q8, Q12 |
| `sources/04_frequency_and_time_domain_analysis.tex` | Lecture 4 and exam Q9 |
| `sources/05_modelling_and_linearization.tex` | Lecture 5 and exam Q2, Q7 |
| `sources/06_bode_plots_and_stability_margins.tex` | Lecture 6 and exam Q3-Q6, Q10, Q11, Q15 |
| `sources/07_nyquist_plot_and_stability.tex` | Lecture 7 and exam Q13-Q14 |
| `sources/08_pi_lead_controller_design.tex` | Lecture 8 and exam Q18 |
| `sources/09_design_specifications_and_tuning.tex` | Lecture 9 and exam Q6, Q9, Q15 |
| `sources/10_unstable_systems.tex` | Lecture 10 and exam Q13 |
| `sources/11_limited_systems_and_lag_control.tex` | Lecture 11 and exam Q17 |
| `sources/12_disturbances_sensitivity_and_prefilters.tex` | Lecture 12 and exam Q16, Q19 |
| `sources/13_feed_forward_control.tex` | Lecture 13 and exam Q20 |

## Key notation

| Symbol | Meaning |
|---|---|
| \(r(t), R(s)\) | reference signal |
| \(e(t), E(s)\) | control error |
| \(u(t), U(s)\) | control input |
| \(y(t), Y(s)\) | output |
| \(y_m(t), Y_m(s)\) | measured output |
| \(G(s)\) | plant transfer function |
| \(C(s)\) | controller transfer function |
| \(H(s)\) | measurement transfer function |
| \(L(s)=C(s)G(s)H(s)\) | loop transfer function |
| \(S(s)=1/(1+L(s))\) | sensitivity |
| \(T(s)=L(s)/(1+L(s))\) | complementary sensitivity |
| \(\omega_c\) | crossover frequency |
| \(\gamma_M\) | phase margin |
| \(A_M\) | gain margin |
| \(K_P,\tau_i,\tau_d\) | PID parameters |
| \(\alpha,\beta,N_i\) | Lead/Lag design parameters |

## Recurring exam concepts

Block diagram reduction; RLC transfer functions; Laplace transform of ODEs; poles, zeros, and stability; Bode plot interpretation; phase margin and gain margin; P-controller stability limits; second-order overshoot; Nyquist encirclement and phase margin; PI-Lead and P-Lead-Lag controller design; steady-state error; disturbance sensitivity; feed-forward disturbance cancellation.

## Build verification

`main.tex` was compiled successfully with a local Node/Tectonic compiler wrapper, producing `build/main.pdf`. A non-fatal Fontconfig warning was emitted by the wrapper, but the PDF was generated successfully. A separate structural check confirmed that all `\input{...}` files exist and that basic brace and environment pairing is balanced.
