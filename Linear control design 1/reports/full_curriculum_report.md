# Fuld pensumrapport: Linear Control Design 1

## Kursusoverblik

Kurset omhandler lineær modellering og PID-baseret controllerdesign i feedbacksystemer. Den operative kæde er: fysisk system eller målinger -> lineær transferfunktion -> frekvens-/tidsanalyse -> stabilitetskrav -> P/PI/PI-Lead/Lag/feed-forward-design -> kontrol af begrænsninger, forstyrrelser og performance.

Notation anvendt her: `G(s)` er plant/system, `C(s)` controller, `L(s)=C(s)G(s)` loop transfer function ved unity feedback, `T(s)=L/(1+L)` closed-loop reference response og `S(s)=1/(1+L)` sensitivity. Et negativt feedback-loop antages, medmindre en konkret figur viser andet.

## Emne: Feedback, blokdiagrammer og håndtuning

### Kilder
- `1_Welcome_Lecture.pdf`, `2_block_control_concept.pdf`, `3_Laplace_TF.pdf`.

### Hvad skal man kunne?
- Identificere reference `r`, fejl `e`, kontrolsignal `u`, output `y`, måling `H(s)y` og disturbance.
- Reducere negative-feedback blokdiagrammer og forstå P, PI, PD/PID-håndtuning.
- Relatere højere proportional gain til hurtigere respons og potentielt mindre robusthed.

### Centrale formler og regler
- Negativ feedback: `Y/R = C G / (1 + C G H)` og loop `L=C G H`.
- `C_P(s)=K_P`; `C_PI(s)=K_P(1 + 1/(tau_i s))`; ideal PID `K_P(1+1/(tau_i s)+tau_d s)`.
- Integralled reducerer stationær fejl; differential/lead dæmper hurtige ændringer/overshoot, men kan forstærke støj.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `r,e,u,y` | reference, fejl, input, output | systemspecifik | Signaler |
| `C,G,H` | controller, plant, sensor | varierer | Transferfunktioner |
| `K_P,tau_i,tau_d` | PID-parametre | `-`, s, s | Positive i normal design |

### Standardmetoder
1. Marker summationsfortegn og forward/back branches.
2. Skriv loopproduktet og luk loopet med nævneren `1+L` ved negativ feedback.
3. Vælg P/PI/Lead ud fra hurtighed, stationær fejl og dæmpning.

### Typiske fejl og faldgruber
- At bruge unity-feedback-formlen når sensoren eller controlleren sidder i feedbackgrenen.
- At ignorere aktuatorsaturation ved aggressiv håndtuning.

## Emne: Laplace, differentialligninger og transferfunktioner

### Kilder
- `3_Laplace_TF.pdf`, `4_Frequency_and_Time_Analysis_WSol.pdf`, `5_Modelling.pdf`.

### Hvad skal man kunne?
- Omsætte en lineær ODE med nul begyndelsesbetingelser til `G(s)=Y(s)/U(s)`.
- Bestemme poler, nulpunkter, orden, stabilitet og DC gain.
- Anvende final value theorem, når stabilitetsbetingelserne holder.

### Centrale formler og regler
- `L{d^n y/dt^n}=s^n Y(s)` ved nul begyndelsesbetingelser.
- `K_ss=lim_(s->0) G(s)` for stabil stationær respons.
- `y_ss=lim_(s->0) sY(s)` kun hvis de relevante poler efter multiplikation ligger i venstre halvplan.
- RHP-pol giver ustabilitet; gentagne poler på imaginæraksen, fx dobbelt integrator, er ikke asymptotisk stabile.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `s=sigma+j omega` | Laplacevariabel | 1/s | `s=j omega` for frekvensrespons |
| `p,z` | pol, nulpunkt | 1/s | Rødder af nævner/tæller |
| `K_ss` | stationær/DC gain | output/input | Kræver relevant stabilitet |

### Standardmetoder
1. Laplace-transformér ODE'en og saml `Y(s)` og `U(s)`.
2. Faktoriser polynomier eller beregn rødder.
3. Kontrollér stabilitet, før slutværdi/DC-gain fortolkes fysisk.

### Typiske fejl og faldgruber
- At kalde et system stabilt alene fordi koefficienterne er positive.
- At bruge DC gain på en transferfunktion med integrator som om den var endelig.

## Emne: Første- og andenordens tidsrespons

### Kilder
- `4_Frequency_and_Time_Analysis_WSol.pdf`, `Lecture_09_PI_LEAD_design_specifications.pdf`.

### Hvad skal man kunne?
- Genkende tidskonstant, naturlig frekvens, dæmpningsforhold, overshoot, rise/settling time og bandwidth.
- Oversætte en specifikation til ønsket controlleradfærd.

