#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    lint = list_of_integers
    lgt = len(lint)
    if lgt == 0:
        return None 
    m = lgt // 2
    if (m == lgt - 1 or lint[m] >= lint[m + 1]) and (m == 0 or lint[m] >= lint[m - 1]):
        return lint[m]
    if m != lgt - 1 and lint[m + 1] > lint[m]:
        return find_peak(lint[m + 1:])
    return find_peak(lint[:m])
