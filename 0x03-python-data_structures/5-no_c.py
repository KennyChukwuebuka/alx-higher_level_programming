#!/usr/bin/python3

def no_c(my_string):
    ret = ''

    for ch in my_string:
        if ch != 'c' and ch != 'C':
            ret += ch
    return ret
