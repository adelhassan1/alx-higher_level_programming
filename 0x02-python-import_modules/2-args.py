#!/usr/bin/python3

if __name__ == "__main":
    """print args"""
    import sys

    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv) - 1):
        print("{}: {}".format(i, sys.argv[i]))
