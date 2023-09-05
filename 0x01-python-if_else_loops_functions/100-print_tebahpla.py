#!/usr/bin/python3
for j in range(ord('z'), ord('a') - 1, -1):
    i = 32 if (j - ord('a')) % 32 == 0 else 0
    print("{}".format(chr(j - i)), end="")

