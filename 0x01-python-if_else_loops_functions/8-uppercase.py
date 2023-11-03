#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if (i <= 122 and i >= 97):
        return True
    else:
        return False


def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) if not islower(i) else (ord(i) - 32)),
              end="")
    print("")
