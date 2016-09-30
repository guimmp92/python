#!/usr/bin/python
# vim: foldlevel=0

"""
Consider a 2D map with a horizontal river passing through its center. There are
n cities on the southern bank with x-coordinates a(1)...a(n) and n cities on the
northern bank with x-coordinates b(1)...b(n). You want to connect as many
north-south pairs of cities as possible with bridges such that no bridges cross.
When connecting cities, you can only connect city i on the northern bank to
city i on the southern bank.

https://people.cs.clemson.edu/~bcdean/dp_practice/
"""
import operator


def dp(X, j, memo):
    if memo[j] == -1:
        curmax = 0
        for i in range(j):
            lis_i = dp(X, i, memo)
            if X[i][1] < X[j][1] and lis_i+1 > curmax:
                curmax = lis_i+1
        memo[j] = curmax
    return memo[j]


def solution(N, S):
    """
    >>> solution([10, 22, 33, 44], [11, 23, 34, 45])
    4
    >>> solution([10, 22, 9, 33], [34, 10, 23, 11])
    2
    >>> solution([10, 22, 9, 33, 0], [34, 10, 23, 11, 50])
    2
    """
    # Create new list sorted based on southern bank coordinates
    X = sorted(zip(S, N), key=operator.itemgetter(0))

    # Apply dp algorithm to get longest ascending subsequence in northern bank coordinates
    memo = [-1] * len(X)
    memo[0] = 1
    dp(X, len(X)-1, memo)
    return max(memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
