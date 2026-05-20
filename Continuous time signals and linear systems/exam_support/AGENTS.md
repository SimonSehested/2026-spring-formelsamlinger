# AGENTS.md

Du bygger en dansk, eksamensrettet LaTeX-formelsamling for 22050 Signaler og lineære systemer i kontinuert tid.

## Hovedmål

Formelsamlingen skal hjælpe en studerende, der forstår meget lidt af faget, med at svare hurtigt og rigtigt på eksamensdelopgaver.

Eksamen antages ud fra projektets rapporter at være hårdt tidsstyret:

- cirka 4 minutter per delopgave
- beståelseskrav omkring 80% rigtige delopgaver
- mange opgaver kræver sandt/falsk-, multiple-choice- eller one-best-answer-logik

Dokumentet skal derfor være en Ctrl+F-problemløser, ikke et kompendium.

## Kilder og prioritet

Brug projektets faktiske materiale:

- `input/exams/`
- `input/lectures/`
- eksisterende formelsamlinger i projektroden
- `sources_da/`
- `sources/`
- alle relevante rapporter i `reports/`

Rapporterne styrer udvælgelsen. Især:

- `reports/full_input_coverage_audit.md`
- `reports/exam_task_taxonomy.md`
- `reports/exam_verification_report_da.md`
- `reports/coverage_report_da.md`

Indarbejd kun materiale, der understøtter eksamensopgavetyper, forelæsningsstof der faktisk bruges til opgaver, eller nødvendige standardforudsætninger. Udelad teori, der ikke hjælper en eksamensbeslutning.

Hvis noget er usikkert, markér det i LaTeX med:

```tex
% TODO: verify from source
```

## Output

Den samlede danske version skal være separat:

- `main_combined_da.tex`
- `sources_combined_da/*.tex`

Overskriv ikke `main_da.tex` eller `sources_da/` medmindre brugeren eksplicit beder om det.

Brug modulariserede `.tex`-filer. Skriv ikke store mængder indhold direkte i hovedfilen.

## Obligatorisk symboloversigt

Efter indholdsfortegnelsen skal der være en symboloversigt på dansk med:

- symbol
- navn/betydning
- enhed
- sidehenvisninger

Symboloversigten skal genereres automatisk med LaTeX-indeks/buildtrin, så siderne følger dokumentet efter compile. Alle centrale symboler, der bruges i formler, skal forklares mindst én gang.

## Formelkrav

Hver vigtig ligning skal have kort forklaring:

- hvad den bruges til
- hvad alle symboler betyder
- enhed for relevante fysiske størrelser
- betingelser for at bruge den
- hurtig kontrol
- typisk fælde

Forklaringen skal være kort og praktisk. Undgå beviser og lange udledninger.

## Eksamenstil

Prioritér:

- metodefinder
- korte opskrifter
- genkendelsesregler
- sandt/falsk-regler
- grænsetjek
- enhedstjek
- stabilitets-, kausalitets- og nul-begyndelsesbetingelsesfælder
- Hz vs rad/s
- checks for om et generelt udsagn kun gælder under ekstra antagelser

Hver tilbagevendende opgavetype skal have en søgbar opskrift med 3-7 trin.

## Stil

Skriv på dansk. Bevar engelske aliaser i overskrifter, når de er nyttige for Ctrl+F eller matcher eksamensord.

Brug:

- kompakte tabeller
- korte punktopstillinger
- display-math
- tydelige overskrifter
- `Brug når`, `Symboler`, `Enheder`, `Hurtigtjek`, `Typiske fælder`

Undgå:

- lange afsnit
- historik
- motivation
- beviser
- forelæsningsnotestil
- dubletter uden eksamensværdi
- usupporterede emner

## Verifikation

Efter ændringer skal dokumentet bygges og verificeres mod rapporterne.

Opret/opdater:

- `reports/coverage_report_combined_da.md`
- `reports/exam_verification_report_combined_da.md`

For hver opgavetype skal rapporten vise, at den nye samling har:

- søgbar opgavetype
- relevant formel/metode
- symbolforklaring
- hurtig sandt/falsk-regel eller plausibilitetstjek
- ingen kendt manglende opskrift

Dokumentet er først færdigt, når LaTeX bygger uden fejl, og sidehenvisninger i symboloversigten er genereret.
