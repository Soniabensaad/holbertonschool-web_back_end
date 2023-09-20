#!/usr/bin/env python3
"""function make_multiplier
that takes a float multiplier
as argument and returns a function
that multiplies a float by multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a multiplier function."""

    def multiplier_function(x: float) -> float:
        """Inner function that multiplies x by the multiplier."""
        return x * multiplier
    return multiplier_function
