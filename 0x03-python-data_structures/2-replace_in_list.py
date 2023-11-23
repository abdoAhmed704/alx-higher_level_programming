#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx < 0) or (idx + 1 > length):
        return None
    in_my_list = my_list
    in_my_list[idx] = element
    return in_my_list
