#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """creates a square and determines area"""

    def __init__(self, size=0):
        """initailizes square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.size
