#!/usr/bin/python

"""
http://www.toptal.com/python/interview-questions
"""

import random

arr = []
for i in range(10):
    arr.append(random.randint(0, 10))
print "The array: {0}".format(arr)


def is_even(num):
    return num % 2 == 0


def even_numbers(l):
    return [num for idx, num in enumerate(l) if is_even(idx) and is_even(num)]


def even_numbers2(l):
    return [num for num in l[::2] if is_even(num)]


print even_numbers(arr)
print even_numbers2(arr)
