#!/user/bin/python3
"""This module containes a class Rectangle"""


class Rectangle:
    """This class defines rectangle by its width and height
        determines area and perimeter
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """intializes Rectangle.
        Args:
            width: width of rec.
            height: height of rec.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """finding the rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """finding the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """print the rectangle with the character #"""
        for i in range(self.height):
            print("#" * self.width, end='')
            if i != self.height - 1:
                print()
        return ''

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance"""
        return f'Rectangle({self.width}, {self.height})'
