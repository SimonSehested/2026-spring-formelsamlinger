# Exam verification report

| Exam | Problem | Required concept | Covered in file/section | Missing? |
|---|---|---|---|---|
| F21 | Q1 | Block diagram reduction with series, parallel, and feedback paths | `sources/02_block_diagrams_and_feedback.tex` / Block diagram algebra | No |
| F21 | Q2 | RLC circuit in Laplace domain and block diagram representation | `sources/05_modelling_and_linearization.tex` / Electrical impedance in Laplace domain | No |
| F21 | Q3 | Pole-zero map to Bode plot, complex poles and zeros | `sources/06_bode_plots_and_stability_margins.tex` / Asymptotic Bode rules | No |
| F21 | Q4 | P-controller stability limit using Bode phase margin | `sources/06_bode_plots_and_stability_margins.tex` / Stability margins; `sources/09_design_specifications_and_tuning.tex` / P-controller stability limit | No |
| F21 | Q5 | Infer transfer function from Bode slopes and phase | `sources/06_bode_plots_and_stability_margins.tex` / Bode form and asymptotic rules | No |
| F21 | Q6 | Select gain for specified phase margin from Bode magnitude | `sources/06_bode_plots_and_stability_margins.tex` / Phase margin; `sources/09_design_specifications_and_tuning.tex` / Magnitude conversion | No |
| F21 | Q7 | Equations of motion and transfer function of coupled masses | `sources/05_modelling_and_linearization.tex` / Newton's second law and transfer functions | No |
| F21 | Q8 | Differential equation to transfer function and poles | `sources/03_laplace_transform_and_transfer_functions.tex` / Differential equation to transfer function | No |
| F21 | Q9 | Unity feedback second-order form and overshoot limit | `sources/04_frequency_and_time_domain_analysis.tex` / Percent overshoot; `sources/09_design_specifications_and_tuning.tex` / Time-domain specifications | No |
| F21 | Q10 | Magnitude Bode plot to transfer function and DC gain | `sources/06_bode_plots_and_stability_margins.tex` / Bode form and magnitude rules | No |
| F21 | Q11 | P-controller gain range from Bode stability | `sources/06_bode_plots_and_stability_margins.tex` / Bode stability criterion and P-controller gain shift | No |
| F21 | Q12 | Higher-order ODE transfer function, double pole at origin, stability | `sources/03_laplace_transform_and_transfer_functions.tex` / Derivative property; `sources/04_frequency_and_time_domain_analysis.tex` / Stability from poles | No |
| F21 | Q13 | Nyquist stability for an open-loop unstable system with P gain | `sources/07_nyquist_plot_and_stability.tex` / Nyquist stability criterion; `sources/10_unstable_systems.tex` / Open-loop unstable plants | No |
| F21 | Q14 | Phase margin read from Nyquist unit-circle intersection | `sources/07_nyquist_plot_and_stability.tex` / Phase margin from unit circle intersection | No |
| F21 | Q15 | Type-0 second-order P control, crossover shift, finite steady-state error | `sources/06_bode_plots_and_stability_margins.tex` / P-controller gain shift; `sources/09_design_specifications_and_tuning.tex` / System type | No |
| F21 | Q16 | Nonstandard feedback branch and steady-state error | `sources/02_block_diagrams_and_feedback.tex` / Feedback reduction; `sources/12_disturbances_sensitivity_and_prefilters.tex` / Sensitivity functions | No |
| F21 | Q17 | P-Lead-Lag controller and lag phase equation for \(\beta\) | `sources/11_limited_systems_and_lag_control.tex` / Lag phase contribution | No |
| F21 | Q18 | PI-Lead controller, desired crossover and phase margin, \(\alpha\), \(K_P\) | `sources/08_pi_lead_controller_design.tex` / PI-Lead transfer function and design equations | No |
| F21 | Q19 | Nested block diagram, Bode DC gain, steady-state error | `sources/02_block_diagrams_and_feedback.tex` / Feedback reduction; `sources/09_design_specifications_and_tuning.tex` / Steady-state error; `sources/12_disturbances_sensitivity_and_prefilters.tex` / Sensitivity functions | No |
| F21 | Q20 | Dynamic disturbance feed-forward and disturbance sensitivity | `sources/13_feed_forward_control.tex` / Ideal dynamic disturbance feed-forward and disturbance sensitivity | No |
| F21 Part 2 no answers | Q11 | P-controller stability range from Bode plot | `sources/06_bode_plots_and_stability_margins.tex` / Stability margins | No |
| F21 Part 2 no answers | Q12 | ODE transfer function and unstable poles at origin | `sources/03_laplace_transform_and_transfer_functions.tex` / Differential equation to transfer function | No |
| F21 Part 2 no answers | Q13 | Nyquist criterion for unstable open-loop system | `sources/07_nyquist_plot_and_stability.tex` / Encirclement equation | No |
| F21 Part 2 no answers | Q14 | Nyquist phase margin from unit circle crossing | `sources/07_nyquist_plot_and_stability.tex` / Phase margin from unit circle intersection | No |
| F21 Part 2 no answers | Q15 | P gain effect on Bode phase and crossover; type-0 error | `sources/06_bode_plots_and_stability_margins.tex` / P-controller gain shift; `sources/09_design_specifications_and_tuning.tex` / Reference error table | No |
| F21 Part 2 no answers | Q16 | Feedback branch gain and DC error | `sources/02_block_diagrams_and_feedback.tex` / Negative feedback reduction; `sources/09_design_specifications_and_tuning.tex` / Steady-state error | No |
| F21 Part 2 no answers | Q17 | P-Lead-Lag phase design | `sources/11_limited_systems_and_lag_control.tex` / Lag phase contribution | No |
| F21 Part 2 no answers | Q18 | PI-Lead phase and magnitude design | `sources/08_pi_lead_controller_design.tex` / Crossover gain condition and phase-margin design equation | No |
| F21 Part 2 no answers | Q19 | Steady-state error through nested loops and Bode DC gain | `sources/09_design_specifications_and_tuning.tex` / Steady-state error; `sources/12_disturbances_sensitivity_and_prefilters.tex` / Sensitivity functions | No |
| F21 Part 2 no answers | Q20 | Feed-forward disturbance cancellation | `sources/13_feed_forward_control.tex` / Disturbance sensitivity with feed-forward | No |

## Verification notes

All exam problems map to at least one searchable section in the generated formula collection. No separate `sources/99_exam_required_extra_topics.tex` file was needed because the exam-only requirements fit the inferred lecture topics.
