# Final review report

## Leverancer

Eksamenspakken er opdateret for de nye eksamensfiler i `support_material/input/exams`,
og slidepensum fra alle 13 forelæsnings-PDF'er er auditeret mod `lcd.pdf`. Der findes
analyser for S20, F21, 2022, E23 og F25, og `full_curriculum_report.md` dokumenterer nu
de ekstra slide-emner, der blev føjet til formelsamlingen.

## LaTeX build

- Kommando: `pdflatex -jobname=lcd -interaction=nonstopmode -halt-on-error support_material\main.tex`.
- Resultat: bestået; kommandoen blev kørt to gange for referencer.
- Output: `lcd.pdf`, A4, 16 sider, 582655 bytes.
- Ikke-fatale advarsler: overfull/underfull boxes ved lange funktionsnavne og hyperref-bookmarkwarnings for matematik i overskrifter; ingen buildstop.
- PDF-tekstkontrol fandt de tidligere eksamensnøgleord samt de nye slidepensumord:
  `REGBOT`, `black-box`, `grey-box`, `lineariser`, `Jacobian`, `dominerende pol`,
  `rate limiter`, `delay`, `non-minimum`, `cascaded` og `Pad`.

## Python validation

- Kommando: `python -m compileall -q support_material\scripts`.
- Resultat: bestået.
- Første kommando fra repo-roden `python -m support_material.scripts.validate_scripts` fejlede på importstien, fordi scriptet importerer `scripts.control`.
- Korrekt kommando: `python -m scripts.validate_scripts` kørt fra `support_material`.
- Resultat: bestået med `Validated 37 checks.`
- Der blev ikke tilføjet nye Python-funktioner i denne slide-audit; de manglende emner
  er metode- og fortolkningsstof, ikke nye beregnings-API'er.

## Kvalitetstjek

| Krav | Status | Dokumentation |
| ---- | ------ | ------------- |
| Alle inputfiler auditeret | Opfyldt | `input_audit.md` dækker S20, F21, 2022, E23 og F25 samt F21-kontrolfiler |
| Analyse pr. eksamenssæt | Opfyldt | `exam_set_analyses/S20.md`, `F21.md`, `2022.md`, `E23.md`, `F25.md` |
| Ingen synlig eksamensopgave sprunget over | Opfyldt med forbehold | 2022 Q1/Q10 er markeret som ikke brugbart tekstudtrukket |
| Merged task taxonomy | Opfyldt | `merged_task_taxonomy.md` |
| Notesektioner opdateret | Opfyldt | Model/tid, feedback/fejl, controllerdesign og disturbance/feed-forward er udbygget |
| Slidepensum dækket | Opfyldt | White/grey/black-box, linearisering, dominerende poler, delay, RHP-zero, rate limiter, REGBOT/kaskade |
| Python-kandidater vurderet | Opfyldt | `script_inventory.md` og `python_coverage_report.md` forklarer accepterede/afviste kandidater |
| Scripts importbare og testet | Opfyldt | 37 beståede checks |
| Alle eksamensopgaver mappet til noter | Opfyldt | `exam_verification_report.md` |
| PDF bygget | Opfyldt | `lcd.pdf` |

## Kendte begrænsninger og manuelle reviewpunkter

- `EXAMS_LCD1_2022_no_answerS.pdf` er uden facit og har ikke brugbart tekstudtræk for Q1/Q10. De to spørgsmål skal visuelt kontrolleres i original PDF, hvis fuld 2022-facitdækning ønskes.
- Bode-, Nyquist-, steprespons- og blokdiagramfigurer kræver fortsat manuel aflæsning i original PDF ved præcise svarvalg.
- Grafiske REGBOT-arkitekturer og Simulink-diagrammer er dækket metodisk, men ikke
  billedkopieret ind i formelsamlingen.
- Hjælpemiddelregler og tilladelse til Python er ikke dokumenteret i inputmaterialet.
- Notebooken og scripts er ikke ændret, fordi de nye opgavetyper ikke retfærdiggør nye API'er.

## Konklusion

Stopkriterierne er opfyldt for alle brugbart udtrukne eksamensopgaver og for de faglige
slide-emner i forelæsning 1-13. Den eneste åbne kildebegrænsning er 2022 Q1/Q10, som
ikke kan analyseres sikkert fra tekstlaget alene.
