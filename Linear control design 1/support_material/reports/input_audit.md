# Inputaudit: Linear Control Design 1

## Identifikation

- Kursus: `34721/34722 Linear Control Design 1`, DTU Electro, Spring Semester 2026.
- Undervisere: Silvia Tolu og Dimitrios Papageorgiou.
- Dokumenteret eksamensformat: 4-timers skriftlig eksamen suppleret af rapport om sidste assignment (`1_Welcome_Lecture.pdf`).
- Observeret opgavestil: multiple choice med beregning, diagramfortolkning og controllerdesign (`Exam_S20.pdf`, `F21.pdf`, `EXAMS_LCD1_2022_no_answerS.pdf`, `eksamenssættet23.pdf`, `F25.pdf`).
- Tilladte hjælpemidler og brug af Python til eksamen: ikke dokumenteret i inputmaterialet.
- Kildeprioritet: eksamenssæt med svar, officiel eksamensoriginal, forelæsningsslides.

## Kilderegister

Alle PDF'er blev tekstudtrukket med `pdftotext -layout -enc UTF-8`; samtlige gav brugbart tekstoutput. Figurer og grafiske ligninger kræver fortsat visuel kontrol ved præcis aflæsning.

| Kilde | Type | Rolle | Kvalitet | Bruges til | Usikkerheder |
| ----- | ---- | ----- | -------- | ---------- | ------------ |
| `input/exams/Exam_S20.pdf` (20 s.) | Eksamen med løsningsnoter | Primær eksamenskilde | Middel; mange figurer/udregninger er grafiske, men løsningen er læsbar | S20 Q1-Q19, design-/stabilitetsmetoder og sensitivity | Q1-Q15 kræver original PDF for præcise figurtal/svarmuligheder |
| `input/exams/F21.pdf` (28 s.) | Eksamen med svar | Primær eksamenskilde | God tekst; figurer findes | Q1-Q20, facit og metoder | Enkelt formel-/figurlayout er OCR-fragmenteret |
| `input/exams/EXAM_LCD1_F21_Part1_no_answers.pdf` (14 s.) | Officiel questionnaire | Kontrolkilde for F21 Q1-Q10 | God tekst; figurer findes | Kontrollere F21 del 1-ordlyd | Ikke separat eksamenssæt; ingen svar |
| `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf` (11 s.) | Officiel questionnaire | Kontrolkilde for F21 Q11-Q20 | God tekst; figurer findes | Kontrollere ordlyd og dato | Ikke separat eksamenssæt; ingen svar |
| `input/exams/EXAMS_LCD1_2022_no_answerS.pdf` (24 s.) | Eksamen uden svar / sammensat questionnaire | Primær opgavetypekilde | Middel; tekstlaget starter ved 2022 Q2 og mangler brugbar Q1/Q10; senere sider indeholder Questions 11-20 fra en questionnaire dateret 2024 | 2022 Q2-Q9 og Q11-Q20 som metode-/coveragekilde | Ingen markerede svar; Q1/Q10 skal visuelt kontrolleres |
| `input/exams/eksamenssættet23.pdf` (16 s.) | Eksamen med markerede svar | Primær eksamenskilde | God tekst; markerede svar er bevaret; figurer kræver original PDF | E23 Q1-Q20, facit og opgavetyper | Bode-/stepfigurer kræver visuel aflæsning |
| `input/exams/F25.pdf` (20 s.) | Eksamen med markerede svar | Primær eksamenskilde | God tekst; figurer findes | Q1-Q20, nye opgavetyper og facit | Figurbaserede Bode/Nyquist/blokdiagrammer kræver original PDF |
| `input/lectures/1_Welcome_Lecture.pdf` (22 s.) | Forelæsning 1 | Kursus-/eksamensramme | God | Kursusmål, format, PID-overblik | Ingen hjælpemiddelregel angivet |
| `input/lectures/2_block_control_concept.pdf` (55 s.) | Forelæsning 2 | Pensum | God; mange diagrammer | Blokdiagrammer, feedback, motor, håndtuning | Diagramalgebra bør aflæses visuelt i konkrete opgaver |
| `input/lectures/3_Laplace_TF.pdf` (46 s.) | Forelæsning 3 | Pensum | Middel/god | PID, Laplace, transferfunktion | Indlejrede boguddrag giver ujævnt tekstflow |
| `input/lectures/4_Frequency_and_Time_Analysis_WSol.pdf` (45 s.) | Forelæsning 4 | Pensum med øvelsessvar | God | DC gain, poler/nulpunkter, 1./2. orden | Plotbaserede værdier er visuelle |
| `input/lectures/5_Modelling.pdf` (32 s.) | Forelæsning 5 | Pensum | God | White/grey/black box, linearisering | Matlab-datafiler medfølger ikke |
| `input/lectures/6_Bode_plot&Stability.pdf` (53 s.) | Forelæsning 6 | Pensum | God; plotintensiv | Bode, marginer, minimum phase | Kurveaflæsning kræver figur |
| `input/lectures/Lecture_07_Nyquist plot and stability.pdf` (25 s.) | Forelæsning 7 | Pensum | God; plotintensiv | Nyquist, encirclements, marginer | Retning/antal aflæses visuelt |
| `input/lectures/Lecture_08_PI_LEAD_design.pdf` (34 s.) | Forelæsning 8 | Pensum | Middel/god | P, PI, PI-Lead design | Flere formler ligger grafisk, rekonstrueret med standardnotation |
| `input/lectures/Lecture_09_PI_LEAD_design_specifications.pdf` (28 s.) | Forelæsning 9 | Pensum | Middel/god | Tidsspecifikationer, bandwidth, type-n | Formeltabel er delvist grafisk |
| `input/lectures/Lecture_10_Unstable_systems (1).pdf` (25 s.) | Forelæsning 10 | Pensum | God | Ustabile systemer, stabilisering | Assignment-arkitektur er ikke eksamensfacit |
| `input/lectures/Lecture_11_Limited_systems (1).pdf` (33 s.) | Forelæsning 11 | Pensum | God | Rate/saturation, windup, Lag | Simulationsresultater ikke reproducerbare uden `.m`-filer |
| `input/lectures/Lecture_12_Disturbances_sensitivity_prefilters.pdf` (26 s.) | Forelæsning 12 | Pensum | God; diagrammer | Disturbance paths, sensitivity, prefilter | Blokdiagramtegn bestemmer fortegn |
| `input/lectures/Lecture_13_Feed_forward.pdf` (23 s.) | Forelæsning 13 | Pensum | God; diagrammer | Reference/disturbance feed-forward | Fortegn og plant path skal aflæses fra opgaven |

