#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    test_list = my_list.copy()
    test_list[idx] = element
    return test_list
