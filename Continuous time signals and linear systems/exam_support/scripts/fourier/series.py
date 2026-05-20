"""Fourier series coefficient helpers."""

from __future__ import annotations

from collections.abc import Iterable

import sympy as sp


def complex_fourier_coefficients(expr: sp.Expr, var: sp.Symbol, period: float | int | sp.Expr, n_values: Iterable[int], *, t_start: float | int | sp.Expr = 0) -> dict[int, sp.Expr]:
    """
    Compute complex Fourier coefficients D_n over [t_start, t_start + period].
    """
    T = sp.sympify(period)
    if T <= 0:
        raise ValueError("period must be positive.")
    start = sp.sympify(t_start)
    omega0 = 2 * sp.pi / T
    x = sp.sympify(expr)
    return {
        int(n): sp.simplify((1 / T) * sp.integrate(x * sp.exp(-sp.I * int(n) * omega0 * var), (var, start, start + T)))
        for n in n_values
    }
