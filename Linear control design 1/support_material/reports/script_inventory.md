# Script inventory

Python er relevant som kontrolberegner for allerede opstillede transferfunktioner og designparametre. Den må ikke fortolke figurer eller vælge controllerarkitektur.

| Opgavetype | Kandidatfunktion | Status | Begrundelse | Input | Output | Validerbar? | Relaterede eksamensopgaver |
| ---------- | ---------------- | ------ | ----------- | ----- | ------ | ----------- | -------------------------- |
| Poler/stabilitet | `transfer_function_poles` | Accepteret | Genbrugelig deterministisk polynomialberegning | Nævnerkoefficienter | Komplekse poler | Ja | F21 Q8,Q12; S20 Q16; 2022 Q8; E23 Q7; F25 Q3,Q20 |
| Stabilitetsinterval i gain | `find_stable_gain_ranges` | Accepteret | Automatiserer `p(j*w,K)=0` og polkontrol mellem grænser | `p(s,K), K, s` | Marginalpunkter og stabile intervaller | Ja | Gain-afhængige stabilitetsopgaver |
| DC-fejl | `unity_feedback_step_error` | Accepteret | Forebygger algebra-/DC-fejl efter loopet er bestemt | `num, den, gain` | `e_ss` | Ja | F21 Q16; 2022 Q16; E23 Q18; F25 Q14 |
| P-gain kontrol | `closed_loop_poles` | Accepteret | Tester kandidatgain uden at vælge svar | `num, den, gain` | Closed-loop poler | Ja | F21 Q4,Q11; 2022 Q6,Q12; S20 Q12 |
| Nyquist marginpunkt | `phase_margin_from_point` | Accepteret | Stabil beregning efter manuel punktaflæsning | Real/imag | Grader | Ja | F21 Q14 |
| Andenordensovershoot | `second_order_characteristics` | Accepteret | Standardparameterkontrol | Nævner | `omega_n,zeta,M_p` | Ja | F21 Q9; S20 Q5; 2022 Q3; F25 Q20 |
| PI-Lead design | `design_pi_lead_at_crossover` | Accepteret | Tung, entydig parameterberegning med checks | TF, `omega_c, PM, Ni` | Parametre/targetcheck | Ja | F21 Q18; S20 Q14; 2022 Q17,Q19; F25 Q16 |
| Lag design | `solve_lag_beta` | Accepteret | Entydig løsning af opgavens lagfaseformel | `phi_lag, Ni` | `beta` | Ja | F21 Q17; S20 Q17-Q18; F25 Q17 |
| Feed-forward | `ideal_disturbance_feedforward` | Accepteret | Kontrollerer ratio/properness efter manuelt fortegn | `G,D,sigma_D` | `F_d`, status | Ja | F21 Q20; 2022 Q18; F25 Q19 |
| Bodebillede til TF | Automatisk plotlæser | Afvist | Input er billede, og RHP/LHP kræver robust fasefortolkning | PDF-figur | TF | Nej | S20 Q6-Q8,Q13; F21 Q3,Q5,Q10; 2022 Q4-Q5; E23 Q8,Q10-Q11,Q16 |
| Nyquist encirclement | Automatisk kurvetæller fra figur | Afvist | Kurveretning og kontur må aflæses fagligt | PDF-figur | Stabilitetsvalg | Nej | S20 Q17-Q18; F21 Q13; 2022 Q12; F25 Q13 |
| Blokdiagramparser | Automatisk reducering fra billede | Afvist | Fortegn og signalplacering er ikke struktureret input | Figur | TF | Nej | S20 Q1,Q3,Q19; F21 Q1,Q2,Q19,Q20; E23 Q1,Q2,Q18-Q20 |
| Saturation/windup design | Automatisk controller-valg | Afvist | Kræver actuator-/performancevalg og simulationer, som kilderne ikke leverer | Model/spec | Controller | Nej | L11 |
| P-Lead closed-form helper | Ny funktion | Afvist | Zero/pole/magnitudebidrag er få direkte formler og dækkes tydeligt i noterne | `alpha, omega_c` | `tau_d`, frekvenser | Ja | S20 Q10-Q11; 2022 Q13; E23 Q14 |
