#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return isinstance(value, int)
    except (ValueError, TypeError):
        return False
    return True
