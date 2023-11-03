#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = str
    if n <= len(str) and n >= 0:
        tmp = tmp.replace(str[n], "", 1)
    return tmp
