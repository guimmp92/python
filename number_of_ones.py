#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/16/

Write a program which determines the number of 1 bits in the internal representation of
a given integer.
"""
import sys


def number_of_ones(x):
    """
    >>> number_of_ones(-39)
    4
    >>> number_of_ones(10)
    2
    >>> number_of_ones(22)
    3
    >>> number_of_ones(56)
    3
    """
    count = 0
    while x != 0:
        count += x & 1
        q, r = divmod(x, 2)  # equivalent to x >> 1
        if x < 0:
            x = q + 1
        else:
            x = q
    return count


def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print number_of_ones(int(line.strip()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
