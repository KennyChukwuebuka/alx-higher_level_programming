#!/usr/bin/python3
def safe_print_division(a, b):
    """safe_print_division

    Args:
        a:  integer
        b:  integer

    Return:
        values of division OR none
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
