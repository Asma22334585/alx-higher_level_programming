#!/usr/bin/python3
"""Task 11"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for x in json:
            self.__dict__.update({x: json[x]})
