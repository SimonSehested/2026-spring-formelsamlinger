import math
import unittest

from exam_tools import (
    arrhenius_ratio,
    cell_potential,
    clausius_clapeyron_pressure,
    equilibrium_constant,
    freezing_point_depression,
    ideal_gas,
    kinetic_linear_fit,
    molar_mass,
    solubility_complete_check,
    solubility_from_ksp,
    unit_cell_volume,
    weak_solution_ph,
)


class Winter2022CalculationTests(unittest.TestCase):
    def test_molar_mass(self):
        self.assertAlmostEqual(molar_mass("C3H8"), 44.097, places=3)

    def test_limiting_reagent_for_propane_combustion_q1(self):
        amounts = {"C3H8": 24 / molar_mass("C3H8"), "O2": 24 / molar_mass("O2")}
        extent = min(amounts["C3H8"] / 1, amounts["O2"] / 5)
        self.assertAlmostEqual(3 * extent, 0.45, places=2)

    def test_reaction_thermodynamics_and_k_q3(self):
        dh = 2 * -46.11
        ds = 2 * 192.4 - 191.61 - 3 * 130.79
        dg = dh - 318.15 * ds / 1000
        self.assertAlmostEqual(dg, -28.85, places=2)
        self.assertAlmostEqual(equilibrium_constant(dg, 318.15) / 5.47e4, 1.0, delta=0.02)

    def test_freezing_point_depression_q7(self):
        self.assertAlmostEqual(3 * 1.86 * 0.75, 4.185, places=3)

    def test_ideal_gas_identifies_molar_mass_q10(self):
        amount = ideal_gas(pressure_pa=101325, volume_m3=33.6e-6, temperature_k=273.15)
        self.assertAlmostEqual(0.108 / amount, molar_mass("C5H12"), delta=0.5)

    def test_clausius_clapeyron_q11(self):
        p2_atm = clausius_clapeyron_pressure(101325, 184.65, 303.15, 14.7) / 101325
        self.assertAlmostEqual(p2_atm, 42.0, delta=1.0)

    def test_initial_rate_order_q12(self):
        exponent = math.log(0.00414 / 0.00138) / math.log(0.045 / 0.015)
        self.assertAlmostEqual(exponent, 1.0, places=8)

    def test_weak_base_ph_q14(self):
        self.assertAlmostEqual(weak_solution_ph(0.030, 1.8e-5, "base"), 10.86, places=2)

    def test_solubility_constant_from_electrochemistry_q15(self):
        delta_g_kj_mol = -1 * 96485.33212 * (0.215 - 0.800) / 1000
        ksp = equilibrium_constant(delta_g_kj_mol, 298.15)
        self.assertAlmostEqual(ksp / 1.3e-10, 1.0, delta=0.08)

    def test_arrhenius_ratio_q24(self):
        ratio = arrhenius_ratio(63.0, 873.15, 1073.15)
        self.assertAlmostEqual(ratio, 5.0, delta=0.2)

    def test_nernst_general_cell_evaluation(self):
        self.assertAlmostEqual(cell_potential(0.0, 2, 0.002), 0.0798, places=3)


class May2024CalculationTests(unittest.TestCase):
    def test_ammonium_hydrogenphosphate_mass_q5(self):
        mass_g = 0.001 * molar_mass("(NH4)2HPO4")
        self.assertAlmostEqual(mass_g, 0.132, places=3)

    def test_molar_mass_ranking_q6(self):
        self.assertGreater(molar_mass("SF6"), molar_mass("Fe"))
        self.assertGreater(molar_mass("SF6"), molar_mass("CO2"))

    def test_hydrogen_from_aluminium_q7(self):
        extent = (25 / molar_mass("Al")) / 2
        self.assertAlmostEqual(3 * extent * molar_mass("H2"), 2.8, delta=0.05)

    def test_copper_concentration_cell_q8(self):
        voltage = cell_potential(0.0, 2, 0.002 / 1.0)
        self.assertAlmostEqual(voltage, 0.080, places=3)

    def test_chromate_solubility_comparison_q14(self):
        silver = solubility_from_ksp(9.0e-12, (2, 1))
        barium = solubility_from_ksp(2.0e-10, (1, 1))
        lead = solubility_from_ksp(1.8e-14, (1, 1))
        self.assertGreater(silver, barium)
        self.assertGreater(barium, lead)

    def test_gibbs_energy_q16(self):
        self.assertAlmostEqual(115.0 - 298.15 * 125.0 / 1000, 77.7, delta=0.1)