### Centrale formler og regler
- Første orden: `G(s)=K_ss/(tau s+1)`, `omega_b=1/tau`, steprespons `K_ss(1-exp(-t/tau))`; 63.2 % nås ved `t=tau`.
- Standard anden orden: `G(s)=omega_n^2/(s^2+2 zeta omega_n s+omega_n^2)`.
- For `0<zeta<1`: `M_p=exp(-pi zeta/sqrt(1-zeta^2))`; 2 %-settling approksimeres `t_s ~= 4/(zeta omega_n)`.
- Bandwidth er -3 dB-punktet relativt til lavfrekvensasymptoten for en stabil closed-loop.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `tau,omega_b` | tidskonstant, breakfrekvens | s, rad/s | Første orden |
| `omega_n,zeta` | naturlig frekvens, damping ratio | rad/s, - | Anden orden |
| `M_p,t_r,t_s` | overshoot, rise/settling time | %, s, s | Steprespons |

### Standardmetoder
1. Sammenlign nævneren med standardformen.
2. Brug overshootkrav til `zeta` og tidskrav til `omega_n`.
3. Brug disse som designmål for crossover og phase margin.

### Typiske fejl og faldgruber
- At forveksle åben-loop crossover med closed-loop bandwidth; de er ofte nær hinanden, ikke identiske.

## Emne: Modellering og linearisering

### Kilder
- `2_block_control_concept.pdf`, `5_Modelling.pdf`.

### Hvad skal man kunne?
- Skelne white-, grey- og black-box modelling.
- Udlede lineære ODE'er fra fysiske love eller identificere enkel førsteordensmodel fra stepdata.
- Linearisere en ikke-lineær model omkring et relevant arbejdspunkt.

### Centrale formler og regler
- Lokal linearisering: `f(x,u) ~= f(x0,u0) + df/dx|0 (x-x0) + df/du|0 (u-u0)`.
- Førsteordens black-box: DC gain fra total outputændring/inputændring og `tau` fra 63.2 %-punktet.
- Modellen er kun gyldig nær arbejdspunktet og uden aktiverede ikke-lineariteteter såsom saturation.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `x0,u0` | arbejdspunkt | systemspecifik | Stationært punkt |
| `Delta x,Delta u` | små afvigelser | systemspecifik | Lineær model |

### Standardmetoder
1. Angiv antagelser og arbejdspunkt.
2. Udled/fit modelstruktur og parametre.
3. Kontrollér modellen mod andre målinger end fit-data.

### Typiske fejl og faldgruber
- At identificere fra store steps, der aktiverer rate- eller amplitudebegrænsning.

## Emne: Bode-plot, poler/nulpunkter og stabilitetsmarginer

### Kilder
- `4_Frequency_and_Time_Analysis_WSol.pdf`, `6_Bode_plot&Stability.pdf`, `Lecture_07_Nyquist plot and stability.pdf`.

### Hvad skal man kunne?
- Konstruere eller tolke magnitude og phase for `G(j omega)`.
- Genkende LHP/RHP-poler og nulpunkter fra hældning og fase.
- Aflæse gain margin, phase margin og crossover frequency.

### Centrale formler og regler
- `M_dB=20 log10 |G(j omega)|`, `|G|=10^(M_dB/20)`.
- En LHP-pol giver efter break `-20 dB/dec` og samlet `-90 deg`; et LHP-nulpunkt giver `+20 dB/dec` og `+90 deg`.
- RHP-nulpunkt har samme magnitudeeffekt som LHP-zero, men negativ fase; RHP-pol omvendt faseeffekt.
- `omega_c`: `|L(j omega_c)|=1`; `gamma_M=180 deg + angle L(j omega_c)`.
- Ved phase crossover `angle L(j omega_pi)=-180 deg`, er gain margin faktor `1/|L(j omega_pi)|`.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `omega_c,omega_pi` | gain-/phase-crossover | rad/s | Læses fra open loop |
| `gamma_M,K_M` | phase-/gain margin | deg, faktor/dB | Positiv margin ønskes normalt |

### Standardmetoder
1. Faktoriser `G(s)` i gain, integratorer og første-/andenordensfaktorer.
2. Markér break frequencies og summer hældnings-/fasebidrag.
3. Brug open-loop magnitude og fase til closed-loop stabilitetsvurdering.

### Typiske fejl og faldgruber
- At læse gain i dB som lineær gain.
- At afgøre RHP/LHP fra magnitude alene; fasen er nødvendig.

## Emne: Nyquist og åbent-loop-ustabile systemer

### Kilder
- `Lecture_07_Nyquist plot and stability.pdf`, `Lecture_10_Unstable_systems (1).pdf`.

### Hvad skal man kunne?
- Vurdere closed-loop-stabilitet for open-loop stabile og ustabile planter via encirclements af `-1`.
- Vælge proportionalt stabiliseringsgain ud fra skæring med negativ realakse.

