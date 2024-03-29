#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """creates a square"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