class WinterFall2024CalculationTests(unittest.TestCase):
    def test_fermentation_q3(self):
        extent = (1000 / molar_mass("C6H12O6")) / 1
        ethanol_mol = 2 * extent
        self.assertAlmostEqual(ethanol_mol, 11.1, delta=0.1)
        self.assertAlmostEqual(ethanol_mol * molar_mass("C2H6O"), 511, delta=2)

    def test_hot_tank_pressure_q4(self):
        pressure = ideal_gas(volume_m3=0.010, amount_mol=5.0, temperature_k=1950 + 273.15)
        self.assertAlmostEqual(pressure / 1e6, 9.24, delta=0.02)

    def test_nabr_freezing_point_q11(self):
        depression = 2 * 1.86 * (12 / molar_mass("NaBr")) / 0.300
        self.assertAlmostEqual(depression, 1.45, delta=0.02)

    def test_bcc_iron_unit_cell_q12(self):
        volume = unit_cell_volume(7874, 55.85, 2)
        self.assertAlmostEqual(volume / 2.36e-29, 1.0, delta=0.01)

    def test_iodide_is_first_order_q13(self):
        times = [0, 60, 120, 300, 1000]
        concentrations = [1.0, 0.498, 0.250, 0.0312, 9.59e-6]
        _, _, r1 = kinetic_linear_fit(times, concentrations, 1)
        _, _, r2 = kinetic_linear_fit(times, concentrations, 2)
        self.assertGreater(r1, 0.999)
        self.assertGreater(r1, r2)

    def test_phosphate_buffer_q17(self):
        self.assertAlmostEqual(-math.log10(6.2e-8) + math.log10(0.05 / 0.15), 6.73, places=2)

    def test_magnesium_hydroxide_ph_q18(self):
        solubility = solubility_from_ksp(5.61e-12, (1, 2))
        ph = 14.0 + math.log10(2 * solubility)
        self.assertAlmostEqual(ph, 10.35, places=2)

    def test_nickel_concentration_cell_q19(self):
        quotient = 3e-5 / 0.5
        voltage = cell_potential(0.0, 2, quotient)
        self.assertAlmostEqual(voltage * 1000, 125, delta=1)

    def test_ammonia_equilibrium_constant_q15(self):
        kp = 95**2 / (52.5 * 157.5**3)
        self.assertAlmostEqual(kp, 4.40e-5, delta=0.02e-5)


class May2025ReuseTests(unittest.TestCase):
    def test_acetic_acid_ph_q16(self):
        self.assertAlmostEqual(weak_solution_ph(0.10, 10 ** -4.7, "acid"), 2.9, delta=0.05)

    def test_ammonia_buffer_after_naoh_q17(self):
        pka_ammonium = 14.0 - (-math.log10(1.80e-5))
        ph = pka_ammonium + math.log10((0.500 + 0.030) / (0.500 - 0.030))
        self.assertAlmostEqual(ph, 9.31, places=2)

    def test_rate_law_orders_q18(self):
        ammonium_order = math.log(0.010 / 0.005) / math.log(0.020 / 0.010)
        nitrite_order = math.log(0.020 / 0.005) / math.log(0.030 / 0.015)
        self.assertAlmostEqual(ammonium_order, 1.0, places=8)
        self.assertAlmostEqual(nitrite_order, 2.0, places=8)

    def test_boiling_point_from_gibbs_switch_q22(self):
        switch_temperature = 30.9 * 1000 / 93.0
        self.assertAlmostEqual(30.9 - switch_temperature * 93.0 / 1000, 0.0, places=8)
        self.assertAlmostEqual(switch_temperature - 273.15, 59.1, delta=0.2)

    def test_copper_hydroxide_solubility_q24(self):
        self.assertAlmostEqual(solubility_from_ksp(1.6e-19, (1, 2)), 3.4e-7, delta=0.1e-7)

    def test_unknown_molar_mass_from_boiling_elevation_q27(self):
        target_delta_t = 100.37 - 100.00
        trial_molar_mass = 150.0
        molality = (9.81 / trial_molar_mass) / 0.0900
        self.assertAlmostEqual(1 * 0.51 * molality, target_delta_t, delta=0.01)

    def test_calcium_carbide_yield_q29(self):
        extent = (10.2 / molar_mass("C")) / 3
        self.assertAlmostEqual(extent * molar_mass("CaC2"), 18.1, delta=0.2)


