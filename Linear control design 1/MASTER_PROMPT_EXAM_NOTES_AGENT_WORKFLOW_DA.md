# Masterprompt: agentbaseret eksamensformelsamling og Python-værktøjskasse

## Sådan bruges denne fil

Læg denne fil i roden af en ny kursusmappe. Kildemateriale skal så vidt muligt ligge under `input/`.

Anbefalet struktur:

```text
input/
  lectures/          forelæsningsslides, noter, kapitler, øvelsesark
  exams/             tidligere eksamenssæt
```

Giv derefter Codex/AI-agenten denne instruktion:

```text
Følg MASTER_PROMPT_EXAM_NOTES_AGENT_WORKFLOW_DA.md. Gennemfør arbejdet helt frem til stopkriterierne.
Du må kun stoppe, hvis du er blokeret af manglende kilder, ødelagte filer eller et valg, som ikke kan udledes af materialet.
```

Udfyld gerne parametrene før start. Ukendte værdier skal AI'en udlede af kilderne eller markere som uafklarede.

```text
KURSUSNAVN: [udfyld eller inferer fra kilder]
UDDANNELSE/KURSUSKODE: [valgfrit]
OUTPUTSPROG: Dansk
EKSAMENSFORMAT: [udfyld eller inferer: skriftlig/typeopgaver/MCQ/mundtlig]
TILLADTE HJÆLPEMIDLER: [ukendt medmindre dokumenteret]
MÅ PYTHON BRUGES TIL EKSAMEN: [ja/nej/ukendt]
SÆRLIGE OUTPUTKRAV: [valgfrit]
```

## Målet

Du skal bygge en eksamenspakke til et fag, hvor eksamen primært består af typeopgaver, beregninger, udledninger og metodevalg.

Pakken skal være brugbar for en studerende, der ikke har set faget før, men som skal kunne løse eksamensopgaver effektivt og korrekt. Den skal ikke være en lang lærebog. Den skal være en eksamensmanual: hvad skal jeg genkende, hvilken metode skal jeg bruge, hvilke formler skal jeg sætte ind, hvilke antagelser gælder, hvad skal jeg tjekke, og hvornår findes der et sikkert Python-script.

Det færdige projekt skal producere:

1. en fuld pensumrapport i Markdown baseret på alle forelæsninger/kilder;
2. én Markdown-analyse pr. eksamenssæt med alle opgaver, opgavetyper og løsningsmetoder;
3. en merged opgavetype- og emnerapport, hvor alle eksamensopgaver er grupperet efter type;
4. en Python-værktøjskasse til de opgaver, hvor Python er fagligt forsvarligt og praktisk;
5. en rapport over, hvad Python dækker og ikke dækker;
6. en eksamensrettet LaTeX-formelsamling/PDF med pensum, metoder, opgavetyper og Python-henvisninger;
7. valideringsrapporter, der dokumenterer at noter, scripts og eksamensdækning hænger sammen.

## Hovedprincipper

- Alt skal baseres på faktiske kilder i repository'et.
- Forelæsningerne skal læses først, så hele pensum og notation forstås, før eksamenerne analyseres.
- Eksamenssættene skal analyseres separat, som om hver analyse udføres af en specialiseret agent.
- Den endelige formelsamling skal bygges ud fra både pensumrapporten og alle eksamensanalyser.
- Python er sekundært. Noterne skal altid kunne bruges uden Python.
- Python må kun bruges til stabile beregninger, algebra, numerik, statistik, plotting eller kontrolberegninger.
- Python må ikke skjule faglige valg, antagelser eller fortolkning.
- Ingen opgavetype må påstås dækket, medmindre den er mappet til en notesektion og eventuelt et valideret script.
- Skriv på dansk, men behold engelske fagtermer og søgealiaser i overskrifter, når kilderne bruger dem.
- Marker antagelser, usikkerheder og manglende kilder eksplicit.

## Obligatorisk outputstruktur

Tilpas navne efter faget, men producer mindst:

```text
main.tex
exam_toolbox.ipynb
sections/
  <emnemoduler>.tex
scripts/
  <faglige undermapper>/
reports/
  input_audit.md
  full_curriculum_report.md
  exam_set_analyses/
    <eksamenssæt_1>.md
    <eksamenssæt_2>.md
    ...
  merged_task_taxonomy.md
  python_coverage_report.md
  script_inventory.md          hvis scripts vurderes
  script_validation_report.md  hvis scripts optages
  script_note_integration_report.md hvis noter refererer til scripts
  coverage_report.md
  exam_verification_report.md
  final_review_report.md
requirements.txt               hvis Python-dependencies bruges
build.log eller build_notes.md
```

