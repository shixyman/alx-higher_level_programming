#!/usr/bin/pytho3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    for i in reversd(my_list):
        print("{:d}".format(i))
