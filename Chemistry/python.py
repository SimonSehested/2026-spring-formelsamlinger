from sympy import *
import sympy.physics.units as spp

print((spp.planck * spp.speed_of_light / (501 * spp.nanometer)).evalf())
