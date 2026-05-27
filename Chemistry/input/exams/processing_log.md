# Processing Log

Entries are recorded in the chronological order defined in `processing_plan.md`.

## 26030 Winter 2021

- File name(s): `26030 2021 Winter Answer Key.pdf`
- Tasks found: Q1-Q25 are listed only as answer letters.
- Tasks ignored and why: Q1-Q25; the corresponding question paper is not present, so no computational pattern can be inferred responsibly.
- Python-solvable tasks: None identifiable.
- Existing functions reused: None.
- Existing functions generalized: None.
- New functions added: None.
- Compositions used: None.
- Tests added: None; no recoverable calculation is available.
- Unresolved issues: Question text and figures for Q1-Q25 are unavailable in the supplied source.
- Exam set complete: `yes`

## 26030 Winter 2022

- File name(s): `26030 2022 Winter Exam.pdf`; `26030 2022 Winter Answer Key.pdf`
- Tasks found: Q1-Q25, including stoichiometry, thermodynamics/equilibrium, gases, colligative properties, kinetics, pH, electrochemistry and conceptual/structure-recognition questions.
- Tasks ignored and why: Q2, Q4-Q6, Q8-Q9, Q13, Q16-Q18 and Q20-Q22 are primarily qualitative, symbolic balancing, periodic/structural or recognition questions that do not justify an exam-facing numerical function.
- Python-solvable tasks: Q1 (`full`), Q3 (`full`), Q7 (`full`), Q10-Q12 (`full`), Q14-Q15 (`full`), Q19 (`partial`), Q23-Q25 (`full`).
- Existing functions reused: `molar_mass`, `reaction_extent`, and `reaction_sum` after their first use within this set cover Q23 and Q25 without added wrappers.
- Existing functions generalized: None.
- New functions added: `molar_mass`, `mass_percent`, `reaction_extent`, `ideal_gas`, `reaction_sum`, `gibbs_energy`, `equilibrium_constant`, `colligative_temperature_change`, `clausius_clapeyron_pressure`, `power_law_exponent`, `weak_solution_ph`, `cell_potential`, `equilibrium_constant_from_cell`, `equilibrium_extent`, `arrhenius_ratio`; these establish independent reusable calculation operations rather than exam-specific solutions.
- Compositions used: `molar_mass` + `reaction_extent` (Q1/Q23); `reaction_sum` + `gibbs_energy` + `equilibrium_constant` (Q3); `ideal_gas` + `molar_mass` (Q10); `equilibrium_constant` + `equilibrium_extent` (Q19); `reaction_sum` + `molar_mass` (Q25).
- Tests added: `Winter2022CalculationTests` covers every introduced public function with exam-derived or directly relevant values.
- Unresolved issues: The extracted Q19 text does not state an initial amount of D even though the keyed option implies additional initial information; solver behavior is tested but reproduction of the keyed option is not claimed.
- Exam set complete: `yes`

## 26020/26021 May 2024 (`202405`)

- File name(s): `26020_26021_202405_exam_random_unmarked.pdf`; `26020_26021_202405_exam_random_marked.pdf`
- Tasks found: Q1-Q20, recovered by OCR of the unmarked PDF and checked against marked selections where text was exposed.
- Tasks ignored and why: Q1-Q4, Q9-Q10, Q12-Q13, Q15, Q18-Q20 are nomenclature, redox balancing, conceptual equilibrium/gas, electronic structure, polarity or periodic-trend selections rather than calculator operations.
- Python-solvable tasks: Q5-Q6 (`full`), Q7 (`partial`), Q8 (`full`), Q11 (`partial`), Q14 (`full`), Q16-Q17 (`full`).
- Existing functions reused: `molar_mass` (Q5-Q7), `reaction_extent` (Q7/Q11), `cell_potential` (Q8), `gibbs_energy` (Q16-Q17).
- Existing functions generalized: None.
- New functions added: `solubility_from_ksp`, because solubility from arbitrary ionic dissolution coefficients is a recurring independent calculation not represented by prior functions.
- Compositions used: `molar_mass` + `reaction_extent` (Q7); `reaction_extent` plus concentration arithmetic after choosing acid/base stoichiometry (Q11).
- Tests added: `May2024CalculationTests` verifies Q5-Q8, Q14 and Q16 numeric patterns; Q11/Q17 are direct use of already-tested operations after the chemical interpretation step.
- Unresolved issues: None.
- Exam set complete: `yes`

