#!/usr/bin/python3
"""text_indentation method."""


def text_indentation(text):
    """print 2 new lines after '.?:' characters

    Args:
        text: string.

    Raises:
        TypeError: If text not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