## Relationer og mangler

- `Exam_S20.pdf`, `F21.pdf`, `eksamenssættet23.pdf` og `F25.pdf` er primære eksamenssæt med facit/markerede svar, bortset fra at S20 kun viser Q1-Q19 i tekstlaget.
- `EXAMS_LCD1_2022_no_answerS.pdf` bruges som opgavetypekilde uden facit; Q1 og Q10 er ikke brugbart tekstudtrukket.
- F21-del-1- og del-2-filerne gentager F21 uden svar og er kontrolkilder, ikke separate sæt.
- Der findes ingen separate øvelsesark, Matlab-scripts, datasæt eller officielle regler om hjælpemidler i `input/`.
- Forelæsningerne refererer til Matlab/Simulink og `.m`-eksempler, men filerne er ikke inkluderet. Python-værktøjer kan derfor valideres matematisk, ikke mod original kode.
- Et historisk genereret dokumenttræ var slettet i git-worktree ved arbejdets start. Det behandles ikke som kilde.

## OCR- og figurforbehold

- Tekstbaserede definitioner, multiple-choice-ordlyd og svar forklares pålideligt af udtrækket.
- Bode-, Nyquist-, blokdiagram- og responsfigurer skal bruges med den originale PDF ved numerisk grafaflæsning.
- Symboler som `gamma_M`, `omega_c`, `tau_i`, `tau_d` og `alpha` er normaliseret i rapporterne, fordi nogle græske tegn/formler mistes i tekstlaget.