## 26020/26021 Winter/Fall 2024 (`202412`)

- File name(s): `26020_26021_202412_exam_random_unmarked.pdf`; `26020_26021_202412_exam_random_marked.pdf`; `26020_2024_fall_exam_random_answers (1).pdf`; `26020 exam 2024F solutions.pdf`
- Tasks found: Q1-Q20 with a typed solution companion and marked exam text.
- Tasks ignored and why: Q1-Q2, Q6-Q10, Q14 and Q20 require trend/notation/structure/bonding/redox reasoning rather than reusable numerical operations.
- Python-solvable tasks: Q3-Q5 (`partial`), Q11-Q13 (`full`), Q15-Q16 (`full`), Q17 (`partial`), Q18-Q19 (`full`).
- Existing functions reused: `molar_mass`, `reaction_extent`, `ideal_gas`, `colligative_temperature_change`, `solubility_from_ksp`, `cell_potential`.
- Existing functions generalized: None.
- New functions added: `unit_cell_volume` for density/cell-content calculations; `kinetic_linear_fit` for integrated-rate-law checks; `buffer_ph` for conjugate buffers; `reaction_quotient` for K/Q and Nernst compositions.
- Compositions used: stoichiometry plus `ideal_gas` (Q4); `molar_mass` plus scalar repeat-unit division (Q16); neutralization plus `buffer_ph` (Q17); `solubility_from_ksp` plus hydroxide-to-pH conversion (Q18); `reaction_quotient` plus `cell_potential` (Q19).
- Tests added: `WinterFall2024CalculationTests` covers Q3-Q4, Q11-Q13 and Q15/Q17-Q19 calculations with supplied solution values.
- Unresolved issues: Q5 is retained as a supported manual rearrangement of the Gibbs relation rather than adding an overloaded solve-any-variable function.
- Exam set complete: `yes`

## 26020/26021 May 2025 (`202505`)

- File name(s): `26020_26021_202505_exam_random_unmarked.pdf`; `26020_26021_202505_exam_random_marked.pdf`; `ksp_solution_2025 - Copy.pdf`
- Tasks found: Q1-Q30, recovered from OCR of the unmarked exam and checked against the annotated solution companion.
- Tasks ignored and why: Q1-Q10, Q13-Q15, Q19-Q20, Q23 and Q25-Q26/Q28 are VSEPR, nomenclature/structure, qualitative physical chemistry, trends or redox-balancing decisions without a worthwhile numerical API operation.
- Python-solvable tasks: Q11 (`full`), Q12 (`partial`), Q16 (`full`), Q17 (`partial`), Q18 (`full`), Q21 (`partial`), Q22 (`full`), Q24 (`full`), Q27 (`partial`), Q29-Q30 (`partial`).
- Existing functions reused: `gibbs_energy`, `reaction_quotient`, `weak_solution_ph`, `buffer_ph`, `power_law_exponent`, `reaction_sum`, `solubility_from_ksp`, `colligative_temperature_change`, `molar_mass`, `reaction_extent`.
- Existing functions generalized: None.
- New functions added: None; every calculation pattern is a direct reuse or a short transparent composition.
- Compositions used: neutralization plus `buffer_ph` (Q17); bond selection plus `reaction_sum` (Q21); inverse colligative calculation (Q27); balanced stoichiometry with `molar_mass`/`reaction_extent` (Q29); Hess equation combination with `reaction_sum` (Q30).
- Tests added: `May2025ReuseTests` verifies Q16-Q18, Q22, Q24, Q27 and Q29 using exam values.
- Unresolved issues: Q12 is supported as ion-product/threshold arithmetic without adding a precipitation-specific wrapper; Q21/Q30 retain the required human setup of bond or Hess coefficients.
- Exam set complete: `yes`

## 26020/26021 August 2025 (`202508`)

