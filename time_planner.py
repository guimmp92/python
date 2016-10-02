#!/usr/bin/python
# vim: foldlevel=0

"""
Implement a meeting planner that can schedule meetings between two persons at a time.

https://www.pramp.com/question/3QnxW6xoPLTNl5jX5Lg1
"""


def solution(dur, A, B):
    """
    >>> solution(30, [(0, 10), (50, 65), (70, 110)], [(5, 20), (25, 50), (75, 105)])
    (75, 105)
    """
    res = None
    i, j = 0, 0
    while i < len(A) and j < len(B):
        overlap = (max(A[i][0], B[j][0]), min(A[i][1], B[j][1]))
        if overlap[1] - overlap[0] >= dur:
            res = overlap
            break
        if A[i][1] <= B[j][1]:  # which one ends first?
            i += 1
        else:
            j += 1
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
