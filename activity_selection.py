#!/usr/bin/python
# vim: foldlevel=0

"""
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single
 person, assuming that a person can only work on a single activity at a time.

http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
"""
import operator


def solution(S, E):
    """
    Time complexity: O(nlog(n))
    >>> solution([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
    [0, 1, 3, 4]
    """
    res = []
    activities = sorted(zip(S, E), key=operator.itemgetter(1))
    res.append(0)
    for i in range(1, len(activities)):
        if activities[i][0] > activities[res[-1]][1]:
            res.append(i)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
