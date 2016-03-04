#!/usr/bin/python

"""
A zero-indexed array A consisting of N integers is given. An equilibrium index of this
array is any integer P such that 0 <= P <= N and the sum of elements of lower indices is
equal to the sum of elements of higher indices, i.e.
A[0] + A[1] + ... + A[P-1] = A[P+1] + ... + A[N-2] + A[N-1]
Sum of zero elements is assumed to be equal to 0. This can happend if P=0 or if P=N-1.

http://blog.codility.com/2011/03/solutions-for-task-equi.html
"""


def find_equi_index(A):
    """
    >>> find_equi_index([-1, 3, -4, 5, 1, -6, 2, 1])
    [1, 3, 7]
    """
    res = []
    totalsum = sum(A)
    cumsum = 0
    for i in range(len(A)):
        if cumsum == totalsum - cumsum - A[i]:
            res.append(i)
        cumsum += A[i]
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
