"""Fourier transform property helpers for e^(-a t)u(t)."""

from __future__ import annotations

import sympy as sp

omega = sp.symbols("omega", real=True)


def exponential_transform_variant(a: float | int | sp.Expr, *, time_scale: float | int | sp.Expr = 1, modulation: float | int | sp.Expr = 0) -> sp.Expr:
    """
    Transform of e^(-a*time_scale*t)u(time_scale*t) multiplied by exp(j*modulation*t).

    For positive time_scale, x(time_scale*t)e^(j*modulation*t) maps to
    (1/time_scale) * X((omega - modulation)/time_scale).
    """
    a_s = sp.sympify(a)
    scale = sp.sympify(time_scale)
    mod = sp.sympify(modulation)
    if scale <= 0:
        raise ValueError("Only positive time_scale is supported for exam use.")
    if a_s <= 0:
        raise ValueError("a must be positive for e^(-a t)u(t) to be absolutely integrable.")
    return sp.simplify((1 / scale) * 1 / (a_s + sp.I * ((omega - mod) / scale)))
