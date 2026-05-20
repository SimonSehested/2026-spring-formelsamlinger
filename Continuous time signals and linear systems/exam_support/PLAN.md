# PLAN.md

Byg en separat, samlet dansk eksamensformelsamling for 22050 Signaler og lineære systemer i kontinuert tid.

## Fase 1: Fastlæg kilder

- Læs `reports/full_input_coverage_audit.md`, `reports/exam_task_taxonomy.md`, `reports/exam_verification_report_da.md` og `reports/coverage_report_da.md`.
- Brug `sources_da/` som primær base.
- Brug de eksisterende PDF-formelsamlinger i roden som sekundære inputkilder.
- Brug eksamener og forelæsninger i `input/` til kontrol, ikke til ukritisk at fylde dokumentet.

## Fase 2: Opdater styrende dokumenter

Opdater:

- `AGENTS.md`
- `PLAN.md`
- `style_guide.md`
- `verification_guide.md`

De skal kræve dansk, hurtig eksamensbrug, alle symboler forklaret, alle ligninger forklaret, sandt/falsk-regler og automatisk symboloversigt med sidehenvisninger.

## Fase 3: Opret separat samlet LaTeX-struktur

Opret:

- `main_combined_da.tex`
- `sources_combined_da/00_start_her.tex`
- `sources_combined_da/01_symboler_og_signaler.tex`
- `sources_combined_da/02_ltic_tidsdomaene.tex`
- `sources_combined_da/03_fourier.tex`
- `sources_combined_da/04_laplace.tex`
- `sources_combined_da/05_bode_filtre_butterworth.tex`
- `sources_combined_da/06_sampling_adc_inamp.tex`
- `sources_combined_da/99_python_hjaelpere.tex`

Bevar modularitet. Hovedfilen skal kun indeholde præambel, symbolregisteropsætning, indholdsfortegnelse og `\input`.

## Fase 4: Symboloversigt

- Tilføj automatisk symbolregistrering.
- Symboloversigten skal stå lige efter indholdsfortegnelsen.
- Hver række skal have symbol, navn/betydning, enhed og sider.
- Markér centrale symboler i teksten, så sidenumre genereres automatisk.

## Fase 5: Skriv eksamensrettet indhold

For hvert emne:

- behold kun eksamensrelevant stof
- forklar alle symboler i formler
- forklar alle ligninger med praktisk brug
- tilføj hurtige regler for sandt/falsk
- tilføj typiske fælder
- tilføj 3-7 trins opskrifter for tilbagevendende opgaver
- brug danske forklaringer og engelske søgealiaser hvor nyttigt

Dokumentet skal hjælpe en svag studerende med at vælge metode hurtigt.

## Fase 6: Python-hjælpere

- Behold fulde Python-henvisninger.
- Gør det tydeligt, hvornår scripts må bruges, og hvornår de ikke må bruges.
- Scripts må aldrig erstatte de manuelle eksamensregler.

## Fase 7: Verifikation

Opret/opdater:

- `reports/coverage_report_combined_da.md`
- `reports/exam_verification_report_combined_da.md`

Kontrollér alle opgavetyper fra rapporterne:

- problemtype
- hurtig metode
- dækkende sektion
- symbolforklaring
- sandt/falsk-regel
- manglende opskrift

## Fase 8: Build

Kør:

- LaTeX compile
- symbolindeks-buildtrin
- LaTeX compile igen indtil sidehenvisninger er stabile

Ret:

- compile errors
- manglende inputfiler
- undefined references
- brudt matematik
- manglende symbolregister

## Stopkriterium

Opgaven er færdig, når:

- `main_combined_da.pdf` bygger uden fejl
- symboloversigten har sidehenvisninger
- rapporterne dokumenterer dækning
- indholdet er kort, dansk, søgbart og eksamensorienteret
