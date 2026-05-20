"""Symbolic response helpers for rational transfer functions."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import sympy as sp

s, t = sp.symbols("s t", real=True)


def _poly_from_coeffs(coeffs: Sequence[float | int | sp.Expr]) -> sp.Expr:
    if len(coeffs) == 0:
        raise ValueError("Coefficient sequence must not be empty.")
    degree = len(coeffs) - 1
    return sp.expand(sum(sp.sympify(c) * s ** (degree - i) for i, c in enumerate(coeffs)))


def inverse_laplace_rational_expr(expr: sp.Expr) -> sp.Expr:
    """Return inverse unilateral Laplace transform of a rational expression."""
    return sp.simplify(sp.inverse_laplace_transform(sp.apart(sp.sympify(expr), s), s, t))


def impulse_response_from_transfer(num: Sequence[float | int | sp.Expr], den: Sequence[float | int | sp.Expr]) -> sp.Expr:
    """
    Compute h(t) = L^-1{H(s)} for a rational transfer function.

    Inputs are coefficients in descending powers of s.
    """
    numerator = _poly_from_coeffs(num)
    denominator = _poly_from_coeffs(den)
    if sp.Poly(denominator, s).degree() < 1:
        raise ValueError("Denominator must have positive degree.")
    return inverse_laplace_rational_expr(numerator / denominator)


def step_response_from_transfer(num: Sequence[float | int | sp.Expr], den: Sequence[float | int | sp.Expr]) -> sp.Expr:
    """Compute y_step(t) = L^-1{H(s)/s}."""
    numerator = _poly_from_coeffs(num)
    denominator = _poly_from_coeffs(den)
    return inverse_laplace_rational_expr(numerator / (denominator * s))


def ramp_response_from_transfer(num: Sequence[float | int | sp.Expr], den: Sequence[float | int | sp.Expr]) -> sp.Expr:
    """Compute y_ramp(t) = L^-1{H(s)/s^2}."""
    numerator = _poly_from_coeffs(num)
    denominator = _poly_from_coeffs(den)
    return inverse_laplace_rational_expr(numerator / (denominator * s**2))


def related_unit_responses(response: sp.Expr, known: str) -> dict[str, sp.Expr]:
    """
    Return impulse, step, and ramp responses from one known causal unit response.

    known must be one of "impulse", "step", or "ramp". The input expression is
    interpreted as a zero-state continuous-time LTIC response in t.
    """
    aliases = {
        "h": "impulse",
        "impulse": "impulse",
        "impuls": "impulse",
        "step": "step",
        "trin": "step",
        "ramp": "ramp",
        "rampe": "ramp",
    }
    kind = aliases.get(known.lower())
    if kind is None:
        raise ValueError("known must be one of impulse, step, or ramp.")

    expr = sp.sympify(response)
    transform = sp.laplace_transform(expr, t, s, noconds=True)
    if kind == "impulse":
        H = transform
    elif kind == "step":
        H = s * transform
    else:
        H = s**2 * transform

    return {
        "impulse": inverse_laplace_rational_expr(H),
        "step": inverse_laplace_rational_expr(H / s),
        "ramp": inverse_laplace_rational_expr(H / s**2),
    }


def zero_input_laplace_second_order(a1: float | int | sp.Expr, a0: float | int | sp.Expr, y0: float | int | sp.Expr, yd0: float | int | sp.Expr) -> sp.Expr:
    """
    Return Y_zi(s) for y'' + a1*y' + a0*y = 0 with y(0-)=y0, y'(0-)=yd0.
    """
    a1s = sp.sympify(a1)
    a0s = sp.sympify(a0)
    y0s = sp.sympify(y0)
    yd0s = sp.sympify(yd0)
    return sp.simplify((s * y0s + yd0s + a1s * y0s) / (s**2 + a1s * s + a0s))


def transfer_from_ode(num: Sequence[float | int | sp.Expr], den: Sequence[float | int | sp.Expr]) -> dict[str, Any]:
    """Return symbolic H(s), zeros, and poles from coefficient lists."""
    numerator = _poly_from_coeffs(num)
    denominator = _poly_from_coeffs(den)
    num_poly = sp.Poly(numerator, s)
    den_poly = sp.Poly(denominator, s)
    return {
        "H": sp.simplify(numerator / denominator),
        "zeros": sp.nroots(num_poly) if num_poly.degree() > 0 else [],
        "poles": sp.nroots(den_poly),
    }


def poly_from_derivative_coeffs(coeffs: Sequence[float | int | sp.Expr]) -> sp.Expr:
    """
    Return a polynomial from ascending derivative coefficients.

    ``[a0, a1, a2]`` means ``a0*y + a1*y' + a2*y''`` and maps to
    ``a0 + a1*s + a2*s**2``.
    """
    if len(coeffs) == 0:
        raise ValueError("Coefficient sequence must not be empty.")
    return sp.expand(sum(sp.sympify(coeffs[k]) * s**k for k in range(len(coeffs))))


def initial_term_from_lhs(
    a_coeffs: Sequence[float | int | sp.Expr],
    y_ics: Sequence[float | int | sp.Expr],
) -> sp.Expr:
    """
    Compute the unilateral Laplace initial-condition term from Q(D)y.

    ``y_ics`` is ``[y(0), y'(0), y''(0), ...]``. For example
    ``y'' + a1*y' + a0*y`` gives ``(s + a1)*y(0) + y'(0)``.
    """
    initial_term = 0
    for k in range(1, len(a_coeffs)):
        a_k = sp.sympify(a_coeffs[k])
        for r in range(k):
            if r < len(y_ics):
                initial_term += a_k * s ** (k - 1 - r) * sp.sympify(y_ics[r])
    return sp.simplify(initial_term)


def choose_initial_conditions(
    *,
    y0_minus: Sequence[float | int | sp.Expr] | None = None,
    y0_plus: Sequence[float | int | sp.Expr] | None = None,
) -> tuple[Sequence[float | int | sp.Expr], str]:
    """Use 0+ initial values when supplied; otherwise use 0- or zeros."""
    if y0_plus is not None:
        return y0_plus, "0+"
    if y0_minus is not None:
        return y0_minus, "0-"
    return [], "0- assumed zero"


def has_dirac_at_zero(time_expr: sp.Expr | None) -> bool:
    """Return True when a time expression contains a DiracDelta located at t=0."""
    if time_expr is None:
        return False
    for delta in time_expr.atoms(sp.DiracDelta):
        arg = delta.args[0]
        try:
            roots = sp.solve(sp.Eq(arg, 0), t)
            if any(sp.simplify(root) == 0 for root in roots):
                return True
        except Exception:
            try:
                if sp.simplify(arg.subs(t, 0)) == 0:
                    return True
            except Exception:
                pass
    return False


def rhs_time_expr(b_coeffs: Sequence[float | int | sp.Expr], x_expr: sp.Expr | None) -> sp.Expr | None:
    """Form P(D)x(t) from ascending RHS derivative coefficients."""
    if x_expr is None:
        return None
    return sp.simplify(sum(sp.sympify(b_k) * sp.diff(x_expr, t, k) for k, b_k in enumerate(b_coeffs)))


def rhs_has_impulse_at_zero(
    b_coeffs: Sequence[float | int | sp.Expr],
    *,
    x_expr: sp.Expr | None = None,
    X_s: sp.Expr | None = None,
) -> bool | None:
    """Best-effort check for an impulse at t=0 on the RHS."""
    if x_expr is not None:
        return has_dirac_at_zero(rhs_time_expr(b_coeffs, x_expr))
    if X_s is not None:
        rhs_s = sp.together(sp.simplify(poly_from_derivative_coeffs(b_coeffs) * X_s))
        num, den = sp.fraction(rhs_s)
        try:
            deg_num = sp.degree(num, s)
            deg_den = sp.degree(den, s)
            if deg_num is None or deg_den is None:
                return None
            return deg_num >= deg_den
        except Exception:
            return None
    return None


def proper_rational_check(F_s: sp.Expr) -> bool | None:
    """Return True when F(s) is strictly proper."""
    F_s = sp.together(sp.simplify(F_s))
    num, den = sp.fraction(F_s)
    try:
        deg_num = sp.degree(num, s)
        deg_den = sp.degree(den, s)
        if deg_num is None or deg_den is None:
            return None
        return deg_num < deg_den
    except Exception:
        return None


def final_value_allowed(F_s: sp.Expr) -> bool | None:
    """
    Check the standard final-value theorem pole condition for s*F(s).

    Returns None when symbolic poles cannot be classified.
    """
    expr = sp.together(sp.simplify(s * F_s))
    _, den = sp.fraction(expr)
    try:
        pole_dict = sp.roots(den, s)
        zero_pole_count = 0
        for pole, mult in pole_dict.items():
            pole = sp.simplify(pole)
            if pole == 0:
                zero_pole_count += mult
                if zero_pole_count > 1:
                    return False
                continue
            if complex(sp.N(pole)).real >= 0:
                return False
        return True
    except Exception:
        return None


def initial_final_values(F_s: sp.Expr, *, time_expr: sp.Expr | None = None) -> dict[str, Any]:
    """Return initial/final values plus flags explaining whether the tests apply."""
    proper = proper_rational_check(F_s)
    contains_dirac = has_dirac_at_zero(time_expr)
    final_allowed = final_value_allowed(F_s)
    initial_value = None
    final_value = None

    if not contains_dirac and proper is not False:
        try:
            candidate = sp.limit(s * F_s, s, sp.oo)
            if candidate not in [sp.oo, -sp.oo, sp.zoo] and not candidate.has(sp.oo, -sp.oo, sp.zoo):
                initial_value = sp.simplify(candidate)
        except Exception:
            initial_value = None

    if final_allowed is not False:
        try:
            candidate = sp.limit(s * F_s, s, 0)
            if candidate not in [sp.oo, -sp.oo, sp.zoo] and not candidate.has(sp.oo, -sp.oo, sp.zoo):
                final_value = sp.simplify(candidate)
        except Exception:
            final_value = None

    return {
        "initial_value": initial_value,
        "final_value": final_value,
        "proper": proper,
        "contains_dirac_at_zero": contains_dirac,
        "final_value_allowed": final_allowed,
    }


def zero_state_zero_input(
    a_coeffs: Sequence[float | int | sp.Expr],
    b_coeffs: Sequence[float | int | sp.Expr],
    *,
    y0_minus: Sequence[float | int | sp.Expr] | None = None,
    y0_plus: Sequence[float | int | sp.Expr] | None = None,
    x_expr: sp.Expr | None = None,
    X_s: sp.Expr | None = None,
    show_time: bool = True,
) -> dict[str, Any]:
    """
    Solve zero-state and zero-input responses for Q(D)y(t) = P(D)x(t).

    Coefficients are in ascending derivative order:
        a_coeffs=[a0, a1, a2] means a0*y + a1*y' + a2*y''.
        b_coeffs=[b0, b1] means b0*x + b1*x'.

    Use either ``y0_minus`` with the full input, or ``y0_plus`` with the input
    after any impulse at t=0 has already been accounted for.
    """
    Q_s = poly_from_derivative_coeffs(a_coeffs)
    P_s = poly_from_derivative_coeffs(b_coeffs)
    H_s = sp.simplify(P_s / Q_s)

    if X_s is None:
        X_s = sp.Integer(0) if x_expr is None else sp.laplace_transform(x_expr, t, s, noconds=True)
    else:
        X_s = sp.sympify(X_s)

    y_ics, ic_used = choose_initial_conditions(y0_minus=y0_minus, y0_plus=y0_plus)
    I_s = initial_term_from_lhs(a_coeffs, y_ics)

    Y_zs = sp.simplify(H_s * X_s)
    Y_zi = sp.simplify(I_s / Q_s)
    Y_total = sp.simplify(Y_zs + Y_zi)

    y_zs_t = None
    y_zi_t = None
    y_total_t = None
    if show_time:
        y_zs_t = sp.inverse_laplace_transform(Y_zs, s, t)
        y_zi_t = sp.inverse_laplace_transform(Y_zi, s, t)
        y_total_t = sp.simplify(y_zs_t + y_zi_t)

    impulse_at_zero = rhs_has_impulse_at_zero(b_coeffs, x_expr=x_expr, X_s=X_s)

    return {
        "Q_s": Q_s,
        "P_s": P_s,
        "H_s": H_s,
        "X_s": X_s,
        "I_s": I_s,
        "laplace_equation": sp.Eq(Q_s * sp.Symbol("Y"), P_s * sp.Symbol("X") + I_s),
        "Y_zs": Y_zs,
        "Y_zi": Y_zi,
        "Y_total": Y_total,
        "y_zs_t": y_zs_t,
        "y_zi_t": y_zi_t,
        "y_total_t": y_total_t,
        "initial_final": {
            "zero_state": initial_final_values(Y_zs, time_expr=y_zs_t),
            "zero_input": initial_final_values(Y_zi, time_expr=y_zi_t),
            "total": initial_final_values(Y_total, time_expr=y_total_t),
        },
        "ic_used": ic_used,
        "impulse_at_zero": impulse_at_zero,
        "warning": (
            "Using 0+ initial values while the RHS appears to contain an impulse at t=0 can double-count the impulse."
            if y0_plus is not None and impulse_at_zero is True
            else None
        ),
    }
