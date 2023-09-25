#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """safe_function

    Args:
        fct:    params
        args:   params

        Return:
            function result
    """
    try:
        res = fct(*args)
        return res
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
