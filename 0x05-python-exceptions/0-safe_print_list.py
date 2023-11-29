#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    while (y <= x - 1):
        try:
            print("{}".format(my_list[y]), end="")
            y += 1
        except Exception:
            break
    print("")
    return y
