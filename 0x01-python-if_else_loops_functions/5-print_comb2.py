#!/usr/bin/python3

for i in range(100):
    if (i != 99):
        print("{0:02d},".format(i), end=" ")
    else:
        print("{0:0d}".format(i))
