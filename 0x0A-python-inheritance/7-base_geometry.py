#!/usr/bin/python3
'''BaseGeometry class.'''


class BaseGeometry:
    '''BaseGeometry class.'''
    def area(self):
        '''Calculates the area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''that validates value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
