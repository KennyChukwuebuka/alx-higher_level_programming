#!/usr/bin/python3
"""Function return available attr and method"""


def lookup(obj):
    """Define lookup
    Args:
        obj
    """
    # Use dir() to get the list of attributes and methods
    attributes_and_methods = dir(obj)
    return attributes_and_methods

# Example usage:


my_list = [1, 2, 3]
result = lookup(my_list)
for item in result:
    print(item)
