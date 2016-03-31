#!/usr/bin/python

"""
Given three sorted arrays A, B and C, find three elements i, j and k from A, B and C
respectively such that max(abs(A[i]-B[j]), abs(B[j]-C[k]), abs(C[k]-A[i]) is
minimized.

http://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
"""
import sys


def solution(arr1, arr2, arr3):
    """
    >>> solution([1, 4, 10], [2, 15, 20], [10, 12])
    (10, 15, 10)
    >>> solution([20, 24, 100], [2, 19, 22, 79, 800], [10, 12, 23, 24, 119])
    (24, 22, 23)
    """
    closest_trio = None
    diff = sys.maxint

    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # Do we have a new closest trio?
        curdiff = max(abs(arr1[i]-arr2[j]), abs(arr1[i]-arr3[k]), abs(arr2[j]-arr3[k]))
        if curdiff < diff:
            diff = curdiff
            closest_trio = (arr1[i], arr2[j], arr3[k])

        # Increment i, j or k
        curmin = min([arr1[i], arr2[j], arr3[k]])
        if arr1[i] == curmin:
            i += 1
        elif arr2[j] == curmin:
            j += 1
        elif arr3[k] == curmin:
            k += 1

    return closest_trio


if __name__ == "__main__":
    import doctest
    doctest.testmod()
