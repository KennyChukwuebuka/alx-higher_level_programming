#!/usr/bin/python3
"""6-rectangle"""


class Rectangle:
    """Class for printing or computation of dimensions of a rectangle

    Attributes:
        number_of_instances (int): counter incrementing for every
            instantiation, and decrementing for every instance deletion.

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Increments number_of_instances width`
        and height`

        Args:
            width parameter
            height parameter
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter.

        Returns:
            width parameter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value params

        Attributes:
            width params

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
        """Returns area of a rectangle

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

    @classmethod
    def __del__(cls):
        """Decrements number_of_instances.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')
