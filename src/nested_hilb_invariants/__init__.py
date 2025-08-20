"""
A SageMath package for verifying conjectures related to
invariants of nested Hilbert schemes of points on the plane.
"""

from .conjectures import (
    B,
    pExp,
    enum_nested,
    WT,
    WT_sum,
    calculate_A_side,
    calculate_B_side,
)

__all__ = [
    "B",
    "pExp",
    "enum_nested",
    "WT",
    "WT_sum",
    "calculate_A_side",
    "calculate_B_side",
]
