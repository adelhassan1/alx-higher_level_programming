#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """creates a square, determines area and prints stdout"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """return square area"""
        return self.__size ** 2

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size, end="")
            print()
