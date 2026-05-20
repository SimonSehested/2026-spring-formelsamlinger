# Exam verification report

## Coverage table

Checked against every PDF currently in `input/exams/`: `F21.pdf` and `Exam_F21_LCD1 Part 2 - no answers.pdf`.

| Source | Problem | Problem type | Fast method | Covered in section | Missing recipe? |
|---|---|---|---|---|---|
| F21 | Q1 | Block diagram reduction | Reduce series/parallel/feedback blocks and preserve signs | `02_block_diagrams...` / Exam recipe: reduce a block diagram | No |
| F21 | Q2 | RLC transfer function and block diagram | Convert to \(s\)-domain impedances and use voltage divider/Kirchhoff equations | `05_modelling...` / Exam recipe: RLC circuit transfer function | No |
| F21 | Q3 | Pole-zero map to Bode plot | Use Bode slope and phase contribution table | `06_bode...` / Exam recipe: infer transfer function from Bode plot | No |
| F21 | Q4 | P-controller stability limit | Read \(-180^\circ\) frequency and compute \(K_{\mathrm{crit}}\) | `06_bode...` / Exam recipe: P-controller stability range from Bode plot | No |
| F21 | Q5 | Transfer function from Bode slopes and phase | Count integrators, break frequencies, poles/zeros, and gain | `06_bode...` / Exam recipe: infer transfer function from Bode plot | No |
| F21 | Q6 | Gain for specified phase margin | Find phase-implied frequency and shift magnitude to \(0\,\mathrm{dB}\) | `06_bode...` / Exam recipe: choose \(K_P\) for desired phase margin | No |
| F21 | Q7 | Coupled masses model | Write one force-balance equation per mass and Laplace transform | `05_modelling...` / Exam recipe: coupled mass equations of motion | No |
| F21 | Q8 | Differential equation to transfer function and poles | Zero initial conditions, collect \(Y\)/\(U\), factor denominator | `03_laplace...` / Exam recipe: ODE to transfer function and poles | No |
| F21 | Q9 | Second-order overshoot | Match denominator to standard second-order form and compute \(M_p\) | `04_frequency...` / Exam recipe: overshoot limit from closed-loop denominator | No |
| F21 | Q10 | Magnitude Bode plot to transfer function and DC gain | Read slopes, break frequencies, and low-frequency gain | `06_bode...` / Exam recipe: infer transfer function from Bode plot | No |
| F21 | Q11 | P-controller gain range from Bode stability | Use \(\omega_\pi\) and \(K_{\mathrm{crit}}=1/|G(j\omega_\pi)|\) | `06_bode...` / Exam recipe: P-controller stability range from Bode plot | No |
| F21 | Q12 | Higher-order ODE, poles at origin, stability | Build \(G(s)\), inspect denominator and repeated origin poles | `03_laplace...`; `04_frequency...` / Stability from poles | No |
| F21 | Q13 | Nyquist stability for open-loop unstable system | Count \(P\), encirclements \(N\), require \(Z=0\) | `07_nyquist...` / Exam recipe: Nyquist stability with unstable open loop | No |
| F21 | Q14 | Phase margin from Nyquist | Read unit-circle crossing angle | `07_nyquist...` / Exam recipe: phase margin from Nyquist plot | No |
| F21 | Q15 | Type-0 P control and finite error | Use gain shift, system type, and final value theorem | `09_design...` / Exam recipe: steady-state error from diagram or Bode DC gain | No |
| F21 | Q16 | Nonstandard feedback branch and DC error | Derive \(E/R\) from diagram before final value theorem | `02_block...` / Exam recipe: non-unity feedback steady-state error | No |
| F21 | Q17 | P-Lead-Lag beta selection | Insert \(N_i\) and lag phase in \(\phi_{\mathrm{lag}}\) equation | `11_limited...` / Exam recipe: solve for Lag parameter \(\beta\) | No |
| F21 | Q18 | PI-Lead design | Choose \(\tau_i\), compute phase deficit, solve \(\alpha,\tau_d,K_P\) | `08_pi_lead...` / Exam recipe: PI-Lead design from \(\omega_c\) and phase margin | No |
| F21 | Q19 | Nested block diagram and steady-state error | Reduce loops, use DC gain and final value theorem | `02_block...`; `09_design...`; `12_disturbances...` | No |
| F21 | Q20 | Feed-forward disturbance cancellation | Read disturbance sign, set \(\sigma_DD+GF_d=0\), check properness, compute disturbance sensitivity | `13_feed_forward...` / Exam recipe: design dynamic disturbance feed-forward | No |
| F21 Part 2 no answers | Q11 | P-controller stability range from Bode plot | Use \(K_{\mathrm{crit}}\) at \(-180^\circ\) phase crossing | `06_bode...` / Exam recipe: P-controller stability range from Bode plot | No |
| F21 Part 2 no answers | Q12 | ODE transfer function and unstable poles at origin | Transform ODE and inspect poles | `03_laplace...`; `04_frequency...` | No |
| F21 Part 2 no answers | Q13 | Nyquist criterion for unstable open loop | Count \(P,N,Z\) | `07_nyquist...`; `10_unstable...` | No |
| F21 Part 2 no answers | Q14 | Nyquist phase margin | Unit-circle crossing angle | `07_nyquist...` / Exam recipe: phase margin from Nyquist plot | No |
| F21 Part 2 no answers | Q15 | P gain effect and type-0 error | Magnitude shift plus steady-state error table/final value | `06_bode...`; `09_design...` | No |
| F21 Part 2 no answers | Q16 | Feedback branch gain and DC error | Derive \(E/R\) directly and evaluate \(s\to0\) | `02_block...` / Exam recipe: non-unity feedback steady-state error | No |
| F21 Part 2 no answers | Q17 | P-Lead-Lag phase design | Solve lag phase equation for \(\beta\) | `11_limited...` / Exam recipe: solve for Lag parameter \(\beta\) | No |
| F21 Part 2 no answers | Q18 | PI-Lead phase and magnitude design | PI phase, lead phase, crossover gain condition | `08_pi_lead...` / Exam recipe: PI-Lead design from \(\omega_c\) and phase margin | No |
| F21 Part 2 no answers | Q19 | Nested loops and steady-state error | Reduce blocks, compute DC error | `02_block...`; `09_design...`; `12_disturbances...` | No |
| F21 Part 2 no answers | Q20 | Feed-forward disturbance cancellation | Read disturbance sign and use \(F_d=-\sigma_DD/G\) with disturbance sensitivity | `13_feed_forward...` / Exam recipe: design dynamic disturbance feed-forward | No |

## Verification notes

Every listed exam problem maps to at least one formula section and at least one recipe or direct lookup table. No `sources/99_exam_required_extra_topics.tex` file was needed because the exam-required tasks fit the inferred lecture topics.

The feed-forward guide was checked against F21 Q20 and uses an explicit disturbance-sign variable \(\sigma_D\), because the correct sign depends on the summing junction in the exam diagram.

The formula collection was checked for lecture-note style by scanning for long derivations and proof language. The rewritten files favor formula blocks, recipes, fast checks, and common traps.
