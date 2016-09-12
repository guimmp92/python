#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array of sorted distinct integers named arr, write a function that returns an
index i in arr for which arr[i] = i or -1 if no such index exists.

Implement the most efficient solution possible, prove the correctness of your solution
and analyze its runtime complexity (in terms of n - the length of arr).

Examples:

Given arr = [-8,0,2,5] the function returns 2, since arr[2] = 2
Given arr = [-1,0,3,6] the function returns -1, since no index in arr satisfies
arr[i] = i

https://www.pramp.com/question/jKoA5GAVy9Sr9jGBjz04
"""


def solution(arr):
    """
    >>> solution([-8, 0, 2, 5])
    2
    >>> solution([-1, 0, 3, 6])
    -1
    """
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] - mid == 0:
            return mid
        if arr[mid] - mid < 0:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
