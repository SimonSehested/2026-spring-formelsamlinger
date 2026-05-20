# Dansk Coverage Report

## Kursus og kilder

- Kursus: 22050 Signaler og lineære systemer i kontinuert tid.
- Dansk version er en parallel formelsamling baseret på den eksisterende verificerede samling i `sources/`.
- Kildemateriale og rapporter er uændrede: eksamener i `input/exams/`, forelæsninger i `input/lectures/`, samt eksisterende coverage- og eksamensverifikationsrapporter.

## Dansk outputstruktur

| Fil | Formål |
|---|---|
| `main_da.tex` | Dansk PDF-shell og inputrækkefølge |
| `sources_da/00_hvis_du_sidder_fast.tex` | Metodefinder til studerende, der ikke ved hvilken opgavetype de sidder med |
| `sources_da/01_ltic_time_domain.tex` | LTIC, kredsløb, foldning og andenordens tidsdomæne |
| `sources_da/02_fourier.tex` | Fourierrækker og Fourier-transformation |
| `sources_da/03_laplace.tex` | Ensidig Laplace, egenrespons/nul-start-respons og invers transformation |
| `sources_da/04_frequency_bode_filters.tex` | Frekvensrespons, Bodeplot, pol-nul, filtre og Butterworth |
| `sources_da/05_sampling_adc_inamp.tex` | Sampling, ADC, anti-aliasing og instrumenteringsforstærker |
| `sources_da/99_python_script_index.tex` | Dansk scriptopslag |

## Oversættelsesprincipper

- Brødtekst, recipes, checks og fælder er oversat til dansk.
- Notation, formler, filstier, funktionsnavne og koefficientrækkefølger er bevaret uændret.
- Engelske aliases er kun bevaret, hvor de er nyttige til Ctrl+F eller matcher kursus-/eksamensord.
- Den danske version har nu et ekstra brugbarhedslag med metodefinder og flere korte eksamensopskrifter. Det er en pædagogisk udvidelse af arbejdsmetoden, ikke en teorimæssig udvidelse af pensum.

## Stuck-student usability

Den danske version er forbedret med henblik på en studerende, der sidder fast og ikke ved, hvilken formel eller metode der skal bruges:

- `sources_da/00_hvis_du_sidder_fast.tex` giver en hurtig tabel fra opgaveord til startmetode.
- De faglige moduler indeholder flere `Brug når`-, `Trin`-, `Hvis du er i tvivl`-, `Hurtigtjek`- og `Typiske fælder`-blokke.
- Opskrifterne er bevidst korte og handlingsorienterede; beviser og lange teoriforklaringer er fortsat udeladt.

## Kendte usikkerheder

- Kredsløbsdiagrammer i PDF-kilderne er billedbaserede; den danske samling bevarer generelle KCL-/impedansregler frem for at reproducere diagrammer.
- Grafisk match af Bodeplot, trinrespons og pol-nul-diagrammer kræver stadig visuel fortolkning.
- Ingen selvstændige officielle løsningssæt er tilføjet; den danske version arver valideringen fra den eksisterende samling.

## Fuld audit

En strengere audit findes i `reports/full_input_coverage_audit.md`. Den gennemgår alle 60 eksamensopgaver og forelæsningerne L01-L13. Audit-forbedringerne er indarbejdet i både dansk og engelsk/mixet version:

- sensitivitet for underdæmpede polkoordinater,
- pol-nul fasefælder,
- Butterworth kausal/antikausal polopdeling,
- Sallen-Key lavpas/højpas matchregler.
