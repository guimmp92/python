#!/usr/bin/python

"""
Selection sort: Repeatedly identify the smallest remaining unsorted element and put it
at the end of the sorted portion of the array.
"""

from random_array import randlist


arr = randlist(50, 100)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def selection_sort(arr):
    cur = 0
    while cur < len(arr):
        minimum = cur
        for idx, value in enumerate(arr[cur+1:]):
            if value < arr[minimum]:
                minimum = cur + idx + 1
        swap(arr, cur, minimum)
        cur += 1

selection_sort(arr)
print arr
