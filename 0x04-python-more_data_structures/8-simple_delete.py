#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """simple_delete

        Args:
            a_dictionary:
            key:

        Return:
            Deletes a key
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
