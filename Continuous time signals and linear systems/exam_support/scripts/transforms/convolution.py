"""Convolution helpers for causal symbolic signals."""

from __future__ import annotations

import sympy as sp

t, s = sp.symbols("t s", real=True)


def convolve_causal(x1: sp.Expr, x2: sp.Expr) -> sp.Expr:
    """
    Convolve causal signals x1(t)u(t) and x2(t)u(t).

    Parameters:
        x1, x2: SymPy expressions in t without the final Heaviside factor.

    Returns:
        SymPy expression for (x1*u) * (x2*u), including Heaviside(t).
    """
    x1s = sp.sympify(x1)
    x2s = sp.sympify(x2)
    x1_l = sp.laplace_transform(x1s * sp.Heaviside(t), t, s, noconds=True)
    x2_l = sp.laplace_transform(x2s * sp.Heaviside(t), t, s, noconds=True)
    return sp.simplify(sp.inverse_laplace_transform(sp.apart(x1_l * x2_l, s), s, t))
