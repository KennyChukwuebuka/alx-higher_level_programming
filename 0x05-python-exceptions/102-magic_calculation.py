#!/usr/bin/python3
def magic_calculation(a, b):
    """magic_calculation

    Args:
        a:
        b:

    Return:
        Bytecodes
    """
    res = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            res += (a ** b) / i
        except:
            res += a + b

    return res
