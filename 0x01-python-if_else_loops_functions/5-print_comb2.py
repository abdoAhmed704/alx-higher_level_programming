#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        i = f"0{i}"
    else:
        i = f"{i}"
    if int(i) != 99:
        print("{:s}".format(i), end=", ")
    else:
        print("{:s}".format(i))
