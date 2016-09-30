#!/usr/bin/python
# vim: foldlevel=0

"""
You are given a set of n types of rectangular 3-D boxes, where the i^th box has
height h(i), width w(i) and depth d(i) (all real numbers). You want to create
a stack of boxes which is as tall as possible, but you can only stack a box on
top of another box if the dimensions of the 2-D base of the lower box are each
strictly larger than those of the 2-D base of the higher box. Of course, you can
rotate a box so that any side functions as its base. It is also allowable to use
multiple instances of the same type of box.

Note: This problem is very similar to the longest increasing subsequence problem.

https://people.cs.clemson.edu/~bcdean/dp_practice/
"""
import operator


def dp(B, j, memo):
    if memo[j] == -1:
        curmax = B[j]
        for i in range(j):
           Bi = dp(B, i, memo)
           if B[j][1] < Bi[1] and B[j][2] < Bi[2] and Bi[0]+B[j][0] > curmax[0]:
                curmax = (Bi[0]+B[j][0], B[j][1], B[j][2])
        memo[j] = curmax
    return memo[j]


def solution(boxes):
    """
    Time complexity: O(n^2)
    >>> boxes = [(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]
    >>> solution(boxes)
    60
    """
    B = set()
    for h, w, d in boxes:
        B.add((h, min(d, w), max(d, w)))
        B.add((w, min(d, h), max(d, h)))
        B.add((d, min(h, w), max(h, w)))
    B = sorted(B, key=lambda x: x[1]*x[2], reverse=True)

    memo = [-1] * len(B)
    dp(B, len(B)-1, memo)
    return max(memo, key=operator.itemgetter(0))[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
