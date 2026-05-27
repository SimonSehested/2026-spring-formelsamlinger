# Overdragelsesrapport: eksamensformelsamling og AI-blueprint

## Formaal og anvendelse

Denne rapport beskriver det strukturerede projekt i `exam_support/`: en dansk,
eksamensrettet formelsamling med tilhoerende Python-hjaelpere, kontrolrapporter
og AI-instruktioner for kurset **22050 Signaler og lineaere systemer i
kontinuert tid**.

Rapporten har to formaal:

1. At forklare, hvad der er bygget, hvordan delene haenger sammen, og hvilke
   kvalitetskrav projektet bruger.
2. At fungere som designgrundlag, naar en AI skal opbygge et tilsvarende
   projekt fra bunden for et nyt matematik- eller teknikfag.

Den praktiske AI-instruks til et nyt fag ligger separat i
`../MASTER_PROMPT_NEW_TECHNICAL_COURSE_DA.md`.

## Status og kildegrundlag

### Hvad rapporten daekker

Kun `exam_support/` behandles som den kanoniske projektmappe. Loese PDF'er,
notebooks og scripts i den overordnede mappe kan vaere arbejdskopier eller
senere eksperimenter og indgaar ikke i inventaret nedenfor.

Denne beskrivelse er baseret paa:

- styringsfilerne `AGENTS.md`, `PLAN.md`, `README_PROMPT.md`,
  `style_guide.md`, `script_guide.md`, `notes_scripts_integration.md`,
  `verification_guide.md` og `script_verification_guide.md`;
- LaTeX-hovedfilerne og modulerne i `sources*` og `sources_combined_da/`;
- Python-modulerne i `scripts/`;
- rapporterne i `reports/`;
- inputmaterialet i `input/`;
- den tilgaengelige git-historik.

### Dokumenterbar status

| Omraade                  | Dokumenteret indhold                                                  |
| ------------------------ | --------------------------------------------------------------------- |
| Input                    | 3 eksamens-PDF'er og 13 forelaesnings-PDF'er                          |
| Slutprodukt              | `main_combined_da.pdf`, rapporteret som 19 sider                      |
| Samlet dansk LaTeX       | `main_combined_da.tex` og 8 moduler i `sources_combined_da/`          |
| Symbolsystem             | `makeidx` og `symbolindex.ist`; rapporteret 62 symbolmarkeringer      |
| Python                   | 23 `.py`-filer under `scripts/`, inklusive pakke- og valideringsfiler |
| Rapporter foer denne fil | 13 Markdown-rapporter i `reports/`                                    |
| Afhaengigheder           | `numpy`, `sympy`, `scipy`, `pandas`, `matplotlib`                     |

Projektets eksisterende valideringsrapport angiver 27 validerede offentlige
hjaelpefunktioner og ingen fejlede funktioner efter koerte smoke checks.

### Snapshot-forbehold

Ved denne rapports udarbejdelse findes lokale, ikke-committede aendringer i
`scripts/lti/second_order.py` og `scripts/validate_scripts.py`. De udvider
blandt andet output og tests for andenordensberegninger. Derfor er
`reports/script_validation_report.md` autoritativ for den senest
dokumenterede valideringskoersel, men den beskriver ikke noedvendigvis alle
lokale udvidelser, foer validering og rapporter koeres/opdateres igen.

## Hvad projektet er

Projektet er ikke et almindeligt kompendium. Det er et eksamenssystem med tre
lag:

1. **Primaert lag: formelsamlingen.** En kort, soegbar PDF skal give formler,
   metodevalg, symbolforklaringer, hurtigtjek og faelder.
2. **Sekundaert lag: Python-vaerktoejskassen.** Importerbare funktioner skal
   beregne eller kontrollere gentagne, veldefinerede opgavetyper.
3. **Kontrollag: rapporter og builds.** Daekning, scriptvalg, validering,
   LaTeX-build og kendte begrænsninger dokumenteres eksplicit.

Det overordnede designprincip er, at Python aldrig erstatter den manuelle
beslutningsregel i noterne. En studerende skal kunne finde metoden i PDF'en
selv hvis Python ikke er tilgaengelig.

## Projektinventar

### Inputmateriale

```text
input/
  exams/       3 tidligere eksamener
  lectures/   13 forelaesnings-PDF'er
```

