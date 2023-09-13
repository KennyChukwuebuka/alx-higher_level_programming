#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print_sorted_dictionary

    Args:
        a_dictionary:

    Return:
        Dictionary by ordered key
    """
    sorted_key_ele = sorted(a_dictionary.keys())

    for key in sorted_key_ele:
        val = a_dictionary[key]
        print('{}: {}'.format(key, val))
