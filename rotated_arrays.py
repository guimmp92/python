#!/usr/bin/python

"""
Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array.
Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}.
"""

from collections import deque
import time

a = [1, 2, 3, 5, 6, 7, 8]
b = [5, 6, 7, 8, 1, 2, 3]
c = [5, 6, 7, 8, 1, 1, 3]
d = [5, 6, 7, 8, 1, 1, 3, 4]

# Implementation w/ deque
def compare(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def are_rotated(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        new_b = deque(b)
        new_b.rotate(i)
        if compare(a, new_b):
            return True

    return False

start = time.time()
print are_rotated(a, b)
print are_rotated(b, a)
print are_rotated(a, c)
print are_rotated(a, d)
stop = time.time()

print "Execution time: {0}".format(str(stop-start))
print

# Implementation w/o deque (lower level)
def are_rotated2(a, b):
    start_at = []
    for idx, elem in enumerate(a):
        if elem == b[0]:
            start_at.append(idx)

    for k in range(len(start_at)):
        i, j = start_at[k], 0
        for _ in range(len(a)):
            if a[i] != b[j]:
                break;
            else:
                i, j = (i+1)%len(a), j+1
        else:  # no break
            return True

    return False

start = time.time()
print are_rotated2(a, b)
print are_rotated2(b, a)
print are_rotated2(a, c)
print are_rotated2(a, d)
stop = time.time()

print "Execution time: {0}".format(str(stop-start))
print