Producer en PDF fra `main.tex`, hvis LaTeX-miljøet tillader det. Hvis PDF ikke kan bygges, skal buildblokeringen dokumenteres konkret i `reports/final_review_report.md`.

## Fase 0: Audit af input

Før noget fagligt skrives:

1. Gennemgå hele repository'et.
2. Kortlæg filer, mapper, filtyper, duplikater og åbenlyst manglende materiale.
3. Identificer kursusnavn, eksamensformat, hjælpemidler, pensum og notation.
4. Registrer forelæsninger, eksamenssæt, løsningsforslag, facit, øvelser og referencefiler.
5. Vurder kvaliteten af hver kilde: tekstudtræk, scanninger, figurer, tabeller, OCR-risici og manglende sider.

Skriv `reports/input_audit.md` med:

| Kilde | Type | Rolle | Kvalitet | Bruges til | Usikkerheder |
| ----- | ---- | ----- | -------- | ---------- | ------------ |

Angiv også kildeprioritet:

1. eksamenssæt og officielle løsningsforslag;
2. forelæsningsmateriale og officielle noter;
3. øvelser, afleveringer og supplerende materiale;
4. uofficielle noter, hvis de findes.

## Fase 1: Fuld pensumrapport fra alle forelæsninger

Læs alle forelæsninger, slides, noter og officielle pensumkilder igennem før eksamensanalysen.

Skriv `reports/full_curriculum_report.md`. Den må gerne være lang. Den skal være en komplet rå pensumkortlægning, ikke den endelige kompakte formelsamling.

Rapporten skal indeholde:

1. kursusoverblik;
2. alle hovedemner og underemner;
3. centrale definitioner;
4. centrale formler;
5. symboler, notation og enheder;
6. antagelser og gyldighedsbetingelser;
7. standardudledninger, som kan forventes til eksamen;
8. typiske beregningstrin;
9. figurer/diagramtyper, der skal kunne tolkes;
10. forbindelser mellem emner;
11. emner, der kun nævnes svagt eller ikke virker eksamenscentrale;
12. uklarheder, manglende dokumentation og notation, der skifter mellem kilder.

For hvert emne skal du skrive:

```text
## Emne: [navn]

### Kilder
- [filnavn/sider/slideintervaller hvis muligt]

### Hvad skal man kunne?
- ...

### Centrale formler og regler
- ...

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |

### Standardmetoder
1. ...
2. ...

### Typiske fejl og faldgruber
- ...
```

Denne rapport skal være bredere end den endelige formelsamling. Den er grundlaget for de næste faser.

## Fase 2: Én agentanalyse pr. eksamenssæt

Opret én analysefil pr. eksamenssæt i `reports/exam_set_analyses/`.

Hvert eksamenssæt skal behandles isoleret, som om en separat agent har ansvar for netop dette sæt. Agenten må bruge `full_curriculum_report.md`, men skal selv læse eksamenssættet og eventuelle løsningsforslag.

Filnavnseksempel:

```text
reports/exam_set_analyses/2023_sommer.md
reports/exam_set_analyses/2024_vinter.md
```

Hver fil skal have denne struktur:

```text
# Eksamensanalyse: [sæt]

## Kilder
- Eksamensfil:
- Løsningsforslag/facit:
- Relevante forelæsninger:

## Overblik
| Opgave | Emne | Opgavetype | Point/vægt hvis kendt | Kræver udledning? | Kan Python hjælpe? |
| ------ | ---- | ---------- | --------------------- | ----------------- | ------------------ |

## Opgave-for-opgave analyse

### Opgave [nummer]
**Kort beskrivelse:**
**Genkendelsessignaler:** ord, formler, figurer eller datastruktur, der afslører typen.
**Relevant pensum:** henvis til emner fra `full_curriculum_report.md`.
**Hurtig løsning:** trinvis metode, ikke bare facit.
**Centrale formler:** kun dem der faktisk bruges.
**Symboler/input fra opgaven:** hvad skal aflæses eller udledes.
**Antagelser:** hvad skal være sandt for metoden.
**Typiske fælder:** konkrete fejlmuligheder.
**Hurtigtjek:** dimensions-, fortegns-, størrelses- eller grænsetjek.
**Python-vurdering:** `notes_only`, `script_assisted` eller `script_primary`.
**Scriptkandidat:** ja/nej og hvorfor.
**Mangler/usikkerheder:** hvis opgaven ikke kan analyseres fuldt.
```

