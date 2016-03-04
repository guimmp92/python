#!/usr/bin/python

"""
Insertion sort
"""

from random_array import randlist

arr = randlist(50, 100)
print "The input array: {0}".format(arr)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def insertion_sort(arr):
    cur = 1
    while cur < len(arr):
        for idx, value in enumerate(reversed(arr[:cur])):
            if arr[cur-idx] < value:
                swap(arr, cur-idx-1, cur-idx)
        cur += 1

insertion_sort(arr)
print "The sorted array: {0}".format(arr)
