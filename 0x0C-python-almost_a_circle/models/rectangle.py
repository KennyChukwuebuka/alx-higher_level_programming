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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area definition"""
        return self.__width * self.__height

    def display(self):
        """display definition"""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Definition of string rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Update the class Rectangle"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update the class rectangle"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
