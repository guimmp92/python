#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/1/
"""
import sys


def fizzbuzz(x, y, n):
    """
    >>> fizzbuzz(3, 5, 10)
    ['1', '2', 'F', '4', 'B', 'F', '7', '8', 'F', 'B']
    >>> fizzbuzz(2, 7, 15)
    ['1', 'F', '3', 'F', '5', 'F', 'B', 'F', '9', 'F', '11', 'F', '13', 'FB', '15']
    """
    res = []
    for i in range(1, n+1):
        next_elem = ""
        if i % x == 0:
            next_elem += "F"
        if i % y == 0:
            next_elem += "B"
        if i % x and i % y:
            next_elem += str(i)
        res.append(next_elem)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = [int(i) for i in line.split(' ')]
            print " ".join(fizzbuzz(*line))
