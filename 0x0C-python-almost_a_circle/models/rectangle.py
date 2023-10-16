# models/rectangle.py
"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """Width Definition
        Args:
            self:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width definition
        Args:
            self:
            value:
        """
        if type(value) is not int:
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """height
        Args:
            self:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height definition
        Args:
            self:
            value:
        """
        if type(value) is not int:
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """x definition"""
        return self.__x

    @x.setter
    def x(self, value):
        """x definition"""
        if type(value) is not int:
            raise ValueError("x must be an integer")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """y definition"""
        return self.__y

    @y.setter
    def y(self, value):
        """y definition"""
        if type(value) is not int:
            raise ValueError("y must be an integer")
        self.__y = value
