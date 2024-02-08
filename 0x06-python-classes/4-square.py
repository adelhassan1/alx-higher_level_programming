#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """creates a square and determines area"""

    def __init__(self, size=0):
        """Initializes square
        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """gets area of square"""
        return self.__size * self.__size
