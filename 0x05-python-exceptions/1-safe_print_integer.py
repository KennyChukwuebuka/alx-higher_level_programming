#!/usr/bin/python3
def safe_print_integer(value):
    """safe_print_integer

    Args:
        value - integer or string

    Return:
        True or False
    """
    try:
        value_to_format = "{:d}".format(value)
        print(value_to_format)
        return True
    except (ValueError, TypeError):
        return False
