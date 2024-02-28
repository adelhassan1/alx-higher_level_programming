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
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
