#!/usr/bin/env python3
"""function sum_mixed_list which takes a list mxd_lst of integers and floats
and returns their sum as a float."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to sum a list of mixed integers and floats."""
    total = 0.0  # Initialize the total as a float
    for x in mxd_lst:
        total += float(x)  # Convert each element to a float and add to total
    return total

