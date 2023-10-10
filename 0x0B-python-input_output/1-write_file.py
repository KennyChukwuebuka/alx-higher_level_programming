#!/usr/bin/python3
"""Define function that write to file"""


def write_file(filename="", text=""):
    """function that write file
    Args:
        filename
        text
    """
    try:

        with open(filename, 'w', encoding='utf-8') as file:

            file.write(text)

            characters_written = len(text)
            return characters_written
    except Exception as e:

        print(f"An error occurred: {e}")
        return 0
