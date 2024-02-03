#!/usr/bin/python3
"""read from file"""

def read_file(filename=""):
    """read from file"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
