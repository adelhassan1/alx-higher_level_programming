#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        """sort list"""
        print(sorted(self))
