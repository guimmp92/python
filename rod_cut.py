#!/usr/bin/python
# vim: foldlevel=0

"""
Given a rod of length n inches and an array of prices that contains prices of all pieces
of size smaller than n. Determine the maximum value obtainable by cutting up the rod and
selling the pieces.

http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
"""


def recursive(values, length):
    if length == 0:
        return 0

    max_value = 0
    for i in range(length):
        max_value = max(max_value, recursive(values, length-i-1) + values[i])
    # Alternatively:
    #return max(v + rec(length-l-1, values) for l, v in enumerate(values) if l+1 <= length)

    return max_value


def solution1(values):
    """
    Recursive solution.
    >>> solution1([1, 5, 8, 9, 10, 17, 17, 20])
    22
    >>> solution1([3, 5, 8, 9, 10, 17, 17, 20])
    24
    """
    return recursive(values, len(values))


def dp(values, length, memo):
    if length == 0:
        return 0

    if memo[length-1] == 0:
        max_value = 0
        for i in range(length):
            max_value = max(max_value, dp(values, length-i-1, memo) + values[i])
        memo[length-1] = max_value

    return memo[length-1]


def solution2(values):
    """
    Top-down dynamic programming.
    >>> solution2([1, 5, 8, 9, 10, 17, 17, 20])
    22
    >>> solution2([3, 5, 8, 9, 10, 17, 17, 20])
    24
    """
    return dp(values, len(values), [0] * len(values))


def solution3(values):
    """
    Bottom-up dynamic programming.
    >>> solution3([1, 5, 8, 9, 10, 17, 17, 20])
    22
    >>> solution3([3, 5, 8, 9, 10, 17, 17, 20])
    24
    """
    memo = [0] * len(values)
    for i in range(len(values)):
        max_value = values[i]
        for j in range(i):
            max_value = max(max_value, memo[i-j-1] + values[j])
        memo[i] = max_value

    return memo[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
