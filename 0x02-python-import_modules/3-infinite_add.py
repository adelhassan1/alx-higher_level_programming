#!/usr/bin/python3

if __name__ == "__main__":
    """print sum of args"""
    import sys

    total = 0
    if len(sys.argv) == 1:
        print('0')
    else:
        for i in range(1, len(sys.argv) - 1):
            total += int(sys.argv[i])
        print("{}".format(total))
