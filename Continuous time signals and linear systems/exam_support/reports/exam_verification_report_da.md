# Dansk Exam Verification Report

## Verifikationsstatus

Den danske formelsamling er en parallel oversættelse af den eksisterende eksamensverificerede samling. Dækningen er derfor tilsigtet identisk med `reports/exam_verification_report.md`.

## Dækningsmapping

| Kilde | Problemtyper | Dækket i dansk version | Mangler? | Risiko |
|---|---|---|---|---|
| 2023 trial | LTIC, kredsløb, impuls/trin, foldning, Fourier, Laplace, Bode, filtre | `sources_da/01` til `sources_da/04` | Nej | Lav til middel |
| August 2024 | Klassifikation, kredsløb, Fourier, Laplace, anden orden, filtre, ADC | `sources_da/01` til `sources_da/05` | Nej | Lav til middel |
| Maj 2025 | Kredsløb, ODE, respons, Fourier, Laplace, frekvensrespons, Butterworth, in-amp, sampling | `sources_da/01` til `sources_da/05` | Nej | Lav til middel |

## Kontrolpunkter

- Alle eksisterende emner og script-henvisninger er repræsenteret i dansk version.
- Formler, notation og Python-funktionsnavne er bevaret for at undgå oversættelsesfejl.
- Sproget er primært dansk med få engelske søgealiaser for eksamensmatch.
- Den danske version har nu en indledende metodefinder og flere opgavetypeopskrifter, så søgning på eksamensord ikke kun finder formler, men også en kort fremgangsmåde.

## Brugbarhedsverifikation

Følgende stuck-student-scenarier er nu dækket med direkte søgbare opskrifter:

| Søgning | Forventet hjælp i dokumentet |
|---|---|
| `hvad skal jeg gøre`, `vælg opgavetype`, `start her` | Metodefinder fra opgaveord til startmetode |
| `klassificer`, `lineær`, `kausal`, `stabil` | Systemklassifikationsopskrift |
| `differentialligning`, `transferfunktion` | ODE til \(H(s)\)-opskrift |
| `impulsrespons`, `trinrespons`, `ramperespons` | Inputvalg og Laplace-arbejdsgang |
| `Fourierrække`, `Fouriertransformation` | Valg mellem \(D_n\) og \(X(\omega)\) |
| `Bodeplot`, `pol-nul`, `filtertype` | Hældnings-, grænse- og faseopskrifter |
| `Butterworth`, `Sallen-Key` | Orden, polvalg og komponentmatch |
| `sampling`, `ADC`, `CMRR` | Alias-, LSB- og instrumenteringsopskrifter |

## Resterende risiko

De samme risici som i den engelske/mixede version gælder: billedbaserede kredsløbsdiagrammer og grafiske matchopgaver kræver stadig manuel fortolkning.

## Fuld audit-opdatering

`reports/full_input_coverage_audit.md` er tilføjet som problem-for-problem- og forelæsning-for-forelæsning-audit mod alle PDF'er i `input/`.

Auditten fandt nogle svage punkter, som nu er rettet i både `sources/` og `sources_da/`:

- 2023 Q19: sensitivitetsformler for underdæmpede polkoordinater.
- 2023 Q20 / 2024 Q18 / 2025 Q18: tydeligere Sallen-Key matchregler for lav \(Q\)-følsomhed.
- 2025 Q17: pol-nul fasefælde for spejlede venstre/højre halvplansnulpunkter.
- 2025 Q18: Butterworth \(H(s)H(-s)\), kausal/antikausal fortolkning.
