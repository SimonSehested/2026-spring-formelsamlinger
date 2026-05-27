# Masterprompt: byg eksamensformelsamling og Python-værktøjskasse til nyt teknisk fag

## Sådan bruges denne fil

Læg denne fil i roden af en ny kursusmappe med kildemateriale under
`input/`. Giv derefter en AI instruktionen:

```text
Følg MASTER_PROMPT_NEW_TECHNICAL_COURSE_DA.md. Gennemfør arbejdet helt frem
til stopkriterierne, medmindre du er blokeret af manglende kilder eller et
valg, som ikke kan udledes af materialet.
```

Udfyld gerne parametrene nedenfor før start. Ukendte værdier skal AI'en
udlede af kilderne eller markere som uafklarede.

```text
KURSUSNAVN: [udfyld eller inferer fra kilder]
UDDANNELSE/KURSUSKODE: [valgfrit]
OUTPUTSPROG: Dansk
EKSAMENSFORMAT: [udfyld eller inferer: skriftlig/MCQ/opgaver/mundtlig]
TILLADTE HJÆLPEMIDLER: [ukendt medmindre dokumenteret]
SÆRLIGE OUTPUTKRAV: [valgfrit]
```

## Din rolle

Du skal opbygge et selvstændigt, eksamensrettet projekt for et matematik-
eller teknikfag ud fra de filer, der faktisk findes i repository'et.

Projektet skal producere:

1. en kompakt, søgbar formelsamling i LaTeX og PDF;
2. en lille, valideret Python-værktøjskasse til tilbagevendende
   beregningsopgaver, når kode er fagligt forsvarlig;
3. rapporter, der dokumenterer kildegrundlag, eksamensdækning, scriptvalg,
   validering og kendte begrænsninger.

Du skal ikke antage fagets emner på forhånd. Inferer fag, notation,
opgavetyper og beregningsbehov fra materialet.

## Forventet input

Undersøg hele repository'et. En typisk struktur er:

```text
input/
  exams/             tidligere eksamener
  lectures/          slides eller forelæsningsnoter
```

## Obligatorisk outputstruktur

Tilpas emnemappenavne efter det fundne fag, men producer mindst:

```text
main.tex
sections/ eller sources/
  00_start_her.tex
  <emnemoduler>.tex
  99_python_hjælpere.tex       hvis scripts optages
scripts/
  <faglige undermapper>/
reports/
  input_audit.md
  exam_task_taxonomy.md
  coverage_report.md
  exam_verification_report.md
  script_inventory.md           hvis scripts vurderes
  script_validation_report.md   hvis scripts optages
  script_note_integration_report.md  hvis noter refererer til scripts
requirements.txt                hvis Python-dependencies bruges
```

Producer en PDF fra `main.tex`. Et symbolregister er obligatorisk, hvis faget har mange symboler eller fysisk notation; ellers skal fravalget begrundes i `coverage_report.md`.

## Hovedprincipper

- Formelsamlingen er primær. Python er kun et sekundært værktøj.
- Optimér for hurtig eksamensbrug, ikke for at gengive et helt pensum.
- Basér indhold på faktiske opgaver og kilder; tilføj ikke stof kun fordi
  det er generelt relevant for faget.
- Skriv på `OUTPUTSPROG`; bevar nyttige engelske eller originale søgealiaser
  i overskrifter, når kilderne bruger dem.
- Forklar antagelser ærligt. Marker påstande, der ikke kan verificeres fra
  kilderne.
- Bevar modularitet: fagindhold skal ligge i emnefiler, ikke som en lang
  hovedfil.
- Automatisér ikke opgaver, hvis det skjuler den faglige vurdering eller ikke
  kan valideres robust.

## Fase 1: Audit af kilder

Før du skriver noter eller scripts:

1. Kortlæg filer, mapper, dokumenttyper og eksisterende output.
2. Identificer kursusnavn, emner, notation, eksamensformat og tilgængelige
   facit/løsninger, hvis dette fremgår af materialet.
3. Registrer hvor mange eksamener, forelæsninger, opgavesæt og
   referencefiler der findes.
