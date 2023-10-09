#!/usr/bin/python3
"""Define a function that
returns true if objecct is
an instance of or false if otherwise"""


def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
