#!/usr/bin/python
# vim: foldlevel=0

"""
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single
 person, assuming that a person can only work on a single activity at a time.

http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
"""
import operator


def solution1(S, E):
    """
    Time complexity: O(nlog(n))
    >>> solution1([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
    [0, 1, 3, 4]
    """
    res = []
    activities = sorted(zip(S, E), key=operator.itemgetter(1))
    res.append(0)
    for i in range(1, len(activities)):
        if activities[i][0] > activities[res[-1]][1]:
            res.append(i)
    return res


def dp(A, j, memo):
    if memo[j] == -1:
        curmax = 0
        for i in range(j):
            maxendinghere = dp(A, i, memo)
            if A[i][1] < A[j][0] and maxendinghere+1 > curmax:
                curmax = maxendinghere+1
        memo[j] = curmax
    return memo[j]


def solution2(S, E):
    """
    Time complexity: O(n^2)
    >>> solution2([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
    4
    """
    activities = sorted(zip(S, E), key=operator.itemgetter(1))
    memo = [-1] * len(activities)
    memo[0] = 1
    dp(activities, len(activities)-1, memo)
    return max(memo)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