- File name(s): `26020_26021_202508_exam_random_unmarked.pdf`; `26020_26021_202508_exam_random_marked.pdf`
- Tasks found: Q1-Q20, recovered by OCR of the unmarked exam; Q3 spans two PDF pages.
- Tasks ignored and why: Q3-Q6, Q10 and Q12 are structure, periodic/bonding, or redox-balancing tasks without useful general numeric automation.
- Python-solvable tasks: Q1-Q2 (`full`), Q7 (`partial`), Q8-Q9 (`full`), Q11 (`partial`), Q13-Q20 (`full`).
- Existing functions reused: `mass_percent`, `molar_mass`, `ideal_gas`, `reaction_sum`, `reaction_extent`, `weak_solution_ph`, `colligative_temperature_change`, `unit_cell_volume`, `arrhenius_ratio`, `solubility_from_ksp`, `buffer_ph`.
- Existing functions generalized: None.
- New functions added: `photon_energy_kj_mol`, since wavelength-to-molar-energy conversion is a standalone quantitative spectrum operation not expressible as a clearer composition of existing tools.
- Compositions used: formula/gas conversion (Q2); precipitate stoichiometry plus `molar_mass` (Q7); reaction mass scaling (Q8); `ideal_gas` plus `reaction_sum` (Q9); interpreted electrochemical energy/potential comparison (Q11); yield via `reaction_extent` (Q13); geometry plus `unit_cell_volume` (Q16); Ksp followed by pOH arithmetic (Q18).
- Tests added: `August2025CalculationTests` checks Q1-Q2, Q7, Q9, Q13-Q20 numerical operations; the activation-energy candidate assertion was corrected from 134 to 193 kJ/mol after computation.
- Unresolved issues: Q11 remains partial because selecting the anode candidate includes reaction-direction interpretation.
- Exam set complete: `yes`

## 26020/26021 December 2025 (`202512`)

- File name(s): `26020_26021_202512_exam_random_unmarked.pdf`; `26020_26021_202512_exam_random_marked.pdf`
- Tasks found: Q1-Q30, recovered by OCR of the unmarked exam; the Q16 kinetics data table was additionally verified from a rendered page image.
- Tasks ignored and why: Q1-Q5, Q7-Q12, Q14, Q17, Q21-Q22 and Q27-Q30 are isotope/electronic, geometry, conceptual intermolecular/equilibrium/catalyst, redox or organic-enumeration tasks rather than reusable numeric calculations.
- Python-solvable tasks: Q6 (`partial`), Q13 (`partial`), Q15-Q16 (`full`), Q18-Q20 (`full`), Q23 (`partial`), Q24-Q25 (`full`), Q26 (`partial`).
- Existing functions reused: `reaction_sum`, `colligative_temperature_change`, `power_law_exponent`, `solubility_from_ksp`, `molar_mass`, `weak_solution_ph`, `buffer_ph`, `gibbs_energy`, `reaction_extent`.
- Existing functions generalized: None.
- New functions added: None; common-ion solubility is already supported by `solubility_from_ksp`.
- Compositions used: bond/Hess setup plus `reaction_sum` (Q6/Q13); solubility plus mass conversion (Q19); neutralization plus `buffer_ph` (Q23); balancing plus gas-volume stoichiometry (Q26).
- Tests added: `December2025ReuseTests` checks Q15-Q16, Q18-Q20 and Q23-Q26, including the common-ion option of `solubility_from_ksp`.
- Unresolved issues: None.
- Exam set complete: `yes`

## Final consolidation pass (aggressive rerun)

- File name(s): `exam_tools/chemistry.py`; `exam_tools/__init__.py`; `tests/test_exam_tools.py`; all preceding coverage and log records.
- Tasks found: Review of all `full` and `partial` calculation mappings and all 21 previously exported functions.
- Tasks ignored and why: No new exam task; this pass audits overlap, wrappers and documentation.
- Python-solvable tasks: All previously mapped `full`/`partial` rows retained their supporting operation or composition.
- Existing functions reused: `molar_mass`, `ideal_gas`, `equilibrium_constant`, `cell_potential`, `clausius_clapeyron_pressure`, `kinetic_linear_fit`, `weak_solution_ph`, `solubility_from_ksp`, `unit_cell_volume`, `arrhenius_ratio`.
- Existing functions generalized: None needed after all exam sets were processed.
- New functions added: None.
- Compositions used: Removed wrappers are replaced by explicit short arithmetic for mass percent, reaction extent, Delta G, reaction property sums, reaction quotients, colligative changes, photon energy, Henderson pH, initial-rate exponents and electrochemical Delta G; incomplete-source equilibrium extent remains a manual ICE/root setup.
- Tests added: Tests were updated to exercise the 10 retained exports while keeping exam calculations visible.
- Unresolved issues: The `26030 Winter 2021` source remains an answer key without question text; `26030 Winter 2022` Q19 has incomplete extracted initial-condition wording as already recorded.
- Exam set complete: `yes`; public API reduced from 21 to 10 functions.
