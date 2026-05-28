# Function Inventory

## Aggressive Consolidation Decision

Final public API size: **12 functions**.

Removed public wrappers because their work is short, visible exam arithmetic:

| Removed function | Replacement |
|---|---|
| `mass_percent` | `100 * molar_mass("Li") / molar_mass("LiFePO4")` |
| `reaction_sum` | Direct signed sum of the few tabulated values in the problem. |
| `gibbs_energy` | `delta_h_kj_mol - temperature_k * delta_s_j_mol_k / 1000` |
| `reaction_quotient` | Direct product/ratio for the written equilibrium expression. |
| `colligative_temperature_change` | `freezing_point_depression` for freezing-point tasks; direct arithmetic for boiling-point elevation. |
| `photon_energy_kj_mol` | Direct `h * c * N_A / wavelength` calculation for its single task. |
| `buffer_ph` | Direct Henderson-Hasselbalch arithmetic after neutralization. |
| `equilibrium_constant_from_cell` | Convert `E` to Delta G explicitly, then call `equilibrium_constant`. |
| `equilibrium_extent` | Manual ICE/root setup; its only source question is incomplete in extraction. |
| `reaction_extent` | Direct `min(n_i / nu_i)` arithmetic after balancing. |
| `power_law_exponent` | Direct `log(rate_2/rate_1) / log(c_2/c_1)` arithmetic. |

## Final Public API

| Function name | Purpose | Input parameters | Output | Units | Example of use | Exam tasks covered | Why it survives |
|---|---|---|---|---|---|---|---|
| `molar_mass` | Parse a chemical formula and calculate formula mass | `formula` | molar mass | g/mol | `molar_mass("Ca(OH)2")` | Stoichiometry and composition tasks across 2022-2025 sets | Formula parsing and atomic-mass lookup are reusable and not useful to repeat in cells. |
| `freezing_point_depression` | Calculate molality, depression and solution freezing point | solute mol or solute mass/molar mass; solvent mass; `i`; optional `Kf` and pure freezing point | result dictionary | mol, mol/kg, degC | `freezing_point_depression(solute_mass_g=1, molar_mass_g_mol=58.44, solvent_mass_kg=.5, vant_hoff_factor=1.8)` | 202412 Q11; 202512 Q15 | Repeated colligative calculation with input conversion and comparison output. |
| `ideal_gas` | Solve one missing ideal-gas variable | one omitted of `pressure_pa`, `volume_m3`, `amount_mol`, `temperature_k` | omitted variable | Pa, m3, mol or K | `ideal_gas(pressure_pa=101325, volume_m3=.001, temperature_k=298.15)` | 26030-2022 Q10; 202412 Q4; 202508 Q2/Q9 | Standard reusable conversion with unit-oriented API. |
| `equilibrium_constant` | Convert standard Delta G to equilibrium constant | `delta_g_kj_mol`, `temperature_k` | K | dimensionless | `equilibrium_constant(-28.8, 318.15)` | 26030-2022 Q3/Q15/Q19 | Retains physical constant and exponent/sign handling. |
| `cell_potential` | Calculate Nernst cell potential | `standard_potential_v`, `electrons`, `reaction_quotient`, `temperature_k` | potential | V | `cell_potential(0, 2, 3e-5/0.5)` | 202405 Q8; 202412 Q19 | Repeated electrochemical formula with physical constants and sign handling. |
| `clausius_clapeyron_pressure` | Calculate vapor pressure at another temperature | initial pressure/temperature, final temperature, vaporization enthalpy | pressure | Pa | `clausius_clapeyron_pressure(101325, 184.65, 303.15, 14.7)` | 26030-2022 Q11 | Exponential pressure-temperature calculation with the gas constant. |
| `kinetic_linear_fit` | Check integrated rate-law linearity | `times_s`, `concentrations_m`, `order` | slope, intercept, R2 | transform-dependent | `kinetic_linear_fit(t, c, 1)` | 202412 Q13 | Nontrivial data-reduction operation. |
| `weak_solution_ph` | Solve monoprotic weak acid/base pH | concentration, `Ka`/`Kb`, `kind` | pH | dimensionless | `weak_solution_ph(.1, 10**-4.2, "acid")` | 26030-2022 Q14; 202505 Q16; 202508 Q14; 202512 Q20 | Repeated nonlinear equilibrium solve. |
| `solubility_from_ksp` | Solve molar solubility, including common ion | `ksp`, dissolution coefficients, optional backgrounds | solubility | mol/L | `solubility_from_ksp(5.61e-12, (1, 2))` | 202405 Q14; 202412 Q18; 202505 Q24; 202508 Q18; 202512 Q18-Q19 | Repeated nonlinear/general stoichiometric Ksp solve. |
| `solubility_complete_check` | Decide whether an added salt mass dissolves fully with a common ion | formula, `Ksp`, added mass, volume, common ion, coefficients | required/max concentrations, decision and excess dictionary | g, mol, mol/L | `solubility_complete_check("CuBr", 5.3e-9, added_mass_mg=100, common_ion_concentration_m=1e-6)` | 202512 Q18 | Prevents reversed required-versus-maximum decisions in mass-to-solubility comparisons. |
| `unit_cell_volume` | Calculate cell volume from density and occupancy | density, molar mass, units per cell | volume | m3 | `unit_cell_volume(7874, 55.85, 2)` | 202412 Q12; 202508 Q16 | Retains Avogadro conversion and crystal-cell units. |
| `arrhenius_ratio` | Calculate rate constant ratio at two temperatures | activation energy, initial/final temperature | ratio | dimensionless | `arrhenius_ratio(63, 873.15, 1073.15)` | 26030-2022 Q24; 202508 Q17 | Repeated exponential rate/temperature calculation with physical constant. |
