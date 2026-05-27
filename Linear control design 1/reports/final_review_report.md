# Final review report

## Leverancer

Eksamenspakken er færdiggjort for det tilgængelige materiale: alle 13 forelæsninger, F21-løsningsfilen og den officielle Q11-Q20-questionnaire er auditeret; alle 20 F21-opgaver er analyseret og mappet; validerede scripts, notebook og en bygget modulær PDF er leveret.

## LaTeX build

- Forsøgt kommando: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Resultat: kunne ikke startes, fordi den lokale MiKTeX-installation mangler Perl-scriptmotoren, som `latexmk` kræver.
- Første direkte buildforsøg viste manglende lokale valgfrie pakker (`babel` med dansk option, `multirow`, `fancyhdr`). `multirow` og `fancyhdr` var ikke funktionelt nødvendige; dansk tekst sættes korrekt med UTF-8/T1 uden lokal hyphenation-pakke.
- Endelig kommando: `pdflatex -interaction=nonstopmode -halt-on-error main.tex` kørt to gange med output gemt i `build.log`.
- Resultat: bestået; `main.pdf` produceret som A4, 11 sider, 390707 bytes.
- Ikke-fatale advarsler: enkelte overfull/underfull boxes ved lange funktionsnavne og hyperref-bookmarkwarnings for matematik i overskrifter; ingen manglende references efter anden pass og intet tab af faglig tekst.

## Python validation

- Kommando: `python -m compileall -q scripts`.
- Resultat: bestået.
- Kommando: `python -c "from scripts.control import *; print('public import ok')"`.
- Resultat: bestået.
- Kommando: `python -m scripts.validate_scripts`.
- Resultat: bestået, 23 checks.
- Notebooken er efter brugerfeedback reduceret til et kommenteret kodeindeks og kørbare kontrolcases; den indeholder ikke længere teksttunge Markdown-sektioner eller den ugyldige prøve-celle med udefineret `s`.
- VS Code-loggen for `notebook controller is DISPOSED` peger på editorens kasserede kernelcontroller, ikke en Python-fejl i notebookens celler. Efter brugerens anvisning opretter projektet ikke et lokalt virtual environment eller en registreret kernelspec.
- Notebook verification: alle 4 kodeceller i `exam_toolbox.ipynb` er udført sekventielt uden cellefejl med tilgængelige dependencies.

## PDF verification

- `pdfinfo main.pdf` bekræfter A4 og 11 sider.
- `pdftotext`-kontrol fandt titel, metodefinder, symbolregister, PI-Lead-design, dynamisk feed-forward og oversigten over validerede funktioner i den byggede PDF.

## Kvalitetstjek

| Krav | Status | Dokumentation |
| ---- | ------ | ------------- |
| Alle inputfiler auditeret | Opfyldt | `input_audit.md` dækker 15 PDF'er |
| Alle forelæsninger læst ind i pensumrapport | Opfyldt | `full_curriculum_report.md` dækker L1-L13 |
| Analyse pr. eksamenssæt | Opfyldt | F21 er eneste identificerede sæt; del-2-filen er companion original |
| Ingen eksamensopgave sprunget over | Opfyldt | Q1-Q20 i `F21.md` og verificationtabel |
| Merged task taxonomy | Opfyldt | `merged_task_taxonomy.md` |
| Prioriterede notesektioner har alle krævede felter | Opfyldt | `sections/03_*.tex` til `07_*.tex`; verificationrapport |
| Python-kandidater vurderet | Opfyldt | `script_inventory.md` |
| Accepterede scripts importbare og testet | Opfyldt | 23 beståede checks |
| Python-dækning/non-coverage forklaret | Opfyldt | `python_coverage_report.md` |
| Notebook matcher validerede funktioner | Opfyldt | `notebook_inventory.md`; top-til-bund-kørsel |
| Scriptreferencer matcher noter | Opfyldt | `script_note_integration_report.md` |
| Alle eksamensopgaver mappet til noter | Opfyldt | `exam_verification_report.md` |
| Symbolregister | Opfyldt | `sections/02_symbolregister.tex` |
| PDF bygget | Opfyldt | `main.pdf`, `build.log` |

## Kendte begrænsninger og manuelle reviewpunkter

- Kildepakken indeholder kun ét samlet eksamenssæt; gentagelsesfrekvens på tværs af år kan ikke bestemmes.
- Hjælpemiddelregler og tilladelse til Python er ikke dokumenteret i inputmaterialet.
- Bode-/Nyquist-/blokdiagramdata skal kontrolleres visuelt i PDF'erne; scripts tolker ikke figurer.
- Matlab/Simulink-eksempelfiler og undervisningsdatasæt er ikke medleveret; Python er valideret mod formler og F21-cases, ikke mod original Matlabkode.
- F21 Q9 bruger afrundet overshootgrænse (`K=20` giver eksakt `12.0265 %`), og Q18's løsningstekst angiver en plantfase, der afviger lidt fra direkte evaluering af den trykte transferfunktion. Begge forhold er synlige i `script_validation_report.md`.

## Konklusion

Stopkriterierne er opfyldt for de tilgængelige kilder. De tilbageværende punkter er eksplicitte kilde-/brugsvilkår og ikke manglende leverancer.
