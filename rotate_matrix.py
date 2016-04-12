#!/usr/bin/python

"""
Rotate a matrix by 90 degrees clockwise.

Input:
    1    2   3   4
    5    6   7   8
    9   10  11  12
Output:
    9    5    1
    10   6    2
    11   7    3
    12   8    4
"""


def solution(m):
    """
    >>> solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
