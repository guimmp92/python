#!/usr/bin/python

"""
Given a sequence of numbers, write a function to find the length of a longest increasing
subsequence of the given sequence without the consecutive constraint.
"""


def _binsearch(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if x >= arr[mid]:
            lo = mid+1
        elif x < arr[mid]:
            hi = mid-1
    return lo


def solution(arr):
    """
    >>> solution([1, 3, -1])
    2
    >>> solution([1, 3, 2, 4, 5, 1])
    4
    >>> solution([1, 20, 5, 15, 40, 10, -5, -2])
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
