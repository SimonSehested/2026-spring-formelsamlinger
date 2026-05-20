# Exam Verification Report: samlet dansk formelsamling

## Verifikationsstatus

Den samlede danske formelsamling bygger på den tidligere danske version og er kontrolleret mod `reports/full_input_coverage_audit.md` og `reports/exam_task_taxonomy.md`.

Målet er ikke at løse alle eksamensopgaver fuldt, men at sikre at hver tilbagevendende opgavetype har en hurtig søgbar metode, relevante formler, symbolforklaringer og sandt/falsk-tjek.

## Dækningsmapping

| Kilde | Problem/opgavetype | Hurtig metode | Dækket i sektion | Symboler forklaret? | Sandt/falsk-regel? | Mangler? |
|---|---|---|---|---|---|---|
| 2023/2024/2025 | LTIC-klassifikation | Test linearitet, tidsinvarians, kausalitet og BIBO | 3.1-3.2 | Ja | Ja | Nej |
| 2023/2024/2025 | Kredsløbsligninger | KCL, komponentlove, DC/HF-grænser | 3.4 | Ja | Ja | Kun billedfortolkning |
| 2023/2024/2025 | Impuls-, trin- og ramperespons | Find \(H(s)\), vælg \(X(s)\), invers Laplace | 3.5, 5.6 | Ja | Ja | Nej |
| 2023/2024/2025 | Foldning | Støtteinterval først, Laplace-produkt for kausale signaler | 3.6 | Ja | Ja | Nej |
| 2023/2024/2025 | Andenordenssystemer | Match nævner til \(\zeta,\omega_n,Q\), tjek poler | 3.7 | Ja | Ja | Nej |
| 2023/2024/2025 | Fourierrække | Find \(T_0\), vælg én periode, brug symmetri | 4.1, 4.3 | Ja | Ja | Nej |
| 2023/2024/2025 | Fouriertransformation | Brug kendt par og én egenskab ad gangen | 4.2-4.3 | Ja | Ja | Nej |
| 2023/2024/2025 | Laplace og ROC | Ensidig definition, afledningsregler, ROC | 5.1-5.2 | Ja | Ja | Nej |
| 2023/2024/2025 | Egenrespons/nul-start | Adskil begyndelsesbetingelser fra \(H(s)X(s)\) | 5.3 | Ja | Ja | Nej |
| 2023/2024/2025 | Invers Laplace | Faktoriser, partialbrøker, kendte inverse par | 5.4 | Ja | Ja | Nej |
| 2023/2024/2025 | Slutværdi/begyndelsesværdi | Tjek poler før slutværdisætning | 5.5 | Ja | Ja | Nej |
| 2023/2024/2025 | Bodeplot | Aflæs hældninger, knæk og fase | 6.1-6.2 | Ja | Ja | Kun grafisk aflæsning |
| 2023/2024/2025 | Pol-nul-filter | Størrelse som afstande, fase som vinkler | 6.3 | Ja | Ja | Kun diagramfortolkning |
| 2023/2024/2025 | Butterworth | Orden-ulighed, polvalg, kausal venstre halvplan | 6.5 | Ja | Ja | Nej |
| 2023/2024/2025 | Sallen-Key sensitivitet | Identificer topologi og brug kursusmatchregel | 6.5 | Ja | Ja | Nej |
| 2024/2025 | Sampling/aliasering | Brug Hz og fold ind i \([0,F_s/2]\) | 7.1 | Ja | Ja | Nej |
| 2024/2025 | ADC/LSB/dynamikområde | Beregn \(\Delta V_{\mathrm{LSB}}\), tjek konvention | 7.2 | Ja | Ja | Nej |
| 2024/2025 | Anti-aliasing + ADC | Sæt filtreret amplitude under LSB | 7.3 | Ja | Ja | Nej |
| 2025 | Instrumenteringsforstærker | Beregn \(G_d,G_c,CMRR\) | 7.4 | Ja | Ja | Kun kredsløbsmodelvalg |

## Brugbarhedstjek

- `00_start_her` giver direkte mapping fra eksamensord til metode.
- `01_symboler_og_signaler` forklarer notation, enheder, Hz/rad/s og generel sandt/falsk-strategi.
- Hver hovedfamilie har mindst én kompakt opskrift eller tjekliste.
- Alle centrale formler har enten lokal symbolforklaring eller er dækket af symboloversigten.
- Kendte eksamensfælder fra auditten er bevaret: slutværdisætning på ustabile systemer, nul-start vs egenrespons, \(H(\omega)\) vs \(H(\jj\omega)\), \(f\) vs \(\omega\), spejlede RHP/LHP-nulpunkter, Butterworth \(H(s)H(-s)\), og Sallen-Key lavpas/højpas-matchregler.

## Resterende risiko

- Billedbaserede kredsløb og plots kan ikke gøres fuldt automatiske i en formelsamling; dokumentet giver reglerne, men brugeren skal stadig aflæse figuren.
- Ingen officielle løsningssæt er tilføjet, så rapporten følger den eksisterende audit og standardformler.

## Buildverifikation

`main_combined_da.pdf` er bygget med LaTeX + makeindex + to efterfølgende LaTeX-pass. Symboloversigten har sidehenvisninger og står efter indholdsfortegnelsen.
