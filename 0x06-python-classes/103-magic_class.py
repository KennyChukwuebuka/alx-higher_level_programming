#!/usr/bin/python3
"""Define the magic"""

import math


class MagicClass:
    """Define Magic class"""

    def __init__(self, radius=0):
        """Define the raduis
        Args:
            radius: parameter definition
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Define the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Define the circumference"""
        return 2 * math.pi * self.__radius
