# Verification Guide

Verificér den samlede danske formelsamling mod eksamensopgavetyperne og rapporterne.

## Primære kontrolkilder

- `reports/full_input_coverage_audit.md`
- `reports/exam_task_taxonomy.md`
- `reports/exam_verification_report_da.md`
- `reports/coverage_report_da.md`
- eksamens-PDF'er i `input/exams/`

## Verifikationsspørgsmål

For hver opgavetype skal du kontrollere:

1. Kan en studerende finde opgavetypen med Ctrl+F?
2. Findes den nødvendige formel eller beslutningsregel?
3. Er alle symboler i formlen forklaret?
4. Er relevante enheder angivet?
5. Findes et hurtigt sandt/falsk- eller plausibilitetstjek?
6. Findes en typisk fælde, hvis opgavetypen ofte afgøres af en fælde?
7. Kan metoden realistisk bruges på cirka 4 minutter?

## Rapportformat

Opret/opdater `reports/exam_verification_report_combined_da.md` med:

| Kilde | Problem/opgavetype | Hurtig metode | Dækket i sektion | Symboler forklaret? | Sandt/falsk-regel? | Mangler? |
|---|---|---|---|---|---|---|

Opret/opdater `reports/coverage_report_combined_da.md` med:

- anvendte kilder
- outputstruktur
- symbolregisterstatus
- tilbagevendende opgavetyper
- kendte usikkerheder
- buildstatus

## Buildkontrol

Den endelige PDF skal bygges med:

- LaTeX
- symbolindeks-buildtrin
- LaTeX igen til sidehenvisninger er stabile

Kontrollér:

- ingen compile errors
- ingen manglende inputfiler
- symboloversigt står efter indholdsfortegnelsen
- symboloversigt har sidehenvisninger
- hovedfilen inputter alle moduler
- dokumentet er dansk, kort og eksamensrettet

## Regler

- Løs ikke hele eksamener, medmindre det er nødvendigt for at afgøre dækning.
- Tilføj ikke stof kun for at gøre dokumentet længere.
- Hvis en manglende regel er nødvendig for flere opgaver, tilføj den som kompakt opskrift.
- Hvis en formel tilføjes primært på grund af eksamensdækning, markér den med:

```tex
% Added from exam coverage
```
