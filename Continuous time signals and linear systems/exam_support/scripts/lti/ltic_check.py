"""Symbolic LTIC checks for differential equations."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import sympy as sp

t = sp.symbols("t", real=True)
x = sp.Function("x")
y = sp.Function("y")


def _signal_derivative_terms(expr: sp.Expr, funcs: Sequence[sp.Function]) -> list[sp.Expr]:
    terms: list[sp.Expr] = []
    for f in funcs:
        base = f(t)
        if expr.has(base):
            terms.append(base)
        for derivative in expr.atoms(sp.Derivative):
            if derivative.expr == base and all(var == t for var in derivative.variables):
                terms.append(derivative)

    unique_terms: list[sp.Expr] = []
    for term in terms:
        if term not in unique_terms:
            unique_terms.append(term)
    return unique_terms


def _make_dummy_substitution(terms: Sequence[sp.Expr]) -> dict[sp.Expr, sp.Symbol]:
    mapping: dict[sp.Expr, sp.Symbol] = {}
    for term in terms:
        if isinstance(term, sp.Derivative):
            base = term.expr
            order = len(term.variables)
        else:
            base = term
            order = 0
        mapping[term] = sp.Symbol(f"{base.func}{order}")
    return mapping


def _find_shifted_inputs(expr: sp.Expr, input_func: sp.Function) -> list[tuple[sp.Expr, sp.Expr, sp.Expr]]:
    shifted = []
    for atom in expr.atoms(sp.Function):
        if atom.func == input_func:
            arg = atom.args[0]
            shifted.append((atom, arg, sp.simplify(arg - t)))
    return shifted


def _causality_check(expr: sp.Expr, input_func: sp.Function) -> tuple[bool | None, list[sp.Expr], list[sp.Expr], list[sp.Expr]]:
    future_inputs: list[sp.Expr] = []
    delayed_inputs: list[sp.Expr] = []
    uncertain_inputs: list[sp.Expr] = []

    for atom, arg, shift in _find_shifted_inputs(expr, input_func):
        if shift == 0:
            continue
        if sp.simplify(sp.diff(arg, t)) != 1:
            uncertain_inputs.append(atom)
            continue
        try:
            shift_num = float(sp.N(shift))
        except Exception:
            uncertain_inputs.append(atom)
            continue
        if shift_num > 0:
            future_inputs.append(atom)
        elif shift_num < 0:
            delayed_inputs.append(atom)

    if future_inputs:
        return False, future_inputs, delayed_inputs, uncertain_inputs
    if uncertain_inputs:
        return None, future_inputs, delayed_inputs, uncertain_inputs
    return True, future_inputs, delayed_inputs, uncertain_inputs


def ltic_check(
    eq: sp.Eq,
    *,
    input_func: sp.Function = x,
    output_func: sp.Function = y,
    show_details: bool = False,
) -> dict[str, Any]:
    """
    Check whether a symbolic differential equation is linear, time-invariant and causal.

    Example:
        eq = sp.Eq(sp.diff(y(t), t, 2) + sp.diff(y(t), t) + 5*y(t), x(t))
        ltic_check(eq)

    The causality check is intentionally simple: future inputs such as x(t+a)
    are marked non-causal, delayed inputs x(t-a) are allowed, and nonlinear
    time arguments such as x(2*t) are marked uncertain.
    """
    if not isinstance(eq, sp.Equality):
        raise TypeError("eq must be a SymPy Eq.")

    expr = sp.simplify(eq.lhs - eq.rhs)
    terms = _signal_derivative_terms(expr, funcs=[input_func, output_func])
    mapping = _make_dummy_substitution(terms)
    expr_dummy = expr.xreplace(mapping)
    variables = list(mapping.values())

    try:
        poly = sp.Poly(expr_dummy, *variables, domain="EX")
        zero_test = sp.simplify(expr_dummy.subs({var: 0 for var in variables}))
        is_linear = poly.total_degree() <= 1 and zero_test == 0
    except Exception:
        is_linear = False

    if is_linear:
        time_varying_coeffs = []
        for var in variables:
            coeff = sp.simplify(sp.diff(expr_dummy, var))
            if coeff.has(t):
                time_varying_coeffs.append((var, coeff))
        is_time_invariant = len(time_varying_coeffs) == 0
    else:
        time_varying_coeffs = []
        is_time_invariant = None

    is_causal, future_inputs, delayed_inputs, uncertain_inputs = _causality_check(expr, input_func)
    is_ltic = is_linear is True and is_time_invariant is True and is_causal is True

    result = {
        "linear": is_linear,
        "time_invariant": is_time_invariant,
        "causal": is_causal,
        "ltic": is_ltic,
        "expr_zero_form": expr,
        "dummy_expr": expr_dummy,
        "substitution": mapping,
        "time_varying_coeffs": time_varying_coeffs,
        "future_inputs": future_inputs,
        "delayed_inputs": delayed_inputs,
        "uncertain_inputs": uncertain_inputs,
    }

    if show_details:
        print("LTIC check")
        print(f"Linear: {is_linear}")
        print(f"Time invariant: {is_time_invariant}")
        print(f"Causal: {is_causal}")
        print(f"LTIC: {is_ltic}")

    return result
