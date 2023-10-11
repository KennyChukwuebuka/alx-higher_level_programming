#!/usr/bin/python3
"""Define append after"""


def append_after(filename="", search_string="", new_string=""):
    """Define append_after
    Args:
        filename
        search_string
        new_string
    """
    read = []
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
        index = 0

        while index < len(read):
            if search_string in read[index]:
                read[index:index + 1] = [read[index], new_string]
