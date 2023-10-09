#!/usr/bin/python3
"""Define a class list"""


class MyList(list):
    """Class with method
    Args:
        list
    """
    def print_sorted(self):
        """Method definition that sort list"""

        print(sorted(list(self)))
