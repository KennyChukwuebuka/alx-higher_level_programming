#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_del = []

    for key, ret_val in a_dictionary.items():
        if ret_val == value:
            key_to_del.append(key)

    for key in key_to_del:
        del a_dictionary[key]

    return a_dictionary
