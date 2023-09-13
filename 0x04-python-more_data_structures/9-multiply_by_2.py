#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply_by_2

        Args:
            a_dictionary:

        Return:
            New dictionaries with all values * 2
    """

    ret_dictionaries = {}

    for key, value in a_dictionary.items():
        ret_dictionaries[key] = value * 2

    return ret_dictionaries
