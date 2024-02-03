#!/usr/bin/python3
"""read """

def read_file(filename=""):
    with open(filename, encoding="UTF-8") as file:
        cont = file.read()
        print(cont, end="")
