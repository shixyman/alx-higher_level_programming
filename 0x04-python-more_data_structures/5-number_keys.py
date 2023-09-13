#!/usr/bin/python3
def number_keys(a_dictionary):
    sm = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        sm += 1

    return (sm)
