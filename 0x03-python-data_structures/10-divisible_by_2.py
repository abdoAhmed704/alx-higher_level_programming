#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    returnlist = []
    for idx in my_list:
        if idx % 2 == 0:
            returnlist.append(True)
        else:
            returnlist.append(False)
    return returnlist
