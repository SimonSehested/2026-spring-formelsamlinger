# Coverage report

## Anvendte kilder

- Forelæsninger: alle 13 PDF'er under `input/lectures/`, læst før eksamensanalysen.
- Eksamen med løsningsnoter/markerede svar: `input/exams/Exam_S20.pdf`, `input/exams/F21.pdf`, `input/exams/eksamenssættet23.pdf`, `input/exams/F25.pdf`.
- Eksamen/questionnaire uden svar: `input/exams/EXAMS_LCD1_2022_no_answerS.pdf`.
- Kontroloriginaler: `input/exams/EXAM_LCD1_F21_Part1_no_answers.pdf` og `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf`.

## Outputstruktur

| Leverance | Status |
| --------- | ------ |
| `reports/input_audit.md` | Opdateret; alle eksamens- og forelæsningskilder dækket |
| `reports/full_curriculum_report.md` | Opdateret; forelæsning 1-13 kortlagt med slide-audit mod `lcd.pdf` |
| `reports/exam_set_analyses/S20.md`, `F21.md`, `2022.md`, `E23.md`, `F25.md` | Oprettet/opdateret; synlige opgaver analyseret |
| `reports/merged_task_taxonomy.md` | Opdateret for S20/F21/2022/E23/F25 |
| `reports/script_inventory.md`, `python_coverage_report.md` | Opdateret; ingen nye scripts nødvendige |
| `sections/*.tex`, `main.tex`, `lcd.pdf` | LaTeX-noter udvidet for både eksamener og slidepensum; PDF bygget i final review |
| `exam_verification_report.md` | Opdateret med mapping for alle synlige opgaver |

## Hovedemner og notesektioner

| Hovedemne | Notesektion | Eksamensrelation |
| --------- | ----------- | --------------- |
| ODE/fysisk model, state-space, poler og TF | `sections/03_model_time.tex` | S20 Q1-Q2,Q16; F21 Q2,Q7,Q8,Q12; 2022 Q8-Q9; E23 Q6-Q7; F25 Q3,Q7,Q20 |
| Første-/andenordensrespons, bandwidth og dæmpet frekvens | `sections/03_model_time.tex` | S20 Q4-Q5,Q7-Q8; F21 Q9-Q10; 2022 Q2-Q3,Q14; E23 Q16-Q17; F25 Q1,Q6,Q20 |
| Bode, P-gain og marginer | `sections/04_frequency_stability.tex`, `sections/06_controller_design.tex` | S20 Q6,Q9,Q12-Q13; F21 Q3-Q6,Q11,Q15; 2022 Q4-Q6,Q11,Q13,Q15; E23 Q8,Q10-Q14; F25 Q5,Q9-Q11 |
| Nyquist og ustabil plant | `sections/04_frequency_stability.tex` | S20 Q17-Q18; F21 Q13-Q14; 2022 Q12; F25 Q13,Q18 |
| Blokdiagram, systemtype og stationær fejl | `sections/05_feedback_error.tex` | S20 Q3,Q19; F21 Q1,Q16,Q19; 2022 Q16; E23 Q1-Q5,Q9,Q12,Q18-Q20; F25 Q2,Q4,Q14,Q15,Q18 |
| P-Lead, PI-Lead og Ziegler--Nichols | `sections/06_controller_design.tex` | S20 Q10-Q11,Q14-Q15; F21 Q18; 2022 Q13,Q17,Q19-Q20; E23 Q14-Q15; F25 Q8,Q16 |
| Lag, limits, disturbance, sensitivity og feed-forward | `sections/07_limits_disturbances_feedforward.tex` | S20 Q17-Q19; F21 Q17,Q20; 2022 Q18; F25 Q12,Q17,Q19 |
| White/grey/black-box, linearisering, dominerende poler og delay | `sections/03_model_time.tex` | Forelæsning 3-5 og 11; REGBOT/modelidentifikation |
| REGBOT balance og cascaded control | `sections/06_controller_design.tex` | Forelæsning 9-13; mandatory assignment-kontekst |
| Non-minimum phase og rate limiter-faldgruber | `sections/04_frequency_stability.tex`, `sections/07_limits_disturbances_feedforward.tex` | Forelæsning 6 og 11 |

## Fravalgte eller nedprioriterede emner

- 2022 Q1 og Q10 er ikke analyseret fagligt, fordi de ikke fremgår brugbart af tekstlaget; de er markeret i `2022.md` og `exam_verification_report.md` som manuelle reviewpunkter.
- Automatisk billedfortolkning af Bode, Nyquist, steprespons, REGBOT-arkitektur og blokdiagrammer er fortsat fravalgt, fordi figurerne ikke har strukturerede data, og fortolkningen er en central eksamenskompetence.
- Der er ikke tilføjet nye Python-funktioner for P-Lead zero/pole, bandwidth eller static loopgain, fordi de er direkte fålinjeformler og hurtigere/sikrere i noterne end som særskilte API'er.

## Symbolregisterstatus

Symbolregister er inkluderet i `sections/02_symbolregister.tex`. De nye sæt bruger samme hovednotation: \(s\), \(\omega_c\), \(\omega_\pi\), \(K_P\), \(K_0\), \(\alpha\), \(\beta\), \(\tau_i\), \(\tau_d\), \(S\), \(T\), \(F_d\).

## Python-status

- Eksisterende offentlige funktioner beholdes; ingen nye scripts var nødvendige for de nye eksamenssæt.
- Python dækker fortsat rødder, gainintervaller, DC-fejl i standardloop, andenordenschecks, PI-Lead/Lag og feed-forward-ratioer.
- Nye S20/2022/E23-opgaver udvider primært `notes_only`-området: systemtype/static constants, plotbaseret bandwidth, Lead-koncept og disturbancekurver.

## Buildstatus

- Build og tests er dokumenteret i `reports/final_review_report.md`; efter slide-audit skal PDF-tekstkontrollen også finde `REGBOT`, `black-box`, `lineariser`, `dominant`, `rate limiter`, `delay` og `non-minimum`.
- Hvis `latexmk` ikke fungerer lokalt, bruges samme direkte `pdflatex`-flow som tidligere.

## Kendte begrænsninger og manuelle reviewpunkter

- 2022-filen er sammensat/uden svar. Q2-Q9 og Q11-Q20 er analyseret; Q1/Q10 kræver visuel kontrol.
- Plotbaserede værdier og blokdiagramfortegn skal kontrolleres i original PDF ved eksakt svarvalg.
- Hjælpemiddelregler og tilladelse til Python er stadig ikke dokumenteret i inputmaterialet.
