"""Small SymPy helpers for matching algebraically equivalent answer forms."""

from __future__ import annotations

import sympy as sp


def expand_expr(expr: sp.Expr) -> sp.Expr:
    """
    Normalize, simplify, and expand a SymPy expression.

    Use when:
        An exam answer option is written in a different but equivalent form.

    Parameters:
        expr: SymPy expression.

    Returns:
        Simplified and expanded SymPy expression.

    Example:
        >>> t = sp.symbols("t", real=True)
        >>> expand_expr(sp.exp(t) * sp.exp(-t))
        1
    """
    expr_s = sp.sympify(expr)
    try:
        expr_s = expr_s.normal()
    except AttributeError:
        pass
    return sp.expand(sp.simplify(expr_s))


def same_after_expand(a: sp.Expr, b: sp.Expr) -> bool:
    """
    Check whether two expressions are equal after simplification/expansion.

    Use when:
        Two MCQ answer forms look different but may be algebraically equal.
    """
    return sp.simplify(expand_expr(a) - expand_expr(b)) == 0


if __name__ == "__main__":
    t = sp.symbols("t", real=True)
    a = ((2.0 * t - 4.0) * sp.exp(0.5 * t) + 4.0) * sp.exp(-0.5 * t) * sp.Heaviside(t)
    b = (2 * t - 4 + 4 * sp.exp(-0.5 * t)) * sp.Heaviside(t)
    print(same_after_expand(a, b))