Eksamenerne bruges til at identificere tilbagevendende opgavetyper og
kontrollere daekning. Forelaesningerne bruges til notation, standardformler
og kursusspecifikke regler. Materialet fyldes ikke ukritisk ind i PDF'en.

### Styring og instruktioner

| Fil                            | Rolle                                                       |
| ------------------------------ | ----------------------------------------------------------- |
| `README_PROMPT.md`             | Oprindeligt prompt-kit og forventede outputs for AI-arbejde |
| `AGENTS.md`                    | Fagspecifikke krav til dansk eksamensformelsamling          |
| `PLAN.md`                      | Konkret byggeplan for den samlede danske version            |
| `style_guide.md`               | Stil- og LaTeX-regler                                       |
| `script_guide.md`              | Kriterier for at oprette, skrive og validere scripts        |
| `notes_scripts_integration.md` | Regler for kobling mellem noter og Python                   |
| `verification_guide.md`        | Kontrol mod eksamensopgavetyper og buildkrav                |
| `script_verification_guide.md` | Kontrolkrav for scriptvaerktoejskassen                      |

Filerne viser en arbejdsform, hvor AI'en foerst skal klassificere materialet,
derefter skrive selektivt og til sidst dokumentere, at resultatet faktisk
daekker eksamen og kan bygges/koeres.

### LaTeX og PDF-output

Projektet indeholder flere generationer af noter. Den mest komplette,
eksamensrettede danske leverance er:

```text
main_combined_da.tex
symbolindex.ist
sources_combined_da/
  00_start_her.tex
  01_symboler_og_signaler.tex
  02_ltic_tidsdomaene.tex
  03_fourier.tex
  04_laplace.tex
  05_bode_filtre_butterworth.tex
  06_sampling_adc_inamp.tex
  99_python_hjaelpere.tex
main_combined_da.pdf
```

`main_combined_da.tex` holder praembel, indholdsfortegnelse,
symbolregisteropsætning og `\input`-struktur samlet. Selve fagindholdet ligger
i moduler, saa emner kan revideres uden at ombygge hele dokumentet.

Symboloversigten placeres efter indholdsfortegnelsen og bygges med et
LaTeX-/makeindex-flow. Hver raekke kan angive symbol, betydning, enhed og
sider, hvilket goer PDF'en praktisk under tidspres.

### Python-vaerktoejskasse

Python-delen er organiseret efter opgavefamilie:

| Mappe/modul                   | Understoettet opgavefamilie                           |
| ----------------------------- | ----------------------------------------------------- |
| `scripts/lti/`                | LTIC-check, responsrelationer og andenordenssystemer  |
| `scripts/transforms/`         | Foldning og invers Laplace                            |
| `scripts/fourier/`            | Fourierrækker og udvalgte transformationsegenskaber   |
| `scripts/frequency/`          | Bodevaerdier og pol-/nulpunktrepræsentation           |
| `scripts/filters/`            | Butterworth-design og RC-frekvensskalering            |
| `scripts/sampling/`           | ADC-oploesning, aliasering og samplingkrav            |
| `scripts/circuits/`           | Instrumenteringsforstaerker og symbolske knudepunkter |
| `scripts/expand.py`           | Symbolsk sammenligning af alternative svarformer      |
| `scripts/validate_scripts.py` | Smoke checks og kendte testcases                      |

Der findes desuden notebooks til interaktiv anvendelse, blandt andet for
LTIC-tjek, andenordensberegning og zero-state/zero-input-problemer.

Scripts er bevidst smaae og importerbare. Deres typiske kontrakt er:

- eksplicitte numeriske eller symbolske inputs;
- kompakt returneret svar, ofte et dictionary med navngivne resultater;
- dokumenterede antagelser og relevante inputchecks;
- brug fra notebook via `from scripts.<topic>.<module> import <function>`.

### Rapporter

| Rapporttype                         | Funktion                                                        |
| ----------------------------------- | --------------------------------------------------------------- |
| `full_input_coverage_audit.md`      | Matrix over eksamens- og forelaesningsdaekning                  |
| `exam_task_taxonomy.md`             | Tilbagevendende opgavetyper, metoder, scriptmode og faelder     |
| `coverage_report*_da.md`            | Hvilke kilder og emner formelsamlingen daekker                  |
| `exam_verification_report*_da.md`   | Kontrol af hurtig metode, symboler og sandt/falsk-regler        |
| `script_inventory.md`               | Accepterede og afviste scriptkandidater samt risiko             |
| `script_validation_report.md`       | Repraesentative inputs, forventninger og valideringsresultater  |
| `script_note_integration_report.md` | Kobling fra scriptfunktion til LaTeX-sektion og manuelle checks |
| `latex_repair_report.md`            | Dokumenterede LaTeX-rettelser                                   |

