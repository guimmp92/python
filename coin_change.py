#!/usr/bin/python

"""
You are given n types of coin denominations of values V1 < V2 < ... < Vn (all integers).
Assume V1 = 1, so you can always make change for any amount of money M.
Give an algorithm which gets the minimal number of coins that make change for an amount
of money M.

http://blog.gainlo.co/index.php/2015/10/22/a-step-by-step-guide-to-dynamic-programming/
"""


def recursive(M, V):
    """
    Time complexity: O(k^n) where k = len(V)
    >>> recursive(12, [1, 2, 5])
    3
    >>> recursive(13, [1, 2, 5])
    4
    >>> recursive(14, [1, 2, 5, 10])
    3
    """
    if M == 0:
        return 0
    if M in V:
        return 1

    return 1 + reduce(min, [recursive(M-v, V) for v in V if v < M])


def dp(M, V):
    """
    Time complexity: O(n)
    >>> dp(12, [1, 2, 5])
    3
    >>> dp(13, [1, 2, 5])
    4
    >>> dp(14, [1, 2, 5, 10])
    3
    """
    memo = dict()
    memo[0] = 0

    for i in range(1, M+1):
        if i in V:
            memo[i] = 1
        else:
            memo[i] = 1 + min([memo[i-v] for v in V if v < i])

    return memo[M]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
