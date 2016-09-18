#!/usr/bin/python
# vim: foldlevel=0

"""
Given a sequence of numbers, write a function to find the length of a longest
increasing subsequence of the given sequence without the consecutive constraint.
"""


def lis(arr, i):
    """ list(i) is the max length of seq ending at i, with arr[i] being part of it.
        list(i) = 1 + max(lis(j)) if arr[j] < arr[i] else 1
    """
    if i == 0:
        return 1
    curmax = 0
    for j in range(i):
        lis_j = lis(arr, j)
        if arr[j] < arr[i]:
            curmax = max(curmax, lis_j)
    return 1 + curmax


def solution1(arr):
    """
    Recursive.
    >>> solution1([10, 22, 9, 33, 21, 50, 41, 60, 80])
    6
    >>> solution1([1, 3, -1])
    2
    >>> solution1([1, 3, 2, 4, 5, 1])
    4
    >>> solution1([1, 20, 5, 15, 40, 10, -5, -2])
    4
    """
    return max(lis(arr, i) for i in range(len(arr)))


def lis2(arr, i, memo):
    if memo[i] == -1:
        curmax = 0
        for j in range(i):
            lis_j = lis2(arr, j, memo)
            if arr[j] < arr[i]:
                curmax = max(curmax, lis_j)
        memo[i] = 1 + curmax
    return memo[i]


def solution2(arr):
    """
    Dynamic programming.
    >>> solution2([10, 22, 9, 33, 21, 50, 41, 60, 80])
    6
    >>> solution2([1, 3, -1])
    2
    >>> solution2([1, 3, 2, 4, 5, 1])
    4
    >>> solution2([1, 20, 5, 15, 40, 10, -5, -2])
    4
    """
    memo = [-1] * len(arr)
    lis2(arr, len(arr)-1, memo)
    return max(memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
