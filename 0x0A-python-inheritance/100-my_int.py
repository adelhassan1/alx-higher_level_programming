#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class that inherits from int"""

    def __eq__(self, other):
        """reverse equality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """reverse none equality"""
        return not super().__ne__(other)
