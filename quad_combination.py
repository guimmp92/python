#!/usr/bin/python

"""
https://www.pramp.com/question/gKQ5zA52mySBOA5GALj9

Given an array of numbers arr and a number S, find 4 different numbers in arr that sum
up to S.

Write a function that gets arr and S and returns an array of 4 indices of such numbers
in arr, or null if no such combination exists.
"""
from collections import defaultdict
from itertools import product


def solution(arr, S):
    """
    >>> solution([3, 7 , 1, 8, -3, 0, 2, 7, -4, -2], -8)
    [2, 4, 8, 9]
    """
    sum = defaultdict(list)
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    # Or:
    for i, j in product(range(len(arr)), repeat=2):  # O(n^2)
        if i != j:
            sum[arr[i]+arr[j]].append(sorted((i, j)))

    for doublesum, idx1 in sum.iteritems():
        idx2 = sum.get(S-doublesum)
        if not idx2:
            continue
        for pr in product(idx1, idx2):
            indices = [i for t in pr for i in t]
            if len(set(indices)) == 4:
                return indices


if __name__ == "__main__":
    import doctest
    doctest.testmod()
