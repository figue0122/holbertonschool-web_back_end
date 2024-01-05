#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies float by multiplier"""

    def mult(value: float) -> float:
        return value * multiplier

    return mult
