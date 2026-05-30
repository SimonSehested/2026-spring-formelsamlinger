"""Symbolic helpers for gain-dependent characteristic-equation stability."""

from __future__ import annotations

import sympy as sp


s = sp.Symbol("s")


def characteristic_from_open_loop(open_loop: sp.Expr, gain: sp.Symbol, s: sp.Symbol) -> sp.Expr:
    """Returner karakteristisk polynomium for unity-feedback: 1 + gain*G(s) = 0.

    Hvis open_loop allerede indeholder gain, bruges 1 + open_loop = 0.
    Hvis open_loop ikke indeholder gain, bruges 1 + gain*open_loop = 0.
    """
    open_loop = sp.sympify(open_loop)

    # Undgå at gange med gain to gange, hvis brugeren allerede har skrevet K*G.
    loop_expr = open_loop if gain in open_loop.free_symbols else gain * open_loop

    numerator, denominator = sp.fraction(sp.cancel(sp.together(1 + loop_expr)))
    return sp.expand(numerator)


def prepare_characteristic(
    expression: sp.Expr,
    gain: sp.Symbol,
    s: sp.Symbol,
    is_characteristic: int | bool = 1,
) -> sp.Expr:
    """Vælg hvordan input skal fortolkes.

    is_characteristic = 1: expression er allerede det karakteristiske polynomium.
    is_characteristic = 0: expression er en åben-sløjfe transferfunktion G(s), og
                           karakteristisk polynomium findes fra 1 + K*G(s) = 0.
    """
    if is_characteristic in (1, True):
        return sp.expand(sp.sympify(expression))
    if is_characteristic in (0, False):
        return characteristic_from_open_loop(expression, gain, s)

    raise ValueError("is_characteristic skal være 1/True eller 0/False.")


def find_stable_gain_ranges(
    expression: sp.Expr,
    gain: sp.Symbol,
    s: sp.Symbol,
    is_characteristic: int | bool = 1,
    omega: sp.Symbol | None = None,
    tolerance: float = 1e-9,
) -> dict[str, object]:
    """Find stabile reelle gain-intervaller.

    Brug enten:
      find_stable_gain_ranges(p, K, s, 1)  # p er karakteristisk polynomium
      find_stable_gain_ranges(G, K, s, 0)  # G er åben-sløjfe transferfunktion

    Ved rationalt input samles udtrykket, og tælleren bruges som polynomium.
    """
    if not isinstance(gain, sp.Symbol) or gain.is_real is not True:
        raise ValueError("gain must be a SymPy symbol declared real=True.")
    if not isinstance(s, sp.Symbol):
        raise ValueError("s must be a SymPy symbol.")
    if tolerance <= 0:
        raise ValueError("tolerance must be positive.")

    frequency = omega if omega is not None else sp.Symbol("omega", real=True)
    if not isinstance(frequency, sp.Symbol) or frequency.is_real is not True:
        raise ValueError("omega must be a SymPy symbol declared real=True.")
    if gain == s or gain == frequency or s == frequency:
        raise ValueError("gain, s and omega must be different symbols.")

    input_expression = sp.sympify(expression)
    characteristic = prepare_characteristic(input_expression, gain, s, is_characteristic)

    unexpected_symbols = characteristic.free_symbols - {s, gain}
    if unexpected_symbols:
        raise ValueError("characteristic may only contain s, gain and numeric constants.")

    combined_expression = sp.cancel(sp.together(characteristic))
    numerator, denominator = sp.fraction(combined_expression)
    characteristic_polynomial = sp.expand(numerator)

    try:
        polynomial = sp.Poly(characteristic_polynomial, s)
    except sp.PolynomialError as exc:
        raise ValueError("characteristic must reduce to a polynomial numerator in s.") from exc

    if polynomial.degree() < 1:
        raise ValueError("characteristic must have positive degree in s.")
    if gain in polynomial.LC().free_symbols:
        raise ValueError("The leading coefficient may not depend on gain.")

    boundary = sp.expand(characteristic_polynomial.subs(s, sp.I * frequency))
    real_equation = sp.simplify(sp.re(boundary))
    imaginary_equation = sp.simplify(sp.im(boundary))
    solutions = sp.solve([real_equation, imaginary_equation], [gain, frequency], dict=True)

    boundary_points: list[dict[str, sp.Expr]] = []
    for solution in solutions:
        if gain not in solution or frequency not in solution:
            continue
        gain_value = sp.simplify(solution[gain])
        omega_value = sp.simplify(solution[frequency])
        if (
            gain_value.free_symbols
            or omega_value.free_symbols
            or gain_value.is_real is not True
            or omega_value.is_real is not True
        ):
            continue
        point = {"gain": gain_value, "omega": omega_value}
        if point not in boundary_points:
            boundary_points.append(point)

    boundary_points.sort(
        key=lambda point: (float(sp.N(point["gain"])), float(sp.N(point["omega"])))
    )
    boundary_gains = sorted(
        {point["gain"] for point in boundary_points}, key=lambda value: float(sp.N(value))
    )

    endpoints = [-sp.oo, *boundary_gains, sp.oo]
    tested_intervals: list[dict[str, object]] = []
    stable_gain_intervals: list[sp.Set] = []

    for lower, upper in zip(endpoints, endpoints[1:]):
        if lower is -sp.oo and upper is sp.oo:
            sample_gain = sp.Integer(0)
        elif lower is -sp.oo:
            sample_gain = upper - 1
        elif upper is sp.oo:
            sample_gain = lower + 1
        else:
            sample_gain = sp.simplify((lower + upper) / 2)

        sample_polynomial = sp.Poly(characteristic_polynomial.subs(gain, sample_gain), s)
        roots = [complex(root) for root in sample_polynomial.nroots()]
        stable = all(root.real < -tolerance for root in roots)
        interval = sp.Interval.open(lower, upper)

        tested_intervals.append(
            {
                "interval": interval,
                "sample_gain": sample_gain,
                "poles": roots,
                "stable": stable,
            }
        )
        if stable:
            stable_gain_intervals.append(interval)

    positive_domain = sp.Interval.open(0, sp.oo)
    positive_stable_intervals = [
        interval.intersect(positive_domain)
        for interval in stable_gain_intervals
        if interval.intersect(positive_domain) != sp.S.EmptySet
    ]

    return {
        "input_expression": input_expression,
        "input_was_characteristic": bool(is_characteristic),
        "characteristic": characteristic_polynomial,
        "discarded_denominator": denominator,
        "boundary_expression": boundary,
        "boundary_equations": [real_equation, imaginary_equation],
        "boundary_points": boundary_points,
        "boundary_gains": boundary_gains,
        "tested_intervals": tested_intervals,
        "stable_gain_intervals": stable_gain_intervals,
        "positive_stable_gain_intervals": positive_stable_intervals,
    }


