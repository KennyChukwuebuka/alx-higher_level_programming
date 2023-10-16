#!/usr/bin/python3
"""Write the class Square that inherit from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Sqaure"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str definition"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
