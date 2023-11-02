#!/usr/bin/python3
for i in range(0, 99):
    if i != 98:
        print(f"{str(i).zfill(2)}", end=", ")
    else:
        print(f"{str(i).zfill(2)}")
