#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) = 0:
        return None
    bigger = my_list[0]
    for idx in my_list:
        if idx > bigger:
            bigger = idx
    return bigger
