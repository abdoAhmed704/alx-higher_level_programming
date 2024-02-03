#!/usr/bin/python3
#Read file

def read_file(filename=""):
    with open(filename, "r") as file:
        cont = file.read()
        print(cont)
