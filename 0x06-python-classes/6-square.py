#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """creates square, determines area,
    print it and and set poistion"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes square
        Args:
            size: size of square.
            position: position of square"""
        self.size = size
        self.position = position

    def area(self):
        """return square area"""
        return self.__size ** 2

    @property
    def size(self):
        """gets size"""
        return self.__size

    @property
    def position(self):
        """gets positioin"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """sets positioin"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))
