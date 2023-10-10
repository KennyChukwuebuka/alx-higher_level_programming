#!/usr/bin/python3
"""Define function that append on a file"""


def append_write(filename="", text=""):
    """ function that appends a string returns the number of characters """

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
