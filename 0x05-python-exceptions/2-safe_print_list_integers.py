#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    if (x <= 0):
        print(0)
        return (0)
    for i in range(x):
        count += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            count -= 1
            continue
    print()
    return (count)
