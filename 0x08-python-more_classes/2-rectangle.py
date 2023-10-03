#!/usr/bin/python3
"""2-rectangle.
"""


class Rectangle:
    """Takes in args for width and height of a rectangle.

    Args:
        width parameter
        height parameter

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter.

        Returns:
            width  horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value parameter

        Attributes:
            width parameter

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

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
            height vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value parameter

        Attributes:
            height parameter

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area of a rectangle of a given `width` and `height`.

        Attributes:
            width parameter
            height parameter

        Returns:
            Area of rectangle: width * height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a rectangle of given `width` and `height`

        Attributes:
            width parameter
            height parameter

        Returns:
            0 if either attribute is 0, or the perimeter: (width * 2) +
            (height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
