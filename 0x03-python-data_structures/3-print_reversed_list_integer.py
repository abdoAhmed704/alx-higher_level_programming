#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    test_list = my_list
    test_list.reverse()
    for idx in test_list:
        print("{:d}".format(idx))
