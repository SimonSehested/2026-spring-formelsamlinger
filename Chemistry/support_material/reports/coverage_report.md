# Coverage Report

## Detected source files

Lecture files were found in `input/lectures/`:

| Folder | Files |
|---|---|
| `input/lectures/` | `Lecture 1.pdf` through `Lecture 10.pdf` |

Exam files were found in `input/exams/`:

| Folder | Files |
|---|---|
| `input/exams/` | `26020 exam 2024F solutions.pdf`; `26020_2024_fall_exam_random_answers (1).pdf`; `26020_26021_202405_exam_random_marked.pdf`; `26020_26021_202405_exam_random_unmarked.pdf`; `26020_26021_202412_exam_random_marked.pdf`; `26020_26021_202412_exam_random_unmarked.pdf`; `26020_26021_202505_exam_random_marked.pdf`; `26020_26021_202505_exam_random_unmarked.pdf`; `26020_26021_202508_exam_random_marked.pdf`; `26020_26021_202508_exam_random_unmarked.pdf`; `26020_26021_202512_exam_random_marked.pdf`; `26020_26021_202512_exam_random_unmarked.pdf`; `26030 2021 Winter Answer Key.pdf`; `26030 2022 Winter Answer Key.pdf`; `26030 2022 Winter Exam.pdf`; `ksp_solution_2025 - Copy.pdf` |

No exercise folder was present. No `source_material/` folder was present; project input is under `input/`.

## Inferred course title

`26020/26021 Chemistry (Polytechnical Foundation)`.

## Inferred lecture/topic structure

The current lecture and exam material supports a ten-topic chemistry structure:

| Order | Inferred topic | Formula file |
|---|---|---|
| 0 | Shared symbols, notation, and units lookup | `sources/00_symbols_and_notation.tex` |
| 1 | Atoms, stoichiometry, empirical/molecular formula, nomenclature | `sources/01_atoms_stoichiometry_nomenclature.tex` |
| 2 | Aqueous reactions, redox balancing, gases | `sources/02_aqueous_reactions_gases.tex` |
| 3 | Thermochemistry, entropy, Gibbs free energy | `sources/03_thermodynamics.tex` |
| 4 | Electronic structure and periodic trends | `sources/04_electronic_structure_periodic_table.tex` |
| 5 | Bonding, Lewis structures, formal charge, VSEPR | `sources/05_bonding_lewis_vsepr.tex` |
| 6 | Intermolecular forces, solids, liquids, colligative properties | `sources/06_intermolecular_forces_solids_liquids.tex` |
| 7 | Kinetics and equilibrium | `sources/07_kinetics_equilibrium.tex` |
| 8 | Organic chemistry, functional groups, chirality, polymers | `sources/08_organic_chemistry.tex` |
| 9 | Acids, bases, buffers, titration, solubility products | `sources/09_acids_bases_solubility.tex` |
| 10 | Electrochemistry and oxidation states | `sources/10_electrochemistry.tex` |
| 99 | Cross-topic exam strategy and mixed recipes | `sources/99_exam_required_extra_topics.tex` |

## Rewrite objective applied

The previous source files were compact theory-reference files. They are being rewritten as executable problem-solving lookup files with:

- `Ctrl+F keywords` subsections in every file.
- Numbered and labelled formulas, reactions, decision rules, and reference tables.
- Explicit recipes for every recurring exam task type identified in the taxonomy.
- Step text that states both the required action and the procedure or numbered reference needed to perform it.
- Fast checks and common traps.
- English plus selected Danish search terms such as `bundfald`, `puffer`, `galvanisk`, `udbytte`, and `oploeselighed`.

## Explicit recipe and reference standard

- The working language remains English, with Danish search aliases retained where present in exam wording.
- The mandatory recipe surface is the 47 task families in `reports/exam_task_taxonomy.md`; supporting formulas outside those families remain numbered lookups.
- Every recipe must state `Use when`, `Given / Find`, `Required references`, procedural `Steps`, `Checks`, and `Common traps`.
- A procedural step is acceptable only when it explains how to perform the action or cites a numbered equation/table/rule that makes the decision executable.
- Formula and reaction labels use `eq:<topic>:<concept>`; lookup and rule tables use `tab:<topic>:<concept>`.

