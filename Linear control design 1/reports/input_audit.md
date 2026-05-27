# Inputaudit: Linear Control Design 1

## Identifikation

- Kursus: `34721/34722 Linear Control Design 1`, DTU Electro, Spring Semester 2026.
- Undervisere: Silvia Tolu og Dimitrios Papageorgiou.
- Dokumenteret eksamensformat: 4-timers skriftlig eksamen suppleret af rapport om sidste assignment (`1_Welcome_Lecture.pdf`).
- Observeret opgavestil: multiple choice med beregning, diagramfortolkning og controllerdesign (`F21.pdf`).
- Tilladte hjælpemidler og brug af Python til eksamen: ikke dokumenteret i inputmaterialet.
- Kildeprioritet: eksamenssæt med svar, officiel eksamensoriginal, forelæsningsslides.

## Kilderegister

Alle PDF'er blev tekstudtrukket med `pdftotext -layout -enc UTF-8`; samtlige gav brugbart tekstoutput. Figurer og grafiske ligninger kræver fortsat visuel kontrol ved præcis aflæsning.

| Kilde | Type | Rolle | Kvalitet | Bruges til | Usikkerheder |
| ----- | ---- | ----- | -------- | ---------- | ------------ |
| `input/exams/F21.pdf` (28 s.) | Eksamen med svar | Primær eksamenskilde | God tekst; figurer findes | Q1-Q20, facit og metoder | Enkelt formel-/figurlayout er OCR-fragmenteret |
| `input/exams/Exam_F21_LCD1 Part 2 - no answers.pdf` (11 s.) | Officiel questionnaire | Kontrolkilde for F21 Q11-Q20 | God tekst; figurer findes | Kontrollere ordlyd og dato | Ikke separat eksamenssæt; ingen svar |
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

- De to eksamens-PDF'er er ikke to forskellige eksamenssæt: del-2-filen gentager Q11-Q20 fra F21 uden svar og er dateret 6. maj 2026, mens `F21.pdf` leverer Q1-Q20 med svar/solutions.
- Der findes ingen separate øvelsesark, Matlab-scripts, datasæt eller officielle regler om hjælpemidler i `input/`.
- Forelæsningerne refererer til Matlab/Simulink og `.m`-eksempler, men filerne er ikke inkluderet. Python-værktøjer kan derfor valideres matematisk, ikke mod original kode.
- Et historisk genereret dokumenttræ var slettet i git-worktree ved arbejdets start. Det behandles ikke som kilde.

## OCR- og figurforbehold

- Tekstbaserede definitioner, multiple-choice-ordlyd og svar forklares pålideligt af udtrækket.
- Bode-, Nyquist-, blokdiagram- og responsfigurer skal bruges med den originale PDF ved numerisk grafaflæsning.
- Symboler som `gamma_M`, `omega_c`, `tau_i`, `tau_d` og `alpha` er normaliseret i rapporterne, fordi nogle græske tegn/formler mistes i tekstlaget.
