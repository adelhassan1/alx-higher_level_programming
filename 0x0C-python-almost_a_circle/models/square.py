#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initalizing
        Args:
            size
            x
            y
            id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string of info about square"""
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size
        Args:
            value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        keys = ['id', 'size', 'x', 'y']
        if args:
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        my_dic = {}
        keys = ['id', 'size', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return my_dic