## Key notation

| Concept | Notation |
|---|---|
| Amount, mass, molar mass | \(n\), \(m\), \(M\) |
| Concentration | \(c\), \([\ce{A}]\) |
| Gas variables | \(p\), \(V\), \(T\), \(R\), \(x_i\) |
| Thermodynamics | \(\Delta U\), \(q\), \(w\), \(\Delta H\), \(\Delta S\), \(\Delta G\) |
| Equilibrium | \(Q\), \(K\), \(K_p\), \(K_c\) |
| Kinetics | \(r\), \(k\), \(E_a\), \(A\), \(t_{1/2}\) |
| Acid/base | \(K_a\), \(K_b\), \(K_w\), \(pK_a\), pH, pOH |
| Solubility | \(K_{sp}\), \(Q_{sp}\), \(s\) |
| Electrochemistry | \(E_{\mathrm{cell}}\), \(E^\circ_{\mathrm{cell}}\), \(F\), \(n\), \(Q\) |

## Symbol explanation layer

The formula collection now provides:

- A shared `Symbols, Notation, and Units` lookup before the topic chapters.
- A compact `Symbols and notation` table in each topic file, placed before the formulas it supports.
- Explicit context rules for overloaded notation, especially \(n\), \(M\), \(Q/q\), and \(p/P\).
- Definitions for formula-reading notation such as \(^{\circ}\), phase labels, activities, logarithms, reaction arrows, and recurring subscripts.

Scope is limited to calculation symbols and chemical notation needed to read the formulas. Element abbreviations and existing named-ion lookups are not expanded into a general glossary.

## Recurring exam concepts used to drive rewrite

- Isotope notation, mass number, proton/neutron/electron count.
- Ionic formula writing and common polyatomic ions.
- Molar mass, mass percent, empirical formula, molecular formula.
- Stoichiometry with limiting reactants, theoretical yield, and gas amounts.
- Net ionic precipitation equations and \(Q_{sp}\) versus \(K_{sp}\).
- Gravimetric concentration from a precipitate mass.
- Complete dissolution and total ion moles for strong soluble salts.
- Redox balancing in acidic/basic solution and oxidation-number assignment.
- Ideal gas law, combined gas law, partial pressure, gas density, and Graham effusion.
- Molar mass and molecular formula from measured gas data.
- Formation enthalpy, Hess's law, combustion enthalpy, bond-enthalpy estimates, \(\Delta G=\Delta H-T\Delta S\).
- Electron configurations, quantum-number validity, atomic/ionic radius and ionization-energy trends.
- Lewis structures, formal charges, resonance, VSEPR shape, bond angles, polarity.
- Ionic versus covalent bond character from electronegativity difference.
- Hydrogen bonding, vapor pressure, unit-cell density, BCC/FCC relations, freezing point depression.
- Unknown molar mass from freezing-point depression or boiling-point elevation.
- Integrated rate laws, half-life, Arrhenius equation, catalyst effects.
- Initial-rate determination of reaction orders and equilibrium composition from an ICE/extent setup.
- Equilibrium expressions, \(Q\) versus \(K\), \(K_p\), Le Chatelier.
- Organic functional-group recognition, aromatic rings, chirality, peptide/amide bonds, polymerization degree.
- Molecular-formula consistency and constitutional isomer enumeration.
- Weak acid/base pH, buffers, phosphate systems, titration stoichiometry/equivalence, \(K_{sp}\) and common-ion calculations.
- Qualitative acid/weak-acid classification and \(K_{sp}\) from an electrochemical potential.
- Galvanic cell potentials, anode/cathode recognition, Nernst equation, concentration cells.

## Known uncertainties

- `pdftotext` is available and extracts searchable task wording from the marked/solution exam PDFs; visually degraded chemical typography in extracted text must still be checked against the source PDF when validating exact species or charges.
- Course constants such as exact phosphate \(pK_a\) values are kept at the approximate values already present in the prior collection.
