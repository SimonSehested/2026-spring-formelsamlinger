# Coverage report

## Anvendte kilder

- Forelæsninger: alle 13 PDF'er under `input/lectures/`, læst før eksamensanalysen.
- Eksamen: `input/exams/F21.pdf` som samlet Q1-Q20 med svar og solution.
- Kontroloriginal: `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf`, som gentager Q11-Q20 uden svar.
- Der er ikke medleveret Matlabfiler, datasæt, hjælpemiddelregler eller flere årgange.

## Outputstruktur

| Leverance | Status |
| --------- | ------ |
| `reports/input_audit.md` | Oprettet; alle 15 PDF-kilder dækket |
| `reports/full_curriculum_report.md` | Oprettet; forelæsning 1-13 kortlagt |
| `reports/exam_set_analyses/F21.md` | Oprettet; Q1-Q20 analyseret |
| `reports/merged_task_taxonomy.md` | Oprettet |
| `reports/script_inventory.md` | Oprettet |
| `scripts/control/*.py`, `scripts/validate_scripts.py` | Oprettet og valideret |
| `exam_toolbox.ipynb`, `reports/notebook_inventory.md` | Oprettet; notebook kørt top-til-bund |
| `reports/python_coverage_report.md` | Oprettet |
| `main.tex`, `sections/*.tex`, `main.pdf` | Oprettet og bygget |
| Integrations-, verification- og reviewrapporter | Oprettet |

## Hovedemner og notesektioner

| Hovedemne | Notesektion | Eksamensrelation |
| --------- | ----------- | --------------- |
| ODE/fysisk model, poler og TF | `sections/03_model_time.tex` | Q2,Q7,Q8,Q12 |
| Første-/andenordensrespons | `sections/03_model_time.tex` | Q9,Q10 |
| Bode og P-gain/margin | `sections/04_frequency_stability.tex`, `sections/06_controller_design.tex` | Q3-Q6,Q11,Q15 |
| Nyquist og ustabil plant | `sections/04_frequency_stability.tex` | Q13,Q14 |
| Feedback og stationær fejl | `sections/05_feedback_error.tex` | Q1,Q16,Q19 |
| PI-Lead | `sections/06_controller_design.tex` | Q18 |
| Lag og begrænsede systemer | `sections/07_limits_disturbances_feedforward.tex` | Q17; L11 |
| Disturbance/sensitivity/prefilter | `sections/07_limits_disturbances_feedforward.tex` | L12 |
| Feed-forward | `sections/07_limits_disturbances_feedforward.tex` | Q20 |

## Fravalgte eller nedprioriterede emner

- Ziegler-Nichols/håndtuning omtales i pensumrapporten, men har ingen direkte F21-typeopgave og er ikke udbygget som prioriteret eksamensopskrift.
- REGBOT mandatory assignment/cascaded arkitektur omtales i pensumkilden, men ikke som særskilt F21-opgave; de generelle loopmetoder dækker de relevante principper.
- Automatisk billedfortolkning af Bode, Nyquist og blokdiagrammer er fravalgt, fordi kilderne ikke giver strukturerede numeriske data og fortolkningen er den faglige opgave.

## Symbolregisterstatus

Symbolregister er inkluderet i `sections/02_symbolregister.tex`, fordi faget bruger signaler, komplekse variable, marginer, controllerparametre og sensitivitetssymboler med overlappende betydning.

## Python-status

- Ni offentlige funktioner er inkluderet og valideret med 23 passing checks.
- Notebooken importerer kun disse validerede funktioner og er udført top-til-bund uden fejl.
- Python dækker beregningskontrol og specificeret PI-Lead/Lag-design; metodevalg og figurlæsning forbliver manuelt.

## Buildstatus

- `latexmk -pdf ...` fejlede lokalt, fordi MiKTeX mangler Perl-scriptmotor.
- PDF blev derefter bygget succesfuldt med to direkte kørsler af `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.
- Dansk `babel` og ubrugt `multirow`/kosmetisk `fancyhdr` var ikke installeret og blev fjernet fra præamblen; dokumentet anvender fortsat UTF-8/T1 og dansk tekst.
- Resultat: `main.pdf`, 11 sider. `build.log` gemmer den succesfulde buildoutput.

## Kendte begrænsninger og manuelle reviewpunkter

- Kun ét historisk eksamenssæt foreligger; prioritering kan ikke bekræftes på tværs af år.
- Plotbaserede værdier og blokdiagramfortegn skal kontrolleres i original PDF.
- Q9-facit afrunder overshootgrænsen; Q18 solutiontekst har en mindre numerisk faseafvigelse fra den trykte TF. Begge er dokumenteret i scriptvalideringen.
- Buildet giver ikke-fatale overfull/bookmark-warnings ved lange funktionsnavne/matematiske headings; fagligt indhold og PDF-generation er ikke påvirket.
