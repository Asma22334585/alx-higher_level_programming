#!/usr/bin/python3
"""Task 13"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    nlist = "\n" + new_string

    mylist = []

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            if search_string in line:
                line = line.replace("\n", nlist)
            mylist.append(line)
        x = "".join(txtlist)

    with open(filename, "w", encoding="UTF-8") as f:
        f.write(x)
