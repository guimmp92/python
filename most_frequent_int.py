#!/usr/bin/python

"""
Find the most frequent integer in an array.
"""

import random

arr = []
for i in range(50):
    arr.append(random.randint(0, 10))
print "The array: {0}".format(arr)

# Implementation with collections.Counter
from collections import Counter
counter = Counter(arr)
print "Answer w/ Counter implementation: {0}".format(counter.most_common(1))

# Implementation with dict
from collections import defaultdict
counts = defaultdict(int)
for elem in arr:
    counts[elem] += 1
most_frequent = None
for elem in counts:
    if most_frequent is None or counts[elem] > most_frequent:
        most_frequent = (elem, counts[elem])
print "Answer w/ dict implementation: {0}".format(counter.most_common(1))
