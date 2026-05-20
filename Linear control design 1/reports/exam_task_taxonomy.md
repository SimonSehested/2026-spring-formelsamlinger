# Exam task taxonomy

## Inferred exam format

The available exam material emphasizes compact control-analysis and controller-design tasks. Many problems can be solved by recognizing the task type, selecting the correct formula, and rejecting inconsistent answer options.

## Task types

| Task type | Common wording / Ctrl+F keywords | Required formulas | Fast method | Common traps | Source problems |
|---|---|---|---|---|---|
| Block diagram reduction | block diagram, feedback, summing junction, non-unity feedback | series/parallel rules, \(Y/R=CG/(1+CGH)\), \(E/R=1/(1+CGH)\) | Reduce inner loops first and preserve summing-junction signs | Losing \(H(s)\), wrong feedback sign | F21 Q1, Q16, Q19 |
| RLC transfer function | RLC, impedance, voltage divider | \(Z_R=R\), \(Z_L=sL\), \(Z_C=1/(sC)\), voltage divider | Convert to impedances, combine, simplify | Choosing wrong output impedance | F21 Q2 |
| Mechanical model | equations of motion, masses, spring, damper | \(\sum F=m\ddot{x}\), relative spring/damper forces | Free-body equation per mass, Laplace transform, solve | Same sign for internal forces on both masses | F21 Q7 |
| ODE to transfer function | differential equation, Laplace, poles | derivative property, \(G=Y/U\), characteristic polynomial | Zero initial conditions, collect \(Y\) and \(U\), factor denominator | Keeping initial-condition terms | F21 Q8, Q12 |
| Pole stability | poles, stable, unstable, origin | \(\operatorname{Re}(p)<0\) for all poles | Inspect denominator roots | Treating repeated origin poles as stable | F21 Q8, Q12 |
| Bode to transfer function | Bode plot, slopes, phase, poles, zeros | Bode factor form and slope table | Count integrators, break frequencies, slope changes, phase signs | Missing RHP zero/pole phase reversal | F21 Q3, Q5, Q10 |
| Phase margin gain selection | desired phase margin, choose \(K_P\) | \(\gamma_M=180^\circ+\angle L(j\omega_c)\), dB conversion | Find phase-implied frequency, set magnitude to 0 dB | Using the old crossover frequency | F21 Q6 |
| P-controller stability range | range of \(K_P\), stability from Bode | \(K_{\mathrm{crit}}=1/|G(j\omega_\pi)|\) | Read magnitude at \(-180^\circ\), require \(0<K_P<K_{\mathrm{crit}}\) for stable plants | Applying stable-plant rule to unstable plants | F21 Q4, Q11 |
| Second-order overshoot | overshoot, damping, standard second-order | \(M_p=100e^{-\zeta\pi/\sqrt{1-\zeta^2}}\%\) | Match denominator to \(s^2+2\zeta\omega_ns+\omega_n^2\) | Applying to non-dominant higher-order systems | F21 Q9 |
| Nyquist unstable-loop stability | Nyquist, encirclement, unstable open loop | \(Z=P+N\), \(Z=0\) | Count \(P\), read encirclements, check \(Z\) | Bode margin shortcut with \(P>0\) | F21 Q13 |
| Nyquist phase margin | unit circle, Nyquist phase margin | \(\gamma_M=180^\circ+\arg L(j\omega_c)\) | Find unit-circle crossing and read angle | Reading gain margin instead | F21 Q14 |
| PI-Lead design | PI-Lead, \(\alpha\), \(\tau_d\), \(N_i\), \(\omega_c\) | PI phase, lead phase, \(\alpha\), \(\tau_d\), gain condition | Compute phase deficit, set lead, then solve \(K_P\) | Forgetting PI negative phase | F21 Q18 |
| P-Lead-Lag beta design | P-Lead-Lag, Lag, \(\beta\), \(N_i\) | \(\phi_{\mathrm{lag}}=\arctan(N_i(1-\beta)/(1+\beta N_i^2))\) | Insert allowed lag phase and solve \(\beta>1\) | Treating Lag as PI | F21 Q17 |
| Steady-state error | steady-state error, final value, DC gain | \(e_{\mathrm{ss}}=\lim sE(s)\), system type table | Derive \(E/R\), insert step, evaluate \(s\to0\) | Using unity-feedback formulas for non-unity diagrams | F21 Q15, Q16, Q19 |
| Disturbance sensitivity | disturbance, sensitivity, output disturbance, input disturbance | \(S=1/(1+L)\), \(T=L/(1+L)\), disturbance paths | Set other inputs to zero, solve requested transfer | Confusing input and output disturbances | F21 Q16, Q19, Q20 |
| Feed-forward cancellation | feed-forward, measured disturbance, cancellation | \(F_d=-\sigma_DD/G\), \(G_{yd}=(\sigma_DD+GF_d)/(1+CG)\) | Read summing-junction sign, set \(\sigma_DD+GF_d=0\), check properness | Wrong sign or improper \(F_d\) | F21 Q20 |

## Recipe coverage

Every recurring task type above has at least one explicit `Exam recipe` section in `sources/*.tex`. The formula sheet also includes keyword headings to support Ctrl+F by English and selected Danish terms.
