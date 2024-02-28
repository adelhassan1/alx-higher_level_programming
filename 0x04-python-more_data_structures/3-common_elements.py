#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_in_set = []
    for x in set_1:
        if x in set_2:
            common_in_set.append(x)
    return common_in_set
