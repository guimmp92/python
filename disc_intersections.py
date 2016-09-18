#!/usr/bin/python
# vim: foldlevel=0

"""
Codility
https://codility.com/programmers/task/number_of_disc_intersections/
http://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
"""


def solution(A):
    """
    O(nlog(n)) time complexity using binary search.
    >>> solution([1, 5, 2, 1, 4, 0])
    11
    """
    import operator

    def _binary_search(arr, lo, hi, x):
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid][0] == x:
                return mid
            if arr[mid][0] < x:
                lo = mid+1
            else:
                hi = mid-1
        return hi

    res = 0
    intervals = [(i-A[i], i+A[i]) for i in range(len(A))]
    intervals = sorted(intervals, key=operator.itemgetter(0))
    for i in range(len(intervals)):
        j = _binary_search(intervals, i, len(intervals)-1, intervals[i][1])
        res += j-i
    if res > 10000000:
        return -1
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
