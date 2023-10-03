#!/usr/bin/python3
"""Add integers"""


def add_integer(a, b=98):
    """add_integer - adds an integer
    Args:
        a:  first argument
        b:  second argument
    
    Return:
        result: integer
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    
    return int(a) + int(b)
