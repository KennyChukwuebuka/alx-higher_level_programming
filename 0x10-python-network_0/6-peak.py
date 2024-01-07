#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers.
-Prototype: def find_peak(list_of_integers):
-You are not allowed to import any module
-Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
"""


def find_peak(list_of_integers):
    """returns a peak in a list of unsorted integers"""
    if list_of_integers:
        return max(list_of_integers)
    return None
