# Exam Task Taxonomy

This taxonomy groups recurring exam work by problem type rather than by lecture topic. Each task type has a matching searchable recipe in `sources/*.tex`.

| Task type | Common wording / keywords | Required formulas or rules | Fast method | Covered in |
|---|---|---|---|---|
| Isotope particle count | isotope, mass number, neutron, proton, electron | \(A=Z+N\) | Read \(Z\), compute \(N=A-Z\), adjust electrons for charge | `01`, isotope notation |
| Ionic formula and naming | ammonium nitrate, phosphate, sulfate, charge neutrality | \(\sum q_in_i=0\) | Balance ion charges to zero; use polyatomic ion table | `01`, ionic formulas |
| Molar mass and mass percent | molar mass, mass percentage, lithium percent | \(n=m/M\), \(w_i=m_i/m_{\mathrm{total}}\) | Sum formula mass; compute element fraction | `01`, core formulas |
| Empirical/molecular formula | empirical formula, sum formula, percent composition | mole ratios, \(M_{\mathrm{molecular}}=kM_{\mathrm{empirical}}\) | Assume 100 g, convert to moles, divide by smallest | `01`, empirical recipe |
| Limiting reactant and yield | limiting, excess, theoretical yield, udbytte | \(\xi_i=n_i/\nu_i\) | Convert to moles, compare extents, scale product | `01`, stoichiometry recipe |
| Net ionic precipitation | precipitate, bundfald, mixing solutions | spectator-ion cancellation, \(Q_{sp}\) | Dissociate, form solid, cancel spectators | `02`, net ionic recipe |
| Redox balancing | balance redox, acidic/basic, permanganate, oxalate, iodide | half-reaction method | Balance atoms/O/H/charge/electrons, neutralize in base | `02`, redox recipe |
| Gas law state change | heated gas tank, pressure, volume, temperature | \(pV=nRT\), combined gas law | Convert \(T\) to K; apply fixed-\(n\) relation | `02`, gas recipe |
| Gas stoichiometry | gas volume in reaction | \(n=pV/RT\) plus coefficients | Convert gas data to moles before stoichiometry | `02`, `99` |
| Reaction enthalpy | formation enthalpy, Hess, combustion | \(\Delta H^\circ=\sum\nu\Delta H_f^\circ(\mathrm{prod})-\sum\nu\Delta H_f^\circ(\mathrm{react})\) | Balance; products minus reactants; reverse/multiply for Hess | `03`, enthalpy recipe |
| Gibbs spontaneity | positive \(\Delta H\), positive \(\Delta S\), temperature | \(\Delta G=\Delta H-T\Delta S\) | Use sign table and switch temperature | `03`, spontaneity recipe |
| Equilibrium from thermodynamics | \(\Delta G^\circ\), \(K\), spontaneous | \(\Delta G^\circ=-RT\ln K\) | Convert units; solve for \(K\) or sign | `03`, `07` |
| Quantum numbers | allowed values, orbital | \(n,\ell,m_\ell,m_s\) ranges | Check each quantum-number rule | `04`, quantum numbers |
| Electron configuration | configuration, valence electrons, ions | Aufbau, Pauli, Hund | Count electrons; fill orbitals; remove \(ns\) first for transition cations | `04`, configuration recipe |
| Periodic trends | largest ionic radius, ionization energy | trend rules, isoelectronic \(Z\) rule | Check isoelectronic first, then period/group trends | `04`, trend recipe |
| Lewis structure/formal charge | nitrate, oxalate, resonance, formal charge | valence count, FC formula | Count electrons, build octets, calculate FC | `05`, Lewis recipe |
| VSEPR and bond angles | planar, non-planar, hydrazine angle, pyramidal | steric number, VSEPR table | Count domains/lone pairs, read geometry and angle | `05`, VSEPR recipe |
| Molecular polarity | polar, dipole, bond polarity | vector dipole sum | Determine bond polarity and symmetry cancellation | `05`, polarity |
| Intermolecular force ranking | vapor pressure, boiling point, hydrogen bond | H-bond criteria, dispersion/polarity | Identify H-bonding, polarity, molar mass | `06`, vapor pressure recipe |
| Unit-cell calculation | BCC, FCC, density, unit-cell volume | \(Z\), \(\rho=ZM/(N_Aa^3)\), radius relations | Identify cell, compute \(a\), convert units | `06`, unit-cell recipe |
| Colligative properties | freezing point, boiling point, NaBr | \(\Delta T=iKm\) | Moles solute per kg solvent; apply \(i\) | `06`, colligative recipe |
| Kinetics order from data | concentration-time, first order, second order | integrated rate-law table | Find linear transformed data and slope | `07`, kinetics recipe |
| Arrhenius and catalyst | activation energy, temperature, catalyst | Arrhenius equation | Use two-temperature relation; catalyst changes rate not \(K\) | `07`, Arrhenius/catalyst |
| Equilibrium expression and shift | \(K_p\), \(Q\), Le Chatelier | products/reactants powers, omit solids/liquids | Write expression, compare \(Q\)/\(K\), apply shift rules | `07`, equilibrium recipe |
| Organic functional groups | aromatic, ester, ether, amide, carboxylic acid | functional-group table | Mark heteroatoms and carbonyls; classify attachments | `08`, functional-group recipe |
| Chirality and biomolecules | chiral center, amino acid, peptide | tetrahedral C with four groups, amide bond | Check four different substituents; identify peptide \(\mathrm{C(=O)-NH}\) | `08`, chirality |
| Polymer degree | degree of polymerization | \(n=M_{\mathrm{polymer}}/M_{\mathrm{repeat}}\) | Divide molar masses | `08`, polymer recipe |
| Weak acid/base pH | weak acid, weak base, \(K_a\), \(K_b\), pH | \(x\approx\sqrt{Kc_0}\) | Compute \(x\), convert pH/pOH, check approximation | `09`, pH recipe |
| Buffer pH | buffer, Henderson, phosphate, puffer | Henderson-Hasselbalch | Neutralize strong acid/base first, then ratio | `09`, buffer recipe |
| Solubility product | \(K_{sp}\), molar solubility, common ion, hydroxide pH | \(K_{sp}\), \(Q_{sp}\), \(s\) patterns | Write dissolution, express concentrations in \(s\), solve | `09`, \(K_{sp}\) recipe |
| Oxidation state | oxidation number of Cr/S/Mn/N | oxidation-state rules | Assign fixed states, solve charge sum | `10`, oxidation recipe |
| Galvanic cell potential | anode, cathode, standard potential | \(E^\circ=E^\circ_{\mathrm{cath}}-E^\circ_{\mathrm{an}}\) | More positive reduction is cathode; do not scale voltage | `10`, galvanic recipe |
| Nernst concentration cell | copper/nickel concentration cell | \(E=(0.0592/n)\log(c_{\mathrm{high}}/c_{\mathrm{low}})\) | Set \(E^\circ=0\), high over low | `10`, Nernst recipe |
| Multiple-choice elimination | correct statement, false statement | units, signs, assumptions | Test each clause independently; one false clause eliminates | `99`, exam strategy |
