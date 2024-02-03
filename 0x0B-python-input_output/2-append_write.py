#!/usr/bin/python3
"""write in file"""


def append_write(filename="", text=""):
    """append in file"""

    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
        return len(text)
