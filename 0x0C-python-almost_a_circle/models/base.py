#!/usr/bin/python3
"""class Base"""
import json
import csv


class Base:
    """class Base"""
    __nb__objects = 0

    def __init__(self, id=None):
        """initializing
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string of dictionaries
        Args
            list_dictionaries - list of dict
        """
        if not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls - class
            list_objs - list of objects
        """
        filename = '{}.json'.format(cls.__name__)

        my_list = []
        if list_objs:
            for x in list_objs:
                my_list.append(x.to_dictionary())
        my_list = cls.to_json_string(my_list)
        with open(filename, 'w') as f:
            f.write(my_list)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        Args:
            json_string - represnts a list of dict
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance
        Args:
            cls - calss
            **dictionary - double pointer to a dictionary
        """
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        if cls.__name__ == 'Square':
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        Args
            cls - class
        """
        my_list = []
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
            return ([cls.create(**x) for x in my_list])
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV
        Args
            cls - class
            list_objs - list of objects
        """
        filename = '{}.csv'.format(cls.__name__)
        if cls.__name__ == 'Rectangle':
            names = ['id', 'width', 'height', 'x', 'y']
        else:
            names = ['id', 'size', 'x', 'y']

        with open(filename, 'w', newline='') as f:
            if list_objs:
                writer = csv.DictWriter(f, fieldnames=names)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())
            else:
                writer.writerow([[]])

    def load_from_file_csv(cls):
        """deserializes in CSV
        Args
            cls
        """
        my_list = []
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                    my_list.append(row)
            return ([cls.create(**x) for x in my_list])
        except FileNotFoundError:
            return ([[]])
