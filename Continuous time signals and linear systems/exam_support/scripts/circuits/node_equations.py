"""Node-equation helpers for Laplace-domain circuit tasks."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import sympy as sp

s = sp.symbols("s", real=True)


def _clean_rational(expr: sp.Expr, s_symbol: sp.Symbol) -> sp.Expr:
    expr_s = sp.together(sp.simplify(sp.sympify(expr)))
    num, den = sp.fraction(expr_s)
    return sp.collect(sp.expand(num), s_symbol) / sp.collect(sp.expand(den), s_symbol)


def solve_node_circuit(
    equations: Sequence[sp.Eq | sp.Expr],
    nodes: Sequence[sp.Symbol],
    input_signal: sp.Symbol | None = None,
    output_node: sp.Symbol | None = None,
    s_symbol: sp.Symbol = s,
) -> dict[str, Any]:
    """
    Solve Laplace-domain node equations and optionally form a transfer function.

    Use when:
        A circuit task gives KCL node equations in the s-domain.

    Parameters:
        equations: SymPy equations. Expressions are interpreted as equal to 0.
        nodes: Unknown node-voltage symbols to solve for.
        input_signal: Known input symbol, e.g. V1.
        output_node: Desired output node, e.g. VB.
        s_symbol: Laplace variable.

    Returns:
        Dictionary with solved node voltages and, when requested, transfer data:
        H, numerator, denominator, numerator_coeffs, denominator_coeffs,
        laplace_equation, differential_equation.

    Assumptions:
        Equations are linear in the node variables and written in the Laplace
        domain. Initial conditions are not included unless manually present in
        the equations.
    """
    if not equations:
        raise ValueError("equations must not be empty.")
    if not nodes:
        raise ValueError("nodes must not be empty.")

    normalized_equations = [eq if isinstance(eq, sp.Equality) else sp.Eq(eq, 0) for eq in equations]
    sol_list = sp.solve(normalized_equations, list(nodes), dict=True)
    if not sol_list:
        raise ValueError("No solution found for the supplied node equations.")

    raw_solution = sol_list[0]
    node_voltages = {
        node: _clean_rational(raw_solution[node], s_symbol)
        for node in nodes
        if node in raw_solution
    }

    result: dict[str, Any] = {
        "node_voltages": node_voltages,
        "raw_solution": raw_solution,
        "H": None,
        "numerator": None,
        "denominator": None,
        "numerator_coeffs": None,
        "denominator_coeffs": None,
        "laplace_equation": None,
        "differential_equation": None,
    }

    if input_signal is None or output_node is None:
        return result
    if output_node not in raw_solution:
        raise ValueError(f"{output_node} was not solved.")

    H = _clean_rational(raw_solution[output_node] / input_signal, s_symbol)
    numerator, denominator = sp.fraction(sp.together(H))
    numerator = sp.collect(sp.expand(numerator), s_symbol)
    denominator = sp.collect(sp.expand(denominator), s_symbol)

    num_poly = sp.Poly(numerator, s_symbol)
    den_poly = sp.Poly(denominator, s_symbol)
    X, Y = sp.symbols("X Y")
    x = sp.Function("x")
    y = sp.Function("y")
    tau = sp.symbols("t", real=True)
    lhs_time = _poly_to_derivative_expr(denominator, Y, y(tau), tau, s_symbol)
    rhs_time = _poly_to_derivative_expr(numerator, X, x(tau), tau, s_symbol)

    result.update(
        {
            "H": numerator / denominator,
            "numerator": numerator,
            "denominator": denominator,
            "numerator_coeffs": num_poly.all_coeffs(),
            "denominator_coeffs": den_poly.all_coeffs(),
            "laplace_equation": sp.Eq(denominator * Y, numerator * X),
            "differential_equation": sp.Eq(lhs_time, rhs_time),
        }
    )
    return result


def _poly_to_derivative_expr(
    poly_expr: sp.Expr,
    laplace_symbol: sp.Symbol,
    time_func: sp.Expr,
    time_symbol: sp.Symbol,
    s_symbol: sp.Symbol,
) -> sp.Expr:
    """Map a polynomial in s times X/Y to a time-domain derivative expression."""
    poly = sp.Poly(sp.expand(poly_expr), s_symbol)
    out = 0
    for (power,), coeff in poly.terms():
        if power == 0:
            out += coeff * time_func
        else:
            out += coeff * sp.diff(time_func, time_symbol, power)
    return sp.simplify(out)
