#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/66/

Print out Pascal's triangle up to a certain depth.
"""
import sys


def pascal(depth):
    triangle = [[1]]
    for d in xrange(1, depth):
        row = [1]
        for i in xrange(1, len(triangle[d-1])):
            row.append(triangle[d-1][i-1] + triangle[d-1][i])
        row.append(1)
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in f:
            triangle = pascal(int(line.strip()))
            triangle = [str(elem) for row in triangle for elem in row]
            print " ".join(triangle)
