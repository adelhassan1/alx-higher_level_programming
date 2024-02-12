#!/user/bin/python3
"""This module containes a class Rectangle"""


class Rectangle:
    """This class defines rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """intializes Rectangle.
        Args:
            width: width of rec.
            height: height of rec.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
