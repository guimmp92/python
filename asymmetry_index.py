#!/usr/bin/python

"""
An integer X and a non-empty zero-indexed array A consisting of N integers are given.
Split the array A into two parts, such that the number of elements equal to X in the
first part is the same as the number of elements different from X in the other part.
More formally we are looking for a number K such that:
- 0 <= K <= N and
- the number of elements equal to X in A[0..K-1] is the same as the number of elements
different from X in A[K..N-1]. For K=0, A[0..K-1] does not contain any element. For K=N,
A[K..N-1] does not contain any element.

For example, given integer X = 5 and array A [5, 5, 1, 7, 2, 3, 5], K equals to 4.

It can be shown that K always exists and is unique.

The python solution below scored 40% in accuracy and 20% in performance on codility?!

Javascript solution: http://pastebin.com/CaTZxrqK
"""


def solution(X, A):
    """
    >>> solution(5, [5, 5, 1, 7, 2, 3, 5])
    4
    >>> solution(5, [5, 1, 7, 2, 3, 5])
    4
    >>> solution(5, [1, 1, 5, 2, 3, 5])
    4
    >>> solution(3, [3, 1, 5, 2, 5])
    4
    >>> solution(3, [0, 1, 5, 2, 3])
    4
    >>> solution(3, [3])
    0
    >>> solution(5, [5, 5, 5, 5, 5, 5])
    0
    >>> solution(1, [3])
    0
    >>> solution(1, [5, 5, 5, 5, 5])
    4
    """
    N = len(A)
    i, j = 0, N-1
    count_left, count_right = 0, 0

    if A[i] == X:
        count_left += 1
    if A[j] != X:
        count_right += 1

    while i < j:
        if count_left <= count_right:
            i += 1
            if A[i] == X:
                count_left += 1
        else:
            j -= 1
            if A[j] != X:
                count_right += 1

    return j


if __name__ == "__main__":
    import doctest
    doctest.testmod()
