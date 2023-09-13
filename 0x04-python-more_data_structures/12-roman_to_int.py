#!/usr/bin/python3
def roman_to_int(roman_string):
    """roman_to_int

        Args:
            roman_string:

            Return:
                0 if not string or None
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return None

    dict_rom_num = {
        'I': 1,
        'V': 5,
        'X': 0,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res = 0
    prv_value = 0

    for i in roman_string[::-1]:
        val = dict_rom_num.get(i, 0)
        if val == 0:
            return 0
        if val < prv_value:
            res -= val
        else:
            res += val
    return res
