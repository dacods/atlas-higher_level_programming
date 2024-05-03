#!/usr/bin/python3
for letters in range(ord('a'), ord('z')+1):
    if ord(letters) == 101 or ord(letters) == 113:
        continue
    print("{:c}".format(letters), end="")