### Centrale formler og regler
- Med undervisningens fortegn: `Z=P+N`, hvor `P` er antal RHP-poler i open loop og `N` er netto clockwise encirclements af `-1`; stabilitet kræver `Z=0`.
- Har plant én RHP-pol, kræves én counter-clockwise encirclement (`N=-1`).
- Multiplikation med positiv `K_P` skalerer Nyquist-kurven radialt; negativ gain spejler om origo.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `P,N,Z` | RHP-poler, CW encirclements, RHP closed-loop poles | - | Kontrollér fortegnskonvention |
| `K_PS` | stabiliseringsgain | - | Kan kræve bestemt fortegn |

### Standardmetoder
1. Tæl open-loop RHP-poler.
2. Aflæs kurveretning og realakseskæring.
3. Skalér til det nødvendige antal encirclements; verificér efterfølgende performance.

### Typiske fejl og faldgruber
- At anvende stabil-plant Bode-marginargument uden at medtage open-loop RHP-poler.

## Emne: P-, PI- og PI-Lead-controllerdesign

### Kilder
- `Lecture_08_PI_LEAD_design.pdf`, `Lecture_09_PI_LEAD_design_specifications.pdf`.

### Hvad skal man kunne?
- Designe controller ud fra ønsket `gamma_M`, `omega_c` og stationær fejl.
- Beregne PI- og lead-parametre samt `K_P` via fase- og magnitudebalance.

### Centrale formler og regler
- `C_PI(s)=K_P (tau_i s+1)/(tau_i s)`, `N_i=omega_c tau_i`, `phi_PI=atan(N_i)-90 deg`.
- `C_lead(s)=(tau_d s+1)/(alpha tau_d s+1)`, `0<alpha<1`.
- `phi_lead,max=asin((1-alpha)/(1+alpha))`; centrer ved `omega_c` med `tau_d=1/(omega_c sqrt(alpha))`.
- Fasebalance: `angle G(j omega_c)+phi_PI+phi_lead=-180 deg+gamma_M`.
- Magnitudebalance: vælg `K_P`, så `|C(j omega_c)G(j omega_c)|=1`.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `alpha` | lead pole/zero-forhold | - | `0<alpha<1` |
| `N_i` | PI-zero placering relativt til crossover | - | Typisk 2-10; slides foreslår 3 |
| `tau_i,tau_d` | PI/lead tidskonstant | s | Positive |

### Standardmetoder
1. Vurder om integrator kræves for stationær fejl.
2. Vælg `N_i`, `alpha` eller påkrævet phase boost.
3. Find ønsket crossover ved fasebalance eller anvend givet `omega_c`.
4. Beregn tidskonstanter og gain; kontroller respons og actuator demand.

### Typiske fejl og faldgruber
- At glemme PI-delens negative fasebidrag.
- At vælge `alpha >= 1` og stadig kalde delen lead.

## Emne: Systemtype og stationær fejl

### Kilder
- `Lecture_08_PI_LEAD_design.pdf`, `Lecture_09_PI_LEAD_design_specifications.pdf`, `Lecture_12_Disturbances_sensitivity_prefilters.pdf`.

### Hvad skal man kunne?
- Bestemme type-n fra antal integratorer i loopet.
- Beregne stationær reference- eller disturbancefejl via final value theorem og korrekt signalvej.

### Centrale formler og regler
- Unity feedback: `E/R=S=1/(1+L)`.
- Unit step: `e_ss=lim_(s->0) 1/(1+L(s))`, hvis lukket loop er stabilt.
- Type 0: endelig ikke-nul stepfejl med endelig gain; type 1: nul stepfejl; type 2: nul rampfejl.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `S,T` | sensitivity, complementary sensitivity | - | `S+T=1` ved unity feedback |
| `e_ss` | stationær fejl | outputenhed | Afhænger af definition af fejl |

### Standardmetoder
1. Udled den faktiske transferfunktion til den efterspurgte fejl.
2. Indsæt step/ramp og brug slutværdi.
3. Kontroller både stabilitet og om measurement noise ændrer fejlfortolkningen.

### Typiske fejl og faldgruber
- At antage `e=r-y`, når diagrammets fejlsignal indeholder forstyrret måling.

## Emne: Begrænsninger, windup og Lag

### Kilder
- `Lecture_11_Limited_systems (1).pdf`; P-Lead-Lag-opgave i `F21.pdf` Q17.

### Hvad skal man kunne?
- Genkende rate limitation og saturation som ikke-lineariteteter.
- Forklare integrator windup og vælge mitigation: integrator limit, prefilter, Lag i stedet for PI eller anti-windup.
- Designe P-Lead-Lag med phase margin.