Brug kun disse support modes:

- `notes_only`: opgaven afgøres af forståelse, bevis, figurfortolkning eller kontekstafhængigt valg;
- `script_assisted`: manuel metode er primær, men kode kan beregne, plotte, løse ligninger eller kontrollere delresultater;
- `script_primary`: en stabil, klart parameteriseret beregning kan udføres af en funktion, mens noter stadig forklarer antagelser og kontrol.

Ingen opgave må springes over. Hvis en opgave er ulæselig eller mangler facit, skal det dokumenteres.

## Fase 3: Merge af alle eksamensanalyser efter opgavetype og emne

Læs `full_curriculum_report.md` og alle filer i `reports/exam_set_analyses/`.

Skriv `reports/merged_task_taxonomy.md`.

Formålet er at samle alle gentagne og mulige eksamensopgavetyper. Rapporten skal gøre det tydeligt, hvad der faktisk kan komme til eksamen, og hvordan det skal løses.

Brug denne tabel:

| Opgavetype | Emne | Genkendelsessignaler | Kilder/eksamensopgaver | Hurtig metode | Nødvendige formler | Symboler/input | Support mode | Scriptkandidat | Typiske fælder | Hurtigtjek |
| ---------- | ---- | -------------------- | ---------------------- | ------------- | ------------------ | -------------- | ------------ | -------------- | -------------- | ---------- |

Efter tabellen skal du skrive en kort sektion pr. opgavetype:

```text
## Opgavetype: [navn]

### Kommer fra
- [eksamenssæt/opgave]
- [forelæsningskilde]

### Brug når
- ...

### Standardopskrift
1. ...
2. ...
3. ...

### Hvad skal noterne dække?
- ...

### Hvad kan Python realistisk dække?
- ...

### Hvad kan Python ikke dække?
- ...

### Prioritet
Høj/middel/lav, med begrundelse.
```

Prioritér højt:

1. opgavetyper, der går igen i flere eksamenssæt;
2. opgavetyper med mange point;
3. opgavetyper med tung beregning;
4. opgavetyper med hyppige faldgruber;
5. opgavetyper, der repræsenterer centrale forelæsningsemner.

## Fase 4a: Python-værktøjskasse

Byg Python-scripts efter `reports/merged_task_taxonomy.md`.

### Optagelseskriterier

Opret kun en funktion, hvis mindst ét af følgende er sandt:

- opgavetypen forekommer gentagne gange;
- beregningen er stabil og klart parameteriseret;
- funktionen reducerer tung algebra, numerik, statistik, simulation eller plotting;
- funktionen kan kontrollere et manuelt svar med et entydigt resultat;
- funktionen forebygger en dokumenteret hyppig regnefejl;
- funktionen kan bruges på flere gamle eksamensopgaver, ikke kun én.

Afvis en funktion, hvis:

- opgaven primært er konceptuel, bevisbaseret eller fortolkningsbaseret;
- inputtet er et billede, fri tekst eller en uklar model uden stabil parser;
- funktionen ville vælge eksamenssvar uden at vise antagelser;
- den kun passer til en enkelt historisk opgave;
- resultatet ikke kan valideres;
- manuel løsning er hurtigere, sikrere og mindre risikabel.

### Scriptstandard

Krav:

- importerbare funktioner, ikke løse notebooks;
- engelske, beskrivende funktionsnavne;
- type hints hvor praktisk;
- korte docstrings med `Use when`, parametre, output og antagelser;
- eksplicit inputvalidering og tydelige fejlbeskeder;
- deterministiske outputs;
- ingen `input()`;
- ingen skjult filafhængighed;
- ingen internetafhængighed;
- plottingfunktioner returnerer `fig, ax` og kalder ikke `show()` automatisk;
- numeriske metoder skal have tolerancer, stopkriterier og advarsler ved dårligt input.

Eksempelstruktur:

```text
scripts/
  __init__.py
  linear_algebra/
    __init__.py
    systems.py
  statistics/
    __init__.py
    inference.py
  validate_scripts.py
```

Eksempelimport:

```python
from scripts.linear_algebra.systems import solve_linear_system
```

### Script inventory

Skriv `reports/script_inventory.md` med både accepterede og afviste kandidater:

