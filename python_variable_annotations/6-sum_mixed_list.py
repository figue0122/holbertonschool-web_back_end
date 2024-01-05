#!/usr/bin/env python3
"""Sum a mix of list and take it as sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of list of floats as float"""
    return sum(mxd_lst)
