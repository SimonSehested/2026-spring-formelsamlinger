"""Laplace transform wrappers."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lti.responses import impulse_response_from_transfer


def inverse_laplace_rational(num: Sequence[float | int | sp.Expr], den: Sequence[float | int | sp.Expr]) -> sp.Expr:
    """
    Inverse Laplace transform of num(s)/den(s).

    Inputs are coefficient lists in descending powers of s.
    """
    return impulse_response_from_transfer(num, den)

