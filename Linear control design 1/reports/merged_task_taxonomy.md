# Merged task taxonomy: Linear Control Design 1

## Grundlag og prioritering

Der findes ét identificeret eksamenssæt, F21, med 20 spørgsmål og solution. Prioritet vurderes derfor ud fra antal opgaver i sættet, centralitet i forelæsningerne og beregnings-/fejlrisiko, ikke gentagelse mellem årgange.

| Opgavetype | Emne | Genkendelsessignaler | Kilder/eksamensopgaver | Hurtig metode | Nødvendige formler | Symboler/input | Support mode | Scriptkandidat | Typiske fælder | Hurtigtjek |
| ---------- | ---- | -------------------- | ---------------------- | ------------- | ------------------ | -------------- | ------------ | -------------- | -------------- | ---------- |
| Blokdiagramreduktion | Feedback | Blokke, summer, feedback | F21 Q1, Q16; L2 | Find forward paths og loop | `forward/(1+loop)` | Fortegn, blokke | `notes_only` | Nej | Forkert signal/fortegn | Slå sidegren fra |
| Fysisk model til TF | Modellering | RLC/masser/ODE | F21 Q2, Q7, Q8, Q12; L2-L5 | Love -> ODE -> Laplace | `G=Y/U` | Parametre, initialvilkår | `notes_only`/`script_assisted` | Kun TF-kontrol | Springe udledning over | Poler og enheder |
| Poler/zeros/stabilitet | Analyse | TF eller ODE | F21 Q8, Q12; L4,L6 | Faktoriser/beregn rødder | RHP-regel | Tæller/nævner | `script_assisted` | Ja | Overse origo-poler | Alle RHP/LHP |
| Bode til/fra TF | Frekvens | dB/phase eller s-plan | F21 Q3,Q5,Q10; L4,L6 | Breaks, slope, phase | `20log10|G|` | Plotværdier | `notes_only` | Nej | dB som gain; RHP | Netto slope |
| P-gain og margin | Stabilitet/design | `K_P`, PM/GM | F21 Q4,Q6,Q11,Q15; L6-L8 | Fasemål -> magnitudegain | `gamma_M=180+phi`; dB | TF/plot, mål | `script_assisted` | Ja | Grænsegain inklusiv | Closed-loop poles |
| Nyquist-stabilitet | Stabilitet | Kurve, `-1`, RHP-pol | F21 Q13; L7,L10 | Tæl P og krævet encirclement | `Z=P+N` | Retning/skæring | `notes_only` | Nej | Forkert retning | Skaleret skæring |
| Nyquist phase margin | Stabilitet | Unit-circle point | F21 Q14; L7 | `atan2` af punkt | `180+phi_c` | `(Re,Im)` | `script_assisted` | Ja | Radian/grad | Kvadrant |
| Stationær referencefejl | Performance | Unit step, type-0/n | F21 Q16,Q19; L8,L9,L12 | Udled `E/R`, tag DC | Final value | DC gains | `script_assisted` | Ja for standardloop | Output i stedet for error | Fejl mellem 0 og 1 |
| Andenordens overshoot | Tidsrespons | `M_p`, `K`, step | F21 Q9; L4,L9 | Match standardform | `M_p(zeta)` | Nævner | `script_assisted` | Ja | Hurtighed vs damping | `zeta` interval |
| PI-Lead-design | Controllerdesign | `omega_c`, PM, `N_i` | F21 Q18; L8,L9 | Fasebalance -> gain | PI/lead equations | TF/specs | `script_primary` | Ja | PI-fase glemt | `0<alpha<1` |
| P-Lead-Lag-design | Limits/design | `beta`, Lag, PM | F21 Q17; L11 | Krævet lagfase -> `beta` | Lag phase | `alpha,N_i` | `script_primary` | Ja | Lag=PI | `beta>1` |
| Limited systems/windup | Ikke-linearitet | saturation/rate | L11 | Find limit, mitigér | limit definitions | actuator data | `notes_only` | Nej | Lineær konklusion | Små/store steps |
| Disturbance/sensitivity | Robusthed | `d`, `S`, Bode | L12 | Superposition og loop | `S=1/(1+L)` | path/fortegn | `notes_only` | Nej | Forkert path | DC sense |
| Prefilter | Referenceformning | `F(s)` før loop | L11,L12 | Form referencepath | `Y/R=FT` | ønsket peak | `notes_only` | Nej | Ændre marginpåstand | Loop uændret |
| Feed-forward rejection | Robusthed | Målt `d`, `F_d` | F21 Q20; L13 | Annulér disturbancepath | `F_d=-sigma_D D/G` | fortegn, `G,D` | `script_assisted` | Ja | improper/ustabil inverse | Numerator nul |

## Opgavetype: Blokdiagramreduktion og stationær fejl

### Kommer fra
- F21 Q1 og Q16; forelæsning 2, 9 og 12.

### Brug når
- Der vises et feedbackdiagram, eller fejlsignal/output skal bestemmes fra et bestemt input.

### Standardopskrift
1. Markér efterspurgt input og output; sæt øvrige input til nul.
2. Skriv loopprodukt og hver forward contribution med korrekt fortegn.
3. Reducér algebraisk og anvend eventuelt `s->0` for unit-step slutværdi.

