#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/18/

Given numbers x and n, where n is a power of 2, print out the smallest multiple of n
which is greater than or equal to x. Do not use division or modulo operator.
"""
import sys


def multiples_gen(n):
    seed = n
    while True:
        yield n
        n += seed


def solution(x, n):
    """
    >>> solution(13, 8)
    16
    >>> solution(17, 16)
    32
    """
    for m in multiples_gen(n):
        if m >= x:
            return m


def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = [int(i) for i in line.split(',')]
            print solution(*line)


if __name__ == "__main__":
    main()