| Opgavetype | Kandidatfunktion | Status | Begrundelse | Input | Output | Validerbar? | Relaterede eksamensopgaver |
| ---------- | ---------------- | ------ | ----------- | ----- | ------ | ----------- | -------------------------- |

### Validering

For hver offentlig funktion skal du køre:

1. importtest;
2. en repræsentativ normal case;
3. mindst én simpel case med kendt resultat;
4. relevante ugyldige inputs;
5. eventuelle numeriske randtilfælde.

Implementer testene i `scripts/validate_scripts.py` eller fokuserede testfiler.

Skriv `reports/script_validation_report.md`:

| Funktion | Fil | Kategori | Testinput | Forventet resultat | Faktisk resultat | Status | Begrænsninger |
| -------- | --- | -------- | --------- | ------------------ | ---------------- | ------ | ------------- |

Du må ikke skrive, at en funktion er valideret, medmindre testen faktisk er kørt.

## Fase 4b: Samlet eksamensnotebook

Når scripts er skrevet og valideret, skal du oprette `exam_toolbox.ipynb` i projektroden. Notebooken er brugerens praktiske eksamensarbejdsfil. Den skal ligne en samlet værktøjskasse, ikke en udviklingsnotebook.

Notebooken skal indeholde:

1. en kort introduktion på dansk: hvad filen bruges til, og at den ikke erstatter faglig metode eller noter;
2. en setup-celle, der finder projektroden robust og gør `scripts/` importbar;
3. alle relevante imports samlet ét sted;
4. import af alle offentlige, validerede funktioner fra `scripts/`;
5. en oversigt over eksamensopgavetyper og hvilke funktioner der passer til dem;
6. én brugssektion pr. funktionsgruppe med forklaring af input, output, antagelser, manuelt tjek og “brug ikke når”;
7. korte eksempelkald med simple, verificerbare tal;
8. ingen tung tekst, ingen skjulte sideeffekter og ingen automatisk afhængighed af gamle eksamensdata.

Notebooken skal være struktureret sådan her, med fagspecifikke navne hvor relevant:

Hver funktionssektion i notebooken skal bruge denne skabelon:

```text
## [Opgavetype/funktionsgruppe]

Brug når:
- ...

Du skal selv finde disse input i opgaven:
- ...

Funktionen returnerer:
- ...

Tjek manuelt:
- ...

Brug ikke når:
- ...

Eksempel:
```

Krav til notebooken:

- Den må kun importere funktioner, der findes og er valideret.
- Den må ikke definere centrale fagfunktioner direkte i notebooken, medmindre de også findes i `scripts/`. Notebooken er brugerflade, ikke kildekodebase.
- Den skal kunne køres fra top til bund uden fejl i et rent miljø, når dependencies fra `requirements.txt` er installeret.
- Den skal være egnet til eksamen: korte forklaringer, tydelige celler, klar opdeling og plads til egne beregninger.
- Den skal ikke indeholde lange løsningsforslag til alle gamle eksamener, men den må gerne have små demonstrationskald.
- Hvis ingen scripts optages, skal notebooken ikke oprettes; begrund i `python_coverage_report.md`, hvorfor den ikke er relevant.

Skriv desuden `reports/notebook_inventory.md` med:

| Notebooksektion | Funktioner | Opgavetyper | Eksempel testet? | Input forklaret? | Output forklaret? | Manuelt tjek forklaret? | Begrænsninger |
| --------------- | ---------- | ----------- | ---------------- | ---------------- | ----------------- | ----------------------- | ------------- |

Notebooken skal indgå i den endelige verification. Ingen funktion må stå i notebooken, hvis den ikke også står i `script_validation_report.md`.

## Fase 5: Rapport over Python-dækning og ikke-dækning

Når scripts er skrevet og valideret, skriv `reports/python_coverage_report.md`.

Rapporten skal forklare hele eksamensrummet i forhold til Python:

| Opgavetype | Support mode | Script/funktion | Hvad Python gør | Hvad brugeren selv skal gøre | Brug ikke når | Status |
| ---------- | ------------ | --------------- | --------------- | ---------------------------- | ------------- | ------ |

Rapporten skal også have:

```text
## Dækket af Python
- ...

## Delvist dækket af Python
- ...

## Ikke dækket af Python
- ...

## Hvorfor ikke alt automatiseres
- ...

## Minimum manuel kunnen, selv med scripts
- ...
```

Denne rapport er et vigtigt mellemprodukt: Den skal gøre det klart, hvilke eksamensopgaver der kan løses eller kontrolleres med scripts, og hvilke der kræver rene noter/metode.

