#!/usr/bin/python

"""
Codility
https://codility.com/demo/take-sample-test/ndi/
http://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
"""


def solution(A):
    """
    A solution in linear time using the merge portion of the mergesort algorithm.
    Similar to intervals_overlap.py.
    >>> solution([1, 5, 2, 1, 4, 0])
    11
    """
    lo_bounds, hi_bounds = list(), list()
    for i, a in enumerate(A):
        lo_bounds.append(i-a)
        hi_bounds.append(i+a)

    lo_bounds.sort()
    hi_bounds.sort()

    overlaps, intersects = 0, 0
    i, j = 0, 0
    while i < len(lo_bounds) and j < len(hi_bounds):
        if lo_bounds[i] <= hi_bounds[j]:
            overlaps += 1
            i += 1
        else:
            overlaps -= 1
            j += 1
        intersects += overlaps // 2

    while j < len(hi_bounds):
        overlaps -= 1
        j += 1
        intersects += overlaps // 2

    return intersects


def solution1(A):
    """
    >>> solution1([1, 5, 2, 1, 4, 0])
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

    intersects //= 2  # we only want unordered pairs
    if intersects > 10000000:
        return -1
    return intersects


def _binsearch(arr, x, lo, hi):
    """
    >>> _binsearch([-4, -1, 0, 0, 2, 5], 0, 0, 5)
    4
    >>> _binsearch([-4, -1, 0, 0, 2, 5], 3, 0, 5)
    5
    """
    while lo <= hi:
        mid = (lo+hi)//2
        if x >= arr[mid]:
            lo = mid+1
        else:
            hi = mid-1
    return lo


def solution2(A):
    """
    O(nlog(n)) time complexity using binary search.
    >>> solution2([1, 5, 2, 1, 4, 0])
    11
    """
    # Create list of intervals
    intervals = list()
    for i, rad in enumerate(A):
        intervals.append([i-rad, i+rad])

    # Sort list by lower bound
    intervals.sort()

    # For each interval, find number of intersections between low and high bounds
    # of interval using binary search
    intersects = 0
    lo_bounds = [i[0] for i in intervals]
    for i, (lo, hi) in enumerate(intervals):
        insert_idx = _binsearch(lo_bounds, hi, i, len(intervals)-1)
        intersects += insert_idx - i + 1

    intersects //= 2
    if intersects > 10000000:
        return -1

    return intersects


if __name__ == "__main__":
    import doctest
    doctest.testmod()
