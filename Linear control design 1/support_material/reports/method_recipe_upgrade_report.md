# Method recipe upgrade report

## Formål

Formelsamlingen er opgraderet fra korte metodepunkter til eksplicitte opskrifter, hvor
hvert trin enten forklarer hvordan handlingen udføres eller henviser til en nummereret
formel. Længde er prioriteret under klarhed.

## Ændringer

- Alle 12 eksplicitte `\paragraph{Metode}`-opskrifter i `sections/03_*.tex` til
  `sections/07_*.tex` er omskrevet med operationelle deltrin.
- Globale vejledninger i `sections/00_start_her.tex`, `sections/01_metodefinder.tex`
  og `sections/08_python_checklists.tex` er gjort konkrete, så de henviser til
  signalrelationer, stabilitetstests, formelnumre og manuelle ansvar.
- Alle displayformler i `sections/*.tex` er konverteret fra unummererede `\[...\]`
  til nummererede `equation`-miljøer med `eq:`-labels.
- `main.tex` bruger nu `\numberwithin{equation}{section}` for stabile formelnumre.
- Python-helper-tabellen dækker nu alle offentlige funktioner fra `scripts.control`,
  ikke kun den tidligere kortere liste.
- Symbolregisteret er udvidet til et sidebrydende register med symbolbetydning,
  enhed/type og alle notesektioner hvor symbolet dukker op.
- F25 er integreret med nye/udbyggede opskrifter for initial-/slutværdi, 1\%-settling,
  standardinputfejl, Ziegler--Nichols PID og reference feed-forward med proper invers.

## Dækningskontrol

- Inventory før ændring: 12 eksplicitte metodeopskrifter, 19 displayformelblokke og
  globale metode-/checklistetabeller.
- Efter ændring: ingen `\[...\]`, `$$`, `equation*` eller `align*` fundet i
  `main.tex` eller `sections/*.tex`.
- Uafhængigt read-only review fandt ingen manglende eller dublerede equation-labels og
  vurderede alle 12 metodeopskrifter som operationelt udbygget.

## Validering

- `pdflatex -interaction=nonstopmode -halt-on-error main.tex` kørt to gange med output
  i `build.log`.
- Slutbuild: `main.pdf` genereret som A4, 18 sider, uden unresolved references eller
  rerun-advarsler.
- `python -m compileall -q scripts`: bestået.
- `python -m scripts.validate_scripts`: bestået, 35 checks.
- `pdftotext`-kontrol bekræftede, at de omskrevne opskrifter, formelreferencer,
  Nyquist-, PI-Lead- og sluttjeksektioner er med i PDF'en.

## Kendte begrænsninger

- Nummereringskravet er anvendt på alle egentlige displayformler. Inline-matematik er
  kun flyttet ud som refererbare formler, hvor opskrifterne har brug for et anker.
- Plot- og blokdiagramlæsning er stadig et manuelt fagligt trin, men opskrifterne giver
  nu konkrete regler for hvad der skal aflæses og hvordan det bruges.
