from sympy import *

s, t = symbols('h t')

H = 2*s**2/(s**2+4*s+4)

print(inverse_laplace_transform(H, s, t))
