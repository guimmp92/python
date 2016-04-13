#!/usr/bin/python

"""
Given an array of integers, find the nearest smaller number for every element such that
the smaller element is on left side.

http://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/
"""


def solution1(arr):
    """
    >>> solution1([1, 6, 4, 10, 2, 5])
    [None, 1, 1, 4, 1, 2]
    >>> solution1([1, 3, 0, 2, 5])
    [None, 1, None, 0, 2]
    """
    nearest_smaller = [None]
    stack = [arr[0]]
    for i in range(1, len(arr)):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        if stack:
            nearest_smaller.append(stack[-1])
        else:
            nearest_smaller.append(None)
        stack.append(arr[i])
    return nearest_smaller


def solution2(arr):
    """
    >>> solution2([1, 6, 4, 10, 2, 5])
    [None, 1, 1, 4, 1, 2]
    >>> solution2([1, 3, 0, 2, 5])
    [None, 1, None, 0, 2]
    """
    nearest_smaller = [None]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            nearest_smaller.append(arr[i-1])
        else:
            j = len(nearest_smaller)-1
            while j >= 0 and arr[j] and arr[j] > arr[i]:
                j -= 1
            if j < 0:
                nearest_smaller.append(None)
            else:
                nearest_smaller.append(arr[j])

    return nearest_smaller


if __name__ == "__main__":
    import doctest
    doctest.testmod()