### Hvad skal noterne dække?
- Ikke-unity feedback, signalfortegn og final value-betingelsen.

### Hvad kan Python realistisk dække?
- DC-kontrol for en allerede udledt standard-unity-loop transferfunktion.

### Hvad kan Python ikke dække?
- Automatisk fortolkning af diagramfigurer eller valg af fejldefinition.

### Prioritet
Høj: grundlag for flere spørgsmål og for disturbance/feed-forward.

## Opgavetype: Model, TF, poler og tidsrespons

### Kommer fra
- F21 Q2, Q7-Q10 og Q12; forelæsning 2-5.

### Brug når
- En ODE, fysisk model, steprespons eller rational transferfunktion gives.

### Standardopskrift
1. Udled `G(s)` fra model eller data.
2. Find poler/zeros og vurder stabilitet.
3. Udled DC og tidsresponsmetrics under de relevante stabilitetsantagelser.

### Hvad skal noterne dække?
- Laplace, første-/andenorden, modelantagelser og RHP/origo-stabilitet.

### Hvad kan Python realistisk dække?
- Rødder, DC-gain og andenordensovershoot efter at brugeren selv har opstillet polynomierne.

### Hvad kan Python ikke dække?
- Fysisk modellering eller Bodefigurens signalfortolkning.

### Prioritet
Høj: seks eksamensspørgsmål og fundament for design.

## Opgavetype: Bode/P-gain/stabilitetsmargin

### Kommer fra
- F21 Q3-Q6, Q11, Q14-Q15; forelæsning 4, 6-8.

### Brug når
- Opgaven viser Bode/Nyquist eller spørger om PM, GM, gain/stabilitet.

### Standardopskrift
1. Bestem om input er en figur eller en analytisk transferfunktion.
2. Find ønsket phase/crossover; konvertér magnitude korrekt mellem dB og faktor.
3. Kontrollér margin eller closed-loop poler for valgte gain.

### Hvad skal noterne dække?
- Hældning/fase, dB-konvertering, PM/GM og Nyquist-punkt.

### Hvad kan Python realistisk dække?
- Evaluere en kendt TF og regne `atan2`, gain og closed-loop poler.

### Hvad kan Python ikke dække?
- Robust aflæsning af et indlejret plot eller Nyquist-encirclement fra billede.

### Prioritet
Høj: flest direkte F21-spørgsmål.

## Opgavetype: Nyquist-stabilisering af ustabil plant

### Kommer fra
- F21 Q13; forelæsning 7 og 10.

### Brug når
- Open-loop har RHP-poler og Nyquistkurvens retning/skæring opgives.

### Standardopskrift
1. Tæl `P`.
2. Kræv `N=-P` for stabilt closed loop efter kursuskonventionen.
3. Skalér kurven med gain og kontroller om den passerer `-1` korrekt.

### Hvad skal noterne dække?
- Fortegn for clockwise/counter-clockwise og hvorfor almindelig margin ikke er nok.

### Hvad kan Python realistisk dække?
- Polkontrol efter en manuelt valgt gain; ikke kernevurderingen.

### Hvad kan Python ikke dække?
- Kurvens orientation og omkredsninger fra figurinput.

### Prioritet
Høj: central metode for ustabile systemer og dokumenteret eksamensspørgsmål.

## Opgavetype: PI-Lead og P-Lead-Lag

### Kommer fra
- F21 Q17-Q18; forelæsning 8, 9 og 11.

### Brug når
- Controllerformen og ønsket `omega_c`/`gamma_M` eller Lag-parameter gives.

### Standardopskrift
1. Beregn plantfase ved crossover og contributions fra allerede valgte controllerdele.
2. Løs for manglende phase contribution (`alpha` eller `beta`).
3. Beregn tidskonstanter og `K_P`; kontroller intervalkrav og open-loop target.

### Hvad skal noterne dække?
- Komplet fase-/magnitudebalance, parametergrænser og forskel på PI og Lag.

### Hvad kan Python realistisk dække?
- Direkte, transparent beregning fra opgivne parametre og polynomial plant.

### Hvad kan Python ikke dække?
- Valget af controllerstruktur, crossover eller acceptabel actuatorbelastning.

### Prioritet
Høj: tunge designberegninger, stærkt repræsenteret i de afsluttende forelæsninger.

## Opgavetype: Disturbance, sensitivity, prefilter og feed-forward

### Kommer fra
- F21 Q20; forelæsning 12-13.

### Brug når
- En ekstern forstyrrelse eller referencefilter indgår i blokdiagrammet.

### Standardopskrift
1. Sæt øvrige input til nul og udled den relevante signalvej.
2. For feed-forward: vælg fortegn så disturbance contributions annullerer nominalt.
3. Kontroller properness/stabilitet; beskriv modelusikkerhed og resterende feedbackrolle.

### Hvad skal noterne dække?
- `S`, `T`, disturbanceplacement, prefiltereffekt og feed-forward-fortegn.

### Hvad kan Python realistisk dække?
- Polynomialberegning af en ideal feed-forward ratio og kontrollere nominal annullering efter manuelt valg af fortegn.

### Hvad kan Python ikke dække?
- Fortegn i en ukendt figur, målelighed eller modelrobusthed.

### Prioritet
Middel/høj: én direkte eksamensopgave, men centrale afsluttende læringsmål.
