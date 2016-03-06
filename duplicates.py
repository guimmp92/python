#!/usr/bin/python

"""
https://www.pramp.com/question/15oxrQx6LjtQj9JK9XlA

Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n and m
respectively, how can you most efficiently compute an array of all persons included
on both arrays?

Solve and analyze the complexity for 2 cases:
1. m ~= n - lengths are approximately the same
2. m >> n - one is much longer than the other

Note: This is not clear in the problem desription but the arrays are sorted.
      Apparently the candidate is expected to ask the interviewer to get that clue.
"""


def duplicates1(arr1, arr2):
    """
    Case #1: len(arr1) ~= len(arr2)
    >>> duplicates1([1, 2, 3, 4], [3, 4, 5, 6, 7, 8, 9])
    [3, 4]
    >>> duplicates1([1, 2, 3, 9], [3, 4, 5, 6, 7, 8])
    [3]
    """
    dups = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            dups.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return dups


def bisect(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mi = (lo+hi)//2
        if x == arr[mi]:
            return True
        elif x < arr[mi]:
            hi = mi-1
        else:
            lo = mi+1
    return False


def duplicates2(arr1, arr2):
    """
    Case #2: len(arr2) >> len(arr1)
    Implementation with custom binary search.
    >>> duplicates2([1, 2, 3, 4], [3, 4, 5, 6, 7, 8, 9])
    [3, 4]
    >>> duplicates2([1, 2, 3, 9], [3, 4, 5, 6, 7, 8])
    [3]
    """
    dups = []
    for i in range(len(arr1)):
        if bisect(arr2, arr1[i]):
            dups.append(arr1[i])
    return dups


def duplicates3(arr1, arr2):
    """
    Case #2: len(arr2) >> len(arr1)
    Implementation with bisect module.
    >>> duplicates3([1, 2, 3, 4], [3, 4, 5, 6, 7, 8, 9])
    [3, 4]
    >>> duplicates3([1, 2, 3, 9], [3, 4, 5, 6, 7, 8])
    [3]
    """
    from bisect import bisect
    dups = []
    for i in range(len(arr1)):
        j = bisect(arr2, arr1[i])
        if j > 0 and arr2[j-1] == arr1[i]:
            dups.append(arr1[i])
    return dups


if __name__ == "__main__":
    import doctest
    doctest.testmod()
