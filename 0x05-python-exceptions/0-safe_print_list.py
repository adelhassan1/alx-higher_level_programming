#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            count += 1
            print(my_list[i], end="")
        print()
        return (count)
    except IndexError:
        count -= 1
        print()
        return (count)
