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

    for index, line in enumerate(read):
        if search_string in line:
            read.insert(index + 1, new_string)

    # Check if the last line already ends with a newline
    if not read[-1].endswith('\n'):
        read[-1] += '\n'

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(read)
