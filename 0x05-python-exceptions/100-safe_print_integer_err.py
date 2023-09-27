#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    """safe_print_integer_err

        Args:
            value: type integer or string

        Return:
            True or False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        import sys
        print("Exception:", e, file=sys.stderr)
        return False