### Centrale formler og regler
- Rate limit: `|du/dt| <= R_max`; saturation: `u_min <= u_sat <= u_max`.
- Lag: `C_lag(s)=(tau_i s+1)/(tau_i s/beta+1)`, `beta>1`.
- Ved `N_i=omega_c tau_i`: `phi_lag=atan(N_i(1-beta)/(1+beta N_i^2))`.
- Lag forbedrer lavfrekvent gain, men giver ikke nødvendigvis nul stepfejl.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `R_max,u_min,u_max` | actuatorgrænser | input/s, input | Ikke-lineære |
| `beta` | Lag-forhold | - | Skal være større end 1 |

### Standardmetoder
1. Undersøg om controllerkrav aktiverer limit.
2. Ved Lag-design: brug fasebalance, løs `beta`, kontrollér `beta>1`.
3. Simulér/valider store og små referencesignaler separat.

### Typiske fejl og faldgruber
- At forvente nul stationær fejl fra Lag som fra PI.
- At validere en lineær controller kun på små signaler, når opgaven kræver stor-step stabilitet.

## Emne: Disturbances, sensitivity og prefilter

### Kilder
- `Lecture_12_Disturbances_sensitivity_prefilters.pdf`.

### Hvad skal man kunne?
- Udlede transferfunktion fra hver disturbance til output/fejl med superposition.
- Fortolke `S` og `T` i frekvensdomænet.
- Forklare at reference-prefilter former tracking, men ikke loopstabilitet eller disturbance rejection.

### Centrale formler og regler
- Outputdisturbance efter plant: `Y/D=S`; plant-inputdisturbance: `Y/D=G S`.
- Reference: `Y/R=T`; measurement noise i standardloop: `Y/N=-T`.
- Referenceprefilter: `Y/R=F T`, mens `L`, marginer og disturbance sensitivities er uændrede.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `d,n,F` | disturbance, noise, prefilter | varierer | Placering/fortegn afgørende |
| `G_yd` | output sensitivity til disturbance | output/disturbance | Opgavespecifik |

### Standardmetoder
1. Sæt øvrige input til nul.
2. Reducér den valgte signalvej med det samme loop i nævneren.
3. Brug DC eller Bode-værdi til steady-state/frekvensvurdering.

### Typiske fejl og faldgruber
- At blande output- og inputdisturbance sammen.

## Emne: Feed-forward

### Kilder
- `Lecture_13_Feed_forward.pdf`; `F21.pdf` Q20.

### Hvad skal man kunne?
- Designe reference-feed-forward for tracking og disturbance-feed-forward for målte forstyrrelser.
- Kontrollere properness, stabilitet og modelusikkerhed.

### Centrale formler og regler
- Hvis disturbancebidraget er `-D(s)d+G(s)F_d(s)d`, vælges ideelt `F_d=D/G`; ved plusfortegn vælges `F_d=-D/G`.
- Med feedback bliver restbidraget `G_yd=(sigma_D D+G F_d)/(1+C G)`.
- En dynamisk invers skal være proper og stabil; ellers anvendes statisk/DC feed-forward eller stabilt lavpasfilter.

### Symboler
| Symbol | Betydning | Enhed | Kommentar |
| ------ | --------- | ----- | --------- |
| `F,F_d` | reference-/disturbance feed-forward | passende ratio | Uden for stabilitetsloop |
| `sigma_D` | disturbance-fortegn | `+/-1` | Fra diagram |

### Standardmetoder
1. Udled den relevante forward plant path og fortegnet.
2. Sæt nominalt disturbance- eller referencebidrag lig ønsket værdi.
3. Kontroller realiserbarhed og robusthed; feedback skal stadig håndtere mismatch.

### Typiske fejl og faldgruber
- At invertere en RHP-zero eller en improper plant uden filter.
- At påstå perfekt rejection ved modelusikkerhed eller umålt disturbance.

## Svagt eller ikke dokumenteret

- Heuristisk Ziegler-Nichols nævnes, men F21 fokuserer på algebra, plotfortolkning og design; det prioriteres lavere i slutnoterne.
- Mandatory REGBOT assignment og cascaded balance-control omtales, men er ikke direkte testet i det tilgængelige eksamenssæt.
- Matlab/Simulink bruges i undervisningen; kildepakken indeholder ikke scripts/data til reproduktion.

## Notations- og dokumentationsusikkerheder

- `F21.pdf` stammer fra 31. maj 2021 for Q1-Q10, mens den vedhæftede questionnaire for Q11-Q20 er dateret 6. maj 2026 og indgår i samme samlede løsnings-PDF. Analysen refererer til spørgsmålene som F21, fordi det er filens samlede identifikation.
- Flere slides viser formler som grafik, hvorfor de operationelle standardformler ovenfor er normaliserede fortolkninger af det viste designstof.
- Hjælpemidler og om Python må anvendes under eksamen er ukendt.
