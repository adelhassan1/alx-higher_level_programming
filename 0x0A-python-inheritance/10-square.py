#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from rectangle"""

    def __init__(self, size):
        """initializing
        Args
            size
        """
        super().__init__(size, size)
        if not super().integer_validator('size', size):
            self.__size = size

    def area(self):
        """gets area of square"""
        return (self.__size ** 2)