Rapportlaget er vigtigt: det forhindrer, at AI'en producerer en lang PDF eller
en stor kodebase uden dokumenteret eksamensrelevans.

## Den konkrete 22050-loesning

### Eksamensdesign

`AGENTS.md` beskriver dokumentet som en Ctrl+F-problemloeser til en
tidskritisk eksamen med korte delopgaver og mange sandt/falsk- eller
multiple-choice-beslutninger. Det giver foelgende produktvalg:

- dansk brugs- og forklaringstekst med engelske soegealiaser;
- metodefinder i starten af dokumentet;
- korte opskrifter frem for lange udledninger;
- symboler, enheder, hurtigtjek og typiske faelder naer formlerne;
- tydelig adskillelse mellem nul-start-respons, egenrespons og total respons;
- manuel kontrol foer et Python-resultat accepteres.

### Identificerede opgavetyper

`reports/exam_task_taxonomy.md` klassificerer 12 overordnede opgavetyper:

| Opgavetype                         | Understoettelse                           |
| ---------------------------------- | ----------------------------------------- |
| LTIC-klassifikation                | Kun noter; fortolkningsopgave             |
| Kredslobsligninger                 | Kun noter; billed- og fortolkningsopgave  |
| Impuls-/trin-/ramperespons         | Noter med scriptassistance                |
| Foldning                           | Script kan vaere primaer beregningshjaelp |
| Fourierrækker                      | Noter med symbolsk assistance             |
| Fouriertransformationsegenskaber   | Noter med afgraenset assistance           |
| Laplacekoncepter og invers Laplace | Noter med symbolsk assistance             |
| Andenordensklassifikation          | Script kan vaere primaer beregningshjaelp |
| Bode-/filtermatching               | Noter med numeriske checks                |
| Butterworth-design                 | Noter med beregningsassistance            |
| ADC og sampling                    | Script kan vaere primaer beregningshjaelp |
| Instrumenteringsforstaerker        | Noter med beregningsassistance            |

Denne taksonomi er projektets centrale mellemprodukt: den afgoer baade
indholdsfortegnelsen og hvilke Python-funktioner der forsvares.

### Afviste automatiseringer

Projektet har eksplicit afvist:

- fuld fortolkning af kredslobsdiagrammer;
- automatisk valg af multiple-choice-svar;
- automatisk matching af plots fra screenshots;
- generel natural-language transformfortolker.

Faelles aarsag er, at inputtet kraever billedfortolkning eller faglig
doemmekraft, som ikke kan valideres stabilt gennem en lille Python-funktion.
Dette er en vaesentlig genbrugsregel for nye fag.

## Arkitektur og dataflow

```text
Ra kursusmateriale
  -> input-audit og eksamensopgavetyper
  -> indholdsvalg og LaTeX-moduler
  -> kandidater til beregningshjaelp
  -> validerede Python-funktioner
  -> kobling mellem opskrifter og scripts
  -> coverage-/verificationrapporter
  -> PDF-build med symbolregister
```

### Lag 1: Audit

AI'en gennemgaar eksamener og forelaesninger og opretter en taksonomi:
Hvilke opgaver gentages? Hvilken hurtig metode afgør dem? Hvilke faelder gaar
igen? Er problemet manuelt, scriptassisteret eller velegnet til en stabil
beregningsfunktion?

### Lag 2: Noter

Noterne skrives ud fra taksonomien, ikke fra forelaesningsrækkefølgen alene.
Hvert tilbagevendende emne boer indeholde:

- genkendelsesord;
- formel eller beslutningsregel;
- symboler og relevante enheder;
- betingelser for brug;
- et hurtigt plausibilitetstjek;
- typiske faelder;
- en kort opskrift ved procedureopgaver.

### Lag 3: Scripts

