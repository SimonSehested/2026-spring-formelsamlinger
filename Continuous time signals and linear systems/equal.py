from sympy import *

R1, R2, C1, s, t = symbols("R1, R2, C1, s, t")

num_a = ((2.0*t - 4.0)*exp(0.5*t) + 4.0)*exp(-0.5*t)*Heaviside(t)
den_a = 1

num_b = (2*t - 4 + 4 * exp(-0.5*t)) * Heaviside(t)
den_b = 1

a = num_a / den_a
b = num_b / den_b

a = a.normal()
a = a.simplify()
a = a.expand()

b = b.normal()
b = b.simplify()
b = b.expand()

equal = a == b

print(equal)
