#!/usr/bin/python3
"""9-rectangle
"""


class Rectangle:
    """Class for printing or computation of dimensions of a rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments number_of_instances

        Args:
            width
            height

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter.

        Returns:
            width

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
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string

        Attributes:
            width
            height
            str (str)

        Returns:
            str (str)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
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
            A string containing the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrements number_of_instances

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances

            Args:
                rect_1 params
                rect_2 params
        Returns:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides of length `size`.

        Args:
            size

        Returns:
            new instance

        """
        return cls(size, size)