Et script optages kun, naar opgavetypen er gentagen, input kan beskrives
entydigt, og output kan valideres mod et simpelt kendt eksempel. Scriptet
returnerer beregninger, ikke en ubegrundet eksamensdom.

### Lag 4: Integration

Naar en LaTeX-sektion henviser til en funktion, skal teksten fortaelle:

- hvorfor og hvornaar funktionen anvendes;
- hvilke inputs den kraever;
- hvad den returnerer;
- hvilket manuelt tjek der stadig skal foretages;
- hvornaar den ikke maa bruges.

### Lag 5: Verification

Projektet slutter ikke ved genererede filer. Coverage- og
verificationrapporter skal kunne vise, at alle vigtige opgavetyper er
soegbare, har metodeindhold og ikke henviser til uvalideret kode.

## Hvordan projektet er blevet lavet

Den praecise dialoghistorik er ikke gemt i projektet. Arbejdsprocessen kan
derimod rekonstrueres fra artefakterne:

1. Kursusmateriale og tidligere formelsamlinger er samlet under `input/` og
   som reference-PDF'er.
2. Eksamensopgaver og forelaesninger er auditeret, hvilket har produceret
   daeknings- og taksonomirapporter.
3. En oprindelig formelsamling i `sources/` og en dansk version i
   `sources_da/` er blevet viderebearbejdet til en separat samlet dansk
   version i `sources_combined_da/`.
4. Den samlede version er gjort mere eksamensrettet med metodefinder,
   symboloversigt, faelder, sandt/falsk-tjek og scriptreferencer.
5. Python-funktioner er organiseret efter faglige opgavefamilier, registreret
   i et inventory og koert gennem smoke-validering.
6. Integration mellem noter og scripts er dokumenteret i en separat rapport.
7. PDF'en er bygget med LaTeX, makeindex og efterfoelgende LaTeX-pass for
   stabile sidehenvisninger.

Git-historikken understøtter, at en stor samlet etablering af
`exam_support/` fandt sted i en samlet commit, med senere opdatering af
Laplace-indhold og PDF-output. Den giver ikke grundlag for at tilskrive alle
enkeltbeslutninger en bestemt raekkefølge eller AI-session.

## Blueprint til et nyt teknisk fag

### Anbefalet startstruktur

```text
new_course_project/
  MASTER_PROMPT_NEW_TECHNICAL_COURSE_DA.md
  input/
    exams/
    solutions/
    lectures/
    exercises/
    reference_notes/
  notes/
  scripts/
  reports/
  requirements.txt
  main.tex
```

Mapper uden materiale kan udelades. AI'en skal inspicere den reelle struktur
og maa ikke antage, at alle kildetyper findes.

### Fase 1: Fastlaeg input og maal

AI'en skal oprette en kildeoversigt og identificere:

- fagets navn, eksamenstype og sprog;
- hvilke eksamener, loesninger og forelaesninger der findes;
- notation, tilladte hjaelpemidler og eventuelle tids-/formatkrav;
- usikre eller manglende kilder.

Output: `reports/input_audit.md`.

### Fase 2: Udled eksamenstaksonomi

Analyser tidligere opgaver og klassificer gentagne opgavetyper. For hver type
registreres soegeord, hurtig metode, kilder, typiske fejl og en af tre modes:

- `notes_only`: faglig vurdering eller bevis/fortolkning;
- `script_assisted`: noter er primaere, kode kontrollerer beregning;
- `script_primary`: en stabil beregning kan udfoeres direkte, men antagelser
  og kontrol fremgaar stadig af noterne.

Output: `reports/exam_task_taxonomy.md`.

### Fase 3: Design formelsamlingen

Opret en modulær LaTeX-struktur organiseret efter opgavetyper og centrale
begreber. Noterne skal vaere korte, soegbare og anvendelige under eksamen.
Kun dokumenteret eksamensrelevant stof eller noedvendige grundforudsætninger
medtages.

Minimumsindhold for hver vigtig opgavetype:

- `Brug naar` eller tilsvarende genkendelsesregel;
- centrale formler/metoder;
- forklaring af symboler og enheder;
- betingelser og antagelser;
- hurtigtjek og faelder;
- kort trinvis opskrift, hvis opgaven er procedurebaseret.

Output: `main.tex`, emnemoduler og en bygbar PDF.

### Fase 4: Byg kun forsvarlige scripts

