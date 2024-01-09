#!/usr/bin/python3
"""
Write_file
"""


def write_file(filename="", text=""):
    """
     writes a string to a text file (UTF8)
    """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
