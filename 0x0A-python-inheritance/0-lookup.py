#!/usr/bin/python3
'''lookup method.'''


def lookup(obj):
    ''' list of available attributes and methods
    Args:
        obj (object): the object

    Returns:
        list:  list object
    '''
    return dir(obj)
