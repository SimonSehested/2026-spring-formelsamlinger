# Style Guide for 22050 Combined Danish Formula Collection

## Formål

Skriv som en hurtig dansk eksamensmanual for en studerende, der skal svare rigtigt på 4 minutter.

Dokumentet må ikke ligne forelæsningsnoter. Det skal ligne et præcist opslagsværk med formler, regler og beslutningshjælp.

## Standardformat for en formel

Brug dette mønster, når det passer:

```tex
\subsubsection{Søgbart navn, dansk og evt. engelsk alias}
\[
...
\]
\textbf{Brug når:} ...
\textbf{Symboler:} ...
\textbf{Enheder:} ...
\textbf{Hurtigtjek:} ...
\textbf{Typiske fælder:} ...
```

Forklar alle symboler, der optræder i ligningen. Hvis et symbol er dimensionsløst, skriv det.

## Sprog og søgbarhed

- Skriv på dansk.
- Brug danske fagord først.
- Bevar engelske aliaser i overskrifter, når de matcher eksamens- eller kursusord.
- Overskrifter skal være konkrete: `Slutværdisætningen`, `Bodeplot fra poler og nulpunkter`, `Aliasfrekvens`.
- Undgå overskrifter som `Teori`, `Vigtigt`, `Resultat`.

## Længde

- Normalt højst 1-3 korte sætninger efter en formel.
- Opskrifter må normalt have 3-7 trin.
- Brug tabeller frem for tekst, når det gør opslag hurtigere.
- Undgå eksempler, medmindre de viser en typisk eksamensfælde.

## Sandt/falsk-regler

Tilføj korte regler, der hjælper med at afgøre udsagn:

- Hvis én delpåstand er falsk, er hele svarmuligheden falsk.
- Tjek specialtilfælde før lang algebra.
- Tjek enheder, fortegn, grænser og antagelser.
- Tjek om en sætning kræver kausalitet, stabilitet eller nul begyndelsesbetingelser.
- Skeln altid mellem Hz og rad/s.

## Symboler og enheder

- Alle centrale symboler skal registreres i symboloversigten.
- Brug ens notation:
  - \(t\): tid, s
  - \(\omega\): vinkelfrekvens, rad/s
  - \(f\): frekvens, Hz
  - \(s\): kompleks frekvens, 1/s
  - \(x(t)\): inputsignal
  - \(y(t)\): outputsignal
  - \(h(t)\): impulsrespons
  - \(H(s)\): overføringsfunktion
  - \(H(j\omega)\): frekvensrespons
  - \(X(\omega)\): Fouriertransformation
  - \(X(s)\): Laplace-transformation
  - \(u(t)\): enhedstrin
  - \(\delta(t)\): Dirac-impuls
- Brug enhedsfeltet aktivt. Skriv `dimensionsløs`, `samme som signal`, eller `afhænger af signal` når en fysisk enhed ikke er fast.

## Python-hjælpere

Behold Python-henvisninger, men skriv dem som sekundær støtte:

- hvornår scriptet passer
- inputformat
- output
- manuel kontrol
- hvornår scriptet ikke må bruges

## Forbudt stil

Undgå:

- lange beviser
- lange udledninger
- historiske forklaringer
- brede forelæsningsafsnit
- materiale uden eksamensdækning
- dubletter der ikke gør opslag hurtigere
- Markdown i `.tex`-filer

## Usikkerhed

Hvis kilden ikke understøtter en formel eller regel klart, skriv:

```tex
% TODO: verify from source
```
