#!/usr/bin/python

"""
Given a sorted array of integers, return the index of the given element.
ihttp://codekata.com/kata/kata02-karate-chop/
"""

import random
import sys

arr = []
for i in range(20):
    arr.append(random.randint(0, 100))
arr = sorted(arr)
print "The array: {0}".format(arr)

print "Enter int to search for:"
key = int(raw_input())


def chop1(key, arr):
    low, high = 0, len(arr)
    while (low <= high):
        mid = (high+low)//2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

print chop1(key, arr)


def binsearch_recursive(key, arr, low, high):
    if low > high:
        return
    mid = (low+high)//2
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        return binsearch_recursive(key, arr, mid+1, high)
    else:
        return binsearch_recursive(key, arr, low, mid-1)


def chop2(key, arr):
    return binsearch_recursive(key, arr, 0, len(arr))

print chop2(key, arr)


def chop3(key, arr):
    low, high = 0, len(arr)
    # Reduce search space until high and low are two consecutive elements
    while (high - low > 1):
        mid = (low+high)//2
        if arr[mid] <= key:
            low = mid
        else:
            high = mid
    if arr[low] == key:
        return low

print chop3(key, arr)
