#!/usr/bin/env python3
"""function sum_list which takes a list input_list of floats as argument
and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list """
    return sum(x for x in input_list)
