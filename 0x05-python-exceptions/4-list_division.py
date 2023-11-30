#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = 5
    idx = 0
    new_list = []
    while idx <= list_length - 1:
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            idx += 1
    return new_list
