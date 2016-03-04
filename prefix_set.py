#!/usr/bin/python

"""
Codility
https://codility.com/demo/take-sample-test/ps/
http://blog.codility.com/2011/03/solutions-for-task-equi.html

A non-empty zero-indexed array A consisting of N integers is given.
The first covering prefix of array A is the smallest integer P such that 0<=P<N and
such that every value that occurs in array A also occurs in sequence
A[0], A[1], ..., A[P].

For example, the first covering prefix of the following 5-element array A:
A[0] = 2
A[1] = 2
A[2] = 1
A[3] = 0
A[4] = 1

is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0],
contains all values that occur in array A.
"""


def solution(A):
    """
    >>> solution([2, 2, 1, 0, 1])
    3
    """
    tracker = dict()
    for elem in A:
        tracker[elem] = 1

    for i in range(len(A)):
        if A[i] in tracker:
            tracker.pop(A[i])
        if not tracker:
            return i

if __name__ == "__main__":
    import doctest
    doctest.testmod()
