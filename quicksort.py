#!/usr/bin/python

"""
Quicksort.
"""

import random

arr = []
for i in range(10):
    arr.append(random.randint(0, 50))
print "The array: {0}".format(arr)


def partition(a, left, right):
    pivot = a[(left+right)//2]
    i, j = left, right
    while i < j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return i


def partition2(a, left, right):
    pivot_idx = (left+right)//2
    pivot = a[pivot_idx]
    to_copy = left
    a[pivot_idx], a[right] = a[right], a[pivot_idx]
    for i in range(left, right):
        if a[i] < pivot:
            a[to_copy], a[i] = a[i], a[to_copy]
            to_copy += 1
    a[to_copy], a[right] = a[right], a[to_copy]
    return to_copy


def quicksort(a, left, right):
    if left < right:
        idx = partition2(a, left, right)
        quicksort(a, left, idx-1)
        quicksort(a, idx+1, right)


quicksort(arr, 0, len(arr)-1)
print arr