if __name__ == "__main__":
    s, K = sp.symbols("s K", real=True)
    G = (s + 1) / (s**2 + 43*s - 90)

    # 0 betyder: G er IKKE det karakteristiske polynomium.
    result_from_G = find_stable_gain_ranges(G, K, s, 0)
    print("Karakteristisk polynomium fra G:", result_from_G["characteristic"])
    print("Stabile positive K-intervaller:", result_from_G["positive_stable_gain_intervals"])

    # 1 betyder: p ER allerede det karakteristiske polynomium.
    p = K*(s + 1) + s**2 + 43*s - 90
    result_from_p = find_stable_gain_ranges(p, K, s, 1)
    print("Karakteristisk polynomium fra p:", result_from_p["characteristic"])
    print("Stabile positive K-intervaller:", result_from_p["positive_stable_gain_intervals"])


def solve_stability_interval_by_boundary(
    char_poly: sp.Expr, gain_symbol: sp.Symbol, variable: sp.Symbol = s
) -> dict[str, object]:
    """Find stable gain intervals using symbolic imaginary-axis boundaries.

    This compact interface mirrors the boundary-test workflow used in exam
    calculations. Declare ``gain_symbol`` with ``real=True``.
    """
    analysis = find_stable_gain_ranges(char_poly, gain_symbol, variable)
    omega = next(
        iter(
            (
                symbol
                for equation in analysis["boundary_equations"]
                for symbol in equation.free_symbols
                if symbol not in {gain_symbol, variable}
            )
        ),
        sp.Symbol("omega", real=True),
    )
    boundary_points = [
        {gain_symbol: point["gain"], omega: point["omega"]}
        for point in analysis["boundary_points"]
    ]
    return {
        "characteristic": analysis["characteristic"],
        "boundary_expression": analysis["boundary_expression"],
        "boundary_equations": analysis["boundary_equations"],
        "boundary_points": boundary_points,
        "boundary_gains": analysis["boundary_gains"],
        "tested_intervals": analysis["tested_intervals"],
        "stable_gain_intervals": analysis["stable_gain_intervals"],
    }
