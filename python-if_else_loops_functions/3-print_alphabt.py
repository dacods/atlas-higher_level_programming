#!/usr/bin/python3
for ascii in range(ord('a'), ord('z')+1):
    letters = chr(ascii)
    if letters != 'e' and letters != 'q':
        print(letters, end='')