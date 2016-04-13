#!/usr/bin/python

"""
Problem 1: Rotate an NxM matrix by 90 degrees.
http://www.geeksforgeeks.org/turn-an-image-by-90-degree/

Input:
    1    2   3   4
    5    6   7   8
    9   10  11  12
Output:
    9    5    1
    10   6    2
    11   7    3
    12   8    4

Problem 2: Rotate an NxN matrix in place by 90 degrees.
CTCI p179

Input:
    1    2   3
    5    6   7
    9   10  11
Output:
    9    5    1
    10   6    2
    11   7    3
"""


def solution1(m):
    """
    >>> solution1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]
    """
    rlen = len(m)
    clen = len(m[0])
    r = [0] * clen
    for i in range(clen):
        r[i] = [0] * rlen
    for i in range(rlen):
        for j in range(clen):
            r[j][rlen-i-1] = m[i][j]
    return r


def solution2(m):
    """
    >>> solution1([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
    [[9, 5, 1], [10, 6, 2], [11, 7, 3]]
    """
    M = len(m)
    for layer in M//2:
        for i in range(M-1):
            m[layer][i], m[i][M-layer-1], m[M-layer-1][M-i-1], m[M-i-1][layer] = \
            m[M-i-1][layer], m[layer][i], m[i][M-layer-1], m[M-layer-1][M-i-1]
        M -= 2
    return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()
