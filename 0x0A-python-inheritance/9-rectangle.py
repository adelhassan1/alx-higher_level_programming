#!/usr/bin/python3
"""class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializing
        Args
            width
            height
        """
        if not super().integer_validator('width', width):
            self.__width = width
        if not super().integer_validator('height', height):
            self.__height = height

    def area(self):
        """gets area"""
        return (self.__width * self.__height)

    def __str__(self):
        """the print function"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
