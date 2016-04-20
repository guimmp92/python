#!/usr/bin/python

"""
Given two integers x and y, return x / y without using the '/' or '*' operators.
"""


def divide(a, b):
    """
    Recursive, most efficient.

    >>> divide(5, 4)
    1
    >>> divide(7, 2)
    3
    >>> divide(1, 3)
    0
    >>> divide(9, 3)
    3
    >>> divide(9, 0)
    -1
    """
    if b == 0:
        return -1
    if a < b:
        return 0

    q, div = 1, b
    while div < a:
        div <<= 1
        q <<= 1

    if div > a:
        div >>= 1
        q >>= 1
        q += divide(a - div, b)

    return q


def multiply(a, b):
    num = 0
    for i in range(b):
        num += a
    return num


def divide1(a, b):
    """
    Slightly more efficient.

    >>> divide1(5, 4)
    1
    >>> divide1(7, 2)
    3
    >>> divide1(1, 3)
    0
    >>> divide1(9, 3)
    3
    """
    q = a
    while True:
        q >>= 1
        num = multiply(q, b)
        if num <= a:
            if a - b < num:
                return q
            if num <= a - b:
                while num <= a - b:
                    q += 1
                    num = multiply(q, b)
                return q


def divide2(a, b):
    """
    Inefficient.

    >>> divide2(5, 4)
    1
    >>> divide2(7, 2)
    3
    >>> divide2(1, 3)
    0
    >>> divide2(9, 3)
    3
    """
    sum, count = 0, 0
    while sum <= a - b:
        sum = sum + b
        count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