Opret funktioner for gentagne beregninger med klart input/output. Afvis
automation naar opgaven primaert handler om fortolkning, billedlaesning,
bevis eller kontekstafhaengige valg.

For hver accepteret funktion kraeves:

- importérbar funktion frem for interaktivt script;
- type hints hvor praktisk og kort docstring;
- eksplicitte antagelser og inputvalidering;
- notebook-venlige outputs;
- repraesentativ smoke test og mindst et simpelt kendt resultat.

Output: `scripts/`, `requirements.txt`, `reports/script_inventory.md` og
`reports/script_validation_report.md`.

### Fase 5: Integrer noter og kode

Tilfoej kun scriptreferencer efter, at den manuelle metode er forklaret. Hver
reference skal angive input, output, kontrol og ikke-anvendelsestilfaelde.

Output: `reports/script_note_integration_report.md`.

### Fase 6: Verificer daekning og build

Kontroller alle taksonomiens opgavetyper mod det endelige dokument og alle
scriptreferencer mod faktiske, validerede funktioner. Byg LaTeX-output og
eventuelt symbolregister. Registrer begrænsninger aerligt.

Output:

- `reports/coverage_report.md`;
- `reports/exam_verification_report.md`;
- kompileret PDF;
- valideret Python-vaerktoejskasse.

## Kvalitetsporte og stopkriterier

Et nyt fagprojekt er ikke faerdigt, foer foelgende er sandt:

| Kontrol     | Krav                                                                   |
| ----------- | ---------------------------------------------------------------------- |
| Kilder      | Alle anvendte inputkilder er listet; mangler er noteret                |
| Taksonomi   | Tilbagevendende eksamensopgavetyper er kortlagt                        |
| Noter       | Hver prioriteret type har metode, symbolforklaring og hurtigtjek       |
| Scripts     | Hver accepteret funktion har klart anvendelsesomraade og koert test    |
| Afvisninger | Risikable automationer er registreret som afvist eller begrænset       |
| Integration | Ingen note henviser til ikke-eksisterende/uvaliderede scripts          |
| Build       | PDF bygger uden fatale fejl; indeks/reference-pass er koert hvis brugt |
| Rapporter   | Coverage, verification, inventory og validation matcher output         |

## Genbrugsregler

### Det der boer genbruges direkte

- workflowet fra input-audit til taksonomi, noter, scripts og verification;
- skellet mellem `notes_only`, `script_assisted` og `script_primary`;
- modulær LaTeX-struktur og kort, eksamensrettet skrivestil;
- inventory- og valideringskrav for Python;
- princippet om at rapporter skal dokumentere huller og begrænsninger.

### Det der skal genudledes for hvert nyt fag

- emneopdeling og notation;
- tilbagevendende opgavetyper;
- hvilke scripts der faktisk giver mening;
- sprog, eksamensformat og brug af symbolregister;
- dependencies og konkrete testcases.

### Det der ikke automatisk boer kopieres

- signal-/systemspecifikke moduler og formler;
- 22050-specifikke eksamensantagelser;
- Python-funktioner uden en tilsvarende tilbagevendende opgavetype i det nye
  fag;
- automatisering af figurer, mixed statements eller komplekse vurderingsvalg
  uden robuste, validerbare inputs.

## Anbefalet brug med en AI

1. Opret en ny kursusmappe med raadokumenter under `input/`.
2. Laeg `MASTER_PROMPT_NEW_TECHNICAL_COURSE_DA.md` i mappen.
3. Udfyld kursusparametrene i promptens startafsnit, hvis de kendes.
4. Bed AI'en foelge prompten helt frem til stopkriterierne.
5. Gennemgaa altid taksonomi, script inventory, validation report og den
   kompilerede PDF manuelt, foer materialet bruges til eksamen.

## Samlet vurdering

`exam_support/` demonstrerer en solid genbrugelig metode: eksamensmateriale
bliver foerst omdannet til en taksonomi, dernaest til en kort formelsamling og
kun til sidst til validerede beregningshjaelpere. Den vaesentligste styrke er
ikke antallet af formler eller scripts, men at projektet dokumenterer
anvendelsesgraenser og forbinder hvert vaerktoej med en konkret opgavetype.

Til et nyt teknisk fag boer samme arkitektur genbruges, mens selve
fagindholdet, scripts og valideringseksempler udledes paa ny fra de faktiske
kilder.
