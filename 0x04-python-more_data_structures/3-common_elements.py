#!/usr/bin/python3
def common_elements(set_1, set_2):
    """common_elements function

    Args:
        set_1:
        set_2:

    Return:
        The unique value in a set
    """

    commonset_value = set_1.intersection(set_2)

    return commonset_value