class August2025CalculationTests(unittest.TestCase):
    def test_lithium_mass_percent_q1(self):
        self.assertAlmostEqual(100 * molar_mass("Li") / molar_mass("LiFePO4"), 4.4, delta=0.05)

    def test_nitrogen_volume_for_calcium_nitride_q2(self):
        product_mol = 5.0 / molar_mass("Ca3N2")
        volume_m3 = ideal_gas(pressure_pa=101325, amount_mol=product_mol, temperature_k=298.15)
        self.assertAlmostEqual(volume_m3 * 1000, 0.83, delta=0.02)

    def test_nacl_concentration_from_agcl_precipitate_q7(self):
        chloride_mol = 13.5 / molar_mass("AgCl")
        self.assertAlmostEqual(chloride_mol / 0.250, 0.38, delta=0.01)

    def test_ethene_combustion_heat_q9(self):
        ethene_mol = ideal_gas(pressure_pa=101325, volume_m3=0.0100, temperature_k=298.15)
        dh = 2 * -393.5 + 2 * -285.8 - 52.4
        self.assertAlmostEqual(abs(ethene_mol * dh), 576, delta=3)

    def test_sodium_bromide_percent_yield_q13(self):
        extent = min((2.30 / molar_mass("Na")) / 2, (9.59 / molar_mass("Br2")) / 1)
        theoretical_mass = 2 * extent * molar_mass("NaBr")
        self.assertAlmostEqual(100 * 7.85 / theoretical_mass, 76, delta=1)

    def test_benzoic_acid_ph_q14(self):
        self.assertAlmostEqual(weak_solution_ph(0.150, 10 ** -4.20, "acid"), 2.5, delta=0.05)

    def test_dmso_freezing_point_q15(self):
        self.assertAlmostEqual(-1.0 * 3.85 * 0.60, -2.31, places=2)

    def test_tantalum_cell_count_q16(self):
        coating_volume_m3 = 10.0e-4 * 10.0e-6
        count = coating_volume_m3 / unit_cell_volume(16680, 180.95, 2)
        self.assertAlmostEqual(count / 2.8e20, 1.0, delta=0.05)

    def test_arrhenius_candidate_q17(self):
        self.assertAlmostEqual(arrhenius_ratio(193, 325 + 273.15, 500 + 273.15), 20 / 3.0e-3, delta=300)

    def test_helium_emission_energy_q19(self):
        energy = 6.62607015e-34 * 299792458.0 * 6.02214076e23 / (501e-9) / 1000
        self.assertAlmostEqual(energy, 239, delta=1)

    def test_equal_acetate_buffer_q20(self):
        self.assertAlmostEqual(-math.log10(1.77e-5) + math.log10(1.50 / 1.50), 4.75, delta=0.01)


class December2025ReuseTests(unittest.TestCase):
    def test_freezing_point_comparison_q15(self):
        nacl = freezing_point_depression(
            solute_mass_g=1.0,
            molar_mass_g_mol=58.44,
            solvent_mass_kg=0.500,
            vant_hoff_factor=1.8,
        )
        cacl2 = freezing_point_depression(
            solute_mass_g=1.0,
            molar_mass_g_mol=110.98,
            solvent_mass_kg=0.500,
            vant_hoff_factor=2.6,
        )
        self.assertAlmostEqual(nacl["freezing_point_c"], -0.1146, delta=0.0001)
        self.assertAlmostEqual(cacl2["freezing_point_c"], -0.0872, delta=0.0001)
        self.assertLess(nacl["freezing_point_c"], cacl2["freezing_point_c"])

    def test_rate_orders_q16(self):
        co_order = math.log(0.045 / 0.03) / math.log(0.75 / 0.5)
        chlorine_order = math.log(0.015 / 0.03) / math.log(1 / 2)
        self.assertAlmostEqual(co_order, 1.0, places=8)
        self.assertAlmostEqual(chlorine_order, 1.0, places=8)

    def test_common_ion_bromide_solubility_q18(self):
        silver = solubility_complete_check(
            "AgBr", ksp=3.3e-13, added_mass_mg=10, common_ion_concentration_m=1.0e-6
        )
        copper = solubility_complete_check(
            "CuBr", ksp=5.3e-9, added_mass_mg=100, common_ion_concentration_m=1.0e-6
        )
        self.assertFalse(silver["dissolves_completely"])
        self.assertTrue(copper["dissolves_completely"])
        self.assertGreater(silver["excess_mass_g"], 0.0)
        self.assertEqual(copper["excess_mass_g"], 0.0)

    def test_barium_sulfate_dissolved_mass_q19(self):
        mass_mg = solubility_from_ksp(1.08e-10, (1, 1)) * 0.100 * molar_mass("BaSO4") * 1000
        self.assertAlmostEqual(mass_mg, 0.24, delta=0.01)

    def test_ammonia_ph_q20(self):
        self.assertAlmostEqual(weak_solution_ph(0.10, 10 ** -4.75, "base"), 11.1, delta=0.05)

    def test_acetate_buffer_after_base_q23(self):
        pka = -math.log10(1.80e-5)
        self.assertAlmostEqual(pka + math.log10((0.500 + 0.015) / (0.500 - 0.015)), 4.77, delta=0.01)

    def test_k_equal_one_temperature_q24(self):
        temperature = 50_000 / 67
        self.assertAlmostEqual(50 - temperature * 67 / 1000, 0.0, places=8)
        self.assertAlmostEqual(temperature, 746, delta=1)

    def test_hydrogen_sulfide_boiling_point_q25(self):
        temperature = 18_700 / 87.8
        self.assertAlmostEqual(temperature - 273.15, -60.2, delta=0.5)

    def test_acetylene_volume_yield_q26(self):
        oxygen_l = 150 * 0.2
        self.assertAlmostEqual(oxygen_l * 2 / 3, 20.0, places=8)


