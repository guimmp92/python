#!/usr/bin/python

"""
In base -2, integers are represented in sequences of bits in the following way. Bits are
ordered from the least to the most significant. Sequence B of N bits represents the
number: sum{ B[i]*(-2)^i for i = 0..N-1 }. The empty sequence represents 0.

Note that such a representation is suitable for both positive and negative integers.

For example, given A = [1, 0, 0, 1, 1] (X=9), the solution should return [1, 1, 0, 1]
(-X=-9). Given A = [1, 0, 0, 1, 1, 1] (X=-23), the solution should return
[1, 1, 0, 1, 0, 1, 1] (-X=23).

References:
* https://en.wikipedia.org/wiki/Negative_base
* http://stackoverflow.com/questions/19517868/integer-division-by-negative-number
* http://stackoverflow.com/questions/15633787/truncated-versus-floored-division-in-python
* http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html

<quote>
For negative b, by the way, everything just flips, and the invariant becomes:
0 >= r > b.
</quote>
"""


from math import floor


def _quotient(dividend, remainder):
    return (dividend - remainder) // -2.


def initial_solution(A):
    """
    >>> solution([1, 0, 0, 1, 1])
    [1, 1, 0, 1]
    >>> solution([1, 0, 0, 1, 1, 1])
    [1, 1, 0, 1, 0, 1, 1]
    """
    res = []
    num = 0
    for i in range(len(A)):
        num += A[i]*pow(-2, i)

    num *= -1
    while num != 0:
        q = _quotient(num, 0)
        if floor(q) == q:
            res.append(0)
        else:
            q = _quotient(num, 1)
            res.append(1)
        num = q

    return res


def solution(A):
    """
    >>> solution([1, 0, 0, 1, 1])
    [1, 1, 0, 1]
    >>> solution([1, 0, 0, 1, 1, 1])
    [1, 1, 0, 1, 0, 1, 1]
    """
    res = []
    num = 0
    for i in range(len(A)):
        num += A[i]*pow(-2, i)

    num *= -1
    while num != 0:
        q, r = divmod(num, -2)
        if r < 0:
            q, r = q+1, r+2  # add 1 and (base) 2 to quotient and remainder, resp.
        res.append(r)
        num = q

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
