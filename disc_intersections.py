#!/usr/bin/python

"""
Codility
https://codility.com/demo/take-sample-test/ndi/
http://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
"""


def solution(A):
    """
    >>> solution([1, 5, 2, 1, 4, 0])
    11
    """
    low_bounds = [0] * len(A)
    high_bounds = [0] * len(A)
    for i in range(len(A)):
        low_bounds[i] = i - A[i]
        high_bounds[i] = i + A[i]
    low_bounds = sorted(low_bounds)
    high_bounds = sorted(high_bounds)

    intersects = 0
    low_idx = 0
    for high_idx in range(len(A)):
        while low_idx < len(A) and high_bounds[high_idx] >= low_bounds[low_idx]:
            low_idx += 1
        intersects += low_idx - high_idx + 1

    intersects /= 2  # we only want unordered pairs
    if intersects > 10000000:
        return -1
    return intersects

if __name__ == "__main__":
    import doctest
    doctest.testmod()
