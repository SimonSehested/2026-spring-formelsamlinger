# Script inventory

Python er relevant som kontrolberegner for allerede opstillede transferfunktioner og designparametre. Den må ikke fortolke figurer eller vælge controllerarkitektur.

| Opgavetype | Kandidatfunktion | Status | Begrundelse | Input | Output | Validerbar? | Relaterede eksamensopgaver |
| ---------- | ---------------- | ------ | ----------- | ----- | ------ | ----------- | -------------------------- |
| Poler/stabilitet | `transfer_function_poles` | Accepteret | Genbrugelig deterministisk polynomialberegning | Nævnerkoefficienter | Komplekse poler | Ja | Q4,Q8,Q11,Q12 |
| Stabilitetsinterval i gain | `find_stable_gain_ranges` | Accepteret | Automatiserer `p(j*w,K)=0` og polkontrol mellem grænser | `p(s,K), K, s` | Marginalpunkter og stabile intervaller | Ja | Gain-afhængige stabilitetsopgaver |
| DC-fejl | `unity_feedback_step_error` | Accepteret | Forebygger algebra-/DC-fejl efter loopet er bestemt | `num, den, gain` | `e_ss` | Ja | Q16 |
| P-gain kontrol | `closed_loop_poles` | Accepteret | Tester kandidatgain uden at vælge svar | `num, den, gain` | Closed-loop poler | Ja | Q4,Q11 |
| Nyquist marginpunkt | `phase_margin_from_point` | Accepteret | Stabil beregning efter manuel punktaflæsning | Real/imag | Grader | Ja | Q14 |
| Andenordensovershoot | `second_order_characteristics` | Accepteret | Standardparameterkontrol | Nævner | `omega_n,zeta,M_p` | Ja | Q9 |
| PI-Lead design | `design_pi_lead_at_crossover` | Accepteret | Tung, entydig parameterberegning med checks | TF, `omega_c, PM, Ni` | Parametre/targetcheck | Ja | Q18 |
| Lag design | `solve_lag_beta` | Accepteret | Entydig løsning af opgavens lagfaseformel | `phi_lag, Ni` | `beta` | Ja | Q17 |
| Feed-forward | `ideal_disturbance_feedforward` | Accepteret | Kontrollerer ratio/properness efter manuelt fortegn | `G,D,sigma_D` | `F_d`, status | Ja | Q20 |
| Bodebillede til TF | Automatisk plotlæser | Afvist | Input er billede, og RHP/LHP kræver robust fasefortolkning | PDF-figur | TF | Nej | Q3,Q5,Q10 |
| Nyquist encirclement | Automatisk kurvetæller fra figur | Afvist | Kurveretning og kontur må aflæses fagligt | PDF-figur | Stabilitetsvalg | Nej | Q13 |
| Blokdiagramparser | Automatisk reducering fra billede | Afvist | Fortegn og signalplacering er ikke struktureret input | Figur | TF | Nej | Q1,Q2,Q19,Q20 |
| Saturation/windup design | Automatisk controller-valg | Afvist | Kræver actuator-/performancevalg og simulationer, som kilderne ikke leverer | Model/spec | Controller | Nej | L11 |
