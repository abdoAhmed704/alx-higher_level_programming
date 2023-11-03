#!/usr/bin/python3
count = 0
for i in range(90, 64, -1):
    count += 1
    print("{:c}".format((i + 32) if (count % 2 != 0) else i), end="")
