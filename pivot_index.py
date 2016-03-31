#!/usr/bin/python

"""
Given an array, find an element before which all elements are smaller than it, and after
which all are greater than it. Return index of the element if there is such an element,
otherwise return -1.
"""


def pivot_index(arr):
    """
    >>> pivot_index([5, 1, 4, 3, 6, 8, 10, 7, 9])
    4
    >>> pivot_index([4, 1, 3, 6, 7, 5, 0, 8, 10, 9])
    7
    >>> pivot_index([-1, 3, -4, 5, 1, -6, 2, 1])
    -1
    >>> pivot_index([5, 1, 4, 4])
    -1
    >>> pivot_index([5, 1, 3, 6, 2, 10, 15, -2, 12, 13, 14, 16, 17])
    11
    """
    pivot = 0
    curmax = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= curmax:
            curmax = arr[i]
            if pivot == -1:
                pivot = i
        else:
            if pivot != -1 and arr[i] < arr[pivot]:
                pivot = -1
    return pivot


if __name__ == "__main__":
    import doctest
    doctest.testmod()
