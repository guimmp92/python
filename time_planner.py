#!/usr/bin/python
# vim: foldlevel=0

"""
Implement a meeting planner that can schedule meetings between two persons at a time.

https://www.pramp.com/question/3QnxW6xoPLTNl5jX5Lg1
"""


def compute_overlap(A, B):
    start, end = max(A[0], B[0]), min(A[1], B[1])
    if start < end:
        return [start, end]


def solution(dur, A, B):
    """
    >>> solution(30, [[0, 10], [50, 65], [70, 110]], [[5, 20], [25, 50], [75, 105]])
    [75, 105]
    """
    res = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        overlap = compute_overlap(A[i], B[j])
        if overlap and overlap[1] - overlap[0] >= dur:
            res = [overlap[0], overlap[0]+dur]
            break
        else:
            if A[i][0] <= B[j][0]:
                i += 1
            else:
                j += 1
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