4. Noter manglende kilder og om figurer, scanninger eller dårlig tekstudtræk
   begrænser analysen.

Skriv `reports/input_audit.md` med:

- inventar over kilder;
- fundet fag- og eksamenskontekst;
- kildeprioritet;
- kendte usikkerheder;
- hvilken dokumentation der skal kontrolleres manuelt.

## Fase 2: Eksamensopgavetyper

Analyser eksamener og relevante opgaver før du beslutter dokumentets
kapitler. Skriv `reports/exam_task_taxonomy.md` med en tabel:

| Opgavetype | Søgeord/aliaser | Kilder | Hurtig metode | Support mode | Muligt script | Typiske fælder |
| ---------- | --------------- | ------ | ------------- | ------------ | ------------- | -------------- |

Brug kun disse support modes:

- `notes_only`: opgaven afgøres af forståelse, bevis, figurfortolkning eller
  et kontekstafhængigt valg;
- `script_assisted`: den manuelle metode er primær, men kode kan beregne,
  plotte eller kontrollere et delresultat;
- `script_primary`: en stabil, klart parameteriseret beregning kan udføres af
  en funktion, mens noter stadig forklarer antagelser og kontrol.

Prioritér opgavetyper, der gentages eller er centrale for eksamen. Angiv
eksplicit emner, der findes i forelæsningerne, men ikke forsvares i en kort
eksamenssamling.

## Fase 3: LaTeX-formelsamling

### Dokumentdesign

Opret `main.tex` og modulære emnefiler. `main.tex` skal normalt kun indeholde:

- præmbel og pakker;
- makrør;
- titel og indholdsfortegnelse;
- eventuelt symbolregister;
- `\input` af emnemoduler.

Start dokumentet med en metodefinder, som kobler opgaveord til den relevante
sektion og den hurtigste forsvarlige metode.

### Krav til hvert prioriteret emne

Hver tilbagevendende opgavetype skal som minimum have:

- en søgbar overskrift med relevante aliaser;
- `Brug når`: hvordan opgavetypen genkendes;
- centrale formler eller beslutningsregler;
- forklaring af alle centrale symboler og relevante enheder;
- antagelser og gyldighedsbetingelser;
- `Hurtigtjek`: en plausibilitets-, dimensions- eller grænsetest;
- `Typiske fælder`: mindst de fejl, som kilderne eller eksamenerne viser;
- en opskrift på 3-7 trin, hvis opgaven er procedurebaseret.

Undgå lange beviser, historiske forklaringer og teori, der ikke gør en
eksamensbeslutning lettere.

### Symbolregister

Hvis faget har mange symboler, skal PDF'en have en automatisk
symboloversigt efter indholdsfortegnelsen med:

- symbol;
- betydning;
- enhed, hvor relevant;
- sidehenvisning.

Brug et buildflow med indeks/reference-pass, så sidehenvisningerne er
stabile. Hvis symbolregister ikke er relevant, dokumenter hvorfor.

## Fase 4: Python-værktøjskasse

### Optagelseskriterier

Opret kun en funktion, hvis mindst et af følgende er sandt:

- opgavetypen forekommer gentagne gange;
- funktionen løser en stabil beregningsopgave med entydigt input;
- funktionen reducerer tung algebra, numerik, statistik, simulation eller
  plotting;
- funktionen kontrollerer et manuelt svar med et klart resultat;
- funktionen forhindrer en dokumenteret, hyppig beregningsfejl.

Afvis en funktion, hvis:

- opgaven hovedsageligt er konceptuel, bevisbaseret eller kræver faglig
  fortolkning;
- inputtet er et billede, fri tekst eller en uklar model uden stabil parser;
- funktionen ville vælge eksamenssvar uden at vise antagelser;
- den kun passer til en enkelt gammel opgave;
- resultatet ikke kan valideres;
- manuel løsning er hurtigere og mindre risikabel.

Registrer både accepterede og afviste kandidater i
`reports/script_inventory.md`.

### Kodestandard

Skriv importerbare funktioner organiseret efter faglig opgavefamilie:

```python
from scripts.topic.module import descriptive_function_name
```

Krav:

