#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0

    for arg in sys.argv[1:]:
        sum = sum + int(arg)
    print(sum)
