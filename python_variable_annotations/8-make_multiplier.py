#!/usr/bin/env python3
"""This module provides a function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def inner(x: float) -> float:
        return x * multiplier
    return inner
