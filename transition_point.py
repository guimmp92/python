#!/usr/bin/python

"""
Algorithm Design Manual p134
"""

def find_transition_point(arr, left, right):
    if left > right:
        return
    mid = (left+right)//2
    if arr[mid-1] == '0' and arr[mid] == '1':
        return mid
    if arr[mid] == '0' and arr[mid+1] == '1':
        return mid+1
    if arr[mid] == '0':
        return find_transition_point(arr, mid+1, right)
    if arr[mid] == '1':
        return find_transition_point(arr, left, mid-1)

a = '000000000000001111111'
print find_transition_point(a, 0, len(a)-1)
