#!/usr/bin/python3
"""class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializing
        Args:
            width
            height
            x
            y
            id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
        Args:
            value
        """
        if type(value) is not int:
            raise TypeError("width must be integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height
        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x
        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("x must be integer")
        if value < 0:
            raise ValueError("x muxt be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y
        Args:
            value
        """
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """find the area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle instance with #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print("{}{}".format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """returns string of info about rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            keys = ['id', 'width', 'height', 'x', 'y']
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return my_dic