## Fase 6: Byg den endelige LaTeX-formelsamling

Byg først LaTeX-dokumentet efter at følgende findes:

- `reports/full_curriculum_report.md`;
- alle `reports/exam_set_analyses/*.md`;
- `reports/merged_task_taxonomy.md`;
- `reports/python_coverage_report.md`;
- scriptvalidering, hvis scripts findes.

Den endelige LaTeX-formelsamling skal ikke bare være en forkortet pensumrapport. Den skal være en eksamensmanual.

### Dokumentdesign

`main.tex` skal normalt kun indeholde:

- præambel og pakker;
- makroer;
- titel;
- indholdsfortegnelse;
- eventuelt symbolregister;
- `\input{sections/...}` for modulære sektioner.

Start med:

1. `00_start_her.tex`: hvordan dokumentet bruges under eksamen;
2. `01_metodefinder.tex`: tabel der kobler opgaveord/genkendelsessignaler til notesektion og metode;
3. emnemoduler;
4. Python-hjælpere, hvis relevante;
5. tjeklister og typiske fælder.

### Krav til hver opgavetype i noterne

Hver prioriteret opgavetype skal have:

```text
\subsection{[Opgavetype] / [søgealiaser]}

\paragraph{Brug når}
Hvordan opgaven genkendes.

\paragraph{Input fra opgaven}
Hvad skal aflæses, beregnes eller antages.

\paragraph{Metode}
3-7 trin, egnet til eksamensbrug.

\paragraph{Formler}
Centrale formler, ikke generel teori.

\paragraph{Symboler}
Forklaring af alle symboler og enheder.

\paragraph{Antagelser}
Hvornår metoden gælder.

\paragraph{Hurtigtjek}
Dimensions-, fortegns-, størrelses- eller grænsetjek.

\paragraph{Typiske fælder}
Konkrete fejlmuligheder fra eksamener og kilder.

\paragraph{Python}
Kun hvis et valideret script findes:
- funktionens navn;
- hvilket input brugeren skal give;
- hvad funktionen returnerer;
- hvad der stadig skal tjekkes manuelt;
- hvornår funktionen ikke må bruges.
```

### Niveaukrav

Noterne skal være så konkrete, at en eksamensbruger kan løse typeopgaver uden at kende faget på forhånd.

Det betyder:

- ingen uforklarede symboler;
- ingen “brug standardformlen” uden at give standardformlen;
- ingen henvisning til teori uden operationel metode;
- ingen opgavetype uden genkendelsessignaler;
- ingen formel uden gyldighedsbetingelser, hvis de betyder noget;
- ingen Python-reference uden manuel metode;
- ingen lang bevistekst, medmindre eksamen kræver udledning.

### Symbolregister

Hvis faget har mange symboler, fysisk notation, indeks, matricer eller statistiknotation, skal PDF'en have et symbolregister med:

| Symbol | Betydning | Enhed | Første notesektion |
| ------ | --------- | ----- | ------------------ |

Hvis symbolregister fravælges, skal begrundelsen stå i `reports/coverage_report.md`.

## Fase 7: Sammenkobling mellem noter og scripts

Skriv `reports/script_note_integration_report.md`.

| Script | Funktion | Notesektion | Support mode | Input | Output | Manuelt tjek | Brug ikke når | Valideret? |
| ------ | -------- | ----------- | ------------ | ----- | ------ | ------------ | ------------- | ---------- |

Krav:

- ingen notesektion må henvise til en ikke-eksisterende funktion;
- ingen notesektion må henvise til en ikke-valideret funktion;
- hver scriptfunktion skal nævnes i noterne eller begrundes som kun intern/test;
- hver Python-reference i noterne skal have en tilsvarende række i rapporten.

## Fase 8: Dækning, verification og build

### Coverage report

Skriv `reports/coverage_report.md`:

- anvendte kilder;
- outputstruktur;
- hovedemner;
- fravalgte emner og hvorfor;
- symbolregisterstatus;
- Python-status;
- kendte begrænsninger;
- buildstatus;
- manuelle reviewpunkter.

### Exam verification report

Skriv `reports/exam_verification_report.md`.

For hver prioriteret opgavetype og hver eksamensopgave:

| Eksamenssæt/opgave | Opgavetype | Notesektion | Metode dækket? | Formler dækket? | Symboler forklaret? | Hurtigtjek/fælde? | Pythonstatus | Mangler? |
| ------------------ | ---------- | ----------- | -------------- | --------------- | ------------------- | ----------------- | ------------ | -------- |

