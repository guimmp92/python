#!/usr/bin/python
# vim: foldlevel=0

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
    mid = (left+right)//2
    pivot = a[mid]
    a[mid], a[right] = a[right], a[mid]
    gt_start = left  # 'greater than' start
    for i in range(left, right):
        if a[i] < pivot:
            a[gt_start], a[i] = a[i], a[gt_start]
            gt_start += 1
    a[gt_start], a[right] = a[right], a[gt_start]
    return gt_start


def quicksort(a, left, right):
    if left >= right:
        return
    pivot = partition(a, left, right)
    quicksort(a, left, pivot-1)
    quicksort(a, pivot+1, right)


quicksort(arr, 0, len(arr)-1)
print arr
