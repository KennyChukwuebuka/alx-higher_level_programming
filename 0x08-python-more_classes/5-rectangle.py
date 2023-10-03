#!/usr/bin/python3
"""5-rectangle"""


class Rectangle:
    """Takes in args for width and height
    Args:
        width   parameter
        height  parameter
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width.

        Returns:
            width parameter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value parameter
        Attributes:
            width parameter

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter.

        Returns:
            height parameter

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value parameter

        Attributes:
            height parameter
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            width parameter
            height parameter

        Returns:
            Area of rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle

        Attributes:
            width parameter
            height parameter

        Returns:
            0 if either attribute is 0, or the perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string

        Attributes:
            width parameter
            height parameter
            str (str)

        Returns:
            str (str)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """str.

        Returns:
            The output of _draw_rectangle

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows eval().

        Returns:
            A string of the code

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def __del__():
        """Prints message upon deletion of instance.

        """
        print('Bye rectangle...')
