#!/usr/bin/python
# vim: foldlevel=0

"""
Given the [weight,profit] pair of N items lying around the floor and the amount
of weight your bag can handle, you need to pack as many items in your bag as
you can provided you generate maximum profit at the end, after you sell each of
the stolen goods.

Note: This is the same problem as the rod cutting one except that you can use
      each item only once. In the rod cutting problem you can use one section
      of the rod of a given length multiple times.

http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
"""


def dp(items, i, capacity, memo):
    if i == 0 or capacity == 0:
        return 0
    if memo[i][capacity] == -1:
        if items[i-1][0] > capacity:
            memo[i][capacity] = dp(items, i-1, capacity, memo)
        else:
            memo[i][capacity] = max(
                dp(items, i-1, capacity, memo),
                items[i-1][1] + dp(items, i-1, capacity-items[i-1][0], memo)
            )
    return memo[i][capacity]


def solution(items, capacity):
    """
    >>> solution([(12, 4), (4, 10), (2, 2), (1, 2), (1, 1)], 15)
    15
    >>> solution([(12, 4), (4, 10), (2, 2), (1, 2), (1, 1)], 17)
    16
    >>> solution([(12, 4), (1, 2), (4, 6), (1, 1), (2, 2)], 15)
    11
    """
    memo = [[-1 for j in range(capacity+1)] for i in range(len(items)+1)]
    return dp(items, len(items), capacity, memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
