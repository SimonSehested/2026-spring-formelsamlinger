# Merged task taxonomy: Linear Control Design 1

## Grundlag og prioritering

Der findes nu fem identificerede eksamenskilder: S20, F21, 2022, E23 og F25.
S20, F21, E23 og F25 har løsningsnoter eller markerede svar; 2022-filen bruges som
opgavetypekilde uden facit, og Q1/Q10 i den fil er ikke brugbart tekstudtrukket.
Prioritet vurderes ud fra gentagelse mellem sættene, centralitet i forelæsningerne
og beregnings-/fejlrisiko.

| Opgavetype | Emne | Genkendelsessignaler | Kilder/eksamensopgaver | Hurtig metode | Nødvendige formler | Symboler/input | Support mode | Scriptkandidat | Typiske fælder | Hurtigtjek |
| ---------- | ---- | -------------------- | ---------------------- | ------------- | ------------------ | -------------- | ------------ | -------------- | -------------- | ---------- |
| Blokdiagramreduktion | Feedback | Blokke, summer, feedback | S20 Q3; F21 Q1,Q16,Q19; E23 Q1,Q2; F25 Q1,Q2,Q15; L2 | Find forward paths og loop | `forward/(1+loop)` | Fortegn, blokke | `notes_only` | Nej | Forkert signal/fortegn | Slå sidegren fra |
| Fysisk model til TF | Modellering | RLC/masser/ODE/state-space | S20 Q1,Q2; F21 Q2,Q7,Q8,Q12; 2022 Q8,Q9; E23 Q6,Q7; F25 Q3,Q7,Q20; L2-L5 | Love/state -> ODE -> Laplace | `G=Y/U` | Parametre, initialvilkår | `notes_only`/`script_assisted` | Kun TF-kontrol | Springe udledning over | Poler og enheder |
| Initial-/slutværdi | Tidsrespons | `y(0)`, `lim y(t)`, sammensat input | S20 Q4; F25 Q1; L3-L4 | Skriv `Y=GU`, brug IVT/FVT | `lim sY` | `G,U,Y` | `script_assisted` | Ja | Bruge kun DC-gain | Stabilitet først |
| Poler/zeros/stabilitet | Analyse | TF, ODE eller parameter | S20 Q16; F21 Q8,Q12; 2022 Q8,Q9; E23 Q6,Q7; F25 Q3; L4,L6 | Faktoriser/beregn rødder | RHP-regel, koefficientkrav | Tæller/nævner | `script_assisted` | Ja | Overse origo-poler/zeros | Alle RHP/LHP |
| Systemtype og static constants | Feedback | Type 0/1/n, `K0`, integrator | 2022 Q9; E23 Q3,Q4,Q5,Q9,Q12; F25 Q4; L8,L9 | Saml `L(s)`, tæl origo-poler | `lim s^nL(s)` | Loop TF | `notes_only` | Nej | `L(0)=inf` som `K0` | Type før DC |
| Bode til/fra TF | Frekvens | dB/phase eller s-plan | S20 Q6,Q8,Q13; F21 Q3,Q5,Q10; 2022 Q4,Q5; E23 Q8,Q10,Q11,Q16; F25 Q5,Q10; L4,L6 | Breaks, slope, phase | `20log10|G|` | Plotværdier | `notes_only` | Nej | dB som gain; RHP | Netto slope |
| Bandwidth/damped frequency | Tids/frekvens | `-3 dB`, peakperiode | S20 Q7,Q8; E23 Q17; L4,L9 | Aflæs niveau eller periode | `|T|=|T0|/sqrt2`, `2pi/Td` | Plot | `notes_only` | Nej | Absolut 0 dB | DC-niveau først |
| P-gain og margin | Stabilitet/design | `K_P`, PM/GM | S20 Q9; F21 Q4,Q6,Q11,Q15; 2022 Q6,Q11,Q15; E23 Q10,Q13; F25 Q9,Q11; L6-L8 | Fasemål -> magnitudegain | `gamma_M=180+phi`; dB | TF/plot, mål | `script_assisted` | Ja | Grænsegain inklusiv | Closed-loop poles |
| Nyquist-stabilitet | Stabilitet | Kurve, `-1`, RHP-pol | S20 Q12,Q17,Q18; F21 Q13; 2022 Q12; F25 Q13,Q18; L7,L10 | Tæl P og krævet encirclement | `Z=P+N` | Retning/skæring | `notes_only` | Nej | Forkert retning | Skaleret skæring |
| Nyquist phase margin | Stabilitet | Unit-circle point | F21 Q14; L7 | `atan2` af punkt | `180+phi_c` | `(Re,Im)` | `script_assisted` | Ja | Radian/grad | Kvadrant |
| Stationær referencefejl | Performance | Unit step, type-0/n, ramp/parabel | F21 Q16,Q19; 2022 Q16; E23 Q18-Q20; F25 Q4,Q14,Q15,Q18; L8,L9,L12 | Udled `E/R`, tag DC | Final value, static constants | DC gains | `script_assisted` | Ja for standardloop | Output i stedet for error | Fejl mellem 0 og 1 |
| Settling/steprespons | Tidsrespons | `M_p`, `K`, `t_s`, stepplot | S20 Q4,Q5,Q8; F21 Q9; 2022 Q2,Q3,Q14; E23 Q16,Q17; F25 Q6,Q20; L4,L9 | Match standardform/dominant pol | `M_p(zeta)`, `-tau ln eps` | Nævner/plot | `script_assisted` | Ja | 1% vs 2%; hurtig pol | Dominant pol |
| P-Lead og Leadbidrag | Controllerdesign | `alpha`, `tau_d`, lead zero/pole | S20 Q10,Q11,Q15; 2022 Q13,Q20; E23 Q14,Q15; L8,L9 | Center lead ved crossover | `1/(tau_d sqrt(alpha))` | `alpha,wc` | `script_assisted` | Nej særskilt | Zero/pole byttes | `0<alpha<1` |
| PI-Lead-design | Controllerdesign | `omega_c`, PM, `N_i`, `alpha` | S20 Q14; F21 Q18; 2022 Q17,Q19; F25 Q16; L8,L9 | Fasebalance -> gain | PI/lead equations | TF/specs | `script_primary` | Ja | PI-fase glemt | `0<alpha<1` |
| Ziegler-Nichols PID | Controllerdesign | `K_u`, `P_u`, sustained oscillation | F25 Q8; L8/L9 | Ultimate period -> PID table | `Kp=.6Ku`, `Ti=Pu/2` | `Ku,Pu` | `script_assisted` | Ja | Vende `2pi/omega` | Gain/tider |
| P-Lead-Lag-design | Limits/design | `beta`, Lag, PM | S20 Q17,Q18; F21 Q17; F25 Q17; L11 | Krævet lagfase -> `beta` | Lag phase | `alpha,N_i` | `script_primary` | Ja | Lag=PI | `beta>1` |
| Limited systems/windup | Ikke-linearitet | saturation/rate | F25 Q12; L11 | Find limit, mitigér | limit definitions | actuator data | `notes_only` | Nej | Lineær konklusion | Små/store steps |
| Disturbance/sensitivity | Robusthed | `d`, `S`, Bode | S20 Q19; E23 Q19,Q20; L12 | Superposition og loop | `S=1/(1+L)` | path/fortegn | `notes_only` | Nej | Forkert path | DC sense |
| Prefilter | Referenceformning | `F(s)` før loop | L11,L12 | Form referencepath | `Y/R=FT` | ønsket peak | `notes_only` | Nej | Ændre marginpåstand | Loop uændret |
| Feed-forward rejection/tracking | Robusthed | Målt `d`, `F_d`, reference-invers | F21 Q20; 2022 Q18; F25 Q19; L13 | Annulér disturbancepath eller inverter plant med filter | `F_d=-sigma_D D/G`, `1/(G(tau_f s+1))` | fortegn, `G,D` | `script_assisted` | Ja | improper/ustabil inverse | Numerator/DC nul |

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
