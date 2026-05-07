# Coverage Report

## Detected source files

Slides were found in `input/lectures/`: Lecture 1 through Lecture 10.

Exam material was found in `input/exams/`: 2024F solution/answers, 202405, 202412, 202505, 202508, 202512 marked/unmarked sets, 26030 2021/2022 answer keys, 26030 2022 Winter Exam, and `ksp_solution_2025 - Copy.pdf`.

No exercise directory was present in the repository.

No `source_material/` directory was present; the repository source material is under `input/`.

## Inferred course title

`26020/26021 Chemistry (Polytechnical Foundation)`.

## Inferred topic structure and output files

| Order | Inferred topic | Source file |
|---|---|---|
| 1 | Atoms, stoichiometry, empirical formulae, mole concept, nomenclature | `sources/01_atoms_stoichiometry_nomenclature.tex` |
| 2 | Aqueous reactions, electrolytes, precipitation, redox introduction, gases | `sources/02_aqueous_reactions_gases.tex` |
| 3 | Thermodynamics, enthalpy, entropy, Gibbs free energy | `sources/03_thermodynamics.tex` |
| 4 | Electronic structure, quantum numbers, periodic trends | `sources/04_electronic_structure_periodic_table.tex` |
| 5 | Chemical bonds, Lewis structures, resonance, VSEPR | `sources/05_bonding_lewis_vsepr.tex` |
| 6 | Intermolecular forces, crystals, phase transitions, colligative properties | `sources/06_intermolecular_forces_solids_liquids.tex` |
| 7 | Chemical kinetics, Arrhenius equation, reaction equilibrium | `sources/07_kinetics_equilibrium.tex` |
| 8 | Organic chemistry, hydrocarbons, functional groups, chirality, peptides | `sources/08_organic_chemistry.tex` |
| 9 | Acids, bases, buffers, titration, solubility products | `sources/09_acids_bases_solubility.tex` |
| 10 | Electrochemistry, galvanic cells, Nernst equation | `sources/10_electrochemistry.tex` |
| 99 | Exam-required compact additions | `sources/99_exam_required_extra_topics.tex` |

## Key notation

- Amount, mass, molar mass: \(n\), \(m\), \(M\)
- Concentration and species concentration: \(c\), \([\ce{A}]\)
- Equilibrium: \(Q\), \(K\), \(K_p\), \(K_{sp}\)
- Acid/base: \(K_a\), \(K_b\), \(K_w\), \(pK_a\), \(pK_b\), pH, pOH
- Thermodynamics: \(\Delta U\), \(q\), \(w\), \(H\), \(\Delta H\), \(\Delta S\), \(\Delta G\)
- Kinetics: \(r\), \(k\), \(E_a\), \(A\), \(t_{1/2}\)
- Electrochemistry: \(E_{\mathrm{cell}}\), \(E^\circ_{\mathrm{cell}}\), \(F\), \(n\), \(Q\)

## Recurring exam concepts

- Isotope notation and neutron count
- Formula writing and molar mass
- Stoichiometry, limiting reactants, gas volumes
- Oxidation states and redox balancing
- Enthalpy from formation enthalpies and Hess's law
- \(\Delta G=\Delta H-T\Delta S\), \(\Delta G^\circ=-RT\ln K\)
- VSEPR geometry, bond angles, polarity, formal charge
- Crystal unit cells, density, BCC/FCC atom counts
- Colligative properties and vapor pressure
- Reaction order, integrated rate laws, Arrhenius relation
- Equilibrium expressions and Le Chatelier shifts
- Organic functional groups, chirality, degree of polymerization
- Weak acid/base pH, buffers, phosphate systems
- Solubility products and common-ion calculations
- Galvanic cells, concentration cells, Nernst equation

## Build verification

`main.tex` was compiled with a downloaded local Tectonic 0.16.9 executable because no system `pdflatex`, `xelatex`, `lualatex`, `latexmk`, or `tectonic` executable was available on PATH. The build completed and wrote `main.pdf`. Tectonic printed a non-fatal Windows fontconfig warning after PDF creation.