class FreezingPointDepressionApiTests(unittest.TestCase):
    def test_direct_solute_amount(self):
        result = freezing_point_depression(
            solute_mol=0.100,
            solvent_mass_kg=0.500,
            vant_hoff_factor=2.0,
        )
        self.assertAlmostEqual(result["molality_mol_kg"], 0.200)
        self.assertAlmostEqual(result["delta_tf_c"], 0.744)
        self.assertAlmostEqual(result["freezing_point_c"], -0.744)

    def test_solute_mass_and_molar_mass(self):
        result = freezing_point_depression(
            solute_mass_g=58.44,
            molar_mass_g_mol=58.44,
            solvent_mass_kg=2.0,
            vant_hoff_factor=1.8,
        )
        self.assertAlmostEqual(result["solute_mol"], 1.0)
        self.assertAlmostEqual(result["molality_mol_kg"], 0.5)
        self.assertAlmostEqual(result["delta_tf_c"], 1.674)

    def test_requires_solute_data(self):
        with self.assertRaises(ValueError):
            freezing_point_depression(solvent_mass_kg=1.0)

    def test_requires_positive_solvent_mass(self):
        with self.assertRaises(ValueError):
            freezing_point_depression(solute_mol=1.0, solvent_mass_kg=0.0)

    def test_requires_positive_vant_hoff_factor(self):
        with self.assertRaises(ValueError):
            freezing_point_depression(solute_mol=1.0, solvent_mass_kg=1.0, vant_hoff_factor=0.0)

    def test_requires_positive_molar_mass_for_mass_input(self):
        with self.assertRaises(ValueError):
            freezing_point_depression(solute_mass_g=1.0, molar_mass_g_mol=0.0, solvent_mass_kg=1.0)


class SolubilityCompleteCheckApiTests(unittest.TestCase):
    def test_gram_input_and_stoichiometric_metal_concentration(self):
        result = solubility_complete_check(
            "Ag2CrO4",
            ksp=9.0e-12,
            added_mass_g=0.001,
            common_ion_concentration_m=1.0e-4,
            stoich_metal=2,
            stoich_common_ion=1,
        )
        self.assertAlmostEqual(
            result["required_metal_concentration_m"],
            2 * result["required_formula_concentration_m"],
        )
        self.assertAlmostEqual(result["max_metal_concentration_m"], (9.0e-12 / 1.0e-4) ** 0.5)
        self.assertAlmostEqual(result["max_formula_concentration_m"], result["max_metal_concentration_m"] / 2)

    def test_zero_common_ion_uses_pure_solvent_solubility(self):
        result = solubility_complete_check("AgBr", ksp=4.0e-12, added_mass_g=0.0)
        self.assertAlmostEqual(result["max_formula_concentration_m"], 2.0e-6)
        self.assertTrue(result["dissolves_completely"])

    def test_requires_one_mass_input(self):
        with self.assertRaises(ValueError):
            solubility_complete_check("AgBr", ksp=3.3e-13)
        with self.assertRaises(ValueError):
            solubility_complete_check("AgBr", ksp=3.3e-13, added_mass_g=1.0, added_mass_mg=1.0)

    def test_rejects_invalid_physical_inputs(self):
        invalid_cases = (
            {"ksp": 0.0, "added_mass_mg": 1.0},
            {"ksp": 1.0, "added_mass_g": -1.0},
            {"ksp": 1.0, "added_mass_mg": 1.0, "solution_volume_l": 0.0},
            {"ksp": 1.0, "added_mass_mg": 1.0, "common_ion_concentration_m": -1.0},
            {"ksp": 1.0, "added_mass_mg": 1.0, "stoich_metal": 0},
            {"ksp": 1.0, "added_mass_mg": 1.0, "stoich_common_ion": 1.5},
        )
        for kwargs in invalid_cases:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                solubility_complete_check("AgBr", **kwargs)


if __name__ == "__main__":
    unittest.main()