- beskrivende engelske funktionsnavne;
- type hints hvor praktisk;
- korte docstrings med `Use when`, parametre, output og antagelser;
- eksplicit inputvalidering og tydelige fejl;
- deterministiske outputs;
- ingen `input()` eller skjult filafhængighed;
- ingen internetafhængighed under brug;
- plottingfunktioner returnerer figur/akse og kalder ikke automatisk
  `show()`.

Brug standard videnskabelige biblioteker, når de er berettigede, og
registrér dem i `requirements.txt`.

### Validering

For hver accepteret offentlig funktion skal du faktisk køre:

- importtest;
- en repræsentativ normal case;
- mindst en kendt/simpel case med forventet resultat;
- relevante ugyldige inputs, hvis funktionen har væsentlige domænekrav.

Implementer dette samlet i `scripts/validate_scripts.py` eller i fokuserede
tests. Skriv `reports/script_validation_report.md` med:

| Funktion | Fil | Kategori | Testinput | Forventet resultat | Resultat | Begrænsninger |
| -------- | --- | -------- | --------- | ------------------ | -------- | ------------- |

Du må ikke kalde en funktion valideret, medmindre testen er blevet kørt.

## Fase 5: Sammenkobling af noter og scripts

Noterne skal være nyttige uden Python. Referer kun en scriptfunktion, når
sektionen allerede indeholder den manuelle metode og dens antagelser.

Ved hver scriptreference skal noten kort oplyse:

- hvilken opgavetype funktionen anvendes til;
- hvilket input brugeren skal udlede af opgaven;
- hvad funktionen returnerer;
- hvad der skal tjekkes manuelt;
- når funktionen ikke må bruges.

Skriv `reports/script_note_integration_report.md` med:

| Script | Funktion | Notesektion | Support mode | Input | Output | Manuelt tjek | Brug ikke når |
| ------ | -------- | ----------- | ------------ | ----- | ------ | ------------ | ------------- |

Ingen notereference må pege på et script, der ikke findes og er valideret.

## Fase 6: Verification og build

### Dækningskontrol

Skriv `reports/coverage_report.md` med:

- anvendte kilder;
- outputstruktur;
- hovedemner og valgte fravalg;
- symbolregisterstatus;
- kendte begrænsninger;
- buildstatus.

Skriv `reports/exam_verification_report.md`, der for hver prioriteret
opgavetype svarer på:

| Opgavetype/kilde | Hurtig metode | Notesektion | Symboler forklaret? | Hurtigtjek/fælde? | Scriptstatus | Mangler? |
| ---------------- | ------------- | ----------- | ------------------- | ----------------- | ------------ | -------- |

Tilpas kommandørne til miljø og outputfilnavne. Ret fatale buildfejl og
uoverensstemmelser mellem rapporter, noter og scripts. Rapporter advarsler,
der ikke kan eller bør fjernes.

## Forbudte genveje

Du må ikke:

- skrive en generisk lærebog i stedet for en eksamensrettet samling;
- oprette scripts bare fordi en formel kan programmeres;
- lade kode erstatte forklaring af metode, symboler eller antagelser;
- automatisere billedfortolkning eller multiple-choice-valg uden robust,
  kontrollerbar representation;
- påstå fuld dækning uden en mapping fra opgavetyper til noter;
- påstå validering uden at køre relevante tests;
- skjule manglende kilder, tvetydig notation eller uløste risici.

## Stopkriterier

Fortsæt arbejdet, til alle relevante punkter er opfyldt:

- kilderne er auditeret og dokumenteret;
- eksamensopgavetyperne er klassificeret og prioriteret;
- en kompakt, søgbar LaTeX-formelsamling er skrevet;
- hver prioriteret opgavetype har metode, centrale symboler og kontrolregel;
- kun fagligt forsvarlige scripts er optaget;
- alle optagne offentlige funktioner er kørt og valideret;
- scriptreferencer i noterne matcher validerede funktioner;
- coverage- og verificationrapporter er opdaterede;
- PDF'en er bygget, eller en konkret lokal buildblokering er rapporteret;
- kendte begrænsninger og manuelle reviewpunkter er tydeligt anført.
