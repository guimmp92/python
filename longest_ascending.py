#!/usr/bin/python

"""
Given a sequence of numbers, write a function to find the length of a longest increasing
subsequence of the given sequence without the consecutive constraint.
"""


def lis(arr, i):
    """ list(i) is the max length of seq ending at i, with arr[i] being part of it.
        list(i) = 1 + max(lis(j)) if arr[j] < arr[i] else 1
    """
    maxendinghere = 1
    for j in range(i):
        lis_j = lis(arr, j)
        if lis_j+1 > maxendinghere and arr[i] > arr[j]:
            maxendinghere = lis_j+1
    return maxendinghere


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
    if not memo.get(i):
        maxendinghere = 1
        for j in range(i):
            lis_j = lis2(arr, j, memo)
            if lis_j+1 > maxendinghere and arr[i] > arr[j]:
                maxendinghere = lis_j+1
        memo[i] = maxendinghere
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
    memo = dict()
    return max(lis2(arr, i, memo) for i in range(len(arr)))


def _binsearch(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if x >= arr[mid]:
            lo = mid+1
        elif x < arr[mid]:
            hi = mid-1
    return lo


def solution3(arr):
    """
    Iterative. Pretty ugly.
    >>> solution3([1, 3, -1])
    2
    >>> solution3([1, 3, 2, 4, 5, 1])
    4
    >>> solution3([1, 20, 5, 15, 40, 10, -5, -2])
    4
    """
    subs = []
    for i, num in enumerate(arr):
        sub, insert_idx = None, None
        for s in subs:
            idx = _binsearch(s, num)  # we assume that there are no duplicates in arr
            if idx == 0:  # num goes to the left of the subsequence
                continue
            if not insert_idx or (insert_idx and idx > insert_idx):
                insert_idx, sub = idx, s
        if sub:
            # The number goes at the end of an existing subsequence, append it.
            if insert_idx == len(sub)-1:
                s.append(num)
            # The number goes in the middle of an existing subsequence, create a new
            # subsequence.
            else:
                subs.append(s[:insert_idx] + [num])
        else:
            # The number is smaller than any number seen so far, create a new
            # subsequence.
            subs.append([num])
    return max(len(s) for s in subs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
