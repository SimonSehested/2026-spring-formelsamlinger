# Coverage Report: samlet dansk formelsamling

## Kilder

- Primær base: `sources_da/` og `main_da.tex`.
- Kontrolrapporter: `reports/full_input_coverage_audit.md`, `reports/exam_task_taxonomy.md`, `reports/exam_verification_report_da.md`, `reports/coverage_report_da.md`.
- Sekundære sammenligningskilder: `S-LS formelsamling.pdf`, `Continuous_time_signals_and_linear_systems-7.pdf`, `main.pdf`, `main_da.pdf`.
- Inputmateriale: 3 eksamens-PDF'er i `input/exams/` og 13 forelæsnings-PDF'er i `input/lectures/`.

## Outputstruktur

| Fil | Formål |
|---|---|
| `main_combined_da.tex` | Separat dansk hovedfil med symbolregister efter indholdsfortegnelse |
| `symbolindex.ist` | Makeindex-style til automatisk symboloversigt |
| `sources_combined_da/00_start_her.tex` | Metodefinder og MCQ-startregler |
| `sources_combined_da/01_symboler_og_signaler.tex` | Symbol-, enheds-, Hz/rad/s- og grundsignalregler |
| `sources_combined_da/02_ltic_tidsdomaene.tex` | LTIC, kredsløb, respons, foldning og anden orden |
| `sources_combined_da/03_fourier.tex` | Fourierrække, Fouriertransformation og Fourier-MCQ-regler |
| `sources_combined_da/04_laplace.tex` | Ensidig Laplace, responsopdeling, invers Laplace og værdisætninger |
| `sources_combined_da/05_bode_filtre_butterworth.tex` | Bode, pol-nul, filterklassifikation, Butterworth og Sallen-Key |
| `sources_combined_da/06_sampling_adc_inamp.tex` | Sampling, ADC, anti-aliasing og instrumenteringsforstærker |
| `sources_combined_da/99_python_hjaelpere.tex` | Fuldt scriptopslag med manuelle kontrolkrav |

## Indholdsvalg

- Den samlede version er dansk og separat, så `main_da.tex` og `sources_da/` bevares.
- Den tidligere duplikering af elementære signaler er samlet i et nyt symbol- og signalmodul.
- Der er tilføjet flere korte forklaringer af symboler, enheder, brugskrav, hurtigtjek og typiske fælder direkte efter centrale formler.
- Python-hjælpere er bevaret fuldt, men formuleret som sekundære regnehjælpemidler efter manuel opgavetype- og antagelsestjek.

## Symbolregister

- Automatisk register er implementeret med `makeidx` og `symbolindex.ist`.
- Symboloversigten står lige efter indholdsfortegnelsen.
- Tabellen indeholder symbol, dansk betydning, enhed og genererede sidehenvisninger.
- Aktuel build genererer 62 symbolmarkeringer.

## Tilbagevendende opgavetyper

De rapporterede opgavetyper er dækket:

- LTIC-klassifikation
- kredsløbsligning og impedansgrænsetjek
- impuls-, trin- og ramperespons
- foldning og støtteintervaller
- Fourierrækker og Fouriertransformegenskaber
- ensidig Laplace, partialbrøker, egenrespons og nul-start-respons
- andenordenssystemer, overshoot, \(Q\), poler og sensitivitet
- Bodeplot, pol-nul-diagrammer og filtertype
- Butterworth-orden, poler, Sallen-Key og RC-skalering
- sampling, aliasering, ADC, anti-aliasing og CMRR

## Kendte usikkerheder

- Kredsløbs- og plotopgaver kræver stadig manuel billedfortolkning fra eksamen.
- Symboler med samme notation i forskellige kontekster, fx \(n\) og \(\omega_c\), kan optræde med kontekstafhængig betydning; dette er markeret i symboloversigten.
- MiKTeX skriver en miljøadvarsel om manglende update-check, men LaTeX-buildet gennemføres uden fejl.

## Buildstatus

Kørt og bestået:

```text
pdflatex -interaction=nonstopmode -halt-on-error main_combined_da.tex
makeindex -s symbolindex.ist -o main_combined_da.ind main_combined_da.idx
pdflatex -interaction=nonstopmode -halt-on-error main_combined_da.tex
pdflatex -interaction=nonstopmode -halt-on-error main_combined_da.tex
```

Resultat: `main_combined_da.pdf`, 19 sider, bygger uden LaTeX-fejl. Resterende logmeldinger er underfull hbox warnings og MiKTeX update-advarsel.
