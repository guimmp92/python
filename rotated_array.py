#!/usr/bin/python

"""
Find minimum element in a rotated sorted array, e.g. 3, 4, 5, 6, 7, 1, 2 (CtCI p52)
"""

from collections import deque
from random_array import randlist

arr = randlist(size=20, upper=100)
arr.sort()
arr_deque = deque(arr)
arr_deque.rotate(5)
arr = list(arr_deque)


def _find_minimum(x, left, right):
    """ My initial recursive implementation. """
    if x[left] < x[right]:
        return left
    middle = (left+right)//2
    if x[middle-1] > x[middle] and x[middle] < x[middle+1]:
        return middle
    if x[left] > x[middle]:
        return _find_minimum(x, left, middle-1)
    else:
        return _find_minimum(x, middle+1, right)


def find_minimum(x):
    """
    >>> find_minimum([28, 29, 59, 70, 80, 0, 1, 3, 5, 8, 9, 10, 11, 12, 17, 18, 22])
    5
    >>> find_minimum([2, 3, 5, 8, 9, 10, 11, 12, 17, 18, 22, 0, 1])
    11
    >>> find_minimum([0, 1, 3, 5, 8, 9, 10, 11, 12, 17, 18, 22])
    0
    """
    left, right = 0, len(x)-1
    while x[left] > x[right]:
        middle = (left+right)//2
        if x[left] > x[middle]:
            right = middle
        else:
            left = middle+1  # remember the +1 otherwise infinite loop
    return left

if __name__ == "__main__":
    import doctest
    doctest.testmod()
