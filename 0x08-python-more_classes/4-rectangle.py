#!/usr/bin/python3
"""4-rectangle
"""


class Rectangle:
    """Takes in args for width and height

    Args:
        width
        height

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value

        Attributes:
            width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value

        Attributes:
            height

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle

        Attributes:
            width
            height

        Returns:
            Area of rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle

        Attributes:
            width
            height

        Returns:
            0 if either attribute is 0, or the perimeter

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """draw rectangle.

        Attributes:
            width
            height

        Returns:
            str (str))

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instances.

        Returns:
            The output of _draw_rectangle

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