Rapporten skal gøre det umuligt at overse en opgavetype. Hvis noget mangler, skal det enten rettes i noterne eller markeres som kendt begrænsning.

### Build

Forsøg at bygge PDF'en fra `main.tex`.

Kør også relevante Python-tests.

Dokumentér:

```text
LaTeX build:
- kommando:
- resultat:
- fejl/advarsler:

Python validation:
- kommando:
- resultat:
- fejl/advarsler:
```

Skriv dette i `reports/final_review_report.md`.

## Fase 9: Endelig kvalitetskontrol

Før arbejdet afsluttes, gennemfør denne tjekliste:

```text
[ ] Alle inputfiler er auditeret.
[ ] Alle forelæsninger/pensumkilder er læst ind i full_curriculum_report.md.
[ ] Hvert eksamenssæt har sin egen analysefil.
[ ] Ingen eksamensopgave er sprunget over uden forklaring.
[ ] Alle opgavetyper er merged i merged_task_taxonomy.md.
[ ] Hver prioriteret opgavetype har en notesektion.
[ ] Hver notesektion har Brug når, Input, Metode, Formler, Symboler, Antagelser, Hurtigtjek og Typiske fælder.
[ ] Python-kandidater er accepteret/afvist med begrundelse.
[ ] Alle accepterede scripts er importbare.
[ ] Alle offentlige scriptfunktioner er testet.
[ ] python_coverage_report.md forklarer både dækket og ikke-dækket.
[ ] Alle Python-henvisninger i noterne peger på validerede funktioner.
[ ] exam_verification_report.md mapper eksamensopgaver til notesektioner.
[ ] PDF er bygget, eller konkret buildblokering er dokumenteret.
[ ] final_review_report.md beskriver resterende begrænsninger.
```

## Forbudte genveje

Du må ikke:

- starte med LaTeX-noterne før pensumrapport og eksamensanalyser findes;
- nøjes med at skrive generelle noter uden mapping til eksamensopgaver;
- springe enkelte eksamensopgaver over, fordi de virker små;
- oprette scripts bare fordi en formel kan programmeres;
- lade Python vælge en metode, hvis metodevalget kræver faglig vurdering;
- automatisere billedfortolkning, figurlæsning eller multiple-choice uden robust repræsentation;
- påstå fuld dækning uden `exam_verification_report.md`;
- påstå scriptvalidering uden at have kørt tests;
- skrive en lang lærebog i stedet for en eksamensmanual;
- bruge uofficielle antagelser uden at markere dem;
- skjule manglende kilder, OCR-problemer, tvetydig notation eller uløste risici.

## Stopkriterier

Fortsæt arbejdet, til alle relevante punkter er opfyldt:

1. `reports/input_audit.md` findes og dækker alle kilder.
2. `reports/full_curriculum_report.md` findes og dækker alle forelæsninger/pensumkilder.
3. Der findes én analysefil pr. eksamenssæt i `reports/exam_set_analyses/`.
4. `reports/merged_task_taxonomy.md` samler alle opgavetyper efter emne og metode.
5. Python-kandidater er vurderet i `reports/script_inventory.md`, hvis Python er relevant.
6. Alle optagne scripts er skrevet, importbare og validerede.
7. `reports/python_coverage_report.md` forklarer, hvad Python dækker og ikke dækker.
8. LaTeX-noterne er bygget modulært ud fra pensumrapport, eksamensanalyser og Python-dækning.
9. Alle prioriterede opgavetyper har konkret metode, formler, symboler, antagelser, hurtigtjek og fælder.
10. Scriptreferencer i noterne matcher validerede funktioner.
11. `reports/coverage_report.md`, `reports/exam_verification_report.md` og `reports/final_review_report.md` er opdaterede.
12. PDF'en er bygget, eller en konkret lokal buildblokering er dokumenteret.
13. Kendte begrænsninger og manuelle reviewpunkter er tydeligt anført.

## Minimal kommando til Codex

Når denne fil ligger i kursusmappen, kan du starte med:

```text
Følg MASTER_PROMPT_EXAM_NOTES_AGENT_WORKFLOW_DA.md.
Byg en eksamensrettet formelsamling og Python-værktøjskasse ud fra alle filer i input/.
Arbejd fase for fase. Stop ikke før stopkriterierne er opfyldt, medmindre en konkret blokering dokumenteres.
```
