#!/usr/bin/python

"""
https://www.codeeval.com/open_challenges/89/

By starting at the top of the triangle and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 27.
5
9 6
4 6 8
0 7 1 5
"""
import sys


def main():
    with open(sys.argv[1], 'r') as f:
        triangle = [[int(i) for i in l.strip().split()] for l in f.read().splitlines()]
        # Traverse the triangle bottom up as opposed to top down.
        for row in xrange(len(triangle)-2, -1, -1):
            # For each element, we add the max of the two adjacent elements below.
            for i in xrange(len(triangle[row])):
                triangle[row][i] += max(triangle[row+1][i], triangle[row+1][i+1])

    # The root now contains the max.
    return triangle[0][0]


if __name__ == "__main__":
    print main()
