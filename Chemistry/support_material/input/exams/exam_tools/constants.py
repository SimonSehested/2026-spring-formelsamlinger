"""Offline numeric physical constants for exam calculations.

The values are generated from SciPy/CODATA physical_constants and vendored
so notebooks can use constants without importing sympy.physics.units or
requiring internet access. All exported constants are floats in SI units.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Constant:
    """Metadata for a physical constant."""

    value: float
    unit: str
    uncertainty: float
    source_name: str


def _normalize_name(name: str) -> str:
    text = str(name).lower().replace("\\", " ")
    text = re.sub(r"[^0-9a-z]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if text.startswith("constant_"):
        return text
    if text[:1].isdigit():
        return "constant_" + text
    return text


PHYSICAL_CONSTANTS = {
    'angstrom_star': Constant(1.00001495e-10, 'm', 9e-17, 'Angstrom star'),
    'avogadro_constant': Constant(6.02214076e+23, 'mol^-1', 0.0, 'Avogadro constant'),
    'bohr_magneton': Constant(9.2740100657e-24, 'J T^-1', 2.9e-33, 'Bohr magneton'),
    'bohr_magneton_in_hz_t': Constant(13996244917.1, 'Hz T^-1', 4.4, 'Bohr magneton in Hz/T'),
    'bohr_magneton_in_k_t': Constant(0.67171381472, 'K T^-1', 2.1e-10, 'Bohr magneton in K/T'),
    'bohr_magneton_in_ev_t': Constant(5.7883817982e-05, 'eV T^-1', 1.8e-14, 'Bohr magneton in eV/T'),
    'bohr_magneton_in_inverse_meter_per_tesla': Constant(46.686447719, 'm^-1 T^-1', 1.5e-08, 'Bohr magneton in inverse meter per tesla'),
    'bohr_magneton_in_inverse_meters_per_tesla': Constant(46.68644814, 'm^-1 T^-1', 2.9e-07, 'Bohr magneton in inverse meters per tesla'),
    'bohr_radius': Constant(5.29177210544e-11, 'm', 8.2e-21, 'Bohr radius'),
    'boltzmann_constant': Constant(1.380649e-23, 'J K^-1', 0.0, 'Boltzmann constant'),
    'boltzmann_constant_in_hz_k': Constant(20836619123.327576, 'Hz K^-1', 0.0, 'Boltzmann constant in Hz/K'),
    'boltzmann_constant_in_ev_k': Constant(8.617333262145179e-05, 'eV K^-1', 0.0, 'Boltzmann constant in eV/K'),
    'boltzmann_constant_in_inverse_meter_per_kelvin': Constant(69.50348004861274, 'm^-1 K^-1', 0.0, 'Boltzmann constant in inverse meter per kelvin'),
    'boltzmann_constant_in_inverse_meters_per_kelvin': Constant(69.503457, 'm^-1 K^-1', 4e-05, 'Boltzmann constant in inverse meters per kelvin'),
    'compton_wavelength': Constant(2.42631023538e-12, 'm', 7.6e-22, 'Compton wavelength'),
    'compton_wavelength_over_2_pi': Constant(3.8615926764e-13, 'm', 1.8e-22, 'Compton wavelength over 2 pi'),
    'copper_x_unit': Constant(1.00207697e-13, 'm', 2.8e-20, 'Copper x unit'),
    'cu_x_unit': Constant(1.00207697e-13, 'm', 2.8e-20, 'Cu x unit'),
    'faraday_constant': Constant(96485.33212331001, 'C mol^-1', 0.0, 'Faraday constant'),
    'faraday_constant_for_conventional_electric_current': Constant(96485.3251, 'C_90 mol^-1', 0.0012, 'Faraday constant for conventional electric current'),
    'fermi_coupling_constant': Constant(1.1663787e-05, 'GeV^-2', 6e-12, 'Fermi coupling constant'),
    'hartree_energy': Constant(4.359744722206e-18, 'J', 4.8e-30, 'Hartree energy'),
    'hartree_energy_in_ev': Constant(27.211386245981, 'eV', 3e-11, 'Hartree energy in eV'),
    'josephson_constant': Constant(483597848416983.6, 'Hz V^-1', 0.0, 'Josephson constant'),
    'loschmidt_constant_273_15_k_100_kpa': Constant(2.6516458048837345e+25, 'm^-3', 0.0, 'Loschmidt constant (273.15 K, 100 kPa)'),
    'loschmidt_constant_273_15_k_101_325_kpa': Constant(2.686780111798444e+25, 'm^-3', 0.0, 'Loschmidt constant (273.15 K, 101.325 kPa)'),
    'mo_x_unit': Constant(1.00209952e-13, 'm', 5.3e-20, 'Mo x unit'),
    'molybdenum_x_unit': Constant(1.00209952e-13, 'm', 5.3e-20, 'Molybdenum x unit'),
    'newtonian_constant_of_gravitation': Constant(6.6743e-11, 'm^3 kg^-1 s^-2', 1.5e-15, 'Newtonian constant of gravitation'),
    'newtonian_constant_of_gravitation_over_h_bar_c': Constant(6.70883e-39, '(GeV/c^2)^-2', 1.5e-43, 'Newtonian constant of gravitation over h-bar c'),
    'planck_constant': Constant(6.62607015e-34, 'J Hz^-1', 0.0, 'Planck constant'),
    'planck_constant_in_ev_s': Constant(4.135667662e-15, 'eV s', 2.5e-23, 'Planck constant in eV s'),
    'planck_constant_in_ev_hz': Constant(4.135667696923859e-15, 'eV Hz^-1', 0.0, 'Planck constant in eV/Hz'),
    'planck_constant_over_2_pi': Constant(1.0545718e-34, 'J s', 1.3e-42, 'Planck constant over 2 pi'),
    'planck_constant_over_2_pi_in_ev_s': Constant(6.582119514e-16, 'eV s', 4e-24, 'Planck constant over 2 pi in eV s'),
    'planck_constant_over_2_pi_times_c_in_mev_fm': Constant(197.3269788, 'MeV fm', 1.2e-06, 'Planck constant over 2 pi times c in MeV fm'),
    'planck_length': Constant(1.616255e-35, 'm', 1.8e-40, 'Planck length'),
    'planck_mass': Constant(2.176434e-08, 'kg', 2.4e-13, 'Planck mass'),
    'planck_mass_energy_equivalent_in_gev': Constant(1.22089e+19, 'GeV', 140000000000000.0, 'Planck mass energy equivalent in GeV'),
    'planck_temperature': Constant(1.416784e+32, 'K', 1.6e+27, 'Planck temperature'),
    'planck_time': Constant(5.391247e-44, 's', 6e-49, 'Planck time'),
    'rydberg_constant': Constant(10973731.568157, 'm^-1', 1.2e-05, 'Rydberg constant'),
    'rydberg_constant_times_c_in_hz': Constant(3289841960250000.0, 'Hz', 3600.0, 'Rydberg constant times c in Hz'),
    'rydberg_constant_times_hc_in_j': Constant(2.179872361103e-18, 'J', 2.4e-30, 'Rydberg constant times hc in J'),
    'rydberg_constant_times_hc_in_ev': Constant(13.60569312299, 'eV', 1.5e-11, 'Rydberg constant times hc in eV'),
    'sackur_tetrode_constant_1_k_100_kpa': Constant(-1.15170753496, '', 4.7e-10, 'Sackur-Tetrode constant (1 K, 100 kPa)'),
    'sackur_tetrode_constant_1_k_101_325_kpa': Constant(-1.16487052149, '', 4.7e-10, 'Sackur-Tetrode constant (1 K, 101.325 kPa)'),
    'stefan_boltzmann_constant': Constant(5.6703744191844314e-08, 'W m^-2 K^-4', 0.0, 'Stefan-Boltzmann constant'),
    'thomson_cross_section': Constant(6.6524587051e-29, 'm^2', 6.2e-38, 'Thomson cross section'),
    'w_to_z_mass_ratio': Constant(0.88145, '', 0.00013, 'W to Z mass ratio'),
    'wien_displacement_law_constant': Constant(0.0028977685, 'm K', 5.1e-09, 'Wien displacement law constant'),
    'wien_frequency_displacement_law_constant': Constant(58789257576.468254, 'Hz K^-1', 0.0, 'Wien frequency displacement law constant'),
    'wien_wavelength_displacement_law_constant': Constant(0.0028977719551851727, 'm K', 0.0, 'Wien wavelength displacement law constant'),
    'alpha_particle_mass': Constant(6.644657345e-27, 'kg', 2.1e-36, 'alpha particle mass'),
    'alpha_particle_mass_energy_equivalent': Constant(5.9719201997e-10, 'J', 1.9e-19, 'alpha particle mass energy equivalent'),
    'alpha_particle_mass_energy_equivalent_in_mev': Constant(3727.3794118, 'MeV', 1.2e-06, 'alpha particle mass energy equivalent in MeV'),
    'alpha_particle_mass_in_u': Constant(4.001506179129, 'u', 6.2e-11, 'alpha particle mass in u'),
    'alpha_particle_molar_mass': Constant(0.0040015061833, 'kg mol^-1', 1.2e-12, 'alpha particle molar mass'),
    'alpha_particle_relative_atomic_mass': Constant(4.001506179129, '', 6.2e-11, 'alpha particle relative atomic mass'),
    'alpha_particle_rms_charge_radius': Constant(1.6785e-15, 'm', 2.1e-18, 'alpha particle rms charge radius'),
    'alpha_particle_electron_mass_ratio': Constant(7294.29954171, '', 1.7e-07, 'alpha particle-electron mass ratio'),
    'alpha_particle_proton_mass_ratio': Constant(3.972599690252, '', 7e-11, 'alpha particle-proton mass ratio'),
    'atomic_mass_constant': Constant(1.66053906892e-27, 'kg', 5.2e-37, 'atomic mass constant'),
    'atomic_mass_constant_energy_equivalent': Constant(1.49241808768e-10, 'J', 4.6e-20, 'atomic mass constant energy equivalent'),
    'atomic_mass_constant_energy_equivalent_in_mev': Constant(931.49410372, 'MeV', 2.9e-07, 'atomic mass constant energy equivalent in MeV'),
    'atomic_mass_unit_electron_volt_relationship': Constant(931494103.72, 'eV', 0.29, 'atomic mass unit-electron volt relationship'),
    'atomic_mass_unit_hartree_relationship': Constant(34231776.922, 'E_h', 0.011, 'atomic mass unit-hartree relationship'),
    'atomic_mass_unit_hertz_relationship': Constant(2.25234272185e+23, 'Hz', 70000000000000.0, 'atomic mass unit-hertz relationship'),
    'atomic_mass_unit_inverse_meter_relationship': Constant(751300662090000.0, 'm^-1', 230000.0, 'atomic mass unit-inverse meter relationship'),
    'atomic_mass_unit_joule_relationship': Constant(1.49241808768e-10, 'J', 4.6e-20, 'atomic mass unit-joule relationship'),
    'atomic_mass_unit_kelvin_relationship': Constant(10809540206700.0, 'K', 3400.0, 'atomic mass unit-kelvin relationship'),
    'atomic_mass_unit_kilogram_relationship': Constant(1.66053906892e-27, 'kg', 5.2e-37, 'atomic mass unit-kilogram relationship'),
    'atomic_unit_of_1st_hyperpolarizability': Constant(3.2063612996e-53, 'C^3 m^3 J^-2', 1.5e-62, 'atomic unit of 1st hyperpolarizability'),
    'atomic_unit_of_1st_hyperpolarizablity': Constant(3.20636151e-53, 'C^3 m^3 J^-2', 2.8e-60, 'atomic unit of 1st hyperpolarizablity'),
    'atomic_unit_of_2nd_hyperpolarizability': Constant(6.2353799735e-65, 'C^4 m^4 J^-3', 3.9e-74, 'atomic unit of 2nd hyperpolarizability'),
    'atomic_unit_of_2nd_hyperpolarizablity': Constant(6.2353808e-65, 'C^4 m^4 J^-3', 1.1e-71, 'atomic unit of 2nd hyperpolarizablity'),
    'atomic_unit_of_action': Constant(1.0545718176461565e-34, 'J s', 0.0, 'atomic unit of action'),
    'atomic_unit_of_charge': Constant(1.602176634e-19, 'C', 0.0, 'atomic unit of charge'),
    'atomic_unit_of_charge_density': Constant(1081202386770.0, 'C m^-3', 510.0, 'atomic unit of charge density'),
    'atomic_unit_of_current': Constant(0.0066236182375082, 'A', 7.2e-15, 'atomic unit of current'),
    'atomic_unit_of_electric_dipole_mom': Constant(8.4783536198e-30, 'C m', 1.3e-39, 'atomic unit of electric dipole mom.'),
    'atomic_unit_of_electric_dipole_moment': Constant(8.47835309e-30, 'C m', 7.3e-37, 'atomic unit of electric dipole moment'),
    'atomic_unit_of_electric_field': Constant(514220675112.0, 'V m^-1', 80.0, 'atomic unit of electric field'),
    'atomic_unit_of_electric_field_gradient': Constant(9.7173624424e+21, 'V m^-2', 3000000000000.0, 'atomic unit of electric field gradient'),
    'atomic_unit_of_electric_polarizability': Constant(1.64877727212e-41, 'C^2 m^2 J^-1', 5.1e-51, 'atomic unit of electric polarizability'),
    'atomic_unit_of_electric_polarizablity': Constant(1.648777274e-41, 'C^2 m^2 J^-1', 1.6e-49, 'atomic unit of electric polarizablity'),
    'atomic_unit_of_electric_potential': Constant(27.211386245981, 'V', 3e-11, 'atomic unit of electric potential'),
    'atomic_unit_of_electric_quadrupole_mom': Constant(4.4865515185e-40, 'C m^2', 1.4e-49, 'atomic unit of electric quadrupole mom.'),
    'atomic_unit_of_electric_quadrupole_moment': Constant(4.48655124e-40, 'C m^2', 3.9e-47, 'atomic unit of electric quadrupole moment'),
    'atomic_unit_of_energy': Constant(4.359744722206e-18, 'J', 4.8e-30, 'atomic unit of energy'),
    'atomic_unit_of_force': Constant(8.2387235038e-08, 'N', 1.3e-17, 'atomic unit of force'),
    'atomic_unit_of_length': Constant(5.29177210544e-11, 'm', 8.2e-21, 'atomic unit of length'),
    'atomic_unit_of_mag_dipole_mom': Constant(1.85480201315e-23, 'J T^-1', 5.8e-33, 'atomic unit of mag. dipole mom.'),
    'atomic_unit_of_mag_flux_density': Constant(235051.757077, 'T', 7.3e-05, 'atomic unit of mag. flux density'),
    'atomic_unit_of_magn_dipole_moment': Constant(1.8548019e-23, 'J T^-1', 1.6e-30, 'atomic unit of magn. dipole moment'),
    'atomic_unit_of_magn_flux_density': Constant(235051.757077, 'T', 7.3e-05, 'atomic unit of magn. flux density'),
    'atomic_unit_of_magnetizability': Constant(7.8910365794e-29, 'J T^-2', 4.9e-38, 'atomic unit of magnetizability'),
    'atomic_unit_of_mass': Constant(9.1093837139e-31, 'kg', 2.8e-40, 'atomic unit of mass'),
    'atomic_unit_of_mom_um': Constant(1.992851882e-24, 'kg m s^-1', 2.4e-32, 'atomic unit of mom.um'),
    'atomic_unit_of_momentum': Constant(1.99285191545e-24, 'kg m s^-1', 3.1e-34, 'atomic unit of momentum'),
    'atomic_unit_of_permittivity': Constant(1.1126500562e-10, 'F m^-1', 1.7e-20, 'atomic unit of permittivity'),
    'atomic_unit_of_time': Constant(2.4188843265864e-17, 's', 2.6e-29, 'atomic unit of time'),
    'atomic_unit_of_velocity': Constant(2187691.26216, 'm s^-1', 0.00034, 'atomic unit of velocity'),
    'characteristic_impedance_of_vacuum': Constant(376.730313412, 'ohm', 5.9e-08, 'characteristic impedance of vacuum'),
    'classical_electron_radius': Constant(2.8179403205e-15, 'm', 1.3e-24, 'classical electron radius'),
    'conductance_quantum': Constant(7.748091729863649e-05, 'S', 0.0, 'conductance quantum'),
    'conventional_value_of_josephson_constant': Constant(483597900000000.0, 'Hz V^-1', 0.0, 'conventional value of Josephson constant'),
    'conventional_value_of_ampere_90': Constant(1.0000000888714378, 'A', 0.0, 'conventional value of ampere-90'),
    'conventional_value_of_coulomb_90': Constant(1.0000000888714378, 'C', 0.0, 'conventional value of coulomb-90'),
    'conventional_value_of_farad_90': Constant(0.9999999822063325, 'F', 0.0, 'conventional value of farad-90'),
    'conventional_value_of_henry_90': Constant(1.0000000177936679, 'H', 0.0, 'conventional value of henry-90'),
    'conventional_value_of_ohm_90': Constant(1.0000000177936679, 'ohm', 0.0, 'conventional value of ohm-90'),
    'conventional_value_of_volt_90': Constant(1.0000001066651072, 'V', 0.0, 'conventional value of volt-90'),
    'conventional_value_of_von_klitzing_constant': Constant(25812.807, 'ohm', 0.0, 'conventional value of von Klitzing constant'),
    'conventional_value_of_watt_90': Constant(1.0000001955365543, 'W', 0.0, 'conventional value of watt-90'),
    'deuteron_g_factor': Constant(0.8574382335, '', 2.2e-09, 'deuteron g factor'),
    'deuteron_mag_mom': Constant(4.330735087e-27, 'J T^-1', 1.1e-35, 'deuteron mag. mom.'),
    'deuteron_mag_mom_to_bohr_magneton_ratio': Constant(0.0004669754568, '', 1.2e-12, 'deuteron mag. mom. to Bohr magneton ratio'),
    'deuteron_mag_mom_to_nuclear_magneton_ratio': Constant(0.8574382335, '', 2.2e-09, 'deuteron mag. mom. to nuclear magneton ratio'),
    'deuteron_magn_moment': Constant(4.33073482e-27, 'J T^-1', 3.8e-34, 'deuteron magn. moment'),
    'deuteron_magn_moment_to_bohr_magneton_ratio': Constant(0.0004669754567, '', 5e-12, 'deuteron magn. moment to Bohr magneton ratio'),
    'deuteron_magn_moment_to_nuclear_magneton_ratio': Constant(0.8574382329, '', 9.2e-09, 'deuteron magn. moment to nuclear magneton ratio'),
    'deuteron_mass': Constant(3.3435837768e-27, 'kg', 1e-36, 'deuteron mass'),
    'deuteron_mass_energy_equivalent': Constant(3.00506323491e-10, 'J', 9.4e-20, 'deuteron mass energy equivalent'),
    'deuteron_mass_energy_equivalent_in_mev': Constant(1875.612945, 'MeV', 5.8e-07, 'deuteron mass energy equivalent in MeV'),
    'deuteron_mass_in_u': Constant(2.013553212544, 'u', 1.5e-11, 'deuteron mass in u'),
    'deuteron_molar_mass': Constant(0.00201355321466, 'kg mol^-1', 6.3e-13, 'deuteron molar mass'),
    'deuteron_relative_atomic_mass': Constant(2.013553212544, '', 1.5e-11, 'deuteron relative atomic mass'),
    'deuteron_rms_charge_radius': Constant(2.12778e-15, 'm', 2.7e-19, 'deuteron rms charge radius'),
    'deuteron_electron_mag_mom_ratio': Constant(-0.000466434555, '', 1.2e-12, 'deuteron-electron mag. mom. ratio'),
    'deuteron_electron_magn_moment_ratio': Constant(-0.0004664345548, '', 5e-12, 'deuteron-electron magn. moment ratio'),
    'deuteron_electron_mass_ratio': Constant(3670.482967655, '', 6.3e-08, 'deuteron-electron mass ratio'),
    'deuteron_neutron_mag_mom_ratio': Constant(-0.44820652, '', 1.1e-07, 'deuteron-neutron mag. mom. ratio'),
    'deuteron_neutron_magn_moment_ratio': Constant(-0.44820652, '', 1.1e-07, 'deuteron-neutron magn. moment ratio'),
    'deuteron_proton_mag_mom_ratio': Constant(0.3070122093, '', 7.9e-10, 'deuteron-proton mag. mom. ratio'),
    'deuteron_proton_magn_moment_ratio': Constant(0.3070122084, '', 4.5e-09, 'deuteron-proton magn. moment ratio'),
    'deuteron_proton_mass_ratio': Constant(1.9990075012699, '', 8.4e-12, 'deuteron-proton mass ratio'),
    'electric_constant': Constant(8.8541878188e-12, 'F m^-1', 1.4e-21, 'electric constant'),
    'electron_charge_to_mass_quotient': Constant(-175882000838.0, 'C kg^-1', 55.0, 'electron charge to mass quotient'),
    'electron_g_factor': Constant(-2.00231930436092, '', 3.6e-13, 'electron g factor'),
    'electron_gyromag_ratio': Constant(176085962784.0, 's^-1 T^-1', 55.0, 'electron gyromag. ratio'),
    'electron_gyromag_ratio_in_mhz_t': Constant(28024.9513861, 'MHz T^-1', 8.7e-06, 'electron gyromag. ratio in MHz/T'),
    'electron_gyromag_ratio_over_2_pi': Constant(28024.95164, 'MHz T^-1', 0.00017, 'electron gyromag. ratio over 2 pi'),
    'electron_gyromagn_ratio': Constant(176085962784.0, 's^-1 T^-1', 55.0, 'electron gyromagn. ratio'),
    'electron_gyromagn_ratio_over_2_pi': Constant(28024.9532, 'MHz T^-1', 0.0024, 'electron gyromagn. ratio over 2 pi'),
    'electron_mag_mom': Constant(-9.2847646917e-24, 'J T^-1', 2.9e-33, 'electron mag. mom.'),
    'electron_mag_mom_anomaly': Constant(0.00115965218046, '', 1.8e-13, 'electron mag. mom. anomaly'),
    'electron_mag_mom_to_bohr_magneton_ratio': Constant(-1.00115965218046, '', 1.8e-13, 'electron mag. mom. to Bohr magneton ratio'),
    'electron_mag_mom_to_nuclear_magneton_ratio': Constant(-1838.281971877, '', 3.2e-08, 'electron mag. mom. to nuclear magneton ratio'),
    'electron_magn_moment': Constant(-9.28476412e-24, 'J T^-1', 8e-31, 'electron magn. moment'),
    'electron_magn_moment_anomaly': Constant(0.0011596521859, '', 3.8e-12, 'electron magn. moment anomaly'),
    'electron_magn_moment_to_bohr_magneton_ratio': Constant(-1.0011596521859, '', 3.8e-12, 'electron magn. moment to Bohr magneton ratio'),
    'electron_magn_moment_to_nuclear_magneton_ratio': Constant(-1838.28197107, '', 8.5e-07, 'electron magn. moment to nuclear magneton ratio'),
    'electron_mass': Constant(9.1093837139e-31, 'kg', 2.8e-40, 'electron mass'),
    'electron_mass_energy_equivalent': Constant(8.187105788e-14, 'J', 2.6e-23, 'electron mass energy equivalent'),
    'electron_mass_energy_equivalent_in_mev': Constant(0.51099895069, 'MeV', 1.6e-10, 'electron mass energy equivalent in MeV'),
    'electron_mass_in_u': Constant(0.0005485799090441, 'u', 9.7e-15, 'electron mass in u'),
    'electron_molar_mass': Constant(5.4857990962e-07, 'kg mol^-1', 1.7e-16, 'electron molar mass'),
    'electron_relative_atomic_mass': Constant(0.0005485799090441, '', 9.7e-15, 'electron relative atomic mass'),
    'electron_to_alpha_particle_mass_ratio': Constant(0.0001370933554733, '', 3.2e-15, 'electron to alpha particle mass ratio'),
    'electron_to_shielded_helion_mag_mom_ratio': Constant(864.05823986, '', 7e-07, 'electron to shielded helion mag. mom. ratio'),
    'electron_to_shielded_helion_magn_moment_ratio': Constant(864.058255, '', 1e-05, 'electron to shielded helion magn. moment ratio'),
    'electron_to_shielded_proton_mag_mom_ratio': Constant(-658.2275856, '', 2.7e-06, 'electron to shielded proton mag. mom. ratio'),
    'electron_to_shielded_proton_magn_moment_ratio': Constant(-658.2275956, '', 7.1e-06, 'electron to shielded proton magn. moment ratio'),
    'electron_volt': Constant(1.602176634e-19, 'J', 0.0, 'electron volt'),
    'electron_volt_atomic_mass_unit_relationship': Constant(1.07354410083e-09, 'u', 3.3e-19, 'electron volt-atomic mass unit relationship'),
    'electron_volt_hartree_relationship': Constant(0.036749322175665, 'E_h', 4e-14, 'electron volt-hartree relationship'),
    'electron_volt_hertz_relationship': Constant(241798924208491.8, 'Hz', 0.0, 'electron volt-hertz relationship'),
    'electron_volt_inverse_meter_relationship': Constant(806554.3937349211, 'm^-1', 0.0, 'electron volt-inverse meter relationship'),
    'electron_volt_joule_relationship': Constant(1.602176634e-19, 'J', 0.0, 'electron volt-joule relationship'),
    'electron_volt_kelvin_relationship': Constant(11604.518121550082, 'K', 0.0, 'electron volt-kelvin relationship'),
    'electron_volt_kilogram_relationship': Constant(1.7826619216278975e-36, 'kg', 0.0, 'electron volt-kilogram relationship'),
    'electron_deuteron_mag_mom_ratio': Constant(-2143.9234921, '', 5.6e-06, 'electron-deuteron mag. mom. ratio'),
    'electron_deuteron_magn_moment_ratio': Constant(-2143.923493, '', 2.3e-05, 'electron-deuteron magn. moment ratio'),
    'electron_deuteron_mass_ratio': Constant(0.0002724437107629, '', 4.7e-15, 'electron-deuteron mass ratio'),
    'electron_helion_mass_ratio': Constant(0.0001819543074649, '', 5.3e-15, 'electron-helion mass ratio'),
    'electron_muon_mag_mom_ratio': Constant(206.7669881, '', 4.6e-06, 'electron-muon mag. mom. ratio'),
    'electron_muon_magn_moment_ratio': Constant(206.7669894, '', 5.4e-06, 'electron-muon magn. moment ratio'),
    'electron_muon_mass_ratio': Constant(0.0048363317, '', 1.1e-10, 'electron-muon mass ratio'),
    'electron_neutron_mag_mom_ratio': Constant(960.92048, '', 0.00023, 'electron-neutron mag. mom. ratio'),
    'electron_neutron_magn_moment_ratio': Constant(960.9205, '', 0.00023, 'electron-neutron magn. moment ratio'),
    'electron_neutron_mass_ratio': Constant(0.00054386734416, '', 2.2e-13, 'electron-neutron mass ratio'),
    'electron_proton_mag_mom_ratio': Constant(-658.21068789, '', 1.9e-07, 'electron-proton mag. mom. ratio'),
    'electron_proton_magn_moment_ratio': Constant(-658.2106862, '', 6.6e-06, 'electron-proton magn. moment ratio'),
    'electron_proton_mass_ratio': Constant(0.0005446170214889, '', 9.4e-15, 'electron-proton mass ratio'),
    'electron_tau_mass_ratio': Constant(0.000287585, '', 1.9e-08, 'electron-tau mass ratio'),
    'electron_triton_mass_ratio': Constant(0.0001819200062327, '', 6.8e-15, 'electron-triton mass ratio'),
    'elementary_charge': Constant(1.602176634e-19, 'C', 0.0, 'elementary charge'),
    'elementary_charge_over_h': Constant(241798926200000.0, 'A J^-1', 1500000.0, 'elementary charge over h'),
    'elementary_charge_over_h_bar': Constant(1519267447878626.0, 'A J^-1', 0.0, 'elementary charge over h-bar'),
    'fine_structure_constant': Constant(0.0072973525643, '', 1.1e-12, 'fine-structure constant'),
    'first_radiation_constant': Constant(3.7417718521927573e-16, 'W m^2', 0.0, 'first radiation constant'),
    'first_radiation_constant_for_spectral_radiance': Constant(1.1910429723971884e-16, 'W m^2 sr^-1', 0.0, 'first radiation constant for spectral radiance'),
    'hartree_atomic_mass_unit_relationship': Constant(2.92126231797e-08, 'u', 9.1e-18, 'hartree-atomic mass unit relationship'),
    'hartree_electron_volt_relationship': Constant(27.211386245981, 'eV', 3e-11, 'hartree-electron volt relationship'),
    'hartree_hertz_relationship': Constant(6579683920499900.0, 'Hz', 7200.0, 'hartree-hertz relationship'),
    'hartree_inverse_meter_relationship': Constant(21947463.136314, 'm^-1', 2.4e-05, 'hartree-inverse meter relationship'),
    'hartree_joule_relationship': Constant(4.359744722206e-18, 'J', 4.8e-30, 'hartree-joule relationship'),
    'hartree_kelvin_relationship': Constant(315775.02480398, 'K', 3.4e-07, 'hartree-kelvin relationship'),
    'hartree_kilogram_relationship': Constant(4.8508702095419e-35, 'kg', 5.3e-47, 'hartree-kilogram relationship'),
    'helion_g_factor': Constant(-4.2552506995, '', 3.4e-09, 'helion g factor'),
    'helion_mag_mom': Constant(-1.07461755198e-26, 'J T^-1', 9.3e-36, 'helion mag. mom.'),
    'helion_mag_mom_to_bohr_magneton_ratio': Constant(-0.00115874098083, '', 9.4e-13, 'helion mag. mom. to Bohr magneton ratio'),
    'helion_mag_mom_to_nuclear_magneton_ratio': Constant(-2.1276253498, '', 1.7e-09, 'helion mag. mom. to nuclear magneton ratio'),
    'helion_mass': Constant(5.0064127862e-27, 'kg', 1.6e-36, 'helion mass'),
    'helion_mass_energy_equivalent': Constant(4.4995394185e-10, 'J', 1.4e-19, 'helion mass energy equivalent'),
    'helion_mass_energy_equivalent_in_mev': Constant(2808.39161112, 'MeV', 8.8e-07, 'helion mass energy equivalent in MeV'),
    'helion_mass_in_u': Constant(3.014932246932, 'u', 7.4e-11, 'helion mass in u'),
    'helion_molar_mass': Constant(0.0030149322501, 'kg mol^-1', 9.4e-13, 'helion molar mass'),
    'helion_relative_atomic_mass': Constant(3.014932246932, '', 7.4e-11, 'helion relative atomic mass'),
    'helion_shielding_shift': Constant(5.9967029e-05, '', 2.3e-11, 'helion shielding shift'),
    'helion_electron_mass_ratio': Constant(5495.88527984, '', 1.6e-07, 'helion-electron mass ratio'),
    'helion_proton_mass_ratio': Constant(2.993152671552, '', 7e-11, 'helion-proton mass ratio'),
    'hertz_atomic_mass_unit_relationship': Constant(4.439821659e-24, 'u', 1.4e-33, 'hertz-atomic mass unit relationship'),
    'hertz_electron_volt_relationship': Constant(4.135667696923859e-15, 'eV', 0.0, 'hertz-electron volt relationship'),
    'hertz_hartree_relationship': Constant(1.5198298460574e-16, 'E_h', 1.7e-28, 'hertz-hartree relationship'),
    'hertz_inverse_meter_relationship': Constant(3.3356409519815204e-09, 'm^-1', 0.0, 'hertz-inverse meter relationship'),
    'hertz_joule_relationship': Constant(6.62607015e-34, 'J', 0.0, 'hertz-joule relationship'),
    'hertz_kelvin_relationship': Constant(4.799243073366221e-11, 'K', 0.0, 'hertz-kelvin relationship'),
    'hertz_kilogram_relationship': Constant(7.372497323812708e-51, 'kg', 0.0, 'hertz-kilogram relationship'),
    'hyperfine_transition_frequency_of_cs_133': Constant(9192631770.0, 'Hz', 0.0, 'hyperfine transition frequency of Cs-133'),
    'inverse_fine_structure_constant': Constant(137.035999177, '', 2.1e-08, 'inverse fine-structure constant'),
    'inverse_meter_atomic_mass_unit_relationship': Constant(1.33102504824e-15, 'u', 4.1e-25, 'inverse meter-atomic mass unit relationship'),
    'inverse_meter_electron_volt_relationship': Constant(1.2398419843320026e-06, 'eV', 0.0, 'inverse meter-electron volt relationship'),
    'inverse_meter_hartree_relationship': Constant(4.5563352529132e-08, 'E_h', 5e-20, 'inverse meter-hartree relationship'),
    'inverse_meter_hertz_relationship': Constant(299792458.0, 'Hz', 0.0, 'inverse meter-hertz relationship'),
    'inverse_meter_joule_relationship': Constant(1.9864458571489286e-25, 'J', 0.0, 'inverse meter-joule relationship'),
    'inverse_meter_kelvin_relationship': Constant(0.014387768775039337, 'K', 0.0, 'inverse meter-kelvin relationship'),
    'inverse_meter_kilogram_relationship': Constant(2.2102190943042335e-42, 'kg', 0.0, 'inverse meter-kilogram relationship'),
    'inverse_of_conductance_quantum': Constant(12906.403729652257, 'ohm', 0.0, 'inverse of conductance quantum'),
    'joule_atomic_mass_unit_relationship': Constant(6700535247.1, 'u', 2.1, 'joule-atomic mass unit relationship'),
    'joule_electron_volt_relationship': Constant(6.241509074460763e+18, 'eV', 0.0, 'joule-electron volt relationship'),
    'joule_hartree_relationship': Constant(2.2937122783969e+17, 'E_h', 250000.0, 'joule-hartree relationship'),
    'joule_hertz_relationship': Constant(1.5091901796421518e+33, 'Hz', 0.0, 'joule-hertz relationship'),
    'joule_inverse_meter_relationship': Constant(5.03411656754271e+24, 'm^-1', 0.0, 'joule-inverse meter relationship'),
    'joule_kelvin_relationship': Constant(7.24297051603992e+22, 'K', 0.0, 'joule-kelvin relationship'),
    'joule_kilogram_relationship': Constant(1.1126500560536185e-17, 'kg', 0.0, 'joule-kilogram relationship'),
    'kelvin_atomic_mass_unit_relationship': Constant(9.2510872884e-14, 'u', 2.9e-23, 'kelvin-atomic mass unit relationship'),
    'kelvin_electron_volt_relationship': Constant(8.617333262145179e-05, 'eV', 0.0, 'kelvin-electron volt relationship'),
    'kelvin_hartree_relationship': Constant(3.1668115634564e-06, 'E_h', 3.5e-18, 'kelvin-hartree relationship'),
    'kelvin_hertz_relationship': Constant(20836619123.327576, 'Hz', 0.0, 'kelvin-hertz relationship'),
    'kelvin_inverse_meter_relationship': Constant(69.50348004861274, 'm^-1', 0.0, 'kelvin-inverse meter relationship'),
    'kelvin_joule_relationship': Constant(1.380649e-23, 'J', 0.0, 'kelvin-joule relationship'),
    'kelvin_kilogram_relationship': Constant(1.5361791872403723e-40, 'kg', 0.0, 'kelvin-kilogram relationship'),
    'kilogram_atomic_mass_unit_relationship': Constant(6.0221407537e+26, 'u', 1.9e+17, 'kilogram-atomic mass unit relationship'),
    'kilogram_electron_volt_relationship': Constant(5.609588603804452e+35, 'eV', 0.0, 'kilogram-electron volt relationship'),
    'kilogram_hartree_relationship': Constant(2.0614857887415e+34, 'E_h', 2.2e+22, 'kilogram-hartree relationship'),
    'kilogram_hertz_relationship': Constant(1.3563924896521321e+50, 'Hz', 0.0, 'kilogram-hertz relationship'),
    'kilogram_inverse_meter_relationship': Constant(4.524438335443823e+41, 'm^-1', 0.0, 'kilogram-inverse meter relationship'),
    'kilogram_joule_relationship': Constant(8.987551787368176e+16, 'J', 0.0, 'kilogram-joule relationship'),
    'kilogram_kelvin_relationship': Constant(6.509657260728958e+39, 'K', 0.0, 'kilogram-kelvin relationship'),
    'lattice_parameter_of_silicon': Constant(5.431020511e-10, 'm', 8.9e-18, 'lattice parameter of silicon'),
    'lattice_spacing_of_ideal_si_220': Constant(1.920155716e-10, 'm', 3.2e-18, 'lattice spacing of ideal Si (220)'),
    'lattice_spacing_of_silicon': Constant(1.920155762e-10, 'm', 5e-18, 'lattice spacing of silicon'),
    'luminous_efficacy': Constant(683.0, 'lm W^-1', 0.0, 'luminous efficacy'),
    'mag_constant': Constant(1.25663706127e-06, 'N A^-2', 2e-16, 'mag. constant'),
    'mag_flux_quantum': Constant(2.0678338484619295e-15, 'Wb', 0.0, 'mag. flux quantum'),
    'magn_constant': Constant(1.2566370614359173e-06, 'N A^-2', 0.0, 'magn. constant'),
    'magn_flux_quantum': Constant(2.0678338484619295e-15, 'Wb', 0.0, 'magn. flux quantum'),
    'molar_planck_constant': Constant(3.990312712893431e-10, 'J Hz^-1 mol^-1', 0.0, 'molar Planck constant'),
    'molar_planck_constant_times_c': Constant(0.119626565582, 'J m mol^-1', 5.4e-11, 'molar Planck constant times c'),
    'molar_gas_constant': Constant(8.31446261815324, 'J mol^-1 K^-1', 0.0, 'molar gas constant'),
    'molar_mass_constant': Constant(0.00100000000105, 'kg mol^-1', 3.1e-13, 'molar mass constant'),
    'molar_mass_of_carbon_12': Constant(0.0120000000126, 'kg mol^-1', 3.7e-12, 'molar mass of carbon-12'),
    'molar_volume_of_ideal_gas_273_15_k_100_kpa': Constant(0.02271095464148557, 'm^3 mol^-1', 0.0, 'molar volume of ideal gas (273.15 K, 100 kPa)'),
    'molar_volume_of_ideal_gas_273_15_k_101_325_kpa': Constant(0.022413969545014137, 'm^3 mol^-1', 0.0, 'molar volume of ideal gas (273.15 K, 101.325 kPa)'),
    'molar_volume_of_silicon': Constant(1.205883199e-05, 'm^3 mol^-1', 6e-13, 'molar volume of silicon'),
    'muon_compton_wavelength': Constant(1.17344411e-14, 'm', 2.6e-22, 'muon Compton wavelength'),
    'muon_compton_wavelength_over_2_pi': Constant(1.867594308e-15, 'm', 4.2e-23, 'muon Compton wavelength over 2 pi'),
    'muon_g_factor': Constant(-2.00233184123, '', 8.2e-10, 'muon g factor'),
    'muon_mag_mom': Constant(-4.4904483e-26, 'J T^-1', 1e-33, 'muon mag. mom.'),
    'muon_mag_mom_anomaly': Constant(0.00116592062, '', 4.1e-10, 'muon mag. mom. anomaly'),
    'muon_mag_mom_to_bohr_magneton_ratio': Constant(-0.00484197048, '', 1.1e-10, 'muon mag. mom. to Bohr magneton ratio'),
    'muon_mag_mom_to_nuclear_magneton_ratio': Constant(-8.89059704, '', 2e-07, 'muon mag. mom. to nuclear magneton ratio'),
    'muon_magn_moment': Constant(-4.49044799e-26, 'J T^-1', 4e-33, 'muon magn. moment'),
    'muon_magn_moment_to_bohr_magneton_ratio': Constant(-0.00484197045, '', 1.3e-10, 'muon magn. moment to Bohr magneton ratio'),
    'muon_magn_moment_to_nuclear_magneton_ratio': Constant(-8.89059698, '', 2.3e-07, 'muon magn. moment to nuclear magneton ratio'),
    'muon_mass': Constant(1.883531627e-28, 'kg', 4.2e-36, 'muon mass'),
    'muon_mass_energy_equivalent': Constant(1.692833804e-11, 'J', 3.8e-19, 'muon mass energy equivalent'),
    'muon_mass_energy_equivalent_in_mev': Constant(105.6583755, 'MeV', 2.3e-06, 'muon mass energy equivalent in MeV'),
    'muon_mass_in_u': Constant(0.1134289257, 'u', 2.5e-09, 'muon mass in u'),
    'muon_molar_mass': Constant(0.0001134289258, 'kg mol^-1', 2.5e-12, 'muon molar mass'),
    'muon_electron_mass_ratio': Constant(206.7682827, '', 4.6e-06, 'muon-electron mass ratio'),
    'muon_neutron_mass_ratio': Constant(0.1124545168, '', 2.5e-09, 'muon-neutron mass ratio'),
    'muon_proton_mag_mom_ratio': Constant(-3.183345146, '', 7.1e-08, 'muon-proton mag. mom. ratio'),
    'muon_proton_magn_moment_ratio': Constant(-3.183345118, '', 8.9e-08, 'muon-proton magn. moment ratio'),
    'muon_proton_mass_ratio': Constant(0.1126095262, '', 2.5e-09, 'muon-proton mass ratio'),
    'muon_tau_mass_ratio': Constant(0.0594635, '', 4e-06, 'muon-tau mass ratio'),
    'natural_unit_of_action': Constant(1.0545718176461565e-34, 'J s', 0.0, 'natural unit of action'),
    'natural_unit_of_action_in_ev_s': Constant(6.582119569509067e-16, 'eV s', 0.0, 'natural unit of action in eV s'),
    'natural_unit_of_energy': Constant(8.187105788e-14, 'J', 2.6e-23, 'natural unit of energy'),
    'natural_unit_of_energy_in_mev': Constant(0.51099895069, 'MeV', 1.6e-10, 'natural unit of energy in MeV'),
    'natural_unit_of_length': Constant(3.8615926744e-13, 'm', 1.2e-22, 'natural unit of length'),
    'natural_unit_of_mass': Constant(9.1093837139e-31, 'kg', 2.8e-40, 'natural unit of mass'),
    'natural_unit_of_mom_um': Constant(2.730924488e-22, 'kg m s^-1', 3.4e-30, 'natural unit of mom.um'),
    'natural_unit_of_mom_um_in_mev_c': Constant(0.5109989461, 'MeV/c', 3.1e-09, 'natural unit of mom.um in MeV/c'),
    'natural_unit_of_momentum': Constant(2.730924488e-22, 'kg m s^-1', 3.4e-30, 'natural unit of momentum'),
    'natural_unit_of_momentum_in_mev_c': Constant(0.5109989461, 'MeV/c', 3.1e-09, 'natural unit of momentum in MeV/c'),
    'natural_unit_of_time': Constant(1.28808866644e-21, 's', 4e-31, 'natural unit of time'),
    'natural_unit_of_velocity': Constant(299792458.0, 'm s^-1', 0.0, 'natural unit of velocity'),
    'neutron_compton_wavelength': Constant(1.31959090382e-15, 'm', 6.7e-25, 'neutron Compton wavelength'),
    'neutron_compton_wavelength_over_2_pi': Constant(2.1001941536e-16, 'm', 1.4e-25, 'neutron Compton wavelength over 2 pi'),
    'neutron_g_factor': Constant(-3.82608552, '', 9e-07, 'neutron g factor'),
    'neutron_gyromag_ratio': Constant(183247174.0, 's^-1 T^-1', 43.0, 'neutron gyromag. ratio'),
    'neutron_gyromag_ratio_in_mhz_t': Constant(29.1646935, 'MHz T^-1', 6.9e-06, 'neutron gyromag. ratio in MHz/T'),
    'neutron_gyromag_ratio_over_2_pi': Constant(29.1646933, 'MHz T^-1', 6.9e-06, 'neutron gyromag. ratio over 2 pi'),
    'neutron_gyromagn_ratio': Constant(183247174.0, 's^-1 T^-1', 43.0, 'neutron gyromagn. ratio'),
    'neutron_gyromagn_ratio_over_2_pi': Constant(29.164695, 'MHz T^-1', 7.3e-06, 'neutron gyromagn. ratio over 2 pi'),
    'neutron_mag_mom': Constant(-9.6623653e-27, 'J T^-1', 2.3e-33, 'neutron mag. mom.'),
    'neutron_mag_mom_to_bohr_magneton_ratio': Constant(-0.00104187565, '', 2.5e-10, 'neutron mag. mom. to Bohr magneton ratio'),
    'neutron_mag_mom_to_nuclear_magneton_ratio': Constant(-1.91304276, '', 4.5e-07, 'neutron mag. mom. to nuclear magneton ratio'),
    'neutron_magn_moment': Constant(-9.6623645e-27, 'J T^-1', 2.4e-33, 'neutron magn. moment'),
    'neutron_magn_moment_to_bohr_magneton_ratio': Constant(-0.00104187563, '', 2.5e-10, 'neutron magn. moment to Bohr magneton ratio'),
    'neutron_magn_moment_to_nuclear_magneton_ratio': Constant(-1.91304273, '', 4.5e-07, 'neutron magn. moment to nuclear magneton ratio'),
    'neutron_mass': Constant(1.67492750056e-27, 'kg', 8.5e-37, 'neutron mass'),
    'neutron_mass_energy_equivalent': Constant(1.50534976514e-10, 'J', 7.6e-20, 'neutron mass energy equivalent'),
    'neutron_mass_energy_equivalent_in_mev': Constant(939.56542194, 'MeV', 4.8e-07, 'neutron mass energy equivalent in MeV'),
    'neutron_mass_in_u': Constant(1.00866491606, 'u', 4e-10, 'neutron mass in u'),
    'neutron_molar_mass': Constant(0.00100866491712, 'kg mol^-1', 5.1e-13, 'neutron molar mass'),
    'neutron_relative_atomic_mass': Constant(1.00866491606, '', 4e-10, 'neutron relative atomic mass'),
    'neutron_to_shielded_proton_mag_mom_ratio': Constant(-0.68499694, '', 1.6e-07, 'neutron to shielded proton mag. mom. ratio'),
    'neutron_to_shielded_proton_magn_moment_ratio': Constant(-0.68499694, '', 1.6e-07, 'neutron to shielded proton magn. moment ratio'),
    'neutron_electron_mag_mom_ratio': Constant(0.00104066884, '', 2.4e-10, 'neutron-electron mag. mom. ratio'),
    'neutron_electron_magn_moment_ratio': Constant(0.00104066882, '', 2.5e-10, 'neutron-electron magn. moment ratio'),
    'neutron_electron_mass_ratio': Constant(1838.683662, '', 7.4e-07, 'neutron-electron mass ratio'),
    'neutron_muon_mass_ratio': Constant(8.89248408, '', 2e-07, 'neutron-muon mass ratio'),
    'neutron_proton_mag_mom_ratio': Constant(-0.68497935, '', 1.6e-07, 'neutron-proton mag. mom. ratio'),
    'neutron_proton_magn_moment_ratio': Constant(-0.68497934, '', 1.6e-07, 'neutron-proton magn. moment ratio'),
    'neutron_proton_mass_difference': Constant(2.30557461e-30, 'kg', 6.7e-37, 'neutron-proton mass difference'),
    'neutron_proton_mass_difference_energy_equivalent': Constant(2.07214712e-13, 'J', 6e-20, 'neutron-proton mass difference energy equivalent'),
    'neutron_proton_mass_difference_energy_equivalent_in_mev': Constant(1.29333251, 'MeV', 3.8e-07, 'neutron-proton mass difference energy equivalent in MeV'),
    'neutron_proton_mass_difference_in_u': Constant(0.00138844948, 'u', 4e-10, 'neutron-proton mass difference in u'),
    'neutron_proton_mass_ratio': Constant(1.00137841946, '', 4e-10, 'neutron-proton mass ratio'),
    'neutron_tau_mass_ratio': Constant(0.528779, '', 3.6e-05, 'neutron-tau mass ratio'),
    'nuclear_magneton': Constant(5.0507837393e-27, 'J T^-1', 1.6e-36, 'nuclear magneton'),
    'nuclear_magneton_in_k_t': Constant(0.00036582677706, 'K T^-1', 1.1e-13, 'nuclear magneton in K/T'),
    'nuclear_magneton_in_mhz_t': Constant(7.6225932188, 'MHz T^-1', 2.4e-09, 'nuclear magneton in MHz/T'),
    'nuclear_magneton_in_ev_t': Constant(3.15245125417e-08, 'eV T^-1', 9.8e-18, 'nuclear magneton in eV/T'),
    'nuclear_magneton_in_inverse_meter_per_tesla': Constant(0.0254262341009, 'm^-1 T^-1', 7.9e-12, 'nuclear magneton in inverse meter per tesla'),
    'nuclear_magneton_in_inverse_meters_per_tesla': Constant(0.02542623432, 'm^-1 T^-1', 1.6e-10, 'nuclear magneton in inverse meters per tesla'),
    'proton_compton_wavelength': Constant(1.3214098536e-15, 'm', 4.1e-25, 'proton Compton wavelength'),
    'proton_compton_wavelength_over_2_pi': Constant(2.10308910109e-16, 'm', 9.7e-26, 'proton Compton wavelength over 2 pi'),
    'proton_charge_to_mass_quotient': Constant(95788331.43, 'C kg^-1', 0.03, 'proton charge to mass quotient'),
    'proton_g_factor': Constant(5.5856946893, '', 1.6e-09, 'proton g factor'),
    'proton_gyromag_ratio': Constant(267522187.08, 's^-1 T^-1', 0.11, 'proton gyromag. ratio'),
    'proton_gyromag_ratio_in_mhz_t': Constant(42.577478461, 'MHz T^-1', 1.8e-08, 'proton gyromag. ratio in MHz/T'),
    'proton_gyromag_ratio_over_2_pi': Constant(42.57747892, 'MHz T^-1', 2.9e-07, 'proton gyromag. ratio over 2 pi'),
    'proton_gyromagn_ratio': Constant(267522187.08, 's^-1 T^-1', 0.11, 'proton gyromagn. ratio'),
    'proton_gyromagn_ratio_over_2_pi': Constant(42.5774813, 'MHz T^-1', 3.7e-06, 'proton gyromagn. ratio over 2 pi'),
    'proton_mag_mom': Constant(1.41060679545e-26, 'J T^-1', 6e-36, 'proton mag. mom.'),
    'proton_mag_mom_to_bohr_magneton_ratio': Constant(0.0015210322023, '', 4.5e-13, 'proton mag. mom. to Bohr magneton ratio'),
    'proton_mag_mom_to_nuclear_magneton_ratio': Constant(2.79284734463, '', 8.2e-10, 'proton mag. mom. to nuclear magneton ratio'),
    'proton_mag_shielding_correction': Constant(2.56715e-05, '', 4.1e-09, 'proton mag. shielding correction'),
    'proton_magn_moment': Constant(1.41060671e-26, 'J T^-1', 1.2e-33, 'proton magn. moment'),
    'proton_magn_moment_to_bohr_magneton_ratio': Constant(0.001521032206, '', 1.5e-11, 'proton magn. moment to Bohr magneton ratio'),
    'proton_magn_moment_to_nuclear_magneton_ratio': Constant(2.792847351, '', 2.8e-08, 'proton magn. moment to nuclear magneton ratio'),
    'proton_magn_shielding_correction': Constant(2.56715e-05, '', 4.1e-09, 'proton magn. shielding correction'),
    'proton_mass': Constant(1.67262192595e-27, 'kg', 5.2e-37, 'proton mass'),
    'proton_mass_energy_equivalent': Constant(1.50327761802e-10, 'J', 4.7e-20, 'proton mass energy equivalent'),
    'proton_mass_energy_equivalent_in_mev': Constant(938.27208943, 'MeV', 2.9e-07, 'proton mass energy equivalent in MeV'),
    'proton_mass_in_u': Constant(1.0072764665789, 'u', 8.3e-12, 'proton mass in u'),
    'proton_molar_mass': Constant(0.00100727646764, 'kg mol^-1', 3.1e-13, 'proton molar mass'),
    'proton_relative_atomic_mass': Constant(1.0072764665789, '', 8.3e-12, 'proton relative atomic mass'),
    'proton_rms_charge_radius': Constant(8.4075e-16, 'm', 6.4e-19, 'proton rms charge radius'),
    'proton_electron_mass_ratio': Constant(1836.152673426, '', 3.2e-08, 'proton-electron mass ratio'),
    'proton_muon_mass_ratio': Constant(8.88024338, '', 2e-07, 'proton-muon mass ratio'),
    'proton_neutron_mag_mom_ratio': Constant(-1.45989802, '', 3.4e-07, 'proton-neutron mag. mom. ratio'),
    'proton_neutron_magn_moment_ratio': Constant(-1.45989805, '', 3.4e-07, 'proton-neutron magn. moment ratio'),
    'proton_neutron_mass_ratio': Constant(0.99862347797, '', 4e-10, 'proton-neutron mass ratio'),
    'proton_tau_mass_ratio': Constant(0.528051, '', 3.6e-05, 'proton-tau mass ratio'),
    'quantum_of_circulation': Constant(0.00036369475467, 'm^2 s^-1', 1.1e-13, 'quantum of circulation'),
    'quantum_of_circulation_times_2': Constant(0.00072738950934, 'm^2 s^-1', 2.3e-13, 'quantum of circulation times 2'),
    'reduced_compton_wavelength': Constant(3.8615926744e-13, 'm', 1.2e-22, 'reduced Compton wavelength'),
    'reduced_planck_constant': Constant(1.0545718176461565e-34, 'J s', 0.0, 'reduced Planck constant'),
    'reduced_planck_constant_in_ev_s': Constant(6.582119569509067e-16, 'eV s', 0.0, 'reduced Planck constant in eV s'),
    'reduced_planck_constant_times_c_in_mev_fm': Constant(197.3269804593025, 'MeV fm', 0.0, 'reduced Planck constant times c in MeV fm'),
    'reduced_muon_compton_wavelength': Constant(1.867594306e-15, 'm', 4.2e-23, 'reduced muon Compton wavelength'),
    'reduced_neutron_compton_wavelength': Constant(2.100194152e-16, 'm', 1.1e-25, 'reduced neutron Compton wavelength'),
    'reduced_proton_compton_wavelength': Constant(2.10308910051e-16, 'm', 6.6e-26, 'reduced proton Compton wavelength'),
    'reduced_tau_compton_wavelength': Constant(1.110538e-16, 'm', 7.5e-21, 'reduced tau Compton wavelength'),
    'second_radiation_constant': Constant(0.014387768775039337, 'm K', 0.0, 'second radiation constant'),
    'shielded_helion_gyromag_ratio': Constant(203789460.78, 's^-1 T^-1', 0.18, 'shielded helion gyromag. ratio'),
    'shielded_helion_gyromag_ratio_in_mhz_t': Constant(32.434100033, 'MHz T^-1', 2.8e-08, 'shielded helion gyromag. ratio in MHz/T'),
    'shielded_helion_gyromag_ratio_over_2_pi': Constant(32.43409966, 'MHz T^-1', 4.3e-07, 'shielded helion gyromag. ratio over 2 pi'),
    'shielded_helion_gyromagn_ratio': Constant(203789460.78, 's^-1 T^-1', 0.18, 'shielded helion gyromagn. ratio'),
    'shielded_helion_gyromagn_ratio_over_2_pi': Constant(32.4341015, 'MHz T^-1', 2.8e-06, 'shielded helion gyromagn. ratio over 2 pi'),
    'shielded_helion_mag_mom': Constant(-1.07455311035e-26, 'J T^-1', 9.3e-36, 'shielded helion mag. mom.'),
    'shielded_helion_mag_mom_to_bohr_magneton_ratio': Constant(-0.00115867149457, '', 9.4e-13, 'shielded helion mag. mom. to Bohr magneton ratio'),
    'shielded_helion_mag_mom_to_nuclear_magneton_ratio': Constant(-2.1274977624, '', 1.7e-09, 'shielded helion mag. mom. to nuclear magneton ratio'),
    'shielded_helion_magn_moment': Constant(-1.074553024e-26, 'J T^-1', 9.3e-34, 'shielded helion magn. moment'),
    'shielded_helion_magn_moment_to_bohr_magneton_ratio': Constant(-0.001158671474, '', 1.4e-11, 'shielded helion magn. moment to Bohr magneton ratio'),
    'shielded_helion_magn_moment_to_nuclear_magneton_ratio': Constant(-2.127497723, '', 2.5e-08, 'shielded helion magn. moment to nuclear magneton ratio'),
    'shielded_helion_to_proton_mag_mom_ratio': Constant(-0.76176657721, '', 6.6e-10, 'shielded helion to proton mag. mom. ratio'),
    'shielded_helion_to_proton_magn_moment_ratio': Constant(-0.761766562, '', 1.2e-08, 'shielded helion to proton magn. moment ratio'),
    'shielded_helion_to_shielded_proton_mag_mom_ratio': Constant(-0.7617861334, '', 3.1e-09, 'shielded helion to shielded proton mag. mom. ratio'),
    'shielded_helion_to_shielded_proton_magn_moment_ratio': Constant(-0.7617861313, '', 3.3e-09, 'shielded helion to shielded proton magn. moment ratio'),
    'shielded_proton_gyromag_ratio': Constant(267515319.4, 's^-1 T^-1', 1.1, 'shielded proton gyromag. ratio'),
    'shielded_proton_gyromag_ratio_in_mhz_t': Constant(42.57638543, 'MHz T^-1', 1.7e-07, 'shielded proton gyromag. ratio in MHz/T'),
    'shielded_proton_gyromag_ratio_over_2_pi': Constant(42.57638507, 'MHz T^-1', 5.3e-07, 'shielded proton gyromag. ratio over 2 pi'),
    'shielded_proton_mag_mom': Constant(1.410570583e-26, 'J T^-1', 5.8e-35, 'shielded proton mag. mom.'),
    'shielded_proton_mag_mom_to_bohr_magneton_ratio': Constant(0.0015209931551, '', 6.2e-12, 'shielded proton mag. mom. to Bohr magneton ratio'),
    'shielded_proton_mag_mom_to_nuclear_magneton_ratio': Constant(2.792775648, '', 1.1e-08, 'shielded proton mag. mom. to nuclear magneton ratio'),
    'shielded_proton_magn_moment': Constant(1.41057047e-26, 'J T^-1', 1.2e-33, 'shielded proton magn. moment'),
    'shielded_proton_magn_moment_to_bohr_magneton_ratio': Constant(0.001520993132, '', 1.6e-11, 'shielded proton magn. moment to Bohr magneton ratio'),
    'shielded_proton_magn_moment_to_nuclear_magneton_ratio': Constant(2.792775604, '', 3e-08, 'shielded proton magn. moment to nuclear magneton ratio'),
    'shielding_difference_of_d_and_p_in_hd': Constant(1.9877e-08, '', 1e-12, 'shielding difference of d and p in HD'),
    'shielding_difference_of_t_and_p_in_ht': Constant(2.3945e-08, '', 2e-12, 'shielding difference of t and p in HT'),
    'speed_of_light_in_vacuum': Constant(299792458.0, 'm s^-1', 0.0, 'speed of light in vacuum'),
    'standard_acceleration_of_gravity': Constant(9.80665, 'm s^-2', 0.0, 'standard acceleration of gravity'),
    'standard_atmosphere': Constant(101325.0, 'Pa', 0.0, 'standard atmosphere'),
    'standard_state_pressure': Constant(100000.0, 'Pa', 0.0, 'standard-state pressure'),
    'tau_compton_wavelength': Constant(6.97771e-16, 'm', 4.7e-20, 'tau Compton wavelength'),
    'tau_compton_wavelength_over_2_pi': Constant(1.11056e-16, 'm', 1e-20, 'tau Compton wavelength over 2 pi'),
    'tau_energy_equivalent': Constant(1776.86, 'MeV', 0.12, 'tau energy equivalent'),
    'tau_mass': Constant(3.16754e-27, 'kg', 2.1e-31, 'tau mass'),
    'tau_mass_energy_equivalent': Constant(2.84684e-10, 'J', 1.9e-14, 'tau mass energy equivalent'),
    'tau_mass_energy_equivalent_in_mev': Constant(1776.82, 'MeV', 0.16, 'tau mass energy equivalent in MeV'),
    'tau_mass_in_u': Constant(1.90754, 'u', 0.00013, 'tau mass in u'),
    'tau_molar_mass': Constant(0.00190754, 'kg mol^-1', 1.3e-07, 'tau molar mass'),
    'tau_electron_mass_ratio': Constant(3477.23, '', 0.23, 'tau-electron mass ratio'),
    'tau_muon_mass_ratio': Constant(16.817, '', 0.0011, 'tau-muon mass ratio'),
    'tau_neutron_mass_ratio': Constant(1.89115, '', 0.00013, 'tau-neutron mass ratio'),
    'tau_proton_mass_ratio': Constant(1.89376, '', 0.00013, 'tau-proton mass ratio'),
    'triton_g_factor': Constant(5.95792493, '', 1.2e-08, 'triton g factor'),
    'triton_mag_mom': Constant(1.5046095178e-26, 'J T^-1', 3e-35, 'triton mag. mom.'),
    'triton_mag_mom_to_bohr_magneton_ratio': Constant(0.0016223936648, '', 3.2e-12, 'triton mag. mom. to Bohr magneton ratio'),
    'triton_mag_mom_to_nuclear_magneton_ratio': Constant(2.978962465, '', 5.9e-09, 'triton mag. mom. to nuclear magneton ratio'),
    'triton_mass': Constant(5.0073567512e-27, 'kg', 1.6e-36, 'triton mass'),
    'triton_mass_energy_equivalent': Constant(4.5003878119e-10, 'J', 1.4e-19, 'triton mass energy equivalent'),
    'triton_mass_energy_equivalent_in_mev': Constant(2808.92113668, 'MeV', 8.8e-07, 'triton mass energy equivalent in MeV'),
    'triton_mass_in_u': Constant(3.01550071597, 'u', 1e-10, 'triton mass in u'),
    'triton_molar_mass': Constant(0.00301550071913, 'kg mol^-1', 9.4e-13, 'triton molar mass'),
    'triton_relative_atomic_mass': Constant(3.01550071597, '', 1e-10, 'triton relative atomic mass'),
    'triton_to_proton_mag_mom_ratio': Constant(1.0666399189, '', 2.1e-09, 'triton to proton mag. mom. ratio'),
    'triton_electron_mag_mom_ratio': Constant(-0.001620514423, '', 2.1e-11, 'triton-electron mag. mom. ratio'),
    'triton_electron_mass_ratio': Constant(5496.92153551, '', 2.1e-07, 'triton-electron mass ratio'),
    'triton_neutron_mag_mom_ratio': Constant(-1.55718553, '', 3.7e-07, 'triton-neutron mag. mom. ratio'),
    'triton_proton_mag_mom_ratio': Constant(1.066639908, '', 1e-08, 'triton-proton mag. mom. ratio'),
    'triton_proton_mass_ratio': Constant(2.99371703403, '', 1e-10, 'triton-proton mass ratio'),
    'unified_atomic_mass_unit': Constant(1.66053906892e-27, 'kg', 5.2e-37, 'unified atomic mass unit'),
    'vacuum_electric_permittivity': Constant(8.8541878188e-12, 'F m^-1', 1.4e-21, 'vacuum electric permittivity'),
    'vacuum_mag_permeability': Constant(1.25663706127e-06, 'N A^-2', 2e-16, 'vacuum mag. permeability'),
    'von_klitzing_constant': Constant(25812.807459304513, 'ohm', 0.0, 'von Klitzing constant'),
    'weak_mixing_angle': Constant(0.22305, '', 0.00023, 'weak mixing angle'),
    'constant_220_lattice_spacing_of_silicon': Constant(1.920155714e-10, 'm', 3.2e-18, '{220} lattice spacing of silicon'),
}

CONSTANT_ALIASES = {
    'alpha_particle_electron_mass_ratio': 'alpha_particle_electron_mass_ratio',
    'alpha_particle_mass': 'alpha_particle_mass',
    'alpha_particle_mass_energy_equivalent': 'alpha_particle_mass_energy_equivalent',
    'alpha_particle_mass_energy_equivalent_in_mev': 'alpha_particle_mass_energy_equivalent_in_mev',
    'alpha_particle_mass_in_u': 'alpha_particle_mass_in_u',
    'alpha_particle_molar_mass': 'alpha_particle_molar_mass',
    'alpha_particle_proton_mass_ratio': 'alpha_particle_proton_mass_ratio',
    'alpha_particle_relative_atomic_mass': 'alpha_particle_relative_atomic_mass',
    'alpha_particle_rms_charge_radius': 'alpha_particle_rms_charge_radius',
    'angstrom_star': 'angstrom_star',
    'atomic_mass_constant': 'atomic_mass_constant',
    'atomic_mass_constant_energy_equivalent': 'atomic_mass_constant_energy_equivalent',
    'atomic_mass_constant_energy_equivalent_in_mev': 'atomic_mass_constant_energy_equivalent_in_mev',
    'atomic_mass_unit_electron_volt_relationship': 'atomic_mass_unit_electron_volt_relationship',
    'atomic_mass_unit_hartree_relationship': 'atomic_mass_unit_hartree_relationship',
    'atomic_mass_unit_hertz_relationship': 'atomic_mass_unit_hertz_relationship',
    'atomic_mass_unit_inverse_meter_relationship': 'atomic_mass_unit_inverse_meter_relationship',
    'atomic_mass_unit_joule_relationship': 'atomic_mass_unit_joule_relationship',
    'atomic_mass_unit_kelvin_relationship': 'atomic_mass_unit_kelvin_relationship',
    'atomic_mass_unit_kilogram_relationship': 'atomic_mass_unit_kilogram_relationship',
    'atomic_unit_of_1st_hyperpolarizability': 'atomic_unit_of_1st_hyperpolarizability',
    'atomic_unit_of_1st_hyperpolarizablity': 'atomic_unit_of_1st_hyperpolarizablity',
    'atomic_unit_of_2nd_hyperpolarizability': 'atomic_unit_of_2nd_hyperpolarizability',
    'atomic_unit_of_2nd_hyperpolarizablity': 'atomic_unit_of_2nd_hyperpolarizablity',
    'atomic_unit_of_action': 'atomic_unit_of_action',
    'atomic_unit_of_charge': 'atomic_unit_of_charge',
    'atomic_unit_of_charge_density': 'atomic_unit_of_charge_density',
    'atomic_unit_of_current': 'atomic_unit_of_current',
    'atomic_unit_of_electric_dipole_mom': 'atomic_unit_of_electric_dipole_mom',
    'atomic_unit_of_electric_dipole_moment': 'atomic_unit_of_electric_dipole_moment',
    'atomic_unit_of_electric_field': 'atomic_unit_of_electric_field',
    'atomic_unit_of_electric_field_gradient': 'atomic_unit_of_electric_field_gradient',
    'atomic_unit_of_electric_polarizability': 'atomic_unit_of_electric_polarizability',
    'atomic_unit_of_electric_polarizablity': 'atomic_unit_of_electric_polarizablity',
    'atomic_unit_of_electric_potential': 'atomic_unit_of_electric_potential',
    'atomic_unit_of_electric_quadrupole_mom': 'atomic_unit_of_electric_quadrupole_mom',
    'atomic_unit_of_electric_quadrupole_moment': 'atomic_unit_of_electric_quadrupole_moment',
    'atomic_unit_of_energy': 'atomic_unit_of_energy',
    'atomic_unit_of_force': 'atomic_unit_of_force',
    'atomic_unit_of_length': 'atomic_unit_of_length',
    'atomic_unit_of_mag_dipole_mom': 'atomic_unit_of_mag_dipole_mom',
    'atomic_unit_of_mag_flux_density': 'atomic_unit_of_mag_flux_density',
    'atomic_unit_of_magn_dipole_moment': 'atomic_unit_of_magn_dipole_moment',
    'atomic_unit_of_magn_flux_density': 'atomic_unit_of_magn_flux_density',
    'atomic_unit_of_magnetizability': 'atomic_unit_of_magnetizability',
    'atomic_unit_of_mass': 'atomic_unit_of_mass',
    'atomic_unit_of_mom_um': 'atomic_unit_of_mom_um',
    'atomic_unit_of_momentum': 'atomic_unit_of_momentum',
    'atomic_unit_of_permittivity': 'atomic_unit_of_permittivity',
    'atomic_unit_of_time': 'atomic_unit_of_time',
    'atomic_unit_of_velocity': 'atomic_unit_of_velocity',
    'avogadro_constant': 'avogadro_constant',
    'bohr_magneton': 'bohr_magneton',
    'bohr_magneton_in_ev_t': 'bohr_magneton_in_ev_t',
    'bohr_magneton_in_hz_t': 'bohr_magneton_in_hz_t',
    'bohr_magneton_in_inverse_meter_per_tesla': 'bohr_magneton_in_inverse_meter_per_tesla',
    'bohr_magneton_in_inverse_meters_per_tesla': 'bohr_magneton_in_inverse_meters_per_tesla',
    'bohr_magneton_in_k_t': 'bohr_magneton_in_k_t',
    'bohr_radius': 'bohr_radius',
    'boltzmann_constant': 'boltzmann_constant',
    'boltzmann_constant_in_ev_k': 'boltzmann_constant_in_ev_k',
    'boltzmann_constant_in_hz_k': 'boltzmann_constant_in_hz_k',
    'boltzmann_constant_in_inverse_meter_per_kelvin': 'boltzmann_constant_in_inverse_meter_per_kelvin',
    'boltzmann_constant_in_inverse_meters_per_kelvin': 'boltzmann_constant_in_inverse_meters_per_kelvin',
    'c': 'speed_of_light_in_vacuum',
    'characteristic_impedance_of_vacuum': 'characteristic_impedance_of_vacuum',
    'classical_electron_radius': 'classical_electron_radius',
    'compton_wavelength': 'compton_wavelength',
    'compton_wavelength_over_2_pi': 'compton_wavelength_over_2_pi',
    'conductance_quantum': 'conductance_quantum',
    'constant_220_lattice_spacing_of_silicon': 'constant_220_lattice_spacing_of_silicon',
    'conventional_value_of_ampere_90': 'conventional_value_of_ampere_90',
    'conventional_value_of_coulomb_90': 'conventional_value_of_coulomb_90',
    'conventional_value_of_farad_90': 'conventional_value_of_farad_90',
    'conventional_value_of_henry_90': 'conventional_value_of_henry_90',
    'conventional_value_of_josephson_constant': 'conventional_value_of_josephson_constant',
    'conventional_value_of_ohm_90': 'conventional_value_of_ohm_90',
    'conventional_value_of_volt_90': 'conventional_value_of_volt_90',
    'conventional_value_of_von_klitzing_constant': 'conventional_value_of_von_klitzing_constant',
    'conventional_value_of_watt_90': 'conventional_value_of_watt_90',
    'copper_x_unit': 'copper_x_unit',
    'cu_x_unit': 'cu_x_unit',
    'deuteron_electron_mag_mom_ratio': 'deuteron_electron_mag_mom_ratio',
    'deuteron_electron_magn_moment_ratio': 'deuteron_electron_magn_moment_ratio',
    'deuteron_electron_mass_ratio': 'deuteron_electron_mass_ratio',
    'deuteron_g_factor': 'deuteron_g_factor',
    'deuteron_mag_mom': 'deuteron_mag_mom',
    'deuteron_mag_mom_to_bohr_magneton_ratio': 'deuteron_mag_mom_to_bohr_magneton_ratio',
    'deuteron_mag_mom_to_nuclear_magneton_ratio': 'deuteron_mag_mom_to_nuclear_magneton_ratio',
    'deuteron_magn_moment': 'deuteron_magn_moment',
    'deuteron_magn_moment_to_bohr_magneton_ratio': 'deuteron_magn_moment_to_bohr_magneton_ratio',
    'deuteron_magn_moment_to_nuclear_magneton_ratio': 'deuteron_magn_moment_to_nuclear_magneton_ratio',
    'deuteron_mass': 'deuteron_mass',
    'deuteron_mass_energy_equivalent': 'deuteron_mass_energy_equivalent',
    'deuteron_mass_energy_equivalent_in_mev': 'deuteron_mass_energy_equivalent_in_mev',
    'deuteron_mass_in_u': 'deuteron_mass_in_u',
    'deuteron_molar_mass': 'deuteron_molar_mass',
    'deuteron_neutron_mag_mom_ratio': 'deuteron_neutron_mag_mom_ratio',
    'deuteron_neutron_magn_moment_ratio': 'deuteron_neutron_magn_moment_ratio',
    'deuteron_proton_mag_mom_ratio': 'deuteron_proton_mag_mom_ratio',
    'deuteron_proton_magn_moment_ratio': 'deuteron_proton_magn_moment_ratio',
    'deuteron_proton_mass_ratio': 'deuteron_proton_mass_ratio',
    'deuteron_relative_atomic_mass': 'deuteron_relative_atomic_mass',
    'deuteron_rms_charge_radius': 'deuteron_rms_charge_radius',
    'e': 'elementary_charge',
    'electric_constant': 'electric_constant',
    'electron_charge_to_mass_quotient': 'electron_charge_to_mass_quotient',
    'electron_deuteron_mag_mom_ratio': 'electron_deuteron_mag_mom_ratio',
    'electron_deuteron_magn_moment_ratio': 'electron_deuteron_magn_moment_ratio',
    'electron_deuteron_mass_ratio': 'electron_deuteron_mass_ratio',
    'electron_g_factor': 'electron_g_factor',
    'electron_gyromag_ratio': 'electron_gyromag_ratio',
    'electron_gyromag_ratio_in_mhz_t': 'electron_gyromag_ratio_in_mhz_t',
    'electron_gyromag_ratio_over_2_pi': 'electron_gyromag_ratio_over_2_pi',
    'electron_gyromagn_ratio': 'electron_gyromagn_ratio',
    'electron_gyromagn_ratio_over_2_pi': 'electron_gyromagn_ratio_over_2_pi',
    'electron_helion_mass_ratio': 'electron_helion_mass_ratio',
    'electron_mag_mom': 'electron_mag_mom',
    'electron_mag_mom_anomaly': 'electron_mag_mom_anomaly',
    'electron_mag_mom_to_bohr_magneton_ratio': 'electron_mag_mom_to_bohr_magneton_ratio',
    'electron_mag_mom_to_nuclear_magneton_ratio': 'electron_mag_mom_to_nuclear_magneton_ratio',
    'electron_magn_moment': 'electron_magn_moment',
    'electron_magn_moment_anomaly': 'electron_magn_moment_anomaly',
    'electron_magn_moment_to_bohr_magneton_ratio': 'electron_magn_moment_to_bohr_magneton_ratio',
    'electron_magn_moment_to_nuclear_magneton_ratio': 'electron_magn_moment_to_nuclear_magneton_ratio',
    'electron_mass': 'electron_mass',
    'electron_mass_energy_equivalent': 'electron_mass_energy_equivalent',
    'electron_mass_energy_equivalent_in_mev': 'electron_mass_energy_equivalent_in_mev',
    'electron_mass_in_u': 'electron_mass_in_u',
    'electron_molar_mass': 'electron_molar_mass',
    'electron_muon_mag_mom_ratio': 'electron_muon_mag_mom_ratio',
    'electron_muon_magn_moment_ratio': 'electron_muon_magn_moment_ratio',
    'electron_muon_mass_ratio': 'electron_muon_mass_ratio',
    'electron_neutron_mag_mom_ratio': 'electron_neutron_mag_mom_ratio',
    'electron_neutron_magn_moment_ratio': 'electron_neutron_magn_moment_ratio',
    'electron_neutron_mass_ratio': 'electron_neutron_mass_ratio',
    'electron_proton_mag_mom_ratio': 'electron_proton_mag_mom_ratio',
    'electron_proton_magn_moment_ratio': 'electron_proton_magn_moment_ratio',
    'electron_proton_mass_ratio': 'electron_proton_mass_ratio',
    'electron_relative_atomic_mass': 'electron_relative_atomic_mass',
    'electron_tau_mass_ratio': 'electron_tau_mass_ratio',
    'electron_to_alpha_particle_mass_ratio': 'electron_to_alpha_particle_mass_ratio',
    'electron_to_shielded_helion_mag_mom_ratio': 'electron_to_shielded_helion_mag_mom_ratio',
    'electron_to_shielded_helion_magn_moment_ratio': 'electron_to_shielded_helion_magn_moment_ratio',
    'electron_to_shielded_proton_mag_mom_ratio': 'electron_to_shielded_proton_mag_mom_ratio',
    'electron_to_shielded_proton_magn_moment_ratio': 'electron_to_shielded_proton_magn_moment_ratio',
    'electron_triton_mass_ratio': 'electron_triton_mass_ratio',
    'electron_volt': 'electron_volt',
    'electron_volt_atomic_mass_unit_relationship': 'electron_volt_atomic_mass_unit_relationship',
    'electron_volt_hartree_relationship': 'electron_volt_hartree_relationship',
    'electron_volt_hertz_relationship': 'electron_volt_hertz_relationship',
    'electron_volt_inverse_meter_relationship': 'electron_volt_inverse_meter_relationship',
    'electron_volt_joule_relationship': 'electron_volt_joule_relationship',
    'electron_volt_kelvin_relationship': 'electron_volt_kelvin_relationship',
    'electron_volt_kilogram_relationship': 'electron_volt_kilogram_relationship',
    'elementary_charge': 'elementary_charge',
    'elementary_charge_over_h': 'elementary_charge_over_h',
    'elementary_charge_over_h_bar': 'elementary_charge_over_h_bar',
    'f': 'faraday_constant',
    'faraday_constant': 'faraday_constant',
    'faraday_constant_for_conventional_electric_current': 'faraday_constant_for_conventional_electric_current',
    'fermi_coupling_constant': 'fermi_coupling_constant',
    'fine_structure_constant': 'fine_structure_constant',
    'first_radiation_constant': 'first_radiation_constant',
    'first_radiation_constant_for_spectral_radiance': 'first_radiation_constant_for_spectral_radiance',
    'h': 'planck_constant',
    'hartree_atomic_mass_unit_relationship': 'hartree_atomic_mass_unit_relationship',
    'hartree_electron_volt_relationship': 'hartree_electron_volt_relationship',
    'hartree_energy': 'hartree_energy',
    'hartree_energy_in_ev': 'hartree_energy_in_ev',
    'hartree_hertz_relationship': 'hartree_hertz_relationship',
    'hartree_inverse_meter_relationship': 'hartree_inverse_meter_relationship',
    'hartree_joule_relationship': 'hartree_joule_relationship',
    'hartree_kelvin_relationship': 'hartree_kelvin_relationship',
    'hartree_kilogram_relationship': 'hartree_kilogram_relationship',
    'hbar': 'reduced_planck_constant',
    'helion_electron_mass_ratio': 'helion_electron_mass_ratio',
    'helion_g_factor': 'helion_g_factor',
    'helion_mag_mom': 'helion_mag_mom',
    'helion_mag_mom_to_bohr_magneton_ratio': 'helion_mag_mom_to_bohr_magneton_ratio',
    'helion_mag_mom_to_nuclear_magneton_ratio': 'helion_mag_mom_to_nuclear_magneton_ratio',
    'helion_mass': 'helion_mass',
    'helion_mass_energy_equivalent': 'helion_mass_energy_equivalent',
    'helion_mass_energy_equivalent_in_mev': 'helion_mass_energy_equivalent_in_mev',
    'helion_mass_in_u': 'helion_mass_in_u',
    'helion_molar_mass': 'helion_molar_mass',
    'helion_proton_mass_ratio': 'helion_proton_mass_ratio',
    'helion_relative_atomic_mass': 'helion_relative_atomic_mass',
    'helion_shielding_shift': 'helion_shielding_shift',
    'hertz_atomic_mass_unit_relationship': 'hertz_atomic_mass_unit_relationship',
    'hertz_electron_volt_relationship': 'hertz_electron_volt_relationship',
    'hertz_hartree_relationship': 'hertz_hartree_relationship',
    'hertz_inverse_meter_relationship': 'hertz_inverse_meter_relationship',
    'hertz_joule_relationship': 'hertz_joule_relationship',
    'hertz_kelvin_relationship': 'hertz_kelvin_relationship',
    'hertz_kilogram_relationship': 'hertz_kilogram_relationship',
    'hyperfine_transition_frequency_of_cs_133': 'hyperfine_transition_frequency_of_cs_133',
    'inverse_fine_structure_constant': 'inverse_fine_structure_constant',
    'inverse_meter_atomic_mass_unit_relationship': 'inverse_meter_atomic_mass_unit_relationship',
    'inverse_meter_electron_volt_relationship': 'inverse_meter_electron_volt_relationship',
    'inverse_meter_hartree_relationship': 'inverse_meter_hartree_relationship',
    'inverse_meter_hertz_relationship': 'inverse_meter_hertz_relationship',
    'inverse_meter_joule_relationship': 'inverse_meter_joule_relationship',
    'inverse_meter_kelvin_relationship': 'inverse_meter_kelvin_relationship',
    'inverse_meter_kilogram_relationship': 'inverse_meter_kilogram_relationship',
    'inverse_of_conductance_quantum': 'inverse_of_conductance_quantum',
    'josephson_constant': 'josephson_constant',
    'joule_atomic_mass_unit_relationship': 'joule_atomic_mass_unit_relationship',
    'joule_electron_volt_relationship': 'joule_electron_volt_relationship',
    'joule_hartree_relationship': 'joule_hartree_relationship',
    'joule_hertz_relationship': 'joule_hertz_relationship',
    'joule_inverse_meter_relationship': 'joule_inverse_meter_relationship',
    'joule_kelvin_relationship': 'joule_kelvin_relationship',
    'joule_kilogram_relationship': 'joule_kilogram_relationship',
    'k_b': 'boltzmann_constant',
    'kelvin_atomic_mass_unit_relationship': 'kelvin_atomic_mass_unit_relationship',
    'kelvin_electron_volt_relationship': 'kelvin_electron_volt_relationship',
    'kelvin_hartree_relationship': 'kelvin_hartree_relationship',
    'kelvin_hertz_relationship': 'kelvin_hertz_relationship',
    'kelvin_inverse_meter_relationship': 'kelvin_inverse_meter_relationship',
    'kelvin_joule_relationship': 'kelvin_joule_relationship',
    'kelvin_kilogram_relationship': 'kelvin_kilogram_relationship',
    'kilogram_atomic_mass_unit_relationship': 'kilogram_atomic_mass_unit_relationship',
    'kilogram_electron_volt_relationship': 'kilogram_electron_volt_relationship',
    'kilogram_hartree_relationship': 'kilogram_hartree_relationship',
    'kilogram_hertz_relationship': 'kilogram_hertz_relationship',
    'kilogram_inverse_meter_relationship': 'kilogram_inverse_meter_relationship',
    'kilogram_joule_relationship': 'kilogram_joule_relationship',
    'kilogram_kelvin_relationship': 'kilogram_kelvin_relationship',
    'lattice_parameter_of_silicon': 'lattice_parameter_of_silicon',
    'lattice_spacing_of_ideal_si_220': 'lattice_spacing_of_ideal_si_220',
    'lattice_spacing_of_silicon': 'lattice_spacing_of_silicon',
    'loschmidt_constant_273_15_k_100_kpa': 'loschmidt_constant_273_15_k_100_kpa',
    'loschmidt_constant_273_15_k_101_325_kpa': 'loschmidt_constant_273_15_k_101_325_kpa',
    'luminous_efficacy': 'luminous_efficacy',
    'mag_constant': 'mag_constant',
    'mag_flux_quantum': 'mag_flux_quantum',
    'magn_constant': 'magn_constant',
    'magn_flux_quantum': 'magn_flux_quantum',
    'mo_x_unit': 'mo_x_unit',
    'molar_gas_constant': 'molar_gas_constant',
    'molar_mass_constant': 'molar_mass_constant',
    'molar_mass_of_carbon_12': 'molar_mass_of_carbon_12',
    'molar_planck_constant': 'molar_planck_constant',
    'molar_planck_constant_times_c': 'molar_planck_constant_times_c',
    'molar_volume_of_ideal_gas_273_15_k_100_kpa': 'molar_volume_of_ideal_gas_273_15_k_100_kpa',
    'molar_volume_of_ideal_gas_273_15_k_101_325_kpa': 'molar_volume_of_ideal_gas_273_15_k_101_325_kpa',
    'molar_volume_of_silicon': 'molar_volume_of_silicon',
    'molybdenum_x_unit': 'molybdenum_x_unit',
    'muon_compton_wavelength': 'muon_compton_wavelength',
    'muon_compton_wavelength_over_2_pi': 'muon_compton_wavelength_over_2_pi',
    'muon_electron_mass_ratio': 'muon_electron_mass_ratio',
    'muon_g_factor': 'muon_g_factor',
    'muon_mag_mom': 'muon_mag_mom',
    'muon_mag_mom_anomaly': 'muon_mag_mom_anomaly',
    'muon_mag_mom_to_bohr_magneton_ratio': 'muon_mag_mom_to_bohr_magneton_ratio',
    'muon_mag_mom_to_nuclear_magneton_ratio': 'muon_mag_mom_to_nuclear_magneton_ratio',
    'muon_magn_moment': 'muon_magn_moment',
    'muon_magn_moment_to_bohr_magneton_ratio': 'muon_magn_moment_to_bohr_magneton_ratio',
    'muon_magn_moment_to_nuclear_magneton_ratio': 'muon_magn_moment_to_nuclear_magneton_ratio',
    'muon_mass': 'muon_mass',
    'muon_mass_energy_equivalent': 'muon_mass_energy_equivalent',
    'muon_mass_energy_equivalent_in_mev': 'muon_mass_energy_equivalent_in_mev',
    'muon_mass_in_u': 'muon_mass_in_u',
    'muon_molar_mass': 'muon_molar_mass',
    'muon_neutron_mass_ratio': 'muon_neutron_mass_ratio',
    'muon_proton_mag_mom_ratio': 'muon_proton_mag_mom_ratio',
    'muon_proton_magn_moment_ratio': 'muon_proton_magn_moment_ratio',
    'muon_proton_mass_ratio': 'muon_proton_mass_ratio',
    'muon_tau_mass_ratio': 'muon_tau_mass_ratio',
    'n_a': 'avogadro_constant',
    'natural_unit_of_action': 'natural_unit_of_action',
    'natural_unit_of_action_in_ev_s': 'natural_unit_of_action_in_ev_s',
    'natural_unit_of_energy': 'natural_unit_of_energy',
    'natural_unit_of_energy_in_mev': 'natural_unit_of_energy_in_mev',
    'natural_unit_of_length': 'natural_unit_of_length',
    'natural_unit_of_mass': 'natural_unit_of_mass',
    'natural_unit_of_mom_um': 'natural_unit_of_mom_um',
    'natural_unit_of_mom_um_in_mev_c': 'natural_unit_of_mom_um_in_mev_c',
    'natural_unit_of_momentum': 'natural_unit_of_momentum',
    'natural_unit_of_momentum_in_mev_c': 'natural_unit_of_momentum_in_mev_c',
    'natural_unit_of_time': 'natural_unit_of_time',
    'natural_unit_of_velocity': 'natural_unit_of_velocity',
    'neutron_compton_wavelength': 'neutron_compton_wavelength',
    'neutron_compton_wavelength_over_2_pi': 'neutron_compton_wavelength_over_2_pi',
    'neutron_electron_mag_mom_ratio': 'neutron_electron_mag_mom_ratio',
    'neutron_electron_magn_moment_ratio': 'neutron_electron_magn_moment_ratio',
    'neutron_electron_mass_ratio': 'neutron_electron_mass_ratio',
    'neutron_g_factor': 'neutron_g_factor',
    'neutron_gyromag_ratio': 'neutron_gyromag_ratio',
    'neutron_gyromag_ratio_in_mhz_t': 'neutron_gyromag_ratio_in_mhz_t',
    'neutron_gyromag_ratio_over_2_pi': 'neutron_gyromag_ratio_over_2_pi',
    'neutron_gyromagn_ratio': 'neutron_gyromagn_ratio',
    'neutron_gyromagn_ratio_over_2_pi': 'neutron_gyromagn_ratio_over_2_pi',
    'neutron_mag_mom': 'neutron_mag_mom',
    'neutron_mag_mom_to_bohr_magneton_ratio': 'neutron_mag_mom_to_bohr_magneton_ratio',
    'neutron_mag_mom_to_nuclear_magneton_ratio': 'neutron_mag_mom_to_nuclear_magneton_ratio',
    'neutron_magn_moment': 'neutron_magn_moment',
    'neutron_magn_moment_to_bohr_magneton_ratio': 'neutron_magn_moment_to_bohr_magneton_ratio',
    'neutron_magn_moment_to_nuclear_magneton_ratio': 'neutron_magn_moment_to_nuclear_magneton_ratio',
    'neutron_mass': 'neutron_mass',
    'neutron_mass_energy_equivalent': 'neutron_mass_energy_equivalent',
    'neutron_mass_energy_equivalent_in_mev': 'neutron_mass_energy_equivalent_in_mev',
    'neutron_mass_in_u': 'neutron_mass_in_u',
    'neutron_molar_mass': 'neutron_molar_mass',
    'neutron_muon_mass_ratio': 'neutron_muon_mass_ratio',
    'neutron_proton_mag_mom_ratio': 'neutron_proton_mag_mom_ratio',
    'neutron_proton_magn_moment_ratio': 'neutron_proton_magn_moment_ratio',
    'neutron_proton_mass_difference': 'neutron_proton_mass_difference',
    'neutron_proton_mass_difference_energy_equivalent': 'neutron_proton_mass_difference_energy_equivalent',
    'neutron_proton_mass_difference_energy_equivalent_in_mev': 'neutron_proton_mass_difference_energy_equivalent_in_mev',
    'neutron_proton_mass_difference_in_u': 'neutron_proton_mass_difference_in_u',
    'neutron_proton_mass_ratio': 'neutron_proton_mass_ratio',
    'neutron_relative_atomic_mass': 'neutron_relative_atomic_mass',
    'neutron_tau_mass_ratio': 'neutron_tau_mass_ratio',
    'neutron_to_shielded_proton_mag_mom_ratio': 'neutron_to_shielded_proton_mag_mom_ratio',
    'neutron_to_shielded_proton_magn_moment_ratio': 'neutron_to_shielded_proton_magn_moment_ratio',
    'newtonian_constant_of_gravitation': 'newtonian_constant_of_gravitation',
    'newtonian_constant_of_gravitation_over_h_bar_c': 'newtonian_constant_of_gravitation_over_h_bar_c',
    'nuclear_magneton': 'nuclear_magneton',
    'nuclear_magneton_in_ev_t': 'nuclear_magneton_in_ev_t',
    'nuclear_magneton_in_inverse_meter_per_tesla': 'nuclear_magneton_in_inverse_meter_per_tesla',
    'nuclear_magneton_in_inverse_meters_per_tesla': 'nuclear_magneton_in_inverse_meters_per_tesla',
    'nuclear_magneton_in_k_t': 'nuclear_magneton_in_k_t',
    'nuclear_magneton_in_mhz_t': 'nuclear_magneton_in_mhz_t',
    'planck': 'planck_constant',
    'planck_constant': 'planck_constant',
    'planck_constant_in_ev_hz': 'planck_constant_in_ev_hz',
    'planck_constant_in_ev_s': 'planck_constant_in_ev_s',
    'planck_constant_over_2_pi': 'planck_constant_over_2_pi',
    'planck_constant_over_2_pi_in_ev_s': 'planck_constant_over_2_pi_in_ev_s',
    'planck_constant_over_2_pi_times_c_in_mev_fm': 'planck_constant_over_2_pi_times_c_in_mev_fm',
    'planck_length': 'planck_length',
    'planck_mass': 'planck_mass',
    'planck_mass_energy_equivalent_in_gev': 'planck_mass_energy_equivalent_in_gev',
    'planck_temperature': 'planck_temperature',
    'planck_time': 'planck_time',
    'proton_charge_to_mass_quotient': 'proton_charge_to_mass_quotient',
    'proton_compton_wavelength': 'proton_compton_wavelength',
    'proton_compton_wavelength_over_2_pi': 'proton_compton_wavelength_over_2_pi',
    'proton_electron_mass_ratio': 'proton_electron_mass_ratio',
    'proton_g_factor': 'proton_g_factor',
    'proton_gyromag_ratio': 'proton_gyromag_ratio',
    'proton_gyromag_ratio_in_mhz_t': 'proton_gyromag_ratio_in_mhz_t',
    'proton_gyromag_ratio_over_2_pi': 'proton_gyromag_ratio_over_2_pi',
    'proton_gyromagn_ratio': 'proton_gyromagn_ratio',
    'proton_gyromagn_ratio_over_2_pi': 'proton_gyromagn_ratio_over_2_pi',
    'proton_mag_mom': 'proton_mag_mom',
    'proton_mag_mom_to_bohr_magneton_ratio': 'proton_mag_mom_to_bohr_magneton_ratio',
    'proton_mag_mom_to_nuclear_magneton_ratio': 'proton_mag_mom_to_nuclear_magneton_ratio',
    'proton_mag_shielding_correction': 'proton_mag_shielding_correction',
    'proton_magn_moment': 'proton_magn_moment',
    'proton_magn_moment_to_bohr_magneton_ratio': 'proton_magn_moment_to_bohr_magneton_ratio',
    'proton_magn_moment_to_nuclear_magneton_ratio': 'proton_magn_moment_to_nuclear_magneton_ratio',
    'proton_magn_shielding_correction': 'proton_magn_shielding_correction',
    'proton_mass': 'proton_mass',
    'proton_mass_energy_equivalent': 'proton_mass_energy_equivalent',
    'proton_mass_energy_equivalent_in_mev': 'proton_mass_energy_equivalent_in_mev',
    'proton_mass_in_u': 'proton_mass_in_u',
    'proton_molar_mass': 'proton_molar_mass',
    'proton_muon_mass_ratio': 'proton_muon_mass_ratio',
    'proton_neutron_mag_mom_ratio': 'proton_neutron_mag_mom_ratio',
    'proton_neutron_magn_moment_ratio': 'proton_neutron_magn_moment_ratio',
    'proton_neutron_mass_ratio': 'proton_neutron_mass_ratio',
    'proton_relative_atomic_mass': 'proton_relative_atomic_mass',
    'proton_rms_charge_radius': 'proton_rms_charge_radius',
    'proton_tau_mass_ratio': 'proton_tau_mass_ratio',
    'quantum_of_circulation': 'quantum_of_circulation',
    'quantum_of_circulation_times_2': 'quantum_of_circulation_times_2',
    'r': 'molar_gas_constant',
    'reduced_compton_wavelength': 'reduced_compton_wavelength',
    'reduced_muon_compton_wavelength': 'reduced_muon_compton_wavelength',
    'reduced_neutron_compton_wavelength': 'reduced_neutron_compton_wavelength',
    'reduced_planck_constant': 'reduced_planck_constant',
    'reduced_planck_constant_in_ev_s': 'reduced_planck_constant_in_ev_s',
    'reduced_planck_constant_times_c_in_mev_fm': 'reduced_planck_constant_times_c_in_mev_fm',
    'reduced_proton_compton_wavelength': 'reduced_proton_compton_wavelength',
    'reduced_tau_compton_wavelength': 'reduced_tau_compton_wavelength',
    'rydberg_constant': 'rydberg_constant',
    'rydberg_constant_times_c_in_hz': 'rydberg_constant_times_c_in_hz',
    'rydberg_constant_times_hc_in_ev': 'rydberg_constant_times_hc_in_ev',
    'rydberg_constant_times_hc_in_j': 'rydberg_constant_times_hc_in_j',
    'sackur_tetrode_constant_1_k_100_kpa': 'sackur_tetrode_constant_1_k_100_kpa',
    'sackur_tetrode_constant_1_k_101_325_kpa': 'sackur_tetrode_constant_1_k_101_325_kpa',
    'second_radiation_constant': 'second_radiation_constant',
    'shielded_helion_gyromag_ratio': 'shielded_helion_gyromag_ratio',
    'shielded_helion_gyromag_ratio_in_mhz_t': 'shielded_helion_gyromag_ratio_in_mhz_t',
    'shielded_helion_gyromag_ratio_over_2_pi': 'shielded_helion_gyromag_ratio_over_2_pi',
    'shielded_helion_gyromagn_ratio': 'shielded_helion_gyromagn_ratio',
    'shielded_helion_gyromagn_ratio_over_2_pi': 'shielded_helion_gyromagn_ratio_over_2_pi',
    'shielded_helion_mag_mom': 'shielded_helion_mag_mom',
    'shielded_helion_mag_mom_to_bohr_magneton_ratio': 'shielded_helion_mag_mom_to_bohr_magneton_ratio',
    'shielded_helion_mag_mom_to_nuclear_magneton_ratio': 'shielded_helion_mag_mom_to_nuclear_magneton_ratio',
    'shielded_helion_magn_moment': 'shielded_helion_magn_moment',
    'shielded_helion_magn_moment_to_bohr_magneton_ratio': 'shielded_helion_magn_moment_to_bohr_magneton_ratio',
    'shielded_helion_magn_moment_to_nuclear_magneton_ratio': 'shielded_helion_magn_moment_to_nuclear_magneton_ratio',
    'shielded_helion_to_proton_mag_mom_ratio': 'shielded_helion_to_proton_mag_mom_ratio',
    'shielded_helion_to_proton_magn_moment_ratio': 'shielded_helion_to_proton_magn_moment_ratio',
    'shielded_helion_to_shielded_proton_mag_mom_ratio': 'shielded_helion_to_shielded_proton_mag_mom_ratio',
    'shielded_helion_to_shielded_proton_magn_moment_ratio': 'shielded_helion_to_shielded_proton_magn_moment_ratio',
    'shielded_proton_gyromag_ratio': 'shielded_proton_gyromag_ratio',
    'shielded_proton_gyromag_ratio_in_mhz_t': 'shielded_proton_gyromag_ratio_in_mhz_t',
    'shielded_proton_gyromag_ratio_over_2_pi': 'shielded_proton_gyromag_ratio_over_2_pi',
    'shielded_proton_mag_mom': 'shielded_proton_mag_mom',
    'shielded_proton_mag_mom_to_bohr_magneton_ratio': 'shielded_proton_mag_mom_to_bohr_magneton_ratio',
    'shielded_proton_mag_mom_to_nuclear_magneton_ratio': 'shielded_proton_mag_mom_to_nuclear_magneton_ratio',
    'shielded_proton_magn_moment': 'shielded_proton_magn_moment',
    'shielded_proton_magn_moment_to_bohr_magneton_ratio': 'shielded_proton_magn_moment_to_bohr_magneton_ratio',
    'shielded_proton_magn_moment_to_nuclear_magneton_ratio': 'shielded_proton_magn_moment_to_nuclear_magneton_ratio',
    'shielding_difference_of_d_and_p_in_hd': 'shielding_difference_of_d_and_p_in_hd',
    'shielding_difference_of_t_and_p_in_ht': 'shielding_difference_of_t_and_p_in_ht',
    'speed_of_light': 'speed_of_light_in_vacuum',
    'speed_of_light_in_vacuum': 'speed_of_light_in_vacuum',
    'standard_acceleration_of_gravity': 'standard_acceleration_of_gravity',
    'standard_atmosphere': 'standard_atmosphere',
    'standard_state_pressure': 'standard_state_pressure',
    'stefan_boltzmann_constant': 'stefan_boltzmann_constant',
    'tau_compton_wavelength': 'tau_compton_wavelength',
    'tau_compton_wavelength_over_2_pi': 'tau_compton_wavelength_over_2_pi',
    'tau_electron_mass_ratio': 'tau_electron_mass_ratio',
    'tau_energy_equivalent': 'tau_energy_equivalent',
    'tau_mass': 'tau_mass',
    'tau_mass_energy_equivalent': 'tau_mass_energy_equivalent',
    'tau_mass_energy_equivalent_in_mev': 'tau_mass_energy_equivalent_in_mev',
    'tau_mass_in_u': 'tau_mass_in_u',
    'tau_molar_mass': 'tau_molar_mass',
    'tau_muon_mass_ratio': 'tau_muon_mass_ratio',
    'tau_neutron_mass_ratio': 'tau_neutron_mass_ratio',
    'tau_proton_mass_ratio': 'tau_proton_mass_ratio',
    'thomson_cross_section': 'thomson_cross_section',
    'triton_electron_mag_mom_ratio': 'triton_electron_mag_mom_ratio',
    'triton_electron_mass_ratio': 'triton_electron_mass_ratio',
    'triton_g_factor': 'triton_g_factor',
    'triton_mag_mom': 'triton_mag_mom',
    'triton_mag_mom_to_bohr_magneton_ratio': 'triton_mag_mom_to_bohr_magneton_ratio',
    'triton_mag_mom_to_nuclear_magneton_ratio': 'triton_mag_mom_to_nuclear_magneton_ratio',
    'triton_mass': 'triton_mass',
    'triton_mass_energy_equivalent': 'triton_mass_energy_equivalent',
    'triton_mass_energy_equivalent_in_mev': 'triton_mass_energy_equivalent_in_mev',
    'triton_mass_in_u': 'triton_mass_in_u',
    'triton_molar_mass': 'triton_molar_mass',
    'triton_neutron_mag_mom_ratio': 'triton_neutron_mag_mom_ratio',
    'triton_proton_mag_mom_ratio': 'triton_proton_mag_mom_ratio',
    'triton_proton_mass_ratio': 'triton_proton_mass_ratio',
    'triton_relative_atomic_mass': 'triton_relative_atomic_mass',
    'triton_to_proton_mag_mom_ratio': 'triton_to_proton_mag_mom_ratio',
    'unified_atomic_mass_unit': 'unified_atomic_mass_unit',
    'vacuum_electric_permittivity': 'vacuum_electric_permittivity',
    'vacuum_mag_permeability': 'vacuum_mag_permeability',
    'von_klitzing_constant': 'von_klitzing_constant',
    'w_to_z_mass_ratio': 'w_to_z_mass_ratio',
    'weak_mixing_angle': 'weak_mixing_angle',
    'wien_displacement_law_constant': 'wien_displacement_law_constant',
    'wien_frequency_displacement_law_constant': 'wien_frequency_displacement_law_constant',
    'wien_wavelength_displacement_law_constant': 'wien_wavelength_displacement_law_constant',
}

angstrom_star = PHYSICAL_CONSTANTS['angstrom_star'].value
avogadro_constant = PHYSICAL_CONSTANTS['avogadro_constant'].value
bohr_magneton = PHYSICAL_CONSTANTS['bohr_magneton'].value
bohr_magneton_in_hz_t = PHYSICAL_CONSTANTS['bohr_magneton_in_hz_t'].value
bohr_magneton_in_k_t = PHYSICAL_CONSTANTS['bohr_magneton_in_k_t'].value
bohr_magneton_in_ev_t = PHYSICAL_CONSTANTS['bohr_magneton_in_ev_t'].value
bohr_magneton_in_inverse_meter_per_tesla = PHYSICAL_CONSTANTS['bohr_magneton_in_inverse_meter_per_tesla'].value
bohr_magneton_in_inverse_meters_per_tesla = PHYSICAL_CONSTANTS['bohr_magneton_in_inverse_meters_per_tesla'].value
bohr_radius = PHYSICAL_CONSTANTS['bohr_radius'].value
boltzmann_constant = PHYSICAL_CONSTANTS['boltzmann_constant'].value
boltzmann_constant_in_hz_k = PHYSICAL_CONSTANTS['boltzmann_constant_in_hz_k'].value
boltzmann_constant_in_ev_k = PHYSICAL_CONSTANTS['boltzmann_constant_in_ev_k'].value
boltzmann_constant_in_inverse_meter_per_kelvin = PHYSICAL_CONSTANTS['boltzmann_constant_in_inverse_meter_per_kelvin'].value
boltzmann_constant_in_inverse_meters_per_kelvin = PHYSICAL_CONSTANTS['boltzmann_constant_in_inverse_meters_per_kelvin'].value
compton_wavelength = PHYSICAL_CONSTANTS['compton_wavelength'].value
compton_wavelength_over_2_pi = PHYSICAL_CONSTANTS['compton_wavelength_over_2_pi'].value
copper_x_unit = PHYSICAL_CONSTANTS['copper_x_unit'].value
cu_x_unit = PHYSICAL_CONSTANTS['cu_x_unit'].value
faraday_constant = PHYSICAL_CONSTANTS['faraday_constant'].value
faraday_constant_for_conventional_electric_current = PHYSICAL_CONSTANTS['faraday_constant_for_conventional_electric_current'].value
fermi_coupling_constant = PHYSICAL_CONSTANTS['fermi_coupling_constant'].value
hartree_energy = PHYSICAL_CONSTANTS['hartree_energy'].value
hartree_energy_in_ev = PHYSICAL_CONSTANTS['hartree_energy_in_ev'].value
josephson_constant = PHYSICAL_CONSTANTS['josephson_constant'].value
loschmidt_constant_273_15_k_100_kpa = PHYSICAL_CONSTANTS['loschmidt_constant_273_15_k_100_kpa'].value
loschmidt_constant_273_15_k_101_325_kpa = PHYSICAL_CONSTANTS['loschmidt_constant_273_15_k_101_325_kpa'].value
mo_x_unit = PHYSICAL_CONSTANTS['mo_x_unit'].value
molybdenum_x_unit = PHYSICAL_CONSTANTS['molybdenum_x_unit'].value
newtonian_constant_of_gravitation = PHYSICAL_CONSTANTS['newtonian_constant_of_gravitation'].value
newtonian_constant_of_gravitation_over_h_bar_c = PHYSICAL_CONSTANTS['newtonian_constant_of_gravitation_over_h_bar_c'].value
planck_constant = PHYSICAL_CONSTANTS['planck_constant'].value
planck_constant_in_ev_s = PHYSICAL_CONSTANTS['planck_constant_in_ev_s'].value
planck_constant_in_ev_hz = PHYSICAL_CONSTANTS['planck_constant_in_ev_hz'].value
planck_constant_over_2_pi = PHYSICAL_CONSTANTS['planck_constant_over_2_pi'].value
planck_constant_over_2_pi_in_ev_s = PHYSICAL_CONSTANTS['planck_constant_over_2_pi_in_ev_s'].value
planck_constant_over_2_pi_times_c_in_mev_fm = PHYSICAL_CONSTANTS['planck_constant_over_2_pi_times_c_in_mev_fm'].value
planck_length = PHYSICAL_CONSTANTS['planck_length'].value
planck_mass = PHYSICAL_CONSTANTS['planck_mass'].value
planck_mass_energy_equivalent_in_gev = PHYSICAL_CONSTANTS['planck_mass_energy_equivalent_in_gev'].value
planck_temperature = PHYSICAL_CONSTANTS['planck_temperature'].value
planck_time = PHYSICAL_CONSTANTS['planck_time'].value
rydberg_constant = PHYSICAL_CONSTANTS['rydberg_constant'].value
rydberg_constant_times_c_in_hz = PHYSICAL_CONSTANTS['rydberg_constant_times_c_in_hz'].value
rydberg_constant_times_hc_in_j = PHYSICAL_CONSTANTS['rydberg_constant_times_hc_in_j'].value
rydberg_constant_times_hc_in_ev = PHYSICAL_CONSTANTS['rydberg_constant_times_hc_in_ev'].value
sackur_tetrode_constant_1_k_100_kpa = PHYSICAL_CONSTANTS['sackur_tetrode_constant_1_k_100_kpa'].value
sackur_tetrode_constant_1_k_101_325_kpa = PHYSICAL_CONSTANTS['sackur_tetrode_constant_1_k_101_325_kpa'].value
stefan_boltzmann_constant = PHYSICAL_CONSTANTS['stefan_boltzmann_constant'].value
thomson_cross_section = PHYSICAL_CONSTANTS['thomson_cross_section'].value
w_to_z_mass_ratio = PHYSICAL_CONSTANTS['w_to_z_mass_ratio'].value
wien_displacement_law_constant = PHYSICAL_CONSTANTS['wien_displacement_law_constant'].value
wien_frequency_displacement_law_constant = PHYSICAL_CONSTANTS['wien_frequency_displacement_law_constant'].value
wien_wavelength_displacement_law_constant = PHYSICAL_CONSTANTS['wien_wavelength_displacement_law_constant'].value
alpha_particle_mass = PHYSICAL_CONSTANTS['alpha_particle_mass'].value
alpha_particle_mass_energy_equivalent = PHYSICAL_CONSTANTS['alpha_particle_mass_energy_equivalent'].value
alpha_particle_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['alpha_particle_mass_energy_equivalent_in_mev'].value
alpha_particle_mass_in_u = PHYSICAL_CONSTANTS['alpha_particle_mass_in_u'].value
alpha_particle_molar_mass = PHYSICAL_CONSTANTS['alpha_particle_molar_mass'].value
alpha_particle_relative_atomic_mass = PHYSICAL_CONSTANTS['alpha_particle_relative_atomic_mass'].value
alpha_particle_rms_charge_radius = PHYSICAL_CONSTANTS['alpha_particle_rms_charge_radius'].value
alpha_particle_electron_mass_ratio = PHYSICAL_CONSTANTS['alpha_particle_electron_mass_ratio'].value
alpha_particle_proton_mass_ratio = PHYSICAL_CONSTANTS['alpha_particle_proton_mass_ratio'].value
atomic_mass_constant = PHYSICAL_CONSTANTS['atomic_mass_constant'].value
atomic_mass_constant_energy_equivalent = PHYSICAL_CONSTANTS['atomic_mass_constant_energy_equivalent'].value
atomic_mass_constant_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['atomic_mass_constant_energy_equivalent_in_mev'].value
atomic_mass_unit_electron_volt_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_electron_volt_relationship'].value
atomic_mass_unit_hartree_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_hartree_relationship'].value
atomic_mass_unit_hertz_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_hertz_relationship'].value
atomic_mass_unit_inverse_meter_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_inverse_meter_relationship'].value
atomic_mass_unit_joule_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_joule_relationship'].value
atomic_mass_unit_kelvin_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_kelvin_relationship'].value
atomic_mass_unit_kilogram_relationship = PHYSICAL_CONSTANTS['atomic_mass_unit_kilogram_relationship'].value
atomic_unit_of_1st_hyperpolarizability = PHYSICAL_CONSTANTS['atomic_unit_of_1st_hyperpolarizability'].value
atomic_unit_of_1st_hyperpolarizablity = PHYSICAL_CONSTANTS['atomic_unit_of_1st_hyperpolarizablity'].value
atomic_unit_of_2nd_hyperpolarizability = PHYSICAL_CONSTANTS['atomic_unit_of_2nd_hyperpolarizability'].value
atomic_unit_of_2nd_hyperpolarizablity = PHYSICAL_CONSTANTS['atomic_unit_of_2nd_hyperpolarizablity'].value
atomic_unit_of_action = PHYSICAL_CONSTANTS['atomic_unit_of_action'].value
atomic_unit_of_charge = PHYSICAL_CONSTANTS['atomic_unit_of_charge'].value
atomic_unit_of_charge_density = PHYSICAL_CONSTANTS['atomic_unit_of_charge_density'].value
atomic_unit_of_current = PHYSICAL_CONSTANTS['atomic_unit_of_current'].value
atomic_unit_of_electric_dipole_mom = PHYSICAL_CONSTANTS['atomic_unit_of_electric_dipole_mom'].value
atomic_unit_of_electric_dipole_moment = PHYSICAL_CONSTANTS['atomic_unit_of_electric_dipole_moment'].value
atomic_unit_of_electric_field = PHYSICAL_CONSTANTS['atomic_unit_of_electric_field'].value
atomic_unit_of_electric_field_gradient = PHYSICAL_CONSTANTS['atomic_unit_of_electric_field_gradient'].value
atomic_unit_of_electric_polarizability = PHYSICAL_CONSTANTS['atomic_unit_of_electric_polarizability'].value
atomic_unit_of_electric_polarizablity = PHYSICAL_CONSTANTS['atomic_unit_of_electric_polarizablity'].value
atomic_unit_of_electric_potential = PHYSICAL_CONSTANTS['atomic_unit_of_electric_potential'].value
atomic_unit_of_electric_quadrupole_mom = PHYSICAL_CONSTANTS['atomic_unit_of_electric_quadrupole_mom'].value
atomic_unit_of_electric_quadrupole_moment = PHYSICAL_CONSTANTS['atomic_unit_of_electric_quadrupole_moment'].value
atomic_unit_of_energy = PHYSICAL_CONSTANTS['atomic_unit_of_energy'].value
atomic_unit_of_force = PHYSICAL_CONSTANTS['atomic_unit_of_force'].value
atomic_unit_of_length = PHYSICAL_CONSTANTS['atomic_unit_of_length'].value
atomic_unit_of_mag_dipole_mom = PHYSICAL_CONSTANTS['atomic_unit_of_mag_dipole_mom'].value
atomic_unit_of_mag_flux_density = PHYSICAL_CONSTANTS['atomic_unit_of_mag_flux_density'].value
atomic_unit_of_magn_dipole_moment = PHYSICAL_CONSTANTS['atomic_unit_of_magn_dipole_moment'].value
atomic_unit_of_magn_flux_density = PHYSICAL_CONSTANTS['atomic_unit_of_magn_flux_density'].value
atomic_unit_of_magnetizability = PHYSICAL_CONSTANTS['atomic_unit_of_magnetizability'].value
atomic_unit_of_mass = PHYSICAL_CONSTANTS['atomic_unit_of_mass'].value
atomic_unit_of_mom_um = PHYSICAL_CONSTANTS['atomic_unit_of_mom_um'].value
atomic_unit_of_momentum = PHYSICAL_CONSTANTS['atomic_unit_of_momentum'].value
atomic_unit_of_permittivity = PHYSICAL_CONSTANTS['atomic_unit_of_permittivity'].value
atomic_unit_of_time = PHYSICAL_CONSTANTS['atomic_unit_of_time'].value
atomic_unit_of_velocity = PHYSICAL_CONSTANTS['atomic_unit_of_velocity'].value
characteristic_impedance_of_vacuum = PHYSICAL_CONSTANTS['characteristic_impedance_of_vacuum'].value
classical_electron_radius = PHYSICAL_CONSTANTS['classical_electron_radius'].value
conductance_quantum = PHYSICAL_CONSTANTS['conductance_quantum'].value
conventional_value_of_josephson_constant = PHYSICAL_CONSTANTS['conventional_value_of_josephson_constant'].value
conventional_value_of_ampere_90 = PHYSICAL_CONSTANTS['conventional_value_of_ampere_90'].value
conventional_value_of_coulomb_90 = PHYSICAL_CONSTANTS['conventional_value_of_coulomb_90'].value
conventional_value_of_farad_90 = PHYSICAL_CONSTANTS['conventional_value_of_farad_90'].value
conventional_value_of_henry_90 = PHYSICAL_CONSTANTS['conventional_value_of_henry_90'].value
conventional_value_of_ohm_90 = PHYSICAL_CONSTANTS['conventional_value_of_ohm_90'].value
conventional_value_of_volt_90 = PHYSICAL_CONSTANTS['conventional_value_of_volt_90'].value
conventional_value_of_von_klitzing_constant = PHYSICAL_CONSTANTS['conventional_value_of_von_klitzing_constant'].value
conventional_value_of_watt_90 = PHYSICAL_CONSTANTS['conventional_value_of_watt_90'].value
deuteron_g_factor = PHYSICAL_CONSTANTS['deuteron_g_factor'].value
deuteron_mag_mom = PHYSICAL_CONSTANTS['deuteron_mag_mom'].value
deuteron_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['deuteron_mag_mom_to_bohr_magneton_ratio'].value
deuteron_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['deuteron_mag_mom_to_nuclear_magneton_ratio'].value
deuteron_magn_moment = PHYSICAL_CONSTANTS['deuteron_magn_moment'].value
deuteron_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['deuteron_magn_moment_to_bohr_magneton_ratio'].value
deuteron_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['deuteron_magn_moment_to_nuclear_magneton_ratio'].value
deuteron_mass = PHYSICAL_CONSTANTS['deuteron_mass'].value
deuteron_mass_energy_equivalent = PHYSICAL_CONSTANTS['deuteron_mass_energy_equivalent'].value
deuteron_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['deuteron_mass_energy_equivalent_in_mev'].value
deuteron_mass_in_u = PHYSICAL_CONSTANTS['deuteron_mass_in_u'].value
deuteron_molar_mass = PHYSICAL_CONSTANTS['deuteron_molar_mass'].value
deuteron_relative_atomic_mass = PHYSICAL_CONSTANTS['deuteron_relative_atomic_mass'].value
deuteron_rms_charge_radius = PHYSICAL_CONSTANTS['deuteron_rms_charge_radius'].value
deuteron_electron_mag_mom_ratio = PHYSICAL_CONSTANTS['deuteron_electron_mag_mom_ratio'].value
deuteron_electron_magn_moment_ratio = PHYSICAL_CONSTANTS['deuteron_electron_magn_moment_ratio'].value
deuteron_electron_mass_ratio = PHYSICAL_CONSTANTS['deuteron_electron_mass_ratio'].value
deuteron_neutron_mag_mom_ratio = PHYSICAL_CONSTANTS['deuteron_neutron_mag_mom_ratio'].value
deuteron_neutron_magn_moment_ratio = PHYSICAL_CONSTANTS['deuteron_neutron_magn_moment_ratio'].value
deuteron_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['deuteron_proton_mag_mom_ratio'].value
deuteron_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['deuteron_proton_magn_moment_ratio'].value
deuteron_proton_mass_ratio = PHYSICAL_CONSTANTS['deuteron_proton_mass_ratio'].value
electric_constant = PHYSICAL_CONSTANTS['electric_constant'].value
electron_charge_to_mass_quotient = PHYSICAL_CONSTANTS['electron_charge_to_mass_quotient'].value
electron_g_factor = PHYSICAL_CONSTANTS['electron_g_factor'].value
electron_gyromag_ratio = PHYSICAL_CONSTANTS['electron_gyromag_ratio'].value
electron_gyromag_ratio_in_mhz_t = PHYSICAL_CONSTANTS['electron_gyromag_ratio_in_mhz_t'].value
electron_gyromag_ratio_over_2_pi = PHYSICAL_CONSTANTS['electron_gyromag_ratio_over_2_pi'].value
electron_gyromagn_ratio = PHYSICAL_CONSTANTS['electron_gyromagn_ratio'].value
electron_gyromagn_ratio_over_2_pi = PHYSICAL_CONSTANTS['electron_gyromagn_ratio_over_2_pi'].value
electron_mag_mom = PHYSICAL_CONSTANTS['electron_mag_mom'].value
electron_mag_mom_anomaly = PHYSICAL_CONSTANTS['electron_mag_mom_anomaly'].value
electron_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['electron_mag_mom_to_bohr_magneton_ratio'].value
electron_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['electron_mag_mom_to_nuclear_magneton_ratio'].value
electron_magn_moment = PHYSICAL_CONSTANTS['electron_magn_moment'].value
electron_magn_moment_anomaly = PHYSICAL_CONSTANTS['electron_magn_moment_anomaly'].value
electron_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['electron_magn_moment_to_bohr_magneton_ratio'].value
electron_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['electron_magn_moment_to_nuclear_magneton_ratio'].value
electron_mass = PHYSICAL_CONSTANTS['electron_mass'].value
electron_mass_energy_equivalent = PHYSICAL_CONSTANTS['electron_mass_energy_equivalent'].value
electron_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['electron_mass_energy_equivalent_in_mev'].value
electron_mass_in_u = PHYSICAL_CONSTANTS['electron_mass_in_u'].value
electron_molar_mass = PHYSICAL_CONSTANTS['electron_molar_mass'].value
electron_relative_atomic_mass = PHYSICAL_CONSTANTS['electron_relative_atomic_mass'].value
electron_to_alpha_particle_mass_ratio = PHYSICAL_CONSTANTS['electron_to_alpha_particle_mass_ratio'].value
electron_to_shielded_helion_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_to_shielded_helion_mag_mom_ratio'].value
electron_to_shielded_helion_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_to_shielded_helion_magn_moment_ratio'].value
electron_to_shielded_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_to_shielded_proton_mag_mom_ratio'].value
electron_to_shielded_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_to_shielded_proton_magn_moment_ratio'].value
electron_volt = PHYSICAL_CONSTANTS['electron_volt'].value
electron_volt_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['electron_volt_atomic_mass_unit_relationship'].value
electron_volt_hartree_relationship = PHYSICAL_CONSTANTS['electron_volt_hartree_relationship'].value
electron_volt_hertz_relationship = PHYSICAL_CONSTANTS['electron_volt_hertz_relationship'].value
electron_volt_inverse_meter_relationship = PHYSICAL_CONSTANTS['electron_volt_inverse_meter_relationship'].value
electron_volt_joule_relationship = PHYSICAL_CONSTANTS['electron_volt_joule_relationship'].value
electron_volt_kelvin_relationship = PHYSICAL_CONSTANTS['electron_volt_kelvin_relationship'].value
electron_volt_kilogram_relationship = PHYSICAL_CONSTANTS['electron_volt_kilogram_relationship'].value
electron_deuteron_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_deuteron_mag_mom_ratio'].value
electron_deuteron_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_deuteron_magn_moment_ratio'].value
electron_deuteron_mass_ratio = PHYSICAL_CONSTANTS['electron_deuteron_mass_ratio'].value
electron_helion_mass_ratio = PHYSICAL_CONSTANTS['electron_helion_mass_ratio'].value
electron_muon_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_muon_mag_mom_ratio'].value
electron_muon_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_muon_magn_moment_ratio'].value
electron_muon_mass_ratio = PHYSICAL_CONSTANTS['electron_muon_mass_ratio'].value
electron_neutron_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_neutron_mag_mom_ratio'].value
electron_neutron_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_neutron_magn_moment_ratio'].value
electron_neutron_mass_ratio = PHYSICAL_CONSTANTS['electron_neutron_mass_ratio'].value
electron_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['electron_proton_mag_mom_ratio'].value
electron_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['electron_proton_magn_moment_ratio'].value
electron_proton_mass_ratio = PHYSICAL_CONSTANTS['electron_proton_mass_ratio'].value
electron_tau_mass_ratio = PHYSICAL_CONSTANTS['electron_tau_mass_ratio'].value
electron_triton_mass_ratio = PHYSICAL_CONSTANTS['electron_triton_mass_ratio'].value
elementary_charge = PHYSICAL_CONSTANTS['elementary_charge'].value
elementary_charge_over_h = PHYSICAL_CONSTANTS['elementary_charge_over_h'].value
elementary_charge_over_h_bar = PHYSICAL_CONSTANTS['elementary_charge_over_h_bar'].value
fine_structure_constant = PHYSICAL_CONSTANTS['fine_structure_constant'].value
first_radiation_constant = PHYSICAL_CONSTANTS['first_radiation_constant'].value
first_radiation_constant_for_spectral_radiance = PHYSICAL_CONSTANTS['first_radiation_constant_for_spectral_radiance'].value
hartree_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['hartree_atomic_mass_unit_relationship'].value
hartree_electron_volt_relationship = PHYSICAL_CONSTANTS['hartree_electron_volt_relationship'].value
hartree_hertz_relationship = PHYSICAL_CONSTANTS['hartree_hertz_relationship'].value
hartree_inverse_meter_relationship = PHYSICAL_CONSTANTS['hartree_inverse_meter_relationship'].value
hartree_joule_relationship = PHYSICAL_CONSTANTS['hartree_joule_relationship'].value
hartree_kelvin_relationship = PHYSICAL_CONSTANTS['hartree_kelvin_relationship'].value
hartree_kilogram_relationship = PHYSICAL_CONSTANTS['hartree_kilogram_relationship'].value
helion_g_factor = PHYSICAL_CONSTANTS['helion_g_factor'].value
helion_mag_mom = PHYSICAL_CONSTANTS['helion_mag_mom'].value
helion_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['helion_mag_mom_to_bohr_magneton_ratio'].value
helion_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['helion_mag_mom_to_nuclear_magneton_ratio'].value
helion_mass = PHYSICAL_CONSTANTS['helion_mass'].value
helion_mass_energy_equivalent = PHYSICAL_CONSTANTS['helion_mass_energy_equivalent'].value
helion_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['helion_mass_energy_equivalent_in_mev'].value
helion_mass_in_u = PHYSICAL_CONSTANTS['helion_mass_in_u'].value
helion_molar_mass = PHYSICAL_CONSTANTS['helion_molar_mass'].value
helion_relative_atomic_mass = PHYSICAL_CONSTANTS['helion_relative_atomic_mass'].value
helion_shielding_shift = PHYSICAL_CONSTANTS['helion_shielding_shift'].value
helion_electron_mass_ratio = PHYSICAL_CONSTANTS['helion_electron_mass_ratio'].value
helion_proton_mass_ratio = PHYSICAL_CONSTANTS['helion_proton_mass_ratio'].value
hertz_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['hertz_atomic_mass_unit_relationship'].value
hertz_electron_volt_relationship = PHYSICAL_CONSTANTS['hertz_electron_volt_relationship'].value
hertz_hartree_relationship = PHYSICAL_CONSTANTS['hertz_hartree_relationship'].value
hertz_inverse_meter_relationship = PHYSICAL_CONSTANTS['hertz_inverse_meter_relationship'].value
hertz_joule_relationship = PHYSICAL_CONSTANTS['hertz_joule_relationship'].value
hertz_kelvin_relationship = PHYSICAL_CONSTANTS['hertz_kelvin_relationship'].value
hertz_kilogram_relationship = PHYSICAL_CONSTANTS['hertz_kilogram_relationship'].value
hyperfine_transition_frequency_of_cs_133 = PHYSICAL_CONSTANTS['hyperfine_transition_frequency_of_cs_133'].value
inverse_fine_structure_constant = PHYSICAL_CONSTANTS['inverse_fine_structure_constant'].value
inverse_meter_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['inverse_meter_atomic_mass_unit_relationship'].value
inverse_meter_electron_volt_relationship = PHYSICAL_CONSTANTS['inverse_meter_electron_volt_relationship'].value
inverse_meter_hartree_relationship = PHYSICAL_CONSTANTS['inverse_meter_hartree_relationship'].value
inverse_meter_hertz_relationship = PHYSICAL_CONSTANTS['inverse_meter_hertz_relationship'].value
inverse_meter_joule_relationship = PHYSICAL_CONSTANTS['inverse_meter_joule_relationship'].value
inverse_meter_kelvin_relationship = PHYSICAL_CONSTANTS['inverse_meter_kelvin_relationship'].value
inverse_meter_kilogram_relationship = PHYSICAL_CONSTANTS['inverse_meter_kilogram_relationship'].value
inverse_of_conductance_quantum = PHYSICAL_CONSTANTS['inverse_of_conductance_quantum'].value
joule_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['joule_atomic_mass_unit_relationship'].value
joule_electron_volt_relationship = PHYSICAL_CONSTANTS['joule_electron_volt_relationship'].value
joule_hartree_relationship = PHYSICAL_CONSTANTS['joule_hartree_relationship'].value
joule_hertz_relationship = PHYSICAL_CONSTANTS['joule_hertz_relationship'].value
joule_inverse_meter_relationship = PHYSICAL_CONSTANTS['joule_inverse_meter_relationship'].value
joule_kelvin_relationship = PHYSICAL_CONSTANTS['joule_kelvin_relationship'].value
joule_kilogram_relationship = PHYSICAL_CONSTANTS['joule_kilogram_relationship'].value
kelvin_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['kelvin_atomic_mass_unit_relationship'].value
kelvin_electron_volt_relationship = PHYSICAL_CONSTANTS['kelvin_electron_volt_relationship'].value
kelvin_hartree_relationship = PHYSICAL_CONSTANTS['kelvin_hartree_relationship'].value
kelvin_hertz_relationship = PHYSICAL_CONSTANTS['kelvin_hertz_relationship'].value
kelvin_inverse_meter_relationship = PHYSICAL_CONSTANTS['kelvin_inverse_meter_relationship'].value
kelvin_joule_relationship = PHYSICAL_CONSTANTS['kelvin_joule_relationship'].value
kelvin_kilogram_relationship = PHYSICAL_CONSTANTS['kelvin_kilogram_relationship'].value
kilogram_atomic_mass_unit_relationship = PHYSICAL_CONSTANTS['kilogram_atomic_mass_unit_relationship'].value
kilogram_electron_volt_relationship = PHYSICAL_CONSTANTS['kilogram_electron_volt_relationship'].value
kilogram_hartree_relationship = PHYSICAL_CONSTANTS['kilogram_hartree_relationship'].value
kilogram_hertz_relationship = PHYSICAL_CONSTANTS['kilogram_hertz_relationship'].value
kilogram_inverse_meter_relationship = PHYSICAL_CONSTANTS['kilogram_inverse_meter_relationship'].value
kilogram_joule_relationship = PHYSICAL_CONSTANTS['kilogram_joule_relationship'].value
kilogram_kelvin_relationship = PHYSICAL_CONSTANTS['kilogram_kelvin_relationship'].value
lattice_parameter_of_silicon = PHYSICAL_CONSTANTS['lattice_parameter_of_silicon'].value
lattice_spacing_of_ideal_si_220 = PHYSICAL_CONSTANTS['lattice_spacing_of_ideal_si_220'].value
lattice_spacing_of_silicon = PHYSICAL_CONSTANTS['lattice_spacing_of_silicon'].value
luminous_efficacy = PHYSICAL_CONSTANTS['luminous_efficacy'].value
mag_constant = PHYSICAL_CONSTANTS['mag_constant'].value
mag_flux_quantum = PHYSICAL_CONSTANTS['mag_flux_quantum'].value
magn_constant = PHYSICAL_CONSTANTS['magn_constant'].value
magn_flux_quantum = PHYSICAL_CONSTANTS['magn_flux_quantum'].value
molar_planck_constant = PHYSICAL_CONSTANTS['molar_planck_constant'].value
molar_planck_constant_times_c = PHYSICAL_CONSTANTS['molar_planck_constant_times_c'].value
molar_gas_constant = PHYSICAL_CONSTANTS['molar_gas_constant'].value
molar_mass_constant = PHYSICAL_CONSTANTS['molar_mass_constant'].value
molar_mass_of_carbon_12 = PHYSICAL_CONSTANTS['molar_mass_of_carbon_12'].value
molar_volume_of_ideal_gas_273_15_k_100_kpa = PHYSICAL_CONSTANTS['molar_volume_of_ideal_gas_273_15_k_100_kpa'].value
molar_volume_of_ideal_gas_273_15_k_101_325_kpa = PHYSICAL_CONSTANTS['molar_volume_of_ideal_gas_273_15_k_101_325_kpa'].value
molar_volume_of_silicon = PHYSICAL_CONSTANTS['molar_volume_of_silicon'].value
muon_compton_wavelength = PHYSICAL_CONSTANTS['muon_compton_wavelength'].value
muon_compton_wavelength_over_2_pi = PHYSICAL_CONSTANTS['muon_compton_wavelength_over_2_pi'].value
muon_g_factor = PHYSICAL_CONSTANTS['muon_g_factor'].value
muon_mag_mom = PHYSICAL_CONSTANTS['muon_mag_mom'].value
muon_mag_mom_anomaly = PHYSICAL_CONSTANTS['muon_mag_mom_anomaly'].value
muon_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['muon_mag_mom_to_bohr_magneton_ratio'].value
muon_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['muon_mag_mom_to_nuclear_magneton_ratio'].value
muon_magn_moment = PHYSICAL_CONSTANTS['muon_magn_moment'].value
muon_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['muon_magn_moment_to_bohr_magneton_ratio'].value
muon_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['muon_magn_moment_to_nuclear_magneton_ratio'].value
muon_mass = PHYSICAL_CONSTANTS['muon_mass'].value
muon_mass_energy_equivalent = PHYSICAL_CONSTANTS['muon_mass_energy_equivalent'].value
muon_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['muon_mass_energy_equivalent_in_mev'].value
muon_mass_in_u = PHYSICAL_CONSTANTS['muon_mass_in_u'].value
muon_molar_mass = PHYSICAL_CONSTANTS['muon_molar_mass'].value
muon_electron_mass_ratio = PHYSICAL_CONSTANTS['muon_electron_mass_ratio'].value
muon_neutron_mass_ratio = PHYSICAL_CONSTANTS['muon_neutron_mass_ratio'].value
muon_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['muon_proton_mag_mom_ratio'].value
muon_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['muon_proton_magn_moment_ratio'].value
muon_proton_mass_ratio = PHYSICAL_CONSTANTS['muon_proton_mass_ratio'].value
muon_tau_mass_ratio = PHYSICAL_CONSTANTS['muon_tau_mass_ratio'].value
natural_unit_of_action = PHYSICAL_CONSTANTS['natural_unit_of_action'].value
natural_unit_of_action_in_ev_s = PHYSICAL_CONSTANTS['natural_unit_of_action_in_ev_s'].value
natural_unit_of_energy = PHYSICAL_CONSTANTS['natural_unit_of_energy'].value
natural_unit_of_energy_in_mev = PHYSICAL_CONSTANTS['natural_unit_of_energy_in_mev'].value
natural_unit_of_length = PHYSICAL_CONSTANTS['natural_unit_of_length'].value
natural_unit_of_mass = PHYSICAL_CONSTANTS['natural_unit_of_mass'].value
natural_unit_of_mom_um = PHYSICAL_CONSTANTS['natural_unit_of_mom_um'].value
natural_unit_of_mom_um_in_mev_c = PHYSICAL_CONSTANTS['natural_unit_of_mom_um_in_mev_c'].value
natural_unit_of_momentum = PHYSICAL_CONSTANTS['natural_unit_of_momentum'].value
natural_unit_of_momentum_in_mev_c = PHYSICAL_CONSTANTS['natural_unit_of_momentum_in_mev_c'].value
natural_unit_of_time = PHYSICAL_CONSTANTS['natural_unit_of_time'].value
natural_unit_of_velocity = PHYSICAL_CONSTANTS['natural_unit_of_velocity'].value
neutron_compton_wavelength = PHYSICAL_CONSTANTS['neutron_compton_wavelength'].value
neutron_compton_wavelength_over_2_pi = PHYSICAL_CONSTANTS['neutron_compton_wavelength_over_2_pi'].value
neutron_g_factor = PHYSICAL_CONSTANTS['neutron_g_factor'].value
neutron_gyromag_ratio = PHYSICAL_CONSTANTS['neutron_gyromag_ratio'].value
neutron_gyromag_ratio_in_mhz_t = PHYSICAL_CONSTANTS['neutron_gyromag_ratio_in_mhz_t'].value
neutron_gyromag_ratio_over_2_pi = PHYSICAL_CONSTANTS['neutron_gyromag_ratio_over_2_pi'].value
neutron_gyromagn_ratio = PHYSICAL_CONSTANTS['neutron_gyromagn_ratio'].value
neutron_gyromagn_ratio_over_2_pi = PHYSICAL_CONSTANTS['neutron_gyromagn_ratio_over_2_pi'].value
neutron_mag_mom = PHYSICAL_CONSTANTS['neutron_mag_mom'].value
neutron_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['neutron_mag_mom_to_bohr_magneton_ratio'].value
neutron_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['neutron_mag_mom_to_nuclear_magneton_ratio'].value
neutron_magn_moment = PHYSICAL_CONSTANTS['neutron_magn_moment'].value
neutron_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['neutron_magn_moment_to_bohr_magneton_ratio'].value
neutron_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['neutron_magn_moment_to_nuclear_magneton_ratio'].value
neutron_mass = PHYSICAL_CONSTANTS['neutron_mass'].value
neutron_mass_energy_equivalent = PHYSICAL_CONSTANTS['neutron_mass_energy_equivalent'].value
neutron_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['neutron_mass_energy_equivalent_in_mev'].value
neutron_mass_in_u = PHYSICAL_CONSTANTS['neutron_mass_in_u'].value
neutron_molar_mass = PHYSICAL_CONSTANTS['neutron_molar_mass'].value
neutron_relative_atomic_mass = PHYSICAL_CONSTANTS['neutron_relative_atomic_mass'].value
neutron_to_shielded_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['neutron_to_shielded_proton_mag_mom_ratio'].value
neutron_to_shielded_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['neutron_to_shielded_proton_magn_moment_ratio'].value
neutron_electron_mag_mom_ratio = PHYSICAL_CONSTANTS['neutron_electron_mag_mom_ratio'].value
neutron_electron_magn_moment_ratio = PHYSICAL_CONSTANTS['neutron_electron_magn_moment_ratio'].value
neutron_electron_mass_ratio = PHYSICAL_CONSTANTS['neutron_electron_mass_ratio'].value
neutron_muon_mass_ratio = PHYSICAL_CONSTANTS['neutron_muon_mass_ratio'].value
neutron_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['neutron_proton_mag_mom_ratio'].value
neutron_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['neutron_proton_magn_moment_ratio'].value
neutron_proton_mass_difference = PHYSICAL_CONSTANTS['neutron_proton_mass_difference'].value
neutron_proton_mass_difference_energy_equivalent = PHYSICAL_CONSTANTS['neutron_proton_mass_difference_energy_equivalent'].value
neutron_proton_mass_difference_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['neutron_proton_mass_difference_energy_equivalent_in_mev'].value
neutron_proton_mass_difference_in_u = PHYSICAL_CONSTANTS['neutron_proton_mass_difference_in_u'].value
neutron_proton_mass_ratio = PHYSICAL_CONSTANTS['neutron_proton_mass_ratio'].value
neutron_tau_mass_ratio = PHYSICAL_CONSTANTS['neutron_tau_mass_ratio'].value
nuclear_magneton = PHYSICAL_CONSTANTS['nuclear_magneton'].value
nuclear_magneton_in_k_t = PHYSICAL_CONSTANTS['nuclear_magneton_in_k_t'].value
nuclear_magneton_in_mhz_t = PHYSICAL_CONSTANTS['nuclear_magneton_in_mhz_t'].value
nuclear_magneton_in_ev_t = PHYSICAL_CONSTANTS['nuclear_magneton_in_ev_t'].value
nuclear_magneton_in_inverse_meter_per_tesla = PHYSICAL_CONSTANTS['nuclear_magneton_in_inverse_meter_per_tesla'].value
nuclear_magneton_in_inverse_meters_per_tesla = PHYSICAL_CONSTANTS['nuclear_magneton_in_inverse_meters_per_tesla'].value
proton_compton_wavelength = PHYSICAL_CONSTANTS['proton_compton_wavelength'].value
proton_compton_wavelength_over_2_pi = PHYSICAL_CONSTANTS['proton_compton_wavelength_over_2_pi'].value
proton_charge_to_mass_quotient = PHYSICAL_CONSTANTS['proton_charge_to_mass_quotient'].value
proton_g_factor = PHYSICAL_CONSTANTS['proton_g_factor'].value
proton_gyromag_ratio = PHYSICAL_CONSTANTS['proton_gyromag_ratio'].value
proton_gyromag_ratio_in_mhz_t = PHYSICAL_CONSTANTS['proton_gyromag_ratio_in_mhz_t'].value
proton_gyromag_ratio_over_2_pi = PHYSICAL_CONSTANTS['proton_gyromag_ratio_over_2_pi'].value
proton_gyromagn_ratio = PHYSICAL_CONSTANTS['proton_gyromagn_ratio'].value
proton_gyromagn_ratio_over_2_pi = PHYSICAL_CONSTANTS['proton_gyromagn_ratio_over_2_pi'].value
proton_mag_mom = PHYSICAL_CONSTANTS['proton_mag_mom'].value
proton_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['proton_mag_mom_to_bohr_magneton_ratio'].value
proton_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['proton_mag_mom_to_nuclear_magneton_ratio'].value
proton_mag_shielding_correction = PHYSICAL_CONSTANTS['proton_mag_shielding_correction'].value
proton_magn_moment = PHYSICAL_CONSTANTS['proton_magn_moment'].value
proton_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['proton_magn_moment_to_bohr_magneton_ratio'].value
proton_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['proton_magn_moment_to_nuclear_magneton_ratio'].value
proton_magn_shielding_correction = PHYSICAL_CONSTANTS['proton_magn_shielding_correction'].value
proton_mass = PHYSICAL_CONSTANTS['proton_mass'].value
proton_mass_energy_equivalent = PHYSICAL_CONSTANTS['proton_mass_energy_equivalent'].value
proton_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['proton_mass_energy_equivalent_in_mev'].value
proton_mass_in_u = PHYSICAL_CONSTANTS['proton_mass_in_u'].value
proton_molar_mass = PHYSICAL_CONSTANTS['proton_molar_mass'].value
proton_relative_atomic_mass = PHYSICAL_CONSTANTS['proton_relative_atomic_mass'].value
proton_rms_charge_radius = PHYSICAL_CONSTANTS['proton_rms_charge_radius'].value
proton_electron_mass_ratio = PHYSICAL_CONSTANTS['proton_electron_mass_ratio'].value
proton_muon_mass_ratio = PHYSICAL_CONSTANTS['proton_muon_mass_ratio'].value
proton_neutron_mag_mom_ratio = PHYSICAL_CONSTANTS['proton_neutron_mag_mom_ratio'].value
proton_neutron_magn_moment_ratio = PHYSICAL_CONSTANTS['proton_neutron_magn_moment_ratio'].value
proton_neutron_mass_ratio = PHYSICAL_CONSTANTS['proton_neutron_mass_ratio'].value
proton_tau_mass_ratio = PHYSICAL_CONSTANTS['proton_tau_mass_ratio'].value
quantum_of_circulation = PHYSICAL_CONSTANTS['quantum_of_circulation'].value
quantum_of_circulation_times_2 = PHYSICAL_CONSTANTS['quantum_of_circulation_times_2'].value
reduced_compton_wavelength = PHYSICAL_CONSTANTS['reduced_compton_wavelength'].value
reduced_planck_constant = PHYSICAL_CONSTANTS['reduced_planck_constant'].value
reduced_planck_constant_in_ev_s = PHYSICAL_CONSTANTS['reduced_planck_constant_in_ev_s'].value
reduced_planck_constant_times_c_in_mev_fm = PHYSICAL_CONSTANTS['reduced_planck_constant_times_c_in_mev_fm'].value
reduced_muon_compton_wavelength = PHYSICAL_CONSTANTS['reduced_muon_compton_wavelength'].value
reduced_neutron_compton_wavelength = PHYSICAL_CONSTANTS['reduced_neutron_compton_wavelength'].value
reduced_proton_compton_wavelength = PHYSICAL_CONSTANTS['reduced_proton_compton_wavelength'].value
reduced_tau_compton_wavelength = PHYSICAL_CONSTANTS['reduced_tau_compton_wavelength'].value
second_radiation_constant = PHYSICAL_CONSTANTS['second_radiation_constant'].value
shielded_helion_gyromag_ratio = PHYSICAL_CONSTANTS['shielded_helion_gyromag_ratio'].value
shielded_helion_gyromag_ratio_in_mhz_t = PHYSICAL_CONSTANTS['shielded_helion_gyromag_ratio_in_mhz_t'].value
shielded_helion_gyromag_ratio_over_2_pi = PHYSICAL_CONSTANTS['shielded_helion_gyromag_ratio_over_2_pi'].value
shielded_helion_gyromagn_ratio = PHYSICAL_CONSTANTS['shielded_helion_gyromagn_ratio'].value
shielded_helion_gyromagn_ratio_over_2_pi = PHYSICAL_CONSTANTS['shielded_helion_gyromagn_ratio_over_2_pi'].value
shielded_helion_mag_mom = PHYSICAL_CONSTANTS['shielded_helion_mag_mom'].value
shielded_helion_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['shielded_helion_mag_mom_to_bohr_magneton_ratio'].value
shielded_helion_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['shielded_helion_mag_mom_to_nuclear_magneton_ratio'].value
shielded_helion_magn_moment = PHYSICAL_CONSTANTS['shielded_helion_magn_moment'].value
shielded_helion_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['shielded_helion_magn_moment_to_bohr_magneton_ratio'].value
shielded_helion_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['shielded_helion_magn_moment_to_nuclear_magneton_ratio'].value
shielded_helion_to_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['shielded_helion_to_proton_mag_mom_ratio'].value
shielded_helion_to_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['shielded_helion_to_proton_magn_moment_ratio'].value
shielded_helion_to_shielded_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['shielded_helion_to_shielded_proton_mag_mom_ratio'].value
shielded_helion_to_shielded_proton_magn_moment_ratio = PHYSICAL_CONSTANTS['shielded_helion_to_shielded_proton_magn_moment_ratio'].value
shielded_proton_gyromag_ratio = PHYSICAL_CONSTANTS['shielded_proton_gyromag_ratio'].value
shielded_proton_gyromag_ratio_in_mhz_t = PHYSICAL_CONSTANTS['shielded_proton_gyromag_ratio_in_mhz_t'].value
shielded_proton_gyromag_ratio_over_2_pi = PHYSICAL_CONSTANTS['shielded_proton_gyromag_ratio_over_2_pi'].value
shielded_proton_mag_mom = PHYSICAL_CONSTANTS['shielded_proton_mag_mom'].value
shielded_proton_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['shielded_proton_mag_mom_to_bohr_magneton_ratio'].value
shielded_proton_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['shielded_proton_mag_mom_to_nuclear_magneton_ratio'].value
shielded_proton_magn_moment = PHYSICAL_CONSTANTS['shielded_proton_magn_moment'].value
shielded_proton_magn_moment_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['shielded_proton_magn_moment_to_bohr_magneton_ratio'].value
shielded_proton_magn_moment_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['shielded_proton_magn_moment_to_nuclear_magneton_ratio'].value
shielding_difference_of_d_and_p_in_hd = PHYSICAL_CONSTANTS['shielding_difference_of_d_and_p_in_hd'].value
shielding_difference_of_t_and_p_in_ht = PHYSICAL_CONSTANTS['shielding_difference_of_t_and_p_in_ht'].value
speed_of_light_in_vacuum = PHYSICAL_CONSTANTS['speed_of_light_in_vacuum'].value
standard_acceleration_of_gravity = PHYSICAL_CONSTANTS['standard_acceleration_of_gravity'].value
standard_atmosphere = PHYSICAL_CONSTANTS['standard_atmosphere'].value
standard_state_pressure = PHYSICAL_CONSTANTS['standard_state_pressure'].value
tau_compton_wavelength = PHYSICAL_CONSTANTS['tau_compton_wavelength'].value
tau_compton_wavelength_over_2_pi = PHYSICAL_CONSTANTS['tau_compton_wavelength_over_2_pi'].value
tau_energy_equivalent = PHYSICAL_CONSTANTS['tau_energy_equivalent'].value
tau_mass = PHYSICAL_CONSTANTS['tau_mass'].value
tau_mass_energy_equivalent = PHYSICAL_CONSTANTS['tau_mass_energy_equivalent'].value
tau_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['tau_mass_energy_equivalent_in_mev'].value
tau_mass_in_u = PHYSICAL_CONSTANTS['tau_mass_in_u'].value
tau_molar_mass = PHYSICAL_CONSTANTS['tau_molar_mass'].value
tau_electron_mass_ratio = PHYSICAL_CONSTANTS['tau_electron_mass_ratio'].value
tau_muon_mass_ratio = PHYSICAL_CONSTANTS['tau_muon_mass_ratio'].value
tau_neutron_mass_ratio = PHYSICAL_CONSTANTS['tau_neutron_mass_ratio'].value
tau_proton_mass_ratio = PHYSICAL_CONSTANTS['tau_proton_mass_ratio'].value
triton_g_factor = PHYSICAL_CONSTANTS['triton_g_factor'].value
triton_mag_mom = PHYSICAL_CONSTANTS['triton_mag_mom'].value
triton_mag_mom_to_bohr_magneton_ratio = PHYSICAL_CONSTANTS['triton_mag_mom_to_bohr_magneton_ratio'].value
triton_mag_mom_to_nuclear_magneton_ratio = PHYSICAL_CONSTANTS['triton_mag_mom_to_nuclear_magneton_ratio'].value
triton_mass = PHYSICAL_CONSTANTS['triton_mass'].value
triton_mass_energy_equivalent = PHYSICAL_CONSTANTS['triton_mass_energy_equivalent'].value
triton_mass_energy_equivalent_in_mev = PHYSICAL_CONSTANTS['triton_mass_energy_equivalent_in_mev'].value
triton_mass_in_u = PHYSICAL_CONSTANTS['triton_mass_in_u'].value
triton_molar_mass = PHYSICAL_CONSTANTS['triton_molar_mass'].value
triton_relative_atomic_mass = PHYSICAL_CONSTANTS['triton_relative_atomic_mass'].value
triton_to_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['triton_to_proton_mag_mom_ratio'].value
triton_electron_mag_mom_ratio = PHYSICAL_CONSTANTS['triton_electron_mag_mom_ratio'].value
triton_electron_mass_ratio = PHYSICAL_CONSTANTS['triton_electron_mass_ratio'].value
triton_neutron_mag_mom_ratio = PHYSICAL_CONSTANTS['triton_neutron_mag_mom_ratio'].value
triton_proton_mag_mom_ratio = PHYSICAL_CONSTANTS['triton_proton_mag_mom_ratio'].value
triton_proton_mass_ratio = PHYSICAL_CONSTANTS['triton_proton_mass_ratio'].value
unified_atomic_mass_unit = PHYSICAL_CONSTANTS['unified_atomic_mass_unit'].value
vacuum_electric_permittivity = PHYSICAL_CONSTANTS['vacuum_electric_permittivity'].value
vacuum_mag_permeability = PHYSICAL_CONSTANTS['vacuum_mag_permeability'].value
von_klitzing_constant = PHYSICAL_CONSTANTS['von_klitzing_constant'].value
weak_mixing_angle = PHYSICAL_CONSTANTS['weak_mixing_angle'].value
constant_220_lattice_spacing_of_silicon = PHYSICAL_CONSTANTS['constant_220_lattice_spacing_of_silicon'].value

R = molar_gas_constant
F = faraday_constant
N_A = avogadro_constant
h = planck_constant
c = speed_of_light_in_vacuum
e = elementary_charge
k_B = boltzmann_constant
speed_of_light = speed_of_light_in_vacuum
planck = planck_constant
hbar = reduced_planck_constant


def constant(name: str) -> float:
    """Return a physical constant value by source name or snake_case name."""

    key = _normalize_name(name)
    try:
        return PHYSICAL_CONSTANTS[CONSTANT_ALIASES[key]].value
    except KeyError as exc:
        raise KeyError(f"Unknown physical constant: {name}") from exc


def constant_info(name: str) -> Constant:
    """Return value, unit, uncertainty, and CODATA source name."""

    key = _normalize_name(name)
    try:
        return PHYSICAL_CONSTANTS[CONSTANT_ALIASES[key]]
    except KeyError as exc:
        raise KeyError(f"Unknown physical constant: {name}") from exc


__all__ = [
    'CONSTANT_ALIASES',
    'Constant',
    'F',
    'N_A',
    'PHYSICAL_CONSTANTS',
    'R',
    'alpha_particle_electron_mass_ratio',
    'alpha_particle_mass',
    'alpha_particle_mass_energy_equivalent',
    'alpha_particle_mass_energy_equivalent_in_mev',
    'alpha_particle_mass_in_u',
    'alpha_particle_molar_mass',
    'alpha_particle_proton_mass_ratio',
    'alpha_particle_relative_atomic_mass',
    'alpha_particle_rms_charge_radius',
    'angstrom_star',
    'atomic_mass_constant',
    'atomic_mass_constant_energy_equivalent',
    'atomic_mass_constant_energy_equivalent_in_mev',
    'atomic_mass_unit_electron_volt_relationship',
    'atomic_mass_unit_hartree_relationship',
    'atomic_mass_unit_hertz_relationship',
    'atomic_mass_unit_inverse_meter_relationship',
    'atomic_mass_unit_joule_relationship',
    'atomic_mass_unit_kelvin_relationship',
    'atomic_mass_unit_kilogram_relationship',
    'atomic_unit_of_1st_hyperpolarizability',
    'atomic_unit_of_1st_hyperpolarizablity',
    'atomic_unit_of_2nd_hyperpolarizability',
    'atomic_unit_of_2nd_hyperpolarizablity',
    'atomic_unit_of_action',
    'atomic_unit_of_charge',
    'atomic_unit_of_charge_density',
    'atomic_unit_of_current',
    'atomic_unit_of_electric_dipole_mom',
    'atomic_unit_of_electric_dipole_moment',
    'atomic_unit_of_electric_field',
    'atomic_unit_of_electric_field_gradient',
    'atomic_unit_of_electric_polarizability',
    'atomic_unit_of_electric_polarizablity',
    'atomic_unit_of_electric_potential',
    'atomic_unit_of_electric_quadrupole_mom',
    'atomic_unit_of_electric_quadrupole_moment',
    'atomic_unit_of_energy',
    'atomic_unit_of_force',
    'atomic_unit_of_length',
    'atomic_unit_of_mag_dipole_mom',
    'atomic_unit_of_mag_flux_density',
    'atomic_unit_of_magn_dipole_moment',
    'atomic_unit_of_magn_flux_density',
    'atomic_unit_of_magnetizability',
    'atomic_unit_of_mass',
    'atomic_unit_of_mom_um',
    'atomic_unit_of_momentum',
    'atomic_unit_of_permittivity',
    'atomic_unit_of_time',
    'atomic_unit_of_velocity',
    'avogadro_constant',
    'bohr_magneton',
    'bohr_magneton_in_ev_t',
    'bohr_magneton_in_hz_t',
    'bohr_magneton_in_inverse_meter_per_tesla',
    'bohr_magneton_in_inverse_meters_per_tesla',
    'bohr_magneton_in_k_t',
    'bohr_radius',
    'boltzmann_constant',
    'boltzmann_constant_in_ev_k',
    'boltzmann_constant_in_hz_k',
    'boltzmann_constant_in_inverse_meter_per_kelvin',
    'boltzmann_constant_in_inverse_meters_per_kelvin',
    'c',
    'characteristic_impedance_of_vacuum',
    'classical_electron_radius',
    'compton_wavelength',
    'compton_wavelength_over_2_pi',
    'conductance_quantum',
    'constant',
    'constant_220_lattice_spacing_of_silicon',
    'constant_info',
    'conventional_value_of_ampere_90',
    'conventional_value_of_coulomb_90',
    'conventional_value_of_farad_90',
    'conventional_value_of_henry_90',
    'conventional_value_of_josephson_constant',
    'conventional_value_of_ohm_90',
    'conventional_value_of_volt_90',
    'conventional_value_of_von_klitzing_constant',
    'conventional_value_of_watt_90',
    'copper_x_unit',
    'cu_x_unit',
    'deuteron_electron_mag_mom_ratio',
    'deuteron_electron_magn_moment_ratio',
    'deuteron_electron_mass_ratio',
    'deuteron_g_factor',
    'deuteron_mag_mom',
    'deuteron_mag_mom_to_bohr_magneton_ratio',
    'deuteron_mag_mom_to_nuclear_magneton_ratio',
    'deuteron_magn_moment',
    'deuteron_magn_moment_to_bohr_magneton_ratio',
    'deuteron_magn_moment_to_nuclear_magneton_ratio',
    'deuteron_mass',
    'deuteron_mass_energy_equivalent',
    'deuteron_mass_energy_equivalent_in_mev',
    'deuteron_mass_in_u',
    'deuteron_molar_mass',
    'deuteron_neutron_mag_mom_ratio',
    'deuteron_neutron_magn_moment_ratio',
    'deuteron_proton_mag_mom_ratio',
    'deuteron_proton_magn_moment_ratio',
    'deuteron_proton_mass_ratio',
    'deuteron_relative_atomic_mass',
    'deuteron_rms_charge_radius',
    'e',
    'electric_constant',
    'electron_charge_to_mass_quotient',
    'electron_deuteron_mag_mom_ratio',
    'electron_deuteron_magn_moment_ratio',
    'electron_deuteron_mass_ratio',
    'electron_g_factor',
    'electron_gyromag_ratio',
    'electron_gyromag_ratio_in_mhz_t',
    'electron_gyromag_ratio_over_2_pi',
    'electron_gyromagn_ratio',
    'electron_gyromagn_ratio_over_2_pi',
    'electron_helion_mass_ratio',
    'electron_mag_mom',
    'electron_mag_mom_anomaly',
    'electron_mag_mom_to_bohr_magneton_ratio',
    'electron_mag_mom_to_nuclear_magneton_ratio',
    'electron_magn_moment',
    'electron_magn_moment_anomaly',
    'electron_magn_moment_to_bohr_magneton_ratio',
    'electron_magn_moment_to_nuclear_magneton_ratio',
    'electron_mass',
    'electron_mass_energy_equivalent',
    'electron_mass_energy_equivalent_in_mev',
    'electron_mass_in_u',
    'electron_molar_mass',
    'electron_muon_mag_mom_ratio',
    'electron_muon_magn_moment_ratio',
    'electron_muon_mass_ratio',
    'electron_neutron_mag_mom_ratio',
    'electron_neutron_magn_moment_ratio',
    'electron_neutron_mass_ratio',
    'electron_proton_mag_mom_ratio',
    'electron_proton_magn_moment_ratio',
    'electron_proton_mass_ratio',
    'electron_relative_atomic_mass',
    'electron_tau_mass_ratio',
    'electron_to_alpha_particle_mass_ratio',
    'electron_to_shielded_helion_mag_mom_ratio',
    'electron_to_shielded_helion_magn_moment_ratio',
    'electron_to_shielded_proton_mag_mom_ratio',
    'electron_to_shielded_proton_magn_moment_ratio',
    'electron_triton_mass_ratio',
    'electron_volt',
    'electron_volt_atomic_mass_unit_relationship',
    'electron_volt_hartree_relationship',
    'electron_volt_hertz_relationship',
    'electron_volt_inverse_meter_relationship',
    'electron_volt_joule_relationship',
    'electron_volt_kelvin_relationship',
    'electron_volt_kilogram_relationship',
    'elementary_charge',
    'elementary_charge_over_h',
    'elementary_charge_over_h_bar',
    'faraday_constant',
    'faraday_constant_for_conventional_electric_current',
    'fermi_coupling_constant',
    'fine_structure_constant',
    'first_radiation_constant',
    'first_radiation_constant_for_spectral_radiance',
    'h',
    'hartree_atomic_mass_unit_relationship',
    'hartree_electron_volt_relationship',
    'hartree_energy',
    'hartree_energy_in_ev',
    'hartree_hertz_relationship',
    'hartree_inverse_meter_relationship',
    'hartree_joule_relationship',
    'hartree_kelvin_relationship',
    'hartree_kilogram_relationship',
    'hbar',
    'helion_electron_mass_ratio',
    'helion_g_factor',
    'helion_mag_mom',
    'helion_mag_mom_to_bohr_magneton_ratio',
    'helion_mag_mom_to_nuclear_magneton_ratio',
    'helion_mass',
    'helion_mass_energy_equivalent',
    'helion_mass_energy_equivalent_in_mev',
    'helion_mass_in_u',
    'helion_molar_mass',
    'helion_proton_mass_ratio',
    'helion_relative_atomic_mass',
    'helion_shielding_shift',
    'hertz_atomic_mass_unit_relationship',
    'hertz_electron_volt_relationship',
    'hertz_hartree_relationship',
    'hertz_inverse_meter_relationship',
    'hertz_joule_relationship',
    'hertz_kelvin_relationship',
    'hertz_kilogram_relationship',
    'hyperfine_transition_frequency_of_cs_133',
    'inverse_fine_structure_constant',
    'inverse_meter_atomic_mass_unit_relationship',
    'inverse_meter_electron_volt_relationship',
    'inverse_meter_hartree_relationship',
    'inverse_meter_hertz_relationship',
    'inverse_meter_joule_relationship',
    'inverse_meter_kelvin_relationship',
    'inverse_meter_kilogram_relationship',
    'inverse_of_conductance_quantum',
    'josephson_constant',
    'joule_atomic_mass_unit_relationship',
    'joule_electron_volt_relationship',
    'joule_hartree_relationship',
    'joule_hertz_relationship',
    'joule_inverse_meter_relationship',
    'joule_kelvin_relationship',
    'joule_kilogram_relationship',
    'k_B',
    'kelvin_atomic_mass_unit_relationship',
    'kelvin_electron_volt_relationship',
    'kelvin_hartree_relationship',
    'kelvin_hertz_relationship',
    'kelvin_inverse_meter_relationship',
    'kelvin_joule_relationship',
    'kelvin_kilogram_relationship',
    'kilogram_atomic_mass_unit_relationship',
    'kilogram_electron_volt_relationship',
    'kilogram_hartree_relationship',
    'kilogram_hertz_relationship',
    'kilogram_inverse_meter_relationship',
    'kilogram_joule_relationship',
    'kilogram_kelvin_relationship',
    'lattice_parameter_of_silicon',
    'lattice_spacing_of_ideal_si_220',
    'lattice_spacing_of_silicon',
    'loschmidt_constant_273_15_k_100_kpa',
    'loschmidt_constant_273_15_k_101_325_kpa',
    'luminous_efficacy',
    'mag_constant',
    'mag_flux_quantum',
    'magn_constant',
    'magn_flux_quantum',
    'mo_x_unit',
    'molar_gas_constant',
    'molar_mass_constant',
    'molar_mass_of_carbon_12',
    'molar_planck_constant',
    'molar_planck_constant_times_c',
    'molar_volume_of_ideal_gas_273_15_k_100_kpa',
    'molar_volume_of_ideal_gas_273_15_k_101_325_kpa',
    'molar_volume_of_silicon',
    'molybdenum_x_unit',
    'muon_compton_wavelength',
    'muon_compton_wavelength_over_2_pi',
    'muon_electron_mass_ratio',
    'muon_g_factor',
    'muon_mag_mom',
    'muon_mag_mom_anomaly',
    'muon_mag_mom_to_bohr_magneton_ratio',
    'muon_mag_mom_to_nuclear_magneton_ratio',
    'muon_magn_moment',
    'muon_magn_moment_to_bohr_magneton_ratio',
    'muon_magn_moment_to_nuclear_magneton_ratio',
    'muon_mass',
    'muon_mass_energy_equivalent',
    'muon_mass_energy_equivalent_in_mev',
    'muon_mass_in_u',
    'muon_molar_mass',
    'muon_neutron_mass_ratio',
    'muon_proton_mag_mom_ratio',
    'muon_proton_magn_moment_ratio',
    'muon_proton_mass_ratio',
    'muon_tau_mass_ratio',
    'natural_unit_of_action',
    'natural_unit_of_action_in_ev_s',
    'natural_unit_of_energy',
    'natural_unit_of_energy_in_mev',
    'natural_unit_of_length',
    'natural_unit_of_mass',
    'natural_unit_of_mom_um',
    'natural_unit_of_mom_um_in_mev_c',
    'natural_unit_of_momentum',
    'natural_unit_of_momentum_in_mev_c',
    'natural_unit_of_time',
    'natural_unit_of_velocity',
    'neutron_compton_wavelength',
    'neutron_compton_wavelength_over_2_pi',
    'neutron_electron_mag_mom_ratio',
    'neutron_electron_magn_moment_ratio',
    'neutron_electron_mass_ratio',
    'neutron_g_factor',
    'neutron_gyromag_ratio',
    'neutron_gyromag_ratio_in_mhz_t',
    'neutron_gyromag_ratio_over_2_pi',
    'neutron_gyromagn_ratio',
    'neutron_gyromagn_ratio_over_2_pi',
    'neutron_mag_mom',
    'neutron_mag_mom_to_bohr_magneton_ratio',
    'neutron_mag_mom_to_nuclear_magneton_ratio',
    'neutron_magn_moment',
    'neutron_magn_moment_to_bohr_magneton_ratio',
    'neutron_magn_moment_to_nuclear_magneton_ratio',
    'neutron_mass',
    'neutron_mass_energy_equivalent',
    'neutron_mass_energy_equivalent_in_mev',
    'neutron_mass_in_u',
    'neutron_molar_mass',
    'neutron_muon_mass_ratio',
    'neutron_proton_mag_mom_ratio',
    'neutron_proton_magn_moment_ratio',
    'neutron_proton_mass_difference',
    'neutron_proton_mass_difference_energy_equivalent',
    'neutron_proton_mass_difference_energy_equivalent_in_mev',
    'neutron_proton_mass_difference_in_u',
    'neutron_proton_mass_ratio',
    'neutron_relative_atomic_mass',
    'neutron_tau_mass_ratio',
    'neutron_to_shielded_proton_mag_mom_ratio',
    'neutron_to_shielded_proton_magn_moment_ratio',
    'newtonian_constant_of_gravitation',
    'newtonian_constant_of_gravitation_over_h_bar_c',
    'nuclear_magneton',
    'nuclear_magneton_in_ev_t',
    'nuclear_magneton_in_inverse_meter_per_tesla',
    'nuclear_magneton_in_inverse_meters_per_tesla',
    'nuclear_magneton_in_k_t',
    'nuclear_magneton_in_mhz_t',
    'planck',
    'planck_constant',
    'planck_constant_in_ev_hz',
    'planck_constant_in_ev_s',
    'planck_constant_over_2_pi',
    'planck_constant_over_2_pi_in_ev_s',
    'planck_constant_over_2_pi_times_c_in_mev_fm',
    'planck_length',
    'planck_mass',
    'planck_mass_energy_equivalent_in_gev',
    'planck_temperature',
    'planck_time',
    'proton_charge_to_mass_quotient',
    'proton_compton_wavelength',
    'proton_compton_wavelength_over_2_pi',
    'proton_electron_mass_ratio',
    'proton_g_factor',
    'proton_gyromag_ratio',
    'proton_gyromag_ratio_in_mhz_t',
    'proton_gyromag_ratio_over_2_pi',
    'proton_gyromagn_ratio',
    'proton_gyromagn_ratio_over_2_pi',
    'proton_mag_mom',
    'proton_mag_mom_to_bohr_magneton_ratio',
    'proton_mag_mom_to_nuclear_magneton_ratio',
    'proton_mag_shielding_correction',
    'proton_magn_moment',
    'proton_magn_moment_to_bohr_magneton_ratio',
    'proton_magn_moment_to_nuclear_magneton_ratio',
    'proton_magn_shielding_correction',
    'proton_mass',
    'proton_mass_energy_equivalent',
    'proton_mass_energy_equivalent_in_mev',
    'proton_mass_in_u',
    'proton_molar_mass',
    'proton_muon_mass_ratio',
    'proton_neutron_mag_mom_ratio',
    'proton_neutron_magn_moment_ratio',
    'proton_neutron_mass_ratio',
    'proton_relative_atomic_mass',
    'proton_rms_charge_radius',
    'proton_tau_mass_ratio',
    'quantum_of_circulation',
    'quantum_of_circulation_times_2',
    'reduced_compton_wavelength',
    'reduced_muon_compton_wavelength',
    'reduced_neutron_compton_wavelength',
    'reduced_planck_constant',
    'reduced_planck_constant_in_ev_s',
    'reduced_planck_constant_times_c_in_mev_fm',
    'reduced_proton_compton_wavelength',
    'reduced_tau_compton_wavelength',
    'rydberg_constant',
    'rydberg_constant_times_c_in_hz',
    'rydberg_constant_times_hc_in_ev',
    'rydberg_constant_times_hc_in_j',
    'sackur_tetrode_constant_1_k_100_kpa',
    'sackur_tetrode_constant_1_k_101_325_kpa',
    'second_radiation_constant',
    'shielded_helion_gyromag_ratio',
    'shielded_helion_gyromag_ratio_in_mhz_t',
    'shielded_helion_gyromag_ratio_over_2_pi',
    'shielded_helion_gyromagn_ratio',
    'shielded_helion_gyromagn_ratio_over_2_pi',
    'shielded_helion_mag_mom',
    'shielded_helion_mag_mom_to_bohr_magneton_ratio',
    'shielded_helion_mag_mom_to_nuclear_magneton_ratio',
    'shielded_helion_magn_moment',
    'shielded_helion_magn_moment_to_bohr_magneton_ratio',
    'shielded_helion_magn_moment_to_nuclear_magneton_ratio',
    'shielded_helion_to_proton_mag_mom_ratio',
    'shielded_helion_to_proton_magn_moment_ratio',
    'shielded_helion_to_shielded_proton_mag_mom_ratio',
    'shielded_helion_to_shielded_proton_magn_moment_ratio',
    'shielded_proton_gyromag_ratio',
    'shielded_proton_gyromag_ratio_in_mhz_t',
    'shielded_proton_gyromag_ratio_over_2_pi',
    'shielded_proton_mag_mom',
    'shielded_proton_mag_mom_to_bohr_magneton_ratio',
    'shielded_proton_mag_mom_to_nuclear_magneton_ratio',
    'shielded_proton_magn_moment',
    'shielded_proton_magn_moment_to_bohr_magneton_ratio',
    'shielded_proton_magn_moment_to_nuclear_magneton_ratio',
    'shielding_difference_of_d_and_p_in_hd',
    'shielding_difference_of_t_and_p_in_ht',
    'speed_of_light',
    'speed_of_light_in_vacuum',
    'standard_acceleration_of_gravity',
    'standard_atmosphere',
    'standard_state_pressure',
    'stefan_boltzmann_constant',
    'tau_compton_wavelength',
    'tau_compton_wavelength_over_2_pi',
    'tau_electron_mass_ratio',
    'tau_energy_equivalent',
    'tau_mass',
    'tau_mass_energy_equivalent',
    'tau_mass_energy_equivalent_in_mev',
    'tau_mass_in_u',
    'tau_molar_mass',
    'tau_muon_mass_ratio',
    'tau_neutron_mass_ratio',
    'tau_proton_mass_ratio',
    'thomson_cross_section',
    'triton_electron_mag_mom_ratio',
    'triton_electron_mass_ratio',
    'triton_g_factor',
    'triton_mag_mom',
    'triton_mag_mom_to_bohr_magneton_ratio',
    'triton_mag_mom_to_nuclear_magneton_ratio',
    'triton_mass',
    'triton_mass_energy_equivalent',
    'triton_mass_energy_equivalent_in_mev',
    'triton_mass_in_u',
    'triton_molar_mass',
    'triton_neutron_mag_mom_ratio',
    'triton_proton_mag_mom_ratio',
    'triton_proton_mass_ratio',
    'triton_relative_atomic_mass',
    'triton_to_proton_mag_mom_ratio',
    'unified_atomic_mass_unit',
    'vacuum_electric_permittivity',
    'vacuum_mag_permeability',
    'von_klitzing_constant',
    'w_to_z_mass_ratio',
    'weak_mixing_angle',
    'wien_displacement_law_constant',
    'wien_frequency_displacement_law_constant',
    'wien_wavelength_displacement_law_constant',
]
