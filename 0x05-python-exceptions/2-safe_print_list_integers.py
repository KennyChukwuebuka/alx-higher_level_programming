#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers

    Args:
        my_list: contains integers and string
        x: number of element

    Return:
        integers
    """
    i = 0
    res = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except (ValueError, TypeError):
            continue
    print()
    return res
