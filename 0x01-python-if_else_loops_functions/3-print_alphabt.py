#!/usr/bin/python3

for i in range(26):
    if (i != 4) & (i != 16):
        print("{}".format(chr(97 + i)), end="")
